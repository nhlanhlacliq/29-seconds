from database import Database
import random

class Summary():
  category = None
  summary = None
  answer = None

  def __init__(self):
    self.set_category()
    self.set_summary()


  def set_category(self):
    # Get user catagory choice
    while True:
      category_num = input("""Choose category:

      1. Anime
      2. Books

      """)
      if category_num.isdigit() and 0 < int(category_num) < 3:
        break
      else:
        print("\nIncorrect input\n")

    category_num = int(category_num)
    categories_menu = {1: 'anime', 2: 'book'}
    self.category = categories_menu[(category_num)]

  def set_summary(self): 
    # getattr essentially calls the menthod using the chosen category(they have the same name)
    category = getattr(Database, self.get_category())
    category_dict = category()

    # get random summary from category... returns tuple.. ("naruto","initially set in konoha village what what")
    random_answer_summary_pair = random.choice(list(category_dict.items()))

    self.answer = random_answer_summary_pair[0]
    self.summary = random_answer_summary_pair[1]
  
  def get_category(self):
    return self.category

  def get_summary(self):
    return self.summary

  def get_answer(self):
    return self.answer
