"""Gets user category choice. returns category, with a random question and answer from that category """
def create_question_object() -> set:
  # Get user catagory choice
  while True:
    category_choice = input("""
    Choose catergory:

    1. Anime
    2. Books

    """)
    if category_choice.isdigit() and 0 < int(category_choice) < 3:
      break
    else:
      print("\nInput must be a number.\n")
  categories_menu = {1: 'anime', 2: 'book'}
  chosen_category = categories_menu[int(category_choice)]

  # getattr essentially calls the menthod using the chosen category(they have the same name)
  category = getattr(InfoDatabase, chosen_category)
  category_dict = category()

  # choice from category is a tuple.. ("naruto","initially set in konoha village what what")
  choice_from_category = random.choice(list(category_dict.items()))

  actual_answer = choice_from_category[0]
  question = choice_from_category[1]

  return chosen_category, question, actual_answer