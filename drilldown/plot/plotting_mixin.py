class Plotting2dMixin:
    def __init__(self):
        pass

    def scatter_plot(self, x, y, **kwargs):
        from .plotly_plots import ScatterPlot

        fig = ScatterPlot(self.data, x, y, **kwargs)

        fig.connect_layer(self)
        fig.ids = self.ids

        return fig

    def scatter_plot_from_selection(self, x, y, **kwargs):
        from .plotly_plots import ScatterPlot

        fig = ScatterPlot(self.selected_data, x, y, **kwargs)

        fig.connect_layer(self, relationship="selected")
        fig.ids = self.selected_ids

        return fig

    def scatter_plot_from_filter(self, x, y, **kwargs):
        from .plotly_plots import ScatterPlot

        fig = ScatterPlot(self.filtered_data, x, y, **kwargs)

        fig.connect_layer(self, relationship="filtered")
        fig.ids = self.filtered_ids

        return fig

    def scatter_3d_plot(self, x, y, z, **kwargs):
        from .plotly_plots import Scatter3dPlot

        fig = Scatter3dPlot(self.data, x, y, z, **kwargs)

        fig.connect_layer(self)
        fig.ids = self.ids

        return fig

    def scatter_3d_plot_from_selection(self, x, y, z, **kwargs):
        from .plotly_plots import Scatter3dPlot

        fig = Scatter3dPlot(self.selected_data, x, y, z, **kwargs)

        fig.connect_layer(self, relationship="selected")
        fig.ids = self.selected_ids

        return fig

    def scatter_3d_plot_from_filter(self, x, y, z, **kwargs):
        from .plotly_plots import Scatter3dPlot

        fig = Scatter3dPlot(self.filtered_data, x, y, z, **kwargs)

        fig.connect_layer(self, relationship="filtered")
        fig.ids = self.filtered_ids

        return fig

    def scatter_ternary_plot(self, a, b, c, **kwargs):
        from .plotly_plots import ScatterTernaryPlot

        fig = ScatterTernaryPlot(self.data, a, b, c, **kwargs)

        fig.connect_layer(self)
        fig.ids = self.ids

        return fig

    def scatter_ternary_plot_from_selection(self, a, b, c, **kwargs):
        from .plotly_plots import ScatterTernaryPlot

        fig = ScatterTernaryPlot(self.selected_data, a, b, c, **kwargs)

        fig.plotter = self

        fig.connect_layer(self, relationship="selected")
        fig.ids = self.selected_ids

        return fig

    def scatter_ternary_plot_from_filter(self, a, b, c, **kwargs):
        from .plotly_plots import ScatterTernaryPlot

        fig = ScatterTernaryPlot(self.filtered_data, a, b, c, **kwargs)

        fig.plotter = self

        fig.connect_layer(self, relationship="filtered")
        fig.ids = self.filtered_ids

        return fig

    def scatter_dimensions_plot(self, dimensions, **kwargs):
        from .plotly_plots import ScatterDimensionsPlot

        fig = ScatterDimensionsPlot(self.data, dimensions, **kwargs)

        fig.connect_layer(self)
        fig.ids = self.ids

        return fig

    def scatter_dimensions_plot_from_selection(self, dimensions, **kwargs):
        from .plotly_plots import ScatterDimensionsPlot

        fig = ScatterDimensionsPlot(self.selected_data, dimensions, **kwargs)

        fig.plotter = self

        fig.connect_layer(self, relationship="selected")
        fig.ids = self.selected_ids

        return fig

    def scatter_dimensions_plot_from_filter(self, dimensions, **kwargs):
        from .plotly_plots import ScatterDimensionsPlot

        fig = ScatterDimensionsPlot(self.filtered_data, dimensions, **kwargs)

        fig.plotter = self

        fig.connect_layer(self, relationship="filtered")
        fig.ids = self.filtered_ids

        return fig

    def bar_plot(self, x, y, **kwargs):
        from .plotly_plots import BarPlot

        fig = BarPlot(self.data, x, y, **kwargs)

        fig.connect_layer(self)
        fig.ids = self.ids

        return fig

    def bar_plot_from_selection(self, x, y, **kwargs):
        from .plotly_plots import BarPlot

        fig = BarPlot(self.selected_data, x, y, **kwargs)

        fig.plotter = self

        fig.connect_layer(self, relationship="selected")
        fig.ids = self.selected_ids

        return fig

    def bar_plot_from_filter(self, x, y, **kwargs):
        from .plotly_plots import BarPlot

        fig = BarPlot(self.filtered_data, x, y, **kwargs)

        fig.plotter = self

        fig.connect_layer(self, relationship="filtered")
        fig.ids = self.filtered_ids

        return fig

    def histogram(self, x, **kwargs):
        from .plotly_plots import Histogram

        fig = Histogram(self.data, x, **kwargs)

        fig.connect_layer(self)
        fig.ids = self.ids

        return fig

    def histogram_from_selection(self, x, **kwargs):
        from .plotly_plots import Histogram

        fig = Histogram(self.selected_data, x, **kwargs)

        fig.plotter = self

        fig.connect_layer(self, relationship="selected")
        fig.ids = self.selected_ids

        return fig

    def histogram_from_filter(self, x, **kwargs):
        from .plotly_plots import Histogram

        fig = Histogram(self.filtered_data, x, **kwargs)

        fig.plotter = self

        fig.connect_layer(self, relationship="filtered")
        fig.ids = self.filtered_ids

        return fig
