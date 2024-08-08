import pandas as pd
from .df_handler import DataFrameHandler
from .excel_handler import ExcelHandler
from .visual_handler import VisualizationHandler


class MyExcel:
    def __init__(self, dataframe: pd.DataFrame, sheet_name: str = "Sheet1"):
        self.sheets = {sheet_name: DataFrameHandler(dataframe)}
        self.current_sheet = sheet_name
        self.excel_handler = ExcelHandler(
            self.sheets[self.current_sheet].get_dataframe()
        )
        self.visualization_handler = VisualizationHandler(
            self.sheets[self.current_sheet].get_dataframe()
        )

    def add_sheet(self, sheet_name: str, dataframe: pd.DataFrame):
        """새 시트 추가"""
        self.sheets[sheet_name] = DataFrameHandler(dataframe)

    def remove_sheet(self, sheet_name: str):
        """시트 제거"""
        if sheet_name in self.sheets:
            del self.sheets[sheet_name]
            if self.current_sheet == sheet_name:
                self.current_sheet = (
                    list(self.sheets.keys())[0] if self.sheets else None
                )

    def select_sheet(self, sheet_name: str):
        """시트 선택"""
        if sheet_name in self.sheets:
            self.current_sheet = sheet_name
            self.excel_handler = ExcelHandler(
                self.sheets[self.current_sheet].get_dataframe()
            )
            self.visualization_handler = VisualizationHandler(
                self.sheets[self.current_sheet].get_dataframe()
            )
        else:
            raise ValueError(f"Sheet '{sheet_name}' does not exist.")

    def save(self, filename):
        """엑셀 파일 저장"""
        with pd.ExcelWriter(filename) as writer:
            for sheet_name, handler in self.sheets.items():
                handler.get_dataframe().to_excel(writer, sheet_name=sheet_name)
        self.excel_handler.save(filename)

    def close(self):
        """엑셀 파일 닫기"""
        self.excel_handler.close()

    @property
    def df(self):
        """현재 선택된 시트의 데이터프레임 접근"""
        return self.sheets[self.current_sheet].df

    def __getattribute__(self, name):
        try:
            sheets = super().__getattribute__("sheets")
            df_handler = sheets[super().__getattribute__("current_sheet")]
            df = df_handler.df
            if hasattr(df, name):
                return getattr(df, name)
            return super().__getattribute__(name)
        except AttributeError:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )

    def __getitem__(self, key):
        return self.df[key]

    # DataFrameHandler 메서드들에 대한 래퍼
    def filter_rows(self, include=None, exclude=None):
        """조건에 맞는 행 필터링. include와 exclude 조건을 구분"""
        return self.sheets[self.current_sheet].filter_rows(include, exclude)
