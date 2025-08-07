from flask import Flask, send_from_directory, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('7research', 'template.html')  

@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory('', filename)

@app.route('/api/data')
def get_data():
    try:
        conn = sqlite3.connect('data.db')
        conn.row_factory = sqlite3.Row 
        c = conn.cursor()
        
        c.execute("SELECT * FROM data_archive")
        
        rows = c.fetchall()
        all_rows_as_dicts = [dict(row) for row in rows] 
        
        conn.close()
        
        return jsonify(all_rows_as_dicts)

    except Exception as e:
        print(f"An error occurred in /api/data: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)