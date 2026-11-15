
import streamlit as st
import sqlite3

st.title("🔍 Search Your Notes")

search = st.text_input("What are you looking for?")

if search:
    conn = sqlite3.connect("mindvault.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM notes
        WHERE title LIKE ? OR content LIKE ? OR category LIKE ?
        ORDER BY id DESC
        """,
        (f"%{search}%", f"%{search}%", f"%{search}%")
    )

    results = cursor.fetchall()
    conn.close()

    if results:
        st.success(f"Found {len(results)} note(s)")

        for note in results:
            with st.expander(f"📌 {note[1]}"):
                st.write("Category:", note[2])
                st.write(note[3])
    else:
        st.warning("No matching notes found.")
