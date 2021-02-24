# movie_edit
The repository to edit movies.  
At first, a python code merging videos is uploaded.

# Prerequests
moviepy  
how to insatall moviepy(https://zulko.github.io/moviepy/install.html)

# Usage
1. Type commands as follows to make folders needed.  
`cd movie_edit-main/video_merge`  
`python prepare.py`

2. Prepare video files in `input_video` folder.  
*Video files must be same size.  

3. Name the files with a number and an underscore at the beginning as follows.  
The videos are merged in the order of the numbers.  
`1_`videofilename  
`2_`videofilename  
...

4. Type the command as follows  
`python video_merge.py`  

The movie merged(default:`video_merged.mp4`) will be made in `output_video` folder. 
You can specify the folder which contains input files to use `--foldername`, and the name of output file to use `--output_filename`.
