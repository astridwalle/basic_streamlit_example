##!/usr/bin/python -u
#-*- coding:utf-8 -*-
#
# Streamlit dashboard for visualizing the basic features
#
# Astrid Walle - Astrid Walle CFDsolutions
# astridwalle@cfdsolutions.net
#---------------------------------------------------------------------------------------------------
#
# 2022-01-21	Script creation
VERSION="2022-01-21"
#---------------------------------------------------------------------------------------------------
#
### EXECUTION
# streamlit run StreamlitDashboard.py
#
#---------------------------------------------------------------------------------------------------
#
### IMPORTS
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
#
#---------------------------------------------------------------------------------------------------
#
### (cached) FUNCTIONS / DATA PREPROCESSING
#
# read tables
@st.cache
def read_table(file,header=0,index_col=False,sep=" "):
    df=pd.read_csv(file,header=header,index_col=index_col,sep=sep)
    return df
#
#---------------------------------------------------------------------------------------------------
#
st.title("Welcome to your example dashboard")

st.write("Let's try some streamlit widgets")

st.markdown("---")

# structure of the dashboard
# columns
# checkbox
# expandable

if st.checkbox("show columns"):

    col1, col2, col3 = st.columns(3)

    col1.write("Column 1")

    col2.image("https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif", use_column_width=True)

    col3.write("Hello")

exp = st.expander("some more elements")

col4, col5 = exp.columns(2)

col4.write("Hello again")

col5.write("col 5")

color = st.sidebar.selectbox("select a color",["green","red","blue"],index=0)


# sidebar 
# for parameter selection


# df
df = pd.read_csv("./opti.csv")

st.write(df)


# scatterplot
x=st.selectbox("select x variable",df.columns.values)
y=st.selectbox("select y variable",df.columns.values)
trace=go.Scatter(x=df[x],y=df[y],name="full dataset",mode="markers",marker=dict(color=color))
fig = go.Figure(data=trace)
st.plotly_chart(fig)

# pics


# interactive barchart


