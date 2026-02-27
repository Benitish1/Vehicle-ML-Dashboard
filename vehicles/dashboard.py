import plotly.express as px 
import plotly.offline as opy 
import plotly.graph_objects as go 
import pandas as pd 
def frequency_table(df): 
    # Simple counts 
    manufacturer_counts = df['manufacturer'].value_counts().reset_index() 
    manufacturer_counts.columns = ['Manufacturer', 'Count'] 
    # Convert to HTML using the correct method name: .to_html() 
    table_html = manufacturer_counts.to_html( 
        classes="table table-bordered table-striped table-sm",  
        float_format='%.2f', 
        justify='center' 
    ) 
    return table_html 


def aggregate_table(df):
    df['profit'] = df['selling_price'] - df['wholesale_price']
    result = df.groupby(['manufacturer','transmission','fuel_type']).agg({
        
        'selling_price': ['count', 'sum'],
        'wholesale_price': ['sum'],
        'profit': ['sum']
    })
    aggregate_table_html = result.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='{:,.0f}'.format,
        justify='center'
    )
    return aggregate_table_html

def compute_range(x):
    return x.max() - x.min()

def crosstab_table(df):
    crosstab_table = pd.crosstab(df["manufacturer"], df["body_type"], margins=True, values=df["selling_price"], aggfunc=compute_range, normalize="index" )
    crosstab_table_html = crosstab_table.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )
    return crosstab_table_html

#aggfunc=sum

def pivot_table(df):
    pivot_table = pd.pivot_table(df, index=["manufacturer"], columns=["body_type"], values="selling_price", aggfunc=["sum","mean"], fill_value=0)
    pivot_table_html = pivot_table.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='{:,.0f}'.format,
        justify='center'
    )
    return pivot_table_html