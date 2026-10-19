# pygames

A small collection of retro games written in Python with
[pygame-ce](https://pyga.me/) (the community edition of pygame).

## Games

### Lode Runner (`loderunner.py`)

A mini Lode Runner clone. Collect all the gold — once the last gold pile is
picked up, an exit ladder appears at the right side of the map. Reach it to
advance to the next level; clearing the last level wins the game. Running into
an enemy ends the game.

Run it with:

```sh
python3 loderunner.py
```

Controls:

| Key | Action |
| --- | --- |
| Arrow keys | Move (hold to keep moving, release to stop) |

Options:

| Option | Description |
| --- | --- |
| `--tick-ms N` | Milliseconds between clock ticks (game refresh rate, default 20). Game speed is independent of the tick rate: entities move based on elapsed time, not tick counts. |
| `--level LEVEL` | Level to start on, 1 to 2 (default 1). |

Example:

```sh
python3 loderunner.py --tick-ms 10 --level 2
```

### Snake (`snake.py`)

A self-driving Snake game. The snake follows a Hamiltonian cycle over the
board and shortcuts towards the food whenever it is safe to do so, so it
never traps itself.

Run it with:

```sh
python3 snake.py
```

Controls:

| Key | Action |
| --- | --- |
| Up | Speed up |
| Down | Slow down |

## Setup

Requirements: Python 3 and the packages listed in [requirements.txt](requirements.txt)
(currently [pygame-ce](https://pyga.me/), the community edition of pygame).

> **Note:** pygame-ce is a drop-in replacement for pygame: it installs the
> same `pygame` module, so the game code needs no changes. Unlike classic
> pygame, pygame-ce ships wheels for recent Python versions, so a plain
> `pip install -r requirements.txt` usually works on a current interpreter.
> If no wheel is available for your Python version, create the virtual
> environment with an older interpreter instead:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the games with the virtual environment activated (or call
`.venv/bin/python` directly):

```sh
python loderunner.py
python snake.py
```

When you are done, deactivate the environment with:

```sh
deactivate
```
