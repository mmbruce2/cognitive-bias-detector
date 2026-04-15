"""
Cognitive Bias Detector
Analyzes 20 cognitive biases across 1000 simulated participants.
Identifies which biases are most prevalent, who is most susceptible, 
and how awareness affects bias scores.

Run: python analyzer.py
"""
import json
import pandas as pd
import matplotlib.pyplot as plt

def main():
    with open('bias_data.json') as f:
        data = json.load(f)
    df = pd.DataFrame(data)

    print("=" * 55)
    print("  COGNITIVE BIAS DETECTOR")
    print("  20 biases | 1000 participants | Real psychological research")
    print("=" * 55)
    print(f"\nTotal records: {len(df)}")

    # Average prevalence by bias
    avg_by_bias = df.groupby('bias_name')['prevalence_score'].mean().sort_values(ascending=False)

    print("\n🧠 Most Prevalent Biases:")
    for bias, score in avg_by_bias.head(10).items():
        bar = '█' * int(score * 20)
        print(f"   {bias:35s}: {score:.2f} {bar}")

    print("\n🔍 Least Prevalent Biases:")
    for bias, score in avg_by_bias.tail(5).items():
        bar = '█' * int(score * 20)
        print(f"   {bias:35s}: {score:.2f} {bar}")

    # Awareness effect
    aware = df[df['awareness'] == 'Yes']['corrected_score'].mean()
    unaware = df[df['awareness'] == 'No']['corrected_score'].mean()
    print(f"\n📊 Awareness Effect:")
    print(f"   Bias-aware participants avg score: {aware:.3f}")
    print(f"   Unaware participants avg score:      {unaware:.3f}")
    print(f"   Awareness reduces bias susceptibility by: {(unaware-aware)*100:.1f}%")

    # By age group
    print("\n👥 Bias Prevalence by Age Group:")
    age_scores = df.groupby('age_group')['prevalence_score'].mean()
    age_order = ['18-25','26-35','36-50','51-65','65+']
    for ag in age_order:
        if ag in age_scores:
            score = age_scores[ag]
            bar = '█' * int(score * 20)
            print(f"   Age {ag}: {score:.2f} {bar}")

    # By profession
    print("\n💼 Bias Prevalence by Profession:")
    prof_scores = df.groupby('profession')['prevalence_score'].mean().sort_values(ascending=False)
    for prof, score in prof_scores.items():
        bar = '█' * int(score * 20)
        print(f"   {prof:12s}: {score:.2f} {bar}")

    # Top bias combinations
    print("\n🎯 Top 5 Highest-Rated Biases:")
    top_biases = avg_by_bias.head(5)
    for i, (bias, score) in enumerate(top_biases.items(), 1):
        row = df[df['bias_name'] == bias].iloc[0]
        print(f"   {i}. {bias}")
        print(f"      \"{row['description']}\"")
        print(f"      Avg score: {score:.2f} | Awareness: {row['awareness']}")

    # Visualizations
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Chart 1: Top 15 biases
    top15 = avg_by_bias.head(15)
    colors = plt.cm.Reds([(v - 0.5) / 0.3 for v in top15.values])
    axes[0,0].barh(range(len(top15)), top15.values[::-1], color=colors[::-1])
    axes[0,0].set_yticks(range(len(top15)))
    axes[0,0].set_yticklabels(top15.index[::-1], fontsize=8)
    axes[0,0].set_xlabel('Average Prevalence Score')
    axes[0,0].set_title('Most Prevalent Cognitive Biases')
    axes[0,0].axvline(x=0.7, color='red', linestyle='--', alpha=0.5)

    # Chart 2: Age group comparison
    age_order = ['18-25','26-35','36-50','51-65','65+']
    age_vals = [age_scores[a] for a in age_order if a in age_scores]
    colors2 = plt.cm.Blues([(i+2)/7 for i in range(len(age_vals))])
    axes[0,1].bar(range(len(age_vals)), age_vals, color=colors2)
    axes[0,1].set_xticks(range(len(age_vals)))
    axes[0,1].set_xticklabels([a for a in age_order if a in age_scores], fontsize=9)
    axes[0,1].set_xlabel('Age Group')
    axes[0,1].set_ylabel('Avg Bias Score')
    axes[0,1].set_title('Bias Susceptibility by Age')
    for i, v in enumerate(age_vals):
        axes[0,1].text(i, v+0.005, f'{v:.3f}', ha='center', fontsize=8)

    # Chart 3: Profession breakdown
    prof_sorted = prof_scores.sort_values(ascending=True)
    colors3 = ['forestgreen' if v < 0.65 else 'coral' for v in prof_sorted.values]
    axes[1,0].barh(prof_sorted.index, prof_sorted.values, color=colors3)
    axes[1,0].set_xlabel('Avg Bias Score')
    axes[1,0].set_title('Bias Susceptibility by Profession')
    axes[1,0].axvline(x=0.68, color='red', linestyle='--', alpha=0.5)

    # Chart 4: Awareness histogram
    aware_scores = df[df['awareness'] == 'Yes']['prevalence_score']
    unaware_scores = df[df['awareness'] == 'No']['prevalence_score']
    axes[1,1].hist(aware_scores, bins=20, alpha=0.6, label=f'Aware (n={len(aware_scores)})', color='green')
    axes[1,1].hist(unaware_scores, bins=20, alpha=0.6, label=f'Unaware (n={len(unaware_scores)})', color='red')
    axes[1,1].set_xlabel('Bias Prevalence Score')
    axes[1,1].set_ylabel('Count')
    axes[1,1].set_title('Bias Score Distribution: Aware vs Unaware')
    axes[1,1].legend()
    axes[1,1].axvline(x=aware, color='green', linestyle='--')
    axes[1,1].axvline(x=unaware, color='red', linestyle='--')

    plt.tight_layout()
    plt.savefig('bias_analysis.png', dpi=150, bbox_inches='tight')
    print(f"\n📈 Chart saved: bias_analysis.png")
    df.to_csv('bias_data.csv', index=False)
    print(f"📄 Data saved: bias_data.csv")

if __name__ == '__main__':
    main()
