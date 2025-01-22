from flask import Flask, request, jsonify
import pymysql
import uuid

app = Flask(__name__)

DB_CONFIG = {
    "host": "database",
    "user": "root",
    "password": "root",
    "database": "license_system",
}

@app.route("/license", methods=["POST"])
def check_license():
    data = request.json
    license_key = data.get("license_key")

    if not license_key:
        return jsonify({"error": "License key is required"}), 400

    connection = None  # Initialize connection to None

    try:
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM license_table WHERE license_key=%s", (license_key,))
        result = cursor.fetchone()
        print(1);
        if result[0] > 0:
            print(2);
            token = str(123456)
            cursor.execute(
                "INSERT INTO token_table (token, timestamp) VALUES (%s, NOW())",
                (token,),
            )
            print(3);
            connection.commit()
            print(4)
            return jsonify({"token": token}), 200
        else:
            print(5)
            return jsonify({"error": "Invalid license"}), 403
        print(6)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=True)

