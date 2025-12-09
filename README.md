# E-Commerce Strategic Dashboard & Simulator

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

## Project Overview

This interactive Business Intelligence (BI) tool analyzes over **100,000 orders** from the Brazilian E-Commerce sector (Olist). It transforms raw data into actionable insights using a local Data Warehouse (SQLite) and provides a **Business Simulator** for financial forecasting.

### [Live Demo - Click Here](https://brecommerce-simulator-pggmfzeqhpbf4nf3fz3sw9.streamlit.app/)

---
<details>
<summary><strong>App Modules & Features</strong></summary>
<br>

The dashboard is divided into 8 strategic modules. Below is a detailed walkthrough of each feature.

### 1. Category Ranking (Top Products)
Identifies the best-selling product categories based on total revenue.
* **Tech:** SQL `JOIN` across 3 tables (Orders, Products, Translations).
* **Insight:** Highlights niche markets versus mass-market categories.

<img src="Outputs/page1.png" alt="Category Rank" width="400"  height="600">


### 2. Geolocation Map
Visualizes customer distribution across Brazil using latitude/longitude data.
* **Tech:** Streamlit `st.map` integrated with geolocation dataset.
* **Insight:** Shows concentration of sales in coastal cities vs. interior regions.

<img src="Outputs/page2.png" alt="Geolocation" width="400"  height="600">

### 3. Sales Trends (Time Series)
Analyzes revenue growth from 2016 to 2018.
* **Tech:** SQL `strftime` for monthly aggregation and Plotly Line Charts.
* **Insight:** Identifies seasonal trends (e.g., Black Friday spikes).

<img src="Outputs/page3.png" alt="Sales Trends" width="400"  height="600">

### 4. Business Simulator (What-If Analysis)
An interactive decision-support tool. Allows stakeholders to simulate changes in **Product Price** and **Freight Costs** to forecast Revenue.
* **Tech:** Dynamic Python calculation using `st.slider`.
* **Value:** Helps in planning pricing strategies and margin estimation.

<img src="Outputs/page4.png" alt="Business Simulator" width="400"  height="600">

### 5. Orders Status (Logistics)
Breakdown of delivery performance. Monitors successful deliveries vs. cancellations.
* **Tech:** SQL `GROUP BY` and Donut Charts.
* **Metric:** Tracks the "Cancellation Rate" KPI.

<img src="Outputs/page5.png" alt="Orders Status" width="400"  height="600">

### 6. Payment Types
Analysis of preferred payment methods by customers.
* **Tech:** Data aggregation and Pie Charts.
* **Insight:** Credit Card vs. Boleto (Cash) usage distribution.

<img src="Outputs/page6.png" alt="Payment Types" width="400"  height="600">

### 7. Customer Satisfaction (Reviews)
Analysis of customer sentiment based on 1-5 star ratings.
* **Tech:** Horizontal Bar Chart with Red-Green color scale.
* **Insight:** Quality Assurance metric monitoring.

<img src="Outputs/page7.png" alt="Reviews" width="400"  height="600">

### 8. Peak Hours (Customer Behavior)
Heatmap analysis identifying the busiest hours of the day.
* **Tech:** SQL Hour extraction and Color-coded Bar Chart.
* **Insight:** Determines optimal times for marketing campaigns (e.g., 14:00 - 16:00).

<img src="Outputs/page8.png" alt="Peak Hours" width="400"  height="600">
</details>

<details>
<summary><strong> Technology Stack</strong></summary>
<br>

* **Python 3.10+**
* **Streamlit**
* **SQLite**
* **Plotly Express**
* **Pandas**
  
</details>

<details>
<summary><strong> How to Run Locally</strong></summary>
<br>

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/NataliaKalista/BrECommerce-Simulator.git](https://github.com/NataliaKalista/BrECommerce-Simulator.git)
    ```
2.  **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the app:**
    ```bash
    streamlit run dashboard.py
    ```
    *(Note: The database `brEcommerce.db` is automatically extracted from the ZIP archive on the first run to bypass GitHub file size limits).*
</details>
