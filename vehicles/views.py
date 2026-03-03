
import pandas as pd 
from django.shortcuts import render 
from .dashboard import aggregate_table, crosstab_table, frequency_table, pivot_table, visualizing_sales_with_icicle_chart, visualizing_sales_with_sunburst_chart, visualizing_sales_with_treemap_chart,frequency_bar_chart,sales_by_country
def dashboard_view(request): 
    queryset = pd.read_csv("dummy_data/vehicles_data_1000.csv") 
    df = pd.DataFrame(queryset) 
    return render(request, "vehicles/index.html", { 
    "frequency_table": frequency_table(df) ,
    "aggregate_table": aggregate_table(df),
    "crosstab_table": crosstab_table(df),
    "pivot_table": pivot_table(df),
    'sunburst_chart': visualizing_sales_with_sunburst_chart(df),
    'treemap_chart': visualizing_sales_with_treemap_chart(df),
    'icircle_chart': visualizing_sales_with_icicle_chart(df),
    'frequency_bar_chart': frequency_bar_chart(df),
    'sales_by_country': sales_by_country(df)
    })