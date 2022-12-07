import streamlit
import pandas 



my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#changing number to fruits name
my_fruits_list = my_fruits_list.set_index('Fruit')
# lets put a pick list 
fruits_selected=streamlit.multiselect("Pick fruits:", list(my_fruits_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruits_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#NEW SECTION TO DISPLAY FRUITYVICE API RESPONSE
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
#importind request
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

#importing snowflakes connectors
import snowflake.connector

# query for trial account metadata
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("use warehouse pc_rivery_wh")
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST_")
my_data_row = my_cur.fetchone()
streamlit.text("The FRUIT LIST contains:")
streamlit.text(my_data_row)
