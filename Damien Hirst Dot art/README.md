# Turtle Dot Painting

## Overview

This Python script creates a colorful dot painting using the Turtle graphics library. It randomly selects colors from a predefined list to draw dots in a grid pattern, making use of Python's built-in `turtle` module and the `random` module for color selection.

## Features

- Draws 100 dots in a 10x10 grid pattern.
- Each dot is colored randomly from a predefined list of RGB color tuples.
- The script uses Turtle graphics, making it a visually engaging way to practice and understand Python coding and the Turtle module.

## Requirements

- Python 3.x
- Turtle Graphics Module (comes standard with Python)

## Installation

No additional installation is required apart from Python itself. This script is standalone and utilizes modules that are included with Python's standard library.

## Usage

To run the script, simply execute the Python file from your terminal or command prompt:

```
python main.py
```

Once the script is running, a window will open displaying the Turtle graphics screen. The script will automatically start drawing the dot painting. When the drawing is complete, click anywhere on the Turtle graphics window to exit.

## How It Works

- The script sets up a Turtle object and a Screen object with RGB color mode enabled.
- The Turtle's speed is set to the fastest to expedite the drawing process.
- The Turtle moves to a starting position and begins drawing dots, each with a random color selected from a predefined list.
- After drawing 10 dots in a row, the Turtle moves to the next row to continue the pattern until 100 dots have been drawn in total.
- The user can exit the drawing by clicking on the Turtle graphics window.

## Customization

You can customize the dot painting by modifying the `color_list` to include colors of your choice. Additionally, the `number_of_dots` can be adjusted to create a larger or smaller painting, though you may need to adjust the movement logic to accommodate a different grid size.

## License

This project is open source and available for use and modification. Feel free to share or adapt it as needed.

---

This README provides a basic introduction and guide for users to run and understand your Turtle graphics project. Adjustments can be made to fit the specific details or requirements of your project or coding environment.
