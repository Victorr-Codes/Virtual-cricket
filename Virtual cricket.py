import random

print("\n\t\t\t\t\t\t\t\tWELCOME TO VIRTUAL CRICKET")
print("\t\t\t\t\t\tNOTE - PLEASE WRITE THE RUNS FROM 1,2,3,4,5,6 THESE ONLY\n\n")
x = 0
while(x<1):
    toss = input("Heads or Tails?\n")
    lst2 = ["heads" ,"tails"]
    lst = [1,2,3,4,5,6]
    lst3 = ["Bat" , "Ball"]
    a = random.choice(lst2)
    
    if a==toss:
        print("You won the toss")
        bob = input("Bat or Ball?\n")
        if bob == "bat":
            sum1 = 0
            while(1):
                b = random.choice(lst)
                userBat = int(input("Enter Runs\n"))
                
                if userBat!=b:
                    sum1 = sum1 + userBat
                    print(f"Current run {sum1}")
                    continue
                
                else:
                    print("Out")
                    print(f"Target {sum1}")
                    
                    sum = 0 
                    while(1):
                        b = random.choice(lst)
                        userBat = int(input("Enter the run which may match to  computer's run\n"))
                        
                        if userBat!=b:
                            sum = sum + b
                            print(f"Current run of computer {sum}")
                            if sum1<sum:
                                print("\nYOU LOSE THE MATCH")
                                break
                            

                        else:
                            print("Computer is out")
                            print(f"Computer made {sum} runs")
                            break
                    break


        else:
            sum4 = 0
            while(1):
                b = random.choice(lst)
                userbowl = int(input("Enter the run which may match to computer's run\n"))

                if b != userbowl:
                    sum4 = sum4 + b
                    print(f"Current run of computer {sum4}")
                    continue

                else:
                    print("Computer is out")
                    print(f"Target {sum4}")
                    
                    sum5 = 0
                    while(1):
                        b = random.choice(lst)
                        userBall = int(input("Enter runs\n"))
                
                        if userBall!=b:
                            sum5 = sum5 + userBall
                            print(f"Current run {sum5}")
                            if sum5>sum4:
                                break

                        else:
                            print("Out")
                            print(f"You made {sum5} runs")
                            print("\nYOU LOSE THE MATCH")
                            break
                    break


    else:
        print("You lose the toss")
        d = random.choice(lst3)
        print(f"Computer choose {d}")
        if d == "Bat":
            sum2 = 0
            while(1):
                b = random.choice(lst)
                userbowl = int(input("Enter the run which may match to computer's run\n"))

                if b != userbowl:
                    sum2 = sum2 + b
                    print(f"Current run of computer {sum2}")
                    continue

                else:
                    print("Computer is out")
                    print(f"Target {sum2}")
                    
                    sum3 = 0
                    while(1):
                        b = random.choice(lst)
                        userBall = int(input("Enter runs\n"))
                
                        if userBall!=b:
                            sum3 = sum3 + userBall
                            print(f"Current run {sum3}")
                            if sum3>sum2:
                                break

                        else:
                            print("Out")
                            print(f"You made {sum3} runs")
                            print("\nYOU LOSE THE MATCH")
                            break
                    break

        else:
            sum6 = 0
            while(1):
                b = random.choice(lst)
                userBat = int(input("Enter Runs\n"))
                
                if userBat!=b:
                    sum6 = sum6 + userBat
                    print(f"Current run {sum6}")
                    continue
                
                else:
                    print("Out")
                    print(f"Target {sum6}")
                    
                    sum7 = 0 
                    while(1):
                        b = random.choice(lst)
                        userBat = int(input("Enter the run which may match to computer's run\n"))
                        
                        if userBat!=b:
                            sum7 = sum7 + b
                            print(f"Current run of computer {sum7}")
                            if sum6<sum7:
                                print("\nYOU LOSE THE MATCH")
                                break
                            

                        else:
                            print("Computer is out")
                            print(f"Computer made {sum7} runs")
                            break
                    break

    x = x+1
