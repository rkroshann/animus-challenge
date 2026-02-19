from flask import Flask, request, render_template, make_response
import hashlib

app = Flask(__name__)

FLAG = "vault{d35m0nd_m1l35}"

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        user_input = request.form.get("text", "")

        # Hash the flag (hidden in cookie)
        hashed_flag = hashlib.sha256(FLAG.encode()).hexdigest()

        message = f"Input '{user_input}' processed successfully."

        response = make_response(render_template("index.html", message=message))
        response.set_cookie("memory_fragment", hashed_flag)

        return response

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

