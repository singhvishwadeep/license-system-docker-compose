from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

DB_CONFIG = {
    "host": "database",
    "user": "root",
    "password": "root",
    "database": "license_system",
}

@app.route("/counter", methods=["GET"])
def counter():
    try:
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Fetch the current count value, making sure to handle None
        cursor.execute("SELECT `count` FROM interaction_table LIMIT 1")
        result = cursor.fetchone()

        if result is None:
            return jsonify({"error": "No data found in interaction_table"}), 404
        
        current_count = result[0]

        # Increment the count value
        new_count = current_count + 1

        # Update the count in the database (with a WHERE clause)
        cursor.execute("UPDATE interaction_table SET `count`=%s WHERE `count`=%s", (new_count, current_count))
        connection.commit()

        return jsonify({"count": new_count}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

