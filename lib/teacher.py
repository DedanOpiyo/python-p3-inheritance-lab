#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]


    # def validRandom(self): # import random
    #     while True:
    #         random_no = random() * 10 
    #         if 0 <= random_no <=7:
    #             return random_no

    def teach(self):
        list_index = random.randint(0, len(self.knowledge)-1)
        return self.knowledge[list_index]
    
# Test
john = Teacher("John", "Johhanah")
# print(john.first_name)
print(john.teach())