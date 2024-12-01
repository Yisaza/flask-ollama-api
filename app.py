from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the inference API! Use the /inference endpoint with POST requests."

@app.route('/inference', methods=['POST'])
def inference():
    try:
        # Mengambil JSON dari permintaan
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON data"}), 400

        # Mendapatkan prompt dari JSON
        prompt = data.get("prompt", "").strip()
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Memanggil model Ollama
        try:
            response = ollama.generate(prompt=prompt, model="llama3.2")  # Gunakan model yang tersedia
            if hasattr(response, "response"):  # Pastikan respons memiliki atribut 'response'
                return jsonify({"response": response.response}), 200
            else:
                return jsonify({"error": "Missing 'response' in Ollama output"}), 500
        except Exception as ollama_error:
            return jsonify({"error": f"Ollama Error: {str(ollama_error)}"}), 500

    except Exception as e:
        # Menangani error lainnya
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
