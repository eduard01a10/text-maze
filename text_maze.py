def chance():  ## This function is for the woods part
    chances = 4
    

    while chances >= 0:
        answer = input("What is your answer? ")

        if answer == "2":
            print(f"Wrong answer, you have {chances} chances left")
        elif answer == "triangle" or answer == "paris".lower():
            print("You win!")
            break
        else:
            print(f"Wrong answer, you have {chances} chances left")
        
        chances -= 1

def run():
    name = input("What is your name? ")
    age = int(input("what is your age? "))

 ## this is the branch "header" also called in development
    if age >= 18 and age != 25:
        print(f"Okay {name}, you are old enough to play, lets continue")
        place = input("Which place do you like? (woods/beach) ")
        
      ## Here it begins the part of the woods  
        if place == "woods":
            print("I really like this place. Now, solve this problem 1 + 1")
            print("You just have 5 chances")
            
            chance()

      ## Here it begins the part of the beach  
        elif place == "beach":
            print("I don't really like this place, but anyway, pick a number")
            
            for i in range(1, 11):
                print(i)
                
            choice = int(input("Which one do you like? "))

            if choice >= 0 and choice <= 5:
                print("You have to answer a little question. What is the capital of France?")

                chance()

            elif choice >= 5 and choice <= 10:
                vinci = ["Da vinci", "davinci", "Da Vinci", "da vinci"]
                answer = input ("Ok, now you have to answer who painted the mona lisa? ")
                if answer in vinci:
                    print("That's right! You have learned a lot and now, you have to do one more task")
                    space = input("Do you think that the moonlanding was true or false? ")
                    if space == "true":
                        print("You are a truly scientist and you need to win, so, here is your reward: https://imgur.com/gallery/dBUZ3Ig")
                    else:
                        print("Wrong asnwer, you lose")
                else:
                    print("Wrong, start the program again")
                 

                

    elif age == 25:
        print("You are an special player, so let's start an special game")
        like = input("Which of these food do you like most? (lasagna/pizza) ")
        
        if like == "lasagna":
            pass
        else:
            pass

    else:
        print("Sorry you are too young to play")


if __name__ == "__main__":
    run()