import pandas as pd


class DataFrameHandler:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def filter_rows(self, **conditions):
        """조건에 맞는 행 필터링"""
        query = " & ".join(
            [
                (
                    f"({col}=={repr(val)})"
                    if not isinstance(val, list)
                    else f"({col}.isin({val}))"
                )
                for col, val in conditions.items()
            ]
        )
        return self.df.query(query)

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
