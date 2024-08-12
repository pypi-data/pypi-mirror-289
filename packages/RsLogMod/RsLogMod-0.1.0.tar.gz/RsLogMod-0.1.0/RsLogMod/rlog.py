from RsLogMod.bin.logger import RsLogger


def rlog(log_file_name: str, log_level: int, log_entry: str):
    logger = RsLogger(log_name=log_file_name, log_level=log_level, log_entry=log_entry)
    logger.log()
