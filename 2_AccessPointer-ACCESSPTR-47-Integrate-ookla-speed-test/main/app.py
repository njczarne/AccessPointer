from flask import Flask
from routes import setup_routes
from tunnel import start_ngrok
from sendEmail import send_outlook_email


app = Flask(__name__)

setup_routes(app)

if __name__ == "__main__":
    port = 5000

    public_url = start_ngrok(port)

    send_outlook_email("njczarne@syr.edu", "website", str(public_url))

    print(f" * Secure ngrok tunnel available at: {public_url}")

    app.run(host="0.0.0.0", port=port)
    
