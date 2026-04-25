

def solve():
    n = int(input())

    if n % 3 != 0:
        print("First")
    else:
        print("Second")
        

if __name__ == "__main__":
    numTests = int(input())
    for i in range(numTests):
        solve()