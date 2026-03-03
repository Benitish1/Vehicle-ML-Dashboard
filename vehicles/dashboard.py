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
    pivot_table = pd.pivot_table(df, index=["manufacturer","transmission"], columns=["body_type"], values="selling_price", aggfunc=["sum","mean"], fill_value=0)
    pivot_table_html = pivot_table.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='{:,.0f}'.format,
        justify='center'
    )
    return pivot_table_html



def visualizing_sales_with_sunburst_chart(df,height=800):
    fig = px.sunburst(df ,path=["manufacturer","fuel_type","body_type"], values="selling_price") #u can also use treemap or icicle instead of sunburst
    fig.update_traces(textinfo="label+value")
    fig.update_layout(height=height)
    return opy.plot(fig, auto_open=False, output_type='div')


def visualizing_sales_with_treemap_chart(df,height=800):
    fig = px.treemap(df ,path=["manufacturer","fuel_type","body_type"], values="selling_price") 
    fig.update_traces(textinfo="label+value")
    fig.update_layout(height=height)
    return opy.plot(fig, auto_open=False, output_type='div')


def visualizing_sales_with_icicle_chart(df,height=800):
    fig = px.icicle(df ,path=["manufacturer","fuel_type","body_type"], values="selling_price") 
    fig.update_traces(textinfo="label+value")
    fig.update_layout(height=height)
    return opy.plot(fig, auto_open=False, output_type='div')


def frequency_bar_chart(df): 
    # Simple counts 
    manufacturer_counts = df['manufacturer'].value_counts().reset_index() 
    manufacturer_counts.columns = ['Manufacturer', 'Count'] 

    fig = px.bar(manufacturer_counts, x='Manufacturer', y='Count', title='Frequency of Manufacturers')
    fig.update_layout(xaxis_title='Manufacturer', yaxis_title='Count')
    return opy.plot(fig, auto_open=False, output_type='div') 

def sales_by_country(df, height=600):
    country_sales = df.groupby('client_country')['selling_price'].sum().reset_index()
    country_sales.columns = ['Country', 'Total Sales']
    fig = px.choropleth(
        country_sales,
        locations='Country',
        locationmode='country names',
        color='Total Sales',
        color_continuous_scale='Viridis',
        title='Total Sales by Country',
   )
    fig.add_scattergeo(
        locations=country_sales['Country'],
        locationmode='country names',
        text=country_sales['Country'],
        mode='text',
        textfont=dict(size=9, color='white'),
        showlegend=False,
    )
    fig.update_layout(height=height, geo=dict(showframe=False, projection_type='natural earth'))
    return opy.plot(fig, auto_open=False, output_type='div')