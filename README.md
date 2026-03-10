# 📊 E-commerce Insights Dashboard

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ecommerce-insights-dashboard-da.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![License](https://img.shields.io/badge/License-Custom-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/VyamsaniHaripriya01/ecommerce-insights-dashboard)
![GitHub Repo Size](https://img.shields.io/github/repo-size/VyamsaniHaripriya01/ecommerce-insights-dashboard)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🚀 Project Overview

An interactive **Streamlit dashboard** that analyzes Flipkart e-commerce product data to generate insights on pricing, discounts, ratings, and product categories.

This project demonstrates an **end-to-end data analytics workflow** including data scraping, cleaning, exploratory data analysis, and interactive visualization.

---

## 📂 Project Structure

```
ecommerce-insight-app
│
├── app/
│ ├── components/
│ │ └── charts.py     # Visualization functions
│ ├── main.py         # Streamlit dashboard
│ └── utils.py        # Data processing utilities
│
├── data/
│ ├── raw/                            # Original dataset
│ │ └── flipkart_com_ecommerce_sample.csv
│ └── processed/                      # Cleaned dataset used in dashboard
│ └── flipkart_cleaned.csv
│
├── notebooks/
│ └── explore_insights.ipynb
│
├── scripts/
│ ├── scrape.py
│ ├── clean_data.py
│ ├── explore_data.py
│ └── unzip_dataset.py
└── LICENSE│
├── requirements.txt
└── README.md
```

---

## 🔍 Features

- 📈 Interactive **data visualizations**
- 🛒 **Product category analysis**
- 💰 **Price and discount insights**
- ⭐ **Rating distribution analysis**
- ☁️ Word cloud visualization of product titles
- 🎛 **Sidebar filters** for dynamic exploration

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Matplotlib
- WordCloud
- Selenium (for data scraping)

---

## 📊 Key Insights

- Top performing product categories
- Discount trends across categories
- Product price distribution
- Relationship between ratings and pricing
- Common keywords in product titles

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/VyamsaniHaripriya01/ecommerce-insight-app.git
```

### 2. Navigate to the project directory
```
cd ecommerce-insight-app
```

### 3. Install dependencies
```python
pip install -r requirements.txt
```


### 4. Run the Streamlit app
```
python -m streamlit run app/main.py
```

---

## 📌 Future Improvements

- Real-time product scraping
- Automated data updates
- Additional advanced analytics
- Integration with business intelligence tools like Power BI

---
## 🚀 Live Demo

Live App: [(https://ecommerce-insights-dashboard-da.streamlit.app/)]

---

## 📊 Dashboard Preview

![Dashboard](images/main_dashboard.png)

![Category Analysis](images/categorywise_analysis.png)

![Rating Analysis](images/rating_analysis.png)

---

## 🔍 Key Insights

- Electronics and clothing categories dominate the marketplace.
- Products with ratings above 4.2 tend to have significantly higher visibility.
- Discounts strongly influence product popularity.
- Certain categories show higher price variance indicating competitive pricing.

---

## License

This project is licensed under a custom license for **personal and educational use only**.

- ✅ You may use, modify, and share this code for learning and personal projects.
- ❌ Commercial use, resale, or offering this code as part of a paid product/service is **not allowed** without the author's permission.

To request commercial use rights, contact: hpriyavtva2001@gmail.com

---

## 👩‍💻 Author

**Vyamsani T V A Hari Priya**

Data Analyst | AI & ML Enthusiast

GitHub:  
https://github.com/VyamsaniHaripriya01