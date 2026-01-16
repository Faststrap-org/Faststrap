"""
Example: Tic-Tac-Toe Game

Demonstrates: Interactive game with HTMX
Components: Button, Card, Alert, Badge
Difficulty: Intermediate

A complete tic-tac-toe game showing:
- Game state management
- Win detection
- Score tracking
- Reset functionality
- Responsive game board
"""

from fasthtml.common import *

from faststrap import *

app = FastHTML()
add_bootstrap(app)

# Game state
board = [""] * 9
current_player = "X"
scores = {"X": 0, "O": 0, "draws": 0}
game_over = False
winner = None


def check_winner():
    """Check if there's a winner"""
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # Rows
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # Columns
        [0, 4, 8],
        [2, 4, 6],  # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]

    if "" not in board:
        return "draw"

    return None


def game_board():
    """Render the game board"""
    return Div(
        *[
            Button(
                board[i] or " ",
                variant=(
                    "outline-primary"
                    if not board[i]
                    else ("primary" if board[i] == "X" else "success")
                ),
                hx_post=f"/move/{i}",
                hx_target="#game-container",
                hx_swap="outerHTML",
                disabled=bool(board[i] or game_over),
                style={
                    "width": "100px",
                    "height": "100px",
                    "font-size": "2rem",
                    "font-weight": "bold",
                },
            )
            for i in range(9)
        ],
        cls="d-grid gap-2",
        style={"grid-template-columns": "repeat(3, 100px)", "justify-content": "center"},
    )


@app.get("/")
def index():
    """Game main page"""
    return Container(
        Div(
            H1("Tic-Tac-Toe", cls=f"text-center {Fx.fade_in}"),
            # Score board
            Row(
                Col(
                    Card(
                        H5("Player X", cls="text-center"),
                        H2(str(scores["X"]), cls="text-center text-primary"),
                        cls="text-center",
                    ),
                    md=4,
                ),
                Col(
                    Card(
                        H5("Draws", cls="text-center"),
                        H2(str(scores["draws"]), cls="text-center text-secondary"),
                        cls="text-center",
                    ),
                    md=4,
                ),
                Col(
                    Card(
                        H5("Player O", cls="text-center"),
                        H2(str(scores["O"]), cls="text-center text-success"),
                        cls="text-center",
                    ),
                    md=4,
                ),
                cls="mb-4",
            ),
            # Game container
            Div(game_status(), game_board(), id="game-container"),
            # Reset button
            Button(
                Icon("arrow-clockwise"),
                " New Game",
                variant="outline-secondary",
                hx_post="/reset",
                hx_target="#game-container",
                hx_swap="outerHTML",
                cls="mt-4 d-block mx-auto",
            ),
            id="game-area",
            cls=f"{Fx.fade_in}",
        ),
        cls="py-5",
        style={"max-width": "600px"},
    )


def game_status():
    """Render game status message"""
    if game_over:
        if winner == "draw":
            return Alert("It's a draw!", variant="secondary", cls="text-center mb-3")
        else:
            return Alert(f"Player {winner} wins! 🎉", variant="success", cls="text-center mb-3")
    else:
        player_color = "primary" if current_player == "X" else "success"
        return Alert(
            "Current player: ",
            Badge(current_player, variant=player_color),
            variant="info",
            cls="text-center mb-3",
        )


@app.post("/move/{position}")
def make_move(position: int):
    """Handle player move"""
    global board, current_player, game_over, winner, scores

    if not game_over and not board[position]:
        board[position] = current_player

        # Check for winner
        result = check_winner()
        if result:
            game_over = True
            winner = result
            if result == "draw":
                scores["draws"] += 1
            else:
                scores[result] += 1
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

    return Div(game_status(), game_board(), id="game-container")


@app.post("/reset")
def reset_game():
    """Reset the game"""
    global board, current_player, game_over, winner
    board = [""] * 9
    current_player = "X"
    game_over = False
    winner = None

    return Div(game_status(), game_board(), id="game-container")


if __name__ == "__main__":
    serve(port=5019)
