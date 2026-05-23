import random

def details(result: str) -> None:
   print("-"*len(a))
   print("Computer chose:", choices[comp])
   print("You chose:", choices[user])
   print("\nResult:", result)
   print("-"*len(a))
def showError() -> None:
   print("-"*len(a))
   print("\nError 404: Option Not Found!!\n") 
   print("-"*len(a))
    
print(a := "-:| Stone Paper Scissors |:-")
print("-"*len(a))
print("1) Stone")
print("2) Paper")
print("3) Scissors")
print("-"*len(a))

choices = {1 : "Stone", 2 : "Paper", 3 : "Scissors"}
results = ["You Won!", "Computer won!", "It's a Draw!"]
points_comp = 0
points_user = 0
rounds = 0

while rounds < 7:
   try:
       user = int(input("Choose one(nums): "))
       comp = random.randint(1, 3)
    
       if user in [1, 2, 3]:        
           if user == comp:
               details(results[2])
               print(f"Rounds Played: {rounds}/7\n")
            
           elif comp - user == 1 or user - comp == 2:
               details(results[1])
               points_comp += 1
               rounds += 1
               print(f"Rounds Played: {rounds}/7\n")
            
           else:
               details(results[0])  
               points_user += 1
               rounds += 1
               print(f"Rounds Played: {rounds}/7\n")  
       else:
           showError()
   except ValueError:
       showError()
        
print("-"*len(a))
print("Computer's score:", points_comp)
print("Your score:", points_user)
if points_user > points_comp:
    print("\nFinal Result: You Win!!") 
else:
    print("\nFinal Result: Computer Wins!!")  
    
print("-"*len(a)) 