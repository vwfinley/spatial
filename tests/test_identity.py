"""
    Tests for `point.py`.
"""
import sys
import unittest

sys.path.insert(0, "..")
from identity import Identity

class IdentityTests(unittest.TestCase):
    """Tests for 'identity.py'."""

    def test_identity(self):
        """trivial test to verify Identity matrix was properly initialized."""
        i = Identity()
        self.assertEqual(i.m[0][0], 1.0)
        self.assertEqual(i.m[0][1], 0.0)
        self.assertEqual(i.m[0][2], 0.0)

        self.assertEqual(i.m[1][0], 0.0)
        self.assertEqual(i.m[1][1], 1.0)
        self.assertEqual(i.m[1][2], 0.0)

        self.assertEqual(i.m[2][0], 0.0)
        self.assertEqual(i.m[2][1], 0.0)
        self.assertEqual(i.m[2][2], 1.0)

if __name__ == '__main__':
    unittest.main()
