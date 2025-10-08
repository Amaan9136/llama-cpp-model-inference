# app.py

from flask import Flask, request, jsonify
from llama_cpp import Llama
from methods.infer_response import generate_response_stream, generate_response

app = Flask(__name__)

MODEL_PATH = "models/llama3.2/llama3.2.bin"
llm = Llama(model_path=MODEL_PATH)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    user_prompt = data.get("prompt", "")
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    prompt = f"You are a helpful assistant.\nUser: {user_prompt}\nAssistant:"

    # Use non-streaming generation for API response
    generated_text = generate_response(llm, prompt)

    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    
    # Use streaming generation for terminal output on app start
    
    # test_prompt = "Hello, who are you?"
    # print(f"Streaming output for test prompt: {test_prompt}\n")
    # for token in generate_response_stream(llm, test_prompt):
    #     print(token, end="", flush=True)
    # print("\n--- End of test streaming output ---\n")

    app.run(host="0.0.0.0", port=5000)
