#Madlibs Game
# This program creates a simple Madlibs game where the user inputs words to fill in the blanks of a story.

print("Welcome to the Madlibs Game!")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

story = f"Once upon a time, a {adjective} {noun} {verb} {adverb}."
print(story)
