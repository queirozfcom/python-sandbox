import logging,os
import rootmodule
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

output_file = os.path.dirname(rootmodule.__file__)+"/output-rot.log"

# logs will be written to the output_file until it 
# reaches 1000000 bytes = 1MB, then a new file will be created
# and the old file will be renamed to output_rot.log.1
handler = RotatingFileHandler(output_file,maxBytes=1000000, backupCount=5)

handler.setFormatter(formatter)

logger.addHandler(handler)

def quux():
    logger.warn("method quux called")
