import pandas as pd
from .df_handler import DataFrameHandler
from .excel_handler import ExcelHandler
from .visual_handler import VisualizationHandler


class MyExcel:
    def __init__(self, dataframe: pd.DataFrame):
        self.df_handler = DataFrameHandler(dataframe)
        self.excel_handler = ExcelHandler(self.df_handler.get_dataframe())
        self.visualization_handler = VisualizationHandler(
            self.df_handler.get_dataframe()
        )

    def save(self, filename):
        """엑셀 파일 저장"""
        self.excel_handler.save(filename)

    def close(self):
        """엑셀 파일 닫기"""
        self.excel_handler.close()

    @property
    def df(self):
        """데이터프레임 접근"""
        return self.df_handler.df

    def __getattribute__(self, name):
        try:
            df_handler = super().__getattribute__("df_handler")
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
        """
        조건에 맞는 행 필터링. include와 exclude 조건을 구분

        Parameters:
        include (dict): 포함 조건을 나타내는 딕셔너리.
                        키는 컬럼명이고 값은 조건.
                        조건은 기본적으로 ('==', value) 형식의 튜플.
                        ('==', '!=', '<', '>', '<=', '>=', 'in', 'contains') 연산자 지원.
        exclude (dict): 제외 조건을 나타내는 딕셔너리.
                        키는 컬럼명이고 값은 조건.
                        조건은 기본적으로 ('!=', value) 형식의 튜플.
                        ('==', '!=', '<', '>', '<=', '>=', 'in', 'contains') 연산자 지원.

        Returns:
        DataFrame: 조건에 맞는 행들로 구성된 DataFrame

        Example Usage:

        # 포함 조건: column1이 'value1'인 행, column2가 5보다 큰 행
        include_conditions = {'column1': 'value1', 'column2': ('>', 5)}

        # 제외 조건: column3이 10 이하인 행, column4가 리스트 [1, 2, 3]에 포함된 행,
        #           column5가 'pattern'을 포함하는 문자열인 행
        exclude_conditions = {'column3': ('<=', 10), 'column4': ('in', [1, 2, 3]), 'column5': ('contains', 'pattern')}

        # 필터링 실행
        filtered_df = self.filter_rows(include=include_conditions, exclude=exclude_conditions)
        """
        query = []

        def build_condition(column, condition, is_exclude=False):
            operator, value = condition
            if operator in ("==", "!=", "<", ">", "<=", ">="):
                if is_exclude:
                    return f"({column} {invert_operator(operator)} {repr(value)})"
                else:
                    return f"({column} {operator} {repr(value)})"
            elif operator == "in":
                if is_exclude:
                    return f"(~{column}.isin({value}))"
                else:
                    return f"({column}.isin({value}))"
            elif operator == "contains":
                if is_exclude:
                    return f"(~{column}.str.contains({repr(value)}))"
                else:
                    return f"({column}.str.contains({repr(value)}))"
            else:
                raise ValueError(f"Unsupported operator: {operator}")

        def invert_operator(operator):
            return {"==": "!=", "!=": "==", "<": ">=", ">": "<=", "<=": ">", ">=": "<"}[
                operator
            ]

        if include:
            query += [
                (
                    build_condition(col, val)
                    if isinstance(val, tuple)
                    else build_condition(col, ("==", val))
                )
                for col, val in include.items()
            ]

        if exclude:
            query += [
                (
                    build_condition(col, val, is_exclude=True)
                    if isinstance(val, tuple)
                    else build_condition(col, ("!=", val))
                )
                for col, val in exclude.items()
            ]

        return self.df.query(" & ".join(query))

    def group_and_aggregate(self, group_by, **aggregations):
        """그룹화 및 집계"""
        return self.df_handler.group_and_aggregate(group_by, **aggregations)

    def fill_missing(self, strategy="mean", columns=None):
        """결측값 채우기"""
        return self.df_handler.fill_missing(strategy, columns)

    def normalize(self, columns=None):
        """정규화"""
        return self.df_handler.normalize(columns)

    # ExcelHandler 메서드들에 대한 래퍼
    def set_column_width(self, **kwargs):
        """컬럼 너비 설정"""
        self.excel_handler.set_column_width(**kwargs)

    def freeze_first_row(self):
        """첫 번째 행 고정"""
        self.excel_handler.freeze_first_row()

    def enable_autowrap(self):
        """자동 줄 바꿈 활성화"""
        self.excel_handler.enable_autowrap()

    def add_hyperlink(self, cell, url, display=None):
        """셀에 하이퍼링크 추가"""
        self.excel_handler.add_hyperlink(cell, url, display)

    def add_hyperlinks_to_column(self, column_name, urls, display_texts=None):
        """컬럼에 있는 각 셀에 하이퍼링크 추가"""
        self.excel_handler.add_hyperlinks_to_column(column_name, urls, display_texts)

    # VisualizationHandler 메서드들에 대한 래퍼
    def plot_histogram(self, column, bins=10, title=None):
        self.visualization_handler.plot_histogram(column, bins, title)

    def plot_boxplot(self, column, by=None, title=None):
        self.visualization_handler.plot_boxplot(column, by, title)

    def plot_scatter(self, x, y, hue=None, title=None):
        self.visualization_handler.plot_scatter(x, y, hue, title)

    def plot_heatmap(self, title=None):
        self.visualization_handler.plot_heatmap(title)

    def plot_bar(self, x, y, hue=None, title=None):
        self.visualization_handler.plot_bar(x, y, hue, title)

    def plot_line(self, x, y, hue=None, title=None):
        self.visualization_handler.plot_line(x, y, hue, title)
