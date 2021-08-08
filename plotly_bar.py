import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# target directory
os.chdir(r"C:\Users\chris\Desktop")

df = pd.read_excel('alcohol.xlsx')         
         
df = df.sort_values(by=['alcohol'], ascending = True)


# create plot and save
colors = ['#F0F0F0',] * len(df['location'])
colors[5] = 'lightblue'


fig = go.Figure(go.Bar(
            x=df['alcohol'],
            y=df['location'],
            marker_color=colors,
            orientation='h',
))


fig.update_layout(
    title="Lithuania has relitevly high alcohol consumption levels when copaired to other contries",
    xaxis_title="Alcohol consumption",
    yaxis_title="Countries",
    legend_title="Legend Title",
    annotations=[
            go.layout.Annotation(
                text='<b>Due to some reason, Lithuania<br>has these levels of alcohol<br>consumption<b>',
                align='left',
                font=dict(
                    family="Arial",
                    size=10,
                    color="black"),

                xref='paper',
                yref='paper',
                x=1.018,
                y=0.65,
                bordercolor='lightgrey',
                borderwidth=0.5)],
    plot_bgcolor='rgb(0, 0, 0, 0)',
    paper_bgcolor='rgb(0, 0, 0, 0)',
    font=dict(
        family="Arial",
        size=10,
        color="grey"
    )
                
)




fig.show()
