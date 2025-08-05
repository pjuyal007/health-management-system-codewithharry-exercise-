# you have 3 clients pankaj neeraj kunal you have to ask the client name and then their diet and exercise
# before that you have to ask whether they want to log or retrive
def getdate():
    import datetime
    return datetime.datetime.now()
print("Do you want to log or retrieve data.1 for log 2 for retrieve")
lr=int(input())
c=int(input("enter the client name : 1. for Pankaj 2. for Neeraj 3. for Kunal: \n"))
# de=int(input("enter diet or workout. 1 for diet 2. for workout"))
if lr==1:
    print("what do you want to log workout or diet ")
    de = int(input("enter 1 for diet 2. for workout"))
    if c==1 and de==1:
        f=open("pdi.txt","a")#a to append /write in file
        die1=input("diet plan for pankaj:\n")
        time=str(getdate())#optional we can directly call function getdate
        f.write(die1+"["+time+"]"+"\n")#f.write(f"{die1} [{time}] \n") better and efficient
        f.close()
        print("successfully logged diet plan for pankaj")
        """
          if c == 1 and de == 1:
        with open("pdi.txt", "a") as f:
            entry = input("Diet plan for Pankaj:\n")
            f.write(f"{entry} [{getdate()}]\n")
        print("Successfully logged diet plan for Pankaj.")
        """
    elif c==1 and de==2:
        f1=open("pwork.txt","a")
        wo1=input("workout plan for pankaj :\n")
        time=str(getdate())
        f1.write(wo1+"["+time+"]"+"\n")
        f1.close()
        print("successfully logged workout plan for pankaj")
    elif c==2 and de==1:
        f2 = open("ndi.txt", "a")
        die2 = input("diet plan for neeraj:\n")
        time = str(getdate())
        f2.write(die2 + "[" + time + "]" + "\n")
        f2.close()
        print("successfully logged diet plan for neeraj")
    elif c==2 and de==2:
        f3 = open("nwork.txt", "a")
        wo2 = input("workout plan for neeraj :\n")
        time = str(getdate())
        f3.write(wo2 + "[" + time + "]" + "\n")
        f3.close()
        print("successfully logged workout plan for neeraj")
    elif c==3 and de==1:
        f4 = open("kdi.txt", "a")
        die3 = input("diet plan for kunal:\n")
        time = str(getdate())
        f4.write(die3 + "[" + time + "]" + "\n")
        f4.close()
        print("successfully logged diet plan for kunal")
    elif c==3 and de==2:
        f5 = open("kwork.txt", "a")
        wo3 = input("workout plan for kunal :\n")
        time = str(getdate())
        f5.write(wo3 + "[" + time + "]" + "\n")
        f5.close()
        print("successfully logged workout plan for kunal")
    else:
        print("Enter valid details ")
import os
if lr==2 :
    print("what do you want to retrieve diet or wokout:")
    de = int(input("enter 1 for diet 2. for workout"))
    if c==1 and de ==1:
        if os.path.exists("pdi.txt"):
            with open("pdi.txt") as f:
                print(f.read())
        else:
            print("No logs found yet for Pankaj's diet.")
    if c==1 and de==2:
        if os.path.exists("pwork.txt"):
            with open("pwork.txt") as f:
                print(f.read())
        else:
            print("No logs found yet for Pankaj's workout.")
    if c==2 and de ==1:
        if os.path.exists("ndi.txt"):
            with open("ndi.txt") as f:
                print(f.read())
        else:
            print("No logs found yet for neeraj's diet.")
    if c==2 and de==2:
        if os.path.exists("nwork.txt"):
            with open("nwork.txt") as f:
                print(f.read())
        else:
            print("No logs found yet for neeraj's workout.")
    if c==3 and de ==1:
        if os.path.exists("kdi.txt"):
            with open("kdi.txt") as f:
                print(f.read())
        else:
            print("No logs found yet for kunal's diet.")
    if c==3 and de==2:
        if os.path.exists("kwork.txt"):
            with open("kwork.txt") as f:
                print(f.read())
        else:
            print("No logs found yet for kunal's workout.")







