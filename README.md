# Experimenting with TransFuser: A imitation with Transformer-Based Sensor Fusion for Autonomous Driving
This is done for the fulfillment of requirements for CSI6900 Spring 2023 at University of Ottawa. 

<img src="figures/demo.gif">




## Setup

Clone the repo, setup CARLA 0.9.10.1, and build the conda environment:

```Shell
git clone https://github.com/ashishgeorge009/CSI6900transfuser.git
cd CSI6900transfuser
git checkout ashishBranch
chmod +x setup_carla.sh
./setup_carla.sh
conda env create -f environment.yml
conda activate tfuse
pip install torch torchvision --pre -f https://download.pytorch.org/whl/nightly/cu121/torch_nightly.html
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
pip install torch-scatter -f https://data.pyg.org/whl/torch1.13.1+cu117.html
pip install mmcv-full==1.7.1 -f https://download.openmmlab.com/mmcv/dist/cu117/torch1.13/index.html
```


### Pretrained Model
Pre-trained agent files for all 4 methods can be downloaded from [AWS](https://s3.eu-central-1.amazonaws.com/avg-projects/transfuser/models_2022.zip):

```Shell
mkdir model_ckpt
wget https://s3.eu-central-1.amazonaws.com/avg-projects/transfuser/models_2022.zip -P model_ckpt
unzip model_ckpt/models_2022.zip -d model_ckpt/
rm model_ckpt/models_2022.zip
```

### Running the evaluations
To evaluate a model, we first launch a CARLA server:

```Shell
./CarlaUE4.sh --world-port=2000 
```

Once the CARLA server is running, evaluate an agent with the script:

PS: Before RUNNING this make sure the `CARLA_ROOT`, `WORK_DIR` are correct in `my_evaluation.sh`. Also make sure the file path to `ROUTES`(contains test cases) and `CHECKPOINT_ENDPOINT` (contains the result csv file) is also correct in `my_evaluation.sh` file.
 
```Shell
./leaderboard/scripts/my_evaluation.sh
```
The simulation will run and you can fins your results in the results file that was mentioned in `CHECKPOINT_ENDPOINT`
