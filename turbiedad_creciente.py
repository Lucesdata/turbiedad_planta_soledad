import pandas as pd     
import plotly           
import plotly.express as px
import numpy as np
from dash import Dash, html, dcc
import plotly.express as px
import dash             
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_daq as daq

df = pd.read_csv("aguatratadalasirena.csv")
pd.to_datetime(df['Time'],errors='ignore')
pd.to_datetime(df['Date'],errors='ignore')

df.rename(columns = {'AP03AT9002TEMP':'temperatura', 'AP03AT9002TURB':'turbiedad', 'AP03AT9002CL2':'cloro', 'AP03AT9002PH':'ph'}, inplace = True)
df['ph']=pd.Series([round(val, 2) for val in df['ph']])
df['turbiedad']=pd.Series([round(val, 2) for val in df['turbiedad']])
df['cloro']=pd.Series([round(val, 3) for val in df['cloro']])
df['temperatura']=pd.Series([round(val, 3) for val in df['temperatura']])

dff = df.groupby('Date', as_index=False)[['ph','turbiedad', 'cloro', 'temperatura']].max()

############################################################################################################

dff_max = df.groupby('Date', as_index=False)[['ph','turbiedad', 'temperatura', 'cloro']].max()
dff2_min = df.groupby('Date', as_index=False)[['ph','turbiedad','temperatura', 'cloro']].min()
dff3_mean = df.groupby('Date', as_index=False)[['ph','turbiedad','temperatura', 'cloro']].mean()
dff4_tail = df.groupby('Date', as_index=False)[['ph','turbiedad','temperatura', 'cloro']].tail(1)

############################################################################################################

dff_max['Indicador']= 'max'
dff2_min['Indicador']= 'min'
dff3_mean['Indicador']= 'promedio'
dff4_tail['Indicador']='ultimo'
df_max_min = pd.concat([dff_max, dff2_min, dff3_mean])

############################################################################################################

turbiedad_max = df["turbiedad"].max()
turbiedad_prom = df["turbiedad"].mean()
turbiedad_min = df["turbiedad"].min()
turbiedad_ulti = df["turbiedad"].tail(1)


ph_max = df["ph"].max()
ph_prom = df["ph"].mean()
ph_min = df["ph"].min()
ph_ulti = df["ph"].tail(1)

cloro_max = df["cloro"].max()
cloro_prom = df["cloro"].mean()
cloro_min = df["cloro"].min()
cloro_ulti = df["cloro"].tail(1)

temperatura_max = df["temperatura"].max()
temperatura_prom = df["temperatura"].mean()
temperatura_min = df["temperatura"].min()
temperatura_ulti = df["temperatura"].tail(1)

############################################################################################################

turbiedad_creciente = dff_max.sort_values(by="turbiedad")
ph_creciente = dff_max.sort_values(by="ph")
cloro_creciente = dff_max.sort_values(by="cloro")
temperatura_creciente = dff_max.sort_values(by="temperatura")

############################################################################################################
############################################################################################################
############################################################################################################


print(turbiedad_creciente)

fig = px.bar(turbiedad_creciente, x = "Date", y = "turbiedad", title="Turbiedad Creciente Planta Soledad")

fig.show()
             