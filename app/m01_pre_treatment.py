from django.templatetags.static import static
import pandas as pd
import numpy as np
import os
from django.conf import settings
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

        pd.set_option('max_columns', None)
        pd.set_option('max_rows', None)
        pd.set_option('display.expand_frame_repr', False)

        self.other_random_str =\
            ''.join(choice(ascii_uppercase) for i in range(16))

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

    def get_columns_types(self):
        self.dataset_columns = {}
        df_coltypes =\
            pd.DataFrame(
                {'column_name':self.dataset_df.dtypes.index,
                 'column_type':self.dataset_df.dtypes.values})
        
        for index, row in df_coltypes.iterrows():
            self.dataset_columns.update(
                {str(row['column_name']):
                 [PD_DTYPES_TRANSLATOR[str(row['column_type'])]]})

    def detail_column_types(self):
        for column in self.dataset_df.columns:
            if len(self.dataset_df[column].unique().tolist()) <= m00.THRESHOLD_ACTOR_CATEGORY * len(self.dataset_df):
                self.dataset_columns[column].append("category")
            else:
                self.dataset_columns[column].append("actor")

            if len(self.dataset_df[column].unique().tolist()) == 1:
                 self.dataset_columns[column].insert(0, "unchanged")
            else:
                 self.dataset_columns[column].insert(0, "changed")

    def remove_nans(self):
        for k, v in self.dataset_columns.items():
            if "amount" in v:
                self.dataset_df[k] = self.dataset_df[k].replace(np.nan, 0)
            if "object" in v:
                self.dataset_df[k] = self.dataset_df[k].replace(
                    np.nan, self.other_random_str)

    def homogeneous_loop(self):
        for k, v in self.dataset_columns.items():
            if "amount" in v and "category" in v:
                pass

        print(self.dataset_df)
        print(self.dataset_columns)

# Declaring functions

def clean_string(column_name: str):
    column_name = column_name.strip()
    column_name = column_name.replace("\n", "")
    column_name = column_name.replace("\n", "")
    column_name = column_name.replace("\n", "")
    return column_name
