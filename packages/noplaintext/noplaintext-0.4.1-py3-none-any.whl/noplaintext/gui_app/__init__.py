# This package is intended to be run as a standalone application.
# Do not import modules from this package into other scripts.

import logging

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from .gui_app import GuiApp