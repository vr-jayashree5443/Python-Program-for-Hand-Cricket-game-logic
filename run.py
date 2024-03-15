  
import random
import math

#func1
def score(bat,bowl,innings,user_score,computer_score):
    user_=0
    computer_=0
    #for score >
    
    i=0
    while(True):
        print("Ball: ",i)
        u=int(input())
        if 1<=u<=6:
            user_=user_+u
        c=random.randint(1,6)
        computer_=computer_+c
        #got ball1 fro user and computer
        if u==c:
            user_=user_-u
            computer_=computer_-c
            break
        if innings==2:
            if bat==0:
                if user_>computer_score:
                    
                    break
            if bat==1:
                if computer_>user_score:
                    
                    break
            
        i+=1
    if bat==0:
        user_score=user_
        if innings==1:
            print(f"Your score:{user_score} Computer's Target:{user_score+1}")
        else:
            print(f"Your score:{user_score} ")
    elif bat==1:
        computer_score=computer_  
        if innings==1:
            #in 2nd innings no need to print target
            print(f"Computer's score:{computer_score} Your Target:{computer_score+1}")
        else:
            print(f"Computer's score:{computer_score}")
    return user_score, computer_score




  #func2
def Hand_Cricket():
    #user-0
    #computer-1
    print("Toss: Odd or Even")
    user_toss=input().lower()
    if user_toss=="odd":
        computer_toss="even"
        #identify who odd, who even
        even=1
        odd=0
    else:
        computer_toss="odd"
        #identify who odd, who even
        even=0
        odd=1
    #got user toss
    #got computer toss

    print("Choose 1-6")
    user=int(input())
    computer=random.randint(1,6)
    total_toss_value=user+computer
    choices=["bat","bowl"]
    
    if total_toss_value%2==0:
    #even
        if even==0:
            #user wins toss
            print("You won the toss")
            print("Opt to: bat or bowl")
            user_choice=input().lower()
            
            if user_choice=="bat":
                computer_choice=choices[1]
                bat=0
                bowl=1
            else:
                computer_choice=choices[0]
                bat=1
                bowl=0
        else:
            print("Computer won the toss", end="")
            computer_choice=random.choice(choices)
            if computer_choice==choices[0]:
                user_choice=choices[1]
                print("and opted to bat")
                bat=1
                bowl=0
            else:
                user_choice=choices[0]
                print("and opted to bowl")
                bat=0
                bowl=1
    else:
    #odd
        if odd==0:
            #user wins toss
            print("You won the toss")
            print("Opt to: bat or bowl")
            user_choice=input().lower()
            choices=["bat","bowl"]
            if user_choice==choices[0]:
                computer_choice=choices[1]
                bat=0
                bowl=1
            else:
                computer_choice=choices[0]
                bat=1
                bowl=0
        else:
            print("Computer won the toss", end="")
            computer_choice=random.choice(choices)
            if computer_choice==choices[0]:
                print("and opted to bat")
                user_choice=choices[1]
                bat=1
                bowl=0
            else:
                user_choice=choices[0]
                print("and opted to bowl")
                bat=0
                bowl=1
    #got user choice
    #got compuer choice
    #bat or bowl
    print("Lets Play")
    #user_, computer_ for adding purpose
    user_score, computer_score=0,0
    
    user_score, computer_score=score(bat,bowl,1,user_score, computer_score)
    #call function 
    
    #1 innings over
    #interval
    print(" Lets Play 2nd Innings")
    bat,bowl=bowl,bat
    if bat==0:
        print("You bat")
    else:
        print("You bowl")
    
    user_score, computer_score=score(bat,bowl,2,user_score, computer_score)
    runs=abs(user_score-computer_score)
    wickets=1
    if user_score>computer_score:
        winner=1
        if bat==0:
            #2nd batsman
            print(f"You won by {wickets} wicket")
        else:
            #2nd bowl
            print(f"You won by {runs} runs")
    elif user_score<computer_score:
        winner=2
        if bat==0:
            #2nd batsman-us
            #computer-1st batsman
            print(f"Computer won by {runs} runs")
            
        else:
            #2nd bowl
            #computer-1st bowl
            print(f"Computer won by {wickets} wicket")
    else:
        winner=0
        print("Its a draw")
    
    return winner
    #winner-0--draw, 1-user,2-pc
            
#final loop with fuction call
print("No of matches")
win_matches={'user':0,'computer':0,'draw':0}
points_table={'user':0,'computer':0}
n=int(input())
w=0
for i in range(n):
    print(f"i val is{i}")
    if i>=1:
        print("Do you want to continue to next match?: Y/n ")
        inp=input().lower()
        if inp=="n":
            break
        
    w=Hand_Cricket()
    if w==1:
        win_matches['user']=win_matches['user']+1
        points_table['user']=points_table['user']+1
    elif w==2:
        win_matches['computer']=win_matches['computer']+1
        points_table['computer']=points_table['computer']+1
    elif w==0:
        win_matches['draw']=win_matches['draw']+1
        points_table['computer']=points_table['computer']+0.5
        win_matches['user']=win_matches['user']+0.5
    print("Do you want to continue to next match?")
print(f"Final points table:{points_table}")        
