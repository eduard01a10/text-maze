def run():
    name = input("What is your name? ")
    age = int(input("what is your age? "))

 ## this is the branch "header" also called in development
    if age >= 18 and age != 25:
        print(f"Okay {name}, you are old enough to play, lets continue")
        place = input("Which place do you like? (woods/beach) ")
        
        if place == "woods":
            print("I really like this place. Now, solve this problem 1 + 1")
            answer = int(input("What is your answer? "))
            chances = 5

            while answer >= 0:
                print("Wrong, you lose. Try harder")
                answer += 1

            if answer == "triangle":
                print("Excelent, you solved the riddle")
            else:
                print("You lose")

## This is the "footer"
    elif age == 25:
        print("You are an special player, so let's start an special game")
        like = input("Which of these food do you like most? (lasagna/pizza) ")
        
        if like == "lasagna":
            print("All right, just like Garfield!")
            gar = input("Do you like garfield? yes / no ")
            
            if gar == "yes":
                print("I like it too but sorry this is not the right way. You lose")
            
            else:
                print("Sorry, but this is not the right way, you lose")

        elif like == "pizza":
            pineapple = input("Would you prefer your pizza with or without pizza? ")
            
            if pineapple == "with":
                print("How dare you! but it's okay, I forgive you ")
            
            elif pineapple == "without":
                print("Okay, that's good")
                music = input("What kind of music do you like rock or pop? ")

                if music == "rock":
                    print("Yay! you win!")
                    print("This is your reward https://imgur.com/gallery/Q2gpFhT")
                
                else:
                    print("Sorry, you lose")

            else:
                print("Wrong answer, you lose")

        else:
            print("You lose")

    else:
        print("Sorry you are too young to play")


if __name__ == "__main__":
    run()