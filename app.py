from flask import Flask , render_template , request , redirect 
import sqlite3
app = Flask(__name__)
conn = sqlite3.connect("links.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS links
             (short_link TEXT PRIMARY KEY, original_link TEXT)''')
conn.commit()
conn.close()

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/find", methods=["POST"])
def find():
    short_link = request.form["short_link"]
    conn = sqlite3.connect("links.db")
    c = conn.cursor()
    c.execute("SELECT original_link FROM links WHERE short_link = ?", (short_link,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return "not found", 404

@app.route("/shorten", methods=["POST"])

def shorten():
  original_link = request.form["original_link"]
  short_link = request.form["short_link"]
  conn = sqlite3.connect("links.db")
  c = conn.cursor()
  c.execute("SELECT * FROM links WHERE short_link = ?" , (short_link,))
  result = c.fetchone()
  conn.close()
  if result :
    return "Short link already exists. Please choose a different short link."
  else:
    conn = sqlite3.connect("links.db")
    c = conn.cursor()
    c.execute("INSERT INTO links (short_link, original_link) VALUES (?,?)",(short_link, original_link))
    conn.commit()
    conn.close()

    return f'Short link created! <a href="http://127.0.0.1:5000/{short_link}">127.0.0.1:5000/{short_link}</a>'

@app.route("/<short_link>")
def redirect_url(short_link):
  conn = sqlite3.connect("links.db")
  c = conn.cursor()
  c.execute("SELECT original_link FROM links WHERE short_link = ?" , (short_link,))
  result = c.fetchone()
  conn.close()
  if result:
    return redirect(result[0])
  else:
    return "Short link not found."

if __name__ == "__main__":
  app.run(debug=True)