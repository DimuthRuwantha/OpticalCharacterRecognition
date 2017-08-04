class ImageObject:
    def __init__(self):
        self.__image_name = ""
        self.__image_matrix = 0
        self.__image_width = 0
        self.__image_height = 0

    def set_image_name(self, name):
        self.__image_name = name

    def get_image_name(self):
        return self.__image_name

    def set_image_matrix(self, matrix):
        self.__image_matrix = matrix

    def get_image_matrix(self):
        return self.__image_matrix

    def set_image_width(self, width):
        self.__image_width = width

    def get_image_width(self):
        return self.__image_width

    def set_image_height(self, height):
        self.__image_height = height

    def get_image_height(self):
        return self.__image_height
