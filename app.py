import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the prompt template
def load_prompt():
    try:
        with open("prompt.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        # Fallback prompt if file doesn't exist
        return """You are a senior business analyst assistant. Your job is to convert raw stakeholder input into clear documentation used in Agile teams.

You will be given unstructured stakeholder notes, interviews, or meeting summaries.

Output the following:

1. A list of high-level business requirements
2. Functional and non-functional requirements
3. Suggested user stories in this format:
   - As a <user type>, I want to <action>, so that <benefit>.
4. Clear acceptance criteria for each user story
5. Any implicit risks, constraints, or assumptions

Use professional, BA-style language.

### Stakeholder Input:
{stakeholder_input}"""

@app.route('/')
def serve_frontend():
    # Serve the HTML frontend directly from the Flask app
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/api/generate-requirements', methods=['POST'])
def generate_requirements():
    try:
        # Get stakeholder input from request
        data = request.get_json()
        stakeholder_input = data.get('stakeholder_input', '')
        
        if not stakeholder_input:
            return jsonify({'error': 'No stakeholder input provided'}), 400
        
        # Load prompt template
        base_prompt = load_prompt()
        
        # Inject stakeholder input into prompt
        final_prompt = base_prompt.format(stakeholder_input=stakeholder_input)
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": final_prompt}],
            temperature=0.3
        )
        
        # Extract the generated requirements
        requirements = response.choices[0].message.content
        
        return jsonify({
            'success': True,
            'requirements': requirements
        })
        
    except Exception as e:
        print(f"Error generating requirements: {str(e)}")
        return jsonify({
            'error': f'Failed to generate requirements: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'openai_configured': bool(os.getenv("OPENAI_API_KEY"))
    })

if __name__ == '__main__':
    # Check if OpenAI API key is configured
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  WARNING: OPENAI_API_KEY not found in environment variables!")
        print("Please create a .env file with your OpenAI API key.")
    else:
        print("✅ OpenAI API key found!")
    
    print("🚀 Starting AI Requirements Generator...")
    print("📱 Frontend available at: http://localhost:5000")
    print("🔌 API endpoint: http://localhost:5000/api/generate-requirements")
    
    app.run(debug=True, host='0.0.0.0', port=5000)