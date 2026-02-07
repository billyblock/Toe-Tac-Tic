# Toe Tac Tic (Misere Tic Tac Toe)

## Overview

This project is a command line toe tac tic written in python that features an AI opponent using the Minimax algorithm to **always** choose the best move.

The AI enumerates every possible future boeard state, assigns scores based on win / loss / tie outcomes. It then selects the move that maximizes the it's chances of winning.

Toe Tac Tic (also known as Misere Tic Tac Toe) has the reverse goal of normal Tic Tac Toe. In Toe Tac Tic, you try to force the opponent into 3 in a row, resulting in a win for you.

## Features

- Fully playable player vs. AI Toe Tac Tic game.
- The AI using Minimax to determine the best move.
- Depth based scoring to prefer faster wins and slow losses.

## Example

```
Current Board:
 | | 
-+-+-
 | | 
-+-+-
 | | 
Select a Row (1-3): 2
Select a Column (1-3): 2

Current Board:
O| | 
-+-+-
 |X| 
-+-+-
 | | 
Select a Row (1-3): 3
Select a Column (1-3): 3

Current Board:
O|O| 
-+-+-
 |X| 
-+-+-
 | |X
Select a Row (1-3): 3
Select a Column (1-3): 2

Current Board:
O|O| 
-+-+-
 |X|O
-+-+-
 |X|X
Select a Row (1-3): 2
Select a Column (1-3): 1

Current Board:
O|O| 
-+-+-
X|X|O
-+-+-
O|X|X
Select a Row (1-3): 1
Select a Column (1-3): 3

Current Board:
O|O|X
-+-+-
X|X|O
-+-+-
O|X|X
Game result: tie
```

## Running the Program

Just press run!

## Why I built this?

This was a starter project in my AI course. It was to intoduce us to the idea that computer intelligence is honestly just an algorithm at the core.
