#
#
#
#   
#   The solution does not depend on the sorting
#   but rather, it depends on the value of k.
#   Whether k > 1 or not.
#
#
#

def solve():

    n, k = input().split(" ")
    n, k = int(n), int(k)

    numStrs = input().split(" ")
    nums = []
    for num in numStrs:
        nums.append(int(num))

    # Check if the numbers are sorted already
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            if k < 2:
                print("NO")
                return

    print("YES")





if __name__ == "__main__":
    numTests = int(input())
    for i in range(numTests):
        solve()