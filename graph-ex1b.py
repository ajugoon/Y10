# This pulls data from on online repository called gapminder
# This data has already been accumulated for us

import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/ajugoon/y10coding/master/testdata.csv')
df.head()

fig = px.line(df, x = "Year", y = "CO2", title='Some Example')
fig.show()
