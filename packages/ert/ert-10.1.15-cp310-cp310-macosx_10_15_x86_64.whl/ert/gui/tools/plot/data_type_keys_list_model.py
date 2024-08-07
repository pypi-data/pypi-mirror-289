from typing import List, Optional

from qtpy.QtCore import QAbstractItemModel, QModelIndex, Qt
from qtpy.QtGui import QColor, QIcon

from ert.gui.tools.plot.plot_api import PlotApiKeyDefinition


class DataTypeKeysListModel(QAbstractItemModel):
    DEFAULT_DATA_TYPE = QColor(255, 255, 255)
    HAS_OBSERVATIONS = QColor(237, 218, 116)
    GROUP_ITEM = QColor(64, 64, 64)

    def __init__(self, keys: List[PlotApiKeyDefinition]):
        QAbstractItemModel.__init__(self)
        self._keys = keys
        self.__icon = QIcon("img:star_filled.svg")

    def index(self, row, column, parent=None, *args, **kwargs):
        return self.createIndex(row, column)

    @staticmethod
    def parent(index=None):
        return QModelIndex()

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._keys)

    @staticmethod
    def columnCount(QModelIndex_parent=None, *args, **kwargs):
        return 1

    def data(self, index, role=None):
        assert isinstance(index, QModelIndex)

        if index.isValid():
            items = self._keys
            row = index.row()
            item = items[row]

            if role == Qt.DisplayRole:
                return item.key
            elif role == Qt.BackgroundRole and item.observations:
                return self.HAS_OBSERVATIONS

        return None

    def itemAt(self, index) -> Optional[PlotApiKeyDefinition]:
        assert isinstance(index, QModelIndex)

        if index.isValid():
            row = index.row()
            return self._keys[row]

        return None
