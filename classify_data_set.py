import random
import os
import shutil

#Classification ratio for train data, valid data, test data
#default ratio is 10 persent
#first moves 10 persent data files frome all data set files(train data folder) to valid folder
#moves 10 persent data files frome train data folder to tset folder afer moving valid data
split_ratio = 0.1

TRAIN_IMAGE_DATA_DIR = 'data_sets/train/images'
TRAIN_LABEL_DATA_DIR = 'data_sets/train/labels'

VALID_IMAGE_DATA_DIR = 'data_sets/valid/images'
VALID_LABEL_DATA_DIR = 'data_sets/valid/labels'

TEST_IMAGE_DATA_DIR = 'data_sets/test/images'
TEST_LABEL_DATA_DIR = 'data_sets/test/labels'

def move_files(frome_img_folder, frome_label_folder,to_img_folder, to_label_folder, ratio):
    #search all data file names in a train folder(folder of all dataset files)
    img_file_name_list = list(map(lambda x : x.split('.')[0], os.listdir(frome_img_folder)))

    #move data files at a certain rate to search for files to move to
    split_num = int(len(img_file_name_list) * ratio)
    random.shuffle(img_file_name_list)

    move_file_name_list = img_file_name_list[:split_num]

    print('=======================================')
    print('start moving...')

    #transfer the data file from train folder into valid folder or test folder
    for file_name in move_file_name_list:
        shutil.move(os.path.join(frome_img_folder,file_name) + '.jpg',
                    os.path.join(to_img_folder,file_name) + '.jpg')
        shutil.move(os.path.join(frome_label_folder,file_name) + '.txt',
                    os.path.join(to_label_folder,file_name) + '.txt')

    print('=======================================')
    print('remaining img nums : ', len(os.listdir(frome_img_folder)),'\nremaining label nums : ', len(os.listdir(frome_label_folder)))
    print('moving img nums : ', len(os.listdir(to_img_folder)),'\nmoving label nums : ', len(os.listdir(to_label_folder)))
    print('=======================================')

print("Move valid data\n")
move_files(TRAIN_IMAGE_DATA_DIR, TRAIN_LABEL_DATA_DIR, VALID_IMAGE_DATA_DIR, VALID_LABEL_DATA_DIR, split_ratio)
print("Move test data\n")
move_files(TRAIN_IMAGE_DATA_DIR, TRAIN_LABEL_DATA_DIR, TEST_IMAGE_DATA_DIR, TEST_LABEL_DATA_DIR, split_ratio)
