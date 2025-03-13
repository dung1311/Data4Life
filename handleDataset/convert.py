import os
import sys
import cv2

classes = {
    'plane': 0,
    'ship': 1,
    'storage-tank': 2,
    'baseball-diamond': 3,
    'tennis-court': 4,
    'basketball-court': 5,
    'ground-track-field': 6,
    'harbor': 7,
    'bridge': 8,
    'large-vehicle': 9,
    'small-vehicle': 10,
    'helicopter': 11,
    'roundabout': 12,
    'soccer-ball-field': 13,
    'swimming-pool': 14
}

def change_format(labels_dir, images_dir, labels_out):
    count = 0
    for file in os.listdir(labels_dir):
        f = open(labels_dir+file, 'r')
        # bo di 2 dong dau
        lines = f.readlines()[2:]
        coordinates = []
        img = cv2.imread(images_dir+file[:-4]+'.jpg')
        imageHeight, imageWidth, _ = img.shape
        count += 1

        for line in lines:
            split_line = line.rsplit(sep=' ', maxsplit=2)
            
            # ['2753 2408 2861 2385 2888 2468 2805 2502', 'plane', '0\n']
            category = classes[split_line[-2]]
            coors = split_line[0].split(' ')
            #['2753', '2408', '2861', '2385', '2888', '2468', '2805', '2502']
            # print(coors)

            coor_x = coors[::2]
            coor_y = coors[1::2]

            x = [float(i) for i in coor_x]
            y = [float(i) for i in coor_y]

            x_max, y_max, x_min, y_min = max(x), max(y), min(x), min(y)
            x_center, y_center = float((x_max+x_min)/2)* (1/imageWidth), float((y_max+y_min)/2)*(1/imageHeight)
            boundingWidth , boundingHeight = (x_max - x_min) * (1/imageWidth), (y_max - y_min) * (1/imageHeight)

            text = f'{category} {x_center} {y_center} {boundingWidth} {boundingHeight}\n'
            File = open(labels_out+file, 'a')
            File.write(text)
            File.close()
    
    print(f'all file: {count}')

def main():
    change_format('../DOTAv1/labels/train_original/', '../DOTAv1/images/train/', '../DOTAv1/labels/train_labels/')
    change_format('../DOTAv1/labels/val_original/', '../DOTAv1/images/val/', '../DOTAv1/labels/val_labels/')

if __name__ == '__main__':
    main()