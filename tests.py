__author__ = 'Jordan Chipman'
__email__ = 'jordanchip@gmail.com'

import unittest
from unrolled_linked_list import UnrolledLinkedList

'''
> Implement your tests here

To run your tests, just run `python tests.py`
'''


class ExampleTest(unittest.TestCase):
    """ Demonstrates how the unittest framework works """

    def getDefaultList(self):
        newList = UnrolledLinkedList(3)
        newList.append(0)
        newList.append(1)
        newList.append(2)
        newList.append(3)
        newList.append(4)
        #{[0, 1], [2, 3, 4]}
        return newList

    def test_append(self):
        list1 = UnrolledLinkedList(6)
        #print "TESTING APPEND"
        list1.append(1)
        list1.append(2)
        list1.append(3)
        list1.append(4)
        list1.append(5)
        list1.append(6)
        #print str(list1)
        self.assertEquals(len(list1), 6)

    def test_get_index(self):
        list1 = self.getDefaultList()
        #print "TESTING GETINDEX"
        self.assertEquals(list1[0],0)
        self.assertEquals(list1[-1],4)
        self.assertEquals(list1[-5],0)

    def test_new_node_append(self):
        list1 = self.getDefaultList()
        #print "TESTING NEW NODE ON APPEND"
        list1.append(5)
        list1.append(6)
        #print str(list1)
        self.assertEquals(str(list1), "{[0, 1], [2, 3], [4, 5, 6]}")
        self.assertEquals(len(list1),7)
        self.assertEquals(list1[3], 3)
        self.assertEquals(list1[-6], 1)

        list1.append(7)
        list1.append(8)
        #print str(list1)
        self.assertEquals(str(list1), "{[0, 1], [2, 3], [4, 5], [6, 7, 8]}")
        self.assertEquals(len(list1), 9)

    def test_contains(self):
        list1 = self.getDefaultList()
        #print "TESTING CONTAINS"
        assert 4 in list1
        assert 0 in list1
        assert not 11 in list1

    def test_deletion(self):
        list1 = self.getDefaultList()
        #print "TESTING DELETION"
        del list1[4]
        #print str(list1)
        self.assertEquals(str(list1), "{[0, 1], [2, 3]}")
        self.assertEquals(list1[-4], 0)

    def test_deletion_and_node(self):
        list1 = self.getDefaultList()
        #print "TESTING DELETION + COMBINE NODES"
        del list1[0]
        del list1[0]
        #print str(list1)
        self.assertEquals(str(list1), "{[2], [3, 4]}")
        assert len(list1) == 3
        assert list1[-1] == 4
        assert list1[-3] == 2
        assert not 1 in list1
        assert not 0 in list1

        del list1[0]

        self.assertEquals(str(list1), "{[3], [4]}")
        assert list1[1] == 4
        assert list1[-1] == 4
        assert not 2 in list1

    def test_setting(self):
        list1 = self.getDefaultList()
        #print "TESTING SETTING"
        list1[0] = 4
        list1[1] = 3
        list1[2] = 2
        list1[3] = 1
        list1[4] = 0
        self.assertEquals(list1[0], 4)
        self.assertEquals(list1[4], 0)
        list1[-5] = 5
        self.assertEquals(list1[-5], 5)
        #print str(list1)
        self.assertEquals(str(list1), "{[5, 3], [2, 1, 0]}")

    def test_iteration(self):
        list1 = self.getDefaultList()
        counter = 0
        for i in list1:
            self.assertEquals(i, counter)
            counter += 1

        counter -= 1

        for i in reversed(list1):
            self.assertEquals(i, counter)
            counter -= 1

    def test_add_two_lists(self):

        list1 = self.getDefaultList()

        #print "TESTING ADDED 2 LISTS TOGETHER"
        list2 = UnrolledLinkedList(5)
        list2.append(5)
        list2.append(6)
        list2.append(7)
        list2.append(8)
        list2.append(9)

        #print str(list1)
        #print str(list2)

        combinedList = list1 + list2
        #print str(combinedList)
        self.assertEquals(str(combinedList), "{[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]}")
        assert 4 in combinedList
        assert 8 in combinedList
        self.assertEquals(combinedList[-6], 4)
        self.assertEquals(combinedList[5], 5)
        self.assertEquals(len(combinedList), 10)
        list4 = UnrolledLinkedList(2)
        list4.append(10)
        list4.append(11)
        combinedList += list4
        #print str(combinedList)

    def test_mult(self):
        combinedList = self.getDefaultList()

        length = len(combinedList)
        #print "TESTING *="
        combinedList *= 2
        #print str(combinedList)
        self.assertEquals(length*2, len(combinedList))

        #print "TESTING STRING LISTS"
        list3 = UnrolledLinkedList(4)
        list3.append('x')
        list3.append('x')
        list3.append('x')
        list3.append('x')
        list3.append('x')
        #print str(list3)
        del list3[2]
        #print str(list3)
        del list3[1]
        #print str(list3)

    def test_slicing(self):
        #print "TESTING SLICING"
        sliceList = UnrolledLinkedList(4)
        sliceList.append(0)
        sliceList.append(1)
        sliceList.append(2)
        sliceList.append(3)
        sliceList.append(4)
        sliceList.append(5)
        sliceList.append(6)
        #print str(sliceList)
        sliceList = sliceList[-1:]
        #print str(sliceList)

    def test_exceptions(self):
        list1 = self.getDefaultList()
        with self.assertRaises(TypeError):
            list1['hi']
        with self.assertRaises(TypeError):
            x = "hi"
            del list1[x]
        with self.assertRaises(TypeError):
            list1["ok"] = 6
        with self.assertRaises(IndexError):
            list1[5]
        with self.assertRaises(IndexError):
            list1[-6]
        with self.assertRaises(IndexError):
            del list1[40]

if __name__ == '__main__':
    unittest.main()
