"""Load the AI101 search maze."""
from pathlib import Path

MAZE_FILE = Path(__file__).resolve().parent / "data" / "maze.txt"


def load_maze(path=MAZE_FILE):
    """Return (grid, start, goal).

    grid is a list of strings, one per row: "#" is a wall, "." is open floor,
    "S" is the start and "G" is the goal. start and goal are (row, column) tuples.
    """
    grid = Path(path).read_text(encoding="utf-8").splitlines()
    start = goal = None
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "S":
                start = (r, c)
            elif cell == "G":
                goal = (r, c)
    return grid, start, goal


if __name__ == "__main__":
    grid, start, goal = load_maze()
    print("\n".join(grid))
    print(f"{len(grid)} rows x {len(grid[0])} columns, start {start}, goal {goal}")
