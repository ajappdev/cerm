import pandas as pd
import numpy as np

# Importing app modules
import app.m00_common as m00

class Describe:

    def __init__(
            self, dataset_df: pd.DataFrame(),
            dataset_columns: dict,
            random_str: str
            ):
        """
        """
        self.dataset_df = dataset_df
        self.dataset_columns = dataset_columns
        self.random_str = random_str
        
        print(self.dataset_df)
        self.describe_date_columns()
    
    def describe_date_columns(self):
        self.date_columns = {}
        for k, v in self.dataset_columns.items():
            if "date" in v:
                self.date_columns.update(
                    {k:get_date_column_attributes(self.dataset_df[k], k)})

    def describe_month_columns(self):
        self.month_columns = {}
        for k, v in self.dataset_columns.items():
            if self.random_str + "_month_" in k:
                self.month_columns.update(
                    {k:get_month_column_attributes(self.dataset_df[k], k)})

        print(self.date_columns)
                

# Declare functons

def get_date_column_attributes(column: pd.Series, column_header: str):
    df_column = pd.DataFrame({column_header:column.values})
    min_value = min(df_column[column_header])
    max_value = max(df_column[column_header])
    covered_period = (max_value - min_value).days
    df_column[column_header] = pd.to_datetime(df_column[column_header].dt.strftime(m00.DATE_FORMAT))
    distinct_values = len(df_column[column_header].unique().tolist())
    if len(df_column) > 0:
        perc_distinct_values = (distinct_values/len(df_column)) * 100
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
    df_column = pd.DataFrame({column_header:column.values})
    min_value = min(df_column[column_header])
    max_value = max(df_column[column_header])
    covered_period = (max_value - min_value).days
    df_column[column_header] = pd.to_datetime(df_column[column_header].dt.strftime(m00.DATE_FORMAT))
    distinct_values = len(df_column[column_header].unique().tolist())
    if len(df_column) > 0:
        perc_distinct_values = (distinct_values/len(df_column)) * 100
    else:
        perc_distinct_values = 0

    return {
        "min_value": min_value,
        "max_value": max_value,
        "covered_period": covered_period,
        "distinct_values": distinct_values,
        "perc_distinct_values": perc_distinct_values
        }