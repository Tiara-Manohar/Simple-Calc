#Simple calculator in Python

def selection():
    global num_1, num_2, operations
    while True:
        try:
            num_1 = float(input("Enter a number: "))
        except ValueError:
           print("Sorry, I did not understand")
           continue
        else:
           break
   
    while True:
        try:   
            operations = input("Enter an operation(+, -, *, /): ")
        except ValueError:
            print("Invalid Operation")
            continue
        else:
            break
            # if operations in ['+', '-', '*', '/']:
                
              
    while True:
      try:
            num_2 = float(input("Enter a number: "))
      except ValueError:
            print("Sorry, I don't understand")
            continue
      else:
          break

def calculate():
    if operations == "+":
        print("Total: {} + {} = {}".format(num_1, num_2, num_1 + num_2))
    elif operations == "-":
        print("Total: {} - {} = {}".format(num_1, num_2, num_1 - num_2))
    if operations == "*":
        print("Total: {} * {} = {}".format(num_1, num_2, num_1 * num_2))
    elif operations == "/":
            try:
               print("Total: {} / {} = {}".format(num_1, num_2, num_1 / num_2))
            except ZeroDivisionError:
                print("Divison by 0 is impossible")
    else: 
         choice = input("Do you want to contiue calculating?[y,n]: ")
         if choice.lower() == "y":
                selection(), calculate()
         elif choice.lower() == "n":
                print("Goodbye!")
    exit
      
       

__name___ = "__main__"
selection()
calculate()



