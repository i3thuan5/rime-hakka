from unittest.case import TestCase
from 產生dict import theh


class 詞表試驗(TestCase):
    def test_詞(self):
        self.pit = {
            "南四縣": "\n\n\n\nkung55",
            "又音": "",
            "反義詞": "",
            "四縣音": "\n\n\n\n（二）kung55",
            "多音字": "（一）kung24四kung53海〔見【空】條〕",
            "大埔音": "\n\n\n\nkung53",
            "對應華語": "",
            "文白讀": "",
            "檔名": "detail_7306.html",
            "海陸音": "\n\n\n\nkung11",
            "筆畫": "03-08",
            "詔安音": "\n\n\n\nkung31",
            "詞目": "【空】",
            "近義詞": "",
            "部首": "穴",
            "釋義": [],
            "饒平音": "\n\n\n\nkung53",
        }
        self.kiatko = ('空', 'kung55')
        self.assertEqual(theh(self.pit), self.kiatko)

    def test_空ê(self):
        self.pit = {
            "檔名": "detail_8219.html"
        }
        with self.assertRaises(ValueError):
            theh(self.pit)
