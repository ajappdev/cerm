import pandas as pd
import numpy as np
from random import choice
from string import ascii_uppercase
import re

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

        self.random_str =\
            ''.join(choice(ascii_uppercase) for i in range(16))

        self.clean_dataset()
        self.create_additional_date_columns()
        self.get_column_types()
        self.detail_column_types()
        self.remove_nans()
        self.attribute_colors_to_columns()
        self.changed_unchanged_columns()

    def clean_dataset(self):
        """
        """
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
        """
        """
        col_types =\
            pd.DataFrame(
                {'column_name':self.dataset_df.dtypes.index,
                 'column_type':self.dataset_df.dtypes.values})
        for index, row in col_types.iterrows():
            if PD_DTYPES_TRANSLATOR[str(row['column_type'])] == "date":
                day_of_week_column_name = self.random_str + "_day of week" + " ("+ row['column_name']+")"
                week_column_name = self.random_str + "_week" + " ("+ row['column_name']+")"
                month_column_name = self.random_str + "_month" + " ("+ row['column_name']+")"
                year_column_name = self.random_str + "_year" + " ("+ row['column_name']+")"
                self.dataset_df[month_column_name] = self.dataset_df[row['column_name']].dt.strftime('%Y-%m')
                self.dataset_df[year_column_name] = self.dataset_df[row['column_name']].dt.year
                self.dataset_df[week_column_name] = self.dataset_df[row['column_name']].dt.strftime('%Y-W%U')
                self.dataset_df[day_of_week_column_name] = self.dataset_df[row['column_name']].dt.day_name()

    def get_column_types(self):
        """
        """
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
        """
        """
        for column in self.dataset_df.columns:
            if len(self.dataset_df[column].unique().tolist()) <= m00.THRESHOLD_ACTOR_CATEGORY * len(self.dataset_df) and "amount" not in self.dataset_columns[column]:
                self.dataset_columns[column].append("category")
            else:
                self.dataset_columns[column].append("actor")

    def remove_nans(self):
        """
        """
        for k, v in self.dataset_columns.items():
            if "amount" in v:
                self.dataset_df[k] = self.dataset_df[k].replace(np.nan, 0)
            if "object" in v:
                self.dataset_df[k] = self.dataset_df[k].replace(
                    np.nan, "Other")

    def attribute_colors_to_columns(self):
        """
        """
        for column in self.dataset_df.columns:
            self.dataset_columns[column].insert(0, random_hex_color())

    def changed_unchanged_columns(self):
        """
        """
        for column in self.dataset_df.columns:
            if len(self.dataset_df[column].unique().tolist()) == 1:
                 self.dataset_columns[column].insert(0, "unchanged")
            else:
                 self.dataset_columns[column].insert(0, "changed")

# Declaring functions

def clean_string(column_name: str):
    """
    """
    column_name = column_name.strip()
    column_name = column_name.replace("\n", " ")
    column_name = column_name.replace("\n", " ")
    column_name = column_name.replace("\n", " ")
    column_name = column_name.strip()
    column_name = re.sub(' +', ' ', column_name)

    return column_name

def random_hex_color():
    """
    """
    import random
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())