import os, sys, random, csv, getpass, platform

gamename = "Rolling Dice Game"

os.system('cls' if os.name == 'nt' else 'clear')
if platform.system() == "Linux":
    os.system("PROMPT_COMMAND='echo -ne \"\033]0;"+gamename+"\007\"'")
else:
    os.system('title '+gamename if os.name == 'nt' else 'title="'+gamename+'" && echo -n -e "\033]0;$title\007"')

P1acc = ""
P2acc = ""
P1s = 0
P2s = 0

import csv

data={}
with open('accdb.csv') as fin:
    reader=csv.reader(fin, skipinitialspace=True, quotechar="'")
    for row in reader:
        data[row[0]]=row[1:]

def run():
    print("Welcome to the rolling dice game")

    print("Player 1:")
    print("login or signup")
    ans = ""
    ans = input("Command: ")
    while ans not in ("login","signup"):
        ans = input("Command: ")

    if (ans == "login"):
        uname = input("Username: ")
        if uname in data["uname"]:
            uid = data["uname"].index(uname)
            pwd = getpass.getpass()
            if pwd == data["password"][uid]:
                a = input(data["q"][uid])
                if data["a"][uid] == a:
                    print("Player 1 logged in.")
                    P1acc = data["uname"][uid]
                else:
                    print("Incorrect password.")
                    run()
                    return
            else:
                print("Incorrect Password.")
                run()
                return
        else:
            print("User does not exist")
            run()
            return
    elif (ans == "signup"):
        uname = input("Username: ")
        pwd = getpass.getpass()
        q = input("Security Question: ")
        a = input("Answer: ")
        open("accdb.csv", "w").close()
        with open('accdb.csv', 'w') as f:
            u = "uname,"+",".join(data["uname"])
            p = "password,"+",".join(data["password"])
            q = "q,"+",".join(data["q"])
            a = "a,"+",".join(data["a"])
            f.write(u+"\n"+p+"\n"+q+"\n"+a)
    print("Player 2:")
    print("login or signup")
    ans = ""
    ans = input("Command: ")
    while ans not in ("login","signup"):
        ans = input("Command: ")

    if (ans == "login"):
        uname = input("Username: ")
        if uname in data["uname"]:
            uid = data["uname"].index(uname)
            pwd = getpass.getpass()
            if pwd == data["password"][uid]:
                a = input(data["q"][uid])
                if data["a"][uid] == a:
                    print("Player 2 logged in.")
                    P2acc = data["uname"][uid]
                else:
                    print("Incorrect password.")
                    run()
                    return
            else:
                print("Incorrect Password.")
                run()
                return
        else:
            print("User does not exist")
            run()
            return
    elif (ans == "signup"):
        uname = input("Username: ")
        pwd = getpass.getpass()
        q = input("Security Question: ")
        a = input("Answer: ")
        open("accdb.csv", "w").close()
        with open('accdb.csv', 'w') as f:
            u = "uname,"+",".join(data["uname"])
            p = "password,"+",".join(data["password"])
            q = "q,"+",".join(data["q"])
            a = "a,"+",".join(data["a"])
            f.write(u+"\n"+p+"\n"+q+"\n"+a)
    print("Round 1")
    print("Enter 'roll' to roll.")
    print("Player 1's turn.")
    ans = ""
    ans = input("Command: ")
    while ans not in ("roll","exit"):
        ans = input("Command: ")
    if ans == "roll":
        dice = (random.randint(1,6),random.randint(1,6))
        print("Player 1 rolled a "+str(dice[0])+" and a "+str(dice[1]))
        if dice[0]+dice[1] in (2,4,6):
            P1s + 10
        elif dice[0]+dice[1] in (1,2,3):
            P1s - 5
        if P1s < 0:
            P1s = 0
    elif ans == "exit":
        exit()
    print("Player 2's turn.")
    ans = ""
    ans = input("Command: ")
    while ans not in ("roll","exit"):
        ans = input("Command: ")
    if ans == "roll":
        dice = (random.randint(1,6),random.randint(1,6))
        print("Player 2 rolled a "+str(dice[0])+" and a "+str(dice[1]))
        if dice[0]+dice[1] in (2,4,6):
            P2s + 10
        elif dice[0]+dice[1] in (1,2,3):
            P2s - 5
        if P2s < 0:
            P1s = 0
    print("Round 1 over.")
    print("Round 2")
    print("Enter 'roll' to roll.")
    print("Player 1's turn.")
    ans = ""
    ans = input("Command: ")
    while ans not in ("roll","exit"):
        ans = input("Command: ")
    if ans == "roll":
        dice = (random.randint(1,6),random.randint(1,6))
        print("Player 1 rolled a "+str(dice[0])+" and a "+str(dice[1]))
        if dice[0]+dice[1] in (2,4,6):
            P1s + 10
        elif dice[0]+dice[1] in (1,2,3):
            P1s - 5
        if P1s < 0:
            P1s = 0
    elif ans == "exit":
        exit()
    print("Player 2's turn.")
    ans = ""
    ans = input("Command: ")
    while ans not in ("roll","exit"):
        ans = input("Command: ")
    if ans == "roll":
        dice = (random.randint(1,6),random.randint(1,6))
        print("Player 2 rolled a "+str(dice[0])+" and a "+str(dice[1]))
        if dice[0]+dice[1] in (2,4,6):
            P2s + 10
        elif dice[0]+dice[1] in (1,2,3):
            P2s - 5
        if P2s < 0:
            P1s = 0
    print("Round 2 over.")
    print("Round 3")
    print("Enter 'roll' to roll.")
    print("Player 1's turn.")
    ans = ""
    ans = input("Command: ")
    while ans not in ("roll","exit"):
        ans = input("Command: ")
    if ans == "roll":
        dice = (random.randint(1,6),random.randint(1,6))
        print("Player 1 rolled a "+str(dice[0])+" and a "+str(dice[1]))
        if dice[0]+dice[1] in (2,4,6):
            P1s + 10
        elif dice[0]+dice[1] in (1,2,3):
            P1s - 5
        if P1s < 0:
            P1s = 0
    elif ans == "exit":
        exit()
    print("Player 2's turn.")
    ans = ""
    ans = input("Command: ")
    while ans not in ("roll","exit"):
        ans = input("Command: ")
    if ans == "roll":
        dice = (random.randint(1,6),random.randint(1,6))
        print("Player 2 rolled a "+str(dice[0])+" and a "+str(dice[1]))
        if dice[0]+dice[1] in (2,4,6):
            P2s + 10
        elif dice[0]+dice[1] in (1,2,3):
            P2s - 5
        if P2s < 0:
            P1s = 0
    print("Round 3 over.")
    print("Round 4")
    print("Enter 'roll' to roll.")
    print("Player 1's turn.")
    ans = ""
    ans = input("Command: ")
    while ans not in ("roll","exit"):
        ans = input("Command: ")
    if ans == "roll":
        dice = (random.randint(1,6),random.randint(1,6))
        print("Player 1 rolled a "+str(dice[0])+" and a "+str(dice[1]))
        if dice[0]+dice[1] in (2,4,6):
            P1s + 10
        elif dice[0]+dice[1] in (1,2,3):
            P1s - 5
        if P1s < 0:
            P1s = 0
    elif ans == "exit":
        exit()
    print("Player 2's turn.")
    ans = ""
    ans = input("Command: ")
    while ans not in ("roll","exit"):
        ans = input("Command: ")
    if ans == "roll":
        dice = (random.randint(1,6),random.randint(1,6))
        print("Player 2 rolled a "+str(dice[0])+" and a "+str(dice[1]))
        if dice[0]+dice[1] in (2,4,6):
            P2s + 10
        elif dice[0]+dice[1] in (1,2,3):
            P2s - 5
        if P2s < 0:
            P1s = 0
    print("Round 4 over.")
    print("Round 5")
    print("Enter 'roll' to roll.")
    print("Player 1's turn.")
    ans = ""
    ans = input("Command: ")
    while ans not in ("roll","exit"):
        ans = input("Command: ")
    if ans == "roll":
        dice = (random.randint(1,6),random.randint(1,6))
        print("Player 1 rolled a "+str(dice[0])+" and a "+str(dice[1]))
        if dice[0]+dice[1] in (2,4,6):
            P1s + 10
        elif dice[0]+dice[1] in (1,2,3):
            P1s - 5
        if P1s < 0:
            P1s = 0
    elif ans == "exit":
        exit()
    print("Player 2's turn.")
    ans = ""
    ans = input("Command: ")
    while ans not in ("roll","exit"):
        ans = input("Command: ")
    if ans == "roll":
        dice = (random.randint(1,6),random.randint(1,6))
        print("Player 2 rolled a "+str(dice[0])+" and a "+str(dice[1]))
        if dice[0]+dice[1] in (2,4,6):
            P2s + 10
        elif dice[0]+dice[1] in (1,2,3):
            P2s - 5
        if P2s < 0:
            P1s = 0
    elif ans == "exit":
        exit()
    print("Round 5 over.")

    if P1s > P2s:
        print("Player 1 wins!")
        s = open("scores.csv", "w")
        s.write("Score, Username\n"+P1s+","+P1acc+"\n"+P2s+","+P2acc)
        print("Saved scores to: scores.csv")
        exit()
    elif P2s > P1s:
        print("Player 2 wins!")
        s = open("scores.csv", "w")
        s.write("Score, Username\n"+P2s+","+P2acc+"\n"+P1s+","+P1acc)
        print("Saved scores to: scores.csv")
        exit()
    elif P2s == P1s:
        print("DRAW. Roll until someone wins")
        while P2s == P1s:
            print("Player 1's turn.")
            ans = ""
            ans = input("Command: ")
            while ans not in ("roll","exit"):
                ans = input("Command: ")
                if ans == "roll":
                    dice = (random.randint(1,6),random.randint(1,6))
                    print("Player 1 rolled a "+str(dice[0])+" and a "+str(dice[1]))
                    if dice[0]+dice[1] in (2,4,6):
                        P1s + 10
                    elif dice[0]+dice[1] in (1,2,3):
                        P1s - 5
                    if P1s < 0:
                        P1s = 0
                elif ans == "exit":
                    exit()
                print("Player 2's turn.")
                ans = ""
                ans = input("Command: ")
                while ans not in ("roll","exit"):
                    ans = input("Command: ")
                    if ans == "roll":
                        dice = (random.randint(1,6),random.randint(1,6))
                        print("Player 2 rolled a "+str(dice[0])+" and a "+str(dice[1]))
                        if dice[0]+dice[1] in (2,4,6):
                            P2s + 10
                        elif dice[0]+dice[1] in (1,2,3):
                            P2s - 5
                        if P2s < 0:
                            P1s = 0
        if P1s > P2s:
            print("Player 1 wins!")
            s = open("scores.csv", "w")
            s.write("Score, Username\n"+P1s+","+P1acc+"\n"+P2s+","+P2acc)
            print("Saved scores to: scores.csv")
            exit()
        elif P2s > P1s:
            print("Player 2 wins!")
            s = open("scores.csv", "w")
            s.write("Score, Username\n"+P2s+","+P2acc+"\n"+P1s+","+P1acc)
            print("Saved scores to: scores.csv")
            exit()
            

if __name__ == "__main__":
    run()
