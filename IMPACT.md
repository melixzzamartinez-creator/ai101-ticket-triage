AI IMPACT ASSESSMENT

INTRODUCTION
My project routes customer support tickets to the correct teams. I tested two systems: a rule-based router and a learned classifier. Both are examples of narrow AI because they focus on one specific task. They can recognize patterns in ticket text to assign categories, but they cannot perform unrelated tasks or understand problems as broadly as humans can.

ERRORS BY GROUP
The rules made 28/39 errors (71.79%) on web tickets, 17/21 (80.95%) on mobile, and 45/60 (75%) overall. Mobile errors were higher, possibly because the rules are based on specific keywords while mobile tickets are shorter and more abbreviated.
The classifier made 12/39 errors (30.77%) on web tickets, 8/21 (38.10%) on mobile, and 20/60 (33.33%) overall. Shorter mobile tickets provide less information for predictions, which may explain the higher error rate.

PRIVACY RISK AND MITIGATION
My system processes support tickets that could contain personal information like emails, phone numbers, or account IDs. My audit found 0 out of 240 training tickets containing @ or 4+ consecutive digits, but other sensitive information could still be present. To reduce this risk, I would mask personal identifiers before training the classifier. I would test this using sample tickets and aim to correctly mask at least 95% of identifiers while keeping false positives below 5%.

TRANSPARENCY RISK AND MITIGATION
My classifier can misroute tickets, and customers may not understand why a decision was made. Unlike the rules router, which shows which keywords triggered a decision, the classifier relies on similar training examples. To improve transparency, I would show the assigned category, supporting evidence, and an option for human review. I would test this by checking whether at least 95% of misrouted tickets submitted for review receive a documented explanation and correction when needed.

EFFECT-ON-WORK RISK AND MITIGATION
AI support systems can replace repetitive tasks like answering basic customer questions, while human agents focus more on complicated issues. This could reduce some support roles or increase workloads for remaining workers. To reduce this risk, I would provide paid training for support agents to learn AI monitoring and complex problem-solving. I would measure the percentage of trained workers who successfully transition into new roles within three months, aiming for at least 80%.