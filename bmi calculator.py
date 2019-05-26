while True:
    while True:
        weight_input = input("What is your weight in pounds?    ")
    
        if weight_input.isdigit():
            print ("Thanks.")
            break
        else:
          print("That's not a number for weight")
          continue
   
    while True:
         height_input = input("What is your height in inches?    ")
         if height_input.isdigit():
             print("thanks.")
             break
            
    
         else:
           print("That's not a number for height.")
           continue
    weight_input = float(weight_input)
    height_input = float(height_input)
    bmi = (weight_input/(height_input**2))*703
    print ("Your BMI is  " + str(bmi))
