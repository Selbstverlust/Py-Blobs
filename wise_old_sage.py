import random

# Answer is declared blank so it can be modified later.
answer = ""

# Name and questions are modified to affect the little back-story told to the user.
name = "Selbstverlust"
question = "Should I start from scratch?"

# Random number generator that ranges from 1 to 9, the int is used later to define which answer will be given back to the user.
random_number = random.randint(1,9)

# If the random number generated is between 1 and 9 it has different answers for every number, in the case that the number is outside that range, the sage ponders if existence is somehow broken.
if random_number == 1:
  answer = "The spirits are clear, the answer is yes, child."
elif random_number == 2:
  answer = "The stars have decided so, child."
elif random_number == 3:
  answer = "Without a doubt, child."
elif random_number == 4:
  answer = "The stars are hazy, return on a cloudless night and ask again, child."
elif random_number == 5:
  answer = "You should reflect on your question and ask again later, child."
elif random_number == 6:
  answer = "It is better for you to not know, child."
elif random_number == 7:
  answer = "The spirits say no, child."
elif random_number == 8:
  answer = "The outlook is not so good, child."
elif random_number == 9:
  answer = "Very doubtful, child."
else:
  answer = "Something is wrong with existence. Ask again later, child."

# Leaving name as an empty string treats the user as a disembodied voice asking the sage a question. Leaving the question empty, makes the sage ponder when someone will ask him a question.
if question != "":
  if name == "":
    print("A nameless voice carried by the wind asks the Wise Old Sage: " + question)
    print("And the Wise Old Sage anwers: " + answer)
  else:
    print(name + " asks the Wise Old Sage: " + question)
    print("And the Wise Old Sage anwers: " + answer)
else:
  print("A breeze goes by the Wise Old Sage, and he wonders when someone will next ask him a question.")
