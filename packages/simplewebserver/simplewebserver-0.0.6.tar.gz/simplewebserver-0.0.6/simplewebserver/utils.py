from dataclasses import asdict
from datetime import datetime
from decimal import Decimal
from io import BufferedWriter
import json
import logging
import traceback


logger = logging.getLogger()

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        elif isinstance(o, datetime):
            return o.isoformat()
        elif isinstance(o, BufferedWriter):
            return '(BufferWriter object)'
        elif hasattr(o, '__dataclass_fields__'):
            return asdict(o)
        
        try:
            return super().default(o)
        except TypeError as te:
            try:
                return str(o)
            except Exception as e:
                logger.error(get_exception_detail(te))
                logger.error(get_exception_detail(e))
                return "Unsupported Type"

def get_exception_detail(e: Exception):
    return [f"{e.__class__.__module__}.{e.__class__.__name__}: {e}"] + traceback.format_list(traceback.extract_tb(e.__traceback__))