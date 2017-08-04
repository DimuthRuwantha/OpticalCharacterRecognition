from ImageReadWrite import ImageWriter
from enhancemant.ImageObject import ImageObject


class TextExtraction:
    """Text Extraction used to find the boundary limits of a character"""

    def __init__(self):

        self.__img_matrix = 0
        self.__img_name = ""
        self.__height = 0
        self.__width = 0

        self.i_writer = ImageWriter.ImageWriter()

    def text_extractor(self, image_obj):

        temp_image_object = ImageObject()

        self.__img_name = image_obj.get_image_name()
        self.__height = image_obj.get_image_height()
        self.__width = image_obj.get_image_width()
        self.__img_matrix = image_obj.get_image_matrix()

        left_limit = self.__width
        right_limit = 0
        top_limit = self.__height
        bottom_limit = 0

        for i in range(self.__width - 1):
            for j in range(self.__height - 1):
                variable = self.__img_matrix[j, i]
                if self.__img_matrix[j, i] < 100:

                    if top_limit > j:
                        top_limit = j
                    if bottom_limit < j:
                        bottom_limit = j

        a = self.__img_matrix[top_limit - 1:bottom_limit + 1, :]

        temp_image_object.set_image_matrix(a)
        temp_image_object.set_image_name('crop{}'.format(self.__img_name))
        # self.i_writer.write_image(temp_object)

        return temp_image_object
