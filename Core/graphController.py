# ---------- LIBRARIES ---------- #
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from colorama import *
import numpy as np
# ---------- MAIN ----------- #
class LineGraph():
    def __init__(self):
        self.dimensions = []

    def initialize(self, rows = 1, cols = 1):
        self.fig = make_subplots(rows = rows, cols = cols)

    def dimensionCheck(self):
        for i in range(len(self.dimensions)):
            if self.dimensions.count(self.dimensions[i]) > 1:
                print(f"{Fore.RED}[-]{Style.RESET_ALL}GRAPH CONTROLLER: Error Occurred Laying Graphs in Grid Pattern")
                print(f"    {Fore.YELLOW}Try Checking Row and Column Parameters")
                quit()
            
    def graphLine(self, xAxis, yAxis, graphName, row, col, colors = []):
        """
        Function that uses data imported to plot onto the graph

        xAxis --> The X Values [REQUIRED]
        yAxis --> The Y Values [REQUIRED]
        graphName --> The Name of the Graph being appended
        row --> The Row Number [REQUIRED]
        col --> The Column Number [REQUIRED]
        colors --> All colors are either auto assigned or there are no colors
        """
        self.dimensions.append(int(f"{row}{col}"))
        try:
            self.fig.append_trace(
                go.Scatter(
                    x = xAxis,
                    y = yAxis,
                    line = dict(color = 'black', width = 1),
                    name = graphName if graphName else 'None'
                ), row = row, col = col  # <------------ upper chart
            )
        except Exception:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} GRAPH CONTROLLER: Row and Column Values Invalid")
            print(f"    {Fore.YELLOW}Try Checking Row and Column Parameters")
            quit()

    def barGraph(self, xAxis, yAxis, graphName, row, col, colors = [], transparency = []):
        pass

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
