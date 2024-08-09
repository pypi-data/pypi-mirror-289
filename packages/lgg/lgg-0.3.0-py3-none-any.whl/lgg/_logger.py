from logging import DEBUG, INFO, Formatter, StreamHandler, FileHandler, getLogger
import sys

__all__ = ["get_logger"]

DEFAULT_NAME = "nameless"
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[;%dm"
BOLD_COLOR_SEQ = "\033[1;%dm"

_COLORS = {
    "WARNING": YELLOW,
    "INFO": GREEN,
    "DEBUG": BLUE,
    "CRITICAL": YELLOW,
    "ERROR": RED,
}


class MyHandler(StreamHandler):
    def __init__(self):
        super().__init__()
        self.stream = sys.stdout


class _ColoredFormatter(Formatter):
    def __init__(self, msg, use_color=True):
        Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        if self.use_color:
            record.levelname = (
                COLOR_SEQ % (30 + _COLORS[record.levelname])
                + record.levelname
                + RESET_SEQ
            )

            if record.name == DEFAULT_NAME:
                record.filename = (
                    BOLD_COLOR_SEQ % (30 + RED) + record.filename + RESET_SEQ
                )
            else:
                record.name = BOLD_COLOR_SEQ % (30 + RED) + record.name + RESET_SEQ

        return Formatter.format(self, record)


def get_logger(name=DEFAULT_NAME, filename=None, use_color=True):
    """Get a custom logger.

    Args:
        name (str, optional): The name of the logger. Defaults to DEFAULT_NAME.
        filename (str, optional): The filename to save the log. Defaults to None.
        use_color (bool, optional): Whether to use color in the console. Defaults to True.

    Returns:
        logging.Logger: The logger.
    """
    logger = getLogger(name)

    cond = True
    for handler in logger.handlers:
        if isinstance(handler, MyHandler):
            cond = False

    if cond:
        # stream handler
        if logger.name == "nameless":
            fmt = (
                "%(asctime)s - %(filename)s:%(lineno)s " "- %(levelname)s:  %(message)s"
            )
        else:
            fmt = "%(asctime)s - %(name)s " "- %(levelname)s:  %(message)s"
            
        # add file handler if filename is provided
        if filename:
            file_handler = FileHandler(filename)
            file_handler.setFormatter(Formatter(fmt))  # Use standard formatter for file
            logger.addHandler(file_handler)
            
        handler = MyHandler()
        handler.setFormatter(_ColoredFormatter(fmt, use_color))  # Use colored formatter for console
        logger.addHandler(handler)

    return logger
