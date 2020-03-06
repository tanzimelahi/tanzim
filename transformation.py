import math
fl=open("howaboutpic.ppm","w")
initialstr="P3\n500 500\n255\n"
data=list(range(250000))
initVal=0
while(initVal<len(data)):
    data[initVal]=["0","0","0"]
    initVal+=1
def plot(x,y,color):# color is a list
    x+=250
    y=250-y
    data[round(x+y*500)]=color

#for the first two octants, the x0 must be smaller than x1
def firstoct(x0,y0,x1,y1,color):#oct 1 and 5
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=2*A+B
    while x<x1:
        plot(x,y,color)
        if d>=0:
            y+=1
            d=d+2*B
        x=x+1
        d=d+2*A
    plot(x1,y1,color)
def secondoct(x0,y0,x1,y1,color):#oct 2 and 6
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A+2*B
    while y<y1:
        plot(x,y,color)
        if d<=0:
            d=d+2*A
            x+=1
        y=y+1
        d=d+2*B
    plot(x1,y1,color)
def thirdoct(x0,y0,x1,y1,color):#oct 3 and 7 remember the x0 and x1 hierarchy is reversed for this one
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A+2*B
    while y<y1:
        plot(x,y,color)
        if d>=0:
            x=x-1
            d=d-2*A
        y=y+1
        d=d+2*B
    plot(x1,y1,color)
def fourthoct(x0,y0,x1,y1,color): #oct 4 and 8
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A+2*B
    while x<x1:
        plot(x,y,color)
        if d<=0:
            y=y-1
            d=d-2*B
        x=x+1
        d=d+2*A
    plot(x1,y1,color)
