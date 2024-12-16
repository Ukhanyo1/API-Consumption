README for api_consumption Web Application
Overview
api_consumption is a Flask-based web application that consumes external APIs to display and manage posts and comments. It provides a simple user interface to:

View a list of posts.
See detailed information about a specific post along with its comments.
Create new posts.
The application interacts with the JSONPlaceholder API for fetching and managing post and comment data.

Features
Home Page: Displays a list of post titles fetched from an external API.
Dynamic Post Details: Clicking on a post dynamically fetches and displays the post's details and comments without refreshing the page.
Create Post: Users can create new posts through a simple form, with feedback provided via flash messages.
Responsive Design: Styled with CSS for an organized layout and a better user experience.
Project Structure
php
Copy code
api_consumption/
├── app.py                  # Main application file
├── templates/              # HTML templates for rendering web pages
│   ├── home.html           # Home page template
│   ├── create_post.html    # Template for creating a new post
│   └── post_details.html   # Template for detailed post view
├── static/                 # Static files (CSS, JS, etc.)
│   ├── styles.css          # Stylesheet for the application
├── requirements.txt        # Python dependencies
└── README.md               # Documentation for the project
Setup and Installation
1. Clone the Repository
bash
Copy code
git clone <repository_url>
cd api_consumption
2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies.

bash
Copy code
# On Unix/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
Install the required Python libraries from requirements.txt.

bash
Copy code
pip install -r requirements.txt
4. Run the Application
Start the Flask development server.

bash
Copy code
python app.py
The app will be accessible at http://127.0.0.1:5000/.

API Integration
The application uses the following API endpoints from JSONPlaceholder:

Posts API

GET /posts - Fetch all posts.
GET /posts/{id} - Fetch details of a specific post.
POST /posts - Create a new post.
Comments API

GET /comments - Fetch comments by post ID.
How to Use
Home Page
Open the app and view a list of post titles.
Click on a title to see its details and comments.
Create Post
Navigate to the "Create a New Post" page by clicking the Create a New Post button.
Fill out the form with a title and content, and submit it.
Flash messages provide feedback on the success or failure of the post creation.
File Details
1. app.py
Routes:
/ (Home Page): Displays a list of posts.
/post_details/<int:post_id>: Fetches and displays details of a selected post and its comments.
/create: Handles form submissions to create new posts.
2. Templates
home.html: Displays the list of posts and dynamically loads post details.
create_post.html: Form for creating a new post.
post_details.html: Template for viewing post details and comments (extended from home.html).
3. requirements.txt
Specifies the Python libraries required for the project:

Flask: Web framework for building the application.
flask-cors: Enable CORS if needed.
requests: For making HTTP requests to APIs.
SQLAlchemy & psycopg2-binary: Pre-included for potential database integration (not currently used).
Customization
To modify the API URLs, update the constants in app.py:

python
Copy code
POSTS_API_URL = "https://jsonplaceholder.typicode.com/posts"
COMMENTS_API_URL = "https://jsonplaceholder.typicode.com/comments"
To update styles, edit the styles.css file in the static/ directory.