

def solve():
    
    n = int(input())

    cells = input()

    streak = 0
    emptyCount = 0
    for i in range(n):
        if cells[i] == '.':
            streak += 1
            emptyCount += 1
        else:
            streak = 0
        if streak >= 3:
            print(2)
            return
    print(emptyCount)
        

if __name__ == "__main__":
    numTests = int(input())
    for i in range(numTests):
        solve()