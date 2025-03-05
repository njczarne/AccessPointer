from flask import Flask, render_template, request, jsonify
import random
from SpeedTest import SpeedTestHandler
from PullData import DatabaseHandler

class Routes:
    def __init__(self, app: Flask):
        self.app = app
        self.db_handler = DatabaseHandler()
        self.speed_test = SpeedTestHandler()
        self.generated_id = None
        self.setup_routes()



    def generate_id(self):
        return random.randint(100000, 999999)

    def setup_routes(self):
        @self.app.route("/")
        def index():
            return render_template("index.html")
        
        @self.app.route("/generate_unique_id", methods=["GET"])
        def generate_id_route():
            self.generated_id = self.generate_id()
            return jsonify({"id": self.generated_id})
        
        @self.app.route("/save_location", methods=["POST"])
        def save_location():
            data = request.json
            latitude, longitude = data.get("latitude"), data.get("longitude")
            id = data.get("id", self.generated_id)

            if latitude is not None and longitude is not None:
                self.db_handler.save_location(latitude, longitude, id)
                return "Location saved successfully!", 200
            return "Invalid data", 400
        
        @self.app.route("/speed_test", methods=["GET"])
        def speed_test():
            if self.generated_id is None:
                self.generated_id = self.generate_id()

            download_speed, upload_speed, ping = self.speed_test.run_speed_test()

            if download_speed is None:
                return jsonify({"error": "Speed test failed"}), 500
            
            self.db_handler.save_speed_test(download_speed, upload_speed, ping, self.generated_id)

            return jsonify({
                "download_speed": f"{download_speed:.2f} Mbps",
                "upload_speed": f"{upload_speed:.2f} Mbps",
                "ping": f"{ping} ms",
                "id": self.generated_id
            })
        
def setup_routes(app):
    Routes(app)

