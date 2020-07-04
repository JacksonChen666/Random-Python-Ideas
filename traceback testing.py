import traceback

import error_testing

t = traceback

try:
    error_testing.valueerror()
except ValueError:
    t.print_exc(2000)
