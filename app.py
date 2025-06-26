from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for songs
songs_data = {
    'hip-hop': [
        {'title': 'Song A', 'popularity': 90, 'listens': 1000, 'likes': 500},
        {'title': 'Song B', 'popularity': 85, 'listens': 800, 'likes': 300},
    ],
    'classical': [
        {'title': 'Song C', 'popularity': 95, 'listens': 1200, 'likes': 600},
        {'title': 'Song D', 'popularity': 80, 'listens': 700, 'likes': 200},
    ],
    'bollywood': [
        {'title': 'Song E', 'popularity': 88, 'listens': 900, 'likes': 400},
        {'title': 'Song F', 'popularity': 82, 'listens': 600, 'likes': 250},
    ],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    genre = request.form.get('genre')
    recommended_songs = songs_data.get(genre, [])
    # Sort songs based on popularity, listens, or likes
    sort_by = request.form.get('sort_by', 'popularity')  # Default to popularity
    recommended_songs = sorted(recommended_songs, key=lambda x: x[sort_by], reverse=True)
    return render_template('recommend.html', songs=recommended_songs, genre=genre)

if __name__ == '__main__':
    app.run(debug=True)
