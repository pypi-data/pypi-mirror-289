from .excel_handler import ExcelHandler
from .df_handler import DataFrameHandler
from .visual_handler import VisualizationHandler
from .my_excel import MyExcel as me

DEFAULT_WIDTH_CONFIG = {
    "Comments": {"width": 90},
    "BestSentence1": {"width": 20},
    "BestSentence2": {"width": 20},
    "FeedBack": {"width": 40},
    "timestamp": {"width": 20},
    "level": {"width": 10},
    "topic": {"width": 20},
    "message": {"width": 40},
    "description": {"width": 60},
    "traceback": {"width": 80},
}


__all__ = [
    "ExcelHandler",
    "DataFrameHandler",
    "VisualizationHandler",
    "me",
    "DEFAULT_WIDTH_CONFIG",
]
