import cv2

from enhancemant.ImageObject import ImageObject


# Created by DimRu 07/05


class ImageReader:
    """Read the Image as a gray scale image"""

    def __init__(self):
        pass

    def image_reader(self, image_name):
        image_object = ImageObject()
        image_object.set_image_name(image_name)

        img = cv2.imread('images/' + image_name, 0)  # read image as a gray scale image
        img = cv2.medianBlur(img, 5)
        image_object.set_image_matrix(img)

        img_shape = img.shape
        image_object.set_image_height(img_shape[0])
        image_object.set_image_width(img_shape[1])

        return image_object
