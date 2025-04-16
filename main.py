import pandas as pd
import plotly.express as px
from datetime import time

if __name__ == '__main__':

    # Load the data
    data = pd.read_csv('data\data.csv', delimiter=";", decimal=",")

    data.Datum = pd.to_datetime(data.Datum)
    data['Dauer in HH:MM:SS'] = pd.to_datetime(data['Dauer in HH:MM:SS'], format='%H:%M:%S')#.dt.time


    print(data.head())
    print(data.dtypes)

    # Create an interactive plot
    fig1 = px.line(data, x='Datum', y='Entfernung in km',  markers=True)
    fig2 = px.line(data, x='Datum', y='Dauer in HH:MM:SS', markers=True )
    fig2.update_layout(yaxis_tickformat = '%H:%M:%S')
    fig3 = px.line(data, x='Datum', y='Geschwindigkeit km/h', markers=True)

    fig1.show()
    fig2.show()
    fig3.show()

    # Save the plot as an HTML file
    fig1.write_html('plot1.html')
    fig2.write_html('plot2.html')
    fig3.write_html('plot3.html')


    html = data.to_html()

    # write html to file
    text_file = open("table.html", "w")
    text_file.write(html)
    text_file.close()
