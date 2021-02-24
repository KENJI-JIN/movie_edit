# movie_edit
the repository to edit movie

# Prerequests
moviepy
https://zulko.github.io/moviepy/install.html

# Usage
At first, please prepare video files in one folder.  
*video files must be same size.  
Next, please name the files with a number and an underscore at the beginning as follows.  
`1_`videofilename  
`2_`videofilename  
...


Finally please type the command as follows
`python video_merge.py --foldername "your folder name"`

The movie merged(default:`video_merged.mp4`) will be made in the same folder. 

You can specify the name of output file to use --output_filename.
