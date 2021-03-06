from nltk.probability import FreqDist
import requests
import bs4
from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.summarization import summarize
import re

# url = 'https://www.lilwaynehq.com/lyrics/tha-carter-3/lollipop/'
# page = requests.get(url)
# page.raise_for_status()
# soup = bs4.BeautifulSoup(page.text, 'html.parser')
# p_elems = [element.text for element in soup.find_all('p')]
# speech = ''.join(p_elems)
# speech = re.sub(' rapper', ' wrapper', speech)
# print(speech)


import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from data import InfoDatabase
from datalist import InfoList
import random
from time import sleep
import nltk
from nltk.corpus import stopwords
from PIL import Image
import string
from os import sys
from score import Score
from difficulty import Difficulty

"""'plot', 'synopsis', 'text' and 'question' are all the same thing. basically the description text of the show/book/lyrics"""

"""Countdown timer"""
def countdown_timer(time):
  for i in range(time):
    print(time - i)
    sleep(1)

"""Generates a wordcloud from a chosen category. the question contains the synopsis which the WC is generated from"""
def generate_wordcloud(time_limit, category, question, difficulty_level):
  # 
  words_freq_dist = {}
  # plt.figure(2)
  stops = set(stopwords.words('english')) #Set used for speed
  more_stops= STOPWORDS
  # will need this for plotting too
  words_in_question = [word for word in nltk.word_tokenize(question) if ((word not in stops) and (word not in more_stops))]
  words_freq_dist = nltk.FreqDist(words_in_question)

  # remove {difficulty level} most counted words, add to clues list
  # not yet working.. returns int of word counts instead of actual word
  clues = []
  for i in range(difficulty_level):
    clue = words_freq_dist.pop(words_freq_dist.max())
    clues.append(clue)
  # print(f"These would be the clues {clues}")

  difficulty_adjusted_question = ''
  for word in words_freq_dist.keys():
    difficulty_adjusted_question += word + ' '

  # words_freq_dist.pprint()
  # print(difficulty_adjusted_question)
  # more_stops.update(['Lil Wayne', 'Static Major', 'Lollipop', 'Lil', 'Wayne', 'Static', 'Major', 'Tanya',
                    # 'trisolaris','trisolaran','moby','dick','macbeth','othello','harry','potter','hermione','voldemort',
                    # 'hobbit','saitama','Goku','Vegeta','Frieza','Dragon Balls','Gatsby','','',])

  wc = WordCloud(max_words=500,relative_scaling=0.5,
                background_color='black',stopwords=more_stops,
                margin=2,random_state=8,contour_width=0.5,
                contour_color='white', colormap='copper')
  
  wc.generate(difficulty_adjusted_question)
  # print(wc)
  colors = wc.to_array()

  # plotting frequency distribution of words in question synopsis.. not really needed. I just wanted to see..
  # words_freq_dist.plot(15, linestyle='-', title="LOL words")
  # plt.legend()

  plt.ion()
  plt.figure()
  plt.title(f"Which {category} is this?\n",
  fontsize=15, color='black')
  plt.imshow(colors, interpolation="bilinear")
  plt.axis('off')
  plt.show()
  # plt.savefig('WC.png')
  # wc_image = Image.open('WC.png')
  # wc_image.show()
  plt.pause(0.001)

  # countdown timer
  countdown_timer(time_limit)
  plt.close(1)
  print("Time's up!")

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

"""Displays choices"""
def show_options(chosen_category, actual_answer):
  options_list = getattr(InfoList, chosen_category)
  options_list = options_list()
  
  options_to_display = []
  options_to_display.append(actual_answer)
  while len(options_to_display) < 4:
    option_to_add = random.choice(options_list)
    if option_to_add not in options_to_display:
      options_to_display.append(option_to_add)
  random.shuffle(options_to_display)
  choices_menu = {}
  for i in range(1, len(options_to_display) + 1):
    choices_menu[i] = options_to_display.pop() 

  print()
  for option_num, option_name in choices_menu.items():
    print(f"{option_num}: {string.capwords(option_name)}")

  return choices_menu

"""Gets and compares user answer to actual answer"""
def get_answer(actual_answer, choices_menu, score, category):
  while True:
    user_answer = input("\n> ")
    if user_answer.isdigit() and 0 < int(user_answer) < len(choices_menu) + 1:
      break
    else:
      print("\nTry again\n")

  if choices_menu[int(user_answer)] == actual_answer:
    print("CORRECTO!")
    score.add_point()
    if category == 'book':
      score.add_point()

  else:
    print("Hmm..")
    sleep(2)
    # print(f"Correct answer: {string.capwords(actual_answer)}")
    print(f"Correct answer: XXXXXXXXXX")
    print("Game over")
    print(f"Score: {score.get_score()}")
    sys.exit(1)



"""Get difficulty mode from user. Modes are just combinations of different time limits and difficulty levels."""
def get_difficulty_mode() -> int:
  print("Choose Difficulty: \n")
  while True:
    difficulty_mode = input("1. Dynamic Difficulty - All's fair in love and war. \n2. Easy but Hard - Let's Dance. \n3. Custom Difficulty.\n> ")
    if difficulty_mode.isdigit() and 0 < int(difficulty_mode) < 4:
      break
    else:
      print("\nIncorrect input (1 - 3).\n")
  difficulty_mode = int(difficulty_mode)
  return difficulty_mode

"""main method"""
def main(difficulty, score):
  # get category, question and answer
  chosen_category, question, actual_answer = create_question_object()
  # get time limit and difficulty level from difficulty object
  time_limit = difficulty.get_time_limit()
  difficulty_level = difficulty.get_difficulty()
  # generate word cloud
  generate_wordcloud(time_limit, chosen_category, question, difficulty_level)

  choices_menu = show_options(chosen_category, actual_answer)
  get_answer(actual_answer, choices_menu, score, chosen_category)
  print(f"Score: {score.get_score()}")

if __name__ == '__main__':
  mode = get_difficulty_mode()
  difficulty = Difficulty(mode)
  score = Score()
  while True:
    difficulty.update(mode)
    main(difficulty, score)