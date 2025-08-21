# EduMate-AI E-Learning Platform 📖

EduMate is an AI-powered study assistant that provides intelligent answers to students' questions using SambaNova's Llama-4-Maverick-17B-128E-Instruct model.

---

## 🚀 Features
- AI-powered Q&A with SambaNova models
- Web interface for asking questions
- Easy setup with environment variables

---

## 📂 Project Structure
```
EduMate/
│── main.py          # FastAPI backend
│── ai_agent.py      # Handles SambaNova API calls
│── index.html       # Frontend UI
│── requirements.txt # Dependencies
│── README.md        # Documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/thekhushalsingh/Edumate-Learning-AI-Application
cd EduMate
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables
Create a `.env` file in the root folder and add:
```env
SAMBA_API_KEY=your_sambanova_api_key_here
SAMBA_API_URL=https://api.sambanova.ai/v1
```

### 4️⃣ Run the Application
```bash
streamlit run main.py --server.port 8501
```

 You can now view your Streamlit app in your browser.
 Local URL: http://localhost:8501

### 5️⃣ Open the Frontend
Simply open `index.html` in your browser.

---

## 📡 API Endpoints

### `POST /ask`
Send a student query and get an AI response.

**Request Body:**
```json
{
  "query": "Explain photosynthesis in simple terms"
}
```

**Response:**
```json
{
  "response": "Photosynthesis is the process by which plants make food using sunlight, carbon dioxide, and water."
}
```

---

## 🛠️ Technologies Used
- **FastAPI** (Backend)
- **SambaNova API** (AI model)
- **HTML + JS** (Frontend)
- **Python-dotenv** (Environment variables)

---
## Screenshot
!image[]()

## 👨‍💻 Author
Developed by Khushal 🚀
