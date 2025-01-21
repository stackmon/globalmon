import unittest
from globalmon.utils import convert_url_to_identifier


# Test cases
class TestConvertUrlToIdentifier(unittest.TestCase):
    def test_simple_url(self):
        url = "https://example.com/path"
        result = convert_url_to_identifier(url)
        self.assertEqual(result, "example_com_path")

    def test_url_without_path(self):
        url = "https://example.com"
        result = convert_url_to_identifier(url)
        self.assertEqual(result, "example_com")

    def test_url_with_multiple_paths(self):
        url = "https://example.com/path/to/resource"
        result = convert_url_to_identifier(url)
        self.assertEqual(result, "example_com_path_to_resource")

    def test_url_with_trailing_slash(self):
        url = "https://example.com/path/"
        result = convert_url_to_identifier(url)
        self.assertEqual(result, "example_com_path")

    def test_url_with_subdomain(self):
        url = "https://sub.example.com/path"
        result = convert_url_to_identifier(url)
        self.assertEqual(result, "sub_example_com_path")

    def test_url_with_no_protocol(self):
        url = "example.com/path"
        result = convert_url_to_identifier(url)
        self.assertEqual(result, "example_com_path")

    def test_url_with_query_params(self):
        url = "https://example.com/path?query=1"
        result = convert_url_to_identifier(url)
        self.assertEqual(result, "example_com_path")

    def test_url_with_fragment(self):
        url = "https://example.com/path#section"
        result = convert_url_to_identifier(url)
        self.assertEqual(result, "example_com_path")


if __name__ == "__main__":
    unittest.main()
