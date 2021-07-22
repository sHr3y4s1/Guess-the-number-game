import random

def game1():
    b="Y"
    while b=="Y":
        a=random.randint(1,100)
        while True:
            num= int(input("Guess the number between the range 1 and 100 (Type 0 to exit): "))
            if num ==0: 
                break        
            if num> a+10:
                print("Go lower")            
            if num< a-10:
                print("Go higher")                        
            if a-10 <= num< a:
                print("Getting closer, a little higher")            
            if a <num<= a+10:
                print("Getting closer, a little lower")   
            if num == a:
                print("BINGO!")
                b=input("Start a new game?(Y/N)").upper()       
                if b=="N":
                    break
        break