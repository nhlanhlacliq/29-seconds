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
import random
from time import sleep
import nltk
from nltk.corpus import stopwords
from PIL import Image
import string
from os import sys
from datalist import DataList
from score import Score
from difficulty import Difficulty
from summary import Summary

"""'plot', 'synopsis', 'text' and 'summary' are all the same thing. basically the description text of the show/book/lyrics"""

"""Countdown timer"""
def countdown_timer(time):
  for i in range(time):
    print(time - i)
    sleep(1)

"""Generates and shows a wordcloud from a chosen category. 
The summary contains the synopsis which the WC is generated from"""
def show_wordcloud(summary_object, difficulty_object):
  # get time limit and difficulty level from difficulty object
  time_limit = difficulty_object.get_time_limit()
  difficulty_level = difficulty_object.get_difficulty()
  # get category and summary from summary object
  category = summary_object.get_category()
  summary = summary_object.get_summary()
  # stop words ("and", "the", "we", etc.)
  stops = set(stopwords.words('english')) #Set used for speed
  more_stops= STOPWORDS
  # will need this for plotting too
  # Make list of words in the summary. dont add word if its a stop word..
  words_in_summary = [word for word in nltk.word_tokenize(summary) if ((word not in stops) and (word not in more_stops))]
  words_freq_dist = nltk.FreqDist(words_in_summary)
  # remove x = {difficulty level} most repeated words, add to clues list
  # clues not yet working.. returns int of word counts instead of actual word
  clues = []
  for i in range(difficulty_level):
    clue = words_freq_dist.pop(words_freq_dist.max())
    clues.append(clue)
  # print(f"These would be the clues {clues}")
  # adjusted summary is summary without x most repeated words 
  adjusted_summary = ''
  for word in words_freq_dist.keys():
    adjusted_summary += word + ' '
  # generate wordcloud from adjusted summary
  wc_rand_state = random.randint(7, 9)
  wc = WordCloud(max_words=500,relative_scaling=0.5,
                background_color='black',stopwords=more_stops,
                margin=2,random_state=wc_rand_state,contour_width=0.5,
                contour_color='white', colormap='Accent')
  wc.generate(adjusted_summary)
  colors = wc.to_array()
  # plotting frequency distribution of words in summary synopsis.. not really needed. I just wanted to see..
  # words_freq_dist.plot(15, linestyle='-', title="LOL words")
  # plt.legend()

  # show wordcloud 
  plt.ion()
  plt.figure()
  plt.title(f"Which {category} is this?\n", fontsize=20, color='black')
  plt.imshow(colors, interpolation="bilinear")
  plt.axis('off')
  plt.show()
  plt.pause(0.001)
  # countdown timer
  countdown_timer(time_limit)
  plt.close(1)
  print("Time's up!")

"""Displays questions. Actual answer, mixed with random questions from same category"""
def display_questions(summary_object):
  category = summary_object.get_category()
  answer = summary_object.get_answer()
  # getattr essentially calls the method using the category(they have the same name)
  category_list = getattr(DataList, category)
  category_list = category_list()
  # add actual answer to questions. add 3 random questions from category
  questions = []
  questions.append(answer)
  while len(questions) < 4:
    random_question = random.choice(category_list)
    if random_question not in questions:
      questions.append(random_question)
  # shuffle questions list. create dictionary representing number : question 
  random.shuffle(questions)
  questions_menu = {}
  for i in range(1, len(questions) + 1):
    questions_menu[i] = questions.pop() 
  # display question menu
  print()
  for question_num, question_name in questions_menu.items():
    print(f"{question_num}: {string.capwords(question_name)}")

  return questions_menu

"""Gets and checks user answer to actual answer. updates score/ ends game if wrong"""
def check_answer(questions_menu, summary_object, score_object):
  while True:
    user_answer = input("\n> ")
    if user_answer.isdigit() and 0 < int(user_answer) < len(questions_menu) + 1:
      break
    else:
      print("\nTry again\n")
  category = summary_object.get_category()
  answer = summary_object.get_answer()
  # if correct, add point
  if questions_menu[int(user_answer)] == answer:
    print("CORRECTO!")
    score_object.add_point()
    if category == 'book':
      score_object.add_point()
  # if wrong, end game. display score
  else:
    print("Hmm..")
    sleep(2)
    # print(f"Correct answer: {string.capwords(actual_answer)}")
    print("Game over")
    print(f"Score: {score_object.get_score()}")
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
def main(difficulty_object, score_object):
  # get category, summary and answer from summary object
  summary_object = Summary()
  category = summary_object.get_category()
  summary = summary_object.get_summary()
  answer = summary_object.get_answer()
  
  # show word cloud of summary, adjust by difficulty
  show_wordcloud(summary_object, difficulty_object)

  # show questions, get and check answer
  questions_menu = display_questions(summary_object)
  check_answer(questions_menu, summary_object, score_object)
  print(f"Score: {score_object.get_score()}")


if __name__ == '__main__':
  mode = get_difficulty_mode()
  difficulty_object = Difficulty(mode)
  score_object = Score()
  while True:
    difficulty_object.update(mode)
    main(difficulty_object, score_object)