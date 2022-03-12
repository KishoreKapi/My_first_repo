n=int(input("Enter size of the NxN matrix :"))
l=[]
l1=[]
for i in range(n):
    l1.append("W")
l.append(l1)
for i in range(n-2):
    l1=[]
    l1.append("W")
    for j in range(n-2):
        l1.append(" ")
    l1.append("W")
    l.append(l1)
l1=[]
l1.append("W")
for i in range(n-2):
    if(i==int(n//2)-1):
        l1.append("O")
    else:
        l1.append("G")
l1.append("W")
l.append(l1)
s="Y"
while(s=="Y"):
    i,j,f=map(str,input("Enter the brick's position and the brick type :").split(" "))
    i=int(i)
    j=int(j)
    if(f not in "DEDSB"):
        f=int(f)
    l[i][j]=f
    s=input("Do you want to continue?")
b=int(input("Enter ball count :"))
print()
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()
print("Ball count is",b)
s=input("Enter the direction in which the ball need to traverse,if you want to terminate type N :")
print()
p=[1,0]
j=int(n//2)
while(s in "STLDRD"):
    if(s=="ST"):
        i=n-1
        for i in range(n-2,0,-1):
            if(l[i][j]=="DE"):
                for k in range(1,n-1):
                    l[i][k]=" "
                break
            elif(l[i][j]=="DS"):
                l[i][j]=" "
                if(1<=j+1<=n-2):
                    l[i][j+1]=" "
                if(1<=j-1<=n-2):
                    l[i][j-1]=" "
                if((1<=i-1<=n-2)and (1<=j-1<=n-2)):
                    l[i-1][j-1]=" "
                if((1<=i-1<=n-2)and (1<=j+1<=n-2)):
                    l[i-1][j+1]=" "
                if((1<=i-1<=n-2)and (1<=j<=n-2)):
                    l[i-1][j]=" "
                if((1<=i+1<=n-2)and (1<=j-1<=n-2)):
                    l[i+1][j-1]=" "
                if((1<=i+1<=n-2)and (1<=j+1<=n-2)):
                    l[i+1][j+1]=" "
                if((1<=i+1<=n-2)):
                    l[i+1][j]=" "
                break
            elif(l[i][j]=="B"):
                l[i][j]=" "
                if(p[1]==0):
                    p[1]=1
                    l[n-1][int(n//2)+p[0]]="O"
                else:
                    p[1]=0
                    l[n-1][int(n//2)-p[0]]="O"
                    p[0]=p[0]+1
                break
            elif(l[i][j]!=" "):
                l[i][j]=l[i][j]-1
                if(l[i][j]==0):
                    l[i][j]=" "
                break
        c=0
        for x in range(n):
            for y in range(n):
                print(l[x][y],end=" ")
                if(1<=x<n-1 and 1<=y<n-1):
                    if(l[x][y]!=" "):
                        c=1
            print()
        if(c==1):
            if(b<=0):
                print("you lose GAME OVER")
            else:
                print("Ball count is",b)
        else:
            print("you win HURRAY..!")
    elif(s=="LD"):
        i=n-1
        while(l[i][j]!="W"):
            i=i-1
            j=j-1
        for k in range(j+1,n):
            if(l[i][k]=="W"):
                b=b-1
                j=int(n//2)
                break
            elif(l[i][k]=="DE"):
                for r in range(1,n-1):
                    l[i][r]=" "
                if(l[n-1][k]!="O"):
                    b=b-1
                    j=int(n//2)
                else:
                    j=k
                break
            elif(l[i][k]=="DS"):
                l[i][k]=" "
                if(1<=k+1<=n-2):
                    l[i][k+1]=" "
                if(1<=k-1<=n-2):
                    l[i][k-1]=" "
                if((1<=i-1<=n-2)and (1<=k-1<=n-2)):
                    l[i-1][k-1]=" "
                if((1<=i-1<=n-2)and (1<=k+1<=n-2)):
                    l[i-1][k+1]=" "
                if((1<=i-1<=n-2)and (1<=k<=n-2)):
                    l[i-1][k]=" "
                if((1<=i+1<=n-2)and (1<=k-1<=n-2)):
                    l[i+1][k-1]=" "
                if((1<=i+1<=n-2)and (1<=k+1<=n-2)):
                    l[i+1][k+1]=" "
                if((1<=i+1<=n-2)):
                    l[i+1][k]=" "
                if(l[n-1][k]!="O"):
                    b=b-1
                    j=int(n//2)
                else:
                    j=k
                break
            elif(l[i][k]=="B"):
                l[i][k]=" "
                if(p[1]==0):
                    p[1]=1
                    l[n-1][int(n//2)+p[0]]="O"
                else:
                    p[1]=0
                    l[n-1][int(n//2)-p[0]]="O"
                    p[0]=p[0]+1
                if(l[n-1][k]!="O"):
                    b=b-1
                    j=int(n//2)
                else:
                    j=k
                break
            elif(l[i][k]!=" "):
                l[i][k]=l[i][k]-1
                if(l[i][k]==0):
                    l[i][k]=" "
                if(l[n-1][k]!="O"):
                    b=b-1
                    j=int(n//2)
                else:
                    j=k
                break
            c=0
        for x in range(n):
            for y in range(n):
                print(l[x][y],end=" ")
                if(1<=x<n-1 and 1<=y<n-1):
                    if(l[x][y]!=" "):
                        c=1
            print()
        if(c==1):
            if(b<=0):
                print("you lose GAME OVER")
            else:
                print("Ball count is",b)
        else:
            print("you win HURRAY..!")
    elif(s=="RD"):
        i=n-1
        while(l[i][j]!="W"):
            i=i-1
            j=j+1
        for k in range(j-1,-1,-1):
            if(l[i][k]=="W"):
                b=b-1
                j=int(n//2)
                break
            elif(l[i][k]=="DE"):
                for r in range(1,n-1):
                    l[i][r]=" "
                if(l[n-1][k]!="O"):
                    b=b-1
                    j=int(n//2)
                else:
                    j=k
                break
            elif(l[i][k]=="DS"):
                l[i][k]=" "
                if(1<=k+1<=n-2):
                    l[i][k+1]=" "
                if(1<=k-1<=n-2):
                    l[i][k-1]=" "
                if((1<=i-1<=n-2)and (1<=k-1<=n-2)):
                    l[i-1][k-1]=" "
                if((1<=i-1<=n-2)and (1<=k+1<=n-2)):
                    l[i-1][k+1]=" "
                if((1<=i-1<=n-2)and (1<=k<=n-2)):
                    l[i-1][k]=" "
                if((1<=i+1<=n-2)and (1<=k-1<=n-2)):
                    l[i+1][k-1]=" "
                if((1<=i+1<=n-2)and (1<=k+1<=n-2)):
                    l[i+1][k+1]=" "
                if((1<=i+1<=n-2)):
                    l[i+1][k]=" "
                if(l[n-1][k]!="O"):
                    b=b-1
                    j=int(n//2)
                else:
                    j=k
                break
            elif(l[i][k]=="B"):
                l[i][k]=" "
                if(p[1]==0):
                    p[1]=1
                    l[n-1][int(n//2)+p[0]]="O"
                else:
                    p[1]=0
                    l[n-1][int(n//2)-p[0]]="O"
                    p[0]=p[0]+1
                if(l[n-1][k]!="O"):
                    b=b-1
                    j=int(n//2)
                else:
                    j=k
                break
            elif(l[i][k]!=" "):
                l[i][k]=l[i][k]-1
                if(l[i][k]==0):
                    l[i][k]=" "
                if(l[n-1][k]!="O"):
                    b=b-1
                    j=int(n//2)
                else:
                    j=k
                break
            c=0
        for x in range(n):
            for y in range(n):
                print(l[x][y],end=" ")
                if(1<=x<n-1 and 1<=y<n-1):
                    if(l[x][y]!=" "):
                        c=1
            print()
        if(c==1):
            if(b<=0):
                print("you lose GAME OVER")
            else:
                print("Ball count is",b)
        else:
            print("you win HURRAY..!")
    s=input("Enter the direction in which the ball need to traverse,if you want to terminate type N :")
    print()
