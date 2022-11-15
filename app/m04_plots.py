
class SimpleSumPlot:

        def __init__(
                self,
                column_one_name,
                column_two_name,
                column_three_name,
                dataset_columns):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name == "" and\
                        self.column_three_name == "":
                if "amount" in self.dataset_columns[self.column_one_name]:
                    return True

            return False


class SimpleAvgPlot:

        def __init__(
                self,
                column_one_name,
                column_two_name,
                column_three_name,
                dataset_columns):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name == "" and\
                        self.column_three_name == "":
                if "amount" in self.dataset_columns[self.column_one_name]:
                    return True

            return False


class SimpleMinPlot:

        def __init__(
                self,
                column_one_name,
                column_two_name,
                column_three_name,
                dataset_columns):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name == "" and\
                        self.column_three_name == "":
                if "amount" in self.dataset_columns[self.column_one_name]:
                    return True

            return False


class SimpleMaxPlot:

        def __init__(
                self,
                column_one_name,
                column_two_name,
                column_three_name,
                dataset_columns):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name == "" and\
                        self.column_three_name == "":
                if "amount" in self.dataset_columns[self.column_one_name]:
                    return True

            return False


class SumPerCategoryPlot:

        def __init__(
                self,
                column_one_name,
                column_two_name,
                column_three_name,
                dataset_columns):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name != "" and\
                        self.column_three_name == "":
                if "category" in self.dataset_columns[self.column_one_name] and "amount" in self.dataset_columns[self.column_two_name]:
                    return True
            return False


class AvgPerCategoryPlot:

        def __init__(
                self,
                column_one_name,
                column_two_name,
                column_three_name,
                dataset_columns):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name != "" and\
                        self.column_three_name == "":
                if "category" in self.dataset_columns[self.column_one_name] and "amount" in self.dataset_columns[self.column_two_name]:
                    return True
            return False


class MinPerCategoryPlot:

        def __init__(
                self,
                column_one_name,
                column_two_name,
                column_three_name,
                dataset_columns):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name != "" and\
                        self.column_three_name == "":
                if "category" in self.dataset_columns[self.column_one_name] and "amount" in self.dataset_columns[self.column_two_name]:
                    return True
            return False


class MaxPerCategoryPlot:

        def __init__(
                self,
                column_one_name,
                column_two_name,
                column_three_name,
                dataset_columns):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name != "" and\
                        self.column_three_name == "":
                if "category" in self.dataset_columns[self.column_one_name] and "amount" in self.dataset_columns[self.column_two_name]:
                    return True
            return False


class MinPerCategoryPlot:

        def __init__(
                self,
                column_one_name,
                column_two_name,
                column_three_name,
                dataset_columns):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name != "" and\
                        self.column_three_name == "":
                if "category" in self.dataset_columns[self.column_one_name] and "amount" in self.dataset_columns[self.column_two_name]:
                    return True
            return False


ONE_D_PLOTS_LIST = [
    SimpleSumPlot,
    SimpleAvgPlot,
    SimpleMinPlot,
    SimpleMaxPlot]

TWO_D_PLOTS_LIST = [
    SumPerCategoryPlot,
    AvgPerCategoryPlot,
    MinPerCategoryPlot,
    MaxPerCategoryPlot
    ] 
THREE_D_PLOTS_LIST = [] 