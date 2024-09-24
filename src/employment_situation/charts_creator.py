import plotly_express as px
import plotly.graph_objects as go
import pandas as pd

def plot_educ_per_country(new_df, select_country):
    countries = new_df["Reference area"].unique()
    for country in countries:
        df_country = new_df[new_df["Reference area"] == select_country]
        fig = px.line(
            df_country, 
            x = "original_period", 
            y = "value", 
            color = "sex", 
            title = f"Education Level according to Sex for {select_country}"
        )
        fig.update_layout(
        xaxis_title = "Quarters", 
        yaxis_title = "Share of population", 

        )

    return fig

def plot_unemployment_per_country(new_df_unemployment, select_country1): 


    countries = new_df_unemployment["country"].unique()

    for country in countries: 
        df_country = new_df_unemployment[new_df_unemployment["country"] == select_country1]
        fig = px.line(
            df_country, 
            x = "period", 
            y = "value", 
            color = "country", 
            title = f"Unemployment for {select_country1}",
            markers = True 
        )
        fig.update_traces(line_color = "limegreen")
        fig.update_layout(
            xaxis_title = "Years",
            yaxis_title = f"Unemployment for {select_country1} (%)"
        )
    return fig 

def plot_output_(new_df_output, select_country2):
    countries = new_df_output["country"].unique()

    for country in countries: 
        df_country = new_df_output[new_df_output["country"] == select_country2]
        fig = px.line(
            df_country, 
            x = "period", 
            y = "value", 
            color = "country", 
            title = f"Output per worker for {select_country2} (GDP constant 2017 international $ at PPP)", 
            markers= True
        )
        fig.update_traces(line_color = "limegreen")
        fig.update_layout(
            xaxis_title = "Years",
            yaxis_title = f"Output per worker for {select_country2} (%)"
        )
    return fig

def plot_inactivity_data(new_df_inactivity, select_country3):
    countries = new_df_inactivity["country"].unique()
    for country in countries: 
        df_country = new_df_inactivity[new_df_inactivity["country"] == select_country3]
        fig = px.line(
            df_country,
            x = "period", 
            y = "value", 
            color = "country", 
            title = f"Inactivity rate for {select_country3}", 
            markers = True
        )
        fig.update_traces(line_color = "limegreen")
        fig.update_layout(
            xaxis_title = "Years", 
            yaxis_title = "Inactivity rate for {select_country3} (%)"
        )
    return fig 

    