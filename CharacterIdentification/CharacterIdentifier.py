from CharacterIdentification.CostCalculator import CostCalculator


# Created by DimRu on 5/16/2017


class CharacterIdentifier:
    """ class compare the matrices and return the maximum confidence letter """

    def __init__(self):
        pass

    @classmethod
    def image_evaluator(cls, img_object, db_img_object):
        """split the letter to 10x10 sub matrices and get the cost for each matrix"""

        cost_calculator = CostCalculator()

        img_matrix = img_object.get_image_matrix()
        db_matrix = db_img_object.get_image_matrix()
        total_cost = 0

        for i in range(0, 50, 10):  # iterate through rows 0 to 50 10 by 10 like 0, 10, 20, 30, 40

            top_limit = i  # define the top limit of the image
            bottom_limit = i + 10  # Define the bottom limit of the image

            for j in range(0, 50, 10):  # iterate through columns
                left_limit = j
                right_limit = j + 10
                sub_matrix = img_matrix[top_limit:bottom_limit, left_limit:right_limit]  # select the sub matrix
                db_sub_matrix = db_matrix[top_limit:bottom_limit, left_limit:right_limit]  # select db sub matrix

                cost = cost_calculator.cost_calculator(sub_matrix,
                                                       db_sub_matrix)  # find the cost comparing with db_sub_matrix
                total_cost += cost
        print("letter {} cost = {}".format(db_img_object.get_image_name()[-5], total_cost))
        return total_cost

    def character_identifier(self, img_object, img_db):
        """iterate through all images and find the cost and return the minimum"""
        cost_min = 10000000
        letter = ""
        for db_image in img_db.values():

            current_cost = self.image_evaluator(img_object, db_image)

            if current_cost < cost_min:
                cost_min = current_cost
                letter = db_image.get_image_name()

        print("========================")
        print("letter identified as " + letter[-5] + "\n")
        return letter[-5]
