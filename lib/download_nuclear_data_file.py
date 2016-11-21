import time
import wget

class DownloadNuclearDataFile(object):
    url = None

    def __init__(self, url=None):
        if url:
            self.url = url
        else:
            self.url = 'https://www-nds.iaea.org/amdc/ame2012/mass.mas12'

    def download_to(self, path=None):
        if not path:
            raise Exception('Error: Inform path destination to the file!')
        file_name = '%s.txt' % str(time.time())
        print path
        print file_name
        try:
            wget.download(self.url, out='%s/%s' % (path, file_name))
            return '%s/%s' % (path, file_name)
        except Exception, e:
            raise Exception('Error on Download Nuclear Data File on URL %s. %s' % (self.url, e))
            return False
