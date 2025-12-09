import pandas as pd
import streamlit as st
import sqlite3
import plotly.express as px
import os 
import zipfile

if not os.path.exists('brEcommerce.db'):
    with zipfile.ZipFile('brEcommerce.zip', 'r') as zip_ref:
        zip_ref.extractall()

st.title("E-Commerce Dashboard")


page = st.sidebar.selectbox('Choose a view', ['Category Rank','Orders Map','Sales Trends','Business Simulator'])

if page== 'Category Rank':
    st.header("Top 5 Categories in Brazil")

    def get_data():
        conn = sqlite3.connect('brEcommerce.db')
        query = """
        SELECT 
        pc.product_category_name_english as Category,
        SUM(oi.price) as total_revenue
        FROM order_items oi 
        JOIN products p ON oi.product_id = p.product_id 
        JOIN product_category pc ON p.product_category_name = pc.product_category_name
        GROUP BY product_category_name_english
        ORDER BY total_revenue DESC
        LIMIT 5;
        """
        
        df_result = pd.read_sql(query, conn)
        conn.close()
        return df_result

    df = get_data()

    st.subheader("Data Frame:")
    st.dataframe(df)

    st.subheader("Visualization:")
    fig = px.bar(
        df, 
        x='Category', 
        y='total_revenue',
        title='Top 5 Categories',
        color_discrete_sequence=["#a06ae7"], 
        text_auto='.2s' 
    )
    
    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Revenue",
        plot_bgcolor="rgba(0,0,0,0)", 
    )

    st.plotly_chart(fig, use_container_width=True)

elif page == 'Orders Map':
    st.header("Geolocation of Customers")
    
    def get_map_data():
        conn2 = sqlite3.connect('brEcommerce.db')
        query2 = """
        SELECT 
            g.geolocation_lat as latitude, g.geolocation_lng as longitude
            FROM orders o JOIN customers c ON o.customer_id = c.customer_id 
            JOIN geolocation g ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix
        GROUP BY g.geolocation_lat, g.geolocation_lng
        LIMIT 1000;
        """

        df_result2 = pd.read_sql(query2, conn2)
        conn2.close()
        return df_result2
    
    df_map = get_map_data()

    st.map(df_map)

elif page == 'Sales Trends':
    st.header('Sales Trends 2016-2018')

    def get_sales_data():
        conn3 = sqlite3.connect('brEcommerce.db')
        query3 = """
        SELECT strftime('%Y-%m', order_purchase_timestamp) AS month, 
            SUM(oi.price) AS total_revenue
        FROM orders o JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.order_status = 'delivered'
        GROUP BY month
        ORDER BY month
        LIMIT 100
        """

        df_result3 = pd.read_sql(query3, conn3)
        conn3.close()
        return df_result3
    
    df_sales= get_sales_data();

    fig = px.line(
        df_sales, 
        x='month', 
        y='total_revenue',
        markers=True, 
        color_discrete_sequence=['#a06ae7'] 
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue",
        hovermode="x unified" 
    )

    st.plotly_chart(fig, use_container_width=True)

elif page == 'Business Simulator':
    st.header('Business Simulator')

    def get_price_freight():
        conn4 = sqlite3.connect('brEcommerce.db')
        query4 = """
        SELECT SUM(oi.price) AS current_revenue, SUM(oi.freight_value) AS current_freight
        FROM orders o JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.order_status = 'delivered'
        LIMIT 1000
        """

        df_result4 = pd.read_sql(query4, conn4)
        conn4.close()
        return df_result4.iloc[0]
    
    df_sim = get_price_freight()
    totals = get_price_freight()
    base_revenue = totals['current_revenue']
    base_freight = totals['current_freight']

    col1, col2 = st.columns(2)

    with col1:
        price_change = st.slider('Product Price Change (%) ', -50,50,0)

    with col2:
        freight_change = st.slider('Freight Price Change (%) ', -50,50,0)

    new_revenue = base_revenue * (1+(price_change/100))
    new_freight = base_freight * (1+(freight_change/100))

    diff_revenue = new_revenue - base_revenue
    diff_freight = new_freight - base_freight

    st.divider()
    st.subheader('Predicted Output: ')

    kpi1,kpi2,kpi3 = st.columns(3)

    with kpi1:
        st.metric (
            label = "Total Revenue",
            value = f"{new_revenue/ 1_000_000:.2f} M BRL",
            delta=f"{diff_revenue:,.0f} BRL"
        )

    with kpi2:
        st.metric(
            label="Freight Value",
            value=f"{new_freight/ 1_000_000:.2f} M BRL",
            delta=f"{diff_freight:,.0f} BRL",
            delta_color = "inverse"
        )
    
    with kpi3:
            total_old = base_revenue + base_freight
            total_new = new_revenue + new_freight
            diff_total = total_new - total_old

            st.metric(
                label="Total Value of Orders",
                value=f"{total_new/ 1_000_000:.2f} M BRL",
                delta = f"{diff_total:,.0f} BRL"
            )





