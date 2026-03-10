import streamlit as st
import pandas as pd
import os
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.utils import load_data
from io import BytesIO

# ----------------------
# Page Config & Styling
# ----------------------
st.set_page_config(
    page_title=" Flipkart E-Commerce Insight Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# ----------------------
# Custom Styled Title Section (working!)
# ----------------------
st.markdown("""
    <div style='
        background-color: #e3f2fd;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    '>
        <h1 style='color: #0d47a1; font-size: 2.5rem;'>🛒 Flipkart E-Commerce Product Insight Dashboard</h1>
        <p style='color: #333; font-size: 1.1rem;'>
            Welcome to the interactive dashboard for analyzing Flipkart product data.
            Upload your dataset to explore pricing trends, top brands, discounts, and customer satisfaction insights.
        </p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<style>

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #eef2f7;
}

/* Make ALL sidebar text dark */
[data-testid="stSidebar"] * {
    color: #000000 !important;
}

/* Multiselect input box */
[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* Dropdown arrow */
[data-baseweb="select"] svg {
    fill: #000000 !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* App background with transparent texture */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/geometry.png");
        background-size: repeat;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)


#st.sidebar.markdown("## 🔎 Filter Products")

# -------------
# File Upload
# -------------
uploaded_file = st.file_uploader("📁 Upload your cleaned CSV file", type=["csv"])

if uploaded_file is not None:
    df = load_data(uploaded_file)

    # Import chart functions after file upload to avoid import error
    from app.components import charts

    #st.markdown("## 📊 Insights Overview")

    # ---------------------
    # View Mode Selector
    # ---------------------
    #st.markdown("### 🧭 Choose Chart Display View")
  #  view_mode = st.radio(
   #     "📐 Select View Mode",
    #    ["One per row (Detailed)", "Two per row (Compact)", "Three per row (Grid)"],
     #   horizontal=True
   # )


    # ------------------
    # Filter Selections
    # ------------------
    with st.sidebar:
        st.markdown("## 🔍 Filter Products", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
    categories = st.sidebar.multiselect("Select Categories", options=df['main_category'].unique())
    ratings = st.sidebar.slider("Minimum Rating", 1.0, 5.0, (1.0, 5.0), step=0.1)
    price_range = st.sidebar.slider("Discounted Price Range (₹)", 0, int(df['discounted_price'].max()), (0, int(df['discounted_price'].max())))

    if categories:
        df = df[df['main_category'].isin(categories)]
    df = df[(df['rating'] >= ratings[0]) & (df['rating'] <= ratings[1])]
    df = df[(df['discounted_price'] >= price_range[0]) & (df['discounted_price'] <= price_range[1])]

    # -------------------
    # Show All Insights - Responsive Layout
    # -------------------
    
   # ---------------------
    # Chart Display View – With Tabs
    # ---------------------
    st.markdown("""
    <div style='background-color: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 10px;'>
        <h2>📊 Insights Overview</h2>
    </div>
""", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📈 Ratings", "💸 Discounts", "💰 Pricing", "🏷️ Brands"])
    
    with tab1:
        st.markdown("### 📈 Average Rating per Category", unsafe_allow_html=True)
        st.pyplot(charts.plot_avg_rating_per_category(df))
    
        st.markdown("### ⭐ Rating vs Discounted Price", unsafe_allow_html=True)
        st.pyplot(charts.plot_rating_vs_discounted_price(df))
    
    with tab2:
        st.markdown("### 💸 Discount % vs Discounted Price", unsafe_allow_html=True)
        st.pyplot(charts.plot_discount_vs_price(df))
    
        st.markdown("### 🧾 Top 10 Discounted Products (Treemap)", unsafe_allow_html=True)
        st.pyplot(charts.plot_top_discount_products_treemap(df))
    
        st.markdown("### 🍭 Average Discount per Category (Lollipop)", unsafe_allow_html=True)
        st.pyplot(charts.plot_lollipop_avg_discount_per_category(df))
    
    with tab3:
        st.markdown("### 📉 Price Distribution (Top Categories)", unsafe_allow_html=True)
        st.pyplot(charts.plot_price_distribution_top_categories(df))
    
    with tab4:
        st.markdown("### 🏷️ Top Brands by Product Count", unsafe_allow_html=True)
        st.pyplot(charts.plot_top_brands_by_product_count(df))



    # -------------------------
    # Download Charts as PDF
    # -------------------------
    st.markdown("## 📥 Download Insights", unsafe_allow_html=True)

    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages

    pdf_buffer = BytesIO()
    with PdfPages(pdf_buffer) as pdf:
        for plot_func in [
            charts.plot_avg_rating_per_category,
            charts.plot_price_distribution_top_categories,
            charts.plot_discount_vs_price,
            charts.plot_rating_vs_discounted_price,
            charts.plot_top_discount_products_treemap,
            charts.plot_top_brands_by_product_count,
            charts.plot_lollipop_avg_discount_per_category
        ]:
            fig = plot_func(df)
            pdf.savefig(fig)
            plt.close(fig)

    st.download_button(
        label="📩 Download All Insights as PDF",
        data=pdf_buffer.getvalue(),
        file_name="ecommerce_insights.pdf",
        mime="application/pdf"
    )

else:
    st.info("👆 Please upload a cleaned e-commerce CSV file to begin.")
