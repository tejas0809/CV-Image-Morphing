import numpy as np
from PIL import Image
from click_correspondences import click_correspondences
from morph_tri import morph_tri
import cv2
import imageio

if __name__=="__main__":
        #input images for the morphine,(both should be of same dimensions)
        firstImage = np.array(Image.open('elonTejas1.jpg').convert('RGB'))
        secondImage = np.array(Image.open('elonTejas2.jpg').convert('RGB'))
        print('--select points for matching the features, no need to select the points on the boundary of the image frames')
        im1_pts, im2_pts = click_correspondences(firstImage, secondImage)
        print('--np arrays of selected points saved in files im1_cor_text.txt im2_cor_text.txt ')
        np.savetxt('im1_cor_text.txt',im1_pts)
        np.savetxt('im2_cor_text.txt',im2_pts)
        #no. of frames to be generated
        print('--generating 60 frames, change frames in line 18 of run.py, if required')
        frames=60
        print('--warp_frac and dissolve_frac are computed according to the required number of frames')

        warp_frac=np.linspace(0,1,frames,endpoint=True)
        dissolve_frac=np.linspace(0,1,frames,endpoint=True)
        # print(warp_frac)
        # print(dissolve_frac)
        print('--generating image frame using morph_tri')
        morphed_im=morph_tri(firstImage, secondImage, im1_pts, im2_pts, warp_frac, dissolve_frac)
        print('--morphed_im created, now creating gif and avi')

        #Create AVI video
        fps = 10
        video_filename = 'outputMorphing.avi'
        morphed_im[:,:,:,0]
        height,width=morphed_im.shape[1],morphed_im.shape[2]
        out = cv2.VideoWriter(video_filename, 0, fps, (width, height))
        img=np.uint8(morphed_im)

        for i in range(morphed_im.shape[0]):
          img=np.uint8(morphed_im[i,:,:,:])
          img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
          out.write(img)
        out.release

        #create gif
        images=[]
        for p in range(morphed_im.shape[0]):
            images.append(np.uint8(morphed_im[p,:,:,:]))

        imageio.mimsave('output.gif',images,duration=0.05)

        print('--check output.gif and outputMorphing.avi files, animation should be ready')
