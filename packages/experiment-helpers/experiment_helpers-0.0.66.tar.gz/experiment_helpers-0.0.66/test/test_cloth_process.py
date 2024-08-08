import os
import sys
sys.path.append('/home/jlb638/Desktop/package')
import torch
from PIL import Image
from datasets import load_dataset

from src.experiment_helpers.cloth_process import check_or_download_model,load_seg_model,get_palette,generate_mask


checkpoint="/scratch/jlb638/fashion_segmentation/cloth_segm.pth"

check_or_download_model(checkpoint)

device="cpu"

palette=get_palette(4)

net = load_seg_model(checkpoint, device=device)
for row in load_dataset("jlbaker361/humans",split="train"):
    image=row["splash"] #Image.open("ArcaneJinx.jpg").convert("RGB")
    cloth_seg = generate_mask(image, net=net, palette=palette, device=device)
    break
    #cloth_seg.save("masked_jinx.jpg")