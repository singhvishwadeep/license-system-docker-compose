from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hardwareinfo", methods=["GET"])
def hardware_info():
    # Simulated hardware information
    hardware_info = {
        "CPU": "Intel i7",
        "RAM": "16GB",
        "Disk": "512GB SSD",
    }
    return jsonify(hardware_info), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)

