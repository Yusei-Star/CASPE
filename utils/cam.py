import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class ActivationsAndGradients:
    """Class for extracting activations and
    registering gradients from targeted intermediate layers"""

    def __init__(self, model, target_layers, reshape_transform):
        self.model = model
        self.gradients = []
        self.activations = []
        self.reshape_transform = reshape_transform
        self.handles = []
        for target_layer in target_layers:
            self.handles.append(
                target_layer.register_forward_hook(self.save_activation)
            )
            # Backward compatibility with older pytorch versions:
            if hasattr(target_layer, "register_full_backward_hook"):
                self.handles.append(
                    target_layer.register_full_backward_hook(self.save_gradient)
                )
            else:
                self.handles.append(
                    target_layer.register_backward_hook(self.save_gradient)
                )

    def save_activation(self, module, input, output):
        activation = output
        if self.reshape_transform is not None:
            activation = self.reshape_transform(activation)
        self.activations.append(activation.cpu().detach())

    def save_gradient(self, module, grad_input, grad_output):
        # Gradients are computed in reverse order
        grad = grad_output[0]
        if self.reshape_transform is not None:
            grad = self.reshape_transform(grad)
        self.gradients = [grad.cpu().detach()] + self.gradients

    def __call__(self, x):
        self.gradients = []
        self.activations = []
        return self.model(x)

    def release(self):
        for handle in self.handles:
            handle.remove()


class GradCAM:
    def __init__(self, model, target_layers, reshape_transform=None, use_cuda=False):
        self.model = model.eval()
        self.target_layers = target_layers
        self.reshape_transform = reshape_transform
        self.cuda = use_cuda
        if self.cuda:
            self.model = model.cuda()
        self.activations_and_grads = ActivationsAndGradients(
            self.model, target_layers, reshape_transform
        )

    """ Get a vector of weights for every channel in the target layer.
        Methods that return weights channels,
        will typically need to only implement this function. """

    @staticmethod
    def get_cam_weights(grads):
        return np.mean(grads, axis=(2, 3), keepdims=True)

    @staticmethod
    def get_loss(output, target_category):
        loss = 0
        for i in range(len(target_category)):
            loss = loss + output["logits"][i, target_category[i]]
        return loss

    def get_cam_image(self, activations, grads):
        weights = self.get_cam_weights(grads)
        weighted_activations = weights * activations
        cam = weighted_activations.sum(axis=1)

    # caculate with final_layer_norm
    def get_cam_fasta(self, activations_list, grads_list):
        arr1_trans = np.transpose(activations_list, (1, 0, 2))
        arr2_trans = np.transpose(grads_list, (1, 0, 2))
        activate = np.mean(arr1_trans, axis=2, keepdims=True)
        grad = np.mean(arr2_trans, axis=2, keepdims=True)
        cam = activate * grad
        return cam

    # caculate with ConvBnRule
    def get_cam_conv_layer(self, activation, grad, cam_width):
        arr1_trans = np.transpose(activation, (0, 2, 1))
        arr2_trans = np.transpose(grad, (0, 2, 1))
        activate = np.mean(arr1_trans, axis=2, keepdims=True)
        grad = np.mean(arr2_trans, axis=2, keepdims=True)
        cam = activate * grad
        return cam[:, :cam_width, :]

    @staticmethod
    def get_target_width_height(input_tensor):
        width, height = input_tensor.size(-1), input_tensor.size(-2)
        return width, height

    def compute_cam_per_layer(self, input_tensor):
        activations_list = [
            a.cpu().data.numpy() for a in self.activations_and_grads.activations
        ]
        grads_list = [
            g.cpu().data.numpy() for g in self.activations_and_grads.gradients
        ]
        width, height = self.get_target_width_height(input_tensor)

        cam_per_target_layer = []
        # Loop over the saliency image from every layer

        for layer_activations, layer_grads in zip(activations_list, grads_list):
            cam = self.get_cam_conv_layer(layer_activations, layer_grads, width)
            cam = np.maximum(cam, 0)
            cam_per_target_layer.append(cam)
            # print(cam_per_target_layer)

        return cam_per_target_layer

    def __call__(self, input_tensor, target_category=None):

        if self.cuda:
            input_tensor = input_tensor.cuda()

        # 正向传播得到网络输出logits(未经过softmax)
        output = self.activations_and_grads(input_tensor)
        if isinstance(target_category, int):
            target_category = [target_category] * input_tensor.size(0)

        if target_category is None:
            target_category = np.argmax(output["logits"].cpu().data.numpy(), axis=-1)
            # print(f"category id: {target_category}")
        else:
            assert len(target_category) == input_tensor.size(0)

        self.model.zero_grad()
        loss = self.get_loss(output, target_category)
        loss.backward(retain_graph=True)

        # In most of the saliency attribution papers, the saliency is
        # computed with a single target layer.
        # Commonly it is the last convolutional layer.
        # Here we support passing a list with multiple target layers.
        # It will compute the saliency image for every image,
        # and then aggregate them (with a default mean aggregation).
        # This gives you more flexibility in case you just want to
        # use all conv layers for example, all Batchnorm layers,
        # or something else.
        cam_per_layer = self.compute_cam_per_layer(input_tensor)

        # attn: B x L x T x T
        attn = np.mean(output["attentions"].cpu().data.numpy(), axis=2)
        return cam_per_layer, attn

    def __del__(self):
        self.activations_and_grads.release()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.activations_and_grads.release()
        if isinstance(exc_value, IndexError):
            # Handle IndexError here...
            print(
                f"An exception occurred in CAM with block: {exc_type}. Message: {exc_value}"
            )
            return True


def solve_singular_matrix(matrix, b):
    try:
        x = np.linalg.inv(matrix) @ b
    except np.linalg.LinAlgError:
        x = np.linalg.pinv(matrix) @ b

    return x
