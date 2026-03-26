import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objs as go
from src.simulator import stream_rows
from src.utils import add_flag
st.title("Well Log Anomaly Realtime")
model = joblib.load("models/isolation_forest.pkl")
if st.button("Start"):
    hist = pd.DataFrame(columns=['GR','RHOB','NPHI','anomaly'])
    for row in stream_rows("data/clean_logs.csv",0.5):
        d = row[['GR','RHOB','NPHI']]
        p = model.predict(d)
        d = add_flag(d,p)
        hist = pd.concat([hist,d]).tail(100)
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=hist['GR']))
        a = hist[hist['anomaly']==1]
        fig.add_trace(go.Scatter(x=a.index,y=a['GR'],mode='markers'))
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(hist.tail(5))
