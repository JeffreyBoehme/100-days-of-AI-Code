while True:
    year = int(input("Which year do you want to check? "))
    if year % 4 == 0:  # true
        if year % 100 == 0:  # not true
            if year % 400 == 0:  # true
                print("Leap Year!")
            else:
                print("Not Leap Year!")
        else:
            print("Leap Year!")
    else:
        print("Not Leap Year!")
