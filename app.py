from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/report-lost")
def report_lost():
    return render_template("report_lost.html")

@app.route("/report-found")
def report_found():
    return render_template("report_found.html")

@app.route("/lost-items")
def lost_items():
    return render_template("lost_items.html")

@app.route("/found-items")
def found_items():
    return render_template("found_items.html")

@app.route("/item")
def item_details():
    return render_template("item_details.html")

@app.route("/claim")
def claim_item():
    return render_template("claim_item.html")

@app.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
