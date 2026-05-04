# Snake in Tkinter

A small desktop Snake game built with Python and Tkinter.

This project was created as a personal learning project focused on practicing object-oriented programming, GUI event handling, game state management and basic game logic in Python.

The project was originally developed and tested on Windows.  
It may also run on Linux, but window icon behavior can differ depending on the operating system and Tkinter environment.

---

## Features

- Snake movement on a Canvas-based game board.
- Keyboard controls.
- Button controls.
- Fruit generation outside the snake body.
- Score tracking.
- High score saved in a text file.
- Collision detection with walls and the snake body.
- Automatic reset after collision.

---

## Tech stack

- Python
- Tkinter
- Canvas

---

## What I practiced

This project helped me practice:

- object-oriented programming in Python,
- separating GUI setup from game logic,
- event handling,
- game loop logic,
- working with coordinates,
- collision detection,
- simple file handling for high score,
- code organization and refactoring.

---

## Project structure

```text
snake.py          # Main GUI setup and application loop
snake_body.py     # Snake class and game logic
high_score.txt    # Saved high score
assets/           # Icons and other graphical assets
