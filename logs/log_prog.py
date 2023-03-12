import logging

def logger_error(log):
    path = 'storage\logging_shortner.log'
    logging.basicConfig(level=logging.INFO, filename=path, encoding='utf-8',
                        format='%(asctime)s  %(levelname)s  %(message)s')
    logging.exception(log)


def logger_info(log):
    path = 'storage\logging_shortner.log'
    logging.basicConfig(level=logging.INFO, filename=path, encoding='utf-8',
                        format='%(asctime)s  %(levelname)s  %(message)s')
    logging.info(log)