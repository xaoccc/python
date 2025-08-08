import plotly.express as px
from country_list import  available_languages, countries_for_language
country_codes = [code for code in available_languages() if code=='en']
country_lst = []
# Get countries names
for country in countries_for_language(country_codes[0]):
    country_lst.append(country[1])

country = input('Select country:')
# Validate Country name
while country not in country_lst:
    print('Invalid value. Try again')
    country = input('Select country:')

value = input('Choose value:')
# Validate value
while not value.isdigit():
    print('Invalid value. Try again')
    value = input('Choose value:')


data = {'Country': [country], 'Values': [int(value)]}
fig = px.choropleth(data, locations='Country', locationmode='country names', color='Values')
fig.show()
