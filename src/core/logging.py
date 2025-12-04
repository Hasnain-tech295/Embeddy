# logging/format helpers

# import logging
# import os
# import sys

# from . import config

# # logging formatters
# FORMATTERS = {
#     'default': logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s'),
#     'simple': logging.Formatter('%(levelname)s %(name)s: %(message)s'),
#     'debug': logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s'),
#     'verbose': logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s'),
#     'timestamp': logging.Formatter('%(asctime)s %(message)s'),
#     'message': logging.Formatter('%(message)s'),
# }

# # logging handlers
# HANDLERS = {
#     'default': logging.StreamHandler(sys.stdout),
#     'file': logging.FileHandler(os.path.join(config.LOG_DIR, 'app.log')),
#     'error': logging.FileHandler(os.path.join(config.LOG_DIR, 'error.log')),
# }

# # logging levels
# LEVELS = {
#     'debug': logging.DEBUG,
#     'info': logging.INFO,
#     'warning': logging.WARNING,
#     'error': logging.ERROR,
#     'critical': logging