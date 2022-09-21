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
        self.fig = make_subplots(rows = rows, cols = cols, shared_xaxes = False, shared_yaxes = False)

    def dimensionCheck(self):
        """
        Function used to check whether rows and columns are open or else warn the user
        """
        for i in range(len(self.dimensions)):
            if self.dimensions.count(self.dimensions[i]) > 1:
                print(f"{Fore.RED}[-]{Style.RESET_ALL}GRAPH CONTROLLER: Error Occurred Laying Graphs in Grid Pattern")
                print(f"    {Fore.YELLOW}Try Checking Row and Column Parameters{Style.RESET_ALL}")
                quit()
            
    def graphOneLine(self, xAxis, yAxis, lineName, row, col, xLabel = "", yLabel = "", color = ""):
        """
        Function that uses data imported to plot onto the graph

        xAxis --> The X Values [REQUIRED]
        yAxis --> The Y Values [REQUIRED]
        graphName --> The Name of the Graph being appended
        row --> The Row Number [REQUIRED]
        col --> The Column Number [REQUIRED]
        colors --> All colors are either auto assigned or there are no colors [NOT ACTIVE]
        xLabel --> Label the X Axis of the subplot
        yLabel --> Label the Y Axis of the subplot
        """
        
        self.dimensions.append(int(f"{row}{col}"))
        try:
            self.fig.append_trace(
                go.Scatter(
                    x = xAxis,
                    y = yAxis,
                    line = dict(color = color if color != "" else 'black', width = 1),
                    name = lineName if lineName else 'No Label',
                ), row = row, col = col  # <------------ upper chart
            )

        except ValueError as e:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} GRAPH CONTROLLER: Error Occured Trying to Graph {Fore.BLUE}Single Line Graph{Style.RESET_ALL} at {Fore.RED}Row: {row}, Column: {col}{Style.RESET_ALL}")
            print(f"    {Fore.YELLOW}Try Checking Color Parameters{Style.RESET_ALL}")
            quit()

        except KeyError as e:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} GRAPH CONTROLLER: Error Occured Trying to Graph {Fore.BLUE}Single Line Graph{Style.RESET_ALL} at {Fore.RED}Row: {row}, Column: {col}{Style.RESET_ALL}")
            print(f"    {Fore.YELLOW}Try Checking Data Column Names to see if data inputted correctly{Style.RESET_ALL}")
            quit()

        except Exception as e:
            print(e)

    def graphMultipleLines(self, xAxis, yAxis, lineName, row, col, colors = []):
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
        tempColors = ['black', 'red', 'green', 'blue', 'cyan', 'gray']
        try:
            for i in range(len(yAxis)):
                self.fig.append_trace(
                    go.Scatter(
                        x = xAxis,
                        y = yAxis[i],
                        line = dict(color = tempColors[i] if len(yAxis) != len(colors) else colors[i], width = 1),
                        name = lineName[i]
                    ), row = row, col = col  # <------------ upper chart
                )
        except IndexError as e:
            print(e)
            print(f"{Fore.RED}[-]{Style.RESET_ALL} GRAPH CONTROLLER: Error Occurred Trying to Graph {Fore.BLUE}Multi Line Graph{Style.RESET_ALL} at {Fore.RED}Row: {row}, Column: {col}{Style.RESET_ALL}")
            print(f"    {Fore.YELLOW}Try Checking Row and Column Parameters{Style.RESET_ALL}")
            quit()

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
