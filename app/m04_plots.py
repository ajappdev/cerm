
class SimpleSumPlot:

        def __init__(
                self,
                column_one_name: str,
                column_two_name: str,
                column_three_name: str,
                dataset_columns: dict,
                random_str: str
                ):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns
            self.random_str = random_str
            self.formulas = "sum_first"
            self.title = ""
            self.sub_title = ""
            self.unit = ""
            self.color = ""
            self.content = ""
            self.content_id = 0
            self.template = "widgets/simple-figure-widget.html"

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name == "" and\
                        self.column_three_name == "":
                if "amount" in self.dataset_columns[self.column_one_name]:
                    if (self.random_str + "_year") not in self.column_one_name:
                        return True

            return False


class SimpleAvgPlot:

        def __init__(
                self,
                column_one_name: str,
                column_two_name: str,
                column_three_name: str,
                dataset_columns: dict,
                random_str: str):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns
            self.random_str = random_str
            self.formulas = "avg_first"
            self.title = ""
            self.sub_title = ""
            self.unit = ""
            self.color = ""
            self.content = ""
            self.content_id = 0
            self.template = "widgets/simple-figure-widget.html"

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name == "" and\
                        self.column_three_name == "":
                if "amount" in self.dataset_columns[self.column_one_name]:
                    if (self.random_str + "_year") not in self.column_one_name:
                        return True

            return False


class SimpleMinPlot:

        def __init__(
                self,
                column_one_name: str,
                column_two_name: str,
                column_three_name: str,
                dataset_columns: dict,
                random_str: str):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns
            self.random_str = random_str
            self.formulas = "min_first"
            self.title = ""
            self.sub_title = ""
            self.unit = ""
            self.color = ""
            self.content = ""
            self.content_id = 0
            self.template = "widgets/simple-figure-widget.html"

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name == "" and\
                        self.column_three_name == "":
                if "amount" in self.dataset_columns[self.column_one_name]:
                    if (self.random_str + "_year") not in self.column_one_name:
                        return True

            return False


class SimpleMaxPlot:

        def __init__(
                self,
                column_one_name: str,
                column_two_name: str,
                column_three_name: str,
                dataset_columns: dict,
                random_str: str):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns
            self.random_str = random_str
            self.formulas = "max_first"
            self.title = ""
            self.sub_title = ""
            self.unit = ""
            self.color = ""
            self.content = ""
            self.content_id = 0
            self.template = "widgets/simple-figure-widget.html"

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name == "" and\
                        self.column_three_name == "":
                if "amount" in self.dataset_columns[self.column_one_name]:
                    if (self.random_str + "_year") not in self.column_one_name:
                        return True

            return False


class CategoryTablePlot:

        def __init__(
                self,
                column_one_name: str,
                column_two_name: str,
                column_three_name: str,
                dataset_columns: dict,
                random_str: str):
            """
            """
            self.column_one_name = column_one_name
            self.column_two_name = column_two_name
            self.column_three_name = column_three_name
            self.dataset_columns = dataset_columns
            self.random_str = random_str
            self.formulas = "table_second_per_first"
            self.title = ""
            self.sub_title = ""
            self.unit = ""
            self.color = ""
            self.content = ""
            self.content_id = 0
            self.template = "widgets/second-per-first-widget.html"

        def is_convenient(self):
            """
            """
            if self.column_one_name != "" and\
                    self.column_two_name != "" and\
                        self.column_three_name == "":
                if "category" in self.dataset_columns[self.column_one_name] and "amount" in self.dataset_columns[self.column_two_name]:
                    if (self.random_str + "_year") not in self.column_two_name:
                        return True
            return False


ONE_D_PLOTS_LIST = [
    SimpleSumPlot,
    SimpleAvgPlot,
    SimpleMinPlot,
    SimpleMaxPlot]

TWO_D_PLOTS_LIST = [
    CategoryTablePlot
    ] 
THREE_D_PLOTS_LIST = []