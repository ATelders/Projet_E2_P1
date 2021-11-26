import main
import pandas as pd
import streamlit as st
import numpy as np

X = pd.read_csv("clean_X.csv")


def test_user_input_features():
    """
    Test user input features
    """
    assert isinstance(main.user_input_features(), pd.DataFrame)


def test_predict_price():
    """
    Test predict price
    """
    Age = st.sidebar.slider('Ancienneté du bien', int(X.Age.min()), int(X.Age.max()), int(X.Age.mean()))
    LotArea = st.sidebar.slider('Surface totale', int(X.LotArea.min()), int(X.LotArea.max()), int(X.LotArea.mean()))
    GrLivArea = st.sidebar.slider('Surface au sol', int(X.GrLivArea.min()), int(X.GrLivArea.max()), int(X.GrLivArea.mean()))
    LotFrontage = st.sidebar.slider('Taille de la façade', int(X.LotFrontage.min()), int(X.LotFrontage.max()), int(X.LotFrontage.mean()))
    GarageArea = st.sidebar.slider('Taille du garage', int(X.GarageArea.min()), int(X.GarageArea.max()), int(X.GarageArea.mean()))
    Fence = st.sidebar.select_slider('Présence de barrières', options=[False, True])
    Pool = st.sidebar.select_slider('Piscine souhaitée?', options=[False, True])

    data = {'Age': 20,
            'GrLivArea': 2000,
            'LotFrontage': 100,
            'LotArea': 500,
            'GarageArea': 100,
            'Fence': True,
            'Pool' : False
            }
    features = pd.DataFrame(data, index=[0])
    assert isinstance(main.predict_price(features), np.ndarray)
    assert isinstance(main.predict_price(features).tolist()[0], float)
    assert 0 < main.predict_price(features).tolist()[0] < 1000000