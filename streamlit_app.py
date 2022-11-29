import streamlit
import pandas 
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#changing number to fruits name
my_fruits_list = my_fruits_list.set_index('Fruit')
# lets put a pick list 
fruits_selected=streamlit.multiselect("Pick fruits:", list(my_fruits_list.index)),['Avacado','Strawberries']
fruits_to_show = my_fruits_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
