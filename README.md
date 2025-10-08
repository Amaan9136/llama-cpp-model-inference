# LLaMA 3.2 Inference API

## Setup

1. Create a Python virtual environment:

   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

2. Install dependencies:

   pip install -r requirements.txt

3. Place your LLaMA 3.2 model weights binary in `models/llama3.2.bin`.
   - If your model is in Ollama's blobs format, convert it to llama.cpp compatible `.bin` weights before use.
   - Alternatively, create a symlink into your Ollama model blobs folder if compatible.

4. Run the Flask API server:

   python app.py

## Usage

Send a POST request to:

`http://localhost:5000/generate`

With JSON body:
```json
{
   "prompt": "Your input prompt text here"
}
```

### The response JSON will contain generated text.

## This solution does **not** use any Ollama APIs or architecture. It uses the open-source `llama.cpp` interface to run inference on the LLaMA 3.2 model stored locally in /models folder (Llama-cpp Model Inference\models\llama3.2\llama3.2.bin).