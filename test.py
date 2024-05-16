# ID verification program for data Analytics class
def process_int(x):
   match x:
      case 3:
         print("Assalam-o-Alikum! Muhammad Hamza. Welcome to the data analysis class")
      case 4:
         print("Assalam-o-ALikum! Muhammad Awais. Welcome to the data analysis class")
      case 11:
         print("Assalam-o-ALikum! Muhammad Raees. Welcome to the data analysis class")
      case x:
         print("Assalam-o-Alikum! Sorry You are not eligible to enter")

input_int: int = int(input("Enter a Roll no: "))
process_int(input_int)