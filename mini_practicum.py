"""
@ASSESSME.USERID: userID
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Mini Practicum 11
@ASSESSME.ANALYZE: YES
"""

import math

class Circle:
   
    def __eq__(self, other) -> bool:
       pass
    
    def __lt__(self, other) -> bool:
        pass
    
    def __hash__(self) -> int:
        pass

    def intersect(self, other):
        pass       

def main():
    circle1 = Circle((0, 0), 2)
    circle2 = Circle((4, 0), 3) 
    circle3 = Circle((3, 3), 1)
    a_list = [circle1, circle2, circle3]
    a_list.sort()
    print(a_list)
    print("circle1 and circle2 intersect:", circle1.intersect(circle2)) # True
    print("circle1 and circle3 intersect:", circle1.intersect(circle3)) # False
    print("circle2 and circle3 intersect:", circle2.intersect(circle3)) # True
    a_set = set(a_list)
    print(a_set)

main()           
    
