from flask import Flask, render_template, request, jsonify
import speedtest
import random
from entryNew import enterNewLocation, enterNewInternet
from SpeedTest import run_speedtest_cli

def generate_id():
    return random.randint(100000, 999999)

generated_id = None

def setup_routes(app : Flask):
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/generate_unique_id", methods=["GET"])
    def generate_id_route():
        global generated_id
        generated_id = generate_id()
        return jsonify({"id": generated_id})

    @app.route("/save_location", methods=["POST"])
    def save_location():
        global generated_id
        data = request.json
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        id = data.get("id", generated_id)

        if latitude is not None and longitude is not None:
            with open("iphone-location.txt", "a") as file:
                file.write(f"Latitude: {latitude}, Longitude: {longitude}\nID: {id}\n")
                
            enterNewLocation(latitude, longitude, id)
            return "Location saved successfully!", 200
        else:
            return "Invalid data", 400
        
    @app.route("/speed_test", methods=["GET"])
    def speed_test():
        global generated_id
        if generated_id is None:
            generated_id = generate_id()

        download_speed, upload_speed, ping = run_speedtest_cli()

        
        # st = speedtest.Speedtest()
        # st.get_best_server()
        # download_speed = st.download() / 1e6
        # upload_speed = st.upload() / 1e6
        # ping = st.results.ping

        enterNewInternet(download_speed, upload_speed, ping, generated_id)

        with open("iphone-location.txt", "a") as file:
            file.write(f"Download Speed: {download_speed:.2f} Mbps\n")
            file.write(f"Upload Speed: {upload_speed:.2f} Mbps\n")
            file.write(f"Ping: {ping} ms\nID: {generated_id}\n\n")

        return jsonify({
            "download_speed": f"{download_speed:.2f} Mbps",
            "upload_speed": f"{upload_speed:.2f} Mbps",
            "ping": f"{ping} ms",
            "id" : generated_id
        })