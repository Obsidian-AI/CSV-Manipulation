# ---------- LIBRARIES ---------- #
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from colorama import *
import numpy as np
# ---------- MAIN ----------- #
class GraphController():
    def __init__(self):
        self.dimensions = []

    def initialize(self, rows = 1, cols = 1):
        self.fig = make_subplots(rows = rows, cols = cols, subplot_titles = ("Plot 1", "Plot 2"))

    def dimensionCheck(self):
        """
        Function used to check whether rows and columns are open or else warn the user
        """
        for i in range(len(self.dimensions)):
            if self.dimensions.count(self.dimensions[i]) > 1:
                print(f"{Fore.RED}[-]{Style.RESET_ALL}GRAPH CONTROLLER: Error Occurred Laying Graphs in Grid Pattern")
                print(f"    {Fore.YELLOW}Try Checking Row and Column Parameters{Style.RESET_ALL}")
                quit()
            
    def graphOneLine(self, xAxis, yAxis, graphName, row, col, colors = []):
        """
        Function that uses data imported to plot onto the graph

        xAxis --> The X Values [REQUIRED]
        yAxis --> The Y Values [REQUIRED]
        graphName --> The Name of the Graph being appended
        row --> The Row Number [REQUIRED]
        col --> The Column Number [REQUIRED]
        colors --> All colors are either auto assigned or there are no colors [NOT ACTIVE]
        """
        self.dimensions.append(int(f"{row}{col}"))
        try:
            self.fig.append_trace(
                go.Scatter(
                    x = xAxis,
                    y = yAxis,
                    line = dict(color = 'black', width = 1),
                    name = graphName if graphName else 'No Label',
                ), row = row, col = col  # <------------ upper chart
            )
        except Exception:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} GRAPH CONTROLLER: Row and Column Values Invalid")
            print(f"    {Fore.YELLOW}Try Checking Row and Column Parameters{Style.RESET_ALL}")
            quit()

    def graphMultipleLines(self, xAxis, yAxis, graphName, row, col, colors = []):
        """
        Function that uses the data provided to graph multiple lines on one chart

        xAxis --> The X Values [REQUIRED]
        yAxis --> The Y Values [REQUIRED]
        graphName --> The Name of the Graph
        row --> The Row Number [REQUIRED]
        col --> The Column Number [REQUIRED]
        colors --> All colors are either auto assigned or can be manually assigned [NOT ACTIVE]
        """
        self.dimensions.append(int(f"{row}{col}"))

    def show(self):
        self.dimensionCheck()
        self.fig.update_layout(
            go.Layout(
                plot_bgcolor = '#efefef',
                font_family = 'Monospace',
                font_color =  '#000000',
                font_size = 20,
                xaxis = dict(
                    rangeslider = dict(
                        visible = False
                    )
                )
            )
        )
        self.fig.show()
