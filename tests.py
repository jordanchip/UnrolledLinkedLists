__author__ = 'Jordan Chipman'
__email__ = 'jordanchip@gmail.com'

import unittest
from unrolled_linked_list import UnrolledLinkedList




'''
> Implement your tests here

To run your tests, just run `python tests.py`
'''

list1 = UnrolledLinkedList(6)
print "TESTING APPEND"
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.append(6)
print str(list1)
assert len(list1) == 6

print "TESTING GETINDEX"
assert list1[0] == 1
assert list1[-1] == 6

print "TESTING NEW NODE ON APPEND"
list1.append(7)
list1.append(8)
print str(list1)
assert str(list1) == "{[1, 2, 3], [4, 5, 6, 7, 8]}"
assert len(list1) == 8
assert list1[3] == 4
assert list1[-6] == 3

list1.append(9)
list1.append(10)
print str(list1)
assert str(list1) == "{[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]}"
assert len(list1) == 10

print "TESTING CONTAINS"
assert 4 in list1
assert 9 in list1
assert not 11 in list1

print "TESTING DELETION"
del list1[9]
print str(list1)
assert str(list1) == "{[1, 2, 3], [4, 5, 6], [7, 8, 9]}"
assert list1[-4] == 6

print "TESTING DELETION + COMBINE NODES"
del list1[5]
print str(list1)
assert str(list1) == "{[1, 2, 3], [4, 5, 7, 8, 9]}"
assert len(list1) == 8
assert list1[-1] == 9
assert list1[-6] == 3
assert list1[3] == 4
del list1[3]
del list1[3]
del list1[3]
print str(list1)
assert str(list1) == "{[1, 2, 3, 8, 9]}"
assert list1[2] == 3
assert list1[-3] == 3

print "TESTING SETTING"
list1[0] = 0
list1[1] = 1
list1[2] = 2
list1[3] = 3
list1[4] = 4
print str(list1)
assert str(list1) == "{[0, 1, 2, 3, 4]}"

print "TESTING ITERATION"
for i in list1:
    print i

print "TESTING REVERSED ITERATION"
for i in reversed(list1):
    print i

print "TESTING ADDED 2 LISTS TOGETHER"
list2 = UnrolledLinkedList(2)
list2.append(5)
list2.append(6)
list2.append(7)

print str(list1)
print str(list2)

combinedList = list1 + list2
print str(combinedList)
assert str(combinedList) == "{[0, 1, 2], [3, 4, 5, 6, 7]}"

print "TESTING *="
combinedList *= 3
print str(combinedList)

print "TESTING STRING LISTS"
list3 = UnrolledLinkedList(4)
list3.append('x')
list3.append('x')
list3.append('x')
list3.append('x')
list3.append('x')
print str(list3)
del list3[2]
print str(list3)
del list3[1]
print str(list3)



class ExampleTest(unittest.TestCase):
    """ Demonstrates how the unittest framework works """

    def test_example(self):
        new_list = UnrolledLinkedList()
        self.assertIsNotNone(new_list)

if __name__ == '__main__':
    unittest.main()
