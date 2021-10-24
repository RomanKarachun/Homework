import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
try:
    from . import rss_reader
except ImportError as err:
    raise ImportError(err)