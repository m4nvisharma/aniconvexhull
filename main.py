#Friendly Problems; Convex Hull
#Manvi Sharma, Neev Shah
#Initializes a list of 50 random integer points, and returns the points that are required 
#to create a shape that is the smallest convex set that contains all points

#importing required modules
import math
import random

import matplotlib.pyplot as plt
import matplotlib.animation as animation

#generating list of 100 random integer coordinates
points = [(random.randint(0,100), random.randint(0,100)) for i in range(50)]

#Sample Tests

#points = [(0, 0), (0, 4), (-4, 0), (5, 0), (0, -6), (1, 0)]
#Output: (-4, 0), (5, 0), (0, -6), (0, 4)

#points = [(1, 2), (3, 1), (5, 6), (5,2), (6,2), (6,7)]
#Output: {{1, 2}, {3, 1}, {5, 6}, {6, 2}, {6,7}}

#points = [(-1,3), (2,5), (2,4), (2,3), (4,0), (5,0), (6,7)]
#Output = (-1, 3), (2,3), (2,5)

#printing all points 
print(points)


#CVX HULL CODE


#sorting list of points by y value (lowest to highest) and returning lowest
def low(points):
    return min(points, key=lambda x: (x[1], x[0]))

    #new = sorted(points, key = lambda k: [k[0], k[1]])
    #return new[0]

#gets polar angle of two coordinate points
#cite https://www.calculator.net/slope-calculator.html?x11=69&y11=0&x12=79&y12=5&type=1&x=Calculate
def getang(x,y):
    ang = math.degrees(math.atan2(y[1] - x[1], y[0] - x[0]))
    return ang

#returning orientation of 3 ordered points
#https://www.geeksforgeeks.org/orientation-3-ordered-points/
def orient(prev, cur, next):
    val = (cur[1] - prev[1]) * (next[0] - cur[0]) - (cur[0] - prev[0]) * (next[1] - cur[1])
    if (val > 0):
        # Clockwise orientation
        return 1
    elif (val < 0):
        # Counterclockwise orientation
        return 2
    else:
        # Collinear orientation
        return 0


def gram(points):
    #sorting by lowest y value and appending smallest value to convex hull
    first = low(points)
    cvx = [first]
    
    #sorting points by polar angle they make with 'first' point
    points.sort(key=lambda x: (getang(first, x), -x[1], x[0]))
    for p in points[1:]:
        #https://www.w3schools.com/python/python_lists_remove.asp
        #considering case of counterclockwise orientation and removing from list, else, appending to convex hull
        while len(cvx) > 1 and orient(cvx[-2], cvx[-1], p) != 2:
            cvx.pop()
        cvx.append(p)
    return cvx

#getting list of points
conhull = gram(points)

#avoiding case of printing start point twice since it is also end point by taking out duplicates from list
if len(conhull) > len(set(conhull)):
   conhull.pop()

#iterating through convex hull points and printing to screen
for p in conhull:
    print(p)


#ANIMATION CODE
#https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

fig, ax = plt.subplots()

#initilizing list to hold all line objects currently drawn on the graph (boundary of cvx hull)
lines = []

#initializing list to store points of the convex hull that have been selected so far
cur = []
def update(frame):
    #removes line from graph and clearing previous lines for next trial
    for line in lines:
        line.remove()
    lines.clear()
    
    #reset to current frame
    cur.clear()
    
    #adds points from determined convex hull list points upto the current frame, progressively building animation
    cur.extend(conhull[:frame + 1])
    #considers case of line connecting last point of cvx hull back to starting points
    if frame > 0 and len(cur) == len(conhull):
        line, = plt.plot([p[0] for p in cur] + [cur[0][0]],[p[1] for p in cur] + [cur[0][1]],'c-*', label="Convex Hull")
        lines.append(line)
    elif frame > 0:
        #draws a line that connects points in cur
        line, = ax.plot([p[0] for p in cur],[p[1] for p in cur],'*-', label="Convex Hull")
        lines.append(line)
    
        
    # Highlights point being examined
    ax.scatter(conhull[frame][0], conhull[frame][1], color="orchid", marker = "4", s=10)
    

ptsx = []
ptsy = []
#places all x values of points in list ptsx, and all y values in ptsy
for i in range(len(points)):
    ptsx.append(points[i][0])
    ptsy.append(points[i][1])
#sets up scatter plot of all points
po = plt.scatter(ptsx, ptsy, label= "points", color= "salmon", marker= "*", s=30)
#sets up animation of determining linegraph of convex hull
ani = animation.FuncAnimation(fig, update, frames=len(conhull), interval=1500)

#shows result on screen
plt.show()


#https://matplotlib.org/stable/gallery/color/named_colors.html
#https://matplotlib.org/stable/api/markers_api.html

#https://en.wikipedia.org/wiki/Graham_scan
#https://www.geeksforgeeks.org/convex-hull-using-graham-scan/
#https://en.wikipedia.org/wiki/Convex_hull#:~:text=The%20convex%20hull%20may%20be,of%20points%20in%20the%20subset.

"""
#I did test with larger sets of coordinates (100, 500, 1000) 
#and it ran successfully but I was unable to copy and paste it onto here.
"""
