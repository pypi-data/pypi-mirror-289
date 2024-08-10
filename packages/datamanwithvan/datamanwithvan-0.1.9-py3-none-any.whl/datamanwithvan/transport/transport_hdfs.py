import logging

from datetime import datetime, timezone

# Section 27 : Before anything else, set up the logger...
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
# End of Section 27


class Transporthdfs:
    """_summary_
    """
    def __init__(self) -> None:
        pass

    def upload(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        operation = {
            "name": "upload",
            "status": -1,
            "started": datetime.now(timezone.utc).timestamp(),
            "finished": "",
            "comments": ""
        }

        logger.info("upload() is not implemented yet")

        return operation

    def download(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        operation = {
            "name": "download",
            "status": -1,
            "started": datetime.now(timezone.utc).timestamp(),
            "finished": "",
            "comments": ""
        }

        logger.info("download() is not implemented yet")

        return operation

    def upload_via_proxy(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        operation = {
            "name": "upload_via_proxy",
            "status": -1,
            "started": datetime.now(timezone.utc).timestamp(),
            "finished": "",
            "comments": ""
        }

        logger.info("upload_via_proxy() is not implemented yet")

        return operation

    def download_via_proxy(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        operation = {
            "name": "download_via_proxy",
            "status": -1,
            "started": datetime.now(timezone.utc).timestamp(),
            "finished": "",
            "comments": ""
        }

        logger.info("upload() is not implemented yet")

        return operation


if __name__ == "__main__":
    pass
