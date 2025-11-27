SIZE = 9

def find_empty(board):
    # Ищем пустую клетку (0)
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return r, c
    return None

def is_valid(board, row, col, num):
    # Проверяем строку
    for c in range(SIZE):
        if board[row][c] == num:
            return False
    # Проверяем столбец
    for r in range(SIZE):
        if board[r][col] == num:
            return False
    # Проверяем квадрат 3x3
    sr = (row // 3) * 3
    sc = (col // 3) * 3
    for r in range(sr, sr + 3):
        for c in range(sc, sc + 3):
            if board[r][c] == num:
                return False
    return True

def solve_sudoku(board):
    pos = find_empty(board)
    # Если пустых нет — решено
    if not pos:
        return True
    row, col = pos

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num  # ставим число
            if solve_sudoku(board):  # рекурсивно решаем дальше
                return True
            board[row][col] = 0      # откат, если не получилось
    return False

# пример доски (0 — пусто)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

if solve_sudoku(board):
    print("Решённый судоку:")
    for row in board:
        print(row)
else:
    print("Решения нет")
