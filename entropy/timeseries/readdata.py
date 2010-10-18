import csv

class CsvReader(object):
    """An object that will read in csv files using the csv module and use the 
       first row as headers to define fieldnames.
       Sample usage:
       reader = CsvReader()
       reader.read_file(in_filename)
    """
    
    def __init__(self):
        self._data ={}
    
    @property
    def fieldnames(self):
        return self._data.keys()
    
    def __validate_fieldnames(self, fieldnames):
        if len(set(fieldnames)) != len(fieldnames):
            raise ValueError("Field names need to be unique")
        
    def __validate_cols(self):
        pass
            
    
    def read_file(self, file, fieldnames=None, dialect='excel', *args, **kwargs):
        """
        Read a file object into the reader instance. All optional arguments are
        passed to a csv.DictReader.
        """
        freader = csv.DictReader(file, fieldnames=fieldnames, dialect=dialect, *args, **kwargs)
        self.__validate_fieldnames(freader.fieldnames)
        
        for field in freader.fieldnames:
            self._data[field]=[]
            
        for row in freader:
            for field in self.fieldnames:
                self._data[field].append(row[field])

        
        
        
        
    