# Voice-Waiter-AI
# 🍽️ Voice Waiter AI

**An AI-powered restaurant assistant that aims to make food ordering easier through voice interaction.**

## 📌 About the Project

Voice Waiter AI is a smart restaurant assistant designed to interact with customers, understand their food requests, and help them place orders using natural language.

The project combines Artificial Intelligence, Python, and voice-processing technologies to create a more interactive restaurant experience.

## ✨ Main Features

- 🎙️ Voice recording to capture customer requests.
- 📝 Speech-to-text conversion using Faster Whisper.
- 🧠 Natural language understanding using Llama 3.
- 💬 AI-generated responses in Arabic.
- 🖥️ A basic web interface for the restaurant experience.
- 🗄️ Database integration is currently under development.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Ollama | Run the local LLM |
| Llama 3 | Understand customer requests |
| Faster Whisper | Speech-to-text |
| SoundDevice | Audio recording |
| SciPy | Audio file processing |
| HTML & CSS | Frontend interface |
| SQLAlchemy & PyMySQL | Database integration |

## 📂 Project Structure

```text
Voice_Waiter_Prototype/
│
├── ai/
│   ├── __init__.py
│   ├── llm_service.py
│   ├── recorder.py
│   └── speech_to_text.py
│
├── backend/
│   └── db.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── assets/
│
├── image/
│
├── main.py
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mohamedbadrawy27-pixel/Voice-Waiter-AI.git
```

### 2. Navigate to the project folder

```bash
cd Voice-Waiter-AI
```

### 3. Install Python dependencies

```bash
pip install requests sounddevice scipy faster-whisper sqlalchemy pymysql python-dotenv
```

### 4. Install Ollama and download Llama 3

Make sure Ollama is installed, then run:

```bash
ollama pull llama3
```

Ensure the Ollama service is running before starting the application.

### 5. Run the application

```bash
python main.py
```

## 🚧 Project Status

**Currently under development.**

The current prototype focuses on the AI and voice-processing components. Frontend integration and database connectivity are planned as part of the next development stages.

## 🔮 Future Improvements

- Complete frontend and backend integration.
- Connect the restaurant database.
- Retrieve real menu prices and availability.
- Add text-to-speech for spoken AI responses.
- Implement order confirmation and management.
- Improve the customer interaction experience.

## 👨‍💻 Developer

Developed independently as an AI and Python learning project.

**GitHub Repository:**  
[Voice Waiter AI](https://github.com/mohamedbadrawy27-pixel/Voice-Waiter-AI)

AI-powered voice restaurant waiter
