# Access Pointer: Geolocation & Speed Test Heatmap

## Description

Access Pointer is a web application designed to measure WiFi network performance (download, upload, ping, jitter) at specific geolocations and visualize the results as a heatmap overlaid on a floor plan. It also provides real-time location tracking of users within the defined area.

The application uses a Flask backend to handle API requests, data storage (via Django ORM), and coordinate mapping. The frontend utilizes HTML, CSS, JavaScript, the LibreSpeed library for speed testing, and heatmap.js for visualization.

## Features

* **WiFi Speed Testing:** Measures download speed, upload speed, ping, and jitter using the embedded LibreSpeed library.
* **Geolocation Capture:** Captures the user's latitude and longitude during speed tests and periodically in the background.
* **Database Storage:** Saves speed test results and corresponding location data using a Django-based SQLite database.
* **Heatmap Visualization:** Generates a heatmap overlay on a floor plan image (`Floor1.png`), representing network speed intensity based on collected data points. Heatmap points are calculated by mapping lat/lon coordinates to image pixels.
* **Live Location Tracking:** Displays a dot on the floor plan representing the user's current location, updated in near real-time. The dot changes color (e.g., red) if the user is outside the predefined map boundaries.
* **Backend API:** Flask routes handle:
    * Serving the main HTML page.
    * Generating unique IDs for test sessions.
    * Saving speed test results.
    * Saving location data (both specific test locations and background updates).
    * Providing data for the heatmap.
    * Providing live location coordinates for a given session.
    * Getting client IP and potentially ISP information.
    * Serving files for the speed test (garbage data, empty endpoints).
* **Session Management:** Tracks active user sessions and cleans up inactive ones.
* **Unit Tests:** Includes unit tests for backend routes.

## Requirements

* Python 3.x
* pip (Python package installer)
* Web Browser supporting Geolocation API, Web Workers, and modern JavaScript.

## Dependencies

Based on the existing `README.md` and code imports:

* **Python Packages:**
    * `Flask`
    * `Django`
    * `requests`
    * *(Optional: `pyngrok` - mentioned but commented out in `FlaskApp.py`)*
* **Frontend Libraries:**
    * `LibreSpeed` (`speedtest.js`, `speedtest_worker.js`) - Included in `/static`.
    * `heatmap.js` - Included via CDN link in HTML.

*Note: The original `README.md` mentions running the Ookla speedtest CLI executable once. This seems related to LibreSpeed's underlying mechanism or a potential alternative setup not fully reflected in the provided Python code.*

## Setup and Installation

1.  **Clone/Download:** Get the project files.
2.  **Install Python Dependencies:** Navigate to the project's root directory (`AccessPointer-main`) in your terminal and install the required packages. It's recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install Flask Django requests
    ```
3.  **Database Setup:** Navigate into the `database` directory and run Django migrations to set up the SQLite database (`db.sqlite3`):
    ```bash
    cd database
    python manage.py migrate
    cd ..
    ```
4.  **Floor Plan:** Ensure the floor plan image file named `Floor1.png` is present in the `AccessPointer-main/static/` directory.
5.  **HTTPS Certificates (Optional):** For HTTPS, place `cert.pem` and `key.pem` files in the project's root directory (`AccessPointer-main`). If not found, the application will run using HTTP.
6.  **IPinfo API Key (Optional):** For ISP information lookup on the `/backend/getIP` route, set the `IPINFO_APIKEY` environment variable with your key.

## Running the Application

1.  **Activate Virtual Environment** (if used):
    ```bash
    source venv/bin/activate # Or `venv\Scripts\activate` on Windows
    ```
2.  **Run Flask App:** Execute the main Flask application file from the root directory (`AccessPointer-main`):
    ```bash
    python FlaskApp.py
    ```
3.  **Access:** Open your web browser and navigate to the address provided in the terminal output (usually `https://0.0.0.0:8000`, `http://0.0.0.0:8000`, or a similar localhost address).

## Notes & Configuration

* **Coordinate Mapping:** The `Routes.py` file contains hardcoded latitude/longitude boundaries (`MIN_LAT`, `MAX_LAT`, `MIN_LON`, `MAX_LON`) and image dimensions (`IMAGE_WIDTH`, `IMAGE_HEIGHT`) used to map GPS coordinates onto the `Floor1.png` image pixels. These need to match the specific floor plan and area being mapped.
* **HTTPS:** Running with HTTPS requires `cert.pem` and `key.pem` files. Otherwise, it defaults to HTTP.
* **Cleanup:** The application includes a background thread to clean up inactive user sessions.
* **Logging:** Specific noisy routes (`/save_user_location`, `/get-live-location`, `/backend/garbage`, `/backend/empty`) are filtered out from the standard Flask request logs.
