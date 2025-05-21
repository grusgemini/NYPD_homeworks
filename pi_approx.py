from MonteCarlo import mc 
import math

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