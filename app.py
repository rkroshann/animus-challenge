from flask import Flask, session, abort

app = Flask(__name__)
app.secret_key = "Mczjsn6"

@app.route("/")
def index():
    session["role"] = "user"
    session["user"] = "guest"
    return "Welcome to the Animus"

@app.route("/admin")
def admin():
    if session.get("role") == "admin" and session.get("user") == app.secret_key[::-1]:
        return "FLAG: vault{d35m0nd_m1l35}"
    else:
        abort(403)

if __name__ == "__main__":
    app.run()
