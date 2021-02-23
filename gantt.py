import plotly.express as px
import plotly
import pandas as pd

#read csv
df = pd.read_excel('tasks.xlsx')

print(df)



import pandas as pd
import plotly.express as px

df = pd.read_csv("robots_gantt_data.csv")
df["start_timestamp"] = pd.to_datetime(df["start_timestamp"])
df["start_timestamp"] = df["start_timestamp"].apply(lambda x: x.replace(year=2021, month=2, day=23))
df["end_timestamp"] = pd.to_datetime(df["end_timestamp"])
df["end_timestamp"] = df["end_timestamp"].apply(lambda x: x.replace(year=2021, month=2, day=23))

df["robot"] = df["robot"]


fig = px.timeline(df, x_start="start_timestamp", x_end="end_timestamp", y="robot",color="occurrence_type")
fig.update_xaxes(
    tickformat="%H\n%M",
    tickformatstops=[
        dict(dtickrange=[3600000, 86400000], value="%H:%M")]  # range is 1 hour to 24 hours
)
fig.show()
plotly.offline.plot(fig,filename='Task_Overview_Gantt.html')