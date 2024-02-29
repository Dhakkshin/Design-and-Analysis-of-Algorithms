import random
import matplotlib.pyplot as plt
import math
import numpy as np


def generateCoordinates(x_min : int, y_min : int, x_max : int, y_max : int, n : int) -> list[int]:
    plane : list[int] = [(random.randint(x_min,x_max+1),random.randint(y_min,y_max+1)) for _ in range(n)]
    return plane

def display_coordinates(coordinates):
    x = [coord[0] for coord in coordinates]
    y = [coord[1] for coord in coordinates]
    
    plt.scatter(x[0], y[0], color='red')  
    plt.scatter(x[1:], y[1:])  
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2D Coordinates')
    plt.show()

def display_coordinates_WithLines(coordinates):
    x = [coord[0] for coord in coordinates]
    y = [coord[1] for coord in coordinates]
    
    plt.scatter(x[0], y[0], color='red')  
    plt.scatter(x[1:], y[1:])  
    
    for i in range(1, len(coordinates)):
        plt.plot([x[0], x[i]], [y[0], y[i]], color='black')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2D Coordinates')
    plt.show()

def plot_points_and_line(points1, points2):
    x1, y1 = zip(*points1)
    x2, y2 = zip(*points2)

    plt.scatter(x1[0], y1[0], color='red')
    plt.scatter(x1[1:], y1[1:])
    plt.plot(x2, y2, color='red')
    plt.title('Graham')

    plt.show()


def sortByAngle(p):
    points = sorted(p, key=lambda x: (x[1],x[0]))
    # print(points)
    # display_coordinates(points)

    start = points[0]
    sortedByAngle = sorted(points, key = lambda point : math.atan2(point[1]-start[1], point[0]-start[0]))
    # print(sortedByAngle)
    # display_coordinates_WithLines(sortedByAngle)
    return points, sortedByAngle


def walkAround(points):
    npPoints = [np.array(x) for x in points]
    circumference = []
    for point in npPoints:
        while len(circumference) >= 2 and np.cross(circumference[-1] - circumference[-2], point - circumference[-1]) < 0:
            circumference.pop()
        circumference.append(point)
    circumference.append(points[0])
    print(circumference)
    return circumference

def graham(initialPoints):
    initialPoints, sortedPoints = sortByAngle(initialPoints)
    boundary = walkAround(sortedPoints)
    plot_points_and_line(initialPoints, boundary)



