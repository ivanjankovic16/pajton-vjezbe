import random

#greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
#colors = ['Red', 'Black', 'Green']

deck = list(range(1, 53))
hand = random.sample(deck, k=5)
#results = random.choices(colors, weights=[18, 18, 2], k=10)
print(hand)
