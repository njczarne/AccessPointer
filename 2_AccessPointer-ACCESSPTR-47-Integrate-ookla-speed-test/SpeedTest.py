import subprocess
import json

def run_speedtest_cli():
    try:
        print("Running speedtest CLI...")
        #Run the ookla speed test
        result = subprocess.run(["./speedtest.exe", "--format=json"], capture_output=True, text=True)

        # If there is an output, parse it
        if result.stdout:
            data = json.loads(result.stdout)

            # Extract relevant fields
            download_speed = (data["download"]["bandwidth"] * 8) / 1_000_000  # Convert to Mbps
            upload_speed = (data["upload"]["bandwidth"] * 8) / 1_000_000  # Convert to Mbps
            ping = data["ping"]["latency"]  # Get ping in ms

            return download_speed, upload_speed, ping
        else:
            return None, None # Error: no output received
        
    except FileNotFoundError:
        return None, None, "Error: Speedtest CLI is not installed or executable path is incorrect."
    except json.JSONDecodeError:
        return None, None, "Error decoding JSON response. Check if the CLI output format has changed."
    except Exception as e:
        return None, None, f"Unexpected error: {e}"
