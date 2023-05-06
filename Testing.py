import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.graph_objs as go
import pickle
import plotly.express as px
import altair as alt

data = pd.read_csv("updated_data.csv")

def run_website():
    with st.sidebar:
        selected = option_menu('Vental Capital Analysis Website',
                            
                            ['Analytics Dashboard',
                             'Categorical ranking',
                            'Predicting success probability',
                            'Implement own dataset'],
                            default_index=0)
        
        
    if(selected == 'Analytics Dashboard'):
        
        x_column = 'total_funding_c'

        # Specify the column name for y-axis values
        y_column = 'revenue_c'

        # Filter the data to exclude null or zero values
        filtered_data = data[(data[x_column].notnull()) & (data[x_column] != 0) & (data[y_column].notnull()) & (data[y_column] != 0)]

        # Create a Streamlit app
        st.title('Total funding vs Total revenue')

        # Extract the x and y values from the filtered data
        x = filtered_data[x_column]
        y = filtered_data[y_column]

        filtered_data = data[(data[x_column].notnull()) & (data[x_column] != 0) & (data[x_column] != 1) & (data[y_column].notnull()) & (data[y_column] != 0) & (data[y_column] != 1)]

        # Create a Streamlit app
        st.title('Visualization')

        # Create the line chart using Plotly
        sc = px.scatter(filtered_data, x=x_column, y=y_column)

        # Set the chart title and axis labels
        sc.update_layout(title='Total funding vs Total revenue', xaxis_title='Funding', yaxis_title='Revenue')

        # Display the chart using Streamlit
        st.plotly_chart(sc)



        st.write("To be coded")

        fig = go.Figure(data=go.Scatter(x=data["incorporated_date_c"], y=data["total_funding_c"], mode='markers'))
        # Add axis labels and title
        fig.update_layout(xaxis_title="Incorporation Date", yaxis_title="Total Funding Amount", title="Company Funding")

        # Show plot
        st.plotly_chart(fig)


        # Create a slider to select the year
        year = st.slider("Select year", min_value=int(data["incorporated_date_c"].min()), max_value=int(data["incorporated_date_c"].max()))

        # Filter the data based on the selected year
        data_filtered = data[data["incorporated_date_c"] == year]

        # Create the plot using Plotly Express
        fig = px.scatter(data_filtered, x="incorporated_date_c", y="total_funding_c")

        # Display the plot
        st.plotly_chart(fig)


        scatter_plot = alt.Chart(data).mark_circle().encode(
            x=alt.X('revenue_growth(%)', title='Revenue Growth Rate'),
            y=alt.Y('last_valuation_c', title='Last Valuation'),
            color=alt.Color('num_funding_rounds', title='Number of Funding Rounds')
        )

        # Create button to filter data
        button_clicked = st.button('Filter data')

        # Create a container to hold the button and the plot
        container = st.container()

        # If button is clicked, filter data and show the filtered scatter plot
        if button_clicked:
            data_filtered = data[data["num_funding_rounds"] > 5]
            filtered_scatter_plot = alt.Chart(data_filtered).mark_circle().encode(
                x=alt.X('revenue_growth(%)', title='Revenue Growth Rate'),
                y=alt.Y('last_valuation_c', title='Last Valuation'),
                color=alt.Color('num_funding_rounds', title='Number of Funding Rounds')
            )
            container.altair_chart(filtered_scatter_plot, use_container_width=True)

        # Show the initial scatter plot
        container.altair_chart(scatter_plot, use_container_width=True)

        # Create a function to filter the data based on the selected range of total funding
        def filter_data(total_fund_min, total_fund_max):
            return data[(data['total_funding_c'] >= total_fund_min) & (data['total_funding_c'] <= total_fund_max)]

        # Create a function to generate the interactive bar chart
        def generate_bar_chart(df):
            chart = alt.Chart(df).mark_bar().encode(
                x='total_funding_c',
                y='employee_growth_6(%)'
            ).properties(
                width=800,
                height=400
            )
            return chart

        # Define the range of total funding to display in the bar chart
        total_fund_min = st.sidebar.slider("Minimum Total Funding", 0, 600000000, 0, 1000000)
        total_fund_max = st.sidebar.slider("Maximum Total Funding", 0, 600000000, 600000000, 1000000)

        # Filter the data based on the selected range of total funding
        filtered_data = filter_data(total_fund_min, total_fund_max)

        # Create a button to generate the bar chart
        if st.button("Generate Bar Chart"):
            # Generate the bar chart
            bar_chart = generate_bar_chart(filtered_data)
            # Display the bar chart
            st.altair_chart(bar_chart, use_container_width=True)



#         # Create a list of categories for the dropdown menu
#         categories = ['All'] + list(data['category_0'].unique())

#         # Define function to filter the data by category
#         def filter_data(category):
#             if category == 'All':
#                 return data
#             else:
#                 return data[data['category_0'] == category]

#         # Define function to create the chart
#         def create_chart(df):
#             chart = alt.Chart(df).mark_bar().encode(
#                 x='category_0',
#                 y='revenue_growth(%)',
#                 tooltip=['category_0', 'revenue_growth(%)']
#             ).properties(
#                 width=700,
#                 height=400
#             )
#             return chart

