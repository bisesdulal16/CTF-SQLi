from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import random

app = Flask(__name__)
FLAG = "flag{you_diddyT}"

#Initialize DB with sample user
def init_db():
    conn = sqlite3.connect("database.db") #Connect to the database
    cur = conn.cursor() #Create cursor to write queries                     
    cur.execute("DROP TABLE IF EXISTS users") #Delete table users if it already exists
    cur.execute("CREATE TABLE users( id INTEGER PRIMARY KEY, username TEXT, password TEXT)")    #Create a new table with primary key, username and password
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "secure123")) #Adds username and password into the placeholder
    conn.commit() #commit changes to the db
    conn.close()   #close the db

#Login page redirection
@app.route("/", methods=["GET", "POST"])
def login():
    #set error
    error = None
    query = None
    
    #gets username and password from the login form
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username.lower() == "admin" and password.lower() == "admin":
            error = "🤡 You really thought 'admin / admin' was gonna work? C’mon now..."
            return render_template("login.html", error=error)
        #connect to the database
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        
        # Vulnerable to SQL Injection – user input directly used in query (on purpose for CTF)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password ='{password}'"
        print("[DEBUG] Executing:", query)
        
        try:
            cur.execute(query)
            user = cur.fetchone()
            
            if user:
                return redirect(url_for("dashboard", auth="success", query=query))
            else:
                error_messages = [
                    {
                        "gif": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjBmdmJxMWh2d2pjNGNwYzJoeHBka3FmZXd3bHN0eDJmcmU0dDJjeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zeQrxoqsBDhVoASka5/giphy.gif",
                        "text": "Nice try, but this isn't your grandma's Facebook account."
                    },
                    {
                        "gif": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnZ1OXIyeHRkZWoyeHZ2bjlrMnJ3ajVoZG11eDNvMXNtbHdrenFhNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JUHFU24yRrWRRnzZ6v/giphy.gif",
                        "text": "Missed the target by a country mile."
                    },
                    {
                        "gif": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExczA5bGw1M3RxbXg2emJsYzk5MTNleG96NmFoZDUzam5mMXV3MHQ2YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LcfBYS8BKhCvK/giphy.gif",
                        "text": "Hackerman would be disappointed."
                    },
                    {
                        "gif": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTlldTAyeDZjZHdhMDBjOHIzZHJpb2l3bGwweHpiZzJwdHd6dnVycSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zqQXG7Rg9PK6s/giphy.gif",
                        "text": "That payload almost made the DB giggle."
                    },
                    {
                        "gif": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHoxcGI0dXczbGpjbjE1eGloNHZza2Z6M3o5dmQ5NXBqbDcxYTA0MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ls2Arx9RuQuz6D3Stb/giphy.gif",
                        "text": "Oops. That login attempt triggered the self-destruct sequence."
                    },
                    {
                        "gif": "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnlyeXh5OXpvd3oxNWFsdG91OGNhMWFwOGxkbHEzbTU1ZXhzNDNrZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3s7Jl1xafxWu0qDBoA/giphy.gif",
                        "text": "That attempt was so dead, it's now a zombie process."
                    },
                    {
                        "gif": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2pqdXZjaTN3ZWdxYXMycTdlbTZycWI4cGd6NDJkMXoyZW1qaTcyaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pboS5T35lhtPRNGh5n/giphy.gif",
                        "text": "That login attempt just mutated into a new virus strain."
                    }
                    ,
                    {
                        "gif": "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3R4NTVpczZzanVkNjRiZzY1N2ZsZ3E1c3JuYWVyYWU1bTFtMjQ3OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DpWKmjyqUWA9UXrkir/giphy.gif",
                        "text": "Nice Try Diddy!"
                    }
                ]
                chosen = random.choice(error_messages)
                return render_template("login.html", error=chosen["text"], gif=chosen["gif"])


        except:
            error = "🧨 Oops! That broke something..."
            return render_template("login.html", error=error)
    
    #take to login page or show error if any
    return render_template("login.html", error=error)

#Dashboard 
@app.route("/dashboard")
def dashboard():
    auth = request.args.get("auth","")
    query = request.args.get("query","")
    if auth == "success":
        msg = "🎉 You made it in!"
    else:
        msg = "🤔 Hmm... nothing to see here."
        
    #get the template from templates/
    return render_template("dashboard.html", msg=msg, query=query)

#Hidden panel with flag
@app.route("/panel")
def panel():
    # Gets the 'user' value from the URL query string, defaults to "" if not provided
    user = request.args.get("auth","")
    #if user is admin take to admin panel
    if user == "admin":
        return f"<h2>🎯 Flag: <code>{FLAG}</code></h2><p>You’ve reached the secret panel!</p>"
    return "Access denied."

@app.route("/404")
def not_found():
    return """
    <h2>404: The flag is in another castle 🏰</h2>
    <img src='https://i.imgflip.com/2/3vzej.jpg' width='300'>
    <p><a href='/'>Try logging in again?</a></p>
    """


if __name__ == "__main__":
    init_db() #set up db everytime the app is run
    app.run(debug=True) #Launch the server

    
    
    