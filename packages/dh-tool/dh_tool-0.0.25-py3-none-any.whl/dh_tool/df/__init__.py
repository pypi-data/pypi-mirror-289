from .excel_handler import ExcelHandler
from .df_handler import DataFrameHandler
from .visual_handler import VisualizationHandler
from .my_excel import MyExcel as me

DEFAULT_WIDTH_CONFIG = {
    "Comments": 90,
    "BestSentence1": 20,
    "BestSentence2": 20,
    "FeedBack": 40,
    "timestamp": 20,
    "level": 10,
    "topic": 20,
    "message": 40,
    "description": 60,
    "traceback": 80,
}


__all__ = [
    "ExcelHandler",
    "DataFrameHandler",
    "VisualizationHandler",
    "me",
    "DEFAULT_WIDTH_CONFIG",
]
