import random

name = "Selbstverlust"
question = "Should I start from scratch?"
answer = ""

random_number = random.randint(1,9)

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

if question != "":
  if name == "":
    print("A nameless voice carried by the wind asks the Wise Old Sage: " + question)
    print("And the Wise Old Sage anwers: " + answer)
  else:
    print(name + " asks the Wise Old Sage: " + question)
    print("And the Wise Old Sage anwers: " + answer)
else:
  print("A breeze goes by the Wise Old Sage, and he wonders when someone will next ask him a question.")
