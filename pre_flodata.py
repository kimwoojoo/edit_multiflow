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
        print "resize %d x %d to %d x %d" % (h, w, 320, 240)
        data2d = np.fromfile(f, np.float32, count=2 * 320 * 240)
        # reshape data into 3D array (columns, rows, channels)
        data2d = np.resize(data2d, (320, 240, 2))
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

        flow_uv = read_flow(dirName+'/'+str(file) + '_fusion.flo')
        print(flow_uv, flow_uv.shape)
        normal_flow = normalize(FloatTensor(flow_uv), dim=0, eps=1e-16).numpy()
        print(normal_flow , normal_flow.shape)
        writeFlowFile(str(file) + '_norm_1.flo', flow_uv)
        print(np.max(normal_flow), np.min(normal_flow))


search('/home/gim/Downloads/PWC-Net/Multi_Frame_Flow/tmp/ex/1')