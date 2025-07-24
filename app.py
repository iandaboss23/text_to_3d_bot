from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Directory to store .obj models
MODEL_FOLDER = os.path.join('static', 'models')
os.makedirs(MODEL_FOLDER, exist_ok=True)

@app.route('/')
def index():
    # List all .obj files in the models folder
    models = [f for f in os.listdir(MODEL_FOLDER) if f.endswith('.obj')]
    return render_template('index.html', models=models)

@app.route('/download', methods=['POST'])
def download():
    model_name = request.form['model']
    return send_from_directory(MODEL_FOLDER, model_name, as_attachment=True)

if __name__ == '__main__':
    # Use 0.0.0.0 and dynamic port for platforms like Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
