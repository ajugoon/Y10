# This pulls data from on online repository called gapminder
# This data has already been accumulated for us

import pandas as pd
import plotly.express as px

df = pd.read_csv('Enter your Github User Data Address here...')
df.head()

fig = px.line(df, x = "Year", y = "CO2", title='Some Example')
fig.show()
