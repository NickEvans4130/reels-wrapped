import json
from collections import Counter

# Load the JSON file
with open(r'C:\Users\nicky\Desktop\reels wrapped\your_instagram_activity\likes\liked_posts.json', 'r') as file:
    data = json.load(file)

# Initialize a Counter to count author frequencies
author_counts = Counter()

# Iterate through the data
for item in data.get("likes_media_likes", []):
    author = item.get("title")
    for entry in item.get("string_list_data", []):
        href = entry.get("href", "")
        if ".com/reel" in href:
            author_counts[author] += 1

# Sort the authors by frequency in descending order
sorted_authors = sorted(author_counts.items(), key=lambda x: x[1], reverse=True)
file.close()
# Display the results
print("Author frequencies (sorted):")
file = open("output.txt","a")
for author, count in sorted_authors:
    print(f"{author}: {count}")
    file.write(f"\n{author}: {count}")
file.close()
# Display the total count
total_count = sum(author_counts.values())
print(f"\nTotal .com/reel links: {total_count}")
