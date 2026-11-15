import streamlit as st
import sqlite3

st.set_page_config(
    page_title="MindVault | Your Second Brain",
    page_icon="🧠",
    layout="wide"
)


# =====================================
# MINDVAULT DESIGN & WELCOME SECTION
# =====================================

st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #F7F4FC;
}

/* Main spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Welcome banner */
.welcome-box {
    background: linear-gradient(135deg, #EAE2F8, #F4EDFC);
    border: 1px solid #D9CBEF;
    border-radius: 22px;
    padding: 40px 25px;
    text-align: center;
    margin-bottom: 30px;
}

/* Main heading */
.welcome-title {
    color: #654A91;
    font-size: 43px;
    font-weight: 800;
    margin-bottom: 10px;
}

/* Subtitle */
.welcome-subtitle {
    color: #796995;
    font-size: 18px;
    margin-bottom: 18px;
}

/* Highlight text */
.highlight-text {
    color: #7955AA;
    font-weight: 700;
    background: #E3D7F5;
    padding: 7px 12px;
    border-radius: 8px;
}

/* Feature cards */
.feature-box {
    background: #FFFFFF;
    border: 1px solid #E5DDF0;
    border-radius: 18px;
    padding: 22px 16px;
    min-height: 145px;
    text-align: center;
}

.feature-box h3 {
    color: #705394;
    font-size: 19px;
}

.feature-box p {
    color: #777080;
    font-size: 14px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #EEE8F7;
}

/* Buttons */
.stButton > button {
    background-color: #B9A5DC;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #967BBE;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #EEE8F7;
}

/* Dark sidebar menu text */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] a {
    color: #382653 !important;
    font-weight: 600;
}

/* Sidebar icons */
section[data-testid="stSidebar"] svg {
    color: #654A91 !important;
}

/* Buttons */
.stButton > button {
    background-color: #B9A5DC;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #967BBE;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# WELCOME CONTENT
# =====================================


st.markdown("""
<div class="welcome-box">

    

</span>
</p><div style="font-size:55px;">🧠</div>
<div class="welcome-title">
    Welcome to MindVault
</div>

<div class="welcome-subtitle">
    Your Second Brain. Your Personal Space.
</div>

<p style="color:#655879; font-size:17px;">
    A little space for all your thoughts,
    ideas and memories.
</p>

<p style="font-size:16px;">
    <span class="highlight-text">
        Save it. Organize it. Find it.
    </span>
</p>

</div>
""", unsafe_allow_html=True)



st.markdown("""
<h2 style="text-align:center; color:#705394;">
    ✨ Explore Your MindVault
</h2>

<p style="text-align:center; color:#898096;">
    Everything important, organized in one place.
</p>
""", unsafe_allow_html=True)


# Feature cards

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h3>📝 Save Notes</h3>
        <p>Capture your thoughts, ideas and important information.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h3>📚 Organize</h3>
        <p>Keep your information organized with categories.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <h3>🔍 Discover</h3>
        <p>Find your saved information whenever you need it.</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div style="
    text-align:center;
    color:#8B7AA4;
    padding:35px 10px 15px 10px;
    font-size:15px;
">
    💜 Your thoughts deserve a home.
    <br>
    <b>MindVault | Your Second Brain</b>
</div>
""", unsafe_allow_html=True)

# Database setup
conn = sqlite3.connect("mindvault.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    content TEXT NOT NULL
)
""")

conn.commit()
cursor.execute("SELECT * FROM notes ORDER BY id DESC")
notes = cursor.fetchall()
conn.close()

# Professional styling
st.markdown("""
<style>

.stApp {
    background: #F4F1E8;
    color: #263B30;
}

.block-container {
    padding: 2rem 3rem;
    max-width: 1250px;
}

[data-testid="stSidebar"] {
    background: #E5EBDD;
    border-right: 1px solid #CFD9CA;
}

.hero {
    background: linear-gradient(120deg, #315B46, #64866A);
    padding: 35px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    color: #FFFFFF;
    font-size: 36px;
}

.hero p {
    color: #E5EBDD;
    font-size: 16px;
}

.stat {
    background: #FFFFFF;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #DCE5D6;
    min-height: 115px;
}

.stat h2 {
    color: #315B46;
    font-size: 30px;
    margin: 5px 0;
}

.stat p {
    color: #718071;
    margin: 0;
}

.note-card {
    background: #FFFFFF;
    border: 1px solid #DCE5D6;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
}

.small-text {
    color: #718071;
    font-size: 13px;
}


</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("# 🧠 MindVault")
    st.caption("YOUR PERSONAL SECOND BRAIN")
    st.divider()

    st.markdown("### MENU")
    st.markdown("🏠 Dashboard")
    st.page_link("pages/1_Add_Note.py", label="Add Note", icon="➕")
    st.page_link("pages/2_My_Notes.py", label="My Notes", icon="📚")
    st.page_link("pages/3_Search_Notes.py", label="Search Notes", icon="🔍")

    st.divider()
    st.markdown("### YOUR SPACE")
    st.caption("Capture your thoughts.")
    st.caption("Organize your knowledge.")
    st.caption("Remember what matters.")

# Hero section
st.markdown("""
<div class="hero">
    <h1>Welcome to MindVault ✨</h1>
    <p>Your ideas deserve a place to live.
    Save, organize and rediscover everything important.</p>
</div>
""", unsafe_allow_html=True)

# Search bar
st.subheader("🔍 Find something in your mind")
search = st.text_input(
    "Search",
    placeholder="Search your notes, ideas, study material..."
)

if search:
    matches = [
        n for n in notes
        if search.lower() in n[1].lower()
        or search.lower() in n[3].lower()
    ]

    for n in matches:
        st.write(f"**{n[1]}** — {n[2]}")
        st.caption(n[3])

    if not matches:
        st.info("No matching notes found.")

st.divider()

# Statistics
total_notes = len(notes)
categories = len(set(n[2] for n in notes))

st.subheader("Your Knowledge Overview")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="stat">
        <p>📝 TOTAL NOTES</p>
        <h2>{total_notes}</h2>
        <p>All your saved information</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="stat">
        <p>🗂️ CATEGORIES</p>
        <h2>{categories}</h2>
        <p>Organized knowledge groups</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat">
        <p>🧠 YOUR SECOND BRAIN</p>
        <h2>Active</h2>
        <p>Your personal knowledge space</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

# Recent notes
left, right = st.columns([2, 1])

with left:
    st.subheader("📚 Recently Added")

    if notes:
        for n in notes[:5]:
            st.markdown(f"""
            <div class="note-card">
                <b>{n[1]}</b>
                <p class="small-text">{n[2]}</p>
                <p>{n[3][:150]}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Your knowledge library is empty. Start by saving your first note!")

with right:
    st.subheader("💡 Organize Your Mind")

    categories_list = [
        ("📖", "Study"),
        ("💼", "Work"),
        ("💭", "Ideas"),
        ("🌸", "Personal"),
        ("⭐", "Important")
    ]

    for emoji, name in categories_list:
        st.markdown(f"""
        <div class="note-card">
            {emoji} &nbsp; <b>{name}</b>
        </div>
        """, unsafe_allow_html=True)

st.divider()

st.markdown(
    "<center><p class='small-text'>MindVault © 2026 | "
    "Capture. Organize. Remember.</p></center>",
    unsafe_allow_html=True
)











