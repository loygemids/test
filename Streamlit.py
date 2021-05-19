import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import geopandas as gpd
#from streamlit_folium import folium_static 
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("schools_combined.csv")


my_page = st.sidebar.radio("Page Nav", ["page 1", "page 2", "page 3"])
if my_page == 'page 1':
    st.title("Data")
    st.header("Public School Data in the Philippines")
    df = pd.read_csv("schools_combined.csv")

    if st.checkbox('Show data', value=True):
        st.subheader('Data')
        data_load_state = st.text('Loading data...')
        st.write(df.head(20))
        data_load_state.markdown('Loading data...**done!**')
    
elif my_page == 'page 2':
    option = st.sidebar.selectbox(
        'Which number do you like best?',
         df['region'].unique())
    'You selected: ', option

    grade_level = df[df["region"]==option].groupby("year_level")["enrollment"].sum()

    # store figure in fig variable
    fig = plt.figure(figsize=(8,6)) 

    plt.bar(grade_level.index, grade_level.values) 

    plt.title("Students in Public Schools", fontsize=16)
    plt.ylabel("Number of Enrollees", fontsize=12)
    plt.xlabel("Year Level", fontsize=12)
    year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
            "first year", "second year", "third year", "fourth year"]
    plt.xticks(range(len(grade_level.index)), year, rotation=45)
elif my_page == 'page 3':
    st.title("Geospatioal Analysis of Schools")
    schools = gpd.read_file('./phl_schp_deped/phl_schp_deped.shp')
    schools["x"] = schools.geometry.centroid.x
    schools["y"] = schools.geometry.centroid.y
    #st.write(schools.head(20))
    # Coordinates to show
    map_center = [14.583197, 121.051538]

    # Styling the map
    mymap = folium.map(location=map_center, height=700, width=1000,
                       tiles="OpenStreetMap", zoom_start=14)
    option_city = st.sidebar.selectbox(
        'Which city',
        schools["Division"].unique())
    
    'You selected: ', option_city
    city = option_city

    df_city = schools[schools["Division"]==city]

    for i in np.arange(len(df_city)):
        lat = df_city["y"].values[i]
        lon = df_city["x"].values[i]
        name = df_city["School"].values[i]
        folium.Marker([lat, lon], popup=name).add_to(mymap)
    folium_static(mymap)
    # display graph
    st.pyplot(fig)
#st.write(df.head(10))

st.title("Hello")
# 3: Adding text in page

# Add title to the page
st.title("Data")
# Add section header
st.header("Public School Data in the Philippines")



# Add any text
data_load_state = st.text('Loading data...')
df = pd.read_csv("schools_combined.csv")
st.write(df.head(20))

if st.textbox('Show data', value=True):
    st.subheader('Data')
    data_load_state = st.text('Loading data...')
    st.write(df.head(20))
    data_load_state.markdown('Loading data...**done!**')

# Customize texts using markdown
data_load_state.markdown('Loading data...**done!**')

# 4: Adding plots to Streamlit

#Copy paste your code from Jupyter but assign plt.figure to variable
grade_level = df.groupby('year_level')['enrollment'].sum()
fig = plt.figure(figsize=(8,6)) 
plt.bar(grade_level.index, grade_level.values) 
plt.title("Students in Public Schools", fontsize=16)
plt.ylabel("Number of Enrollees", fontsize=12)
plt.xlabel("Year Level", fontsize=12)
year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
        "first year", "second year", "third year", "fourth year"]
plt.xticks(range(len(grade_level.index)), year, rotation=45)

# display graph by plotting figure variable
plt.show()
st.pyplot(fig)

# 5: Adding interactive options: checkbox


    
    # 6: Adding interactive options: dropdown box
#Create dropdown box
option = option = st.selectbox('which region', df['region'].unique())

'You selected: ', option

# Filter the entry in the plot
grade_level = df['region' == option].groupby("year_level")["enrollment"].sum()

# store figure in fig variable
fig = plt.figure(figsize=(8,6)) 

plt.bar(grade_level.index, grade_level.values) 

plt.title("Students in Public Schools", fontsize=16)
plt.ylabel("Number of Enrollees", fontsize=12)
plt.xlabel("Year Level", fontsize=12)
year = ["grade 1","grade 2", "grade 3", "grade 4", "grade 5", "grade 6",
        "first year", "second year", "third year", "fourth year"]
plt.xticks(range(len(grade_level.index)), year, rotation=45)

# display graph
st.pyplot(fig)