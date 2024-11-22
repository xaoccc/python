import matplotlib.pyplot as plt
import numpy as np
from random import randint
from time import sleep


def generate_random_color():
    """Generates a random RGB color."""
    return randint(0, 255), randint(0, 255), randint(0, 255)


def plot_grid(darts, title):
    """Plots the grid using Matplotlib."""
    # Create a color map for visualization
    color_map = {
        "current_color": (0, 255, 0),  # Green
        "red": (255, 0, 0),  # Red
        "white": (255, 255, 255)  # White
    }
    random_colors = {}

    # Generate color grid
    color_grid = []
    for row in darts:
        color_row = []
        for cell in row:
            if cell.startswith("#"):  # For random colors
                if cell not in random_colors:
                    random_colors[cell] = generate_random_color()
                color_row.append(random_colors[cell])
            else:
                color_row.append(color_map[cell])
        color_grid.append(color_row)

    color_grid = np.array(color_grid) / 255  # Normalize RGB values to [0, 1]

    plt.imshow(color_grid, interpolation="nearest")
    plt.title(title)
    plt.axis("off")
    plt.show()


def mark(darts, row, col):
    """Marks connected cells of the same color starting from (row, col)."""
    if row < 0 or row > 6 or col < 0 or col > 6:
        return

    if darts[row][col] != "current_color":
        return

    # Mark the current cell as red
    darts[row][col] = "red"

    # Recursively mark neighboring cells
    mark(darts, row - 1, col)
    mark(darts, row, col - 1)
    mark(darts, row + 1, col)
    mark(darts, row, col + 1)


def unmark(darts, row, col):
    """Reverts marked cells (red) back to a random color."""
    if row < 0 or row > 6 or col < 0 or col > 6:
        return

    if darts[row][col] != "red":
        return

    # Change the marked cell to a random color
    darts[row][col] = f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"

    # Recursively unmark neighboring cells
    unmark(darts, row - 1, col)
    unmark(darts, row, col - 1)
    unmark(darts, row + 1, col)
    unmark(darts, row, col + 1)


def shoot(hit_sector, darts, throw):
    """Handles the shooting action with visualization."""
    if hit_sector == "current_color":
        print("Before marking:")
        plot_grid(darts, "Before Marking")

        # Mark the target area
        mark(darts, throw[0], throw[1])
        print("After marking:")
        plot_grid(darts, "After Marking")
        sleep(1)

        # Unmark the area (reverting to random colors)
        unmark(darts, throw[0], throw[1])
        print("After unmarking:")
        plot_grid(darts, "After Unmarking")


# Initialize the darts board
darts = [
    ["current_color", "current_color", "white", "white", "white", "white", "white"],
    ["white", "current_color", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white", "white"],
]

# Simulate a shot at position (0, 0) hitting the "current_color" sector
shoot("current_color", darts, (0, 0))


def onclick(event):
    """Handles mouse click events."""
    if event.xdata is None or event.ydata is None:
        return  # Ignore clicks outside the axes

    # Convert click coordinates to grid indices
    col = int(event.xdata)
    row = int(event.ydata)

    # Check if the click is within bounds
    if 0 <= row < len(darts) and 0 <= col < len(darts[0]):
        if darts[row][col] == "current_color":
            mark(darts, row, col)
        elif darts[row][col] == "red":
            unmark(darts, row, col)
        update_plot()


def update_plot():
    """Updates the plot after marking or unmarking."""
    ax.clear()
    plot_grid(ax, darts)
    fig.canvas.draw()


# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
plot_grid(ax, darts)
fig.canvas.mpl_connect("button_press_event", onclick)

plt.title("Click on a Cell to Mark/Unmark")
plt.show()