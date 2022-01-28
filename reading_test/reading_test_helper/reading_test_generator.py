import random
import itertools
from typing import List


class ReadingTestGenerator():

    def __init__(self):
        pass


    def generate_reading_test_ids(self):
        NUM_TESTS = 10
        choices = random.choices(range(NUM_TESTS), k = 3)
        return choices
