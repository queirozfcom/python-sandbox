import logging,os
import rootmodule

logger = logging.getLogger(__name__)

# add more information to the messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create a file in the root module directory
output_file = os.path.dirname(rootmodule.__file__)+"/output.log"

handler = logging.FileHandler(output_file)
handler.setFormatter(formatter)

# by default, the level is WARN
logger.setLevel(logging.INFO)

logger.addHandler(handler)

def baz():
    logger.info("method baz() called in rootmodule.baz ")
