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
import random
from time import sleep
import nltk
from nltk.corpus import stopwords
from PIL import Image

"""'plot', 'synopsis', 'text' and 'question' are all the same thing. basically the description text of the show/book/lyrics"""

"""Generates a wordcloud from a chosen category. the question contains the synopsis which the WC is generated from"""
def generate_wordcloud(time_to_answer, category, question, difficulty_level):
  # 
  words_freq_dist = {}
  # plt.figure(2)
  stops = set(stopwords.words('english')) #Set used for speed
  more_stops= STOPWORDS
  # will need this for plotting too
  words_in_question = [word for word in nltk.word_tokenize(question) if ((word not in stops) and (word not in more_stops))]
  words_freq_dist = nltk.FreqDist(words_in_question)

  # remove {difficulty level} most counted words, add to clues list
  clues = []
  for i in range(difficulty_level):
    clues.append(words_freq_dist.pop(words_freq_dist.max()))
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
  plt.show(block=True)
  # plt.savefig('WC.png')
  # wc_image = Image.open('WC.png')
  # wc_image.show()

  sleep(time_to_answer)
  print("Eyh!!!")
  plt.close(1)

"""Gets user category choice. returns category, with a random question and answer from that category """
def setup() -> set:
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

  # Get difficulty level
  while True:
    difficulty_level = input("Difficulty level (0 - 4):\n> ")
    if difficulty_level.isdigit() and -1 < int(category_choice) < 5:
      break
    else:
      print("\nTry again (0 - 4).\n")

  # getattr essentially calls the menthod using the chosen category(they have the same name)
  category_dict_method_to_call = getattr(InfoDatabase, chosen_category)
  category_dict = category_dict_method_to_call()
  choice_from_category_dict = random.choice(list(category_dict.items()))
  question = choice_from_category_dict[1]
  actual_answer = choice_from_category_dict[0]

  return chosen_category, question, actual_answer, int(difficulty_level)

"""Displays choices"""
def show_options(chosen_category):
  pass

"""Gets and compares user answer to actual answer"""
def get_answer(actual_answer):
  pass

"""main method"""
def main(time_to_answer):
  chosen_category, question, actual_answer, difficulty_level = setup()
  generate_wordcloud(time_to_answer, chosen_category, question, difficulty_level)

if __name__ == '__main__':
  main(3)