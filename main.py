from flask import Flask, jsonify
import json
from collections import Counter

app = Flask(__name__)

# Load and process the JSON file
with open('input.json', 'r') as file:
    data = json.load(file)

# Count .com/reel likes and find top 10 authors
author_counts = Counter()
for item in data.get("likes_media_likes", []):
    author = item.get("title")
    for entry in item.get("string_list_data", []):
        href = entry.get("href", "")
        if ".com/reel" in href:
            author_counts[author] += 1

total_likes = sum(author_counts.values())
top_10_authors = author_counts.most_common(10)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({
        "total_likes": total_likes,
        "top_10_authors": top_10_authors
    })

if __name__ == '__main__':
    app.run(debug=True)
