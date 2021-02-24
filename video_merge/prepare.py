import os

input_folder = "input_video"
output_folder = "output_video"
if not os.path.exists(input_folder):
    os.mkdir(input_folder)
if not os.path.exists(output_folder):
    os.mkdir(output_folder)