from router import route_ticket
from vectors import bag_of_words
from classifier import knn_predict

def hybrid_route(text, vocab, train_vectors, train_categories, cutoff=0.6):
    rule_label = route_ticket(text)

    rule_label = {
        "login": "account",
        "other-default": "other"
    }.get(rule_label, rule_label)

    if rule_label != "other":
        return rule_label, "rules", 1.0

    vector = bag_of_words(text, vocab)

    prediction, confidence, neighbors = knn_predict(
        vector,
        train_vectors,
        train_categories,
        k=5
    )

    if confidence < cutoff:
        return "human", "review", confidence

    return prediction, "classifier", confidence