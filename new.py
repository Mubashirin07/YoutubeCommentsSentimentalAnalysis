import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tqdm import tqdm


plt.style.use('ggplot')


def analyze_comments():
    df = pd.read_csv('Full Comments.csv', encoding_errors='ignore')
    # print(dataset.head(10))

    sia = SentimentIntensityAnalyzer()
    print(sia.polarity_scores('I am so happy!'))
    # run the polarity score on the entire dataset

    res = {}
    negative_count = 0
    neutral_count = 0
    positive_count = 0
    total_scores = {}
    total_comments = len(df)

    for i, row in tqdm(df.iterrows(), total=len(df)):
        comment = row['Comment']
        user = row['Username']
        res[user] = sia.polarity_scores(comment)
        scores = sia.polarity_scores(comment)
        if scores['compound'] < 0:
            negative_count += 1
        elif scores['compound'] == 0:
            neutral_count += 1
        else:
            positive_count += 1

    for key, value in scores.items():
        if key in total_scores:
            total_scores[key] += value
        else:
            total_scores[key] = value

    summary = f"Total Comments: {total_comments}\n" \
              f"Positive Sentiment: {positive_count} ({round((positive_count / total_comments) * 100, 2)}%)\n" \
              f"Neutral Sentiment: {neutral_count} ({round((neutral_count / total_comments) * 100, 2)}%)\n" \
              f"Negative Sentiment: {negative_count} ({round((negative_count / total_comments) * 100, 2)}%)\n" \
              f"Mean Sentiment: {round(sum(total_scores.values()) / len(total_scores), 4)}"

    # Plotting

    sentiments = ['Positive', 'Negative', 'Neutral']
    counts = [positive_count, negative_count, neutral_count]
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(sentiments, counts, color=['green', 'red', 'blue'])

    # Display counts on top of the bars
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{count}', ha='center', va='bottom')

    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Distribution')
    plt.grid(True)
    # plot score results
    plt.show()
    return summary
