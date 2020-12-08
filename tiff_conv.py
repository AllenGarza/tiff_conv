import sys
import os
from skimage import io as sk


# Ensure you have skimage installed, use "pip install -U scikit-image"


def main():
    folder = sys.argv[1]
    if os.path.abspath(folder):
        dir_out = os.path.join(os.path.abspath(folder) + "_out")
        try:
            os.mkdir(dir_out)
        except OSError:
            print("Creation of out directory failed, ignore this error message if it already exists")

    else:
        print('usage: tiff_conv [input-dir] \n')
        print('outputs to [input-dir]_out \n')
        print('changes any .jpg image in a directory to .tif, any .tif any other image file is left alone.')

    for f in os.listdir(folder):
        if f[-4:] == ".jpg":
            newFilename = f.replace(".jpg", ".tif") # get a string of file name, change extension to .tif
            imagePath = os.path.join(folder, f)     # path to image file
            img = sk.imread(imagePath)              # read image file using scikit
            imageOutPath = os.path.join(dir_out, newFilename)   # create a path using the *_out/file.tif
            out = sk.imsave(imageOutPath, img)      # save to that newly created path with new extension (*.tif)


if __name__ == '__main__':
    main()
