# 🚀 Asteroids Game (Python + Pygame)

A classic **Asteroids-style arcade game** built with **Python** and **Pygame**.

The project was created as a programming practice project to learn:

* object-oriented programming;
* game loops and real-time updates;
* sprite management;
* collision detection;
* vector movement;
* game state management.

## 🎮 Features

### Player

* Control the spaceship using keyboard:

  * `W` — move forward
  * `S` — move backward
  * `A` / `D` — rotate left and right
  * `SPACE` — shoot

The player movement is based on vector rotation and speed calculations.

### Asteroids

* Asteroids spawn automatically from screen edges.
* Each asteroid has:

  * position;
  * velocity;
  * radius;
  * movement logic.

Large asteroids split into smaller ones when destroyed.

### Shooting System

* The player can fire projectiles.
* Bullets move according to the ship's direction.
* Shooting has a cooldown to limit the fire rate.

### Collision System

The game includes circle-based collision detection:

* player ↔ asteroid
* shot ↔ asteroid

When collisions happen:

* the player loses the game;
* asteroids are destroyed;
* explosions are created.

### Explosion Effects

Destroyed asteroids create a visual explosion effect:

* expanding orange circle;
* temporary animation;
* automatic removal after its lifetime ends.

### Score System

The game tracks the player's score.

Points are awarded for destroying asteroids and displayed on the screen.

## 🏗️ Project Structure

```
Asteroids/
│
├── main.py              # Game loop and initialization
├── player.py            # Player spaceship logic
├── asteroid.py          # Asteroid behavior and splitting
├── asteroidfield.py     # Asteroid spawning system
├── shot.py              # Bullet/projectile logic
├── explosion.py         # Explosion visual effects
├── circleshape.py       # Base class for circular objects
├── constants.py         # Game constants
├── logger.py            # Game event logging
│
└── README.md
```

## 🧩 Architecture

The game uses `pygame.sprite.Group` containers:

* `updatable` — objects that receive updates every frame;
* `drawable` — objects that are rendered on the screen;
* `asteroids` — active asteroid objects;
* `shots` — active projectiles.

Objects automatically register themselves into required groups through the `containers` pattern.

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd Asteroids
```

Install dependencies:

```bash
pip install pygame
```

## ▶️ Running the Game

Start the game:

```bash
python main.py
```

## 🕹️ Gameplay

The goal is to survive as long as possible and destroy as many asteroids as you can.

* Avoid collisions.
* Destroy asteroids.
* Earn points.
* Try to beat your high score.

## 🧠 What I Learned

During this project I practiced:

* Python classes and inheritance;
* object composition;
* Pygame sprites;
* game loops;
* delta time (`dt`);
* vector mathematics;
* collision detection;
* event handling;
* managing multiple game objects.

## 🔮 Possible Future Improvements

Ideas for future development:

* player lives system;
* high score saving;
* sound effects;
* particle explosions;
* animated sprites;
* asteroid textures;
* power-ups;
* levels with increasing difficulty.

## 📌 Technologies

* Python 3
* Pygame
* Git
* Object-Oriented Programming
