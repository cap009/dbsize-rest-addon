from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/db_size', methods=['GET'])
def get_db_size():
    try:
        conn = mysql.connector.connect(
            host='core-mariadb',  # <-- Correct host for Home Assistant add-on
            user='homeassistant',
            password='Cap70952058',
            database='homeassistant',
            ssl_disabled=True
        )
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ROUND(SUM(data_length + index_length) / 1024 / 1024, 2)
            FROM information_schema.tables
            WHERE table_schema = 'homeassistant';
        """)
        size_mb = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return jsonify({"db_size": size_mb})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
