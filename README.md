# IntelliSQL-Intelligent-SQL-Querying-with-LLMs-Using-Gemini-Pro

# 🧠 SmartQuery AI – Natural Language to SQL Engine  

## 📘 Overview  

SmartQuery AI is a web-based application that converts plain English questions into SQL queries using AI.  
Users can interact with a MySQL database without writing SQL manually.  

The system automatically generates the SQL query and displays the result.

## 🚀 Features  

✔ Converts English questions to SQL  
✔ Executes queries on MySQL database  
✔ Displays generated SQL query  
✔ Shows query results  
✔ Simple and user-friendly interface  
✔ Handles API and database errors

## 🛠️ Technologies Used  

- Python 3  
- Flask  
- MySQL  
- Google Gemini API  
- HTML  
- CSS

- ## 📂 Project Structure  

SmartQueryAI/  
│── app.py  
│── query_engine.py  
│── db_connection.py  
│── requirements.txt  
│── .env  
│  
├── templates/  
│   └── index.html  
│  
└── static/

## ⚙️ Installation & Setup  

### Step 1: Install Packages  

pip install -r requirements.txt  

---

### Step 2: Setup MySQL Database  

CREATE DATABASE smartquery;  
USE smartquery;  

CREATE TABLE employees (  
    id INT PRIMARY KEY AUTO_INCREMENT,  
    name VARCHAR(100),  
    department VARCHAR(50),  
    salary INT  
);

### Step 3: Configure Environment Variables  

Create a .env file and add:  

GEMINI_API_KEY=your_api_key_here  
DB_HOST=localhost  
DB_USER=root  
DB_PASSWORD=your_password  
DB_NAME=smartquery  

---

### Step 4: Run the Application  

python app.py  

Open browser and visit:  
http://127.0.0.1:5000  

---

## 💡 Sample Queries  

- Show all employees  
- Show employees with salary above 50000  
- Who earns the highest salary?  
- Count total employees  

---

## ⚠️ Limitations  

- Free API tier has limited requests  
- Requires internet connection  
- Depends on external API availability  

---

## 🔮 Future Enhancements  

- Support multiple databases  
- Add user authentication  
- Voice-based query input  
- Improved UI design  

---

## 📜 License  

This project is developed for academic and learning purposes.
- python-dotenv  
-
