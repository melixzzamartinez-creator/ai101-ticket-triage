import random
from tickets import load_tickets
from vectors import build_vocabulary, bag_of_words
from hybrid import hybrid_route

tickets = load_tickets("train")

shuffled = list(tickets)
random.Random(101).shuffle(shuffled)

fit_tickets = shuffled[:180]
tuning_tickets = shuffled[180:]

vocab = build_vocabulary([t["text"] for t in fit_tickets])
train_vectors = [bag_of_words(t["text"], vocab) for t in fit_tickets]
train_categories = [t["category"] for t in fit_tickets]

cutoffs = [0.4, 0.6, 0.8, 1.0]

for cutoff in cutoffs:
    errors = 0
    reviews = 0

    for ticket in tuning_tickets:
        prediction, source, confidence = hybrid_route(
            ticket["text"],
            vocab,
            train_vectors,
            train_categories,
            cutoff=cutoff
        )

        if prediction == "human":
            reviews += 1
        elif prediction != ticket["category"]:
            errors += 1

    total = errors + reviews

    print(
        f"cutoff={cutoff} "
        f"errors={errors} "
        f"reviews={reviews} "
        f"total={total} "
    )