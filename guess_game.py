import random
win=0
lose=0
while True:
    
    level=int(input("Enter the length of the word you would like to guess(4-10)or press 0 for quit: "))
        
    if level==0:
        print(f"no of matches won {win}")
        print(f"no of matches lose {lose}")
        break
    with open("words.txt", "r",) as file:
        words = [line.strip() for line in file if line.strip()]

    matching_words = [word for word in words if len(word) == level]

    if not matching_words:
        print("No words available for this length")
        continue

    secret_word = random.choice(matching_words)

    space=["_" for i in range(len(secret_word))]
    print(space)
    guess=0
    hint=0


    while True:
        letter=input("Enter a letter and HINT for hint : ").strip().lower()
        if len(letter) == 1 and letter.isalpha():   
            if letter in secret_word :
                print("Good guess")
                i=0
                for j in secret_word:
                    if j==letter:
                        space[i]=letter
                    i+=1
                print("".join(space))

        elif letter=="hint":
            
            if hint==1:
                print("Sorry no more hints")
                continue
            j=0
            for i in space:
                
                if i =="_":
                    space[j]=secret_word[j]
                    print("".join(space))
                    hint=1
                    break
                j+=1
            
        else:
            print("Please enter exactly one letter")
            continue

        if letter!="hint" and letter not in secret_word:
            guess+=1
            if guess>6:
                print("You lose ,you have used all your 6 attempts")
                lose+=1
                print(f"{secret_word} was the answer")
                break
            print("Wrong guess")
            print(f"guesses left {6-guess}")

        if "_" not in space:
            print("You won")
            win=win+1    
            break
