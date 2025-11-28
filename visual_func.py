import matplotlib.pyplot as plt
import seaborn as sns

def visualisation(metrics, data):
    
    sns.set_theme(style="whitegrid", palette="deep")
    plt.figure(figsize=(14, 6))
    for col in metrics:
        sns.lineplot(
            data=data,
            x="Week Number",
            y=col,
            label=col,
            sort=False
        )
        
    metrics_str = ", ".join(metrics)
    plt.title(f"Weekly Metrics: {metrics_str}", fontsize=16)
    plt.xlabel("Week Number")
    plt.ylabel("Value")
    plt.legend(title="Metric")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return