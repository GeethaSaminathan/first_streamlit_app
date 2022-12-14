import streamlit
import pandas 
import snowflake.connector
import requests
from urllib.error import URLError
# import pandas
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#changing number to fruits name
my_fruits_list = my_fruits_list.set_index('Fruit')
#lets select pick list
fruits_selected = streamlit.multiselect("Pick fruits:", list(my_fruits_list.index))
fruits_to_show = my_fruits_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(fruits_to_show)
#create function
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized



#NEW SECTION TO DISPLAY FRUITYVICE API RESPONSE
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
       streamlit.error("Please select fruit to get info.")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
except URLError as e:
      streamlit.error()
#function to load list into a single button
streamlit.header("The FRUIT LIST contains:")
#snowflake related function
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("use warehouse pc_rivery_wh")
       my_cur.execute("SELECT * FROM fruit_load_list")
       return my_cur.fetchall()
# add a button to load fruit
if streamlit.button('Get FRUIT LOAD LIST'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
  
#adding second text to streamlit
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
       my_cur.execute("use warehouse pc_rivery_wh")
       my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"')")
       return "Thanks for adding "+ new_fruit
    
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)


# stopping tempor
streamlit.stop()

