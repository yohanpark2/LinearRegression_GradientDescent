import random
import matplotlib.pyplot as plt

x= []
y= []

for i in range (1,5):
    x.append(i*0.1)
    y.append(i*0.1)

#data -----------------------------------------------------------
# prime of cost is sigma {(2*w*(x**2) + 2*b*x - 2*x*y)} / numOfdata

numOfdata = 4
a = 0.1 # learning rate

w = random.uniform(-5,5)
b = random.uniform(-5,5) 
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
        p_cost += (2*w*(x[i]**2) + 2*b*x[i] - 2*x[i]*y[i])
        
    weight = w - ((a*p_cost) / numOfdata)
    return weight

def get_nextb(w,b,x,y):
    b_cost = 0
    for i in range(numOfdata):
        b_cost += w*x[i] + b -y[i]
    bios = b - a*2*b_cost/numOfdata
    return bios

for X in range(numOflearning):
    w  = get_nextweight(w,b,x,y)
    c = get_cost(w,b,x,y)
    W_val.append(w)
    print("W =",w,end='  ')
    cost_val.append(c)
    print("cost =",c)
    num.append(X)
    print()
w1 =w
c1 =c
print("optimization of w : end")
print("----------------------------------------------------------------------")


for X in range(numOflearning):
    b = get_nextb(w,b,x,y)
    c = get_cost(w,b,x,y)
    b_val.append(b)
    cost_val2.append(c)
    print("b =", b, end=' ')
    print("cost =", c)
    num2.append(X)
    print()
print("optimization of b :end")

plt.plot(num,cost_val)
plt.show()
print("cost optimization grapth about weight")
print("optimization set is w = ",w1," and cost is",c1)
plt.plot(num2,cost_val2)
plt.show()
print("cost optimization graph about weight and bios")
print()

print("optimization set is w=",w,", b=",b,"and cost is",c)


