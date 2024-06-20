from django.shortcuts import render
from django import forms

class SudokuForm(forms.Form):
    cell_0 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_1 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_2 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_3 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_4 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_5 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_6 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_7 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_8 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_9 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_10 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_11 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_12 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_13 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_14 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_15 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_16 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_17 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_18 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_19 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_20 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_21 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_22 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_23 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_24 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_25 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_26 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_27 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_28 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_29 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_30 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_31 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_32 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_33 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_34 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_35 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_36 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_37 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_38 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_39 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_40 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_41 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_42 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_43 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_44 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_45 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_46 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_47 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_48 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_49 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_50 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_51 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_52 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_53 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_54 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_55 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_56 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_57 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_58 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_59 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_60 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_61 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_62 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_63 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_64 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_65 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_66 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_67 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_68 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_69 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_70 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_71 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_72 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_73 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_74 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_75 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_76 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_77 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_78 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_79 = forms.IntegerField(min_value=0, max_value=9, required=False)
    cell_80 = forms.IntegerField(min_value=0, max_value=9, required=False)

class SudokuForm(forms.Form):
    for i in range(81):
        exec(f'cell_{i} = forms.IntegerField(min_value=0, max_value=9, required=False)')

def index(request):
    if request.method == 'POST':
        form = SudokuForm(request.POST)
        if form.is_valid():
            grid = []
            for i in range(9):
                row = []
                for j in range(9):
                    row.append(form.cleaned_data[f'cell_{i * 9 + j}'] or 0)
                grid.append(row)
            solved_grid = [row[:] for row in grid]  # Make a deep copy of the grid
            if solve_sudoku(solved_grid):
                return render(request, 'solver/result.html', {'board': solved_grid})
            else:
                return render(request, 'solver/result.html', {'board': None, 'error': 'Sudoku puzzle cannot be solved.'})
    else:
        form = SudokuForm()
    return render(request, 'solver/index.html', {'form': form})

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False
    for x in range(9):
        if board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_location = find_empty_location(board)
    if not empty_location:
        return True
    row, col = empty_location

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False