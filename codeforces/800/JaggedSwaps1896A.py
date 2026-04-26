
def solve():
    n = int(input())
    seq = input().split(" ")

    if seq[0] == "1":
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    numTests = int(input())
    for i in range(numTests):
        solve()