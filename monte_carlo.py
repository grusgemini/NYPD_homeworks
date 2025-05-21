import random
import math

def mc(iterations):
    inside = 0
    
    for _ in range(iterations):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    
    return (inside / iterations) * 4



iterations = int(input('Please enter the total number of iterations:'))
steps = int(input('Please enter the display step:'))

i = 1
while i <= int(int(iterations)/int(steps)):  
    approx = str(mc(int(steps*i)))
    step = str(steps*i)
    print(step + ": " + approx)
    i += 1

final_approx = approx

print('The calculated final value is: ' + final_approx)
print('Python math.pi equals to: ' + str(math.pi))