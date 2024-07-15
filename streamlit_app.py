import streamlit as st
import pandas as pd
import plost

# Set page config to be expandable
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# Load css file
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("Seattle Weather Dashboard")
st.sidebar.subheader("Heatmap parameter")
heatmap_chart_color = st.sidebar.selectbox("Color by", ["temp_min", "temp_max"])

st.sidebar.subheader("Donut chart parameter")
donnut_chart_theta = st.sidebar.selectbox("Select data", ["q2", "q3"])

st.sidebar.subheader("Line chart parameters")
plot_data = st.sidebar.multiselect('Select data', ["temp_min", "temp_max"], ["temp_min", "temp_max"])
plot_height = st.sidebar.slider('Specify line plot height', 200, 500, 250)

# st.sidebar.subheader("Bar chart parameter")
# bar_chart = st.sidebar.selectbox("Filter by", ["1", "2"])

st.sidebar.markdown('''
                    ---
                    **Created by** [Omar Alaridi](https://www.linkedin.com/in/omar-alaridi)
                    ''')

# Main page
# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

c1, c2 = st.columns((7,3))
with c1:
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
with c2:
    st.markdown('### Donut chart')
    plost.donut_chart(
        data=stocks,
        theta=donnut_chart_theta,
        color='company',
        legend='bottom', 
        use_container_width=True)

# Row C
st.markdown('### Line chart')
st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)