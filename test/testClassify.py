import os
import sys

import unittest

#import classify.classify
import classify
currDir = os.path.dirname(__file__)


class ClassifyTest(unittest.TestCase):
	
	def setUp(self):
		dataFile = open(os.path.join(currDir,"marks.dat"))
		self._data = classify.getData(dataFile)

	def test_InvalidRange(self):
		boundaries = [49, 0]
		self.assertEqual(['none'], classify.thoseInRange(self._data, 49, 0))

		boundaries = [1, 0]
		self.assertEqual(['none'], classify.thoseInRange(self._data, 1, 0))

	def test_OutputAll(self):
		boundaries = [0, 101]
		self.assertEqual(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'], classify.thoseInRange(self._data, boundaries[0], boundaries[1]))

	#tests that the lower boundary is inclusive
	def test_LowerBound(self):
		boundaries = [78, 101]
		self.assertEqual(['a', 'c', 'h', 'i'], classify.thoseInRange(self._data, boundaries[0], boundaries[1]))
	
	#tests that the lower boundary is exclusive
	def test_UpperBound(self):
		boundaries = [10, 56]		
		self.assertEqual(['f', 'g', 'j', 'k'], classify.thoseInRange(self._data, boundaries[0], boundaries[1]))
		
		
if __name__ == '__main__':
	unittest.main()
