from random import randint
from PIL import Image, ImageDraw
import os

GRIDSIZE = 5
STUDENTS_NUM = 3

def get_words(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return lines

words = get_words("words.txt")

for student in range(STUDENTS_NUM):
    filename = "student_" + str(STUDENTS_NUM + 1) + ".png"
    image = Image.new(mode = "")
    cards = set()
    while len(cards) < 25:
        cards.add(words[randint(0, len(words) - 1)])
    print(*cards, end="\n\n")