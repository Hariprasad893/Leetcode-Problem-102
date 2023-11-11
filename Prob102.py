def levelOrder(root):
  # initializing an empty queue
  q = queue.Queue()
        
  # initializing an empty list to store the level order BT
  FinalList = []
  
  #putting the root in the queue
  q.put(root)
  
  # iterating till all the elements of the BT are stored in the main list level wise
  while q.empty() is False:
    # initializing an empty list to store the elements of a level
    LevelList = []
    # storing the current length of the queue
    q_len = q.qsize()
    # iterating over the queue
    for i in range(q_len):
      # popping the first element 
      node = q.get()
      if node!=None:
        # appending the node into the Level List
        LevelList.append(node.val)
        # appending the left and right children to the queue
        q.put(node.left)
        q.put(node.right)
  
    # storing the Level List at every level
    if LevelList:
        FinalList.append(LevelList)
  return FinalList
