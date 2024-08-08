import pandas as pd


class DataFrameHandler:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

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
        query_str = " & ".join(query)
        return self.df.query(query_str)

    def group_and_aggregate(self, group_by, **aggregations):
        """그룹화 및 집계"""
        return self.df.groupby(group_by).agg(aggregations)

    def fill_missing(self, strategy="mean", columns=None):
        """결측값 채우기"""
        if columns is None:
            columns = self.df.select_dtypes(include="number").columns
        else:
            columns = self.df[columns].select_dtypes(include="number").columns

        if strategy == "mean":
            self.df[columns] = self.df[columns].fillna(self.df[columns].mean())
        elif strategy == "median":
            self.df[columns] = self.df[columns].fillna(self.df[columns].median())
        elif strategy == "mode":
            self.df[columns] = self.df[columns].fillna(self.df[columns].mode().iloc[0])
        elif strategy == "ffill":
            self.df[columns] = self.df[columns].fillna(method="ffill")
        elif strategy == "bfill":
            self.df[columns] = self.df[columns].fillna(method="bfill")
        return self.df

    def normalize(self, columns=None):
        """정규화"""
        if columns is None:
            columns = self.df.select_dtypes(include="number").columns
        else:
            columns = self.df[columns].select_dtypes(include="number").columns

        self.df[columns] = (self.df[columns] - self.df[columns].mean()) / self.df[
            columns
        ].std()
        return self.df

    def get_dataframe(self):
        """데이터프레임 반환"""
        return self.df
