import json
import os

def get_annotation_len(images):
    # max idx + 1
    dict_len = len(images)


    return dict_len

def main():
    # Shoplifting_119_x720.mp4.json
    #/media/gim/SUB/Shoplifting_1280x720/data/save_csv/Shoplifting_edit.json
    #file_name = 'Shoplifting_edit.json'
    file_path = '/media/gim/SUB/Shoplifting_1280x720/data/save_csv/Shoplifting_edit.json'
    if os.path.exists(file_path):
        print("Edit file exist. continue editing")
        jstring = open(file_path, 'r').read()

    dict = json.loads(jstring)
    print(get_annotation_len(dict['annotations']))
    print(dict['annotations'][0]['bbox'])
    #print(dict['annotations'])




