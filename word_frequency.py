# Import libraries
from collections import Counter
import nltk.downloader as downloader
downloader.download('stopwords')
from nltk.corpus import stopwords


# Define stop words (replace with your own list if desired)
stop_words = stopwords.words('english')
c = "random_paragraphs.txt"

# Read text file content
try:
  with open(c, "r") as f:
    text = f.read().lower()
except FileNotFoundError:
  print("Error: File 'random_paragraphs.txt' not found.")
  exit()

# Preprocess text (split into words and remove stop words)
processed_text = [word for word in text.split() if word not in stop_words]

# Count word frequency
word_counts = Counter(processed_text)

# Display word frequency
print("Word Frequency Count:")
for word, count in word_counts.items():
  print(f"{word}: {count}")
