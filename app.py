import streamlit as st

# Page setup
st.set_page_config(page_title="MASTER PIECE COLLECTION", layout="centered")

# Sea blue style + BLACK LINKS
st.markdown("""
    <style>
    .stApp {
        background-color: #2E8BC0;
    }
    .title {
        background-color: #145DA0;
        color: white;
        padding: 15px;
        text-align: center;
        border-radius: 10px;
        font-size: 24px;
        font-weight: bold;
    }
    a {
        color: black !important;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">MASTER PIECE COLLECTION</div>', unsafe_allow_html=True)

# 🔗 MAIN LINK (FOR QR CODE)
st.markdown("### 🔗 Main Access Link")
st.markdown("[Open MASTER PIECE COLLECTION](https://your-app-link.streamlit.app)")

# Menu
option = st.radio("Select Option", ["Our Services", "Catalogue", "Contact Us"])

# ================= SERVICES =================
if option == "Our Services":
    st.subheader("Our Services")

    st.write("### 1. Men's Wear")
    st.markdown("[View Designs](https://www.pinterest.com/search/pins/?q=mens%20fashion)")

    st.write("### 2. Native Attire")
    st.markdown("[View Designs](https://www.pinterest.com/search/pins/?q=african%20wear%20styles)")

    st.write("### 3. Exotic Formal Wear")
    st.markdown("[View Designs](https://www.pinterest.com/search/pins/?q=formal%20wear%20men)")

    st.write("### 4. Custom Tailoring")
    st.markdown("[View Designs](https://www.pinterest.com/search/pins/?q=tailoring%20designs)")

    st.write("### 5. Ready-made Outfit")
    st.markdown("[View Designs](https://www.pinterest.com/search/pins/?q=ready%20to%20wear%20fashion)")

    st.write("### 6. Alterations and More")
    st.markdown("[View Designs](https://www.pinterest.com/search/pins/?q=clothing%20alterations)")

# ================= CATALOGUE =================
elif option == "Catalogue":
    st.subheader("Fashion Catalogue")
    st.markdown("[View Designs](https://www.pinterest.com/search/pins/?q=fashion%20designs)")

# ================= CONTACT =================
elif option == "Contact Us":
    st.subheader("Contact Us")

    st.write("📍 Location:")
    st.write("NEW EDUBIASE, ASHANTI REGION, ADANSI SOUTH DISTRICT, OPPOSITE THE GHANA EDUCATION SERVICE")

    st.write("📞 Contact:")
    st.write("0558141486")
    st.write("0208981941")
    st.write("0240253567")