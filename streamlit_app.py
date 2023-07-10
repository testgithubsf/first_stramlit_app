import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_friuts_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruits_list)
