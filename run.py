#!/usr/bin/env python3
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = [
    {"bias": "Confirmation Bias", "category": "Belief", "prevalence": 85, "impact_score": 8, "description": "Seeking information that confirms existing beliefs while ignoring contradicting evidence", "mitigation": "Actively seek disconfirming evidence and consider opposite viewpoints"},
    {"bias": "Anchoring Bias", "category": "Decision", "prevalence": 75, "impact_score": 7, "description": "Relying too heavily on the first piece of information encountered", "mitigation": "Use multiple independent starting points and update systematically"},
    {"bias": "Availability Heuristic", "category": "Memory", "prevalence": 72, "impact_score": 6, "description": "Overestimating importance of information that comes to mind easily", "mitigation": "Seek statistical base rates and consider retrieval factors"},
    {"bias": "Overconfidence Effect", "category": "Belief", "prevalence": 80, "impact_score": 8, "description": "Excessive confidence in own answers relative to actual accuracy", "mitigation": "Calibration training and pre-mortem analysis"},
    {"bias": "Sunk Cost Fallacy", "category": "Decision", "prevalence": 68, "impact_score": 7, "description": "Continuing investment based on prior investments rather than future value", "mitigation": "Focus on marginal costs and benefits only"},
    {"bias": "Dunning-Kruger Effect", "category": "Belief", "prevalence": 62, "impact_score": 9, "description": "Low ability people overestimate their competence", "mitigation": "Seek expert feedback and structured self-assessment"},
    {"bias": "Status Quo Bias", "category": "Decision", "prevalence": 65, "impact_score": 6, "description": "Preferring current state over change despite potential improvement", "mitigation": "Compare all options including change scenarios equally"},
    {"bias": "Halo Effect", "category": "Perception", "prevalence": 70, "impact_score": 7, "description": "Letting overall impression influence evaluation of specific traits", "mitigation": "Evaluate traits independently before aggregating"},
    {"bias": "Fundamental Attribution Error", "category": "Social", "prevalence": 78, "impact_score": 7, "description": "Attributing others behaviors to disposition over situation", "mitigation": "Consider situational factors before judgment"},
    {"bias": "Groupthink", "category": "Social", "prevalence": 82, "impact_score": 8, "description": "Groups seeking information that confirms shared beliefs", "mitigation": "Designate devil advocate and require minority reports"},
    {"bias": "Gamblers Fallacy", "category": "Probability", "prevalence": 60, "impact_score": 6, "description": "Believing past random events influence future outcomes", "mitigation": "Understand independence of events and use base rates"},
    {"bias": "Bandwagon Effect", "category": "Social", "prevalence": 72, "impact_score": 7, "description": "Doing things because many other people do them", "mitigation": "Decide based on evidence before checking others opinions"},
    {"bias": "Optimism Bias", "category": "Belief", "prevalence": 75, "impact_score": 6, "description": "Overestimating likelihood of positive events and underestimating negatives", "mitigation": "Use premortem and consider worst case scenarios"},
    {"bias": "Hindsight Bias", "category": "Memory", "prevalence": 70, "impact_score": 6, "description": "Seeing past events as having been predictable after they occurred", "mitigation": "Record predictions before outcomes are known"},
    {"bias": "Survivorship Bias", "category": "Analysis", "prevalence": 65, "impact_score": 8, "description": "Focusing on successes that passed selection process", "mitigation": "Always examine failed cases and base rate of failure"},
]

with open('/tmp/cognitive-bias-detector/biases.json', 'w') as f:
    json.dump(data, f, indent=2)

df = pd.DataFrame(data)
df['risk_score'] = df['prevalence'] * df['impact_score'] / 10

print("=" * 60)
print("  COGNITIVE BIAS DETECTOR")
print("  15 Biases | Prevalence, Impact, Risk, Mitigation")
print("=" * 60)
print(f"\nTotal biases: {len(df)}")

print("\n🚨 HIGHEST RISK BIASES (prevalence x impact):")
risk_sorted = df.sort_values('risk_score', ascending=False)
for i, (_, r) in enumerate(risk_sorted.iterrows()):
    print(f"   #{i+1} {r['bias']}: risk {r['risk_score']:.1f} | {r['prevalence']}% prevalence | impact {r['impact_score']}/10 | {r['category']}")

print("\n📊 BY CATEGORY (avg risk score):")
by_cat = df.groupby('category').agg(
    count=('bias', 'count'),
    avg_prevalence=('prevalence', 'mean'),
    avg_impact=('impact_score', 'mean'),
    avg_risk=('risk_score', 'mean')
)
for cat, row in by_cat.sort_values('avg_risk', ascending=False).iterrows():
    print(f"   {cat}: {int(row['count'])} biases | {row['avg_prevalence']:.0f}% avg prevalence | risk {row['avg_risk']:.1f}")

