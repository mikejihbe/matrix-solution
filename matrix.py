

def iterate_matrix_clockwise(matrix):
    if len(matrix) == 0:
        return []
    left = 0
    top = 0
    right = len(matrix[0])
    bottom = len(matrix)

    result = []
    while True:
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1
        if top >= bottom:
            break
        for i in range(top, bottom):
            result.append(matrix[i][right-1])
        right -= 1
        if right <= left:
            break
        for i in range(right-1, left -1, -1):
            result.append(matrix[bottom-1][i])
        bottom += 1
        if bottom >= top:
            break
    return result

test_cases = [
    # base cases
    {
        "name": "0x0",
        "matrix": []
    },{
        "name": "1x1",
        "matrix": [[0]]
    },{
        "name": "2x1",
        "matrix": [[0,1]]
    },{
        "name": "1x2",
        "matrix": [
            [0],
            [1]
        ]
    },
    # Left termination
    {
        "name": "2x2",
        "matrix": [
            [0, 1],
            [3, 2]
        ]
    },
    # Right Termination
    {
        "name": "4x3",
        "matrix": [
            [0,  1,  2, 3],
            [9, 10, 11, 4],
            [8,  7,  6, 5]
        ]
    },
    # Down Termination
    {
        "name": "3x4",
        "matrix": [
            [0,  1, 2],
            [9, 10, 3],
            [8, 11, 4],
            [7,  6, 5]
        ]
    },
    # Up termination
    {
        "name": "2x3",
        "matrix": [
            [0, 1],
            [5, 2],
            [4, 3]
        ]
    },
    # Multi Spiral
    {
        "name": "5x5",
        "matrix": [
            [ 0,  1,  2,  3, 4],
            [15, 16, 17, 18, 5],
            [14, 23, 24, 19, 6],
            [13, 22, 21, 20, 7],
            [12, 11, 10,  9, 8],
        ]
    },
]

for _, test in enumerate(test_cases):
    result = iterate_matrix_clockwise(test["matrix"])
    passing = True
    for i, n in enumerate(result):
        if i != n:
            passing = False
            print("%s: FAIL. Got " % test["name"], result)
            break
    if passing:
        print("%s: pass" % test["name"])
