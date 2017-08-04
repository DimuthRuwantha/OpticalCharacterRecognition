from ImageReadWrite.ImageWriter import ImageWriter
from enhancemant.ImageObject import ImageObject


# Created by DimRu on 5/9/2017


class CharacterExtraction:
    """ Add the class description here """

    def __init__(self):
        self.__image_matrix = 0
        self.__image_name = ""
        self.__image_height = 0
        self.__image_width = 0
        self.__image_list = []

    def split_image(self, image_object):
        """Splitting the image into letter wise images"""

        # i_writer = ImageWriter()

        # Extract all the parameters from the image object
        self.__image_matrix = image_object.get_image_matrix()
        self.__image_name = image_object.get_image_name()
        self.__image_height = image_object.get_image_height()
        self.__image_width = image_object.get_image_width()

        has_black = False
        pre_col_black = False
        left_limit = 0
        right_limit = 0
        no = 0

        for i in range(self.__image_width):

            if has_black:  # check previous column whether it has black
                pre_col_black = True
            has_black = False

            for j in range(self.__image_height):  # Iterate row by row in each column

                if self.__image_matrix[j, i] < 100:
                    has_black = True
                    if not pre_col_black:
                        left_limit = i

            if pre_col_black and not has_black:  # true when columns are black to white
                no += 1
                right_limit = i
                image_width = right_limit - left_limit
                char_img = self.__image_matrix[:, left_limit - 1:right_limit + 1]
                image_name = "{}char.bmp".format(no)

                image_object = ImageObject()
                image_object.set_image_matrix(char_img)
                image_object.set_image_name(image_name)
                image_object.set_image_width(image_width)
                image_object.set_image_height(self.__image_height)

                self.__image_list.append(image_object)
                # i_writer.write_image(image_object)
                pre_col_black = False

    def get_image_list(self):
        return self.__image_list
