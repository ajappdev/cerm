import pandas as pd
import app.m04_plots as m04

class DrawPlots:

    def __init__(
            self,
            dataset_df: pd.DataFrame(),
            decided_plots: list,
            dataset_columns: dict,
            random_str: str):
        """
        """
        self.dataset_df = dataset_df
        self.decided_plots = decided_plots
        self.random_str = random_str
        self.dataset_columns = dataset_columns
        self.plots = []
        self.draw()

    def draw(self):
        """
        """
        plot_index = 0
        for element in self.decided_plots:
            plot_index += 1
            plot_class = getattr(m04, list(element.keys())[0])

            first_col = element[list(element.keys())[0]][0]
            second_col = element[list(element.keys())[0]][1]
            third_col = element[list(element.keys())[0]][2]

            instance = plot_class(
                first_col,
                second_col,
                third_col,
                self.dataset_columns,
                self.random_str)

            formulas = instance.formulas
            if formulas == "sum_first":
                instance.title = "Total " + str(
                    first_col).lower()
                instance.sub_title = "Sum of " + str(
                    first_col).lower() + " column"
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    first_col][1]
                instance.content = self.dataset_df[
                    first_col].sum()
                instance.content_id = plot_index
                self.plots.append(instance)

            if formulas == "avg_first":
                instance.title = "Average " + str(
                    first_col).lower()
                instance.sub_title = "Mean of " + str(
                    first_col).lower() + " column"
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    first_col][1]
                instance.content = self.dataset_df[
                    first_col].mean()
                instance.content_id = plot_index
                self.plots.append(instance)

            if formulas == "min_first":
                instance.title = "Lowest " + str(
                    first_col).lower()
                instance.sub_title = "Minium of " + str(
                    first_col).lower() + " column"
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    first_col][1]
                instance.content = self.dataset_df[
                    first_col].min()
                instance.content_id = plot_index
                self.plots.append(instance)

            if formulas == "max_first":
                instance.title = "Highest " + str(
                    first_col).lower()
                instance.sub_title = "Maximum of " + str(
                    first_col).lower() + " column"
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    first_col][1]
                instance.content = self.dataset_df[
                    first_col].max()
                instance.content_id = plot_index
                self.plots.append(instance)

            if formulas == "table_second_per_first":

                instance.title = self.remove_random_str(str(second_col)) + " per " + self.remove_random_str(str(first_col))
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    first_col][1]
                instance.content = self.dataset_df.groupby(
                    first_col)[second_col].agg(
                        ['sum','mean', 'min', 'max']).reset_index()
                instance.content.columns = instance.content.columns.str.replace(
                    self.random_str + "_", '')
                instance.content_id = plot_index
                self.plots.append(instance)

    def remove_random_str(self, name: str):
        print(name, self.random_str)
        return name.replace(self.random_str + "_", '').lower()
