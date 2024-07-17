import streamlit as st
import pandas as pd
import plost

# Set page config to be expandable
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# Load css file
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Sidebar
st.sidebar.header("Weather Dashboard")
page = st.sidebar.selectbox("Select a page", ["Heatmap", "Line Chart"])

if page == "Heatmap":
    st.sidebar.subheader("Heatmap parameter")
    heatmap_chart_color = st.sidebar.selectbox("Color by", ["precipitation", "temp_min", "temp_max", "wind"])

if page == "Line Chart":
    st.sidebar.subheader("Line chart parameters")
    plot_data = st.sidebar.multiselect('Select data', ["precipitation", "temp_min", "temp_max", "wind"], ["temp_min", "temp_max"])
    plot_height = st.sidebar.slider('Specify line plot height', 200, 800, 400)

st.sidebar.markdown('''
                    ---
                    **Created by** [Omar Alaridi](https://www.linkedin.com/in/omar-alaridi)
                    ''')

# Load data
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

# Main page content
if page == "Heatmap":
    st.markdown('### Heatmap')
    plost.time_hist(
        data=seattle_weather,
        date='date',
        x_unit='week',
        y_unit='day',
        color=heatmap_chart_color,
        aggregate='median',
        legend=None,
        height=345,
        use_container_width=True)

elif page == "Line Chart":
    st.markdown('### Line chart')
    st.line_chart(seattle_weather, x='date', y=plot_data, height=plot_height)
