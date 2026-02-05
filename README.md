# 🤖 AI Log Analyzer Agent (Python + Ollama)

An AI-powered agent that reads log/error files and generates a clear,
human-readable summary explaining:
- What the error is
- Why it happened
- How to fix it

The project runs completely **offline** using a local LLM via **Ollama**.

---

## 🚀 Features

- 📂 Upload log files
- 🧠 AI understands Python errors
- 📝 Generates summary & fix suggestions
- 🖥️ Simple UI using Streamlit
- 🔐 No paid API keys required
- ⚡ Fast and developer-friendly

---

## 🧠 Architecture


---

## 🛠️ Tech Stack

- Python
- LangChain
- Ollama (Local LLM)
- Streamlit
- Pandas

---

## 📁 Project Structure

🔹 Step 1: Clone the Repository
git clone https://github.com/vikas-m-sharma/log-analyzer-AI.git
cd log-analyzer-AI

🔹 Step 2: Create Virtual Environment (Recommended)
python -m venv ai
ai\Scripts\activate   # Windows
pip install -r requirements.txt
ollama --version
ollama pull mistral
cd src
python main.py
cd src
streamlit run app.py
