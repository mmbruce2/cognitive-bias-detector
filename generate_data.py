import json, random, os
os.makedirs('/tmp/cognitive-bias-detector', exist_ok=True)
random.seed(7)

biases = [
    ('Confirmation Bias', 'Seeing information that confirms pre-existing beliefs', 0.73),
    ('Availability Heuristic', 'Overestimating importance of readily available information', 0.68),
    ('Anchoring Bias', 'Relying too heavily on the first piece of information encountered', 0.72),
    ('Overconfidence Effect', 'Overestimating your own abilities or knowledge', 0.77),
    ('Sunk Cost Fallacy', 'Continuing a behavior because of prior investment', 0.70),
    ('Bandwagon Effect', 'Doing things because many others are doing them', 0.65),
    ('Dunning-Kruger Effect', 'Low-ability people overestimating their competence', 0.80),
    ('Loss Aversion', 'Feeling pain of loss more acutely than pleasure from equivalent gains', 0.75),
    ('Framing Effect', 'Drawing different conclusions from same info depending on presentation', 0.69),
    ('Recency Bias', 'Remembering recent events more vividly than earlier ones', 0.64),
    ('Halo Effect', 'Letting overall impression influence feelings about specific traits', 0.71),
    ('Survivorship Bias', 'Focusing on successes and ignoring all the failures', 0.66),
    ("Gambler's Fallacy", 'Believing past random events influence future outcomes', 0.63),
    ('Fundamental Attribution Error', 'Attributing others behavior to character vs situation', 0.68),
    ('Groupthink', 'Conformity pressure leading to poor group decisions', 0.72),
    ('Negativity Bias', 'Giving more weight to negative experiences than positive ones', 0.67),
    ('Optimism Bias', 'Underestimating likelihood of negative events happening to you', 0.74),
    ('Authority Bias', 'Overvaluing opinions of authority figures', 0.61),
    ('Status Quo Bias', 'Preferring things stay the same over making changes', 0.58),
    ('Peak-End Rule', 'Judging experiences by peak moment and ending vs the average', 0.62),
]

data = []
for bias_name, description, base_prevalence in biases:
    for pid in range(1, 51):
        age_group = random.choice(['18-25', '26-35', '36-50', '51-65', '65+'])
        profession = random.choice(['Student', 'Tech', 'Finance', 'Healthcare', 'Education', 'Other'])
        score = min(1.0, max(0.0, base_prevalence + random.gauss(0, 0.15)))
        aware = random.random() < 0.35
        aware_score = min(1.0, max(0.0, score + (0.05 if aware else -0.03)))
        data.append({
            'participant_id': f'P{pid:03d}',
            'bias_name': bias_name,
            'description': description,
            'age_group': age_group,
            'profession': profession,
            'prevalence_score': round(score, 3),
            'awareness': 'Yes' if aware else 'No',
            'corrected_score': round(aware_score, 3),
        })

with open('/tmp/cognitive-bias-detector/bias_data.json', 'w') as f:
    json.dump(data, f, indent=2)
print(f'Generated {len(data)} records across {len(biases)} biases')
