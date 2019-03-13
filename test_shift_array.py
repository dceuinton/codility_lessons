import unittest
import shift_array

class test_binary_gap(unittest.TestCase):

	def test_shift_array(self):
		self.assertEqual(shift_array.cyclic_rotate_array([], 2), [])
		self.assertEqual(shift_array.cyclic_rotate_array([1], 1), [1])
		self.assertEqual(shift_array.cyclic_rotate_array([1, 2], 1), [2, 1])
		self.assertEqual(shift_array.cyclic_rotate_array([1, 2], 2), [1, 2])
		self.assertEqual(shift_array.cyclic_rotate_array([1, 2], 2), [1, 2])

		self.assertEqual(shift_array.cyclic_rotate_array([0, 0, 0], 1), [0, 0, 0])		
		self.assertEqual(shift_array.cyclic_rotate_array([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])		


if __name__ == '__main__':
	unittest.main()