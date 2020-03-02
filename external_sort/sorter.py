import sys
import os
import logging

from errors import MemoryStarvationError


logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)


class Sorter:

    def __init__(self, max_size, input_file, output_file):
        self.max_size = max_size
        self.input_file = input_file
        self.output_file = output_file
        self.current_directory = os.getcwd()

    @staticmethod
    def get_file_location(self, file_name):
        file_location = self.current_directory + '\\' + file_name
        logging.debug('{} file is being processed'.format(file_location))
        return file_location

    def create_temporary_folder(self):
        path = self.current_directory + '\\' + 'temporary_folder'
        logging.debug('Create temporary folder {}'.format(path))
        os.mkdir(path)

    def shatter_file(self):
        input_file_location = self.get_file_location(self, self.input_file)
        with open(input_file_location) as input_file:
            trapped_memory_sum = 0
            for line in input_file:
                logging.debug('Handling line - {}'.format(line))
                trapped_memory_line = sys.getsizeof(line)
                if trapped_memory_line > self.max_size :
                    raise MemoryStarvationError()












