# 🧠 AI SQL Database Assistant

An AI-powered SQL assistant that converts natural language questions into SQL queries and executes them on a SQLite database.

Built using **LangChain 1.x**, **OpenAI LLM**, **SQLite**, and **Streamlit**.

---

## 🚀 Features

- 🔍 Convert natural language → SQL
- 🗄 Execute queries on SQLite database
- 📊 Display results in Streamlit UI
- 🤖 Uses LLM for intelligent query generation
- ⚡ Simple and lightweight setup

---

## 🛠 Tech Stack

- Python
- LangChain 1.x
- OpenAI API
- SQLite (Built-in Python DB)
- Streamlit

---

## 📁 Project Structure
├── app.py # Streamlit AI SQL Assistant
├── init_db.py # Database initialization script
├── database.db # SQLite database (auto-generated)
├── requirements.txt
└── README.md 

### 🗄 Initialize Database (Run Once)

Before running the app, create the database:

```bash
python init_db.py 

This will create:
database.db
users table
Sample data
After this, run:
streamlit run app.py