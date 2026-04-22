#
#   Input: int n
#
#   Output: permutation of length 3n
#
#   n blocks with 3 elements, the sum of the medians of these
#   blocks are MAXIMIZED
#
#   1 2 3 4 5 6 7 8 9 10 11 12
#   5 2 4 8 3 9 7 1 6
#   median(5,2,4) + median(8,3,9) + median(7,1,6) = 4 + 8 + 6 = 18 
#   1,11,12   2,9,10   3,7,8  4,5,6 = 11 + 9 + 7 + 5 = 32
#
#
#
#   n = 2
#
#   1,2,3,4,5,6
#   (1,3,5) + (2,4,6) = 3 + 4 = 7 X WRONG
#   (1,3,4) + (2,5,6) = 3 + 5 = 8 ✅
#
#
def solve():
    numTests = int(input())

    for i in range(numTests):
        n = int(input())

        # Generate array
        array = [str(i + 1) for i in range(3 * n)]

        l, r = 0, len(array) - 1

        perm = ""

        while l < r:
            perm += array[l] + " "
            l += 1

            for i in range(2):
                perm += array[r] + " "
                r -= 1
            
        print(perm)

if __name__ == "__main__":
    solve()