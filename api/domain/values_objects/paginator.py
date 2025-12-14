from typing import Optional

class Pagination:
    def __init__(self, page=1,size=10):
        self.page =max(page,1)
        self.size = min(max(size,1), 200)
        
    @property
    def offset(self)-> int:
        return (self.page-1)* self.size