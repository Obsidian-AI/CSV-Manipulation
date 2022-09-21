# ---------- LIBRARIES ---------- #
# Global
import pandas as pd
import json
import time
import colorama
from colorama import *

# Local
from Utilities.keyController import keyController
from Core.graphController import GraphController
from Core.pandaManipulator import PandasManipulation

# ---------- MAIN SECTION ---------- #
def main():
    # Load the Data (Edit in config.json)
    data = pd.read_csv(keyController().getConfigKey('file path'))

    # Initialize Controllers
    pandasController = PandasManipulation(data)
    graphController = GraphController()
    
    try:
        ##########################################################################
        # TABLE MANIPULATION
        pandasController.addColumns(['Open', 'High', 'Low'], columnName = 'Add Columns')
        pandasController.subtractColumns(['Open', 'High', 'Low'], columnName = 'Subtract Columns')
        pandasController.multiplyColumns(['Open', 'High', 'Low'], columnName = 'Multiply Columns')
        pandasController.divideColumns(['Open', 'High', 'Low'], columnName = 'Divide Columns')
        pandasController.changeColumnHeader('Volume', 'Testing Set')
        pandasController.duplicateColumn('Testing Set', 'Volume')
        pandasController.dropEmptyRows()
        ##########################################################################

        data = pandasController.finalData()

        ##########################################################################
        # GRAPH CONTROLLER
        graphController.initialize(rows = 3, cols = 3)
        graphController.graphOneLine(data.index, data['Close'], "Single Line Close", 1, 1, color = 'blue')
        graphController.graphOneLine(data.index, data['Open'], "Single Line High", 1, 2)
        graphController.graphOneLine(data.index, data['High'], "Single Line Low", 1, 3)
        graphController.graphMultipleLines(data.index, [data['Close'], data['Testing Set']], ["Multiline Close", "Multiline Volume"], 2, 1)
        graphController.graphMultipleLines(data.index, [data['Close'], data['Testing Set']], ["Multiline Close", "Multiline Volume"], 2, 2, colors = ['green', 'cyan'])
        graphController.graphMultipleLines(data.index, [data['Close'], data['Testing Set']], ["Multiline Close", "Multiline Volume"], 2, 3, colors = ['orange', 'white'])
        ##########################################################################

    except SyntaxError:
        print(f"{Fore.RED}[-]{Style.RESET_ALL} Incorrect Syntax Used")
        print(f"{Fore.YELLOW} Try Checking the functions you entered and look at manual to see if properly entered")


    # Final Data
    final = pandasController.finalData()
    graphController.show()

    # Save file
    final.to_csv(f'Output/output.csv', index = False, header = True)
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Saved File to Output Folder")
    print(pd.read_csv(f'Output/output.csv'))

if __name__ == '__main__':
    main()