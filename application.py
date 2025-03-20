import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("airbnb.csv")
df.head()

st.sidebar.header("Filters")
neighbourhood_group = st.sidebar.multiselect("Select Neighbourhood Group", df["neighbourhood_group"].unique(), df["neighbourhood_group"].unique())
listing_type = st.sidebar.multiselect("Select Listing Type", df["room_type"].unique(), df["room_type"].unique())

filtered_df = df[(df["neighbourhood_group"].isin(neighbourhood_group)) & (df["room_type"].isin(listing_type))]


tab1, tab2 = st.tabs(["Overview", "Analysis"])

with tab1:
    st.title("Lara Bonavoglia Comas - Airbnb")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Listings by Neighbourhood Group")
        fig1 = px.histogram(filtered_df, x="neighbourhood_group", color="room_type", barmode="group")
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Price Distribution by Listing Type")
        fig2 = px.box(filtered_df[filtered_df["price"] < 500], x="room_type", y="price")
        st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.title("Detailed Analysis")
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Reviews per Month by Neighbourhood")
        fig3 = px.bar(filtered_df.groupby("neighbourhood")["reviews_per_month"].mean().reset_index(), 
                      x="neighbourhood", y="reviews_per_month", color="neighbourhood")
        st.plotly_chart(fig3, use_container_width=True)
    
    with col4:
        st.subheader("Price vs. Number of Reviews")
        fig4 = px.scatter(filtered_df, x="number_of_reviews", y="price", color="room_type")
        st.plotly_chart(fig4, use_container_width=True)

    st.subheader("Listings Map")
    st.map(filtered_df.dropna(subset=["latitude", "longitude"]))

st.sidebar.text("Airbnb Analysis Dashboard")
