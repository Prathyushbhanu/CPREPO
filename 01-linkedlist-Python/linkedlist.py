"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
   def __init__(self, value):
       self.value = value
       self.next = None
    
class LinkedList(object):
   def __init__(self, head=None):
       self.head = head
    
   def append(self, new_element):
       # Your code goes here
       current = self.head
       if self.head:
           while current.next:
               current = current.next
           current.next = new_element
       else:
           self.head = new_element
        
   def get_position(self, position):
       """Get an element from a particular position. Assume the first position is "1". Return "None" if position is not in the list."""
       counter = 1
