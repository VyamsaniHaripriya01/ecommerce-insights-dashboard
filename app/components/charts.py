import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import squarify
import pandas as pd

# Ensure correct backend for matplotlib with Streamlit
plt.switch_backend('agg')

def plot_avg_rating_per_category(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_rating = df.groupby('main_category')['rating'].mean().sort_values(ascending=False)
    sns.barplot(x=avg_rating.values, y=avg_rating.index, ax=ax, palette='viridis')
    ax.set_title('Average Rating by Main Category')
    return fig

def plot_price_distribution_top_categories(df):
    top5 = df['main_category'].value_counts().nlargest(5).index
    top_df = df[df['main_category'].isin(top5)]
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=top_df, x='main_category', y='discounted_price', ax=ax)
    ax.set_title('Price Distribution Across Top 5 Categories (Capped at ₹5000)')
    ax.set_ylim(0, 5000)
    return fig

def plot_discount_vs_price(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='discounted_price', y='discount_percent', ax=ax, alpha=0.5)
    sns.regplot(data=df, x='discounted_price', y='discount_percent', scatter=False, ax=ax, color='red')
    ax.set_title('Discount % vs Discounted Price')
    return fig

def plot_rating_vs_discounted_price(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='discounted_price', y='rating', ax=ax, alpha=0.5, color='purple')
    sns.regplot(data=df, x='discounted_price', y='rating', scatter=False, ax=ax, color='red')
    ax.set_title('Rating vs Discounted Price')
    return fig

def plot_top_discount_products_treemap(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    top10 = df.sort_values('discount_percent', ascending=False).head(10)
    labels = [f"{name[:25]}...\n{disc:.1f}%" for name, disc in zip(top10['product_name'], top10['discount_percent'])]
    squarify.plot(sizes=top10['discount_percent'], label=labels, alpha=0.8)
    plt.title('Top 10 Products by Discount % (Treemap)')
    plt.axis('off')
    return fig

def plot_top_brands_by_product_count(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    top_brands = df['brand'].value_counts().nlargest(10)
    sns.barplot(x=top_brands.values, y=top_brands.index, ax=ax)
    ax.set_title('Top 10 Brands by Product Count')
    return fig

def plot_lollipop_avg_discount_per_category(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_discount = df.groupby('main_category')['discount_percent'].mean().sort_values()
    ax.hlines(y=avg_discount.index, xmin=0, xmax=avg_discount.values, color='skyblue')
    ax.plot(avg_discount.values, avg_discount.index, "o")
    ax.set_title("Average Discount % per Category")
    return fig
