# potential negative  to asking if the user will help
negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")

# keywords for exiting the conversation
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

# random starter questions
random_questions = (
    "Why are you here? ",
    "Are there many humans like you? ",
    "What do you consume for sustenance? ",
    "Is there intelligent life on this planet? ",
    "Does Earth have a leader? ",
    "What planets have you visited? ",
    "What technology do you have on this planet?"
)

# Answers to questions the user might ask the alien bot
alienbabble = (
    # Your planet...
    {r'.*\s*your planet':
         ("My planet is a utopia of diverse organisms and species. ",
          "I am from Opidipus, the capital of the Wayward Galaxies. ")
     },
    # why do you...?
    {r'why\sdo\syou\s(.*[^\?]*)\??':
         ("What makes you think I {0}? ",
          "Don't you think I should {0}? ",
          "Who says I {0}? ")
     },
    # why...?
    {r'.*why\s+.*':
         ("That's just the way I've always done it. ",
          "Why do you think {0}? ",
          "Because I said so. ")
     },
    # what...?
    {r'.*what\s+.*':
         ("Why do you ask? ",
          "That's not very polite. ",
          "I don't know. ")
     },
    # it is...
    {r'.*it\s+is':
         ("Your evidence...? ",
          "Are you sure about that? ",
          "Who said? ")
     },
    # I think...
    {r'.*i\s+think\s(.*)[\?\.\!]?':
         ("You think but you're not sure {0}? ",
          "Why do you think {0}? ")
     },
    # Other responses
    {r'.*':
         ("Please tell me more. ",
          "Tell me more! ",
          "Why do you say that? ",
          "I see. Can you elaborate? ",
          "Interesting. Can you tell me more? ",
          "I see. How do you think? ",
          "Why? ",
          "How do you think I feel when you say that? ")
     }
)

# dictionary used to switch pronouns and verbs so responses make sense
reflections = {
    "i'm": "you are",
    "you're": "i'm",
    "was": "were",
    "i": "you",
    "are": "am",
    "am": "are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "I",
    "me": "you"
}
