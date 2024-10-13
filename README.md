# Pong Game vs rule-based AI

## Description
Pong Game is a classic arcade-style game implemented in Python using the Turtle graphics library. The game features two paddles (one controlled by the player and the other by AI), a bouncing ball, and a scoring system. Players have three lives represented by hearts, which are displayed at the top right corner of the screen. If the player loses all hearts, a game over message is displayed, accompanied by sound effects.

## Features
- **Two Paddles**: One controlled by the player (using the keyboard) and the other controlled by AI.
- **Ball Mechanics**: The ball bounces off the paddles and walls, simulating realistic gameplay.
- **Lives System**: Players start with three lives represented by heart icons. Each time the player misses the ball, a heart is removed.
- **Game Over**: When the player loses all hearts, a game over message is displayed, and a sound is played.
- **Simple AI**: The left paddle is controlled by a basic AI that moves according to the ball's position.

## Requirements
- Python 3.x
- `pygame` library for sound handling
- `turtle` module (comes with Python)

## Installation
Clone the repository:
```
git clone https://github.com/NMAMII/Rule-based-AI-Pong.git
```
Navigate to the project directory:
```
cd pong-game
```
Install required packages:
```
pip install pygame
```
## Usage
Run the game using Python:
```
python main.py
```
Control the right paddle using the Up and Down arrow keys.

### Sound Effects
A game over sound effect (game_over.mp3) is included.
## Future Improvements
- Implement reinforcement learning (RL) to create a learning AI opponent.
- Add more visual features (e.g., game over screen, difficulty levels).
- Support for two-player local gameplay.
