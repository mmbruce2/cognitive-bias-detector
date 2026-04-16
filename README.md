# 🧠 Cognitive Bias Detector

Analyzes **15 cognitive biases** — prevalence, impact severity, risk scores, and mitigation strategies across Belief, Decision, Social, Memory, Probability, Perception, and Analysis categories.

## What It Does

- **15 cognitive biases** tracked: Confirmation Bias, Anchoring, Dunning-Kruger, Groupthink, Sunk Cost, and more
- **Highest risk**: Confirmation Bias 68.0 (85% prevalence, 8/10 impact), Groupthink 65.6 (82%, 8/10), Overconfidence 64.0 (80%, 8/10)
- **Highest impact**: Dunning-Kruger 9/10 (low ability people overestimate competence), Confirmation/Overconfidence/Groupthink/Survivorship all 8/10
- **Most prevalent**: Confirmation Bias 85%, Groupthink 82%, Overconfidence 80%, Fundamental Attribution Error 78%
- **Highest risk categories**: Belief avg 58.2, Social avg 56.9, Analysis avg 52.0
- **Mitigation strategies** for each bias with actionable steps
- **4 charts**: Risk rankings, prevalence vs impact scatter, category risk breakdown, category pie chart

## Quick Start

```bash
pip install pandas matplotlib
python run.py
```

## Key Findings

```
🚨 TOP 5 HIGHEST RISK BIASES:
   Confirmation Bias: risk 68.0 (85%, 8/10)
   Groupthink: risk 65.6 (82%, 8/10)
   Overconfidence: risk 64.0 (80%, 8/10)
   Dunning-Kruger: risk 55.8 (62%, 9/10)
   Fundamental Attribution: risk 54.6 (78%, 7/10)

📊 BY CATEGORY (avg risk):
   Belief: 58.2 | Social: 56.9 | Analysis: 52.0

🎯 MOST PREVALENT:
   Confirmation 85% | Groupthink 82% | Overconfidence 80%

💥 HIGHEST IMPACT:
   Dunning-Kruger 9/10 | Confirmation/Overconfidence/Groupthink/Survivorship 8/10
```

## Bias Categories

| Category | Count | Avg Risk |
|----------|-------|----------|
| Belief | 4 | 58.2 |
| Social | 3 | 56.9 |
| Decision | 3 | 46.4 |
| Memory | 2 | 42.6 |
| Analysis | 1 | 52.0 |

## Data Source

Research synthesis from Kahneman & Tversky's prospect theory, cognitive psychology literature, and behavioral economics research (1970s-2024).

## Tech Stack

- Python 3
- pandas — data processing
- matplotlib — visualization