"""
Project 4: Image or Text Recognition (Basic)


Submitted By: Aanchal Pathak
Role: AI Intern
"""

print("=" * 50)
print("TEXT SENTIMENT RECOGNITION SYSTEM")
print("=" * 50)

# User Input
text = input("\nEnter a sentence: ").lower()

# Keyword Lists
positive_words = [
    "love",
    "good",
    "great",
    "excellent",
    "happy",
    "amazing",
    "awesome",
    "fantastic",
    "best",
    "wonderful"
]

negative_words = [
    "hate",
    "bad",
    "sad",
    "terrible",
    "worst",
    "awful",
    "angry",
    "poor",
    "boring",
    "disappointed"
]

# Sentiment Recognition
positive_count = 0
negative_count = 0

for word in positive_words:
    if word in text:
        positive_count += 1

for word in negative_words:
    if word in text:
        negative_count += 1

# Display Result
print("\nRecognition Result")
print("-" * 30)

if positive_count > negative_count:
    print("Detected Sentiment: Positive 😊")

elif negative_count > positive_count:
    print("Detected Sentiment: Negative 😔")

else:
    print("Detected Sentiment: Neutral 😐")

print("-" * 30)
print("Thank you for using the Text Recognition System!")