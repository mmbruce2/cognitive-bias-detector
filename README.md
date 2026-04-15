# 🧠 Cognitive Bias Detector

Analyzes **20 cognitive biases** across **1000 simulated participants**. Identifies which biases are most prevalent in the population, how susceptibility varies by age and profession, and the relationship between bias awareness and actual bias scores.

## What It Does

- **Ranks 20 cognitive biases** by population-level prevalence
- **Breaks down susceptibility** by age group and profession
- **Measures awareness effect** — bias-aware vs unaware participants
- **4 visualizations**: top 15 biases, age demographic breakdown, profession comparison, awareness histogram

## Quick Start

```bash
pip install pandas matplotlib
python analyzer.py
```

## Key Findings

```
🧠 Most Prevalent Biases:
   1. Dunning-Kruger Effect      0.81
   2. Overconfidence Effect      0.78
   3. Optimism Bias              0.76
   4. Loss Aversion               0.76
   5. Confirmation Bias          0.74

👥 Age: 26-35 has highest susceptibility (0.71)
💼 Profession: Tech workers most susceptible (0.70)
📊 Awareness effect: Aware participants score 0.741 vs 0.656 for unaware
```

## Prediction Logic

Bias scores are modeled from documented psychological research on each bias's population-level prevalence, with individual variation via Gaussian noise and demographic weighting.

## Data Source

Cognitive bias prevalence scores based on documented research from Kahneman & Tversky, Dunning-Kruger studies, and meta-analyses of behavioral economics literature.

## Tech Stack

- Python 3
- pandas — data processing
- matplotlib — visualization
