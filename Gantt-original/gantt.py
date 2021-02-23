#from:  https://community.plotly.com/t/how-do-i-change-the-x-axis-representation-of-time-on-the-px-timeline/44834/3
import pandas as pd
import plotly.express as px

df = pd.read_csv("graph_data.csv")
df["start_timestamp"] = pd.to_datetime(df["start_timestamp"])
df["start_timestamp"] = df["start_timestamp"].apply(lambda x: x.replace(year=1970, month=1, day=1))
df["end_timestamp"] = pd.to_datetime(df["end_timestamp"])
df["end_timestamp"] = df["end_timestamp"].apply(lambda x: x.replace(year=1970, month=1, day=1))

df["occurrence_date"] = pd.to_datetime(df["occurrence_date"]).dt.weekday


fig = px.timeline(df, x_start="start_timestamp", x_end="end_timestamp", y="occurrence_date",color="occurrence_type")
fig.update_xaxes(
    tickformat="%H\n%M",
    tickformatstops=[
        dict(dtickrange=[3600000, 86400000], value="%H:%M")]  # range is 1 hour to 24 hours
)
fig.show()