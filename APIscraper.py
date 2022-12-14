import requests
import os
import json
from flask import Flask
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Define the URL of the API you want to scrape
api_url = "https://www.sportsbet.com.au/apigw/accounts/balance?pendingbetcount=true&freebetcount=true&jointAccountBalance=true"

# Get the access token from the environment variable
access_token = os.getenv("ACCESS_TOKEN")

# Define the access token as a request header
headers = {"accesstoken": "access_token"}

# Create a Flask app
app = Flask(__name__)

# Define a route for the localhost URL that will handle the GET request and display the data from the API
@app.route("/")
def index():
  # Make a GET request to the API
  response = requests.get(api_url, headers=headers)
  
  # Check the status code of the response
  if response.status_code == 200:
    # If the status code is 200, then the request was successful
    # and you can now process the data from the API
    data = response.json()
    
    # You can now access the data from the API using the "data" variable
    # and return it as a response to the browser
    return data
  else:
    # If the status code is not 200, then there was an error
    # with the request, and you should handle it here
    return "There was an error with the request"

    

# Start the Flask app on your localhost server
if __name__ == "__main__":
  app.run()
