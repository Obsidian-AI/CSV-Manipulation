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
        pandasController.dropEmptyRows()

        # GRAPH CONTROLLER
        graphController.initialize(rows = 3, cols = 3)
        graphController.graphOneLine(pandasController.finalData().index, pandasController.finalData()['Close'], "Close", 1, 1)
        graphController.graphOneLine(pandasController.finalData().index, pandasController.finalData()['Open'], "High", 1, 2)
        graphController.graphOneLine(pandasController.finalData().index, pandasController.finalData()['High'], "Low", 1, 3)
        graphController.graphMultipleLines(pandasController.finalData().index, [pandasController.finalData()['Close'], pandasController.finalData()['Open']], "Multiline Graph", 2, 1)
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