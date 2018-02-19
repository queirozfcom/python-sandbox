import logging
import traceback

logger = logging.getLogger(__name__)

# add more information to the messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# stream handler prints errors to STDERR, which defaults to STDOUT
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger.addHandler(handler)

def abc():
    try:
    	raise Exception("some exception")
    except Exception:
        tb = traceback.format_exc() 
        logger.error(tb) 
