import os
import datetime


class Gateway:
    def __init__(self):
        pass

    def log(self, message: str):
        yymmdd_hhmmss = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        yymmdd = datetime.datetime.now().strftime("%Y%m%d")
        classname = self.__class__.__name__
        path = os.getenv("GATEWAY_LOG")
        file_name = f"{path}/{yymmdd}.log"
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(f"{yymmdd_hhmmss} {classname} {message}\n")
