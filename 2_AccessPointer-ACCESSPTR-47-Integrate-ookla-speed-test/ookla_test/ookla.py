import subprocess
import json

def run_speedtest_cli():
    try:
        print("Running speedtest CLI...")
        result = subprocess.run(["speedtest", "--format=json"], capture_output=True, text=True)
        
        if result.stdout:
            data = json.loads(result.stdout)  # Parse JSON output
            
            # Extract relevant fields
            download_speed = (data["download"]["bandwidth"] * 8) / 1_000_000  # Convert to Mbps
            upload_speed = (data["upload"]["bandwidth"] * 8) / 1_000_000  # Convert to Mbps
            ping = data["ping"]["latency"]  # Get ping in ms
            
            # Print formatted results
            print("\nSpeedtest Results:")
            print(f"Download Speed: {download_speed:.2f} Mbps")
            print(f"Upload Speed: {upload_speed:.2f} Mbps")
            print(f"Ping: {ping:.2f} ms")
        else:
            print("No output received. Possible error:", result.stderr)
    except FileNotFoundError:
        print("Speedtest CLI is not installed. Install it from https://www.speedtest.net/apps/cli")
    except json.JSONDecodeError:
        print("Error decoding JSON response. Check if the CLI output format has changed.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_speedtest_cli()
