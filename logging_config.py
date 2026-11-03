import logging.config
import datetime


BEIJING_TZ = datetime.timezone(datetime.timedelta(hours=8))


def beijing_time_converter(timestamp):
    """将时间转换为北京时间"""
    return datetime.datetime.fromtimestamp(timestamp, tz=BEIJING_TZ).timetuple()


class BeijingTimeFormatter(logging.Formatter):
    """日志时间使用北京时间 (Actions 运行环境是 UTC 时区)。

    dictConfig 会忽略 formatter 配置中的 converter 字段, 所以需要通过子类指定。
    """

    converter = staticmethod(beijing_time_converter)


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "()": BeijingTimeFormatter,
            "fmt": "%(asctime)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}


def init_logger():
    """初始化日志"""
    logging.config.dictConfig(LOGGING_CONFIG)
    return logging.getLogger()
