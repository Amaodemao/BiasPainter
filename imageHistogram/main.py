import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import pandas as pd

def color_hist(image, image_name="a given image", show_total=True, bins=256, min=0, max=256, ax=None):
    if ax is None:
        ax = plt.figure(figsize=(8, 6)).add_subplot()
    if show_total:
        ax.hist(image, bins=bins, range=(min, max), color='blue', label="Total")
    try:
        mean = np.mean(image)
        median = np.median(image)
        oneThird = np.percentile(image, 33)
    except:
        mean = 255
        median = 255
        oneThird = 255
    ax.legend(loc='best')
    ax.set_title(f"Color Histogram of {image_name}")
    ax.set_xlabel(f"Intensity Value, mean brightness {mean}, median {median}, oneThird {oneThird}")
    ax.set_ylabel("Count")
    
    return mean, median, oneThird

def main():
    if os.path.exists('output.csv'):
        df = pd.read_csv('output.csv')
    else:
        df = pd.DataFrame()
    for root, dirs, files in os.walk(".\inputs"):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                path = os.path.join(root, file)
            figure = plt.figure(figsize=(24, 6)).subplots(1, 3)
            img = np.array(Image.open(path))
            marker = np.zeros_like(img)
            figure[0].imshow(img)
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
            mean, median, oneThird = color_hist(values.ravel(), file, ax=figure[1])
            figure[2].imshow(marker)
            outputDir = os.path.dirname(path.replace('inputs', 'outputs'))
            if not os.path.exists(outputDir):
                os.makedirs(outputDir)
                plt.savefig(os.path.join(outputDir, file))
            else:
                plt.savefig(os.path.join(outputDir, file))
            plt.close()
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