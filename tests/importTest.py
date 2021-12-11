import sys
sys.path.append(".")
# from app.use_cases.calcWeightForTasks import weight_tasks_class as w

import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
