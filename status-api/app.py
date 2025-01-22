from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

HANDSHAKE_API = "http://handshake-api:5004/license"
COUNTER_API = "http://counter-api:5002/counter"
HARDWAREINFO_API = "http://hardwareinfo-api:5003/hardwareinfo"

@app.route("/status", methods=["GET"])
def status():
    license_key = "VALID_LICENSE_KEY"
    try:
        # Step 1: Handshake API
        handshake_response = requests.post(HANDSHAKE_API, json={"license_key": license_key})
        if handshake_response.status_code != 200:
            return jsonify({"error": "License validation failed with: " + str(handshake_response.status_code) + str(handshake_response.json())}), 403

        token = handshake_response.json().get("token")
        # Step 2: Counter API
        counter_response = requests.get(COUNTER_API)
        counter_data = counter_response.json()

        # Step 3: Hardware Info API
        headers = {"Authorization": f"Bearer {token}"}
        hardwareinfo_response = requests.get(HARDWAREINFO_API, headers=headers)
        hardwareinfo_data = hardwareinfo_response.json()

        return jsonify({
            "counter": counter_data,
            "hardware_info": hardwareinfo_data,
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

