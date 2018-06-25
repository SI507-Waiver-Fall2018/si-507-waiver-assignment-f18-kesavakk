# Imports -- you may add others but do not need to
import plotly
import csv
plotly.tools.set_credentials_file(username='kesava.k3', api_key='yHh05VCzbAdr20JPvm69')


# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets
nouns=[]
count=[]
f = open("noun_data.csv", "r")

reader = csv.reader(f)
i = 0
for line in reader:
    if i > 0:
        nouns.append(line[0])
        count.append(line[1])
    i+=1

trace = plotly.graph_objs.Bar(x=nouns, y=count,
    marker=dict(
        color=['rgba(204,204,204,1)', 'rgba(222,45,38,0.8)',
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)']), width = [0.8, 0.55, 0.5, 0.25, 0.1])
data = [trace]
layout = plotly.graph_objs.Layout(title='Nouns data', width=800, height=640)
fig = plotly.graph_objs.Figure(data=data, layout=layout)

plotly.plotly.image.save_as(fig, filename='part4_viz_image.png')
