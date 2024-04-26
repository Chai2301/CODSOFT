# import random module
import random
# Below are the instructions to play the game
print('Rules for the game ROCK PAPER SCISSORS are :\n'
      "--------------------------------------------------\n"
      "  Rock vs Paper --> Paper wins \n"
      "  Rock vs Scissors --> Rock wins \n"
      "  Paper vs Scissors --> Scissor wins \n",sep="   ")
     
def main():
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("4. Exit")
    print("---------------------------------")

    while True:
         # ---------User statements----------------
         user_choice=int(input("Enter Your Choice (1-4):"))
         print("-"*30)

         if user_choice==1:
             print("USER CHOICE: Rock")
         elif user_choice==2:
             print("USER CHOICE: Paper")
         elif user_choice==3:
             print("USER CHOICE: Scissor")
         elif  user_choice==4:
             break
         else:
             print("Please enter a valid Choice!!")

         # ---------Computer statements---------------
         comp_choice=random.randint(1,3)

         if comp_choice==1:
             print("COMPUTER CHOICE: Rock")
         elif comp_choice==2:
             print("COMPUTER CHOICE: Paper")
         else:
             print("COMPUTER CHOICE: Scissor")
         
         # --------condition for Draw--------------
         if user_choice==comp_choice:
             print("Its a Draw!!")
         
         # ----------condition for winning--------------
         if user_choice==1 and comp_choice==2:
             print("-"*30)
             print("Computer Wins!!")
             print("-"*30)
         elif user_choice==2 and comp_choice==1:
             print("-"*30)
             print("User Wins!!")
             print("-"*30)         

         if user_choice==1 and comp_choice==3:
             print("-"*30)
             print("User Wins!!")
             print("-"*30)
         elif user_choice==3 and comp_choice==1:
             print("-"*30)
             print("Computer Wins!!")
             print("-"*30)

         if user_choice==2 and comp_choice==3:
             print("-"*30)
             print("Computer Wins!!")
             print("-"*30)
         elif user_choice==3 and comp_choice==2:
             print("-"*30)
             print("User Wins!!")
             print("-"*30)

main()
print("Thankyou For Playing, I hope u enjoyed!!")
             
     