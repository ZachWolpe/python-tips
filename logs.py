
# SECURITY LEVELS

# DEBUG     - for devs, troubleshoot and test
# INFO      - informational about current state
# WARNING   - system doesn't crash but could cause a problem. Example RAM limit approaching.
# ERROR     - couldn't do x, but system can still run
# CRITICAL  - whole system is impaired

import logging, coloredlogs

formatter   = logging.Formatter("[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S")
handler     = logging.FileHandler('log-data.log')
logger      = logging.getLogger('Custom Logger:')
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)
coloredlogs.install(level='DEBUG', logger=logger)

# Some examples.
logger.debug("this is a DEBUG message")
logger.info("this is an INFO message")
logger.warning("this is a WARNING message")
logger.error("this is an ERROR message")
logger.critical("this is a CRITCAL message")

