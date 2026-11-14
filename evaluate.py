from tickets import load_tickets
from router import route_ticket

def accuracy(predict, tickets):
    correct = 0

    for ticket in tickets:
        prediction = predict(ticket)
        if prediction == ticket["category"]:
            correct +=1


    return correct / len(tickets) if tickets else 0

train_tickets = load_tickets("train")

result = accuracy(
    lambda ticket: route_ticket(ticket["text"]),
    train_tickets
)

print("Build accuracy:", f"{result:.2%}")

from collections import Counter

category_counts = Counter(ticket["category"] for ticket in train_tickets)
print("Training categories:", category_counts)

majority_category = category_counts.most_common(1)[0][0]

baseline = accuracy(
    lambda ticket: majority_category,
    train_tickets
)

print("Majority baseline:", f"{baseline:.2%}")

test_tickets = load_tickets("test")

held_out = accuracy(
    lambda ticket: route_ticket(ticket["text"]),
    test_tickets
)

print("Held-out accuracy:", f"{held_out:.2%}")

print("\nBuild error:")

shown = 0

for ticket in train_tickets:
    predicted = route_ticket(ticket["text"])
    actual = ticket["category"]

    if predicted != actual:
        print("Text:", ticket["text"])
        print("Predicted:", predicted)
        print("Actual:", actual)
        print("---")

        shown += 1
        if shown == 5:
            break