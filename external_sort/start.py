# standard imports
import sys

# internal imports
from errors import LaunchParametersError
from sorter import Sorter


if len(sys.argv) != 4:
    raise LaunchParametersError()

MAX_SIZE = sys.argv[1]
INPUT_FILE = sys.argv[2]
OUTPUT_FILE = sys.argv[3]


def start(max_size,input_file, output_file):

    pass