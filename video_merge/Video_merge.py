#!/usr/bin/env python
# coding: utf-8

from moviepy.editor import *
import glob
import argparse

parser = argparse.ArgumentParser(description='merge video files') 
parser.add_argument('--foldername', default='input_video/')
parser.add_argument('--output_filename', default='output_video/video_merged.mp4')
args = parser.parse_args() 

folder_path=args.foldername
save_path = args.output_filename
file_paths=glob.glob(folder_path+"*")

for i, file_path in enumerate(file_paths):
    tmp = VideoFileClip(file_path)
    if i==0:
        final_clip = tmp
    else:
        final_clip = concatenate_videoclips([final_clip, tmp])

final_clip.write_videofile(save_path)