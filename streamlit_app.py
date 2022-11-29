import streamlit
streamlit.header('🍽️Breakfast Menu')
streamlit.text('🍌Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket🍊 Smoothie')
streamlit.text('🍇🍉Hard-Boiled Free-Range Egg')
import pandas 
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# lets put a pick list 
streamlit.multiselect("Pick fruits:", list(my_fruits_list.index))
  streamlit.dataframe(my_fruits_list)
