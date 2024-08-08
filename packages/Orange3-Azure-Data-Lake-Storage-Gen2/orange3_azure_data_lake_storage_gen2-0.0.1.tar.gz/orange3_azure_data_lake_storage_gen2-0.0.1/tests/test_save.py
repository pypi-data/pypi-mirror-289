# -*- coding: utf-8 -*-

from Orange.data import Table
from Orange.widgets.utils.widgetpreview import WidgetPreview
from orangecontrib.adls.widgets.owadlssave import OWADLSSave

table = Table("iris")
WidgetPreview(OWADLSSave).run(input_data=table)
