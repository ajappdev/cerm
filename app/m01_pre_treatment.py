import pandas as pd
import numpy as np
from random import choice
from string import ascii_uppercase

# Importing app modules
import app.m00_common as m00

# Declaring global variables
PD_DTYPES_TRANSLATOR = {
    'datetime64[ns]': 'date',
    'object': 'object',
    'datetime64': 'date',
    'int64': 'amount',
    'float64': 'amount',
    'timedelta[ns]': 'date'
}
class PreTreatment:

    def __init__(self, dataset_df: pd.DataFrame()):
        """
        """
        self.dataset_df = dataset_df

        self.other_random_str =\
            ''.join(choice(ascii_uppercase) for i in range(16))

        self.clean_dataset()
        self.create_additional_date_columns()
        self.get_column_types()
        self.detail_column_types()
        self.remove_nans()
        self.changed_unchanged_columns()
        self.describe_date_columns()

    def clean_dataset(self):
        
        # Clean dataset columns names
        new_columns = []
        for column in self.dataset_df.columns:
            new_columns.append(clean_string(column))

        self.dataset_df.columns = new_columns

        # Remove empty columns
        for column in self.dataset_df.columns:
            if self.dataset_df[column].isnull().all():
                self.dataset_df = self.dataset_df.drop(column, axis=1)

    def create_additional_date_columns(self):
        col_types =\
            pd.DataFrame(
                {'column_name':self.dataset_df.dtypes.index,
                 'column_type':self.dataset_df.dtypes.values})
        for index, row in col_types.iterrows():
            if PD_DTYPES_TRANSLATOR[str(row['column_type'])] == "date":
                day_of_week_column_name = row['column_name']+"_"+self.other_random_str+"_day_of_week"
                week_column_name = row['column_name']+"_"+self.other_random_str+"_week"
                month_column_name = row['column_name']+"_"+self.other_random_str+"_month"
                year_column_name = row['column_name']+"_"+self.other_random_str+"_year"
                self.dataset_df[month_column_name] = self.dataset_df[row['column_name']].dt.strftime('%Y-%m')
                self.dataset_df[year_column_name] = self.dataset_df[row['column_name']].dt.year
                self.dataset_df[week_column_name] = self.dataset_df[row['column_name']].dt.strftime('%Y-%U')
                self.dataset_df[day_of_week_column_name] = self.dataset_df[row['column_name']].dt.day_name()

    def get_column_types(self):
        col_types =\
            pd.DataFrame(
                {'column_name':self.dataset_df.dtypes.index,
                 'column_type':self.dataset_df.dtypes.values})
        self.dataset_columns = {}
        for index, row in col_types.iterrows():
            self.dataset_columns.update(
                {str(row['column_name']):
                 [PD_DTYPES_TRANSLATOR[str(row['column_type'])]]})

    def detail_column_types(self):
        for column in self.dataset_df.columns:
            if len(self.dataset_df[column].unique().tolist()) <= m00.THRESHOLD_ACTOR_CATEGORY * len(self.dataset_df):
                self.dataset_columns[column].append("category")
            else:
                self.dataset_columns[column].append("actor")

    def remove_nans(self):
        for k, v in self.dataset_columns.items():
            if "amount" in v:
                self.dataset_df[k] = self.dataset_df[k].replace(np.nan, 0)
            if "object" in v:
                self.dataset_df[k] = self.dataset_df[k].replace(
                    np.nan, self.other_random_str)

    def changed_unchanged_columns(self):
        for column in self.dataset_df.columns:
            if len(self.dataset_df[column].unique().tolist()) == 1:
                 self.dataset_columns[column].insert(0, "unchanged")
            else:
                 self.dataset_columns[column].insert(0, "changed")

    def describe_date_columns(self):
        self.date_columns = {}
        for k, v in self.dataset_columns.items():
            if "date" in v:
                self.date_columns.update({k:{}})
                describe_date_column(self.dataset_df[k], k)

# Declaring functions

def clean_string(column_name: str):
    column_name = column_name.strip()
    column_name = column_name.replace("\n", " ")
    column_name = column_name.replace("\n", " ")
    column_name = column_name.replace("\n", " ")
    return column_name

def describe_date_column(column: pd.Series, column_header: str):
    df_column = pd.DataFrame({column_header:column.values})
    min_value = min(df_column[column_header])
    max_value = max(df_column[column_header])
    covered_period = (max_value - min_value).days
    print(covered_period)
