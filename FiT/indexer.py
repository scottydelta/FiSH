#indexer.py
import os
from common import IndexerException
from hashlib import sha1
import json

class FileIndexer(object):
    '''The FileIndexer class generates an index(dictionary) of all filenames 
    with their SHA1 checksums as keys and a tuple of (<filename>,<size>) as corresponding values
    The FileIndexer recursively traverses all subdirectories of main directory supplied'''
    def __init__(self, path):
        if not os.path.exists(path):
            raise IndexerException(1, 'Invalid path supplied')
        if not os.path.isdir(path):
            raise IndexerException(2,'Path is not directory')
        self.path=os.path.abspath(path)
        self._generate_index()
        print 'indexed'

    def _generate_index(self):
        temp_index={}
        for item in os.walk(self.path):
            base_dir, _discard, basenames=item
            for basename in basenames:
                filename=os.path.join(base_dir,basename)
                #Skip broken symlinks!
                if not os.path.exists(filename):
                    continue
                file_size=os.stat(filename).st_size
                #Generate SHA1 sum of file -- is kinda slow
                with open(filename,'rb') as file_obj:
                    sha1sum=sha1(file_obj.read()).hexdigest()
                #Associate file hash with filename and size
                temp_index[sha1sum]=(filename,file_size)
        self.index=temp_index

    def getFile(self, fileIndex):
        '''Returns a file object of the file at index opened in read mode'''
        if not fileIndex in self.index.keys():
            raise IndexerException(3,'INVALID_FILE_ID')
        filename, file_size=self.index[fileIndex]
        if not os.path.exists(filename) :
            self._generate_index()
            raise IndexerException(4,'DIR_CHANGED')
        with open(filename,'rb') as file_obj:
            sha1sum=sha1(file_obj.read()).hexdigest()
        if sha1sum != fileIndex:
            self._generate_index()
            raise IndexerException(8,'FILE_CHANGED')
        return open(filename, 'rb')

    def getFileSize(self, fileIndex):
        return self.index[fileIndex][1]

    def saveFile(self, fileName, overwrite=False):
        '''Returns a file like object to write data to in current directory'''
        file_path=os.path.join(self.path, fileName)
        if os.path.exists(file_path):
            if not overwrite:
                raise IndexerException(5,'File already exists')
        return open(file_path,'wb')

    def reduced_index(self):
        red_fn=lambda x:(os.path.basename(x[0]),x[1])
        return json.dumps(dict([(k,red_fn(v)) for k,v in self.index.iteritems()]))

if __name__ == '__main__':
    print len(FileIndexer(raw_input('Enter path:')).index.keys())

