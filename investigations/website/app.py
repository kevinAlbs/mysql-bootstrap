from flask import Flask, render_template, redirect, request
import mysql.connector
import credentials

connection = mysql.connector.connect(
  host=credentials.mysql_host,
  user=credentials.mysql_user,
  password=credentials.mysql_password,
  database="test_from_kevin"
)



app = Flask(__name__)

@app.route("/")
def main():
    # Select all items.
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items")
    results = cursor.fetchall()
    # `results` is a list of tuples. Example: [(1, "Test item"), (2, "Test item 2").
    return render_template('hello.html', results=results)

@app.route("/add_data", methods=["post"])
def add_data():
    # Add data from user form into database
    description = request.form["description"]
    cursor = connection.cursor()
    sql = "INSERT INTO items (description) VALUES (%s)"
    cursor.execute(sql, [description])
    connection.commit()
    # Redirect back to home page.
    return redirect("/")

if __name__ == "__main__":
    app.run()