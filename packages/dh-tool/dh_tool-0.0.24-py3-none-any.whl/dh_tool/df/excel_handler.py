import pandas as pd

from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Alignment


class ExcelHandler:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
        self.workbook = Workbook()
        self.worksheet = self.workbook.active
        # 데이터프레임을 엑셀 시트에 추가
        for r in dataframe_to_rows(self.df, index=False, header=True):
            self.worksheet.append(r)

    def set_column_width(self, **kwargs):
        """컬럼 너비 설정"""
        for column, width in kwargs.items():
            col_idx = self.df.columns.get_loc(column) + 1
            col_letter = chr(64 + col_idx)
            self.worksheet.column_dimensions[col_letter].width = width

    def freeze_first_row(self):
        """첫 번째 행 고정"""
        self.worksheet.freeze_panes = self.worksheet["A2"]

    def enable_autowrap(self):
        """자동 줄 바꿈 활성화"""
        for row in self.worksheet.iter_rows():
            for cell in row:
                cell.alignment = Alignment(wrap_text=True)

    def add_hyperlink(self, cell, url, display=None):
        """셀에 하이퍼링크 추가"""
        self.worksheet[cell].hyperlink = url
        self.worksheet[cell].value = display if display else url
        self.worksheet[cell].style = "Hyperlink"

    def add_hyperlinks_to_column(self, column_name, urls, display_texts=None):
        """컬럼에 있는 각 셀에 하이퍼링크 추가"""
        if len(urls) != len(self.df):
            raise ValueError(
                "The length of the URL list must match the length of the dataframe."
            )

        if display_texts and len(display_texts) != len(self.df):
            raise ValueError(
                "The length of the display_texts list must match the length of the dataframe."
            )

        col_idx = self.df.columns.get_loc(column_name) + 1
        for i, url in enumerate(urls, start=2):  # start=2 to account for header row
            cell = f"{chr(64 + col_idx)}{i}"
            display = display_texts[i - 2] if display_texts else None
            self.add_hyperlink(cell, url, display)

    def save(self, filename):
        """엑셀 파일 저장"""
        self.workbook.save(filename)

    def close(self):
        """엑셀 파일 닫기"""
        del self.workbook

    def __del__(self):
        self.close()
