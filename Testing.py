import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.graph_objs as go
import pickle
import plotly.express as px
import altair as alt
import numpy as np

data = pd.read_csv("final dataset.csv")
st.set_page_config(page_title="Venture Capital")

def run_website():
    with st.sidebar:
        selected = option_menu('Venture Capital Analysis Website',
                            
                            ['Analytics Dashboard',
                             'Categorical ranking',
                            'Search',
                            'Company Profile'],
                            default_index=0)
        
        
    if(selected == 'Analytics Dashboard'):
        
        st.title('Analytics Dashboard')
        st.title('Revenue Growth by Company Category')
        st.write('Select a category from the dropdown menu to filter the data.')
        

        # Define the options for the selectbox
        options = ['Overall', 'Technology','Finance','Health and Wellness','Retail and E-commerce','Education','Media and Entertainment','Travel and Hospitality','Marketing and Advertising','Human Resources','Real Estate and Property','Food and Beverage']

        # Get the user's selection
        selected_option = st.selectbox('Select a chart', options)

        # Display the selected chart
        if selected_option == 'Overall':
            industry_categories = ['Technology', 'Finance', 'Health and Wellness', 'Retail and E-commerce', 'Education',
                                   'Media and Entertainment', 'Travel and Hospitality', 'Marketing and Advertising',
                                   'Human Resources', 'Real Estate and Property', 'Food and Beverage', 'Others']

            # Calculate the average revenue growth rate for each industry category
            average_revenue_growth = {}

            for category in industry_categories:
                category_df = data[data[category] == 1]
                average_growth = category_df['revenue_c'].mean()
                average_revenue_growth[category] = average_growth

            # Create a Bar object
            bar = go.Bar(x=list(average_revenue_growth.keys()), y=list(average_revenue_growth.values()))

            # Set the layout
            layout = go.Layout(title='Average Revenue Growth Rate by Industry Category',
                               xaxis=dict(title='Industry Category'),
                               yaxis=dict(title='Average Revenue Growth'),
                               height=500)

            # Create a Figure object
            fig = go.Figure(data=[bar], layout=layout)

            # Display the graph in Streamlit
            st.plotly_chart(fig)

        if selected_option == 'Technology':
            
            variables = [
                'Information Technology', 'Software', 'Mobile Apps', 'Internet',
                'Artificial Intelligence (AI)', 'Internet of Things (IoT)', 'Web Development',
                'Cloud', 'Automation', 'Big Data', 'Machine Learning', 'Robotics',
                'Blockchain', 'Augmented Reality (Ar)', 'Virtual Reality (VR)', 'Smart Home',
                'Clean Energy', 'Sensor', 'Nanotechnology', 'Developer Apis' ]

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Variable': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Variable', y='Mean Revenue', title='Average Mean Revenue by Variable')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            
        if selected_option == 'Finance':
            
            variables =  ['Financial Services', 'Fintech', 'Payments', 'Insurance', 'Investment', 'Accounting', 'Lending', 'Personal Finance', 'Cryptocurrency', 'Invoice Trading', 'Wealth Management', 'Transaction Processing', 'Micro Lending']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Variable': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Variable', y='Mean Revenue', title='Average Mean Revenue by Variable')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            

            
             
        if selected_option == 'Health and Wellness':
            
            variables = ['Health Care', 'Healthtech', 'Medical Device', 'Fitness', 'Medical', 'Biotechnology', 'Nutrition', 'Dental', 'Pharmaceuticals', 'Personal Health', 'Home Health Care', 'Medtech', 'Elder Care']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Health and Wellness': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Health and Wellness', y='Mean Revenue', title='Average Mean Revenue by Health and Wellness')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            
            
        if selected_option == 'Retail and E-commerce':
            
            variables =  ['E-Commerce', 'Marketplace', 'Retail', 'Fashion', 'Grocery', 'Shopping', 'Cosmetics', 'Gift', 'Catering', 'Wholesale', 'Subscription Service', 'Bakery', 'Alcohol', 'Mattress']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Retail and E-commerce': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Retail and E-commerce', y='Mean Revenue', title='Average Mean Revenue by Retail and E-commerce')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            
            
        if selected_option == 'Health and Wellness':
            
            variables = ['Health Care', 'Healthtech', 'Medical Device', 'Fitness', 'Medical', 'Biotechnology', 'Nutrition', 'Dental', 'Pharmaceuticals', 'Personal Health', 'Home Health Care', 'Medtech', 'Elder Care']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Health and Wellness': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Health and Wellness', y='Mean Revenue', title='Average Mean Revenue by Health and Wellness')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            
        if selected_option == 'Education':
            
            variables = ['Education', 'E-Learning', 'EdTech', 'Training', 'Higher Education', 'Secondary Education', 'Tutoring']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Education': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Education', y='Mean Revenue', title='Average Mean Education')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            
        if selected_option == 'Media and Entertainment':
            
            variables = ['Media & Entertainment', 'Music', 'TV', 'Broadcasting', 'Photography', 'Film Production', 'Content Creators']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Media and Entertainment': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Media and Entertainment', y='Mean Revenue', title='Average Mean Media and Entertainment')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            
        if selected_option == 'Travel and Hospitality':
            
            variables = ['Travel', 'Tourism', 'Hospitality', 'Adventure Travel', 'Resorts', 'Co-Living', 'Fast-moving Consumer Goods (FMCG)', 'Tea', 'Air Transportation', 'Maritime']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Travel and Hospitality': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Travel and Hospitality', y='Mean Revenue', title='Average Mean Travel and Hospitality')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            
        if selected_option == 'Marketing and Advertising':
            
            variables =['Marketing', 'Digital Marketing', 'Advertising', 'Content Marketing', 'Loyalty', 'Loyalty Programs', 'Payroll', 'Email Marketing', 'Influencers', 'Affiliate Marketing']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Marketing and Advertising': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Marketing and Advertising', y='Mean Revenue', title='Average Mean Marketing and Advertising')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            
        if selected_option == 'Human Resources':
            
            variables =['Human Resources', 'Recruitment', 'Staffing Agency', 'Employment', 'Employee Benefits', 'Entrepreneur First', 'Professional Networking']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Human Resources': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Human Resources', y='Mean Revenue', title='Average Mean Human Resources')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            
        if selected_option == 'Real Estate and Property':
            
            variables =['Real Estate', 'Property Management', 'PropTech', 'Construction', 'Home Renovation', 'Parking', 'Real Estate Investment', 'Smart Building']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Real Estate and Property': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Real Estate and Property', y='Mean Revenue', title='Average Mean Real Estate and Property')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
            
        if selected_option == 'Food and Beverage':
            
            variables =['Food & Beverage (F&B)', 'Food Processing', 'Foodtech', 'Food Delivery', 'Coffee', 'Restaurants', 'Catering', 'Bakery', 'Alcohol', 'Hydroponics']

            categories = [
                'category_0', 'category_1', 'category_2', 'category_3',
                'category_4', 'category_5', 'category_6', 'category_7',
                'category_8' ]
           

            average_mean_revenues = []

            # Loop through each variable
            for variable in variables:
                # Select rows where the variable is present in any of the category columns
                variable_companies = data[data[categories].apply(lambda x: variable in x.values, axis=1)]

                # Calculate the average mean revenue for the variable
                average_mean_revenue = variable_companies['revenue_c'].mean()
                average_mean_revenues.append((variable, average_mean_revenue))


            # Extract the categories and average revenues for plotting
            variable_labels = [x[0] for x in average_mean_revenues]
            mean_revenues = [x[1] for x in average_mean_revenues]

            # Create a DataFrame for the data
            data1 = pd.DataFrame({'Food and Beverage': variable_labels, 'Mean Revenue': mean_revenues})

            fig = px.bar(data1, x='Food and Beveragey', y='Mean Revenue', title='Average Mean Food and Beverage')

            # Display the graph in Streamlit
            st.plotly_chart(fig)
                 
                 
   
        # Revenye vs Total Funding graph
        st.title('Revenue vs Total Funding')
        x_column = 'total_funding_c'
        y_column = 'revenue_c'

        filtered_data = data[(data[x_column].notnull()) & (data[x_column] != 0) & (data[y_column].notnull()) & (data[y_column] != 0)]

        x = filtered_data[x_column]
        y = filtered_data[y_column]

        filtered_data = data[(data[x_column].notnull()) & (data[x_column] != 0) & (data[x_column] != 1) & (data[y_column].notnull()) & (data[y_column] != 0) & (data[y_column] != 1)]

        sc = px.scatter(filtered_data, x=x_column, y=y_column)

        # Set the chart title and axis labels
        sc.update_layout(title='Total funding vs Total revenue', xaxis_title='Funding', yaxis_title='Revenue')

        # Display the chart using Streamlit
        st.plotly_chart(sc)

        fig = go.Figure(data=go.Scatter(x=data["incorporated_date_c"], y=data["revenue_c"], mode='markers'))
        # Add axis labels and title
        fig.update_layout(xaxis_title="Incorporation Date", yaxis_title="Total Revenue", title="Revenue over time")

        # Show plot
        st.plotly_chart(fig)
        
        # Employee Growth vs revenue growth graph
        button = st.button('Employee Growth (12 months)')
        
        # Create a container to hold the button and the plot
        container = st.container()

        fig = go.Figure(data=go.Scatter(x=data["revenue_growth(%)"], y=data["employee_growth_6(%)"], mode='markers'))
        # Add axis labels and title
        fig.update_layout(xaxis_title="Revenue_growth(%)", yaxis_title="Employee_growth_6(%)", title="Revenue Growth vs Employee Growth (6 months)")

        # Show plot
        st.plotly_chart(fig)

        # If button is clicked, filter data and show the filtered scatter plot
        if button:
            fig = go.Figure(data=go.Scatter(x=data["revenue_growth(%)"], y=data["employee_growth_12(%)"], mode='markers'))
            
            # Add axis labels and title
            fig.update_layout(xaxis_title="Revenue_growth(%)", yaxis_title="Employee_growth_12(%)", title="Revenue Growth vs Employee Growth (12 months)")

            # Show plot
            st.plotly_chart(fig)


        # Create a slider to select the year
        year_ranges = {
            "Before 1990": (None, 1989),
            "1990-1995": (1990, 1995),
            "1996-2000": (1996, 2000),
            "2001-2005": (2001, 2005),
            "2006-2010": (2006, 2010),
            "2011-2015": (2011, 2015),
            "2016-2020": (2016, 2020),
            "2021 until now": (2021, None)
        }

        # Get the selected year range from the option menu
        selected_range = st.selectbox("Select year range", list(year_ranges.keys()))

        # Get the minimum and maximum years based on the selected range
        min_year, max_year = year_ranges[selected_range]

        # Filter the data based on the selected year range
        data_filtered = data.copy()  # Create a copy of the original data

        if min_year is not None:
            data_filtered = data_filtered[data_filtered["incorporated_date_c"] >= min_year]
        if max_year is not None:
            data_filtered = data_filtered[data_filtered["incorporated_date_c"] <= max_year]

        # Create the plot using Plotly Express
        fig = px.scatter(data_filtered, x="incorporated_date_c", y="total_funding_c")

        # Set the title of the chart
        fig.update_layout(title=f'Incorporate Date vs Total Funding ({selected_range})')

        # Display the plot
        st.plotly_chart(fig)

