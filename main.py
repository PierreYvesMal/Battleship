def create_grid(m: int, n: int) -> list[list[str]]:
    """
    Creates a grid of size M x N filled with blank spaces " ".
    :param m: Number of rows
    :param n: Number of columns
    :returns: A 2D list representing an M x N grid
    """
    pass

def print_grid(grid: list[list[str]]) -> None:
    """
    Prints the grid to the console.
    :param grid: A 2D list representing the grid
    """
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

def human_preparation(grid: list[list[str]]) -> list[list[str]]:
    """
    The human is prompted to enter coordinates to place their boats.
    The grid is marked with "B" for each cell occupied by a boat.
    :param grid: A 2D list representing the grid
    """
    boats = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2
    }
    print("Place your boats on the grid.")
    for boat_name, boat_length in boats.items():
        boat_success = False # Flag to check if the boat was placed successfully
        while not boat_success: # If the boat was not placed successfully, the whole boat placing process should be repeated
            print(f"Placing boat: {boat_name} (length: {boat_length})")
            start = input("Enter the starting coordinates of the boat (e.g., A1): ")
            stop = input("Enter the ending coordinates of the boat (e.g., A3): ")
            #TODO
    # Hint: Check the boundaries and emptiness of the cell before placing a boat.
    # Hint: If the boat was not placed successfully, the whole boat placing process should be started over.

def computer_preparation(grid: list[list[str]]):
    """
    The computer randomly places boats on the grid.
    The grid is marked with "B" for each cell occupied by a boat.
    :param grid: A 2D list representing the grid
    """
    # Hint: Use the random module to generate random coordinates for the boats
    # Hint: Check the boundaries and emptiness of the cell before placing a boat.
    pass

if __name__ == "__main__":
    human_grid = create_grid(10, 10)
    human_preparation(human_grid)
