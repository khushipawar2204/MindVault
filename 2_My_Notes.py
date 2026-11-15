
import streamlit as st
import sqlite3

st.title("📚 My Notes")

conn = sqlite3.connect("mindvault.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM notes ORDER BY id DESC")
notes = cursor.fetchall()

conn.close()

if notes:
    for note in notes:
        with st.expander(f"📌 {note[1]}"):
            st.write("Category:", note[2])
            st.write(note[3])
else:
    st.info("No notes saved yet. Add your first note!")