#         scatter_plot = alt.Chart(data).mark_circle().encode(
#             x=alt.X('revenue_growth(%)', title='Revenue Growth Rate'),
#             y=alt.Y('last_valuation_c', title='Last Valuation'),
#             color=alt.Color('num_funding_rounds', title='Number of Funding Rounds')
#         )

#         # Create button to filter data
#         button_clicked = st.button('Filter data')

#         # Create a container to hold the button and the plot
#         container = st.container()

#         # If button is clicked, filter data and show the filtered scatter plot
#         if button_clicked:
#             data_filtered = data[data["num_funding_rounds"] > 5]
#             filtered_scatter_plot = alt.Chart(data_filtered).mark_circle().encode(
#                 x=alt.X('revenue_growth(%)', title='Revenue Growth Rate'),
#                 y=alt.Y('last_valuation_c', title='Last Valuation'),
#                 color=alt.Color('num_funding_rounds', title='Number of Funding Rounds')
#             )
#             container.altair_chart(filtered_scatter_plot, use_container_width=True)

#         # Show the initial scatter plot
#         container.altair_chart(scatter_plot, use_container_width=True)

        # Create a function to filter the data based on the selected range of total funding

        
        columns = ["employee_growth_6(%)", "revenue_growth(%)"]

        # Create the plot using Plotly Express
        fig = px.scatter(data, x="employee_growth_6(%)", y="revenue_growth(%)", hover_name="name_c")

        # Set the title of the chart
        fig.update_layout(title="Employee Growth vs Revenue Growth")

        # Display the plot
        st.plotly_chart(fig)

        def filter_data(min_value, max_value):
            filtered_data = data[(data["total_funding_c"] >= min_value) & (data["total_funding_c"] <= max_value)]
            return filtered_data

        def generate_bar_chart(data):
            chart = alt.Chart(data).mark_bar().encode(
                x="total_funding_c",
                y="revenue_growth(%)",
                tooltip=["total_funding_c", "revenue_growth(%)"]
            ).properties(
                title="Employee Growth and Revenue Growth",
                width=600,
                height=400
            )
            return chart

        # Sidebar sliders for filtering total funding
        total_fund_min = st.slider("Minimum Total Funding", 0, 600000000, 0, 1000000)
        total_fund_max = st.slider("Maximum Total Funding", 0, 600000000, 600000000, 1000000)

        # Button to generate the bar chart
        if st.button("Generate Bar Chart"):
            filtered_data = filter_data(total_fund_min, total_fund_max)
            bar_chart = generate_bar_chart(filtered_data)
            st.altair_chart(bar_chart, use_container_width=True)
            
               
                   

            # Filter the data based on the selected range of total funding
          

            # Create a button to generate the bar chart
                 



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

