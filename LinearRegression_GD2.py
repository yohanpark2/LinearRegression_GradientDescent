import random
import matplotlib.pyplot as plt

x= []
y= []
a2 = 2
b2 = 2

for i in range (-5,6):
    x.append(i)
    y.append(i*a2+b2)

#data -----------------------------------------------------------
# prime of cost is  sigma {(2*w*(x**2) + 2*b*x - 2*x*y)} / numOfdata

numOfdata = 10
a = 0.01 # learning rate

w = random.uniform(-0.1,0.1)
b = random.uniform(-0.1,0.1)
# hypothesis = w*x + b


W_val = []
cost_val = []
num = []
b_val = []
cost_val2 = []
num2 = []

numOflearning = 100

def get_cost(w,b,x,y): #  MSE
    cost = 0
    for i in range (numOfdata): 
        cost += ((w*x[i] + b - y[i])**2)
    cost = cost / numOfdata
    return cost

def get_nextweight(w,b,x,y):
    p_cost=0
    for i in range(numOfdata):
        p_cost += 2*(w*(x[i]) + b - y[i])*x[i]
        
    weight = w - ((a*p_cost) / numOfdata)
    return weight

def get_nextb(w,b,x,y):
    b_cost = 0
    for i in range(numOfdata):
        b_cost += 2*(w*x[i] + b -y[i])
    bios = b - a*b_cost/numOfdata
    return bios

for X in range(numOflearning):
    w = get_nextweight(w,b,x,y)
    b = get_nextb(w,b,x,y)
    c = get_cost(w,b,x,y)
    W_val.append(w)
    b_val.append(b)
    print("W =",w,end='  ')
    cost_val.append(c)
    print("cost =",c)
    num.append(X)
    print()

#for X in range(numOflearning):
#    b = get_nextb(w,b,x,y)
#    c = get_cost(w,b,x,y)
#    b_val.append(b)
#    cost_val2.append(c)
#    print("b =", b, end=' ')
#    print("cost =", c)
#    num2.append(X)
#    print()
#print("optimization of b :end")

plt.plot(num,cost_val)
plt.show()
print()

print("optimization set is w=",w,", b=",b,"and cost is",c)


