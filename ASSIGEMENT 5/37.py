def solve(n):
    board = [["."] * n for _ in range(n)]
    results = []

    def backtrack(row):
        if row == n:
            results.append(["".join(r) for r in board])
            return

        for col in range(n):
            safe = True

            for r in range(row):
                if (board[r][col] == "Q" or
                    (row-r == abs(col - board[r].index("Q")))):
                    safe = False
                    break

            if safe:
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)
    return results


for board in solve(4):
    for row in board:
        print(row)
    print()







    """..Q.
Q...
...Q
.Q.."""