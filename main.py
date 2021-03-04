import requests
import bs4
from nltk.tokenize import sent_tokenize
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

def main():
  chosen_category, question, actual_answer = setup()

  stopwords = STOPWORDS
  stopwords.update(['Lil Wayne', 'Static Major', 'Lollipop', 'Lil', 'Wayne', 'Static', 'Major', 'Tanya'])

  wc = WordCloud(max_words=500,relative_scaling=0.5,
                background_color='white',stopwords=stopwords,
                margin=2,random_state=7,contour_width=0.5,
                contour_color='brown', colormap='copper').generate(question)

  colors = wc.to_array()

  plt.figure()
  plt.title(f"Which {chosen_category} is this?\n",
  fontsize=15, color='black')
  plt.imshow(colors, interpolation="bilinear")
  plt.axis('off')
  plt.show()
  ##plt.savefig('hound_wordcloud.png')

def setup():
  
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
  categories_menu = {1: 'anime', 
  2: 'books'}
  chosen_category = categories_menu[int(category_choice)]

  # as you can see getattr essentially calls the menthod
  category_dict_method_to_call = getattr(InfoDatabase, chosen_category)
  category_dict = category_dict_method_to_call()
  choice_from_category_dict = random.choice(list(category_dict.items()))
  question = choice_from_category_dict[1]
  actual_answer = choice_from_category_dict[0]

  # print(actual_answer)
  return chosen_category, question, actual_answer




if __name__ == '__main__':
  main()