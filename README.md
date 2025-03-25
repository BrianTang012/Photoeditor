# Image Processing Tool

## Overview
The Image Processing Tool provides an interactive interface to apply various transformations and effects to images. The tool allows the user to adjust image brightness, contrast, apply filters such as blur and edge detection, convert to grayscale, and make selections on the image using rectangle and magic wand methods.

## Features
- **Change Brightness**: Adjust the brightness of the image.
- **Change Contrast**: Modify the contrast of the image.
- **Convert to Grayscale**: Convert the image to grayscale.
- **Apply Blur Effect**: Blur the image for a softening effect.
- **Apply Edge Detection**: Detect and highlight the edges within the image.
- **Apply Embossed Effect**: Apply an embossed effect to give the image a 3D appearance.
- **Rectangle Selection**: Select and manipulate a rectangular region of the image.
- **Magic Wand Selection**: Select pixels based on color similarity, with customizable tolerance.

## Requirements
- Python 3.x
- Numpy
- Matplotlib

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Install the required dependencies:
    ```bash
    pip install numpy matplotlib
    ```

## Usage

1. Replace `"your_image.png"` in the code with the path to your image file.
2. Run the script to start the interactive menu:
    ```bash
    python image_processing_tool.py
    ```

3. In the interactive menu, you can:
   - Enter `1` to change the brightness.
   - Enter `2` to change the contrast.
   - Enter `3` to convert the image to grayscale.
   - Enter `4` to apply a blur effect.
   - Enter `5` to apply edge detection.
   - Enter `6` to apply the embossed effect.
   - Enter `7` to make a rectangular selection.
   - Enter `8` to make a magic wand selection.
   - Enter `d` to display the image after modification.
   - Enter `q` to quit the application.

### Example Workflow

1. Start the script and choose an option from the interactive menu.
2. For example, to adjust brightness:
    - Enter `1` and input the desired brightness change (positive or negative).
3. To apply a blur effect:
    - Enter `4` to soften the image.
4. Use `d` to display the current image at any point.

