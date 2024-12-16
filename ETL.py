import requests
import pandas as pd
from sqlalchemy import create_engine

# Database connection details
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "Api_posts"
DB_USER = "postgres"
DB_PASS = "3708"

# URL to fetch data from
url = "https://jsonplaceholder.typicode.com/posts"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data into a DataFrame
    data = response.json()
    df = pd.DataFrame(data)
    
    # Create a connection to the PostgreSQL database
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    
    # Ensure the table exists and append data
    table_name = "posts"
    with engine.connect() as conn:
        df.to_sql(table_name, conn, if_exists="append", index=False)
        print(f"Data successfully inserted into '{table_name}' table.")
    
    # Extract titles into a list
    titles = df['title'].tolist()
    print("Titles:")
    print(titles)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
