import cv2


class ImageWriter:
    """Writes the image to the disk"""

    def __init__(self):
        self.__image_name = ""
        self.__image = 0

    def write_image(self, image):
        self.__image_name = image.get_image_name()
        self.__image = image.get_image_matrix()
        full_path = "{}{}".format("images\\", self.__image_name)
        cv2.imwrite(full_path, self.__image)
        # print("Image {} written successfully".format(self.__image_name))