#         # Create Streamlit app
#         st.title('Revenue Growth by Company Category')
#         st.write('Select a category from the dropdown menu to filter the data.')

#         # Add dropdown menu to select category
#         category = st.selectbox('Select a category:', categories)

#         # Filter data by selected category
#         filtered_data = filter_data(category)

#         # Create chart with filtered data
#         chart = create_chart(filtered_data)
#         st.altair_chart(chart, use_container_width=True)

if(selected == 'Categorical ranking'):

        st.title('Categorical Ranking')
        num_var_display = {
                           'total_funding_c': 'Total Funding',
                           'last_valuation_c': 'Last Valuation',
                           'last_round_size_c': 'Last Funding Amount',
                           'revenue_c': 'Latest Year Revenue',
                           'revenue_growth(%)': 'Revenue Growth (%)',
                           'EBIT_c': 'Earnings Before Interest and Tax',
                           'employee_growth_6(%)': 'Employee Growth Past 6 Months (%)',
                           'employee_growth_12(%)': 'Employee Growth Past 12 Months (%)',
                           'num_founders': 'Number of Founders',
                           'num_funding_rounds': 'Number of Funding Rounds',
                           'num_shareholders': 'Number of Shareholders',
                           'min_share': 'Minimum Share',
                           'median_share': 'Median Share',
                           'max_share': 'Maximum Share'}
        num_feature = list(num_var_display.keys())
        target_feature = st.selectbox('Select a target feature', list(num_var_display.keys()), format_func=lambda x: num_var_display[x])

        if(target_feature):
            num_cat_var_display = {'name_c':'Company name',
                                    'incorporated_date_c':'Incorporated Date',
                                    'date_of_last_round':'Date of Last Round',
                                    'fy_end':'Date of Financial Year End',
                                    'total_funding_c': 'Total Funding',
                                    'last_valuation_c': 'Last Valuation',
                                    'last_round_size_c': 'Last Funding Amount',
                                    'revenue_c': 'Latest Year Revenue',
                                    'revenue_growth(%)': 'Revenue Growth (%)',
                                    'EBIT_c': 'Earnings Before Interest and Tax',
                                    'employee_growth_6(%)': 'Employee Growth Past 6 Months (%)',
                                    'employee_growth_12(%)': 'Employee Growth Past 12 Months (%)',
                                    'num_founders': 'Number of Founders',
                                    'num_funding_rounds': 'Number of Funding Rounds',
                                    'num_shareholders': 'Number of Shareholders',
                                    'min_share': 'Minimum Share',
                                    'median_share': 'Median Share',
                                    'max_share': 'Maximum Share',
                                    'category': 'Category'}
                                    
            corr_feature = st.multiselect('Select corresponding features', 
                                [feat for feat in num_cat_var_display.keys() if feat != target_feature], 
                                format_func=lambda x: num_cat_var_display[x])
            if(corr_feature):
                # Only keep the selected features
                selected_features = [target_feature] + corr_feature
                selected_data = data[selected_features]

                sorted_top = selected_data.sort_values(target_feature, ascending=False)
                sorted_bottom = selected_data.sort_values(target_feature, ascending=True)

                # Get the top 10 and bottom 10 companies based on the selected feature
                top_10 = sorted_top.head(10)
                bottom_10 = sorted_bottom.head(10)

                # Only keep the target feature and corresponding feature columns
                top_10 = top_10[[target_feature] + corr_feature]
                bottom_10 = bottom_10[[target_feature] + corr_feature]

                # Rename columns to display friendly names
                top_10.rename(columns=num_cat_var_display, inplace=True)
                bottom_10.rename(columns=num_cat_var_display, inplace=True)

                # Display the data table only if corr_feature is not empty
                if len(corr_feature) > 0:
                    st.write("Top 10")
                    st.write(top_10)
                    st.write("Bottom 10")
                    st.write(bottom_10)

                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=top_10[''], y=top_10[target_feature], mode='lines',name = 'Top10', line = dict(color = 'blue')))
                    fig.add_trace(go.Scatter(x=bottom_10[f], y=bottom_10[target_feature], mode='lines',name = 'Bottom10', line = dict(color = 'blue')))
                            
                    fig.update_layout(title='Two Datasets in One Plot',
                    xaxis_title=f,
                    yaxis_title=target_feature)

                    fig.show()
                    

                    for f in selected_features:
                        b = go.Figure()
                        b.add_trace(go.Scatter(x=top_10[f], y=top_10[target_feature], mode='lines',name = 'Top10', line = dict(color = 'blue')))
                        b.add_trace(go.Scatter(x=bottom_10[f], y=bottom_10[target_feature], mode='lines',name = 'Bottom10', line = dict(color = 'red')))
                                
                        b.update_layout(title='Two Datasets in One Plot',
                        xaxis_title=f,
                        yaxis_title=target_feature)
                        b.show()

  

    if(selected == 'Predicting success probability'):

        st.title('Predicting success probability')
        col1, col2, col3 = st.columns(3)


    if(selected == 'Implement own dataset'):

        st.title('Implement your dataset')
        file = st.file_uploader("Upload Your Dataset")
        if file:
            df = pd.read_csv(file,index_col = None)
            df.to_csv('dataset.csv', index = None)

run_website()
