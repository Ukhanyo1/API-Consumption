from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

# API URLs
POSTS_API_URL = "https://jsonplaceholder.typicode.com/posts"
COMMENTS_API_URL = "https://jsonplaceholder.typicode.com/comments"

# Routes
@app.route('/')
def home():
    """Fetch and display post titles."""
    response = requests.get(POSTS_API_URL)
    if response.status_code == 200:
        posts = response.json()
        selected_post = None
        comments = []
        return render_template('home.html', posts=posts, selected_post=selected_post, comments=comments)
    return "Failed to fetch posts", 500

@app.route('/post_details/<int:post_id>')
def post_details(post_id):
    """View post details and comments."""
    post_response = requests.get(f"{POSTS_API_URL}/{post_id}")
    comments_response = requests.get(COMMENTS_API_URL, params={"postId": post_id})

    if post_response.status_code == 200:
        post = post_response.json()
        comments = comments_response.json() if comments_response.status_code == 200 else []
        return jsonify({
            'title': post['title'],
            'body': post['body'],
            'comments': comments
        })
    return jsonify({'error': 'Failed to fetch post details'}), 500

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    """Create a new post."""
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')

        if title and body:
            response = requests.post(POSTS_API_URL, json={"title": title, "body": body})
            if response.status_code == 201:
                flash("Post created successfully!", "success")
                return redirect(url_for('home'))
            flash("Failed to create post. Please try again.", "danger")
            return redirect(url_for('create_post'))

        flash("Title and body are required.", "warning")
        return redirect(url_for('create_post'))

    return render_template('create_post.html')

if __name__ == '__main__':
    app.run(debug=True)
