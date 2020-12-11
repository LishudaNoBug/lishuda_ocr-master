import os
from ocr import ocr
import time
import shutil
import argparse
import numpy as np
from PIL import Image
from glob import glob

"""运行时指定参数
"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image to be scanned")
args = vars(ap.parse_args())


def single_pic_proc(image_file):
    image = np.array(Image.open(image_file).convert('RGB'))
    result, image_framed = ocr(image)
    return result,image_framed


if __name__ == '__main__':
    imageFilePath = args["image"]

    image_files = glob(imageFilePath)


    result_dir = './test_result'
    for image_file in sorted(image_files):
        t = time.time()
        result, image_framed = single_pic_proc(image_file)
        output_file = os.path.join(result_dir, image_file.split('/')[-1])
        txt_file = os.path.join(result_dir, image_file.split('/')[-1].split('.')[0]+'.txt')

        txt_f = open(txt_file, 'w')
        Image.fromarray(image_framed).save(output_file)
        # 解析完的数据附加耗时信息等
        # print(txt_file)
        # print("Mission complete, it took {:.3f}s".format(time.time() - t))
        # print("\nRecognition Result:\n")
        for key in result:
            print(result[key][1])
            txt_f.write(result[key][1]+'\n')
        txt_f.close()