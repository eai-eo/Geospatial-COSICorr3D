"""
# Author : Saif Aati
# Contact: SAIF AATI  <saif@caltech.edu> <saifaati@gmail.com>
# Copyright (C) 2022
"""
import logging
import os, sys, re
from datetime import datetime
from typing import Optional

from geoCosiCorr3D.geoCore.constants import SOFTWARE


class geoCosiCorr3DLog:
    def __init__(self, log_prefix: str, log_dir: Optional[str] = None):
        if log_dir is None:
            log_dir = os.getcwd()

        # TODO: this is a bit of a hack. Cosicorr should use named loggers for better log handling.
        root = logging.getLogger()
        already_configured = bool(root.handlers)
        if already_configured:
            return

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        now = datetime.now()
        GENERATION_TIME = now.strftime("%Y-%m-%d-T%H%M%S")
        log_prefix = re.sub(r"\s+", "_", log_prefix.strip())  # Strip out any spaces in the filename
        logfile = os.path.join(log_dir, log_prefix + "_" + GENERATION_TIME + '.log')
        print(f"Logfile will be at {logfile}")
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s : %(levelname)s : %(message)s",
            handlers=[
                logging.FileHandler(logfile, delay=True),  # delay means don't create the file until you have something to write.
                logging.StreamHandler(sys.stdout)
            ]
        )