print("\n🎯 MOST PREVALENT (how often people exhibit):")
for _, r in df.nlargest(5, 'prevalence').iterrows():
    print(f"   {r['bias']}: {r['prevalence']}% | {r['category']} | impact {r['impact_score']}/10")

print("\n💥 HIGHEST IMPACT (severity when present):")
for _, r in df.nlargest(5, 'impact_score').iterrows():
    print(f"   {r['bias']}: {r['impact_score']}/10 | {r['prevalence']}% prevalence | {r['category']}")

print("\n🧠 BELIEF-RELATED BIASES:")
belief = df[df['category'] == 'Belief']
for _, r in belief.iterrows():
    print(f"   {r['bias']}: {r['prevalence']}% | impact {r['impact_score']}/10 | {r['description'][:60]}...")

print("\n⚖️ DECISION-RELATED BIASES:")
decision = df[df['category'] == 'Decision']
for _, r in decision.iterrows():
    print(f"   {r['bias']}: {r['prevalence']}% | impact {r['impact_score']}/10 | {r['description'][:60]}...")

print("\n🗣️ SOCIAL-RELATED BIASES:")
social = df[df['category'] == 'Social']
for _, r in social.iterrows():
    print(f"   {r['bias']}: {r['prevalence']}% | impact {r['impact_score']}/10 | {r['description'][:60]}...")

print("\n🔧 BIASES NEEDING MOST ATTENTION (high prev + high impact):")
for _, r in df[(df['prevalence'] >= 70) & (df['impact_score'] >= 7)].iterrows():
    print(f"   {r['bias']} ({r['category']}): {r['prevalence']}% prev | {r['impact_score']}/10 impact | MITIGATION: {r['mitigation']}")

# Charts
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

cat_colors = {'Belief': '#E63946', 'Decision': '#2E86AB', 'Social': '#F18F01', 'Memory': '#2ECC71', 'Probability': '#9B59B6', 'Perception': '#1ABC9C', 'Analysis': '#34495E'}

# Chart 1: Risk score by bias
risk_top = df.nlargest(12, 'risk_score').sort_values('risk_score')
colors_risk = [cat_colors.get(c, 'gray') for c in risk_top['category']]
axes[0,0].barh(range(len(risk_top)), risk_top['risk_score'], color=colors_risk)
axes[0,0].set_yticks(range(len(risk_top)))
axes[0,0].set_yticklabels(risk_top['bias'], fontsize=8)
axes[0,0].set_xlabel('Risk Score (Prevalence x Impact / 10)')
axes[0,0].set_title('Cognitive Bias Risk Rankings (Color=Category)')
for i, v in enumerate(risk_top['risk_score']):
    axes[0,0].text(v+0.1, i, f'{v:.1f}', va='center', fontsize=7)

# Chart 2: Prevalence vs Impact
for cat, color in cat_colors.items():
    subset = df[df['category'] == cat]
    if len(subset) > 0:
        axes[0,1].scatter(subset['prevalence'], subset['impact_score'], c=color, label=cat, s=60, alpha=0.8)
axes[0,1].set_xlabel('Prevalence (%)')
axes[0,1].set_ylabel('Impact Score (1-10)')
axes[0,1].set_title('Prevalence vs Impact (Color=Category)')
axes[0,1].legend(fontsize=8)
for _, r in df.iterrows():
    if r['impact_score'] >= 8 or r['prevalence'] >= 78:
        axes[0,1].annotate(r['bias'][:15], (r['prevalence'], r['impact_score']), fontsize=6)

# Chart 3: Category breakdown (avg risk)
cat_risk = df.groupby('category')['risk_score'].mean().sort_values(ascending=True)
axes[1,0].barh(range(len(cat_risk)), cat_risk.values, color=[cat_colors.get(c, 'gray') for c in cat_risk.index])
axes[1,0].set_yticks(range(len(cat_risk)))
axes[1,0].set_yticklabels(cat_risk.index, fontsize=9)
axes[1,0].set_xlabel('Average Risk Score')
axes[1,0].set_title('Risk by Category')
for i, v in enumerate(cat_risk.values):
    axes[1,0].text(v+0.05, i, f'{v:.1f}', va='center', fontsize=8)

# Chart 4: Top biases by category (grouped)
by_cat_count = df.groupby('category').size().sort_values(ascending=False)
axes[1,1].pie(by_cat_count.values, labels=by_cat_count.index, autopct='%1.0f%%', colors=[cat_colors.get(c, 'gray') for c in by_cat_count.index])
axes[1,1].set_title('Biases by Category')

plt.tight_layout()
plt.savefig('/tmp/cognitive-bias-detector/bias_analysis.png', dpi=150, bbox_inches='tight')
print("\n📈 Chart saved: bias_analysis.png")
df.to_csv('/tmp/cognitive-bias-detector/biases.csv', index=False)
print("📄 Data saved: biases.csv")
print("DONE")