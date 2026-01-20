"""
Bob Klemm
5/27/2022

'Fractal Tree'
"""

import matplotlib.pyplot as plt
import math


"""
Inspired by some fractal-like trees that I saw at a state park...
"""


#initialized parameters
branch_factor = math.sqrt(2)/2 #each iteration will be smaller than the previous
branch_angle = [45,40,35,30,25] #degree angle
n = 5 #iterations (keep runtime low to start; n < 6)

def treefractal(branch_angle, branch_factor, n): 
    
    #initialize tree 
    x = [0,0] #x coordinate
    y = [0,1] #y coordinate
    z = [-1,0] #index of iteration
    j = 1 #old point counter
    
    for num in range(0,n):
    
        if num == 0:
            m = [num - 1, num + 1]
            
        else: 
            new_m = []
            for item in m:
                new_m.append(item - 1)
                new_m.append(item + 1)
            m = new_m
        
        
        for i in range(0,2**(num+1)): #how many new points for that iteration
            z.append(num+1)
            
            a = branch_factor**(num+1) * math.sin(m[i] * math.pi / 180 * branch_angle[num])
            b = branch_factor**(num+1) * math.cos(m[i] * math.pi / 180 * branch_angle[num])
    
            #add new point on plot
            x.append(x[j] + a)
            y.append(y[j] + b)
            
            if len(z) % 2 == 0:
                j += 1

    plt.scatter(x,y)
    plt.axis('equal')
    plt.title('A Tree Fractal: Type 1')
    plt.show()

treefractal(branch_angle, branch_factor, n)



#initialized parameters
branch_factor = .75 #each iteration will be smaller than the previous
branch_angle = [45,40,35,30,25] #degree angle
n = 5 #iterations (keep runtime low to start; n < 6)

def treefractal2(branch_angle, branch_factor, n):
    
    #initialize tree 
    x = [0,0] #x coordinate
    y = [0,1] #y coordinate
    z = [-1,0] #index of iteration
    j = 1 #old point counter
    
    for num in range(0,n):
    
        m = [-1, 1]
        
        for i in range(0,2**(num+1)): #how many new points for that iteration
            z.append(num+1)
            
            k = i % 2
            
            a = branch_factor**(num+1) * math.sin(m[k] * math.pi / 180 * branch_angle[num])
            b = branch_factor**(num+1) * math.cos(math.pi / 180 * branch_angle[num])
    
            #add new point on plot
            x.append(x[j] + a)
            y.append(y[j] + b)
            
            if len(z) % 2 == 0:
                j += 1

    plt.scatter(x,y)
    plt.axis('equal')
    plt.title('A Tree Fractal: Type 2')
    plt.show()

treefractal2(branch_angle, branch_factor, n)
    
