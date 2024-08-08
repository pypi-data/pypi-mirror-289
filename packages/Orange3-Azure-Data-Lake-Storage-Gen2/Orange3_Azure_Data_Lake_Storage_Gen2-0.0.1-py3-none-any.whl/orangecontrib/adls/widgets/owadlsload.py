#!/usr/bin/env python
# -*- coding: utf-8 -*-
from AnyQt.QtCore import Qt
from AnyQt.QtWidgets import QStyle, QSizePolicy
from Orange.data import Table
from Orange.data.io import TabReader, CSVReader, ExcelReader
from Orange.widgets import gui, settings
from Orange.widgets.widget import OWWidget, Msg, Output

import csv
import tempfile
import pickle
import os
from io import StringIO

from .azure_utils import AzureConnector

class OWADLSLoad(OWWidget):
    name = "ADLS Loader"
    description = "Opens a file via ADLS"
    icon = "icons/adls_load.svg"
    priority = 55
    keywords = "adls"

    class Outputs:
        data = Output("Table", Table)

    class Error(OWWidget.Error):
        sql_exception = Msg('Exception with adls: {} => {}')

    settingsHandler = settings.DomainContextHandler()
    account = settings.ContextSetting("orange3adlstest")
    login_type_index = settings.ContextSetting(1)
    login_token = settings.ContextSetting(os.environ.get('AZURE_TEST_TOKEN', ''))
    filesystem = settings.ContextSetting("testcontainer")
    directory = settings.ContextSetting("/")
    filetype_index = settings.ContextSetting(1)
    filename = settings.ContextSetting("iris.csv")

    want_control_area = False

    def __init__(self):
        super().__init__()
        self.result_set = None
        self.populate_mainArea()
        self.reload()

    def populate_mainArea(self):
        login_types = ('Entra', 'SAS')
        filetypes = ('csv','tab','xlsx','pckl')

        wb = gui.widgetBox(self.mainArea, orientation=Qt.Vertical)

        self.account_input = gui.lineEdit(wb, self, "account", label='Account Name')
        self.login_type_combo = gui.comboBox(wb, self, "login_type_index", items=login_types, minimumWidth=200, callback=self.login_type_changed, label='Login Type')
        self.token_input = gui.lineEdit(wb, self, "login_token", disabled=self.login_type_index == 0, label='Token')
        self.token_input.setEchoMode(self.token_input.Password)
        self.filesystem_input = gui.lineEdit(wb, self, "filesystem", label='File System')
        self.directory_input = gui.lineEdit(wb, self, "directory", label='Directory')
        self.filetype_combo = gui.comboBox(wb, self, "filetype_index", items=filetypes, minimumWidth=200, label='File Type')
        self.filepath_input = gui.lineEdit(wb, self, "filename", label='File Path')

        gui.button(wb, self, 'load', callback=self.load_adls,
            disabled=0, icon=self.style().standardIcon(QStyle.SP_DirOpenIcon),
            sizePolicy=(QSizePolicy.Maximum, QSizePolicy.Fixed)
        )

    def login_type_changed(self):
        enabled = self.login_type_index == 1
        self.token_input.setEnabled(enabled)

    def reload(self):
        pass

    def load_adls(self, event):
        if self.login_type_index == 0:
            ac = AzureConnector(self.account)
        else:
            ac = AzureConnector(self.account, self.login_token)
        data = ac.download_file(self.filesystem, self.directory, self.filename)
        if self.filetype_index == 0: # csv
            with StringIO(data.decode('UTF-8')) as fh:
                reader = csv.reader(fh, delimiter=CSVReader.DELIMITERS[0])
                table = TabReader.data_table(reader)
        elif self.filetype_index == 1: # tab
            with StringIO(data.decode('UTF-8')) as fh:
                reader = csv.reader(fh, delimiter=TabReader.DELIMITERS[0])
                table = TabReader.data_table(reader)
        elif self.filetype_index == 2: # excel
            with tempfile.NamedTemporaryFile(suffix='.xlsx') as f:
                f.write(data)
                f.flush()
                table = ExcelReader(f.name).read()
        elif self.filetype_index == 3: # pickle
            table = pickle.loads(data)

        self.Outputs.data.send(table)
