import unittest
from full_names import get_full_name


class NamesTestCase(unittest.TestCase):
    """Tests for names.py."""

    def test_first_last(self):
        """Test names like Janis Joplin."""
        full_name = get_full_name('janis', 'joplin')
        self.assertEqual(full_name, 'Janis Joplin')

    def test_first_middle_last(self):
        """Test names like Janis Kis Joplin."""
        full_name = get_full_name('janis', 'joplin', 'Kis')
        self.assertEqual(full_name, 'Janis Kis Joplin')

    def test_first_nomiddle_last(self):
        """Test names like Janis Joplin."""
        full_name = get_full_name('janis', 'joplin', ' ')
        self.assertEqual(full_name, 'Janis   Joplin')


if __name__ == '__main__':
    unittest.main()