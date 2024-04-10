# SOLID IMPLEMENTATION: Interface segregation principle

# FileIO interface is used by initializing with the filename and then using either the get_line_list
# method to read lines from the file or the write data method to save a string to the file

import os
from abc import ABC, abstractmethod

## interface for FileIO operations
class FileIOInterface(ABC):
    @abstractmethod
    def __init__(self, filename: str):
        pass

    @abstractmethod
    def get_line_list(self) -> list[str]:
        pass

    @abstractmethod
    def write_data(self, data: str):
        pass

## implements FileIOInterface
class FileIO(FileIOInterface):
    def __init__(self, filename: str):
        self.filename = filename
    
    ## returns list of each line inside file
    def get_line_list(self) -> list[str]:
        try:
            file = open(self.filename, "r")
            lines = list()
            for line in file:
                lines.append(line.strip())
            file.close()
            return lines
        except IOError:
            print(f"Failed to open {self.filename}")
            return list()
    
    ## creates/overwrites file with provided data
    def write_data(self, data: str) -> None:
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        file = open(self.filename, "w")
        file.write(data)
        file.close()

def main():
    input_file = FileIO("url.in")
    output_file = FileIO("output.log")
    output_file.write_data(str(input_file.get_line_list()))

if __name__=="__main__":
    main()