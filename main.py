def create_grid(m: int, n: int) -> list[list[str]]:
    """
    Creates a grid of size M x N filled with blank spaces " ".
    :param m: Number of rows
    :param n: Number of columns
    :returns: A 2D list representing an M x N grid
    """
    grid = []
    for l in range(m):
        line = []
        for c in range(n):
            line.append(' ')
        grid.append(line)
    for line in grid:
        print(''.join(line),end='')

create_grid(5,5)

def print_grid(grid: list[list[str]]) -> None:
    for line in grid:
        print(''.join(line),end='')

    """
    Prints the grid to the console.
    :param grid: A 2D list representing the grid
    """
    ''
    # Hint: check the join method for strings and the len function for lists
    # Hint: check the end parameter of the print function to avoid printing a newline character
    pass

def to_coordinates(text: str) -> tuple[int, int]:
    """
    Converts a string coordinates to a tuple of integers.
    :param text: A string representing the coordinates (e.g., "A1")
    :returns: A tuple of integers representing the row and column indices
    """
    # Hint: check the ord function to convert a character to its ASCII code
    # Hint: check the int function to convert a string to an integer
    pass

def add_boat(grid: list[list[str]], start: str, stop: str) -> bool:
    """
    Adds a boat to the grid, specified by start and stop coordinates.
    :param grid: A 2D list representing the grid
    :param start: Starting coordinates of the boat (e.g., "A1")
    :param stop: Ending coordinates of the boat (e.g., "A3")
    :returns: True if the boat was added successfully, False otherwise
    """
    # Hint: use the to_coordinates function
    # Hint: check the boundaries to avoid placing a boat outside the grid
    pass

if __name__ == "__main__":
    grid = create_grid(10, 10)
    add_boat(grid, "B2", "B5")
    print_grid(grid)