# Linear algebra
# experimenting with linear algebra tools

from invert import inverting




if __name__ == '__main__':
    print(" [1].\n [2].\n [3].\n [4].\n")
    user_cho = int(input("Enter you choice: "))
    while (user_cho <= 0 or user_cho >= 5):
        print("Please pick a correct option")
        user_cho = int(input("Enter you choice: "))

    print("You choice : ",user_cho)

    if user_cho == 1:
        inverting()
    elif user_cho == 2:
        other()
    elif user_cho == 3:
        other()
    elif user_cho == 4:
        other()
    else:
        print("Unknown Option Selected!")


