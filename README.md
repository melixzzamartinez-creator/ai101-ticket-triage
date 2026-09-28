# ai101-ticket-triage

Practice data for **AI101 Introduction to AI Concepts & Math Foundations**.

The support inbox of a note-taking app gets hundreds of messages a week, and each one has to reach the right team. In this course you build two ways to sort them. In Unit 2 you write the rules yourself. In Unit 3 you build a system that learns from labeled examples. In Unit 4 you check both for fairness.

The tickets were written for this course. They are not real customer messages. The app is fictional: it has web and mobile versions and three plans (Free, Pro and Team).

## What's in the repo

| File | What it is |
|---|---|
| `data/tickets.csv` | 240 labeled tickets. Build, explore and tune with these. |
| `data/test_tickets.csv` | 60 held-out tickets. Use them only to **measure** a finished system. |
| `data/maze.txt` | A small grid maze for the search lessons in Unit 2. |
| `tickets.py` | `load_tickets(split)` reads either file into a list of dictionaries. |
| `maze.py` | `load_maze()` reads the maze and finds the start and goal. |

You need Python 3.9 or newer. The loaders use only the standard library; numpy comes in when Unit 3 asks for it.

## Quick start

```bash
git clone https://github.com/Maestro-College-AI-Software-Engineering/ai101-ticket-triage.git
cd ai101-ticket-triage
python tickets.py
python maze.py
```

`python tickets.py` should report 240 training tickets and 60 test tickets. In your own code:

```python
from tickets import load_tickets

tickets = load_tickets("train")
print(tickets[0]["text"], "->", tickets[0]["category"])
```

## Columns

| Column | Meaning |
|---|---|
| `id` | Ticket number, `T001` to `T300`. The numbers say nothing about the category. |
| `channel` | Where the ticket was written: `web` (the website's help form) or `mobile` (the phone app's help button). |
| `text` | The message exactly as the customer typed it, typos and abbreviations included. |
| `category` | The team that should handle it: `billing`, `technical`, `account` or `other`. |

## How the tickets were labeled

Each ticket is labeled with the team that has to act on it, even when it mentions another topic.

- **billing**: charges, refunds, invoices and receipts, prices and discounts, changing or cancelling a paid plan, and payment methods.
- **account**: signing in, passwords, two-factor codes, locked or suspended accounts, changing an email or username, profiles, deleting or merging accounts, and suspicious sign-ins.
- **technical**: the app misbehaving, such as crashes, sync problems, slowness, error messages, missing or damaged notes, failed exports or uploads, and notifications.
- **other**: feature requests, feedback, how-to questions about existing features, and business questions.

Some tickets are hard to label, just like a real inbox. When you disagree with a label, say so in your write-up rather than changing the file.

## Rules for fair measurement

1. Build and tune only with `data/tickets.csv`.
2. Use `data/test_tickets.csv` to measure. If you change your system after looking at individual test tickets, your test score is no longer honest. Say so when you report it.
3. Write the logic yourself. No machine-learning libraries (scikit-learn, pandas and the like) in this course.

## The maze

In `data/maze.txt`, `#` is a wall, `.` is open floor, `S` is the start and `G` is the goal. You can move up, down, left or right, one cell per step, and never through a wall.
