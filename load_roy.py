from skimage.draw import polygon
import numpy as np
import plistlib
import cv2
x= 3328
y= 4084
altura = x
largura = y
def load_inbreast_mask(mask_path, imshape=(largura, altura)):
    """
    This function loads a osirix xml region as a binary numpy array for INBREAST
    dataset

    @mask_path : Path to the xml file
    @imshape : The shape of the image as an array e.g. [4084, 3328]

    return: numpy array where positions in the roi are assigned a value of 1.

    """

    def load_point(point_string):
        x, y = tuple([float(num) for num in point_string.strip('()').split(',')])
        return y, x

    mask = np.zeros(imshape)
    with open(mask_path, 'rb') as mask_file:
        plist_dict = plistlib.load(mask_file, fmt=plistlib.FMT_XML)['Images'][0]
        numRois = plist_dict['NumberOfROIs']
        rois = plist_dict['ROIs']
        assert len(rois) == numRois
        for roi in rois:
            numPoints = roi['NumberOfPoints']
            points = roi['Point_px']
            assert numPoints == len(points)
            points = [load_point(point) for point in points]
            if len(points) <= 2:
                for point in points:
                    mask[int(point[0]), int(point[1])] = 255
            else:
                x, y = zip(*points)
                x, y = np.array(x), np.array(y)
                poly_x, poly_y = polygon(x, y, shape=imshape)
                mask[poly_x, poly_y] = 255
    return mask

def main():
    #mask_path = "ALLROI/20586908.roi"
    codigo = "22670324.xml"
    mask_path = "C:/Users/vicente/Downloads/IC/Inbreast/AllXML/" + codigo
    mask = load_inbreast_mask(mask_path, imshape=(largura, altura))
    cv2.imwrite( codigo +'.png', mask)
    print("end")



if __name__ == "__main__":
   main()