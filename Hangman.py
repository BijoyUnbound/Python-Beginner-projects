import random

words = ["apple", "bridge", "cloud", "dragon", "echo", "forest", "galaxy", "harbor", 
         "island", "jungle", "knight", "lantern", "mountain", "nebula", "ocean", 
         "puzzle", "quartz", "river", "storm", "thunder", "umbrella", "voyage", 
         "whisper", "xenon", "yellow", "zenith"]

random_words = random.choice(words)

print(a:="-:| Hangman |:-")
print("-"*len(a))

blanks = ["-" for i in random_words]
used_letters = set()
print(f"Hidden Word: | {" ".join(blanks)} |\n")

tries = 10
while tries > 0:
    
    if " ".join(blanks) == " ".join(random_words):
        print("Yay!, You've completed it!")
        break
            
    guess = input("Enter a letter: ").lower()
    if guess.isalpha() or len(guess) == 0:
        if guess in used_letters:
            print(f"{guess} is used already, try another")
        
        used_letters.add(guess)
        
        if guess in random_words:
            for k, i in enumerate(random_words):
                if guess == i:
                    blanks[k] = guess
            print(f"\nHidden Word: | {" ".join(blanks)} |\n")
            
        else:
            print(f"Hidden Word: | {" ".join(blanks)} |\n")
            print("Wrong guess, try again!")
            tries -= 1
            print(f"[Tries Left: {tries}]")
    else:
        print("\nInvalid Input!!)")     