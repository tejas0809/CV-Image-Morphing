'''
  File name: morph_tri.py
  Author:
  Date created:
'''

'''
  File clarification:
    Image morphing via Triangulation
    - Input im1: target image
    - Input im2: source image
    - Input im1_pts: correspondences coordiantes in the target image
    - Input im2_pts: correspondences coordiantes in the source image
    - Input warp_frac: a vector contains warping parameters
    - Input dissolve_frac: a vector contains cross dissolve parameters

    - Output morphed_im: a set of morphed images obtained from different warp and dissolve parameters.
                         The size should be [number of images, image height, image Width, color channel number]
'''

from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt
def morph_tri(im1, im2, im1_pts, im2_pts, warp_frac, dissolve_frac):
  # TODO: Your code here
  # Tips: use Delaunay() function to get Delaunay triangulation;
  # Tips: use tri.find_simplex(pts) to find the triangulation index that pts locates in.
  warp_frac=1-warp_frac
  dissolve_frac=1-dissolve_frac
  # im_FramePts=np.array([[0,0],[0,im1.shape[0]-1],[im1.shape[1]-1,0],[im1.shape[1]-1,im1.shape[0]-1],[0,int(im1.shape[0]/2)],[int(im1.shape[1]/2),0],[int(im1.shape[1]/2),im1.shape[0]-1],[im1.shape[1]-1,int(im1.shape[0]/2)]])
  # im1_pts=np.append(im1_pts,im_FramePts,0)
  # im2_pts=np.append(im2_pts,im_FramePts,0)
  # frames=60
  morphed_im = np.zeros((warp_frac.shape[0],im1.shape[0],im1.shape[1],im1.shape[2]))
  # for i in range(warp_frac.shape[0])
  i=0
  for warp,diss in zip(warp_frac,dissolve_frac):
      # warp_frac=1-(i/(frames-1))
      # dissolve_frac=1-(i/(frames-1))
      imt_pts = warp*im1_pts + (1 - warp)*im2_pts
      Tri_t = Delaunay(imt_pts)
      Triangles_points_t = Tri_t.simplices
      xx, yy = np.meshgrid(np.arange(0, im1.shape[1]), np.arange(0, im1.shape[0]))
      ind=np.stack((xx,yy),-1)


      ind1=ind.reshape(-1,2)
      oness1=np.ones((ind1.shape[0],1))

      xy1=np.concatenate((ind1,oness1),axis=1)
      xy1=xy1.reshape((xy1.shape[0],xy1.shape[1],1))

      triangle_xy_index_t = Tri_t.find_simplex(ind1)

      triangle_xy_points_t = Triangles_points_t[triangle_xy_index_t]

      triangle_xy_points_coords_t=imt_pts[triangle_xy_points_t]

      oness=np.ones((triangle_xy_points_coords_t.shape[0],3,1))
      matrix_stack_t = np.concatenate((triangle_xy_points_coords_t,oness),axis=2)

      matrix_stack_up_t=np.transpose(matrix_stack_t,(0,2,1))

      matrix_stack_inv_t=np.linalg.inv(matrix_stack_up_t)

      abg_t=matrix_stack_inv_t@xy1

      triangle_xy_points_coords_1=im1_pts[triangle_xy_points_t]

      oness_1=np.ones((triangle_xy_points_coords_1.shape[0],3,1))
      matrix_stack_1 = np.concatenate((triangle_xy_points_coords_1,oness_1),axis=2)
      matrix_stack_up_1=np.transpose(matrix_stack_1,(0,2,1))

      xy1_1=matrix_stack_up_1@abg_t


      triangle_xy_points_coords_2=im2_pts[triangle_xy_points_t]

      oness_2=np.ones((triangle_xy_points_coords_2.shape[0],3,1))
      matrix_stack_2 = np.concatenate((triangle_xy_points_coords_2,oness_2),axis=2)
      matrix_stack_up_2=np.transpose(matrix_stack_2,(0,2,1))

      xy1_2=matrix_stack_up_2@abg_t


      xy1=xy1[:,0:2,:]

      xy1_1=xy1_1[:,0:2,:]

      xy1_2=xy1_2[:,0:2,:]

      xy1_sq = xy1.reshape((im1.shape[0],im1.shape[1],2))

      xy1_1_sq=xy1_1.reshape((im1.shape[0],im1.shape[1],2))
      xy1_2_sq=xy1_2.reshape((im1.shape[0],im1.shape[1],2))

      xy1_sq=np.array(xy1_sq,dtype=int)
      xy1_1_sq=np.array(xy1_1_sq,dtype=int)
      xy1_2_sq=np.array(xy1_2_sq,dtype=int)

      for rgb in range(im1.shape[2]):
        morphed_im[i,xy1_sq[:,:,1],xy1_sq[:,:,0],rgb]=im1[xy1_1_sq[:,:,1],xy1_1_sq[:,:,0],rgb]*diss + im2[xy1_2_sq[:,:,1],xy1_2_sq[:,:,0],rgb]*(1-diss)


      # image_t=morphed_im[i,:,:,:]
      # image_t=np.array(image_t,dtype=int)
      i=i+1
      # plt.imshow(image_t)
      # plt.show()

  return morphed_im
