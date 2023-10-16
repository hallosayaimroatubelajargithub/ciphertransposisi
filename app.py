from flask import Flask, request, render_template
from cipher import encrypt, decrypt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        key = int(request.form.get("key"))
        operation = request.form.get("operation")

        if operation == "encrypt":
            result = encrypt(text, key)
        else:
            result = decrypt(text, key)

        return render_template("index.html", result=result)

    return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True)
