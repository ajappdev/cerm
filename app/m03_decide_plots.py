import pandas as pd
import numpy as np
from datetime import date, datetime

# Importing app modules
import app.m00_common as m00
import app.m04_plots as m04


class DecidePlots:

    def __init__(
            self,
            dataset_df: pd.DataFrame(),
            dataset_columns: dict,
            category_columns: dict,
            date_columns: dict,
            month_columns: dict,
            week_columns: dict,
            random_str: str
            ):
        """
        """
        self.dataset_df = dataset_df
        self.dataset_columns = dataset_columns
        self.date_columns = date_columns
        self.category_columns = category_columns
        self.month_columns = month_columns
        self.week_columns = week_columns
        self.random_str = random_str

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        self.decided_plots = []

        self.check_one_d_plots()
        self.check_two_d_plots()
        self.check_three_d_plots()
        
    def check_one_d_plots(self):
        columns = list(self.dataset_columns.keys())
        for x in range(len(columns)):
            for plot in m04.ONE_D_PLOTS_LIST:
                tested_plot = plot(
                    columns[x], "", "", self.dataset_columns, self.category_columns, self.month_columns, self.random_str)
                if tested_plot.is_convenient():
                    self.decided_plots.append(
                        {tested_plot.__class__.__name__:[columns[x], "", ""]})

    def check_two_d_plots(self):
        columns = list(self.dataset_columns.keys())
        for x in range(len(columns)):
            for y in range(len(columns)):
                if x != y:
                    for plot in m04.TWO_D_PLOTS_LIST:
                        tested_plot = plot(
                            columns[x], columns[y], "", self.dataset_columns, self.category_columns, self.month_columns, self.random_str)
                        if tested_plot.is_convenient():
                            self.decided_plots.append(
                                {tested_plot.__class__.__name__:[columns[x], columns[y], ""]})

    def check_three_d_plots(self):
        columns = list(self.dataset_columns.keys())
        for x in range(len(columns)):
            for y in range(len(columns)):
                if x != y:
                    for plot in m04.THREE_D_PLOTS_LIST:
                        tested_plot = plot(
                            columns[x], columns[y], "", self.dataset_columns, self.category_columns, self.month_columns, self.random_str)
                        if tested_plot.is_convenient():
                            self.decided_plots.append(
                                [columns[x], "-----", columns[y], tested_plot])