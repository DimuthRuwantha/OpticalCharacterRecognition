import cv2

from ImageReadWrite.ImageWriter import ImageWriter
from enhancemant.ImageObject import ImageObject


class Enhancement:
    """Pre-process of the Image"""

    def __init__(self):
        self.__grey_image = ImageObject()
        self.__invert_grey_image = ImageObject()
        self.__threshold_image = ImageObject()
        self.__i_writer = ImageWriter()

    # converting to gray is not needed since image is read in gray scale
    def im_to_gray(self, image):  # Create a grey image object
        self.__grey_image.set_image_name("g{}".format(image.get_image_name()))
        self.__i_writer.write_image(self.__grey_image)

    def invert(self, image=ImageObject()):
        """Convert image into negative
        @:parameter
            imageObject
        @:return
            negative image object"""
        self.__invert_grey_image.set_image_matrix(255 - image.get_image_matrix())
        self.__invert_grey_image.set_image_name("i{}".format(image.get_image_name()))
        self.__invert_grey_image.set_image_height(image.get_image_height())
        self.__invert_grey_image.set_image_width(image.get_image_width())
        self.__i_writer.write_image(self.__invert_grey_image)
        return self.__invert_grey_image

    def binarization(self, image=ImageObject()):
        """binarize the image using a threshold value
        @:parameter
            image object
        @:return binarized image"""

        image_val = image.get_image_matrix()
        retval, img = cv2.threshold(image_val, 127, 255, cv2.THRESH_BINARY)
        self.__threshold_image.set_image_matrix(img)
        self.__threshold_image.set_image_name("binarized {}".format(image.get_image_name()))
        self.__threshold_image.set_image_height(image.get_image_height())
        self.__threshold_image.set_image_width(image.get_image_width())
        self.__i_writer.write_image(self.__threshold_image)
        return self.__threshold_image
