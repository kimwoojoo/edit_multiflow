import cv2
import numpy as np
import json
import os

def get_annotation_len(images):
    # max idx + 1
    dict_len = len(images)


    return dict_len

#frame_info
# 0 : image_name, 1 : annotations_id, 2 : bbox 3 : category 4 : outputName
def read_frame(frame_info,avg_size):
    for i in frame_info :
        edit_name = str(i[1])

        if i[3] == 1 :
            save_frameName = './tmp/ex/'+ 'notcrop_1/' + edit_name + '.png'

        elif i[3] == 2:
            save_frameName = './tmp/ex/' + 'notcrop_2/' + edit_name + '.png'

        frame = cv2.imread(str(i[0]))
        #dst_frame = crop_bbox(frame, i[2])
        save_frame(frame, save_frameName)

def crop_bbox(frame,bbox):
    result = frame[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
    return result

def save_frame(frame, frame_name) :
    print(frame_name)
    try :
        cv2.imwrite(frame_name, frame)
    except Exception as e:
        print(str(e))


def change_bbox_file_info(file_info, idx, avg_bbox_data):
    file_info[idx][2] = avg_bbox_data
    file_info[idx+1][2] = avg_bbox_data
    file_info[idx+2][2] = avg_bbox_data

    return file_info

def avg_bbox(file_info) :
    x=0
    y=0
    w=0
    h=0

    avg_bbox_data = []

    for box in range(0, len(file_info)-1, 3) :

        x += int(file_info[box][2][0]) + int(file_info[box+1][2][0]) + int(file_info[box+2][2][0])
        y += int(file_info[box][2][1]) + int(file_info[box+1][2][1]) + int(file_info[box+2][2][1])
        w += int(file_info[box][2][2]) + int(file_info[box+1][2][2]) + int(file_info[box+2][2][2])
        h += int(file_info[box][2][3]) + int(file_info[box+1][2][3]) + int(file_info[box+2][2][3])
        avg_bbox_data.append(x / 3)
        avg_bbox_data.append(y / 3)
        avg_bbox_data.append(w / 3)
        avg_bbox_data.append(h / 3)

        file_info = change_bbox_file_info(file_info, box, avg_bbox_data)
        avg_bbox_data = []
        x=0
        y=0
        w=0
        h=0

    return file_info

def get_file_info(dict, dst, images_idx, annotations_idx) :
    file_info = []
    # dictionary
    for file in range(images_idx):
        for jile in range(annotations_idx):
            if dict['images'][file]['id'] == dict['annotations'][jile]['image_id']:
                # file_name redefine
                file_name = dict['images'][file]['file_name']
                file_dir = file_name[:file_name.find('x720') + 4]
                file_path = dst + file_dir + '/' + file_name
                # 0 : image_name, 1 : annotations_id, 2 : bbox 3 : category 4 : outputName
                file_info.append([file_path, dict['annotations'][jile]['id'], dict['annotations'][jile]['bbox'],
                                  dict['annotations'][jile]['category_id'], file_dir])

    return file_info

def main():

    # Shoplifting_119_x720.mp4.json
    #/media/gim/SUB/Shoplifting_1280x720/data/save_csv/Shoplifting_edit.json
    #file_name = 'Shoplifting_edit.json'
    file_path = '/media/gim/SUB/Shoplifting_1280x720/data/save_csv/Shoplifting_edit.json'
    if os.path.exists(file_path):
        print("Edit file exist. continue editing")
        jstring = open(file_path, 'r').read()

    dict = json.loads(jstring)

    annotations_idx = int(get_annotation_len(dict['annotations']))
    images_idx = int(get_annotation_len(dict['images']))
    print(annotations_idx , images_idx)

    #print(dict['annotations'])

    #image_dir
    dst = '/media/gim/SUB/Shoplifting_1280x720/'
    # 0 : image_name, 1 : annotations_id, 2 : bbox 3 : category 4 : outputName
    file_info = get_file_info(dict, dst, images_idx, annotations_idx)
    avg_size = [0,0,0,0]

    for i in file_info :
        avg_size[0] += i[2][0]
        avg_size[1] += i[2][1]
        avg_size[2] += i[2][2]
        avg_size[3] += i[2][3]

    avg_size[0] = avg_size[0] / len(file_info)
    avg_size[1] = avg_size[1] / len(file_info)
    avg_size[2] = avg_size[2] / len(file_info)
    avg_size[3] = avg_size[3] / len(file_info)
    print (avg_size)

    file_info = avg_bbox(file_info)
    read_frame(file_info,avg_size)







    #print file_info[0] file_info[1] file_info[2]
    # for fname in frame_name :
    #     real_frame_name.append(dst + dir_name + fname)

    # dir_name = 'Shoplifting_119_x720/'
    # frame_info = []
    # frame_name.append('Shoplifting_119_x72020190911185719_150.jpg')
    # frame_name.append('Shoplifting_119_x72020190911185719_151.jpg')
    # frame_name.append('Shoplifting_119_x72020190911185720_152.jpg')
    # real_frame_name = []
    # bbox = []
    # #x,y,w,h
    # bbox.append([ 369.0, 161.0, 140.0, 276.0 ])
    # bbox.append([ 371.0, 165.0, 129.0, 306.0 ])
    # bbox.append([ 355.0, 171.0, 146.0, 302.0 ])
    #
    # bbox_data = avg_bbox(bbox)
    #
    # for fname in frame_name :
    #     real_frame_name.append(dst + dir_name + fname)
    #
    # read_frame(1, real_frame_name,bbox_data)




main()