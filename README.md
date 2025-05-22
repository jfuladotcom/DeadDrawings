# Dead Drawings: Reviving Data Visualization with AI-Powered Insight Surfacing

A Flask web application for rapid, AI-powered data exploration. Upload CSVs, visualize your data, and surface actionable insights using Google’s Gemini 2.0 Flash model—all in one intuitive interface.

---

## Features

- **CSV Upload & Preview:** Securely upload CSV files and preview their structure.
- **Interactive Filtering:** Filter data by key attributes for targeted exploration.
- **Knowledge Graph Visualization:** Visualize relationships and patterns.
- **AI-Powered Insights:** Instantly generate clear, jargon-free insights and correlations using Gemini 2.0 Flash.
- **Empathetic AI Guidance:** The AI responds as a friendly data visualization expert, making complex trends easy to grasp.
- **Markdown Rendering:** AI responses are rendered in Markdown for rich formatting.

---

## Demo

> Upload a dataset, select filters, and ask questions—get instant, actionable insights from Gemini 2.0 Flash.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Google Gemini API key ([get yours here](https://ai.google.dev/gemini-api/docs/quickstart))
- Basic familiarity with Flask

### Installation

1. **Clone the repository:**
git clone [https://github.com/jfuladotcom/gemini-data-insight-app.git](https://github.com/jfuladotcom/DeadDrawings.git)
cd gemini-data-insight-app

2. **Install dependencies:**

pip install flask pandas markdown-it-py google-generativeai

3. **Set your Google Gemini API key:**
- Get your key from [Google AI Studio](https://ai.google.dev/gemini-api/docs/quickstart).
- Set it in your environment:
  ```
  export GOOGLE_API_KEY="your_api_key_here"
  ```

4. **Run the application:**
python app.py

5. **Open your browser:**  
Visit `http://127.0.0.1:5000/`

---

## Usage

1. **Upload a CSV:**  
Drag and drop your CSV file or select it via the upload interface.

2. **Explore Data:**  
- See file details, column names, and row count.
- Filter data by relevant attributes using the left panel.

3. **Visualize:**  
- The main panel displays a knowledge graph or other visualizations (customizable).

4. **Ask Questions:**  
- Use the AI prompt panel to ask questions about your data.
- Example: “Why does welding have lower energy consumption?”
- The AI provides concise, friendly explanations and highlights key correlations.

---

## Project Structure

├── app.py # Flask backend

├── templates/

│ └── machine.html # Main UI template

├── static/

│ └── uploads/ # Uploaded CSV storage

└── README.md

---

## Key Code Highlights

- **Gemini API Integration:**  
  Uses `google-generativeai` for AI-powered insights.
- **Markdown Rendering:**  
  Uses `markdown-it-py` for rich, readable AI responses.
- **Secure File Handling:**  
  Only allows `.csv` files; files are stored in a dedicated uploads folder.

---

## Example AI Prompt

> “You are an empathetic data visualization expert. When a user asks a question about their uploaded CSV data, respond with warmth and understanding, as if you are guiding a non-technical colleague. Focus on providing a clear, short, and to-the-point explanation using the data provided. In addition to answering the user's question, proactively highlight the strongest correlations between variables to help the user find interesting connections…”

---

## Troubleshooting

- **API Key Not Set:**  
  Ensure you have set the `GOOGLE_API_KEY` environment variable before running the app.
- **Large Files:**  
  The app supports files up to 16MB by default. Adjust `MAX_CONTENT_LENGTH` in `app.py` as needed.
- **Dependencies:**  
  If you encounter import errors, double-check your Python environment and installed packages.

---

## Credits & References

- [Google Gemini API Quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [pandas Documentation](https://pandas.pydata.org/)
- [markdown-it-py](https://markdown-it-py.readthedocs.io/)

---

## License

MIT License

---

## Contributing

Pull requests welcome! 

---

## Acknowledgements

- Google for Gemini API and documentation
- Flask community for web framework support

---

**Ready to shape the future of AI-powered data exploration? Fork, clone, and start building!**
