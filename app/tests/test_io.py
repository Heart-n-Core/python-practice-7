import os
import unittest
from pathlib import Path

from app.io.input import read_file_builtin, read_file_with_pandas


class BaseInputFileTestCase(unittest.TestCase):
    test_path = Path("data/test_data.txt")
    cities = [
        "Kyiv",
        "Kharkiv",
        "Odesa",
        "Dnipro",
        "Zaporizhzhia",
        "Lviv",
        "Kryvyi Rih",
        "Mykolaiv",
        "Mariupol",
        "Vinnytsia",
    ]
    expected_content = "\n".join(cities)

    @classmethod
    def setUpClass(cls):
        cls.test_path.parent.mkdir(parents=True, exist_ok=True)
        cls.test_path.write_text(cls.expected_content, encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        if cls.test_path.exists():
            os.remove(cls.test_path)


class ReadFileBuiltinTests(BaseInputFileTestCase):
    def test_returns_all(self):
        result = read_file_builtin(str(self.test_path))
        self.assertEqual(result, self.expected_content)

    def test_is_string(self):
        result = read_file_builtin(str(self.test_path))
        self.assertIsInstance(result, str)

    def test_contains_all(self):
        result = read_file_builtin(str(self.test_path))
        for city in self.cities:
            with self.subTest(city=city):
                self.assertIn(city, result.splitlines())


class ReadFileWithPandasTests(BaseInputFileTestCase):
    def test_returns_all(self):
        result = read_file_with_pandas(str(self.test_path))
        self.assertEqual(result, self.expected_content)

    def test_is_string(self):
        result = read_file_with_pandas(str(self.test_path))
        self.assertIsInstance(result, str)

    def test_returns_same_lines_number(self):
        result = read_file_with_pandas(str(self.test_path))
        self.assertEqual(len(result.splitlines()), len(self.cities))
