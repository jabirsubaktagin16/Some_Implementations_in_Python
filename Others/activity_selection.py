def printMaxActivities(start, finish):
    n=len(finish)
    print("The Following Activities are selected")

    i=0
    print(i, end=" ")

    for j in range(n):
        if start[j] >= finish[i]:
            print(j, end=" ")
            i=j

if __name__ == '__main__':
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    printMaxActivities(start, finish)