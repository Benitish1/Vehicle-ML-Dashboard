
import pandas as pd 
from django.shortcuts import render 
from .dashboard import aggregate_table, crosstab_table, frequency_table, pivot_table
def dashboard_view(request): 
    queryset = pd.read_csv("dummy_data/vehicles_data_1000.csv") 
    df = pd.DataFrame(queryset) 
    return render(request, "vehicles/index.html", { 
    "frequency_table": frequency_table(df) ,
    "aggregate_table": aggregate_table(df),
    "crosstab_table": crosstab_table(df),
    "pivot_table": pivot_table(df)
    })