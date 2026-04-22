#
#
#   This problem seems suspiciously easy...
#   It was slightly hard because of the test case 2 % 2 == 0 which would be incorrect.
#

def solve():
    weight = int(input())

    if weight > 2 and weight % 2 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()