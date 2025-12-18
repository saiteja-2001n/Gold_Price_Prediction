import streamlit as st
import pandas as pd
import pickle
import os
import plotly.express as px

# --------------------- Page Setup ---------------------
st.set_page_config(page_title="Gold Price Prediction", layout="centered")

# ------------------- Project Info ---------------------
st.markdown("""
# 🪙 Gold Price Prediction App
Predict the **Gold Price (GLD)** using macroeconomic indicators.

### 🔍 Features Used:
- 📉 S&P 500 Index (SPX)
- 🛢️ Crude Oil Prices (USO)
- 🪙 Silver Prices (SLV)
- 💶 EUR/USD Exchange Rate

---
""", unsafe_allow_html=True)

# ----------------- Load Model -------------------------
model_path = "knn_gold1.pkl"

if not os.path.exists(model_path):
    st.error("❌ Model file not found. Please place 'knn_gold1.pkl' in this folder.")
    st.stop()

with open(model_path, "rb") as file:
    model = pickle.load(file)

# ----------------- Input Section ----------------------
st.markdown("## 🎛️ Enter Input Values Below")

col1, col2 = st.columns(2)

with col1:
    spx = st.slider("S&P 500 Index (SPX)", 600.0, 2900.0, 670.0)
    uso = st.slider("Crude Oil Price (USO)", 5.0, 120.0, 10.0)

with col2:
    slv = st.slider("Silver Price (SLV)", 5.0, 50.0, 5.0)
    eur = st.slider("EUR/USD Exchange Rate", 1.0, 2.0, 1.0)

# ---------------- Predict Button ----------------------
if st.button("🔮 Predict Gold Price"):
    input_data = pd.DataFrame([[spx, uso, slv, eur]],
                              columns=['SPX', 'USO', 'SLV', 'EUR/USD'])

    prediction = model.predict(input_data)[0]
    st.success(f"🌟 Predicted Gold Price (GLD): **${prediction:.2f}**")
    st.info('The Predicted Gold Price is in DOLLORS  and EURO Currency')

    # Visualize Input Features
    st.markdown("### 🔧 Input Features Visualized")
    fig_bar = px.bar(
        input_data.T.reset_index().rename(columns={"index": "Feature", 0: "Value"}),
        x="Feature", y="Value",
        title="Input Features for Prediction"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

