import time
import random
import logging

from .AbstractWrapper import AbstractWrapper

class DelayWrapper(AbstractWrapper):

    """
    Parameters:
        client (AbstractClient): Ie. HttpClient
        length (int):            Delay length in seconds
        maxLength (int):         If specified, delay will be a random value between length and maxLength
        
    Returns: 
        (Response): https://requests.readthedocs.io/en/latest/api/#requests.Response
    """
    def __init__(self, client, length=0, maxLength=None):
        super().__init__(client)
        self.length = length
        self.maxLength = maxLength

    def download(self, request):
        delay = self._generateDelayLength()
        logging.info(f'Delaying by {delay}s ... {request.method} {request.url}')
        
        time.sleep(delay)
        return self.client.download(request)

    def _generateDelayLength(self):
        if self.maxLength is None:
            return self.length
        else:
            return random.randrange(self.length, self.maxLength+1)
