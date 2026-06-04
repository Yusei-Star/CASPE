# CASPE

## Overview

The relationship between protein sequence and its properties remains unknown.We developed CASPE (Critical Amino acids Streamline Protein Evolution), a platform adopting Grad-CAM for interpretability and Point Cloud for efficiency, to identify critical residues related to protein properties.

![CASPE_framework](images/README/CASPE_framework.png)

## Installation

### Environment Setup

**Option 1: Using conda (Recommended)**

```bash
conda env create -f CASPE.yaml
```

**The command above is used to install the code runtime environment. It takes about 8 minutes (depending on network speed).

**Option 2：Or you can download the environment tar (CASPE_env.tar.gz) and create the environment manually. (https://zenodo.org/records/17982688)**

```
cd /anaconda3/envs
mkdir CASPE
tar -xzvf CASPE_env.tar.gz -C /anaconda3/envs/CASPE
```

### Dependencies

Core requirements:

* Python 3.10
* PyTorch 2.4.1
* Biopython
* Ubuntu 22.04.5 LTS
* RTX 4090

### Using Pre-trained Models

## Quick Start

### For locating critical residues

bash

CASPE can locate the critical amino acid sites in a protein sequence that are most relevant to thermostability or pH tolerance. When you use this function, you need to download the corresponding models and adjust the parameters in the code according to different requirements at the same time. CASPETs are for locating the critical residues about thermostability and CASPEA is for pH tolerance.

**Download the weight file from the website, and extract it, place it in the "resources/checkpoints/" folder.

#### **Checkpoints based on CAS**


| Model file name                       | Description                                            | Download Link                           |
| ------------------------------------- | ------------------------------------------------------ | --------------------------------------- |
| CASPET_model_1.zip                    | CASPET-1: Model related to thermostability (dataset1) | [https://zenodo.org/records/20523796]() |
| CASPET_model_2.zip<br />(Recommended) | CASPET-2: Model related to thermostability (dataset2) | [https://zenodo.org/records/20523796]() |
| CASPET_model_3.zip                    | CASPET-3: Model related to thermostability (dataset3) | [https://zenodo.org/records/20523796]() |
| CASPET_model_4.zip                    | CASPET-4: Model related to thermostability (dataset4) | [https://zenodo.org/records/20523796]() |
| CASPEA_model.zip                      | CASPEA: Model related to pH tolerance                  | [https://zenodo.org/records/20523796]() |

**For example: Download the file "CASPET_model_1.zip" and extract it. Then, place the extracted files into folder "resources/checkpoints/CASPET-1"

├── CASPET-1
│   ├── 20-25_50-55_70-80_transformer.txt
│   └── best_checkpoint.pth
├── CASPET-3
│   ├── best_checkpoint.pth
│   └── less_20_38-45_65-70_transformer_new.txt
└── CASPET-4
     ├── 26_45-50_60-65_transformer.txt
     └── best_checkpoint.pth

#### Locating critical residues

```
python run_get_site.py -c resources/checkpoint -m CASPET-2 -n 5 -i resources/dataset/data_for_CAS/locate.txt -o output/test_CAS_value.json
```

**The command above is used to locate critical sites on three sequences. It takes about 10 seconds to run on an rtx4090

#### Predict the most optimal amino acids

You can also predict the most optimal amino acids based on the current microenvironment.

Firstly, you need to generate microenvironment data for the critical sites based on the sites information of sequence and the PQR file.

```
python run_generate_point_cloud.py -i resources/dataset/data_for_Micro_Env/pred/pqr -j output/test_CAS_value.json -o resources/dataset/data_for_APCNet
```

**The command above is used to generate 45 microenvironment datas. It takes about 3 seconds to run on an rtx4090.

Sencondly, predict the most optimal amino acids based on the current microenvironment.

```
python run_predict_res.py -c resources/checkpoint -m APCNetT -i resources/dataset/data_for_APCNet/pred -o output/aa_pred.csv
```

**The command above is used to predict the most suitable amino acids. It takes about 3 seconds to run on an rtx4090.

#### APCNet models


| Model file name | Description                               | Download Link                           |
| --------------- | ----------------------------------------- | --------------------------------------- |
| APCNetT.zip     | APCNetT: APCNet for thermostability      | [https://zenodo.org/records/20523796]() |
| APCNetAA.zip    | APCNetAA: APCNet for acid-tolerance      | [https://zenodo.org/records/20523796]() |
| APCNetAL.zip    | APCNetAL: APCNet for alkaline-tolerance | [https://zenodo.org/records/20523796]() |

## Reproduction Guide for results in paper

This section provides a step-by-step guide for reviewers to reproduce the initial experimental results and validate the global feasibility of the CASPE framework.

### Fig.2 in mainbody

Before running the reproduction script, please download the specific initial model (CASPET and APCNet-1st: [https://zenodo.org/records/20523796](https://))

1、Note: Each sequence should be run four times to obtain four results based on the CASPET, and then all the results should be summarized.

```
python run_get_site.py -c resources/checkpoint -m CASPET-1 -n 5 -i resources/dataset/data_for_CAS/BG_EG_CBHI_seq.txt -o output/BG_EG_CBHI_CAS_value_1.json
```



2、Note: This dataset is specifically curated and filtered to adapt to the initial model architecture, with point cloud sizes strictly ranging from **512 to 1536**. The JSON files obtained in the previous step all need to be converted into micro-environments and placed in the same folder, or download from [https://zenodo.org/records/20523796]() (data_for_APCNet_BG_EG_CBHI.zip)

```
python run_generate_point_cloud.py -i resources/dataset/data_for_Micro_Env/BG_EG_CBHI -j output/BG_EG_CBHI_CAS_value_1.json -n 512 -x 1536 -o resources/dataset/data_for_APCNet_BG_EG_CBHI
```



3、Note: The original evaluation and baseline validation presented in the manuscript were executed based on the final optimized state of the first-stage training (`last_checkpoint`)

**Please download APCNet-1st.zip([https://zenodo.org/records/20523796](https://)), extract it, and move it to "resources/checkpoints".

├── APCNetT-1st
     ├── args.txt
     ├── best_checkpoint.pth
     ├── last_checkpoint.pth
     ├── log.txt
     └── out.txt

```
python run_predict_res.py -c resources/checkpoint -m APCNetT-1st -w last -i resources/dataset/data_for_APCNet_BG_EG_CBHI/pred -o output/BG_EG_CBHI_pred_1st.csv
```

## Details for use

### Data Preparation for fine-tuning ESM2

We get the target sequences from dataset, and the sequence related to thermostability or pH tolerance (data_CAS_train.tar.gz) could be regarded as the input of ESM2, download the pretrained- model from https://github.com/facebookresearch/esm

### ESM2 fine-tuning for classfication

```
Waiting for update

```

### For locating critical residues

See at Quick Start

### Generate microenvironment

Get pdb files from AlphaFold (https://alphafold.com/), Get the microenvironment, the data_type is 'train/val', and you can get the pqr_site_file by locating critical residues or generating according to your knowledge.

The examples (point_cloud_for_train.tar.gz) could be downloaded from https://zenodo.org/records/17982688.

Before generating point cloud, we get pqr file from pdb file by PDB2PQR (https://pdb2pqr.readthedocs.io/en/latest/getting.html)

```
Waiting for update
```

### APCNet Training

After getting the h5 in the last step, we can train APCNet here. The examples (data_for_APCNet.tar.gz) could be downloaded from https://zenodo.org/records/17982688.

```
Waiting for update
```

## Citation

If you find the models useful in your research, we ask that you cite the relevant paper:

```
@article{author2025caspe,
  author={},
  title={},
  year={},
  doi={},
  url={},
  journal={}
}
```

## Acknowledgment

* [facebookresearch/esm: Evolutionary Scale Modeling (esm): Pretrained language models for proteins](https://github.com/facebookresearch/esm)
* [ma-xu/pointMLP-pytorch: [ICLR 2022 poster] Official PyTorch implementation of &#34;Rethinking Network Design and Local Geometry in Point Cloud: A Simple Residual MLP Framework&#34;](https://github.com/ma-xu/pointMLP-pytorch)
* [jacobgil/pytorch-grad-cam: Advanced AI Explainability for computer vision. Support for CNNs, Vision Transformers, Classification, Object detection, Segmentation, Image similarity and more.](https://github.com/jacobgil/pytorch-grad-cam)

## License

This project is licensed under the Apache 2.0 License - see the LICENSE  file for details.
