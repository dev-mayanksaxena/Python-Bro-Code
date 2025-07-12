#Madlibs Game
# This program creates a simple Madlibs game where the user inputs words to fill in the blanks of a story.

print("Welcome to the Madlibs Game!")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

place = input("Enter a place: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")

story = (
	f"Once upon a time in {place}, a {adjective} {noun} decided to {verb} {adverb}. "
	f"Along the way, it met a {animal} who was feeling very {emotion}. "
	f"Together, they went on an adventure that changed their lives forever!"
)
print(story)
