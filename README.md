# sqli-panel

A beginner-friendly SQL Injection Capture The Flag (CTF) challenge built with Flask and SQLite.

This challenge features a vulnerable login page, basic WAF-style input filtering, embedded clues, and a hidden flag. It’s designed for students and beginners learning web security and SQL injection — with just enough humor to keep things interesting.

---

## 🧠 What You'll Practice

- SQL Injection basics (`' OR 1=1--` and beyond)
- Bypassing simple WAF filters
- Inspecting HTML source for clues
- Using browser dev tools (F12 👀)
- Following hidden routes to flags

---

## 🚀 How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/sqli-panel.git
   cd sqli-panel

2. (Optional) Create and activate a virtual environment:

    ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install Flask:

    ```bash
    pip install flask

4. Run the app:

    ```bash
    python app.py

## 🎯 Objective
Your mission is to bypass the login form and retrieve the hidden flag.

## 💬 Hints

- View source… seriously.
- The console might know things.
- Not all inputs are welcome.
- Who needs passwords anyway?

📁 Project Structure
pgsql
Copy
Edit
sqli-panel/
├── app.py
├── database.db (auto-generated)
├── static/
│   └── style.css
├── templates/
│   ├── login.html
│   └── dashboard.html
🧪 Tested With
Python 3.10+

Flask 2.2+

Google Chrome / Firefox

⚠️ Disclaimer
This project is for educational use only. Do not attempt to exploit real systems without proper authorization.

🧑‍💻 Author
Made by @diddy as part of a semester-long cybersecurity learning project.

yaml
Copy
Edit

---

Let me know if you'd like a version with screenshots, walkthrough link, or to format this for HackDome challenge upload too 🔥









