import builtins
from datetime import datetime
import inspect

class CustomPrinter:
    def __init__(self, include_time=True, include_file=True, include_line=True, separator=':'):
        self._original_print = builtins.print
        self.include_time = include_time
        self.include_file = include_file
        self.include_line = include_line
        self.separator = separator

    def print(self, *args, **kwargs):
        custom_args = self._build_custom_args()
        output_args = custom_args + args
        self._original_print(*output_args, **kwargs)

    def activate(self):
        builtins.print = self.print

    def deactivate(self):
        builtins.print = self._original_print

    def _build_custom_args(self):
        custom_parts = []
        
        if self.include_time:
            time_log = datetime.now().isoformat(timespec='seconds')
            custom_parts.append(time_log)
        
        if self.include_file:
            current_file = inspect.stack()[2].filename
            custom_parts.append(current_file)
        
        if self.include_line:
            current_row = inspect.stack()[2].lineno
            custom_parts.append(str(current_row))
        
        return (self.separator.join(custom_parts), '|') if custom_parts else ()
