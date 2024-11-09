# Packaging Measurement Tool - Documentation

## Overview
The Packaging Measurement Tool is a Python-based utility designed to help operators determine the optimal orientation for packaging items in fulfillment centers. It automates the decision-making process regarding how to place an item for packaging based on its dimensions, reducing human error and optimizing packaging operations.

The tool works by calculating the sum of the length and height of an item to determine if it should be oriented in a "Standard" or "Stand-Tall" position. Additionally, a 3D visualization feature provides operators with a visual representation to ensure proper understanding of item orientation.

## Features
- **Automated Orientation Decision**: Determines if items should be placed in a "Standard" or "Stand-Tall" orientation based on the sum of their length and height.
- **3D Visualization**: Uses `matplotlib` to generate a visual representation of how the item should be positioned.
- **Error Handling**: Provides context-sensitive error messages to help users input correct dimensions.
- **Built-In Help**: Users can type 'help' at any prompt to receive instructions on how to use the tool.

## Installation
To install and run the Packaging Measurement Tool, follow these steps:

### Prerequisites
- **Python 3.x**: The tool requires Python version 3 or above.
- **Dependencies**: The following Python libraries are required:
  - `matplotlib`
  - `numpy`

You can install these dependencies by running:
```sh
pip install -r requirements.txt
```

### Running the Tool
To use the tool, navigate to the folder where the script is located and execute the following command:
```sh
python src/packaging_tool.py
```

## Usage
Once you run the script, you will be prompted to enter the item dimensions (length, width, height) in inches. Depending on the inputs, the tool will suggest an optimal orientation:

- **Standard**: Lay the item flat with its longest side as the primary axis.
- **Stand-Tall**: Stand the item vertically with the longest side upright.
- **Sideline**: If the item's dimensions exceed certain thresholds, the tool will suggest not inducting the item.

### Example
```sh
Enter the length of the item (in inches): 6
Enter the width of the item (in inches): 4
Enter the height of the item (in inches): 2
```
The output will specify whether to use "Standard" or "Stand-Tall" orientation. A 3D visualization window will also appear, showing how the item should be placed.

## Visual Representation
The 3D visualization is a key feature of this tool. It helps the operator see the recommended positioning for the item. A 3D cuboid representing the item is displayed with an arrow indicating the correct orientation and machine induction direction. The axis labels are designed to align with the physical orientation of the packaging station.

The visualization helps minimize errors and confusion, especially in fulfillment environments with a high volume of varied item sizes.

## How It Works
1. **Input Validation**: Users are prompted to enter numeric values for length, width, and height. If non-numeric inputs are detected, an error message is shown, and users are prompted again.
2. **Orientation Decision Logic**:
   - If `length + height > 14 inches`, the tool suggests sidelining the item.
   - If `12 inches <= length + height <= 14 inches`, it recommends the "Stand-Tall" orientation.
   - Otherwise, it recommends the "Standard" orientation.
3. **3D Visualization**: Based on the recommended orientation, a 3D visualization is generated, showing how to position the item.

## Challenges and Solutions
### Algorithm Refinement
Initially, the algorithm struggled with items where the length and width were nearly identical, leading to inconsistent recommendations. To address this, a tolerance range was added to ensure more consistent and accurate decisions, making the logic more robust.

### Visualization Accuracy
The visual representation initially did not always match the calculated orientation, leading to confusion. Dynamic adjustments were made to the plot parameters to ensure the 3D model aligns with the dimensions provided by the user, offering greater clarity.

### Error Handling
Early feedback indicated that the error messages were too vague, leading to confusion for new users. Context-specific messages were added, such as prompts to ensure dimensions were positive numbers. This improvement reduced the number of user errors and made the tool more accessible.

## Future Improvements
- **User Interface (UI)**: Develop a Graphical User Interface (GUI) using `Tkinter` to make the tool more user-friendly for operators without technical backgrounds.
- **More Orientation Types**: Expand the decision-making logic to consider other orientations, optimizing not just by dimensions but also by weight distribution and item fragility.
- **Batch Processing**: Add support for handling multiple items at once, allowing operators to input a list of dimensions for bulk analysis.

## Troubleshooting
### Common Errors
- **Invalid Input**: If non-numeric or negative numbers are entered, the tool will prompt for valid input. Double-check the values to ensure they are correct.
- **Visualization Not Displaying**: Ensure that `matplotlib` is installed correctly. If running remotely or on a server, ensure that display capabilities are available.

### Getting Help
If you encounter issues, use the 'help' command at any prompt within the script for more guidance.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Special thanks to all contributors who helped refine the logic and improve the visualization features. The Packaging Measurement Tool is a product of iterative design and feedback aimed at making warehouse operations more efficient.
