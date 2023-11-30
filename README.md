# Chess-AI

My attempt at creating an AI chess bot, using Pytorch (Neural Net)

Pieces (7):
- Blank
- Pawn
- Bishop
- Knight
- Rook
- King
- Queen

## Moves 

## Legal:
- 

## Illegal:

## Check/checkmate

## Castling:
Once per game, each king can make a move known as castling. Castling consists of moving the king two squares toward a rook of the same color on the same rank, and then placing the rook on the square that the king crossed.

Castling is permissible if the following conditions are met:

Neither the king nor the rook has previously moved during the game.
There are no pieces between the king and the rook.
The king is not in check and does not pass through or finish on a square attacked by an enemy piece

## En Passant:
When a pawn makes a two-step advance from its starting position and there is an opponent's pawn on a square next to the destination square on an adjacent file, then the opponent's pawn can capture it en passant ("in passing"), moving to the square the pawn passed over. This can be done only on the turn immediately following the enemy pawn's two-square advance

## Promotion: 

Pawn reaches eighth rank as a part of the move it can be promoted to any piece choosen. 

Rank -> rows and files -> columns

Chess Game Environment:

Game State Representation: Define how the chess board and the pieces on it are represented in your program. This includes the position of pieces, the color to move, castling rights, en passant targets, etc.
Rules Engine: A set of rules governing the movements of different chess pieces, check, checkmate, and stalemate conditions.
Game Outcome Determination: Mechanism to decide the game's outcome (win, lose, draw).
Neural Network (NN):

Architecture: Design a neural network architecture suitable for learning chess strategies. Typically, convolutional neural networks (CNNs) are effective for grid-based inputs like chess.
Input Layer: Should be able to process the board state representation.
Output Layer: Generally, two outputs are needed: one for move probabilities and another for evaluating the board state (winning likelihood).
Training: Define how the network will be trained (e.g., supervised learning using historical game data, reinforcement learning through self-play).
Monte Carlo Tree Search (MCTS):

Node Structure: Each node represents a game state and contains statistics like visit count, win count, and move probabilities.
Selection: Mechanism to traverse the tree from the root to a leaf node based on a strategy (e.g., Upper Confidence Bound applied to trees - UCT).
Expansion: Add one or more child nodes to the tree, representing possible moves from the current game state.
Simulation: Simulate games (or parts of games) from the leaf nodes using a default policy (e.g., random moves or a simpler heuristic).
Backpropagation: Update the nodes with the results of the simulation, propagating back to the root.
Integration of NN with MCTS:

The NN guides the MCTS by providing move probabilities and board state evaluations, replacing or augmenting traditional heuristics and simulation policies.
User Interface (UI):

UI considerations

Debugging and Validation: Ensuring the engine plays valid and optimal chess.
Performance Measurement: Using standard chess engine benchmarks and playing against other engines.
Iterative Improvement: Based on testing results, the neural network and MCTS algorithms might need tuning and optimization.
Hardware and Software Considerations:

Given the computational demands of training neural networks and running MCTS, appropriate hardware (like GPUs for neural network training) and software (efficient programming languages and libraries for neural network and MCTS implementation) would be crucial


