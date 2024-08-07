from typing import TYPE_CHECKING

from qtpy.QtGui import QColor
from qtpy.QtWidgets import QHBoxLayout

from ert.gui.tools.plot import ColorBox
from ert.gui.tools.plot import style_chooser as sc

from .customization_view import CustomizationView, WidgetProperty

if TYPE_CHECKING:
    from ert.gui.plottery import PlotConfig


class StyleCustomizationView(CustomizationView):
    default_style = WidgetProperty()
    history_style = WidgetProperty()
    observs_style = WidgetProperty()
    color_cycle = WidgetProperty()
    observs_color = WidgetProperty()

    def __init__(self):
        CustomizationView.__init__(self)

        layout = QHBoxLayout()

        self.addRow("", layout)
        self.addStyleChooser(
            "default_style", "Default", "Line and marker style for default lines."
        )
        self.addStyleChooser(
            "history_style", "History", "Line and marker style for the history line."
        )
        self.addStyleChooser(
            "observs_style",
            "Observation",
            "Line and marker style for the observation line.",
            line_style_set=sc.STYLESET_TOGGLE,
        )

        self["default_style"].createLabelLayout(layout)

        self.addSpacing(10)

        color_layout = QHBoxLayout()

        self._color_boxes = []
        for name in ["#1", "#2", "#3", "#4", "#5"]:
            color_box = self.createColorBox(name)
            self._color_boxes.append(color_box)
            color_layout.addWidget(color_box)

        self.addRow("Color cycle", color_layout)
        self.updateProperty(
            "color_cycle",
            StyleCustomizationView.getColorCycle,
            StyleCustomizationView.setColorCycle,
        )

        self._observs_color_box = self.createColorBox("observations_color")
        self.addRow("Observations color", self._observs_color_box)
        self.updateProperty(
            "observs_color",
            StyleCustomizationView.getObservationsColor,
            StyleCustomizationView.setObservationsColor,
        )

    def getObservationsColor(self):
        return str(self._observs_color_box.color.name())

    def setObservationsColor(self, name):
        self._observs_color_box.color = name

    @staticmethod
    def createColorBox(name):
        color_box = ColorBox(QColor(255, 255, 255), 20)
        color_box.setToolTip(name)
        return color_box

    def getColorCycle(self):
        colors = []
        for color_box in self._color_boxes:
            colors.append(str(color_box.color.name()))

        return colors

    def setColorCycle(self, color_cycle):
        for index, color in enumerate(color_cycle):
            if 0 <= index < len(self._color_boxes):
                color_box = self._color_boxes[index]
                color_box.color = color

    def applyCustomization(self, plot_config: "PlotConfig"):
        plot_config.setDefaultStyle(self.default_style)
        plot_config.setHistoryStyle(self.history_style)
        plot_config.setObservationsStyle(self.observs_style)
        plot_config.setObservationsColor(self.observs_color)
        plot_config.setLineColorCycle(self.color_cycle)

    def revertCustomization(self, plot_config: "PlotConfig"):
        self.default_style = plot_config.defaultStyle()
        self.history_style = plot_config.historyStyle()
        self.observs_style = plot_config.observationsStyle()
        self.observs_color = plot_config.observationsColor()
        self.color_cycle = plot_config.lineColorCycle()
