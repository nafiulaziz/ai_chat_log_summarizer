# AI Chat Log Summarizer 🧠💬

AI Chat Log Summarizer is a Django-based web app that allows users to upload .txt chat logs between a user and an AI, then generates a concise summary including message counts and the most frequently used keywords using basic NLP techniques.

---

## 📌 Features

- ✅ Upload .txt chat log files
✅ Parse messages by speaker (User / AI)
✅ Count total, User, and AI messages
✅ Extract top 5 keywords (using NLTK or TF-IDF)
✅ Generate and display a readable summary


---

## 🗂️ Project Structure
ai_chat_log_summarizer/
├── summarizer/ # Core Django app
│ ├── templates/
│ │ └── summarizer/
│ │ ├── upload.html
│ │ └── summary.html
│ ├── views.py
│ ├── urls.py
│ └── utils.py # Contains logic for parsing and summarizing
├── media/ # Stores uploaded chat files
├── manage.py
├── requirements.txt
└── README.md

---

## 🚀 Features

- Upload .txt chat log files.
Parses and separates messages by speaker (User / AI).
Counts total messages, user messages, and AI messages.

- Extracts the top 5 keywords using NLTK or TF-IDF.
Displays an easy-to-read summary on a web page.


---

## 💬 Chat Format Example

```text
User: Hi, can you tell me about Python?
AI: Sure! Python is a popular programming language known for its readability.
User: What can I use it for?
AI: You can use Python for web development, data analysis, AI, and more.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai_chat_log_summarizer.git
cd ai_chat_log_summarizer

2. Create a Virtual Environment
python -m venv myenv
myenv\Scripts\activate  # On Windows

3. Download NLTK Stopwords
# Inside Python shell
import nltk
nltk.download('stopwords')

4. Run Migrations
python manage.py migrate

5. Start the Development Server
python manage.py runserver

🌐 Usage
Open http://127.0.0.1:8000/ in your browser.

Upload a .txt chat log file.

View the summary with keyword analysis and message stats.

🧩 Tech Stack
Backend: Django (Python)

NLP: NLTK, Scikit-learn (TfidfVectorizer)

Frontend: HTML, Django Templates

📄 License
This project is licensed under the MIT License.

📫 Contact
For any questions, reach out at: nafiulaziz.na@gmail.com
