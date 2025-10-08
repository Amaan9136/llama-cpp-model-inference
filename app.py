from flask import Flask, request, jsonify
from llama_cpp import Llama

app = Flask(__name__)

# Path to your model binary weights file inside models directory
MODEL_PATH = "models/llama3.2/llama3.2.bin"

# Load the model once when starting the app
llm = Llama(model_path=MODEL_PATH)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    # Run inference
    output = llm(prompt, max_tokens=128, stop=["\n"])
    generated_text = output.get("choices", [{}])[0].get("text", "")
    
    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
