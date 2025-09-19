from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_form():
    action = request.form.get("action")
    email = request.form.get("email")
    password = request.form.get("password")

    if action == "login":
        if email == "test@test.com" and password == "1234":
            return "Login Successful!"
        else:
            return "Invalid credentials!"

    if action == "signup":
        username = request.form.get("username")
        return f"Signup Successful for {username}!"

if __name__ == "__main__":
    app.run(debug=True)
