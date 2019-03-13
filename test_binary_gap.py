import unittest
import binary_gap

class test_binary_gap(unittest.TestCase):

	def test_solution(self):
		self.assertEqual(binary_gap.solution(1), 0)


if __name__ == '__main__':
	unittest.main()