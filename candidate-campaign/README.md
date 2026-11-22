---
title: Chen Weilun No. 1 Campaign
emoji: 🎓
colorFrom: green
colorTo: yellow
sdk: docker
app_port: 7860
---

# Chen Weilun No. 1 | Student Representative Candidate

A bilingual, mobile-friendly campaign introduction site built with Flet, featuring a browser-based AI assistant powered by `@mlc-ai/web-llm`.
The chat interface uses HTML, CSS, JavaScript, and Vite. Model inference runs locally in the visitor's browser with WebGPU.
The homepage and assistant offer English and Traditional Chinese.

The campaign video presents three promises:

- Healthy fruit snacks
- 200 shopping points when buying school supplies or books
- More outdoor classes

## Requirements

- Python and Node.js 22.12 or later
- A recent Chrome or Edge browser with WebGPU and a compatible GPU
- An internet connection for the initial model download

## Build and run locally

From this directory, install the frontend dependencies and build the WebLLM page:

```powershell
& npm.cmd ci
& npm.cmd run build
```

Create a Python virtual environment if needed, install the app dependency, and start Flet:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

For local browsing, use `http://127.0.0.1:8080`. `0.0.0.0` is a server bind address, not a browser URL.

The home page links to the built chat page in `assets/webllm`. For frontend development, run `& npm.cmd run dev`.

## Deploy to Render

Push this project to GitHub, then create a **Web Service** in Render and connect the repository:

1. Set **Root Directory** to `candidate-campaign`.
2. Select **Docker** as the runtime and use `Dockerfile` as the Dockerfile path.
3. Create the service. The app binds to `0.0.0.0` and listens on Render's `PORT` environment variable. Use `/` as the health check path if configuring one.

The multi-stage Dockerfile builds the WebLLM frontend before creating the Python/Flet runtime image. Port `7860` is used when `PORT` is not set and is also suitable for Hugging Face Spaces. Render's free service may spin down when idle; each visitor downloads and runs the WebGPU model in their own browser.

## WebLLM model and privacy

The default model is `Qwen2.5-1.5B-Instruct-q4f16_1-MLC`. The chat page automatically checks for WebGPU and starts downloading approximately 1–2 GB of model files when supported, with visible loading progress. WebLLM can cache the model in the browser for later visits. Chat inference runs locally with WebGPU and is not sent to Ollama or another inference API.

The ten most recent user and assistant messages are saved in the browser's local storage and restored when the chat page is reopened on the same browser and site address. Use **Clear chat** to delete the saved conversation. The history stays on the device and is not sent to an inference server; clearing browser site data also deletes it. The initial model download requires an internet connection. Visitors whose browsers do not support WebGPU see a compatibility notice.

## Project structure

```text
candidate-campaign/
├── main.py                 # Flet campaign introduction
├── main_picture.png        # Main campaign photo
├── assets/
│   ├── campaign.mp4        # Campaign video
│   ├── main_picture.png    # Main photo served by Flet
│   └── webllm/             # Vite build output served by Flet
├── webllm/
│   ├── index.html
│   └── src/
│       ├── main.js         # WebGPU check, progress, streaming chat, and context
│       ├── style.css
│       └── worker.js       # WebLLM web worker
├── Dockerfile
├── package.json
├── vite.config.js
└── requirements.txt
```
