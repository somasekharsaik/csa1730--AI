% Facts: fruit(FruitName, Color)

fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(orange, orange).
fruit(kiwi, green).
fruit(blueberry, blue).
fruit(watermelon, green).
fruit(papaya, orange).
fruit(strawberry, red).
fruit(mango, yellow).

% Query Example:
% ?- fruit(Fruit, Color).
%     --> Will return all fruits and their colors via backtracking.

% ?- fruit(Fruit, red).
%     --> Will return all fruits that are red.
