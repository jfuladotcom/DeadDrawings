import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from markdown_it import MarkdownIt
import pandas as pd
from google import genai

app = Flask(__name__)
md = MarkdownIt()

UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

GEMINI_API_KEY = os.environ.get('GOOGLE_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set. Please set it before running the application.")

client = genai.Client(api_key=GEMINI_API_KEY)

DATA_STORE = {}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('machine.html')

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    filename = secure_filename(file.filename)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    try:
        file.stream.seek(0)
        df = pd.read_csv(file)  # Read directly from the uploaded file stream!
        key = os.urandom(8).hex()
        DATA_STORE[key] = {
            "df_json": df.to_json(orient='split'),
            "filename": filename
        }
        return jsonify({
            'key': key,
            'columns': df.columns.tolist(),
            'row_count': len(df)
        })
    except Exception as e:
        return jsonify({'error': f'Failed to process CSV: {str(e)}'}), 400

@app.route('/get-csv-data')
def get_csv_data():
    key = request.args.get('key')
    if not key or key not in DATA_STORE:
        return jsonify({'error': 'Invalid key'}), 404
    df = pd.read_json(DATA_STORE[key]['df_json'], orient='split')
    return jsonify({'data': df.to_dict(orient='records')})

@app.route('/ai_prompt', methods=['POST'])
def ai_prompt():
    data = request.get_json()
    prompt = data.get('prompt', '')
    key = data.get('key', '')

    if key not in DATA_STORE:
        return jsonify({'response': 'No data uploaded yet.'})

    df = pd.read_json(DATA_STORE[key]['df_json'], orient='split')
    data_sample = df.head(500).to_csv(index=False)
    # Empathetic data visualization expert system prompt
    system_prompt = (
        "You are an empathetic data visualization expert. When a user asks a question about their uploaded CSV data, "
        "respond with warmth and understanding, as if you are guiding a non-technical colleague. Focus on providing a clear, "
        "short, and to-the-point explanation using the data provided. In addition to answering the user's question, "
        "proactively highlight the strongest correlations between variables to help the user find interesting connections. "
        "Avoid jargon, and use simple language to make complex patterns easy to grasp. If the user’s question is unclear, gently clarify what insights they are seeking. "
        "Your goal is to help the user quickly understand the most relevant trends, patterns, or answers based on their question and the data sample. "
        "Always acknowledge the user's curiosity or concern, and offer your insight in 2-4 sentences.\n\n"
        
        f"User's question: {prompt}\n\n"
        f"Here are the first 500 rows of the uploaded CSV data:\n"
        f"{data_sample}\n"
        f"(Columns: {', '.join(df.columns)})"
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=system_prompt
    )
    answer = response.text.strip() if response.text else "No response from Gemini."
    return jsonify({'response': md.render(answer)})

if __name__ == '__main__':
    app.run(debug=True)



