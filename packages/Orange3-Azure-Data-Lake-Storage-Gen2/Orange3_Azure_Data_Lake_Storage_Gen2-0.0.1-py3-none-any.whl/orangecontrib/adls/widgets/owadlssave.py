#!/usr/bin/env python
# -*- coding: utf-8 -*-
from AnyQt.QtCore import Qt
from Orange.data import Table
from Orange.data.io import TabReader, CSVReader, ExcelReader
from Orange.data.io import PICKLE_PROTOCOL
from Orange.widgets import gui, settings
from Orange.widgets.widget import OWWidget, Msg, Input

from io import StringIO
import tempfile
import csv
import os
import pickle

from .azure_utils import AzureConnector

class OWADLSSave(OWWidget):
    name = "ADLS Upload"
    description = "Uploads a table to ADLS"
    icon = "icons/adls_save.svg"
    priority = 55
    keywords = "adls"

    class Inputs:
        data = Input("Table", Table)

    class Error(OWWidget.Error):
        sql_exception = Msg('Exception with adls: {} => {}')

    settingsHandler = settings.DomainContextHandler()
    account = settings.ContextSetting("orange3adlstest")
    login_type_index = settings.ContextSetting(1)
    login_token = settings.ContextSetting(os.environ.get('AZURE_TEST_TOKEN', ''))
    filesystem = settings.ContextSetting("testcontainer")
    directory = settings.ContextSetting("/")
    filetype_index = settings.ContextSetting(3)
    filename = settings.ContextSetting("iris.pckl")

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

    def login_type_changed(self):
        enabled = self.login_type_index == 1
        self.token_input.setEnabled(enabled)

    def reload(self):
        pass

    def convert_table(self, reader, filename: str, table: Table) -> str:
        fh = StringIO()
        writer = csv.writer(fh, delimiter=reader.DELIMITERS[0])
        reader.write_headers(writer.writerow, table, True)
        reader.write_data(writer.writerow, table)
        reader.write_table_metadata(filename, table)
        data = fh.getvalue()
        fh.close()
        return data

    def _to_tab(self, filename: str, table: Table) -> str:
        return self.convert_table(TabReader, filename, table)

    def _to_csv(self, filename: str, table: Table) -> str:
        return self.convert_table(CSVReader, filename, table)

    def _to_pickle(self, filename: str, table: Table) -> bytes:
        return pickle.dumps(table, protocol=PICKLE_PROTOCOL)

    def _to_excel(self, filename: str, table: Table) -> bytes:
        with tempfile.NamedTemporaryFile() as f:
            ExcelReader.write_file(f.name, table)
            f.flush()
            with open(f.name, 'rb') as fh:
                data = fh.read()
                return data


    @Inputs.data
    def dataset(self, data):
        self.data = data
        self.on_new_input()

    def on_new_input(self):
        if self.login_type_index == 0:
            ac = AzureConnector(self.account)
        else:
            ac = AzureConnector(self.account, self.login_token)

        if self.filetype_index == 0:
            data = self._to_csv(self.filename, self.data)
        elif self.filetype_index == 1:
            data = self._to_tab(self.filename, self.data)
        elif self.filetype_index == 2:
            data = self._to_excel(self.filename, self.data)
        elif self.filetype_index == 3:
            data = self._to_pickle(self.filename, self.data)

        ac.upload_file(self.filesystem, self.directory,
            self.filename, data)
