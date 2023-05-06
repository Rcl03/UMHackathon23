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
                            'Search',
                            'Company Profile'],
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

        fig = go.Figure(data=go.Scatter(x=data["incorporated_date_c"], y=data["revenue_c"], mode='markers'))
        # Add axis labels and title
        fig.update_layout(xaxis_title="Incorporation Date", yaxis_title="Total Revenue", title="Revenue over time")

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

    if(selected == 'Search'):

# get unique values from grp_category columns
        grp_categories = data.filter(regex='grp_category').values.ravel()
        grp_categories = pd.unique([x for x in grp_categories if str(x) != 'nan'])

        # Main category dropdown
        main_categories = ['Technology', 'Finance', 'Health and Wellness', 'Retail and E-commerce', 'Education', 'Media and Entertainment', 'Travel and Hospitality', 'Marketing and Advertising', 'Human Resources', 'Real Estate and Property', 'Food and Beverage', 'Other']  # replace with your own categories
        selected_main_category = st.selectbox('Select main category', main_categories)

        # Detailed category dropdown
        if selected_main_category == 'Technology':
            detailed_categories = ['Information Technology', 'Software', 'Mobile Apps', 'Internet', 'Artificial Intelligence', 'Internet of Things', 'Web Development', 'Cloud', 'Automation', 'Big Data', 'Machine Learning', 'Robotics', 'Blockchain', 'Augmented Reality', 'Virtual Reality', 'Smart Home', 'Clean Energy', 'Sensor', 'Nanotechnology', 'Developer Apis']  # replace with your own categories
            detailed_categories.append('All')
        elif selected_main_category == 'Finance':
            detailed_categories = ['Financial Services', 'Fintech', 'Payments', 'Insurance', 'Investment', 'Accounting', 'Lending', 'Personal Finance', 'Cryptocurrency', 'Invoice Trading', 'Wealth Management', 'Transaction Processing', 'Micro Lending']  # replace with your own categories
            detailed_categories.append('All')
        elif selected_main_category == 'Health and Wellness':
            detailed_categories = ['Health Care', 'Healthtech', 'Medical Device', 'Fitness', 'Medical', 'Biotechnology', 'Nutrition', 'Dental', 'Pharmaceuticals', 'Personal Health', 'Home Health Care', 'Medtech', 'Elder Care']  # replace with your own categories
            detailed_categories.append('All')
        elif selected_main_category == 'Retail and E-commerce':
            detailed_categories = ['E-Commerce', 'Marketplace', 'Retail', 'Fashion', 'Grocery', 'Shopping', 'Cosmetics', 'Gift', 'Catering', 'Wholesale', 'Subscription Service', 'Bakery', 'Alcohol', 'Mattress']
            detailed_categories.append('All')
        elif selected_main_category == 'Education':
            detailed_categories = ['Education', 'E-Learning', 'EdTech', 'Training', 'Higher Education', 'Secondary Education', 'Tutoring']
            detailed_categories.append('All')
        elif selected_main_category == 'Media and Entertainment':
            detailed_categories = ['Media & Entertainment', 'Music', 'TV', 'Broadcasting', 'Photography', 'Film Production', 'Content Creators']
            detailed_categories.append('All')
        elif selected_main_category == 'Travel and Hospitality':
            detailed_categories = ['Travel', 'Tourism', 'Hospitality', 'Adventure Travel', 'Resorts', 'Co-Living', 'Fast-moving Consumer Goods (FMCG)', 'Tea', 'Air Transportation', 'Maritime']
            detailed_categories.append('All')
        elif selected_main_category == 'Marketing and Advertising':
            detailed_categories = ['Marketing', 'Digital Marketing', 'Advertising', 'Content Marketing', 'Loyalty', 'Loyalty Programs', 'Payroll', 'Email Marketing', 'Influencers', 'Affiliate Marketing']
            detailed_categories.append('All')
        elif selected_main_category == 'Human Resources':
            detailed_categories = ['Human Resources', 'Recruitment', 'Staffing Agency', 'Employment', 'Employee Benefits', 'Entrepreneur First', 'Professional Networking']
            detailed_categories.append('All')
        elif selected_main_category == 'Real Estate and Property':
            detailed_categories = ['Real Estate', 'Property Management', 'PropTech', 'Construction', 'Home Renovation', 'Parking', 'Real Estate Investment', 'Smart Building']
            detailed_categories.append('All')
        elif selected_main_category == 'Food and Beverage':
            detailed_categories = ['Food & Beverage (F&B)', 'Food Processing', 'Foodtech', 'Food Delivery', 'Coffee', 'Restaurants', 'Catering', 'Bakery', 'Alcohol', 'Hydroponics']
            detailed_categories.append('All')
        else:
            detailed_categories = ['Other']
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
                (data['grp_category_0'] == selected_main_category) & (
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
            columns=['grp_category_0', 'grp_category_1', 'grp_category_2', 'grp_category_3', 'grp_category_4', 'grp_category_5',
                     'grp_category_6', 'grp_category_7', 'grp_category_8'])
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
                st.write("Categories: {}, {}, {}, {}, {}, {}, {}, {}".format(row[18], row[19], row[20], row[21], row[23], row[24], row[25], row[26]))
                # Sample data
                
                x_data1 = ['Total Funding', 'Revenue', 'Ebit']  # Y-axis names
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
               
                x_data2 = ['Revenue Growth', 'Employee Growth(6m)', 'Employee Growth (12m)']  # Y-axis names
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
