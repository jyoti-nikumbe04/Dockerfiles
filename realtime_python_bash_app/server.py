from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Serve the index.html file
@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'app'), 'index.html')

# Serve the styles.css file
@app.route('/styles.css')
def styles():
    return send_from_directory(os.path.join(app.root_path, 'app'), 'styles.css')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
