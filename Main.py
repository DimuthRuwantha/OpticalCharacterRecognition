from CharacterIdentification.CharacterDb import CharacterDb
from CharacterIdentification.CharacterIdentifier import CharacterIdentifier
from CharacterIdentification.ScaleProcessor import ScaleProcessor
from Extractions.CharacterExtraction import CharacterExtraction
from Extractions.TextExtraction import TextExtraction
from ImageReadWrite.ImageReader import ImageReader
from ImageReadWrite.ImageWriter import ImageWriter
from enhancemant.Enhancement import Enhancement
from enhancemant.ImageObject import ImageObject

if __name__ == '__main__':

    # initializing Objects
    char_db = CharacterDb()
    image_object = ImageObject()  # store image properties
    grey_image = ImageObject()
    inverted_grey_image = ImageObject()
    binary_grey_image = ImageObject()
    binarized_i_grey_image = ImageObject()
    enhancement = Enhancement()
    scale_process = ScaleProcessor()

    i_writer = ImageWriter()
    i_reader = ImageReader()
    textExtractor = TextExtraction()  # set the boundary for single character
    char_splitter = CharacterExtraction()
    char_identifier = CharacterIdentifier()
# ================================================================================#

    img_dict = char_db.character_db()  # object read all the characters in the db store to a dictionary
    s = str(input("Enter Image Name:"))

    img_object = i_reader.image_reader(s)

    binary_grey_image = enhancement.binarization(img_object)

    img_object.set_image_name("grey scale {}".format(img_object.get_image_name()))
    i_writer.write_image(img_object)

    char_splitter.split_image(binary_grey_image)  # split a word into characters

    letter_list = char_splitter.get_image_list()  # return the list split into characters

    word = ''
    for letter in letter_list:
        img_obj = textExtractor.text_extractor(letter)
        img_obj = scale_process.scale_processor(img_obj)
        word += char_identifier.character_identifier(img_obj, img_dict)

    print("text was identified as : " + word)
    input("press enter to exit")
