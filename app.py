from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
FLAG = "flag{you_diddyT}"

#Initialize DB with sample user
def init_db():
    conn = sqlite3.connect("database.db") #Connect to the database
    cur = conn.cursor() #Create cursor to write queries                     
    cur.execute("DROP TABLE IF EXISTS users") #Delete table users if it already exists
    cur.execute("CREATE TABLE users( id INTEGER PRIMARY KEY, username TEXT, password TEXT)")    #Create a new table with primary key, username and password
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", ("admin","secure123")) #Adds username and password into the placeholder
    conn.commit() #commit changes to the db
    conn.close()   #close the db

#Login page redirection
@app.route("/", methods=["GET", "POST"])
def login():
    #set error
    error = None
    
    #gets username and password from the login form
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    
        #connect to the database
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        
        # Vulnerable to SQL Injection – user input directly used in query (on purpose for CTF)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password ='{password}'"
        print("[DEBUG] Executing:", query)
        cur.execute(query)
        user = cur.fetchone() #returns the first matching row
        
        #if it returns a row from the db redirect to dashboard
        if user:
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid credentials."
    
    #take to login page or show error if any
    return render_template("login.html", error=error)

#Dashboard 
@app.route("/dashboard")
def dashboard():
    #get the template from templates/
    return render_template("dashboard.html")

#Admin redirection
@app.route("/admin")
def admin():
    # Gets the 'user' value from the URL query string, defaults to "" if not provided
    user = request.args.get("user","")
    #if user is admin take to admin panel
    if user == "admin":
        return f"<h2>Welcome, admin! <br> Flag: <code>{FLAG}</code></h2>"
    return "Access denied."


if __name__ == "__main__":
    init_db() #set up db everytime the app is run
    app.run(debug=True) #Launch the server

    
    
    