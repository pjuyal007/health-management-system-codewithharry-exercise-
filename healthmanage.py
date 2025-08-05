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
    print("what do you want to log workout plan or diet plan.Type 'finish' in last line of input when your plan is finished ")
    de = int(input("enter 1 for diet 2. for workout : "))
    if c==1 and de==1:
        diets = []
        f=open("pdi.txt","a")#a to append /write in file
        print("diet plan for pankaj:")
        while True:
          die1 = input()
          if die1.lower()== 'finish':
              break#exit from while loop
          diets.append(die1)
        die2= '\n'.join(diets)#joims the strings with the seperator we want

        f.write(f"{die2} [{getdate()}] \n")
        f.close()
        print("successfully logged diet plan for pankaj")
    elif c==1 and de==2:
        works = []
        f=open("pwork.txt","a")
        print("workout plan for pankaj")
        while True:
           wo1 = input()
           if wo1.lower()=='finish':
                break
           works.append(wo1)
        wo2="\n".join(works)
        f.write(f" {wo2} {getdate()}:\n")
        f.close()
        print("successfully logged workout plan for pankaj")
    if c==2 and de==1:
        diets = []
        f=open("ndi.txt","a")#a to append /write in file
        print("diet plan for neeraj:")
        while True:
          die1 = input()
          if die1.lower()== 'finish':
              break
          diets.append(die1)
        die2= '\n'.join(diets)#joims the strings with the seperator we want

        f.write(f"{die2} [{getdate()}] \n")
        f.close()
        print("successfully logged diet plan for neeraj")
    elif c==2 and de==2:
        works = []
        f=open("nwork.txt","a")
        print("workout plan for neeraj")
        while True:
           wo1 = input()
           if wo1.lower()=='finish':
                break
           works.append(wo1)
        wo2="\n".join(works)
        f.write(f" {wo2} {getdate()}:\n")
        f.close()
        print("successfully logged workout plan for neeraj")
    if c==3 and de==1:
        diets = []
        f=open("kdi.txt","a")#a to append /write in file
        print("diet plan for kunal:")
        while True:
          die1 = input()
          if die1.lower()== 'finish':
              break
          diets.append(die1)
        die2= '\n'.join(diets)#joims the strings with the seperator we want

        f.write(f"{die2} [{getdate()}] \n")
        f.close()
        print("successfully logged diet plan for kunal")
    elif c==3 and de==2:
        works = []
        f=open("kwork.txt","a")
        print("workout plan for kunal")
        while True:
           wo1 = input()
           if wo1.lower()=='finish':
                break
           works.append(wo1)
        wo2="\n".join(works)
        f.write(f" {wo2} {getdate()}:\n")
        f.close()
        print("successfully logged workout plan for kunal")
    else:
        print("Enter valid details ")
import os
if lr==2 :
    print("what do you want to retrieve diet or workout :")
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








