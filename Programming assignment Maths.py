m=int(input('Enter the rows'))
n=int(input('Enter the column'))
matrix=[]
for i in range(m):
    l=list(map(int,input().split()))
    matrix.append(l)
pivot_position=[]  

def row_interchange(matrix,i,x):
    matrix[i],matrix[x]=matrix[x],matrix[i]
    return matrix

def row_replacement(i,m,pivot,j):       
    for p in range(i+1,m):
        scaling=matrix[p][j]/pivot
        for c in range(j,n):
            matrix[p][c]=matrix[p][c]-scaling*matrix[i][c]
    return matrix 

#converting into echelon form

def echelon(matrix):                           
    i,j=0,0    
    while i<m and j<n:
        pivot=0
        pivotrow=0
        for h in range(i,m):
            if matrix[h][j]!=0:
                pivot=matrix[h][j]
                pivotrow=h
                break
        if pivot!=0:
            row_interchange(matrix,i,pivotrow)
            pivot=matrix[i][j]
            t=(i,j)
            pivot_position.append(t)
            row_replacement(i,m,pivot,j)
            i+=1
        j+=1
    return matrix

matrix=echelon(matrix)

print('Pivot Position')
print(pivot_position) 

#converting into reduced echelon form

def reduce_echelon(matrix,pivot_position): 

    for s in pivot_position:
        scaling=matrix[s[0]][s[1]]
        for j in range(len(matrix[s[0]])):
            matrix[s[0]][j]=matrix[s[0]][j]/scaling 

    for s in pivot_position:
        for i in range(0,s[0]):
            scaling=matrix[i][s[1]]
            for j in range(n):
                matrix[i][j]=matrix[i][j]-scaling*matrix[s[0]][j] 

    for i in range(m):
        for j in range(n):
            if abs(matrix[i][j])<10**(-10):
                matrix[i][j]=0.0 
                
    return matrix  

matrix=reduce_echelon(matrix,pivot_position)   

print('RREF')
print(reduce_echelon(matrix,pivot_position))
print('')

#General solution in parametric form

#check for trivial or non-trivial solution
count=0                                   
for i in range(0,n):
    for j in range(len(pivot_position)):
        if i==pivot_position[j][1]:
            count+=1
if count==n:
    print('Unique solution') 
    for t in range(len(matrix)):
        print('x',t+1,'=',0)
else:
    print('Infinitely many solutions')
    l=[]
    for i in range(n):
        l.append(i)
    p=[]    
    for i in range(n):
        for j in range(len(pivot_position)):
            if i==pivot_position[j][1]:
                p.append(i)
    np=[]            
    for i in l:
        if i not in p:
            np.append(i)  
    # print(np)
    a=""
    for i in np:
        d=[]
        for b in range(n):
            d.append(0) 
        for j in range(m):
            for k in pivot_position:
                if k[0]==j:
                    d[k[1]]=(-1)*(matrix[j][i])/matrix[j][k[1]]
        d[i]=1
        a=a+'x'+str(i+1)+'*'+str(d)+"+"
    a=a.rstrip('+')
    print(a)
        


      




     









    



         
