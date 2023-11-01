def main():
     print("Which is your favorite meal? Please input below")
     print("1. Chicken")
     print("2. Burger")
     print("3. Pizza")
     answer = int(input())
     meal_test(answer)


def meal_test (answer):
    if answer == 1:
        print ("Chicken is pretty yummy!")
    elif answer == 2:
        print ("I like burgers too, cheeseburgers specifically")
    elif answer == 3:
        print ("Pizza is a classic, but really good choice.")
    else:
        print("That is not an option!")


if  __name__ == "__main__":
     main()
