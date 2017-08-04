from ImageReadWrite.ImageReader import ImageReader


# Created by DimRu on 5/16/2017


class CharacterDb:
    """ Class reads the characters defined previously and store in a dictionary """

    def __init__(self):
        self.i_reader = ImageReader()
        self.n_list = ['A.bmp', 'B.bmp', 'C.bmp', 'D.bmp', 'E.bmp', 'F.bmp', 'G.bmp',
                       'H.bmp', 'I.bmp', 'J.bmp', 'K.bmp', 'L.bmp', 'M.bmp', 'N.bmp',
                       'O.bmp', 'P.bmp', 'Q.bmp', 'R.bmp', 'S.bmp', 'T.bmp', 'U.bmp',
                       'V.bmp', 'W.bmp', 'X.bmp', 'Y.bmp', 'Z.bmp', ]
        self.i_list = {}  # initializing a dictionary

    '''@:return dictionary file name as the key image object as value'''

    def character_db(self):
        for item in self.n_list:
            i_str = 'data/' + item
            self.i_list[item] = self.i_reader.image_reader(i_str)
        return self.i_list
