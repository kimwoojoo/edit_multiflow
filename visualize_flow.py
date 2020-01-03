import numpy as np
import matplotlib.colors as cl
import matplotlib.pyplot as plt
import flow_vis
import os
import cv2
import torch
from torch.nn.functional import normalize
from torch import FloatTensor

def read_flow(filename):
    """
    read optical flow from Middlebury .flo file
    :param filename: name of the flow file
    :return: optical flow data in matrix
    """
    f = open(filename, 'rb')
    magic = np.fromfile(f, np.float32, count=1)
    data2d = None

    if 202021.25 != magic:
        print 'Magic number incorrect. Invalid .flo file'
    else:
        w = np.fromfile(f, np.int32, count=1)
        h = np.fromfile(f, np.int32, count=1)
        print "Reading %d x %d flo file" % (h, w)
        data2d = np.fromfile(f, np.float32, count=2 * w * h)
        # reshape data into 3D array (columns, rows, channels)
        data2d = np.resize(data2d, (h[0], w[0], 2))
    f.close()
    return data2d



def writeFlowFile(filename, uv):
    """
    According to the matlab code of Deqing Sun and c++ source code of Daniel Scharstein
    Contact: dqsun@cs.brown.edu
    Contact: schar@middlebury.edu
    """
    TAG_STRING = np.array(202021.25, dtype=np.float32)
    if uv.shape[2] != 2:
        sys.exit("writeFlowFile: flow must have two bands!");
    H = np.array(uv.shape[0], dtype=np.int32)
    W = np.array(uv.shape[1], dtype=np.int32)
    with open(filename, 'wb') as f:
        f.write(TAG_STRING.tobytes())
        f.write(W.tobytes())
        f.write(H.tobytes())
        f.write(uv.tobytes())



def search(dirName):
    filenames = os.listdir(dirName)
    listnames = []

    for filename in filenames :
        real_filename = os.path.join(dirName, filename)

        fileext = os.path.splitext(real_filename)[-1]
        if fileext == '.flo':
            print(os.path.splitext(filename)[0])
            s = os.path.splitext(filename)[0].split('_')

            print(int(s[0]))
            listnames.append(int(s[0]))



    listnames.sort()

    for file in listnames:

        #2 images crop_flow
        # flow_uv = read_flow(dirName+'/'+str(file) + '_fusion.flo')
        # flow_color = flow_vis.flow_to_color(flow_uv, convert_to_bgr=True)
        # fig = plt.figure()
        # img1 = cv2.imread(dirName + '/' + str(file) + '.png')
        # ax1 = fig.add_subplot(2, 2, 1)
        # ax1.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        # ax1.set_title('input_image')
        # ax2 = fig.add_subplot(2, 2, 2)
        # ax2.imshow(flow_color)
        # ax2.set_title('opticalflow_image')
        # Display the image
        # normal_flow = normalize(FloatTensor(flow_uv), dim=0, eps=1e-16).numpy()
        # print(normal_flow)
        #notclop_flow

        #4 images crop_flow
        flow_uv = read_flow(dirName+'/'+str(file) + '_fusion.flo')
        print(flow_uv)
        flow_color = flow_vis.flow_to_color(flow_uv, convert_to_bgr=True)
        fig = plt.figure()
        img1 = cv2.imread(dirName + '/' + str(file) + '.png')
        ax1 = fig.add_subplot(2, 2, 1)
        ax1.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        ax1.set_title('input_image')
        ax1.axis('off')
        ax2 = fig.add_subplot(2, 2, 2)
        ax2.imshow(flow_color)
        ax2.set_title('opticalflow_image')
        ax2.axis('off')
        # Display the image
        # normal_flow = normalize(FloatTensor(flow_uv), dim=0, eps=1e-16).numpy()
        # print(normal_flow)
        #notclop_flow
        flow_uv2 = read_flow('/home/gim/Downloads/PWC-Net/Multi_Frame_Flow/tmp/ex/notcrop_1'+'/'+str(file) + '_fusion.flo')
        flow_color2 = flow_vis.flow_to_color(flow_uv2, convert_to_bgr=True)
        img2 = cv2.imread('/home/gim/Downloads/PWC-Net/Multi_Frame_Flow/tmp/ex/notcrop_1' + '/' + str(file) + '.png')
        ax3 = fig.add_subplot(2, 2, 3)
        ax3.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
        ax3.set_title('input_image')
        ax3.axis('off')
        ax4 = fig.add_subplot(2, 2, 4)
        ax4.imshow(flow_color2)
        ax4.set_title('opticalflow_image')
        ax4.axis('off')
        # demensiond avg
        #fig.savefig('/home/gim/Downloads/PWC-Net/Multi_Frame_Flow/tmp/ex/optical_1'+'/'+str(file) + '_optical_flow' + '.png')




        #plt.show()


search('/home/gim/Downloads/PWC-Net/Multi_Frame_Flow/tmp/ex/1')
# # Load normalized flow image of shape [H,W,2]
# flow_uv = read_flow('./tmp/notcrop_S147_fusion.flo')
# print(flow_uv)
# # Apply the coloring (for OpenCV, set convert_to_bgr=True)
# flow_color = flow_vis.flow_to_color(flow_uv, convert_to_bgr=False)
#
# # Display the image
# plt.imshow(flow_color)
# plt.show()
# flow_uv2 = read_flow('./tmp/S221_fusion.flo')
#
# # Apply the coloring (for OpenCV, set convert_to_bgr=True)
# flow_color2 = flow_vis.flow_to_color(flow_uv2, convert_to_bgr=False)
#
# # Display the image
# plt.imshow(flow_color2)
# plt.show()
#
# flow_uv2 = read_flow('./tmp/notcrop_S154_fusion.flo')
#
# # Apply the coloring (for OpenCV, set convert_to_bgr=True)
# flow_color2 = flow_vis.flow_to_color(flow_uv2, convert_to_bgr=False)
#
# # Display the image
# plt.imshow(flow_color2)
# plt.show()