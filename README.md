<!--markdown file>
# Offline Multimodal AI Assistant with Memory

## Overview

This project is a lightweight, real-time AI system that integrates vision, memory, and local language models to generate context-aware, personalized responses entirely offline.

It is designed as a prototype of an edge AI assistant capable of perceiving its environment, remembering user-specific information, and responding intelligently with minimal latency.

---

## Features

* Memory System
  Stores and recalls user information (e.g., name) using local JSON storage

* Computer Vision
  Performs real-time face detection using OpenCV and incorporates environmental context into responses

* Local LLM Integration
  Uses a locally hosted model (Mistral via Ollama) with no cloud dependency

* Text-to-Speech
  Generates spoken responses using pyttsx3

* Optimized Pipeline
  Includes cached vision processing and a modular structure for efficient execution

---

## System Architecture

User Input
↓
Memory Check ↔ Local Storage (JSON)
↓
Vision Module (Camera Input)
↓
Prompt Builder
↓
Local LLM (Ollama)
↓
Response Generation + Voice Output

---

## Tech Stack

* Python
* OpenCV
* Ollama (Mistral)
* pyttsx3
* Requests

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/omai.git
cd omai
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run Local LLM

Install and run Ollama:

```bash
ollama run mistral
```

Keep this running in a separate terminal.

---

## Run the Project

```bash
python main.py
```

---

## Demo

Example interactions:

* "My name is Sauravi" → stores user identity
* "Who am I?" → recalls stored memory
* "What do you see?" → uses camera to detect presence

(Add your demo video link here)

---

## Key Challenges and Solutions

Challenge: Running LLMs on edge devices with limited compute and memory

Solution:

* Used lightweight local models (Mistral via Ollama)
* Reduced latency using cached vision processing
* Designed a modular pipeline for efficient execution

---

## Future Improvements

* Add speech-to-text (Whisper or Vosk)
* Replace face detection with YOLO object detection
* Expand memory to conversational history
* Optimize for NVIDIA Jetson devices
* Add asynchronous processing for real-time performance

---

## Author

Sauravi Sar
https://github.com/yourusername

---

## Notes

This project demonstrates a practical approach to building offline, multimodal AI systems that can operate in real-world environments with limited resources.
