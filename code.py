import csv 
import pandas as pd
import plotly.express as px

scatterdata= pd.read_csv('data.csv')
scatterchart= px.scatter(scatterdata, x='date', y= 'cases', color= 'country')
scatterchart.show()