# item-measurement-tool

## Overview
The Item Measurement Tool is a Python script designed to help operators determine the optimal orientation for items into a specific packing machine. By automating the orientation decision process, this tool reduces human error by up to 25%, ensuring faster and more consistent packaging, leading to increased efficiency.

## Features
- Calculates optimal item orientation for packaging.
- Provides recommendations for either "Standard" or "Stand-Tall" orientation.
- 3D visualization of item placement for better understanding.

## Installation
To use the tool, you need Python 3.x installed on your system. Then, install the required libraries:

```sh
pip install -r requirements.txt
```

## Usage
To run the tool, enter the following command:

```sh
python src/packaging_tool.py
```

Follow the prompts to enter item dimensions.

## Example
```sh
Enter the length of the item (in inches): 6
Enter the width of the item (in inches): 4
Enter the height of the item (in inches): 2
```
The tool will then display the optimal orientation along with a 3D visualization.

## Challenges and Solutions
- **Algorithm Refinement**: Improved the logic for handling similar dimensions to ensure accurate recommendations.
- **Visualization Accuracy**: Enhanced the 3D visualization to align precisely with calculated orientations.

## Interactive Demo
You can find a video demo of how the tool works [here](https://portfolio.slamminstam.com/images/video_measurement-tool_demo_v1.0.0.mp4).

## Key Learning Outcomes
- Improved skills in algorithm development and Python error handling.
- Gained experience in creating interactive visualizations.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
