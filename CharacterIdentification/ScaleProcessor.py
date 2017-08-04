import cv2

import enhancemant.ImageObject as ImageObject


# Created by DimRu on 5/16/2017


class ScaleProcessor:
    """ fix the scale of the image """

    def __init__(self):
        self.RATIO = 1

    def is_valid(self, image_object):
        i_ratio = image_object.get_image_height() / image_object.get_image_width()

        if i_ratio == self.RATIO:
            return True
        else:
            return False

    def scale_processor(self, image_object=ImageObject.ImageObject()):

        dim = (50, 50)  # image resize dimensions
        img_matrix = image_object.get_image_matrix()
        resized_img = cv2.resize(img_matrix, dim)  # interpolation=cv2.INTER_AREA)
        image_object.set_image_matrix(resized_img)

        return image_object
