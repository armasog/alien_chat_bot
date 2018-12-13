import re
import random
import config

name = ""

# Define greet() below:
def greet():
    name = input("What's your name Earthling?")
    will_help = input(
        "Hi {}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? ".format(name))
    if will_help in config.negative_responses:
        print('Ok bye')
        return False
    else:
        return True


# Define make_exit() here:
def make_exit(reply):
    for command in config.exit_commands:
        if command in reply:
            print('Ok Bye')
            return True


# Define alienbot() next:
def alienbot():
    if greet():
        reply = input(random.choice(config.random_questions)).lower()
        while not make_exit(reply):
            reply = converse(reply)


# Define converse() below:
def converse(reply):
    for pair in config.alienbabble:
        for regex_pattern, alien_answers in pair.items():
            found_match = re.match(regex_pattern, reply)
            if found_match:
                alien_answer = random.choice(alien_answers)
                formatted_alien_answer = alien_answer.format(*[reflect(matching_group) for matching_group in found_match.groups()])
                reply = input(formatted_alien_answer).lower()
                return reply

def reflect(response):
    words = response.split()
    for index, word in enumerate(words):
        if word in config.reflections:
            words[index] = config.reflections[word]
    return ' '.join(words)


alienbot()
