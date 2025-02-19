import datetime as dt
import sqlite3
from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Homepage with links and date filter form
@app.route("/")
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Housing Market Data API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 20px;
                }
                .container {
                    max-width: 800px;
                    margin: auto;
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h2 {
                    text-align: center;
                    color: #333;
                }
                h4 {
                    text-align: center;
                    color: #555;
                }
                a {
                    display: block;
                    text-align: center;
                    margin: 15px 0;
                    text-decoration: none;
                    color: #007BFF;
                    font-size: 18px;
                    transition: color 0.3s;
                }
                a:hover {
                    color: #0056b3;
                }
                form {
                    text-align: center;
                    margin-top: 20px;
                }
                select, input[type="date"], input[type="submit"] {
                    padding: 10px;
                    margin: 10px 0;
                    border-radius: 5px;
                    border: 1px solid #ccc;
                }
                input[type="submit"] {
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2><u>Housing Market Data API</u></h2>
                <h4>Click the Links Below to View Housing Data</h4>
                <a href='/api/v1.0/charlotte'>Charlotte Housing Data</a>
                <a href='/api/v1.0/houston'>Houston Housing Data</a>
                <a href='/api/v1.0/va_beach'>Virginia Beach Housing Data</a>
                
                <h4>Filter Housing Data by Date:</h4>
                <form action='/api/v1.0/filter' method='GET'>
                    City: 
                    <select name='city' required>
                        <option value='charlotte'>Charlotte</option>
                        <option value='houston'>Houston</option>
                        <option value='va_beach'>Virginia Beach</option>
                    </select><br>
                    Start Date: <input type='date' name='start' required><br>
                    End Date: <input type='date' name='end'><br>
                    <input type='submit' value='Get Housing Data'>
                </form>
            </div>
        </body>
        </html>
    ''')

# Route to fetch all data for a specific city
@app.route("/api/v1.0/<city>")
def get_city_data(city):
    # Connect to SQLite database
    conn = sqlite3.connect('housing_data.sqlite')
    cursor = conn.cursor()

    # Validate city input
    if city not in ["charlotte", "houston", "va_beach"]:
        return jsonify({"error": "City not found"}), 404

    # Fetch data for the specified city
    query = f"SELECT * FROM {city}_housing"
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    conn.close()

    # Convert to list of dictionaries
    results = [dict(zip(columns, row)) for row in data]
    return jsonify(results)

# Route to filter data by date range
@app.route("/api/v1.0/filter")
def filter_by_date():
    city = request.args.get("city")
    start_date = request.args.get("start")
    end_date = request.args.get("end")

    # Validate city input
    if city not in ["charlotte", "houston", "va_beach"]:
        return jsonify({"error": "Invalid city"}), 400
    if not start_date:
        return jsonify({"error": "Start date is required"}), 400

    # Connect to SQLite database
    conn = sqlite3.connect('housing_data.sqlite')
    cursor = conn.cursor()

    # Prepare the query
    query = f"SELECT * FROM {city}_housing WHERE period_begin >= ?"
    params = [start_date]
    
    if end_date:
        query += " AND period_begin <= ?"
        params.append(end_date)

    # Execute the query
    try:
        cursor.execute(query, params)
        filtered_data = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

    # Convert the result to a list of dictionaries
    results = [dict(zip(columns, row)) for row in filtered_data]
    
    return jsonify(results)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)