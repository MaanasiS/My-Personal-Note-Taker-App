from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import datetime
import os

app = Flask(__name__)
DB_FILE = "notes.db"

# ---------------- DATABASE HELPERS ---------------- #
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT,
                timestamp TEXT
            )"""
    )
    conn.commit()
    conn.close()

def add_note_db(content):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO notes (content, timestamp) VALUES (?, ?)",
              (content, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_notes_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, content, timestamp FROM notes ORDER BY id DESC")
    notes = c.fetchall()
    conn.close()
    return notes

def get_note_by_id(note_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, content, timestamp FROM notes WHERE id=?", (note_id,))
    note = c.fetchone()
    conn.close()
    return note

def update_note_db(note_id, new_content):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE notes SET content=?, timestamp=? WHERE id=?",
              (new_content, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), note_id))
    conn.commit()
    conn.close()

def delete_note_db(note_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()

# ---------------- ROUTES ---------------- #
@app.route("/")
def index():
    notes = get_notes_db()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    content = request.form.get("content", "").strip()
    if content:
        add_note_db(content)
    return redirect(url_for("index"))

@app.route("/note/<int:note_id>")
def view_note(note_id):
    note = get_note_by_id(note_id)
    if not note:
        return redirect(url_for("index"))
    return render_template("note.html", note=note)

@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = get_note_by_id(note_id)
    if not note:
        return redirect(url_for("index"))
    if request.method == "POST":
        new_content = request.form.get("content", "").strip()
        if new_content:
            update_note_db(note_id, new_content)
        return redirect(url_for("view_note", note_id=note_id))
    return render_template("edit.html", note=note)

@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    delete_note_db(note_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)












