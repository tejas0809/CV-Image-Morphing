'''
  File name: click_correspondences.py
  Author:
  Date created:
'''
import numpy as np
import matplotlib.pyplot as plt
from cpselect import cpselect
from PIL import Image
'''
  File clarification:
    Click correspondences between two images
    - Input im1: target image
    - Input im2: source image
    - Output im1_pts: correspondences coordiantes in the target image
    - Output im2_pts: correspondences coordiantes in the source image
'''

def click_correspondences(im1, im2):
  '''
    Tips:
      - use 'matplotlib.pyplot.subplot' to create a figure that shows the source and target image together
      - add arguments in the 'imshow' function for better image view
      - use function 'ginput' and click correspondences in two images in turn
      - please check the 'ginput' function documentation carefully
        + determine the number of correspondences by yourself which is the argument of 'ginput' function
        + when using ginput, left click represents selection, right click represents removing the last click
        + click points in two images in turn and once you finish it, the function is supposed to
          return a NumPy array contains correspondences position in two images
  '''

  # TODO: Your code here

  im1_pts, im2_pts = cpselect(im1,im2)
  im_FramePts=np.array([[0,0],[0,im1.shape[0]-1],[im1.shape[1]-1,0],[im1.shape[1]-1,im1.shape[0]-1],[0,int(im1.shape[0]/2)],[int(im1.shape[1]/2),0],[int(im1.shape[1]/2),im1.shape[0]-1],[im1.shape[1]-1,int(im1.shape[0]/2)]])
  im1_pts=np.append(im1_pts,im_FramePts,0)
  im2_pts=np.append(im2_pts,im_FramePts,0)
  # print(im1_pts.shape)
  return im1_pts, im2_pts


if __name__ == "__main__":

    # import time
    firstImage = np.array(Image.open('1.jpg').convert('RGB'))
    secondImage = np.array(Image.open('2.jpg').convert('RGB'))
    print(firstImage.shape)
    print(secondImage.shape)
    fig= plt.figure(dpi=200)
    fig.add_subplot(2,2,1)
    plt.imshow(firstImage)
    fig.add_subplot(2,2,2)
    plt.imshow(secondImage)
    plt.show()
    im1_pts, im2_pts = click_correspondences(firstImage, secondImage)
    print(im1_pts.shape)
    print(im2_pts.shape)
    print(len(im1_pts),len(im2_pts))
    np.savetxt('im1_cor_text.txt',im1_pts)
    np.savetxt('im2_cor_text.txt',im2_pts)
    print(im1_pts, im2_pts)
