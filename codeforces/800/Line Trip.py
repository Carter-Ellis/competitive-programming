#
#   Start at point 0
#   Gas stations: n can be 1 - 50
#   Destination: x can be 2 - 100  ---- Never a gas station
#
#   3 7
#   1 2 5
#   
#   Solution: Max Distance between two gas stations Max(gas station dist, dist between last gas station and x)
#
#   Compute dist between last gas station and x
#   Compute max distance between all gas stations

def solve():
    
    n, x = input().split(" ")
    n, x = int(n), int(x)

    gasLocs = input().split(" ")

    # last gas station and x
    turnAroundDist = (x - int(gasLocs[n - 1])) * 2
    startDist = int(gasLocs[0])

    maxGasDist = 0
    for i in range(n - 1):
        dist = int(gasLocs[i + 1]) - int(gasLocs[i])
        if maxGasDist < dist:
            maxGasDist = dist

    print(max(maxGasDist, turnAroundDist, startDist))
if __name__ == "__main__":
    numTests = int(input())
    for i in range(numTests):
        solve()