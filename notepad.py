text=[]
num=[]
accu=[]
count=0
while True:
    print("1. Enter text\n2. Find a word\n3. Replace a word\n4.Show the current text\n5. Exit")
    c=int(input("Enter Choice Here::"))
    if c==1:
        print("press 1 for entering text\npress 2 for entering integers here")
        choi=int(input("enter choice here::"))
        if choi==1:
            te=input("enter text here::").split(" ")
            for i in te:
                text.append(i)
        if choi==2:
            te=input("enter space seprated text here::").split(" ")
            for i in te:
                num.append(i)
    elif c==2:
        won=int(input("press 1 for 1st occurance\npress 2 for all occurance::"))
        word=input("enter word for finding::")
        for i in range(len(text)):
            if text[i]==word:
                count+=1
                accu.append(i+1)
        if len(accu)>0:
            print(word,"occurs",count,"times")
        else:
            print(word,"does not occcur in this text")
        if won==1:
            print(f"{word}, found at {accu[0]}")
        elif won==2:
            print(f"{word}, occurs at these positions{accu}")
    elif c==3:
        l=int(input("press 1 for replacing from text list\npress 2 for replacing from integer list::"))
        if l==1:
            nu=(input("enter word you want to replace::"))
            word=input(f"enter word or integer you want to replace with {nu}::")
            for i in range(len(text)):
                if (nu)==text[i]:
                    text[i]=word
        elif l==2:
            nu=(input("enter integer you want to replace::"))
            word=input(f"enter integer or word you want to replace with {num}::")
            for i in range(len(num)):
                if (nu)==num[i]:
                    num[i]=word
    elif c==4:
        print("which notes do you want to see press 1 for text and 2 for integer")
        orig=int(input("enter choice ::"))
        if orig==1:
            ori=" ".join(text)
            print(ori)
        elif orig==2:
            ori=" ".join(num)    
            print(ori)
    elif c==5:
        print("Thanks for Using Our Program")
        break