import pandas as pd
import numpy as np
from datetime import date, datetime

# Importing app modules
import app.m00_common as m00

class Describe:

    def __init__(
            self,
            dataset_df: pd.DataFrame(),
            dataset_columns: dict,
            random_str: str
            ):
        """
        """
        self.dataset_df = dataset_df
        self.dataset_columns = dataset_columns
        self.random_str = random_str
        
        self.describe_date_columns()
        self.describe_month_columns()
        self.describe_week_columns()
        self.describe_category_columns()

    def describe_category_columns(self):
        """
        """
        self.category_columns = {}
        for k, v in self.dataset_columns.items():
            if "category" in v:
                self.category_columns.update(
                    {k:get_category_column_attributes(self.dataset_df[k], k)})

    def describe_date_columns(self):
        """
        """
        self.date_columns = {}
        for k, v in self.dataset_columns.items():
            if "date" in v:
                self.date_columns.update(
                    {k:get_date_column_attributes(self.dataset_df[k], k)})

    def describe_month_columns(self):
        """
        """
        self.month_columns = {}
        for k, v in self.dataset_columns.items():
            if self.random_str + "_month_" in k:
                self.month_columns.update(
                    {k:get_month_column_attributes(self.dataset_df[k], k)})

    def describe_week_columns(self):
        """
        """
        self.week_columns = {}
        for k, v in self.dataset_columns.items():
            if self.random_str + "_week_" in k:
                self.week_columns.update(
                    {k:get_week_column_attributes(self.dataset_df[k], k)})
                

# Declare functons

def get_category_column_attributes(column: pd.Series, column_header: str):
    """
    """
    df_column = pd.DataFrame({column_header:column.values})
    distinct_values = len(df_column[column_header].unique().tolist())
    return {
        "distinct_values": distinct_values
        }

def get_date_column_attributes(column: pd.Series, column_header: str):
    """
    """
    df_column = pd.DataFrame({column_header:column.values})
    min_value = min(df_column[column_header])
    max_value = max(df_column[column_header])
    covered_period = (max_value - min_value).days
    df_column[column_header] = pd.to_datetime(df_column[column_header].dt.strftime(m00.DATE_FORMAT))
    distinct_values = len(df_column[column_header].unique().tolist())

    if covered_period > 0:
        perc_distinct_values = (distinct_values/covered_period) * 100
    else:
        perc_distinct_values = 0

    return {
        "min_value": min_value,
        "max_value": max_value,
        "covered_period": covered_period,
        "distinct_values": distinct_values,
        "perc_distinct_values": perc_distinct_values
        }


def get_month_column_attributes(column: pd.Series, column_header: str):
    """
    """
    df_column = pd.DataFrame({column_header:column.values})
    min_value = min(df_column[column_header])
    max_value = max(df_column[column_header])
    min_period = datetime.strptime(str(str(str(min_value).split('-')[0]) + "-" + str(str(min_value).split('-')[1]) + "-" + "01"), m00.DATE_FORMAT)
    max_period = datetime.strptime(str(str(str(max_value).split('-')[0]) + "-" + str(str(max_value).split('-')[1]) + "-" + "01"), m00.DATE_FORMAT)
    covered_period = diff_month(max_period, min_period)
    distinct_values = len(df_column[column_header].unique().tolist())

    if covered_period > 0:
        perc_distinct_values = (distinct_values/covered_period) * 100
    else:
        perc_distinct_values = 0

    return {
        "min_value": min_value,
        "max_value": max_value,
        "covered_period": covered_period,
        "min_period": min_period,
        "max_period": max_period,
        "distinct_values": distinct_values,
        "perc_distinct_values": perc_distinct_values
        }


def get_week_column_attributes(column: pd.Series, column_header: str):
    """
    """
    df_column = pd.DataFrame({column_header:column.values})
    min_value = min(df_column[column_header])
    max_value = max(df_column[column_header])
    min_period = datetime.strptime(min_value + '-1', "%Y-W%W-%w")
    max_period = datetime.strptime(max_value + '-1', "%Y-W%W-%w")
    covered_period = diff_week(max_period, min_period)
    distinct_values = len(df_column[column_header].unique().tolist())

    if covered_period > 0:
        perc_distinct_values = (distinct_values/covered_period) * 100
    else:
        perc_distinct_values = 0

    return {
        "min_value": min_value,
        "max_value": max_value,
        "covered_period": covered_period,
        "min_period": min_period,
        "max_period": max_period,
        "distinct_values": distinct_values,
        "perc_distinct_values": perc_distinct_values
        }


def diff_month(d1, d2):
    """
    """
    return (d1.year - d2.year) * 12 + d1.month - d2.month + 1
    

def diff_week(d1, d2):
    """
    """
    return (d1.year - d2.year) * 52 + int(d1.strftime("%W")) - int(d2.strftime("%W")) + 1