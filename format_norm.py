import os
import numpy as np
import argparse

def convert_ark_to_array(vector_path='xvector.txt'):
    data_path = []
    ivector = []
    f = open(vector_path)
    for line in f.readlines():
        split_data = line.strip().split(' ')
        split_data = [item for item in split_data if item!='']
        name_item = split_data[0]
        features_item = np.array(split_data[2:-1]).astype('float')
        data_path.append({'pic_path': name_item})
        ivector.append(features_item)

    return data_path, ivector


if __name__ == '__main__':

    # Gain paramters
    parser = argparse.ArgumentParser(description='Format convertion')
    parser.add_argument('--vector_path', default='', type=str, help='input vector path: ivector or xvector')
    parser.add_argument('--save_path', default='vector.npz', type=str, help='save features path')
    global args
    args = parser.parse_args()

    assert args.vector_path!=''
    assert args.save_path!=''
  
    data_path, ivector = convert_ark_to_array(args.vector_path)
    np.savez_compressed(args.save_path,
                        data_path=data_path,
                        features=ivector
                        )





