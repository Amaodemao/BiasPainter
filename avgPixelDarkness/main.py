import os
import cv2
import numpy as np
import csv
import pandas as pd
from PIL import Image
import numba

def test():
    path = os.getcwd()
    print("Current Directory", path)
    
    print(os.path.basename(path))

# def main():
#     if os.path.exists('output.csv'):
#         df = pd.read_csv('output.csv')
#     else:
#         df = pd.DataFrame()
#     for root, dirs, files in os.walk(".\inputs"):
#         for file in files:
#             if file.endswith('.jpg') or file.endswith('.png'):
#                 path = os.path.join(root, file)
#                 print(path)
#                 count = 0
#                 sum = np.zeros((1, 3))
#                 img = cv2.imread(path).astype(np.float32)
#                 shape = list(img.shape)
#                 for i in range(shape[0]):
#                     for j in range(shape[1]):
#                         if img[i, j][0] != 255.0 and img[i, j][1] != 255.0 and img[i, j][2] != 255.0:
#                             count += 1
#                             sum += img[i, j]
#                 if count != 0:
#                     avg = sum / count # average color of the face
#                 else:
#                     avg = np.empty((1,3)) # indicate the existence of invalid
#                     avg.fill(255)         # output / no face was detected or
#                                           # cropped from the input image.
#                 avg_num = (avg[0][0] + avg[0][1] + avg[0][2]) / 3
#                 filename = os.path.basename(path)
#                 path = os.path.dirname(path)
#                 directory = os.path.basename(path)
#                 print(path + "   " + str(avg_num))
#                 # write the output to a csv file
#                 if not filename in df.index:
#                     df = df.append(pd.Series(name=filename))
#                 #if df does not include the column, add it
#                 if not directory in df.columns:
#                     df[directory] = np.nan
#                 df.at[filename, directory] = avg_num
#         df.to_csv('output.csv', mode='a', header=True)

# @numba.jit
def main():
    if os.path.exists('output.csv'):
        df = pd.read_csv('output.csv')
    else:
        df = pd.DataFrame()
    for root, dirs, files in os.walk(".\inputs"):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                path = os.path.join(root, file)
            img = np.array(Image.open(path))
            marker = np.zeros_like(img)
            values = []
            length = img.shape[0]
            width = img.shape[1]
            for i in range(length):
                for j in range(width):
                    if img[i][j][0] >= 250 and img[i][j][1] >= 250 and img[i][j][2] >= 250:
                        marker[i][j][0] = 0
                        marker[i][j][1] = 0
                        marker[i][j][2] = 0
                        continue
                    if img[i][j][0] <= 5 and img[i][j][1] <= 5 and img[i][j][2] <= 5:
                        marker[i][j][0] = 0
                        marker[i][j][1] = 0
                        marker[i][j][2] = 0
                        continue
                    # elif img[i][j][0] >= 250 or img[i][j][1] >= 250 or img[i][j][2] >= 250:
                    #     marker[i][j] = img[i][j]
                    #     continue
                    else:
                        marker[i][j] = img[i][j]
                        values.append(img[i][j])
            values = np.array(values)
            # print(values.ravel())
            mean = np.mean(values.ravel())
            filename = os.path.basename(path)
            path = os.path.dirname(path)
            directory = os.path.basename(path)
            print(path + "   " + str(mean))
            #if df does not include the index, add it
            if not filename in df.index:
                df = df.append(pd.Series(name=filename))
            #if df does not include the column, add it
            if not directory in df.columns:
                df[directory] = np.nan
            df.at[filename, directory] = mean
    df.to_csv('output.csv', mode='w')

main()