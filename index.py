class OneIndexedList(list):
  def __getitem__(self, index):
    if type(index) == int and index > 0: 
      index -= 1 
    if type(index) == slice:
      start, stop = index.start, index.stop 
      if start and start > 0: 
        start -= 1 
      if stop and stop > 0: 
        stop -=  1 
      index = slice(start, stop, index.step) 
    return super().__getitem__(index) 
     
  def __setitem__(self, index, val): 
    super().__setitem__(index-1, val)



