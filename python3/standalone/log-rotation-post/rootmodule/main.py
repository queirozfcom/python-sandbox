import logging

from rootmodule.bar import bar
from rootmodule.baz import baz
from rootmodule.quux import quux
from rootmodule.abc import abc

#logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.error("Error message from main.py")


abc()

