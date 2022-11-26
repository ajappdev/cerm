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
        for element in self.decided_plots:
            plot_class = getattr(m04, list(element.keys())[0])
            instance = plot_class(
                element[list(element.keys())[0]][0],
                element[list(element.keys())[0]][1],
                element[list(element.keys())[0]][2],
                self.dataset_columns,
                self.random_str)

            formulas = instance.formulas
            if formulas == "sum_first":
                instance.title = "Total " + str(
                    element[list(element.keys())[0]][0]).lower()
                instance.sub_title = "Sum of " + str(
                    element[list(element.keys())[0]][0]).lower() + " column"
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    element[list(element.keys())[0]][0]][1]
                instance.content = self.dataset_df[
                    element[list(element.keys())[0]][0]].sum()
                self.plots.append(instance)

            if formulas == "avg_first":
                instance.title = "Average " + str(
                    element[list(element.keys())[0]][0]).lower()
                instance.sub_title = "Mean of " + str(
                    element[list(element.keys())[0]][0]).lower() + " column"
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    element[list(element.keys())[0]][0]][1]
                instance.content = self.dataset_df[
                    element[list(element.keys())[0]][0]].mean()
                self.plots.append(instance)

            if formulas == "min_first":
                instance.title = "Lowest " + str(
                    element[list(element.keys())[0]][0]).lower()
                instance.sub_title = "Minium of " + str(
                    element[list(element.keys())[0]][0]).lower() + " column"
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    element[list(element.keys())[0]][0]][1]
                instance.content = self.dataset_df[
                    element[list(element.keys())[0]][0]].min()
                self.plots.append(instance)

            if formulas == "max_first":
                instance.title = "Highest " + str(
                    element[list(element.keys())[0]][0]).lower()
                instance.sub_title = "Maximum of " + str(
                    element[list(element.keys())[0]][0]).lower() + " column"
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    element[list(element.keys())[0]][0]][1]
                instance.content = self.dataset_df[
                    element[list(element.keys())[0]][0]].max()
                self.plots.append(instance)