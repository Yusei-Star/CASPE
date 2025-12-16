import os
import glob
import h5py
import numpy as np
from torch.utils.data import Dataset

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"


def load_data(datadir):
    all_data = []
    all_label = []
    for h5_name in glob.glob(os.path.join(datadir, "*.h5")):
        # print(f"h5_name: {h5_name}")
        f = h5py.File(h5_name, "r")
        data = f["data"][()].astype("float32")
        label = f["label"][()].astype("int64")
        f.close()
        all_data.append(data)
        all_label.append(label)
    all_data = np.concatenate(all_data, axis=0)
    all_label = np.concatenate(all_label, axis=0)
    return all_data, all_label
    

def translate_pointcloud(pointcloud):
    xyz1 = np.random.uniform(low=8.0 / 9.0, high=9.0 / 8.0, size=[4])
    xyz2 = np.random.uniform(low=-0.1, high=0.1, size=[4])

    translated_pointcloud = np.add(np.multiply(pointcloud, xyz1), xyz2).astype(
        "float32"
    )
    return translated_pointcloud


def get_file_paths(datadir, file_type):

    h5_file_paths = []
    name_list = []
    search_path = os.path.join(datadir, f"*.{file_type}")

    for file_path in glob.glob(search_path):
        h5_file_paths.append(file_path)
        file_name = os.path.basename(file_path)
        name_list.append( file_name[:-3])

    return h5_file_paths, name_list


class ptData(Dataset):
    def __init__(self, datadir, partition="train", max_trans_ratio=0.75):
        self.partition = partition
        self.trans_ratio = max_trans_ratio
        self.dirlen = len(datadir)
        if self.partition == "pred":
            self.file_paths, self.name_list = get_file_paths(datadir, "h5")
        else:
            self.data, self.label = load_data(datadir)

    def __getitem__(self, item):
        
        if self.partition == "pred":
            file = h5py.File(self.file_paths[item], "r")
            label = file["label"][()].astype("int64")
            data = file["data"][()].astype("float32")
            name = self.name_list[item]     
            return data, label, name
        else:
            data = self.data[item]
            label = self.label[item]
            if self.partition == "train" and np.random.rand() > self.trans_ratio: 
                data = translate_pointcloud(data)
                np.random.shuffle(data)
            return data, label   

    def __len__(self):
            if self.partition == "pred":
                return len(self.file_paths)
            else:
                return len(self.data)


if __name__ == "__main__":

    from torch.utils.data import DataLoader
    
    # train_loader = DataLoader(ptData("apcnet/data/train",partition='train'), num_workers=4,
    #                           batch_size=16, shuffle=True, drop_last=True)
    # for batch_idx, (data, label) in enumerate(train_loader):
    #     print(f"batch_idx: {batch_idx}  | data shape: {data.shape} | ;lable shape: {label.shape}")
    
    train_loader = DataLoader(ptData("resources/dataset/data_for_APCNet/pred",partition='pred'), num_workers=4,
                              batch_size=16, shuffle=True, drop_last=True)
    for batch_idx, (data, label, name) in enumerate(train_loader):
        print(f"batch_idx: {batch_idx}  | data shape: {data.shape} | ;lable shape: {label.shape} | name shape: {len(name)}")
