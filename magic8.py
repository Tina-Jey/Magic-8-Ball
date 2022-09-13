name = "Sky"
question = "Will it rain tomorrow?"
anwser = ""
import random

random_number = random.randint(1, 10)
print(random_number)

if random_number == 1:
  anwser = "Yes - definitely"
elif random_number == 2:
  anwser = "It is decidedly so"
elif random_number == 3:
  anwser = "Without a doubt"
elif random_number == 4:
 anwser = "Reply hazy, try again."
elif random_number == 5:
  anwser = "Ask again later."
elif random_number == 6:
  anwser = "Better not tell you now."
elif random_number == 7:
  anwser = "My sources say no."
elif random_number == 8:
  anwser = "Outlook not so good."
elif random_number == 9:
  anwser = "Very doubtful."
elif random_number == 10:
  anwser = "Shake the ball again."
else:
  anwser = "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + anwser)