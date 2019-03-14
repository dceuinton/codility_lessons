import unittest
import shift_array

class test_binary_gap(unittest.TestCase):

	def test_cyclic_rotate_empty_array(self):
		self.assertEqual(shift_array.cyclic_rotate_array([], 1), [])

	def test_cyclic_rotate_single_element_array(self):
		self.assertEqual(shift_array.cyclic_rotate_array([1], 1), [1])

	def test_cyclic_rotate_single_shift(self):
		self.assertEqual(shift_array.cyclic_rotate_array([1, 2], 1), [2, 1])

	def test_cyclic_rotate_to_original_array(self):
		self.assertEqual(shift_array.cyclic_rotate_array([1, 2], 2), [1, 2])

	def test_cyclic_rotate_more_than_size_of_array(self):
		self.assertEqual(shift_array.cyclic_rotate_array([1, 2], 3), [2, 1])

	def test_cyclic_rotate_array_of_same_values(self):
		self.assertEqual(shift_array.cyclic_rotate_array([0, 0, 0], 1), [0, 0, 0])		

	def test_cyclic_rotate_full_example(self):
		self.assertEqual(shift_array.cyclic_rotate_array([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])		


if __name__ == '__main__':
	unittest.main()