
# Flask API for LLM Inference

This project demonstrates how to create a simple Flask API that uses the Ollama library to run a language model and generate responses. The API provides functionality via a single endpoint `/inference` that accepts prompts and returns generated responses.

## Features

- A `/inference` API endpoint for submitting prompts.
- Integration with the Ollama library for language model inference.
- Simple JSON response for generated outputs.

## Requirements

- Python 3.8 or higher
- Virtual environment
- `pip`

## Installation and Running the Application

1. Clone this repository or download the project files to your local machine:
   git clone <repository-url>
   cd <project-folder>

2. Create and activate a virtual environment:
   python3 -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate     # On Windows

3. Install the required dependencies:
   pip install -r requirements.txt

4. Start the Ollama server by running:
   ollama serve

5. Ensure the llama3.2 model is available by running:
   ollama pull llama2

6. Run the Flask application:
   python app.py

   The application will be accessible at http://127.0.0.1:5000.

## Testing the API

You can test the API using `curl` or an API testing tool like Postman.

1. Send a POST request using curl:
   curl -X POST http://127.0.0.1:5000/inference \
   -H "Content-Type: application/json" \
   -d '{"prompt": "Hello, how are you?"}'

2. The server will return a JSON response like this:
   {
       "response": "I'm just a language model, so I don't have feelings or emotions like humans do, but I'm functioning properly and ready to help you with any questions or tasks you may have! How can I assist you today?"
   }

## Contact

For any inquiries or issues, please contact:  
Justin Chandra  
Email: justnchandra@gmail.com