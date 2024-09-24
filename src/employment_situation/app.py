import streamlit as st
from streamlit_option_menu import option_menu

from data_loader import  download_educ_data, download_unemployment_data, download_output_perworker, download_inactivity_data
from charts_creator import plot_educ_per_country, plot_unemployment_per_country, plot_output_, plot_inactivity_data

from csv import writer
import importlib

def main() -> None:
    package_dir = importlib.resources.files("employment_situation")
    st.set_page_config(
        page_title="The Employment Situation around the World ",
        page_icon=str(package_dir / "images/favicon.png"),
    )
    st.image(str(package_dir / "images/dbnomics.svg"), width=300)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css(str(package_dir / "assets/styles.css"))
    st.markdown(
        """
        <style>
        hr {
            height: 1px;
            border: none;
            color: #333;
            background-color: #333;
            margin-top: 3px;
            margin-bottom: 3px;
        }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=[
                "Explanations",
                "Education",
                "Unemployment Rate",
                "Output per Worker",
                "Inactivity Rate",
                "Sources"
            ],
            icons=[
                "book",
                "bar-chart",
                "bar-chart",
                "bar-chart",
                "bar-chart",
                "search",
            ],
            menu_icon=":",
            default_index=0,
        )

    if selected == "Explanations":
        st.write("In progress...")    

    if selected == "Education":
    #Education level for country / men vs women
        df = download_educ_data()
        countries = df["Reference area"].unique()
        select_country = st.selectbox("Select a country", countries)
        if select_country:
            fig = plot_educ_per_country(df, select_country)
            st.plotly_chart(fig)

    if selected == "Unemployment Rate":
    #Plot mean level of education per year 
        df1 = download_unemployment_data()
        countries = df1["country"].unique()
        select_country1 = st.selectbox("Select a country/region", countries)
        if select_country1:
            fig1 = plot_unemployment_per_country(df1, select_country1)
            st.plotly_chart(fig1)
    if selected == "Output per Worker":
        df2 = download_output_perworker()
        countries = df2["country"].unique()
        select_country2 = st.selectbox("Select a country/region", countries)
        if select_country2:
            fig2 = plot_output_(df2, select_country2)
            st.plotly_chart(fig2)
    if selected == "Inactivity Rate":
        df3 = download_inactivity_data()
        countries = df3["country"].unique()
        select_country3 = st.selectbox("Select a country", countries)
        if select_country3:
            fig3 = plot_inactivity_data(df3, select_country3)
            st.plotly_chart(fig3)
if __name__ == "__main__":
    main()