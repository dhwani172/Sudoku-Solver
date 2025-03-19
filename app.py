from flask import Flask, request, jsonify
from flask_cors import CORS
import SudokuSolver

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    board = data['board']
    if SudokuSolver.solve_sudoku(board):
        return jsonify({"status": "success", "board": board})
    else:
        return jsonify({"status": "failure", "message": "No solution exists"})

if __name__ == '__main__':
    app.run(debug=True)




