def run():
    name = input("What is your name? ")
    age = int(input("what is your age? "))

    if age >= 18 and age != 25:
        print(f"Okay {name}, you are old enough to play, lets continue")
        place = input("Which place do you like? (woods/beach) ")
        
        if place == "woods":
            print("I really like this place. Now, solve this problem 1 + 1")
            answer = int(input("What is your answer? "))

            if answer == 2:
                print("Wrong, you lose. Try harder")
            elif answer == "triangle":
                print("Excelent, you solved the riddle")
            else:
                print("You lose")

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