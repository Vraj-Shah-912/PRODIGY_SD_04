from django.shortcuts import render
from .forms import SudokuForm
from .sudoku_solver import solve_sudoku

def parse_input(grid_str):
    rows = grid_str.strip().split("\n")
    board = []
    for row in rows:
        board.append([int(x) if x != '.' else 0 for x in row.split()])
    return board

def index(request):
    if request.method == "POST":
        form = SudokuForm(request.POST)
        if form.is_valid():
            grid_str = form.cleaned_data['grid']
            board = parse_input(grid_str)
            solve_sudoku(board)
            return render(request, 'solver/result.html', {'board': board})
    else:
        form = SudokuForm()
    return render(request, 'solver/index.html', {'form': form})
