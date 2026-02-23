from flask import Flask, request, render_template, make_response
import base64

app = Flask(__name__)

FLAG = "vault{FOSSUNITED}"

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        user_input = request.form.get("text", "")

        # Encode flag directly to Base64 (NO hashing)
        encoded_flag = base64.b64encode(FLAG.encode()).decode()

        message = f"Input '{user_input}' processed successfully."

        response = make_response(render_template("index.html", message=message))
        response.set_cookie("memory_fragment", encoded_flag)

        return response

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
