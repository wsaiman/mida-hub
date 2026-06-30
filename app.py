import streamlit as st
import json

st.set_page_config(
    page_title="MIDA Tools Hub",
    page_icon="🏢",
    layout="wide"
)

# ── Styling ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Hide default Streamlit header */
    #MainMenu, header, footer {visibility: hidden;}

    /* Page background */
    .stApp { background-color: #f5f7fa; }

    /* Header section */
    .hub-header {
        background: linear-gradient(135deg, #1a3a5c, #2563a8);
        padding: 2.5rem 2rem 2rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        color: white;
    }
    .hub-header h1 {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
        color: white;
    }
    .hub-header p {
        font-size: 1rem;
        opacity: 0.85;
        margin: 0.4rem 0 0 0;
        color: white;
    }

    /* App card */
    .app-card {
        background: white;
        border-radius: 12px;
        padding: 1.6rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
        transition: box-shadow 0.2s ease;
        height: 100%;
    }
    .app-card:hover {
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
    .app-icon {
        font-size: 2.2rem;
        margin-bottom: 0.8rem;
    }
    .app-name {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.4rem;
    }
    .app-desc {
        font-size: 0.88rem;
        color: #718096;
        line-height: 1.5;
        min-height: 40px;
    }

    /* Button override */
    .stLinkButton a {
        background-color: #2563a8 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-size: 0.85rem !important;
        padding: 0.45rem 1.2rem !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        width: 100% !important;
        display: block !important;
        text-align: center !important;
    }
    .stLinkButton a:hover {
        background-color: #1a4f8a !important;
    }

    /* Footer */
    .hub-footer {
        text-align: center;
        color: #a0aec0;
        font-size: 0.78rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)


# ── Load apps config ────────────────────────────────────────────────────────────
with open("apps.json", "r") as f:
    config = json.load(f)

apps = config["apps"]


# ── Header ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hub-header">
    <h1>🏢 MIDA Tools Hub</h1>
    <p>Pilih aplikasi yang ingin digunakan</p>
</div>
""", unsafe_allow_html=True)


# ── App Cards Grid ──────────────────────────────────────────────────────────────
cols_per_row = 3

for i in range(0, len(apps), cols_per_row):
    row_apps = apps[i:i + cols_per_row]
    cols = st.columns(cols_per_row, gap="medium")

    for col, app in zip(cols, row_apps):
        with col:
            st.markdown(f"""
            <div class="app-card">
                <div class="app-icon">{app['icon']}</div>
                <div class="app-name">{app['name']}</div>
                <div class="app-desc">{app['description']}</div>
            </div>
            """, unsafe_allow_html=True)

            if app.get("url"):
                st.link_button(
                    f"Open {app['name']} →",
                    url=app["url"],
                    use_container_width=True
                )
            else:
                st.button("Coming Soon", disabled=True,
                          use_container_width=True, key=app["name"])

    st.markdown("<br>", unsafe_allow_html=True)


# ── Footer ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hub-footer">
    MIDA Statistics Unit &nbsp;·&nbsp; {len(apps)} tools available
</div>
""", unsafe_allow_html=True)