# #         # Create Streamlit app
# #         st.title('Revenue Growth by Company Category')
# #         st.write('Select a category from the dropdown menu to filter the data.')

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

    if(selected == 'Search'):
        
        st.title('Search')

        # Create a radio button for selecting the search method
        search_method = st.radio('Select Search Method', ('Search by Company', 'Search by Category'))

        if search_method == 'Search by Company':
            # Display content for searching by company
            st.header('Search by Company')
            # Your code for searching by company goes here

        elif search_method == 'Search by Category':
            # Display content for searching by category
            st.header('Search by Category')
            # get unique values from grp_category columns
            grp_categories = data.filter(regex='grp_category').values.ravel()
            grp_categories = pd.unique([x for x in grp_categories if str(x) != 'nan'])

            # Main category dropdown
            main_categories = ['Technology', 'Finance', 'Health and Wellness', 'Retail and E-commerce', 'Education',
                               'Media and Entertainment', 'Travel and Hospitality', 'Marketing and Advertising',
                               'Human Resources', 'Real Estate and Property', 'Food and Beverage',
                               'Other']  # replace with your own categories
            selected_main_category = st.selectbox('Select main category', main_categories)

            # Detailed category dropdown
            if selected_main_category == 'Technology':
                detailed_categories = ['Information Technology', 'Software', 'Mobile Apps', 'Internet',
                                       'Artificial Intelligence (AI)', 'Internet of Things (IoT)', 'Web Development',
                                       'Cloud', 'Automation', 'Big Data', 'Machine Learning', 'Robotics', 'Blockchain',
                                       'Augmented Reality', 'Virtual Reality', 'Smart Home', 'Clean Energy', 'Sensor',
                                       'Nanotechnology', 'Developer Apis']
                detailed_categories.append('All')
            elif selected_main_category == 'Finance':
                detailed_categories = ['Financial Services', 'Fintech', 'Payments', 'Insurance', 'Investment',
                                       'Accounting', 'Lending', 'Personal Finance', 'Cryptocurrency', 'Invoice Trading',
                                       'Wealth Management', 'Transaction Processing',
                                       'Micro Lending']  # replace with your own categories
                detailed_categories.append('All')
            elif selected_main_category == 'Health and Wellness':
                detailed_categories = ['Health Care', 'Healthtech', 'Medical Device', 'Fitness', 'Medical',
                                       'Biotechnology', 'Nutrition', 'Dental', 'Pharmaceutical', 'Personal Health',
                                       'Home Health Care', 'Medtech', 'Elder Care']  # replace with your own categories
                detailed_categories.append('All')
            elif selected_main_category == 'Retail and E-commerce':
                detailed_categories = ['E-Commerce', 'Marketplace', 'Retail', 'Fashion', 'Grocery', 'Shopping',
                                       'Cosmetics', 'Gift', 'Catering', 'Wholesale', 'Subscription Service', 'Bakery',
                                       'Alcohol', 'Mattress']
                detailed_categories.append('All')
            elif selected_main_category == 'Education':
                detailed_categories = ['Education', 'E-Learning', 'EdTech', 'Training', 'Higher Education',
                                       'Secondary Education', 'Tutoring']
                detailed_categories.append('All')
            elif selected_main_category == 'Media and Entertainment':
                detailed_categories = ['Media & Entertainment', 'Music', 'TV', 'Broadcasting', 'Photography',
                                       'Film Production', 'Content Creators']
                detailed_categories.append('All')
            elif selected_main_category == 'Travel and Hospitality':
                detailed_categories = ['Travel', 'Tourism', 'Hospitality', 'Adventure Travel', 'Resorts', 'Co-Living',
                                       'Fast-moving Consumer Goods (FMCG)', 'Tea', 'Air Transportation', 'Maritime']
                detailed_categories.append('All')
            elif selected_main_category == 'Marketing and Advertising':
                detailed_categories = ['Marketing', 'Digital Marketing', 'Advertising', 'Content Marketing', 'Loyalty',
                                       'Loyalty Programs', 'Payroll', 'Email Marketing', 'Influencers',
                                       'Affiliate Marketing']
                detailed_categories.append('All')
            elif selected_main_category == 'Human Resources':
                detailed_categories = ['Human Resources', 'Recruitment', 'Staffing Agency', 'Employment',
                                       'Employee Benefits', 'Entrepreneur First', 'Professional Networking']
                detailed_categories.append('All')
            elif selected_main_category == 'Real Estate and Property':
                detailed_categories = ['Real Estate', 'Property Management', 'PropTech', 'Construction',
                                       'Home Renovation', 'Parking', 'Real Estate Investment', 'Smart Building']
                detailed_categories.append('All')
            elif selected_main_category == 'Food and Beverage':
                detailed_categories = ['Food & Beverage (F&B)', 'Food Processing', 'Foodtech', 'Food Delivery',
                                       'Coffee', 'Restaurants', 'Catering', 'Bakery', 'Alcohol', 'Hydroponics']
                detailed_categories.append('All')
            else:
                detailed_categories = ['Internet of Things (IoT)', 'Apps', 'Consulting', 'Agriculture', 'Saas',
                                       'Online Portals', 'Logistics', 'Manufacturing', 'Human Resources (HR)',
                                       'Enterprise Software', 'Automotive', 'Engineering', 'AgriTech', 'Mobile',
                                       'Wellness', 'Delivery', 'Technology', 'Gaming', 'Consumer Goods',
                                       'Transportation', 'Web Design', 'Social Media', 'Rental', 'Data Analytics',
                                       'Beauty', 'Digital', 'Lifestyle',
                                       'Information & Communications Technology (ICT)', 'Sustainability', 'Finance',
                                       'B2B', 'Analytics', 'Drones', 'Information Services', 'Events', 'Web Apps',
                                       'Supply Chain', 'Farming', 'Computer', 'Telecommunications', 'News',
                                       'Waste Management', 'Social Enterprise', 'IT Solutions Provider', 'Security',
                                       'Renewable Energy', 'Enterprise Solutions', 'Mobile Payments', 'Co-Working',
                                       'Hardware', 'Sports', 'Event Management', 'Digital Transformation', 'Energy',
                                       'Children', 'Health', 'Design', 'Cyber Security', 'Environment', 'Search Engine',
                                       'Business Intelligence', 'Point of Sale (POS)', 'Recycling', 'Crowdfunding',
                                       'Solar', 'Women', 'Communities', 'Virtual Reality (VR)', 'Organic',
                                       'Home Services', 'Industrial Automation', 'Digital Media', 'Oil & Gas',
                                       'Chemicals', 'Research', 'Delivery Service', 'Professional Services',
                                       'Consumer Electronics', 'Ride Sharing', 'Market Research', 'Shipping',
                                       'Insurtech', 'Data', 'Pharmaceutical', 'Interior Design', 'Lighting', 'Platform',
                                       'Enterprise Resource Planning (Erp)', 'Freight Services',
                                       'Small & Medium-sized Enterprises (SMEs)', 'Augmented Reality (Ar)', 'Cleaners',
                                       'Digital Wallet', 'Mobile Games', 'Printing', 'Hotel', 'Building Materials',
                                       'Skincare', '3D Technology', 'Cleaning Services', 'Automobile',
                                       'Customer Service', 'Car Sharing', 'Courier Service', 'Graphic Design',
                                       'Publishing', 'Electric Vehicle (Ev)', 'Property', 'Outsourcing',
                                       'Sustainable Farming', 'Crm', 'Product Design', 'Procurement', '3D Printing',
                                       'Aerospace', 'Wedding', 'Machinery', 'Maintenance', 'Video Streaming',
                                       'Ticketing', 'Trading', 'Ios', 'Enterprise Applications', 'Water', 'Video',
                                       'Home Decor', 'Social Media Marketing', 'Wireless', 'UX Design', 'Shoes',
                                       'Video Games', 'Electrical Distribution', 'Textiles', 'Cloud Solutions',
                                       'Car Rental', 'Predictive Analytics', 'Business Development', 'Hospital',
                                       'E-Books', 'Crowdsourcing', 'Management Consulting', 'Banking',
                                       'Location Based Services', 'Greentech', 'E-Commerce Platforms',
                                       'Document Management', 'Repair', 'Sales', 'Mobile Advertising',
                                       'Cloud Computing', 'Facial Recognition', 'Contractors', 'Aquaculture',
                                       'Environmental Consulting', 'Packaging Services', 'Rewards', 'Electronics',
                                       'Legal Tech', 'Travel Agency', 'Psychology', 'Fleet Management', 'Consumer',
                                       'Service Industry', 'Gamification', 'Social Network', 'Database', 'Enterprise',
                                       'Books', 'Wine & Spirits', 'Facility Management', 'Semiconductors',
                                       'Data Science', 'Distribution', 'Legal', 'Leisure', 'Management Systems',
                                       'Cleantech', 'Safety', 'Recreation', 'Energy Efficiency', 'Oil & Energy',
                                       'Battery', 'Developer Platform', 'Android', 'Cloud Data Services', 'Messaging',
                                       'Animal Feed', 'Venture Capital', 'Digital Signage', 'Materials',
                                       'Medical Research', 'Furniture', 'Social News', 'Price Comparison', 'Coupons',
                                       'Aviation', 'Consumer Research', 'B2C', 'App Development', 'Public Relations',
                                       'Online Games', 'Developer Tools', 'Simulation', 'Flowers', 'Mobility',
                                       'Equipment', 'Pet', 'Vending Machine', 'Deep Learning', 'Jewellery',
                                       'Asset Management', 'Wearables', 'Leasing', 'Incubators', 'Toys',
                                       'Data Visualization', 'Gps', 'Water Treatment', 'Private Social Networking',
                                       'Document Preparation', 'Bitcoin', 'Chatbot', 'Collaboration', 'E-Scooter',
                                       'Warehouse', 'VoIP', 'Cloud Security', 'Social', 'Enviromental', 'Green',
                                       'Customer Success', 'Universities', 'Biomedical', 'Risk Management',
                                       'Network Security', 'Data Integration', 'Web', 'Programming',
                                       'Communications Infrastructure', 'Accommodation', 'Mobile Health (mHealth)',
                                       'Esports', 'Microfinance', 'Tours', 'Sales Automation', 'Marine Transportation',
                                       'Data Mining', 'Content', 'Auto Insurance', 'Real Time', 'Fundraising', 'Bus',
                                       'Dating', 'Ethereum', 'Web Hosting', 'Trading Platform', 'Mapping Services',
                                       'Data Management', 'Online', 'Renewable', 'Autonomous Vehicles', 'Cloud Kitchen',
                                       'Workflow Digitalization Service', 'Architecture', 'Freelance',
                                       'Digital Banking', 'App Marketing', 'Import', 'Football', 'Seo', 'Timber',
                                       'Paper', 'Recruiment', 'Cards', 'Task Management', 'Air Conditioner',
                                       'Association', 'Communications', 'Gift Card', 'Markeplace', 'Tracking',
                                       'Qr Codes', 'Business', 'Animal', 'Test & Measurement', 'Mobile Advetising',
                                       'Software Engineering', 'Diamonds', 'Productivity Tools',
                                       'Last Mile Transportation', 'Web Developer', 'Leather',
                                       'Human Computer Interaction', 'Game', 'Social Commerce',
                                       'Food and Beverage (F&B)', 'Translation', 'Elderly', 'Coding',
                                       'Natural Language Processing', 'Luxury Goods', 'Financial Exchanges',
                                       'Diagnostics', 'Satellite Communication', 'Audio', 'Peer-to-Peer (P2P)',
                                       'Genetics', 'Consumer Software', 'Api', 'Plastic', 'Medicine', 'Film',
                                       'Intellectual Property', 'Industrial Manufacturing', 'Mobile Devices',
                                       'Smart Cities', 'Mechanical Engineering', 'Skills Assessment', 'Wallet',
                                       'Retail Technology', 'Local Advertising', 'Social Entrepreneurship', 'Unbanked',
                                       'Service Providers', 'Government', 'Parenting', 'Debt Collections', 'Carrier',
                                       'Image Recognition', 'Computer Vision', 'Identity Management',
                                       'Project Management', 'It Infrastructure', 'Exchange', 'Marketing Automation',
                                       'Cooking', 'Infrastructure', 'Bicycles', 'E-Procurement', 'Home Electronics',
                                       'Ad Network', 'Brand Marketing', 'Travel Accommodations', 'Lidar', 'Satellite',
                                       'Property Development', 'Social Media Management', 'Email', 'IT Management',
                                       'Sharing Economy', 'Genomics', 'Clinical Trials', 'Integrated Circuits',
                                       'Therapeutics', 'Business Information Systems', 'Power Generation',
                                       'Social Media Advertising', 'Commercial Lending', 'Funding Platform',
                                       'Bioresearch', 'Gardening', 'Poultry', 'Industrial Engineering', 'Social Impact',
                                       'Sms', 'Same Day Delivery', 'Fishing', 'Cms', 'Electric', 'Corporate Training',
                                       'Food Alternatives', 'Vacation Rental']
                detailed_categories.append('All')
            selected_detailed_category = st.selectbox('Select detailed category', detailed_categories)

            # Filter data based on selected categories
            if selected_detailed_category == 'All':
                filtered_df = data[data['grp_category_0'].eq(selected_main_category) |
                                   data['grp_category_1'].eq(selected_main_category) |
                                   data['grp_category_2'].eq(selected_main_category) |
                                   data['grp_category_3'].eq(selected_main_category) |
                                   data['grp_category_4'].eq(selected_main_category) |
                                   data['grp_category_5'].eq(selected_main_category) |
                                   data['grp_category_6'].eq(selected_main_category) |
                                   data['grp_category_7'].eq(selected_main_category) |
                                   data['grp_category_8'].eq(selected_main_category)]
            else:
                filtered_df = data[
                    (
                            (data['grp_category_0'] == selected_main_category) |
                            (data['grp_category_1'] == selected_main_category) |
                            (data['grp_category_2'] == selected_main_category) |
                            (data['grp_category_3'] == selected_main_category) |
                            (data['grp_category_4'] == selected_main_category) |
                            (data['grp_category_5'] == selected_main_category) |
                            (data['grp_category_6'] == selected_main_category) |
                            (data['grp_category_7'] == selected_main_category) |
                            (data['grp_category_8'] == selected_main_category)
                    ) & (
                            (data['category_0'] == selected_detailed_category) |
                            (data['category_1'] == selected_detailed_category) |
                            (data['category_2'] == selected_detailed_category) |
                            (data['category_3'] == selected_detailed_category) |
                            (data['category_4'] == selected_detailed_category) |
                            (data['category_5'] == selected_detailed_category) |
                            (data['category_6'] == selected_detailed_category) |
                            (data['category_7'] == selected_detailed_category) |
                            (data['category_8'] == selected_detailed_category)
                    )]

            # Display filtered data
            # Drop columns 'grp_ctgry_0' to 'grp_ctgry_8'
            data_filtered = filtered_df.drop(
                columns=['grp_category_0', 'grp_category_1', 'grp_category_2', 'grp_category_3', 'grp_category_4',
                         'grp_category_5',
                         'grp_category_6', 'grp_category_7', 'grp_category_8'])
            # Create a dictionary to map column names to formal names
            formal_names = {
                'name_c': 'Company Name',
                'incorporated_date_c': 'Incorporated Date',
                'total_funding_c': 'Total Funding',
                'last_valuation_c': 'Last Valuation',
                'last_round_size_c': 'Last Round Size',
                'revenue_c': 'Latest Year Revenue',
                'date_of_last_round': 'Date of Last Round',
                'fy_end': 'Date of Financial Year End',
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
                'category_0': 'Category 1',
                'category_1': 'Category 2',
                'category_2': 'Category 3',
                'category_3': 'Category 4',
                'category_4': 'Category 5',
                'category_5': 'Category 6',
                'category_6': 'Category 7',
                'category_7': 'Category 8',
                'category_8': 'Category 9'
            }

            # Rename the columns using the formal names
            data_filtered.rename(columns=formal_names, inplace=True)

            # Display the filtered data with formal column names
            st.write(data_filtered)


    if(selected == 'Company Profile'):

        input = st.selectbox(label='Name of company', options=data['name_c'])
        count = 0
        for value in data['name_c']:
            if input == value:
                row = data.iloc[count]
                st.write("Incorporated date: ", row[1])
                st.write("Last valuation: ", row[3])
                st.write("Amount raised during last funding round: ", row[4])
                st.write("Date of last fund raise: ", row[6])
                st.write("Date of financial year end: ", row[7])
                st.write("Number of founder: ", row[12])
                st.write("Number of funding round: ", row[13])
                st.write("Number of shareholder: ", row[14])
                st.write("Minimum share in %: ", row[15])
                st.write("Median share in %: ", row[16])
                st.write("Maximum share in %: ", row[17])
                st.write("Categories: ", row[18])
                # Sample data
                
                x_data1 = ['Total Funding', 'Revenue', 'Ebit']  # X-axis names
                # Use y-axis values as x-axis values
                y_data1 = [row[2], row[5], row[9]] 

                # Create bar trace for y-variable
                trace1 = go.Bar(x=x_data1, y=y_data1,width=0.5)

                # Create layout
                layout1 = go.Layout(
                    title='"Total Funding","Revenue","EBIT',
                    xaxis=dict(title='Features'),
                    yaxis=dict(title='Amount')
                )
                
                fig1 = go.Figure(data=[trace1], layout=layout1)

                # Display the figure
                st.plotly_chart(fig1)
               
                x_data2 = ['Revenue Growth', 'Employee Growth(6m)', 'Employee Growth (12m)']  # X-axis names
                # Use y-axis values as x-axis values
                y_data2 = [row[8], row[10], row[11]] 

                # Create bar trace for y-variable
                trace2 = go.Bar(x=x_data2, y=y_data2,width=0.5)

                # Create layout
                layout2 = go.Layout(
                    title='"Revenue Growth","Employee Growth(6m)","Employee Growth (12m)',
                    xaxis=dict(title='Features'),
                    yaxis=dict(title='Amount')
                )
                
                fig2 = go.Figure(data=[trace2], layout=layout2)

                # Display the figure
                st.plotly_chart(fig2)
            count = count+1


run_website()

