The MySQL credentials are not included in this repository. Copy the `credentials.py.example` file into `credentials.py` and fill in the MySQL credentials.

In Powershell, install `mysql-connector-python` and `flask`:

```
pip install mysql-connector-python
pip install flask
```

`flask` is a Python web framwork. To run a flask app:

```
cd website
flask run --debug
```

Expect output to include something like: `* Running on http://127.0.0.1:5000`. Open `http://127.0.0.1:5000` to see a welcome page.

Here is the page:

[!screenshot](screenshot.png)

I suggest reading the [Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/) for an overview of `flask`.