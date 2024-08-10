import logging

from datamanwithvan.transport import transport_adlsgen2
from datamanwithvan.transport import transport_hdfs
from datamanwithvan.transport import transport_local
from datamanwithvan.transport import transport_s3

# Section 25 : Before anything else, set up the logger...
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_format = logging.Formatter(
    '%(asctime)s - %(name)s (%(levelname)s) : %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)
try:
    file_handler = logging.FileHandler("/var/log/datamanwithvan/dmwv.log")
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s (%(levelname)s) : %(message)s')
    logger.addHandler(file_handler)
except Exception as e:
    logger.error(f"Error while trying to open log file: {e}")
console_handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
# End of Section 25


class Transport:
    """_summary_
    """

    task_metadata = {}
    config = None
    transport_adlsgen2 = transport_adlsgen2.Transportadlsgen2()
    transport_hdfs = transport_hdfs.Transporthdfs()
    transport_local = transport_local.Transportlocal()
    transport_s3 = transport_s3.Transports3()

    def __init__(self, task_metadata, config) -> None:
        self.task_metadata = task_metadata
        self.config = config

    def dummy(self):
        return True


if __name__ == "__main__":
    pass
