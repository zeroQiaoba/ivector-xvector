import os
import numpy as np
import argparse

def convert_ark_to_array(ivector_path='ivector.txt', xvector_path='xvector.txt',save_path='./i_x_vector.npz'):
    data_path1 = []
    ivector = []
    f = open(ivector_path)
    for line in f.readlines():
        split_data = line.strip().split(' ')
        split_data = [item for item in split_data if item!='']
        name_item = split_data[0]
        features_item = np.array(split_data[2:-1]).astype('float')
        data_path1.append({'pic_path': name_item})
        ivector.append(features_item)

    data_path2 = []
    xvector = []
    f = open(xvector_path)
    for line in f.readlines():
        split_data = line.strip().split(' ')
        split_data = [item for item in split_data if item!='']
        name_item = split_data[0]
        features_item = np.array(split_data[2:-1]).astype('float')
        data_path2.append({'pic_path': name_item})
        xvector.append(features_item)

    assert data_path1==data_path2

    np.savez_compressed(save_path,
                        data_path=data_path1,
                        ivector=ivector,
                        xvector=xvector
                        )


if __name__ == '__main__':

    # Gain paramters
    parser = argparse.ArgumentParser(description='Format convertion')
    parser.add_argument('--ivector_path', default='ivector/data/feat/ivectors_enroll_mfcc/ivector.txt', type=str, help='input ivector path')
    parser.add_argument('--xvector_path', default='xvector/data/feat/xvectors_enroll_mfcc/xvector.txt', type=str, help='input xvector path')
    parser.add_argument('--save_path', default='./i_x_vector.npz', type=str, help='save features path')
    global args
    args = parser.parse_args()

    convert_ark_to_array(args.ivector_path, args.xvector_path, args.save_path)