def calculate_bmi(height, weight):
    print("height = " + str(height))
    print("weight = " + str(weight))
    bmi = weight / (height * height)
    print("bmi = " + str(bmi))

    if(bmi < 18.5):
        print("under weight")
    elif(bmi >= 18.5 and bmi <= 25.0):
        print("normal weight")
    else:
        print("over weight")

calculate_bmi(weight=57, height=1.73)