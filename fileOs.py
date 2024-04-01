import math as m
import ast
import matplotlib.pyplot as plt


valueX = []
with open("Assignment or Projects/Assignment graph/numbers.txt", "r") as file:
    data = file.readlines()
    for line in data:
        valueX.extend([int(x) for x in line.split(',')])


def graph1():
    result = []
    for x in valueX:
        num = x
        result.append((num * num) + (7 * num) + 2)
    return result
def graph2():
    result = []
    for x in valueX:
        num = x
        result.append((3 * num) + 2)
    return result
def graph3():
    result = []
    for x in valueX:
        num = x
        result.append(num**2)
    return result
def graph4():
    result = []
    for x in valueX:
        num = x
        result.append(num**3)
    return result
def graph5():
    result = []
    for x in valueX:
        num = x
        result.append(num**5)
    return result
def graph6():
    result = []
    for x in valueX:
        num = x
        result.append((num**3) + (2 * num**2) + num + 10)
    return result
def graph7():
    result = []
    for x in valueX:
        num = x
        result.append(
            (num**4) - (3 * num**3) + (2 * num**2) - num + 11)
    return result
def graph8():
    result = []
    for x in valueX:
        result.append(m.sin(x))
    return result
def graph9():
    result = []
    for x in valueX:
        result.append(m.cos(x))
    return result
def graph10():
    result = []
    for x in valueX:
        num = x
        result.append((num**5) + (4 * num**4) + (num**3) - (2 * num **2 + 100))
    return result

numberPick = int(input("LIST OF FUNCTIONS:\n1.) f(x) = x^2 + 7x + 2\n2.) f(x) = 3x + 2\n3.) f(x) = x^2\n4.) f(x) = x^3\n5.) f(x) = x^5\n6.) f(x) = x^3 + 2x^2 + x + 10\n7.) f(x) = x^4 - 3x^3 + 2x^2 - x + 11\n8.) f(x) = sin(x)\n9.) f(x) = cos(x)\n10.) f(x) = x^5 + 4x^4 + x^3 - 2x^2 + 100\n11.) All Functions from 1-10\n\nEnter the number of the function you want to solve: "))
questions = [
    "x^2 + 7x + 2",
    "3x + 2",
    "x^2",
    "x^3",
    "x^5",
    "x^3 + 2x^2 + x + 10",
    "x^4 - 3x^3 + 2x^2 - x + 11",
    "sin(x)",
    "cos(x)",
    "x^5 + 4x^4 + x^3 - 2x^2 + 100"]

def createFile(numberEquation):
    if numberEquation == 1:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph1()))
    elif numberEquation == 2:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph2()))
    elif numberEquation == 3:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph3()))
    elif numberEquation == 4:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph4()))
    elif numberEquation == 5:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph5()))
    elif numberEquation == 6:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph6()))
    elif numberEquation == 7:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph7()))
    elif numberEquation == 8:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph8()))
    elif numberEquation == 9:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph9()))
    elif numberEquation == 10:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph10()))
    elif numberEquation == 11:
        with open("Assignment or Projects/Assignment graph/result.txt", "w") as file:
            file.write(str(graph1()))
            file.write("\n")
            file.write(str(graph2()))
            file.write("\n")
            file.write(str(graph3()))
            file.write("\n")
            file.write(str(graph4()))
            file.write("\n")
            file.write(str(graph5()))
            file.write("\n")
            file.write(str(graph6()))
            file.write("\n")
            file.write(str(graph7()))
            file.write("\n")
            file.write(str(graph8()))
            file.write("\n")
            file.write(str(graph9()))
            file.write("\n")
            file.write(str(graph10()))

def fileRead():
    results = []
    with open("Assignment or Projects/Assignment graph/result.txt", "r") as file:
        data = file.readlines()
        for line in data:
            results.append(ast.literal_eval(line.strip()))
    return results

def plot_results():
    if numberPick == 11:
        results = fileRead()
        for i, result in enumerate(results):
            plt.plot(valueX, result, label=f"{questions[i]}")
    elif numberPick < 11:
        results = fileRead()
        for i, result in enumerate(results):
            plt.plot(valueX, result, label=f"{questions[numberPick - 1]}")
    plt.xlabel('Number')
    plt.ylabel('Result')
    plt.legend(loc="best")
    plt.show()

createFile(numberPick)
plot_results()