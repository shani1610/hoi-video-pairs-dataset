# Human-Object Interaction Video Pairs 

this repository provides the code for creating Human-Object Interaction Video pairs, 
when for each video contains human-object interaction we have a corresponding video where the object has been removed, using inpainting method, 
in this case, i use ProPainter. 
these pairs of video can be used for various tasks, I will add later on my usage as example. 
I encourage other researchers to use these pairs of videos. 
the dataset I used is InterCap. the dataset contains videos of humans interacting with everyday objects like: skateboard, umbrella, suitcase, and various interaction with the same object for example: lifting a suitcase, dragging a suitcase. 
the dataset inludes interactions with soccer ball, suitcase, toolbox, tennis racquet, chair (move, pick up, sit), umbrella, cup, skateboard, bottle. 


then run to get the videos and object masks (there is a default input path, output path and resize factor but these can be changed). 
ProPainter required the video and the mask of the object to be removed, 
the mask can be obtained using methods like XMEM, but luckely Intercap provided also the object mask so it was ideal choice for this task. 

# Examples

## Umbrella 



https://github.com/user-attachments/assets/e731a3b4-f20d-4b6e-8fed-c7df7677ef3d



https://github.com/user-attachments/assets/81a5f268-8377-4c23-ba82-f6e6314ad813

## chair

https://github.com/user-attachments/assets/94f55094-43e9-47df-bca7-55bdc2a1ad4d


https://github.com/user-attachments/assets/89d44093-38d7-4314-908c-565f6c92cc3e

## ball

https://github.com/user-attachments/assets/2a91a1e4-cca7-4e3c-908c-99586b0b0c22


https://github.com/user-attachments/assets/ee541bee-acf0-40b2-bfaf-79d484d512b0

## racket

https://github.com/user-attachments/assets/f25b5fde-1458-4dcb-8815-bbcaf7648cd8


https://github.com/user-attachments/assets/939e502e-c477-43dc-8acb-a86979f43f22

# Installation

register and download the data from [here](https://intercap.is.tue.mpg.de/)
the dataset extract into the data folder of the repository. 

I am using python 3.8.19, CUDA 11.2

```
conda create -n hoi-env python=3.8 
conda activate hoi-env
```
requirement file contains the requirments for ProPainter:
```pip install -r requirements.txt```

the corresponding PyTorch for me is 
```
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
```
please pay attention to the CUDA version, we need the Pytorch corresponding to `nvcc --version` and not the driver's one `nvidia smi`

### ProPainter:

the inpainting is being done using (ProPainter)[https://github.com/sczhou/ProPainter], for object removal ProPainter requires the frames and the masks of the object to be removed. 

please clone the repository and replace the inference_propainter.py with inference_propainter_my.py 

## inpainting

```
cd ProPainter/
```

```
python inference_propainter.py -i "./../data/images_for_ppainter/Date01_Sub01_backpack_back/Date01_Sub01_backpack_back" -m "./../data/images_for_ppainter/Date01_Sub01_backpack_back/Date01_Sub01_backpack_back_mask_resized" -o "./../data/hoi_dataset/Date01_Sub01_backpack_back" --name_of_subject "Date01_Sub01_backpack_back" --save_frames_behave
```

or just run the 

```
python ./sample/intercap4propainter.py
```

then run the script ```./scripts/ppainter_inference.sh```

if you make any changes run before that: ```chmod +x ./scripts/ppainter_inference.sh```

# Acknowledgements

For the tree i used:
(https://tree.nathanfriend.io/)[https://tree.nathanfriend.io/]


