import cv2
import requests
import pyttsx3
import json
import re
import time

# ---------------- MEMORY ----------------
def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(data):
    with open("memory.json", "w") as f:
        json.dump(data, f)

# ---------------- VISION (REAL DETECTION) ----------------
def detect():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "camera not accessible"

    ret, frame = cap.read()
    cap.release()

    if not ret:
        return "no image captured"

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        return f"{len(faces)} person(s) detected"
    else:
        return "no person detected"

# ----------- CACHED VISION (FASTER) -----------
last_vision = ""
last_time = 0

def detect_cached():
    global last_vision, last_time

    if time.time() - last_time < 3:
        return last_vision

    last_vision = detect()
    last_time = time.time()

    return last_vision

# ---------------- LLM ----------------
def ask_llm(user_input, vision, memory):
    name = memory.get("name", "User")

    prompt = f"""
You are a helpful offline AI assistant.

User name: {name}
User said: {user_input}
Vision: {vision}

Respond naturally, briefly, and conversationally.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except:
        return "I'm having trouble connecting to the local model."

# ---------------- TTS (FIXED) ----------------
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except:
        print("(TTS failed)")

# ---------------- MAIN ----------------
def main():
    memory = load_memory()

    print("AI Assistant Started (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # -------- MEMORY STORE (FIXED) --------
        if "my name is" in user_input.lower():
            match = re.search(r"my name is (.+)", user_input.lower())

            if match:
                name = match.group(1).strip().title()
                memory["name"] = name
                save_memory(memory)

                response = f"Nice to meet you, {name}"
                print("AI:", response)
                speak(response)
                continue

        # -------- MEMORY RECALL (DIRECT) --------
        if "who am i" in user_input.lower() or "what is my name" in user_input.lower():
            name = memory.get("name")

            if name:
                response = f"You are {name}"
            else:
                response = "I don't know your name yet"

            print("AI:", response)
            speak(response)
            continue

        # -------- VISION --------
        print("Checking camera...")
        vision = detect_cached()
        print("Vision:", vision)

        # -------- LLM --------
        print("Thinking...")
        response = ask_llm(user_input, vision, memory)

        print("AI:", response)
        speak(response)


# ---------------- RUN ----------------
if __name__ == "__main__":
    main()