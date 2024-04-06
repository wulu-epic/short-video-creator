import string, random
from threading import Thread

class Utilities(object):
    def __init__(self) -> None:
        pass

    def random_string(self):
        result = ''
        k = string.ascii_letters + string.ascii_uppercase + string.digits
        for _ in range(16):
            result += k[random.randint(0, len(k)-1)]
        
        return result
    
    def text_edge_cases(self, text : str) -> str:
        characters_to_remove = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        for character in text:
            if character in characters_to_remove:
                text = text.replace(character, '_')

        return text
    
    def clean_threads(self, threads : list[Thread]) -> None:
        for thread in threads:
            thread.join()
