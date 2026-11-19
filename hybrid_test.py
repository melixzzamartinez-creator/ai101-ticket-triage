import random
from tickets import load_tickets
from vectors import build_vocabulary, bag_of_words
from hybrid import hybrid_route

tickets = load_tickets("train")
random.Random(101).shuffle(tickets)

fit_tickets = tickets[:180]
test_tickets = load_tickets("test")

vocab = build_vocabulary([t["text"] for t in fit_tickets])
train_vectors = [bag_of_words(t["text"], vocab) for t in fit_tickets]
train_categories = [t["category"] for t in fit_tickets]

errors = 0
reviews = 0

for ticket in test_tickets:
    prediction, source, confidence = hybrid_route(
        ticket["text"],
        vocab,
        train_vectors,
        train_categories,
        cutoff=0.4
    )

    if prediction == "human":
        reviews += 1
    elif prediction != ticket["category"]:
        errors += 1

print("Errors:", errors)
print("Human reviews:", reviews)
print("Total:", errors + reviews)