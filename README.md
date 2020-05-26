###CIS581: Computer Vision and Computational Photography
###Project 2: Image Morphing
##Name: Tejas Srivastava tjss@seas.upenn.edu  14547354

The objective of the project was to understand and implement image morphing in Python, thus producing a morph animation of our face into another person's face.

##File structure
-click_correspondences.py
-cpselect.py
both these files are used to select the strong matching points in both the images and store the co-ordinates of those points in files im1_cor_text.txt and im2_cor_text.txt.
-morph_tri.py
used to generate the morphed image frames using triangulation, warping and dissolving. (in barycentric coordinates).
-run.py
used to run the code.
to change the images, change their names in line 10 and line 11 of run.py
number of frames generated can also be changed in line 19 of run.py
both avi and gif is created for each morph (outputMorphing.avi and output.gif). These filenames can be changed in line 32 and line 49 of run.py
-image input filenames
  -beard1.jpg
  -beard2.jpg

  -elonTejas1.jpg
  -elonTejas2.jpg

  -tsms1.jpg
  -tsms2.jpg

-output Files for corresponding inputs
  -output_beard.gif
  -output_beard.AVI

  -output_elonTejas.gif
  -output_elonTejas.AVI

  -output_tsms.gif
  -output_tsms.AVI

##Running the code
-Simply use 'python3 run.py' for running the code.
-Please make sure the required dependencies are installed.
-To change the images, change their names in line 10 and line 11 of run.py
-Number of frames generated can also be changed in line 19 of run.py
-Both avi and gif is created for each morph (outputMorphing.avi and output.gif).
-These filenames can be changed in line 32 and line 49 of run.py
