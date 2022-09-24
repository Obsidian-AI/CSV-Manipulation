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
        """
        Function that initializes the number of subplots
        """
        try:
            self.fig = make_subplots(rows = rows, cols = cols, subplot_titles = ("Plot 1", "Plot 2", "Plot 3", "Plot 4", "Plot 5", "Plot 6", "Plot 7"))
            print(f"\n{Fore.BLUE}GRAPHING MODULE:{Style.RESET_ALL}")
        except Exception:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Unknown Error Occurred Trying to Initialize Graphing Module")
            quit()

    def dimensionCheck(self):
        """
        Function used to check whether rows and columns are open or else warn the user
        """
        for i in range(len(self.dimensions)):
            if self.dimensions.count(self.dimensions[i]) > 1:
                print(f"{Fore.RED}[-]{Style.RESET_ALL}GRAPH CONTROLLER: Error Occurred Laying Graphs in Grid Pattern")
                print(f"    {Fore.YELLOW}Try Checking Row and Column Parameters{Style.RESET_ALL}")
                quit()
            
    def graphOneLineChart(self, xAxis, yAxis, lineName, row, col, graphName = "", color = ""):
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
                ), row = row, col = col
            )
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Created Single Line Graph on Row: {row} and Column: {col}")

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

    def graphMultipleLinesChart(self, xAxis, yAxis, lineName, row, col, colors = []):
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
                    ), row = row, col = col
                )
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Created Multiline Graph on Row: {row} and Column: {col}")

        except IndexError as e:
            print(e)
            print(f"{Fore.RED}[-]{Style.RESET_ALL} GRAPH CONTROLLER: Error Occurred Trying to Graph {Fore.BLUE}Multi Line Graph{Style.RESET_ALL} at {Fore.RED}Row: {row}, Column: {col}{Style.RESET_ALL}")
            print(f"    {Fore.YELLOW}Try Checking Row and Column Parameters{Style.RESET_ALL}")
            quit()

    def graphHorizontalLine(self, value, row, col, color = 'black', lineType = 'dash', thickness = 2):
        """
        Function that graphs a horizontal line at a y value on any graph of the user's choice

        value --> The Y Value for line
        row --> The Row Number
        col --> The Column Number
        color --> The color of the line
        lineType --> The type of line that you would like to add
        thickness --> The amount of thickness you would like to add within a line
        """
        try:
            self.fig.add_hline(y = value, line_dash = lineType, row = row, col = col, line_color = color, line_width = thickness)
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Create a Horizontal Line on Row: {row} and Column: {col}")

        except Exception:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} GRAPH CONTROLLER: Error Occurred Trying to Graph Horizontal Line on Row: {row} and Column {col}")
            print(f"    {Fore.YELLOW}Try Checking the Function Row and Column Parameters{Style.RESET_ALL}")
            quit()

    def graphBarGraph(self, x, y, row, col, name = "", errorInterval = [], colors = []):
        """
        Function that creates a bar graph with the ability to add error intervals

        x --> X Axis Names [REQUIRED]
        y --> The Data [REQUIRED]
        row --> The Row Number [REQUIRED]
        col --> The Column Number [REQUIRED]
        errorInterval --> Add Confidence Intervals with the error bar range
        colors --> Set the Colors of the graph [NOT ACTIVE]
        """
        try:
            self.fig.append_trace(
                go.Bar(
                    name = name if name != "" else None,
                    x = x,
                    y = y,
                    error_y = dict(type='data', array = errorInterval) if errorInterval != [] else None
                ), row = row, col = col
            )

            if f"{row}{col}" not in self.dimensions:
                self.dimensions.append(f"{row}{col}")
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Created Bar Graph on Row: {row} and Column: {col}")
            else:
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Modified Bar Graph on Row: {row} and Column: {col}")

        except Exception:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Error Occurred Trying to Create Bar Graph on Row: {row} and Column {col}")
            exit()

    def show(self):
        self.dimensionCheck()
        self.fig.update_layout(
            go.Layout(
                plot_bgcolor = '#efefef',
                font_family = 'Monospace',
                font_color =  '#000000',
                font_size = 20,
                barmode='group',
                xaxis = dict(
                    rangeslider = dict(
                        visible = False
                    )
                )
            )
        )
        self.fig.show()
