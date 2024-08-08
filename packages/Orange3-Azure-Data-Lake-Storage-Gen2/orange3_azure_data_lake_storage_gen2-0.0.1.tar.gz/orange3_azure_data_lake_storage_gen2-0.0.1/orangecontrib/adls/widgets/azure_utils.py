#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from azure.storage.filedatalake import (
    DataLakeServiceClient
)
from azure.identity import DefaultAzureCredential

class AzureConnector:

    def __init__(self, account_name: str, sas_token: str = None):
        if sas_token:
            self.service_client = self.get_service_client_sas(account_name, sas_token)
        else:
            self.service_client = self.get_service_client_token_credential(account_name)


    def get_service_client_token_credential(self, account_name: str) -> DataLakeServiceClient:
        account_url = f"https://{account_name}.dfs.core.windows.net"
        token_credential = DefaultAzureCredential()

        service_client = DataLakeServiceClient(account_url, credential=token_credential)

        return service_client

    def get_service_client_sas(self, account_name: str, sas_token: str) -> DataLakeServiceClient:
        account_url = f"https://{account_name}.dfs.core.windows.net"

        # The SAS token string can be passed in as credential param or appended to the account URL
        service_client = DataLakeServiceClient(account_url, credential=sas_token)

        return service_client

    def download_file(self, filesystem:str, directory:str, file_name: str) -> str:
        directory_client = self.service_client.get_directory_client(
            filesystem, directory)
        file_client = directory_client.get_file_client(file_name)
        download = file_client.download_file()
        data = download.readall()
        return data

    def upload_file(self,
        filesystem:str, directory:str,
        file_name: str, data: bytes
    ):
        directory_client = self.service_client.get_directory_client(
            filesystem, directory)
        file_client = directory_client.get_file_client(file_name)
        file_client.upload_data(data, overwrite=True)
