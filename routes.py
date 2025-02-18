from flask import Flask, render_template, request, jsonify
import speedtest
from entryNew import enterNewLocation, enterNewInternet

def setup_routes(app : Flask):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/save_location", methods=["POST"])
    def save_location():
        data = request.json
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude is not None and longitude is not None:
            with open("iphone-location.txt", "a") as file:
                file.write(f"Latitude: {latitude}, Longitude: {longitude}\n")
            enterNewLocation(latitude, longitude)
            return "Location saved successfully!", 200
        else:
            return "Invalid data", 400
        
    @app.route("/speed_test", methods=["GET"])
    def speed_test():
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1e6
        upload_speed = st.upload() / 1e6
        ping = st.results.ping

        enterNewInternet(download_speed, upload_speed, ping)

        with open("iphone-location.txt", "a") as file:
            file.write(f"Download Speed: {download_speed:.2f} Mbps\n")
            file.write(f"Upload Speed: {upload_speed:.2f} Mbps\n")
            file.write(f"Ping: {ping} ms\n\n")

        return jsonify({
            "download_speed": f"{download_speed:.2f} Mbps",
            "upload_speed": f"{upload_speed:.2f} Mbps",
            "ping": f"{ping} ms"
        })