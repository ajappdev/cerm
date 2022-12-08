import pandas as pd
import app.m04_plots as m04
import app.m00_common as m00
class DrawPlots:

    def __init__(
            self,
            dataset_df: pd.DataFrame(),
            decided_plots: list,
            dataset_columns: dict,
            category_columns: dict,
            month_columns: dict,
            random_str: str):
        """
        """
        self.dataset_df = dataset_df
        self.decided_plots = decided_plots
        self.random_str = random_str
        self.dataset_columns = dataset_columns
        self.category_columns = category_columns
        self.month_columns = month_columns
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
                self.category_columns,
                self.month_columns,
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

            if formulas == "plot_second_per_first":

                instance.title = self.remove_random_str(str(second_col)) + " per " + self.remove_random_str(str(first_col))
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    first_col][1]
                instance.content = self.dataset_df.groupby(
                    first_col)[second_col].agg(
                        ['sum','mean', 'min', 'max']).reset_index()
                instance.content = instance.content.sort_values(by=['sum'], ascending=False)
                instance.content['display_column'] = ""
                instance.content['sort_rank'] = 0
                index_display = 0
                for index, row in instance.content.iterrows():
                    index_display += 1
                    if index_display <= m00.OTHER_SECOND_PER_FIRST_THRESHOLD:
                        instance.content.loc[index, 'display_column'] = instance.content.loc[index, str(first_col)]
                    else:
                        instance.content.loc[index, 'display_column'] = "Other"
                    if str(instance.content.loc[index, 'display_column']).lower() == "other":
                        instance.content.loc[index, 'sort_rank'] = 1
                instance.content = instance.content.groupby(
                    'display_column').agg({'sum':'sum', 'mean':'mean','min':'min','max':'max', 'sort_rank': 'sum'}).reset_index()
                instance.content.columns = instance.content.columns.str.replace(
                    self.random_str + "_", '')      
                instance.content_id = plot_index
                instance.content = instance.content.sort_values(by=['sort_rank', 'sum'], ascending=[True, False])
                instance.content = instance.content.drop('sort_rank', axis=1)
                instance.content = instance.content.rename(columns = {'display_column':self.remove_random_str(str(first_col))})

                total_sum_column = instance.content['sum'].sum()
                if total_sum_column > 0:
                    instance.content['perc_pie_chart'] = (instance.content['sum'] / total_sum_column)
                else:
                    instance.content['perc_pie_chart'] = 0
                instance.pie_chart_labels = instance.content[
                    self.remove_random_str(str(first_col))].tolist()
                instance.pie_chart_values = instance.content['perc_pie_chart'].tolist()

                self.plots.append(instance)

            if formulas == "monthly_amount":
                instance.title = self.remove_random_str(str(first_col)) + " per month"
                instance.unit = "Unit"
                instance.color = self.dataset_columns[
                    first_col][1]
                instance.content = self.dataset_df.groupby(
                    second_col)[first_col].agg(
                        ['sum']).reset_index()
                instance.content.columns = [self.remove_random_str(str(second_col)), self.remove_random_str(str(first_col))]
                instance.content = instance.content.sort_values(by=[self.remove_random_str(str(second_col))], ascending=[False])
                instance.content_id = plot_index
                instance.pie_chart_labels = instance.content[
                    self.remove_random_str(str(second_col))].tolist()
                instance.pie_chart_values = instance.content[
                    self.remove_random_str(str(first_col))].tolist()
                instance.pie_chart_labels.reverse()
                instance.pie_chart_values.reverse()
                self.plots.append(instance)

    def remove_random_str(self, name: str):
        return name.replace(self.random_str + "_", '').lower()
