# standard imports
import sys

# internal imports
from errors import LaunchParametersError
import sorter


if len(sys.argv) != 4:
    raise LaunchParametersError()

MAX_SIZE = sys.argv[1]
INPUT_FILE = sys.argv[2]
OUTPUT_FILE = sys.argv[3]

sorter.logging.debug('Get parametrs : {} {} {}'.format(MAX_SIZE, INPUT_FILE, OUTPUT_FILE))

sorter = sorter.Sorter(MAX_SIZE, INPUT_FILE, OUTPUT_FILE)
sorter.shatter_file()