def oneSlopePos(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while x<=x1:
        plot(x,y,color)
        x+=1
        y+=1

def oneSlopeNeg(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while x<=x1:
        plot(x,y,color)
        x+=1
        y-=1
def zeroSlope(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while(x<=x1):
        plot(x,y,color)
        x+=1
def undefinedSlope(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while y<=y1:
        plot(x,y,color)
        y+=1

def drawline(x0,y0,x1,y1,color):# whenever possible x0 must be greater than x1(left to right orientation)
    if(x0>x1):
        store=x0
        x0=x1
        x1=store
        storage=y0
        y0=y1
        y1=storage
    if(x0==x1):
        if(y1<y0):
            store=y0
            y0=y1
            y1=store
        undefinedSlope(x0,y0,x1,y1,color)
    elif(y0==y1):
        zeroSlope(x0,y0,x1,y1,color)
    elif abs(x1-x0)>=abs(y1-y0):
        if y1>y0:
            firstoct(x0,y0,x1,y1,color)
        else:
            fourthoct(x0,y0,x1,y1,color)
    else:
        if y1>y0:
            secondoct(x0,y0,x1,y1,color)
        else:
            thirdoct(x1,y1,x0,y0,color)



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
def update_matrix(row,column,matrix,value):
    matrix[column][row]=value
def print_matrix(matrix):
    result=""
    row=len(matrix[0])
    col=len(matrix)
    for x in range(row):
        for y in range(col):
            add=str(matrix[y][x])
            if len(add)==1:
                result+=add+"   "
            elif len(add)==2:
                result+=add+"  "
            else:
                result+=add+" "
        result+="\n"
    print(result)
        


def ident(matrix):
    row=len(matrix[0])
    col=row
    for x in range(row):
        for y in range(col):
            if(x==y):
                matrix[y][x]=1
            else:
                matrix[y][x]=0
def matrix_multiplication(m1,m2):
    result=new_matrix(len(m1[0]),len(m2))
    for secondCol in range(len(m2)):
        for y in range(len(m1[0])):
            add=0
            for x in range(len(m1)):
                add+=(m1[x][y]*m2[secondCol][x])
            result[secondCol][y]=add
    for x in range(len(m2)):
        m2[x]=result[x]
    
def empty_matrix():
    m = []
    m.append( [] )
    return m
#test cases

#that ends here
def add_point(matrix,x,y,z=0):
    if len(matrix[0])==0:
        matrix[0].append(x)
        matrix[0].append(y)
        matrix[0].append(z)
        matrix[0].append(1)
    else:
        matrix.append([])
        matrix[len(matrix)-1].append(x)
        matrix[len(matrix)-1].append(y)
        matrix[len(matrix)-1].append(z)
        matrix[len(matrix)-1].append(1)
def add_edge(matrix,x0,y0,z0,x1,y1,z1):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)
def add_lines(matrix,color):
    step=0
    while(step<len(matrix)):
        #print("x0:"+str(matrix[step][0])+"  "+"y0:"+str(matrix[step][1])+"  "+"x1:"+str(matrix[step+1][0])+"  "+"y1:"+str(matrix[step+1][1]))
        drawline(matrix[step][0],matrix[step][1],matrix[step+1][0],matrix[step+1][1],color)
        step+=2
def scale(sx,sy,sz):
    info=[sx,sy,sz]
    matrix=new_matrix(4,4)
    ident(matrix)
    for col in range(len(matrix)-1):
        for row in range(len(matrix[0])-1):
            if row==col:
                matrix[col][row]=info[col]

    return matrix
def move(a,b,c):
    info=[a,b,c]
    matrix=new_matrix(4,4)
    ident(matrix)
    for row in range(len(matrix)-1):
        matrix[3][row]=info[row]
    return matrix

def x_rotation(angle):
    angle=math.radians(angle)
    matrix=new_matrix(4,4)
    ident(matrix)
    update_matrix(1,1,matrix,(math.cos(angle)))
    update_matrix(1,2,matrix,-1*(math.sin(angle)))
    update_matrix(2,1,matrix,(math.sin(angle)))
    update_matrix(2,2,matrix,(math.cos(angle)))
    return matrix

def y_rotation(angle):
    angle=math.radians(angle)
    matrix=new_matrix(4,4)
    ident(matrix)
    update_matrix(0,0,matrix,(math.cos(angle)))
    update_matrix(0,2,matrix,(math.sin(angle)))
    update_matrix(2,0,matrix,(-1*math.sin(angle)))
    update_matrix(2,2,matrix,(math.cos(angle)))
    return matrix


def z_rotation(angle):
    angle=math.radians(angle)
    matrix=new_matrix(4,4)
    ident(matrix)
    update_matrix(0,0,matrix,(math.cos(angle)))
    update_matrix(0,1,matrix,-1*(math.sin(angle)))
    update_matrix(1,0,matrix,(math.sin(angle)))
    update_matrix(1,1,matrix,(math.cos(angle)))
    return matrix          
    

    
def rotation (angle,axis_of_rotation):
    if(axis_of_rotation=="x"):
        return x_rotation(angle)
    elif axis_of_rotation=="y":
        return y_rotation(angle)
    else:
        return z_rotation(angle)
transformation_matrix=new_matrix()
ident(transformation_matrix)
edge_matrix=empty_matrix()
def apply(transform,edge):
    matrix_multiplication(transform,edge)
fl2=open("script.txt",'r')
info=fl2.readlines()
for a in range(len(info)):
        key=info[a].strip()
        if key=="line":
            fin_info=info[a+1].split()
            add_edge(edge_matrix,int(fin_info[0]),int(fin_info[1]),int(fin_info[2]),int(fin_info[3]),int(fin_info[4]),int(fin_info[5]))
        elif key=="move":
            fin_info=info[a+1].split()
            matrix_multiplication(move(int(fin_info[0]),int(fin_info[1]),int(fin_info[2])),transformation_matrix)
        elif key=="scale":
            fin_info=info[a+1].split()
            matrix_multiplication(scale(int(fin_info[0]),int(fin_info[1]),int(fin_info[2])),transformation_matrix)
        elif key=="rotate":
            fin_info=info[a+1].split()
            #print_matrix(rotation(int(fin_info[1]),fin_info[0]))
            #print_matrix(transformation_matrix)
            matrix_multiplication(rotation(int(fin_info[1]),fin_info[0]),transformation_matrix)
            #print_matrix(transformation_matrix)
        elif key=="apply":
            print_matrix(edge_matrix)
            print_matrix(transformation_matrix)
            apply(transformation_matrix,edge_matrix)
            print_matrix(edge_matrix)
            #print_matrix(transformation_matrix)
            add_lines(edge_matrix,["0","255","0"])
        elif key=="ident":
            ident(transformation_matrix)
fl2.close()
for ls in data:
    for a in ls:
       initialstr+=a+" "
    initialstr+=" "
fl.write(initialstr)
fl.close()

