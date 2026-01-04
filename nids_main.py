# AI-Based Network Intrusion Detection System
import streamlit as st
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt

# PAGE CONFIG

st.set_page_config(
    page_title="AI NIDS Dashboard",
    layout="wide"
)

st.title("🔐 AI-Powered Network Intrusion Detection System")
st.markdown("""
This system uses **Machine Learning (Random Forest)** to detect  
**malicious network traffic** such as DDoS or abnormal behavior.
""")

# DATA LOADING (SIMULATION MODE)

@st.cache_data
def load_data():
    """
    Simulates network traffic similar to CIC-IDS2017 dataset
    """
    np.random.seed(42)
    n_samples = 5000

    data = {
        "Destination_Port": np.random.randint(1, 65535, n_samples),
        "Flow_Duration": np.random.randint(1, 100000, n_samples),
        "Total_Fwd_Packets": np.random.randint(1, 100, n_samples),
        "Packet_Length_Mean": np.random.uniform(10, 1500, n_samples),
        "Active_Mean": np.random.uniform(0, 1000, n_samples),
        "Label": np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3])
    }

    df = pd.DataFrame(data)

    # Introduce attack patterns
    df.loc[df["Label"] == 1, "Total_Fwd_Packets"] += np.random.randint(50, 200)
    df.loc[df["Label"] == 1, "Flow_Duration"] = np.random.randint(1, 1000)

    return df

df = load_data()
# SIDEBAR CONTROLS
st.sidebar.header("⚙️ Model Controls")

train_size = st.sidebar.slider(
    "Training Data Percentage",
    min_value=50,
    max_value=90,
    value=80
)

n_trees = st.sidebar.slider(
    "Number of Trees (Random Forest)",
    min_value=10,
    max_value=200,
    value=100
)

# PREPROCESSING
X = df.drop("Label", axis=1)
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=(100 - train_size) / 100,
    random_state=42
)

# MODEL TRAINING

st.divider()
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("1️⃣ Model Training")

    if st.button("Train Model Now"):
        with st.spinner("Training Random Forest..."):
            model = RandomForestClassifier(n_estimators=n_trees)
            model.fit(X_train, y_train)
            st.session_state["model"] = model
        st.success("Model trained successfully!")

# MODEL EVALUATION
with col2:
    st.subheader("2️⃣ Performance Metrics")

    if "model" in st.session_state:
        model = st.session_state["model"]
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)

        m1, m2, m3 = st.columns(3)
        m1.metric("Accuracy", f"{acc*100:.2f}%")
        m2.metric("Total Records", len(df))
        m3.metric("Threats Detected", int(sum(y_pred)))

        st.write("### Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred)

        fig, ax = plt.subplots(figsize=(4, 3))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Reds", ax=ax)
        st.pyplot(fig)

    else:
        st.warning("Train the model first.")

# LIVE TRAFFIC SIMULATION
st.divider()
st.subheader("3️⃣ Live Network Traffic Simulator")

c1, c2, c3, c4 = st.columns(4)

flow_duration = c1.number_input("Flow Duration (ms)", 0, 100000, 500)
packets = c2.number_input("Total Packets", 0, 500, 100)
pkt_length = c3.number_input("Packet Length Mean", 0, 1500, 500)
active_time = c4.number_input("Active Mean", 0, 1000, 50)

if st.button("Analyze Traffic"):
    if "model" in st.session_state:
        model = st.session_state["model"]

        input_data = np.array([[
            80,  # Destination Port (HTTP)
            flow_duration,
            packets,
            pkt_length,
            active_time
        ]])

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("🚨 MALICIOUS TRAFFIC DETECTED!")
        else:
            st.success("✅ Traffic is BENIGN (Safe)")

    else:
        st.error("Please train the model first.")
