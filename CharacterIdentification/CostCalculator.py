import numpy as np


# Created by DimRu on 5/30/2017


class CostCalculator:
    """ Add the class description here """

    def __init__(self):
        pass

    def cost_calculator(self, img_matrix, db_matrix):
        result = np.sqrt(np.absolute(np.array(img_matrix) - np.array(db_matrix)))
        cost = result.sum()

        return cost  # check result value if the value is lower than threashold value return true
