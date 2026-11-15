import streamlit as st

st.title("➕ Add a New Note")

title = st.text_input("Note Title")

category = st.selectbox(
    "Category",
    ["Study", "Work", "Ideas", "Personal", "Important"]
)

content = st.text_area("Write your note here")

if st.button("Save Note"):
    if title and content:
        import sqlite3

        conn = sqlite3.connect("mindvault.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO notes (title, category, content) VALUES (?, ?, ?)",
            (title, category, content)
        )

        conn.commit()
        conn.close()

        st.success("Note saved successfully!")
    else:
        st.warning("Please enter title and content.")
