import streamlit as st

# Config Halaman
st.set_page_config(
    page_title="PLAYER: qwertyunpie",
    page_icon="👾",
    layout="centered"
)

# ==============================================
# Style CSS
# ==============================================
st.markdown("""
<style>
    /* --- Import Font --- */
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

    /* --- Main Background --- */
    .stApp {
        background-color: #f0f2f5; 
        /* Grid */
        background-image: 
            linear-gradient(#cad2e0 1px, transparent 1px),
            linear-gradient(90deg, #cad2e0 1px, transparent 1px);
        background-size: 40px 40px;
    }

    /* --- Main Container (Game) --- */
    .main .block-container {
        background-color: #ffffff;
        border: 4px solid #000000; 
        padding: 2rem;
        max-width: 700px;
        box-shadow: 10px 10px 0px 0px #000000;
    }
    
    /* --- Typograph --- */
    h1, h2, h3, p, div, span, button, a {
        font-family: 'Press Start 2P', cursive !important;
        color: #000000 !important;
    }
    
    h1 {
        text-transform: uppercase;
        font-size: 1.5rem !important;
        text-align: center;
        margin-bottom: 20px;
        background-color: #ff7eb6; 
        border: 3px solid #000000;
        padding: 15px;
        box-shadow: 5px 5px 0px 0px #000000;
    }
    
    /* --- Profile Area --- */
    .stAlert {
        background-color: #e0fbfc;
        border: 3px solid #000000;
        box-shadow: 5px 5px 0px 0px #000000;
    }

    /* --- Retro Buttons --- */
    div[data-testid="stLinkButton"] a {
        background-color: #ffffff !important;
        border: 3px solid #000000 !important;
        color: #000000 !important;
        font-family: 'Press Start 2P', cursive !important;
        font-size: 0.7rem !important;
        text-decoration: none;
        border-radius: 0px !important; 
        padding: 15px !important;
        text-align: center;
        /* Shadow warna-warni */
        box-shadow: 6px 6px 0px 0px #7afcff !important; 
        transition: all 0.1s ease-in-out !important;
        margin-bottom: 5px;
    }

    /* Efek Tekan Tombol */
    div[data-testid="stLinkButton"] a:hover {
        transform: translate(4px, 4px); 
        box-shadow: 2px 2px 0px 0px #000000 !important; 
        background-color: #7afcff !important; 
    }

    /* --- Saweria Button --- */
    div[data-testid="stLinkButton"] a[href*="saweria.co"] {
        background-color: #fffd82 !important; 
        box-shadow: 6px 6px 0px 0px #ff0055 !important; 
    }
    
    div[data-testid="stLinkButton"] a[href*="saweria.co"]:hover {
        background-color: #ff0055 !important; 
        color: #ffffff !important; 
    }

    /* --- Images --- */
    img {
        border: 3px solid #000000;
        box-shadow: 5px 5px 0px 0px #cad2e0;
    }
    
    hr {
        border-top: 4px solid #000000;
        opacity: 1;
    }

</style>
""", unsafe_allow_html=True)

# --- User Info ---
nama_channel = "qwertyunpie"
level = "LVL 4444" 
role = "Class: Noobiez Streamer"
bio_text = """
About Me:
> Full-time Gamers
> &
> Part-time Programmers
"""

links = {
    "📺 YOUTUBE": "https://youtube.com/@qwertyunpie",
    "👾 TWITCH": "https://twitch.tv/yunpie4444",
    "📸 INSTAGRAM": "https://instagram.com/denisyundaa",
    "💬 DISCORD SERVER": "https://discord.gg/29wsHMwxB8"
}

link_saweria = "https://saweria.co/qwertyunpie"

# --- Main ---

# Header Box
st.markdown(f"<h1>👾 {nama_channel} <br><span style='font-size:12px'>{level} | {role}</span></h1>", unsafe_allow_html=True)

# Bio Box 
st.info(bio_text)

# --- Saweria Button ---
st.write("---")
st.write("### 🛡️ SUPPORT QUEST")
st.link_button("🎒 SEND SUPPLIES", link_saweria, use_container_width=True)

# --- Links ---
st.write("---")
st.write("### 🚀 WARP ZONES")

col1, col2 = st.columns(2)

# Buttons selang-seling kiri kanan
items = list(links.items())

# Bagian Kiri
with col1:
    st.link_button(items[0][0], items[0][1], use_container_width=True)
    st.link_button(items[2][0], items[2][1], use_container_width=True)

# Bagian Kanan
with col2:
    st.link_button(items[1][0], items[1][1], use_container_width=True)
    st.link_button(items[3][0], items[3][1], use_container_width=True)


# --- Games ---
st.write("---")
st.write("### 🕹️ CURRENT MISSION")
c1, c2 = st.columns(2)

with c1:
    st.image("https://www.pixelstalk.net/wp-content/uploads/images6/Stardew-Valley-HD-Wallpaper-1.jpg", caption="FARMING...")
with c2:
    st.image("https://www.hdwallpapers.in/download/sage_4k_hd_valorant_2-2560x1440.jpg", caption="HARDSTUCK...")

# --- Footer ---
st.write("---")
st.markdown("<br><center><small>BUILT WITH PYTHON • &copy; 2026 YUNPIE</small></center>", unsafe_allow_html=True)