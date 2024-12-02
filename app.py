from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the inference API! Use the /inference endpoint with POST requests."

@app.route('/inference', methods=['POST'])
def inference():
    try:
        # JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON data"}), 400

        # JSON prompt
        prompt = data.get("prompt", "").strip()
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Ollama model
        try:
            response = ollama.generate(prompt=prompt, model="llama3.2")  
            if hasattr(response, "response"):  
                return jsonify({"response": response.response}), 200
            else:
                return jsonify({"error": "Missing 'response' in Ollama output"}), 500
        except Exception as ollama_error:
            return jsonify({"error": f"Ollama Error: {str(ollama_error)}"}), 500

    except Exception as e:
        # error handle
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
