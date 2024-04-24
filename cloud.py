import re
from collections import Counter
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import nltk

nltk.download('stopwords')
with open("random_paragraphs.txt", 'r') as file:
    text = file.read()
stop_words = set(stopwords.words('english'))
words = re.findall(r'\b\w+\b', text.lower())
filtered_words = [word for word in words if word not in stop_words]
word_counts = Counter(filtered_words)
words = list(word_counts.keys())
frequencies = list(word_counts.values())
sorted_indices = sorted(range(len(frequencies)), key=lambda i: frequencies[i], reverse=True)
sorted_words = [words[i] for i in sorted_indices]
sorted_frequencies = [frequencies[i] for i in sorted_indices]
print("Top 10 Word Frequencies:")
for word, frequency in zip(sorted_words[:10], sorted_frequencies[:10]):
    print(f"{word}: {frequency}")
plt.figure(figsize=(10, 6))
plt.bar(sorted_words[:10], sorted_frequencies[:10], color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Word Frequencies')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r'C:\Users\Entertech\Desktop\project\plot.png')