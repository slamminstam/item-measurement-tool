import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def get_item_orientation(length, width, height):
    """
    Determine the optimal orientation for the packaging item.
    Items with length + height greater than 12" (and up to 14") should be positioned vertically.
    Items with dimensions adding to less than 12" should be inducted horizontally and placed centered in the bag.
    
    Parameters:
        length (float): Length of the item.
        width (float): Width of the item.
        height (float): Height of the item.

    Returns:
        str: Recommended orientation of the item.
    """
    # Calculate the sum of length and height
    length_height_sum = length + height

    # Determine orientation based on length and height criteria
    if length + height > 14:
        return "Sideline: Item exceeds dimensions for standard induction. Do not induct."
    if 12 <= length_height_sum <= 14:
        return "Stand-Tall: Position with longest side standing vertically, centered, all the way to the back of the bag"
    elif length + width + height < 12:
        return "Standard: Lay flat with longest side as primary axis, place centered and all the way back"
    else:
        # General lay flat rule for larger items
        return "Standard: Lay flat with longest side as the primary axis, place centered and all the way back"


def get_optimal_orientation(length, width, height):
    """
    Determine the optimal orientation configuration for the packaging item.
    This function considers all possible orientations to find the one that
    minimizes the space needed for efficient packaging.
    
    Parameters:
        length (float): Length of the item.
        width (float): Width of the item.
        height (float): Height of the item.

    Returns:
        str: Optimal orientation of the item.
    """
    orientations = {
        'Length x Width': length * width,
        'Length x Height': length * height,
        'Width x Height': width * height
    }
    optimal_orientation = min(orientations, key=orientations.get)
    return f"Optimal orientation: {optimal_orientation}, Area: {orientations[optimal_orientation]} sq. inches"

def display_help():
    """
    Display help/documentation for the Packaging Measurement Tool.
    """
    help_text = """
    Packaging Measurement Tool Help Menu
    ------------------------------------
    This tool helps determine the optimal orientation for packaging items.
    
    Instructions:
    1. Enter the dimensions of the item (length, width, height) in inches when prompted.
    2. The tool will recommend the best orientation based on the measurements provided.
    3. Items with a combined length and height between 12" and 14" will be positioned vertically.
    4. Items with dimensions adding to less than 12" will be inducted horizontally, centered, and placed to the back of the bag.
    5. The tool will also calculate the optimal orientation to minimize the area required for packaging.
    
    Commands:
    - Enter numeric values when prompted to receive recommendations.
    - Type 'help' during input to display this help menu.
    """
    print(help_text)

def wrap_text(text, width=50):
    """
    Manually wrap text to fit within a certain width.
    
    Parameters:
        text (str): The text to be wrapped.
        width (int): Maximum number of characters per line.

    Returns:
        str: The wrapped text.
    """
    words = text.split()
    wrapped_lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > width:
            wrapped_lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)

    wrapped_lines.append(" ".join(current_line))
    return "\n".join(wrapped_lines)

