ans = input("Welcome to the Treasure Island. Your Mission is to find the treasure!! Left or right?: ")
if ans == "left":
    ans = input("Swim or Wait?")
    if ans == "swim":
        ans = input("WHich door? red blue or yellow?")
        if ans == "yellow":
            print("You Win!!")
        else:
            print("You loose")
    else:
        print("You loose")
else:
    print("You loose")