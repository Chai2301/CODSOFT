def main():
   print("----------------------------")
   print("Simple Calculator")
   print("----------------------------")
   print("1. Add")
   print("2. Subtract")
   print("3. Multiply")
   print("4. Divide")
   print("5. Quit")
   print("----------------------------")

   while True:
      choice=int(input("Enter your choice (1-5):"))
      print("----------------------------")

      if choice==5:
         print("Exiting the program.")
         break
      else:
         if choice in (1,2,3,4):
            val1=float(input("Enter 1st value:"))
            val2=float(input("Enter 2nd value:"))

            if choice==1:
               print("----------------------------")
               print("Add=",val1+val2)  
               print("----------------------------")
            if choice==2:
               print("Subtract=",val1-val2)
               print("----------------------------")
            if choice==3:
               print("Multiply=",val1*val2)
               print("----------------------------")
            if choice==4:
               print("Divide=",val1/val2)
               print("----------------------------")

# main program
main()