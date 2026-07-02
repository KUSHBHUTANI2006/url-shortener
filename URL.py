#lets start like menu page where there will some option to select 
import sqlite3
conn = sqlite3.connect('urls.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS urls (short_link TEXT PRIMARY KEY, original_link TEXT)""")
conn.commit()
print("welcome to the link shortener:")
while True: 
  print("1 shorten a link ")
  print("2 check for the orignal link for the short link")
  print("3 exit ")
  option = int(input("enter the option you want to select:"))
  if option == 1:
    link = input("enter the link you want to shorten:")
    while True:
      new_link = input("enter the short link you want to create ")
      cursor.execute("SELECT * FROM urls WHERE short_link = ?", (new_link,))
      result = cursor.fetchone()
      if result:
        print("the short link you entered is already in use please try again wit another short link ")
      else:
        print("the shortened link is:", new_link)
        cursor.execute("INSERT INTO urls (short_link, original_link) VALUES (?, ?)", (new_link, link))
        conn.commit()
        break
  elif option == 2:
    short_link = input("enter the short link you want to check the orignal link for :")
    cursor.execute("SELECT original_link FROM urls WHERE short_link = ?", (short_link,))
    result = cursor.fetchone()
    if result:
      print("orignal link for the short link you entered is:", result[0])
    else:
      print("the orignal link is not found for the short link you entered:")
  else:
    print("thanks for using the link shortener:")
    exit()