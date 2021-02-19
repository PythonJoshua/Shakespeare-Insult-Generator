import random
from guizero import App, PushButton, Text

def insult_me():
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)
    insult = "Thou " + word_a + " " + word_b + " " + word_c + "!"
    return insult

def new_insult():
    new_insult = insult_me()
    message.value = new_insult

list_a = []
list_b = []
list_c = []

with open("insults.csv", "r") as f:
    for line in f:
        words = line.split(",")
        list_a.append(words[0])
        list_b.append(words[1])
        list_c.append(words[2].strip())

app = App("Shakespearean Insult Generator")
message = Text(app, insult_me() )
button = PushButton(app, new_insult, text="Insult me again")
app.display()