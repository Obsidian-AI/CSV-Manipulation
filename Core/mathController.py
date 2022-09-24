# ---------- LIBRARIES ---------- #
# Global
import pandas as pd
from colorama import *
import numpy as np
import scipy.stats as st



# ---------- TABLE MANIPULATION CLASS ---------- #
class MathController():
    def __init__(self):
        pass

    def confidenceInterval(self, data, confidence = 0.95):
        """
        Function that calculates the confidence intervals
        """
        try:
            st.t.interval(alpha = confidence, df = len(data) - 1, loc = np.mean(data), scale = st.sem(data))
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Successfully Found Range of Confidence Interval")

        except TypeError:
            print(f"{Fore.RED}[-]{Style.RESET_ALL} Type Error Occurred trying to find confidence interval")
            print(f"    {Fore.YELLOW}Try Checking the Data Inputted and make sure no words are involved{Style.RESET_ALL}")
            quit()

        return st.t.interval(alpha = confidence, df = len(data) - 1, loc = np.mean(data), scale = st.sem(data))
        