from typing import Optional

import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from engine.settings import get_settings, Scopes


def get_data_google_sheets(sample_spreadsheet_id: str, tab_index: Optional[int] = None):
    values = []
    settings = get_settings()
    scopes = [
        Scopes.SPREADSHEET_SCOPE,
    ]
    credentials = Credentials.from_service_account_file(
        settings.JSON_PATH.__str__(), scopes=scopes
    )
    gc = gspread.authorize(credentials).open_by_key(sample_spreadsheet_id)
    if tab_index:
        values.append(gc.get_worksheet(tab_index).get_all_values())
    else:
        for sheet in gc.worksheets():
            values.append(sheet.get_all_values())
    tables = []
    for row in values:
        dfi = pd.DataFrame(row)
        dfi.columns = dfi.iloc[0]
        dfi.drop(dfi.index[0], inplace=True)
        tables.append(dfi)
    return tables
