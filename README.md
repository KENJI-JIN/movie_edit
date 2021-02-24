# movie_edit
the repository to edit movie  
At first, a source code merging videos is uploaded.

# Prerequests
moviepy  
how to insatall moviepy(https://zulko.github.io/moviepy/install.html)

# Usage
At first, please prepare video files in `input_video` folder.  
*video files must be same size.  
Next, please name the files with a number and an underscore at the beginning as follows.  
The videos are merged in the order of the numbers.  
`1_`videofilename  
`2_`videofilename  
...


Finally please type the command as follows  
`cd movie_edit`  
`python video_merge.py`  

The movie merged(default:`video_merged.mp4`) will be made in `output_video` folder. 
You can specify the folder to save oputput file to use `--foldername`, and the name of output file to use `--output_filename`.