def visualize_orientation_3d(length, width, height, orientation):
    """
    Visualize the item in 3D to provide better clarity for operators.
    
    Parameters:
        length (float): Length of the item.
        width (float): Width of the item.
        height (float): Height of the item.
        orientation (str): The recommended orientation of the item.
    """
    fig = plt.figure(figsize=(10, 8))  # Increased figure size for better visualization
    ax = fig.add_subplot(111, projection='3d')
    
    # Adjust dimensions and rotate the item based on orientation
    if "Stand-Tall" in orientation:
        # Stand tall - place the longest side as the vertical dimension
        if length >= width and length >= height:
            x, y, z = width, length, height
            induct_direction = (0, y, 0)  # Induct along y-axis from 0 -> length
            induct_text_location = (0, y / 2, 0)
        elif width >= length and width >= height:
            x, y, z = length, width, height
            induct_direction = (0, y, 0)  # Induct along y-axis from 0 -> width
            induct_text_location = (0, y / 2, 0)
        else:
            x, y, z = width, length, height
            induct_direction = (0, y, 0)  # Induct along y-axis from 0 -> height
            induct_text_location = (0, y / 2, 0)
        orientation_label = "Stand-Tall Orientation (Induct Vertically, Centered and Back)"
    elif "centered in the bag" in orientation:
        # Special case for small items - use given orientation explicitly
        x, y, z = length, height, width
        orientation_label = "Lay Flat, Centered in Bag (Induct Horizontally - Place to the Back)"
        induct_direction = (x, 0, 0)  # Horizontal induction direction
        induct_text_location = (x / 2, 0, 0)
    else:
        # Lay flat - determine the longest dimension for primary axis
        if length >= width and length >= height:
            x, y, z = length, min(width, height), max(width, height)
        elif width >= length and width >= height:
            x, y, z = width, min(length, height), max(length, height)
        else:
            x, y, z = height, min(length, width), max(length, width)
        orientation_label = "Lay Flat with Longest Side as Primary Axis (Induct Horizontally - Longest Side First, Place Centered and Back)"
        induct_direction = (x, 0, 0)  # Longest side direction induction
        induct_text_location = (x / 2, 0, 0)
    
    # Define the vertices of the cuboid
    vertices = [
        [0, 0, 0],
        [x, 0, 0],
        [x, y, 0],
        [0, y, 0],
        [0, 0, z],
        [x, 0, z],
        [x, y, z],
        [0, y, z]
    ]

    # Define the six faces of the cuboid
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # Bottom face
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # Front face
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # Top face
        [vertices[3], vertices[0], vertices[4], vertices[7]],  # Back face
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Left face
        [vertices[4], vertices[5], vertices[6], vertices[7]]   # Right face
    ]

    # Create a 3D polygon to represent the item
    poly3d = Poly3DCollection(faces, facecolors='skyblue', linewidths=1, edgecolors='r', alpha=.25)
    ax.add_collection3d(poly3d)
    
    # Highlight the recommended orientation with dynamic positioning
    wrapped_orientation_label = wrap_text(orientation_label, width=40)
    ax.text2D(0.05, 0.90, wrapped_orientation_label, transform=ax.transAxes, fontsize=12, color='red', fontweight='bold', bbox=dict(facecolor='white', alpha=0.8))
    
    # Add an arrow to indicate machine location and induction direction
    ax.quiver(0, 0, 0, *induct_direction, color='green', linewidth=4, arrow_length_ratio=0.2)
    ax.text(*induct_text_location, 'Machine Induct Direction', color='blue', fontsize=10, fontweight='bold', ha='center', va='center')
    
    # Set labels for clarity
    ax.set_xlabel('X Axis (inches)')
    ax.set_ylabel('Y Axis (inches)')
    ax.set_zlabel('Z Axis (inches)')
    ax.set_title('Stand Tall' if "Stand-Tall" in orientation else 'Standard', pad=20)
    
    # Set axis limits with a bit more margin for better visualization
    margin = 0.2 * max(x, y, z)
    ax.set_xlim([0, max(x, y, z) + margin])
    ax.set_ylim([0, max(x, y, z) + margin])
    ax.set_zlim([0, max(x, y, z) + margin])
    
    # Ensure tight layout without overlap
    plt.subplots_adjust(top=0.85, right=0.9)
    plt.show()


def main():
    """
    Main function to interact with the user and determine the packaging orientation.
    """
    print("Welcome to the Packaging Measurement Tool - Type 'help' at any prompt for help.")
    try:
        
        # Get item dimensions from the user
        user_input = input("Enter the length of the item (in inches): ").strip().lower()
        if user_input == 'help':
            display_help()
            return
        length = float(user_input)
        user_input = input("Enter the width of the item (in inches): ").strip().lower()
        if user_input == 'help':
            display_help()
            return
        width = float(user_input)
        user_input = input("Enter the height of the item (in inches): ").strip().lower()
        if user_input == 'help':
            display_help()
            return
        height = float(user_input)

        # Get the recommended orientation
        orientation = get_item_orientation(length, width, height)
        optimal_orientation = get_optimal_orientation(length, width, height)

        # Display the results
        print(f"Recommended orientation: {orientation}")
        print(optimal_orientation)

        # Visualize the orientation in 3D
        visualize_orientation_3d(length, width, height, orientation)
    except ValueError:
        print("Invalid input. Please enter numeric values for the dimensions.")

if __name__ == "__main__":
    main()
