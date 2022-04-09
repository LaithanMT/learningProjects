print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("How old are you? "))

health = 10

print("Hello " + name + ", you are " + str(age) + " years old.")

if age >= 18:
    print("You are old enough to play!")

    weapon = input("Pick a weapon (Sword/Baton/Taser): ")
    want_to_play = input("Do you want to play? (Y/N)").upper()
    if want_to_play == "Y":
        print("You are starting with 10 health. Let's play!")

        left_or_right = input("First choice... Left or Right (Left/Right)? ").lower()
        if left_or_right == "left":
            ans = input("Nice. You follow the path around and reach a lake... do you Swim Across or Go Around (Across/Around)? ").lower()
            if ans == "across":
                print("You were bitten by a fish, and you lose 5 points of health")
                health -= 5

            elif ans == "around":
                print("You run around the river, and make it to the other side")

            ans = input("You notice a house and a river. Which do you go to (House/River) ").lower()
            if ans == "house":
                if weapon.lower() == "sword":
                    print("You go to the house, and are greeted by the owner... You slash through him")
                
                elif weapon.lower() == "baton":
                    print("He pushes your baton aside, hits you, and you take 5 points of damage")
                    health -= 5
                
                else:
                    print("He laughs at your weapon, and smashes it out of your hands... you take 5 points of damage")

                if health <= 0:
                    print("Your health is depleted and you lost")

                else:
                    print("Congratulations, you survived!")

            else:
                print("You fell in the river and lost...")

        else:
            print("You fell down and died!")
    else:
        print("Oh... okay.")
else:
    print("You are not old enough to play...")