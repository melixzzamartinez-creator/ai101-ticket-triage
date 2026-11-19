AI APPROACH CHOICES
1. REVIEW SENTIMENT
I would choose a learned classifier for predicting whether customer reviews are positive or negative.
REASON 1: Reviews can express the same sentiment using different words, sarcasm, or complicated sentences. A learned classifier can recognize patterns beyond fixed keywords.
REASON 2: In my ticket-routing project, the learned classifier achieved 66.67% accuracy, compared with 25% for the rules. This shows that learning from labeled examples can outperform simple keyword rules, although sentiment analysis would need its own evaluation.

2. WAREHOUSE ROBOT
STATES: Each available position in the warehouse grid.
MOVES: Up, down, left, or right, as long as the move does not hit a wall or obstacle.
START: The robot's starting position.
GOAL: The destination where the robot must deliver an item.
SEARCH ALGORITHM: I would choose Breadth-First Search (BFS) over Depth-First Search (DFS).
REASON: BFS finds the shortest path when every move has the same cost. DFS may explore a longer path before finding the destination.