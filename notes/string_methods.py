# LV 2nd methods notes

name = input("What is your name").strip().title()
# .lower() => makes it all lower case
# .upper() => all upper case
# .capitalize => capitalize the first letter
# .title() => capitalizes the first letter of every word
age = int(input("Bro how old are you?"))

print("Hello {}, it is nice to meet you! I can't believe you are {:.2f}!".format(name,age))

print(f"Hello {name}, it is nice to meet you! I can't believe you are {age:.1f}!")


# print(age.isdigit())

#print("Really? " + age + "is old")

sentence = "The quick brown fox jumps over te lazy dog!"

word="brown"
start= sentence.find("fox")
length = len("fox")


print(sentence.replace(word, "yellow"))
