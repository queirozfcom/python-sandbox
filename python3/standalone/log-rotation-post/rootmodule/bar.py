import logging

logger = logging.getLogger(__name__)
# add more information to the messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# stream handler = stdout
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

def bar():
    logger.info("bar() method called")
	
