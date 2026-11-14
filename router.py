from collections import Counter
from tickets import load_tickets
import string

def words(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return set(text.split())

print(words("My CARD was charged twice!"))

payment_keywords = {"payment", "refund", "card"}
ticket_words = words("My CARD was charged twice!")
matches = payment_keywords.intersection(ticket_words)
print ("Matches:", matches)

def route_ticket(text):
    ticket_words = words(text)

    billing = {"refund", "payment", "card", "charged"}
    login = {"password", "login", "singin"}
    technical = {"crashing", "freezing", "error"}

    if ticket_words & billing:
        return "billing"
    elif ticket_words & login:
        return "login"
    elif ticket_words & technical:
        return "technical"
    else:
        return "other-default"

print("Billing:", route_ticket("I need a refund"))
print("Login:", route_ticket("I forgot my password"))
print("Technical:", route_ticket("My app keeps crashing"))
print("Default:", route_ticket("Please add dark mode"))
print("Conflict:", route_ticket("I need a refund and password reset"))

tickets = [
    "I need a refund",
    "I forgot my password",
    "My app keeps crashing",
    "Please add dark mode",
    "I need a refund and password reset"
]

results = [route_ticket(ticket) for ticket in tickets]
matched = sum(result != "other-default" for result in results)

print("Matched:", matched)
print("Default:", len(tickets) - matched)
print("Coverage:", f"{matched / len(tickets) * 100:.0f}%")

train_tickets = load_tickets("train")

counts = Counter(
    route_ticket(ticket["text"]) for ticket in train_tickets
)

print(counts)
print("Total:", sum(counts.values()))

def route_with_trace(text):
    ticket_words = words(text)
    facts = set(ticket_words)
    trace = []

    #RULE 1: DETECT A MONEY ISSUE
    if "refund" in facts and(
        "charged" in facts or "payment" in facts
    ):
        facts.add("money_issue")
        trace.append("Rule 1: refund + charged/payment -> money_issue")

    #RULE 2: USE THE NEW FACT
    if "money_issue" in facts:
        trace.append("Rule 2: money_issue -> billing")
        return "billing", trace

    #OTHERWISE, USE EXISTING ROUTER
    return route_ticket(text), trace

for ticket in [
    "My card was charged twice, I need a refund",
    "I forgot my password"
]:
    category, trace = route_with_trace(ticket)

    print("\nTicket", ticket)
    print("Category:", category)
    print("Trace:", trace)