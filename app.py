import streamlit as st
from fetch_data import get_cars
st.title('Car Rental Dashboard')
df=get_cars()
st.dataframe(df)
st.write('Total Cars:')
st.metric('Cars Count',len(df))

#add saerch features
search=st.text_input('Search by Brand')
if search:
    df=df[
        df['brand'].str.contains(search,case=False)]
st.dataframe(df)
#add filter 
brands=df['brand'].unique()
selected=st.selectbox('Select Brand',brands)

filtered=df[df['brand']==selected]
st.dataframe(filtered)

#add charts
st.bar_chart(df.groupby('brand').size())