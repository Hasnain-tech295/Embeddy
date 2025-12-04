# central config loader (env)

# https://github.com/12factor/methodology/blob/master/config.md

# import os
# import logging
# import logging.config

# from dotenv import load_dotenv

# load_dotenv()

# # logging
# logging.config.dictConfig({
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
#         },
#     },
#     'handlers': {
#         'default': {
#             'level': 'INFO',
#             'formatter': 'standard',
#             'class': 'logging.StreamHandler',
#             'stream': 'ext://sys.stdout',  # Default is stderr
#         },
#     },
#     'loggers': {
#         '': {  # root logger
#             'handlers': ['default'],
#             'level': 'WARNING',
#             'propagate': False
#         },
#         'my.package': {
#             'handlers': ['default'],
#             'level': 'INFO',
#             'propagate': False
#         },
#     }
# })

# # env
# ENV = os.environ.get('ENV', 'dev')
# DEBUG = os.environ.get('DEBUG', '