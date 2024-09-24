import importlib

import pandas as pd
from dbnomics import fetch_series

package_dir = importlib.resources.files("employment_situation")
"""
taux de chômage au sens du BIT
taux de concentration de l'emploi
taux de retour à l'emploi après 6 mois
taux d'inactivité : https://db.nomics.world/ILO/EIP_DWAP_SEX_EDU_RT?q=inactivity+rate&tab=list
chômage de longue durée 
niveau d'éducation et taux d'illetrisme
"""


def download_educ_data():
    female_educ_df = fetch_series(
        [
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/ARG.BA_150.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/BRA.BX_6355.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/CAN.BA_147.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/CHE.BA_253.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/COL.BA_358.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/EGY.BA_582.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/FRA.BA_148.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/IDN.BA_510.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/IND.BA_14121.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/KEN.BX_3465.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/KOR.BA_222.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/PER.BX_375.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/PSE.BA_592.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/RWA.BA_1590.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/USA.BA_453.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/VNM.BA_1788.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_F.Q",
            "",
        ]
    )

    male_educ_df = fetch_series(
        [
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/ARG.BA_150.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/BRA.BX_6355.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/CAN.BA_147.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/CHE.BA_253.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/COL.BA_358.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/EGY.BA_582.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/FRA.BA_148.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/IDN.BA_510.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/IND.BA_14121.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/KEN.BX_3465.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/KOR.BA_222.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/PER.BX_375.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/PSE.BA_592.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/RWA.BA_1590.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/USA.BA_453.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
            "ILO/EMP_TEMP_SEX_ECO_EDU_NB/VNM.BA_1788.ECO_AGGREGATE_TOTAL.EDU_AGGREGATE_TOTAL.SEX_M.Q",
        ]
    )

    list_concat_df = [female_educ_df, male_educ_df]
    new_df = pd.concat(list_concat_df)
    new_df["period"] = pd.to_datetime(new_df["original_period"]).dt.strftime("%Y-%m")
    return new_df


def download_unemployment_data():
    # Dowload unemployment data
    df_unemployment = pd.read_csv(package_dir / "data/unemployment.csv")

    new_df_unemployment = pd.melt(
        df_unemployment, id_vars=["period"], var_name="country", value_name="value"
    )
    new_df_unemployment["country"] = new_df_unemployment["country"].str.extract(
        r"(^[^\–]+)"
    )

    return new_df_unemployment


def download_output_perworker():
    df_outpout = pd.read_csv(package_dir / "data/output_perworker.csv")
    new_df_output = pd.melt(
        df_outpout, id_vars=["period"], var_name="country", value_name="value"
    )
    new_df_output["country"] = new_df_output["country"].str.extract(r"(^[^\–]+)")

    return new_df_output

def download_inactivity_data():
    df_inactivity = pd.read_csv(package_dir / "data/inactivity_data.csv")
    new_df_inactivity = pd.melt(
        df_inactivity, id_vars=["period"], var_name = "country", value_name ="value")
    new_df_inactivity["country"] = new_df_inactivity["country"].str.extract(r"(^[^\–]+)")
    return new_df_inactivity