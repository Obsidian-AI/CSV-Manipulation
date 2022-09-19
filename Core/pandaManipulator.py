# ---------- LIBRARIES ---------- #
# Global
import pandas as pd
import colorama
from colorama import *


# ---------- TABLE MANIPULATION CLASS ---------- #
class PandasManipulation():
    def __init__(self, data):
        self.data = data.copy()

    def addColumns(self, columns, columnName = ""):
        try:
            df = pd.DataFrame(self.data)
            self.data[columnName] = df[columns].sum(axis=1)
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Added {columns}")

        except KeyError:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Error Occurred when trying to add the following columns:")
            print(f"    {columns}")
            print(f"{Fore.YELLOW} Try Checking Column Names")
            quit()

    def subtractColumns(self, columns, columnName = ""):
        try:
            df = self.data.copy()
            df['subtractions'] = df[columns[0]]
            for i in range(len(columns)):
                try:
                    df['subtractions'] = df['subtractions'] - df[columns[i + 1]]
                except IndexError:
                    break

            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Subtracted {columns}")

            if columnName == "":
                return df['subtractions']
            else:
                self.data[columnName] = df['subtractions']
                return self.data

        except KeyError:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Error Occurred when trying to subtract the following columns:")
            print(f"    {columns}")
            print(f"{Fore.YELLOW} Try Checking Column Names")
            quit()

    def multiplyColumns(self, columns, columnName = ""):
        try:
            df = self.data.copy()
            df['multiply'] = df[columns[0]]
            for i in range(len(columns)):
                try:
                    df['multiply'] = df['multiply'].mul(df[columns[i + 1]])
                except IndexError:
                    break

            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Multiplied {columns}")

            if columnName == "":
                return df['multiply']
            else:
                self.data[columnName] = df['multiply']
                return self.data
        except KeyError:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Error Occurred when trying to multiply the following columns:")
            print(f"    {columns}")
            quit()

    def divideColumns(self, columns, columnName = ""):
        try:
            df = self.data.copy()
            df['multiply'] = df[columns[0]]
            for i in range(len(columns)):
                try:
                    df['multiply'] = df['multiply'].div (df[columns[i + 1]])
                except IndexError:
                    break

            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Divided {columns}")

            if columnName == "":
                return df['multiply']
            else:
                self.data[columnName] = df['multiply']
                return self.data
        except KeyError:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Error Occurred when trying to divide the following columns:")
            print(f"    {columns}")
            print(f"{Fore.YELLOW} Try Checking Column Names")
            quit()

    def changeColumnHeader(self, oldName, newName):
        try:
            if oldName in list(self.data.columns):
                self.data.rename(columns = {oldName : newName}, inplace = True)
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Renamed Header from {oldName} to {newName}")
                return self.data
            else:
                print(f"{Fore.RED}[-]{Style.RESET_ALL} Error Occurred when trying to rename {oldName} to {newName}")
                print(f"{Fore.YELLOW} Try Checking if Original Name Column exists")
                quit()

        except:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Unknown Error Occurred when trying to change column header")

    def dropEmptyRows(self):
        try:
            self.data = self.data.dropna()
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Dropped all Empty Rows")
        
        except:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Unknown Error Occurred Trying to drop empty table values")

    def finalData(self):
        return self.data