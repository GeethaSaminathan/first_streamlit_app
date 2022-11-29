import sreamlit
import pandas 
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#changing number to fruits name
my_fruits_list = my_fruits_list.set_index('Fruit')
# lets put a pick list 
streamlit.multiselect("Pick fruits:", list(my_fruits_list.index))
streamlit.dataframe(my_fruits_list)
