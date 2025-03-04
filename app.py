import threading
import subprocess
import sys
from flask import Flask
from routes import setup_routes
from tunnel import start_ngrok
from sendEmail import send_outlook_email
from PullData import print_data


app = Flask(__name__)

setup_routes(app)

# Function to listen for user input in a seperate thread
def listen_for_input():
    while True:
        user_input = input("Press 1 to print current data: ")
        if user_input == '1':
            print_data() # calls the function in PullData to print data from the database
        else:
            print("Invalid input")

# Function to run Flask app in a seperate thread
def run_flask():
    port = 8001 # changed port number due to the default one being used by AirPlay

    public_url = start_ngrok(port)

    send_outlook_email("njczarne@syr.edu", "website", str(public_url))

    print(f" * Secure ngrok tunnel available at: {public_url}")

    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":

    # Start a seperate thread to listen for user input
    input_thread = threading.Thread(target=listen_for_input)
    input_thread.daemon = True # thread will exit when main program exits
    input_thread.start()


    # Start Flask in a seperate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Keep the main program running so both threads can operate
    while True:
        pass # keeps main thread running indefinitely

    

    
    
