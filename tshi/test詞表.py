from unittest.case import TestCase
from 產生dict import theh


class 詞表試驗(TestCase):
    def tearDown(self):
        self.assertEqual(theh(self.pit), self.kiatko)

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

    def test_雙字(self):
        self.pit = {
            "南四縣": "\n\n\n\na24ba24",
            "又音": "",
            "反義詞": "",
            "四縣音": "\n\n\n\na24ba24",
            "多音字": "",
            "大埔音": "\n\n\n\na33ba33",
            "對應華語": "阿爸、爸爸",
            "文白讀": "",
            "檔名": "detail_2.html",
            "海陸音": "\n\n\n\na33ba53",
            "詔安音": "",
            "詞性": "",
            "詞目": "【阿爸】",
            "近義詞": "",
            "釋義": [],
            "饒平音": "\n\n\n\na11ba11"
        }
        self.kiatko = ('阿爸', 'a24 ba24')

    def test_罕音(self):
        self.pit = {
            "南四縣": "",
            "又音": "",
            "反義詞": "",
            "四縣音": "\n\n\n\nen24deu24",
            "多音字": "",
            "大埔音": "",
            "對應華語": "我們",
            "文白讀": "",
            "檔名": "detail_2626.html",
            "海陸音": "\n\n\n\nen53deu53",
            "詔安音": "",
            "詞性": "代",
            "詞目": "【{[F307]}兜】",
            "近義詞": "【】、【俚】、【俚】、【兜儕】、【兩儕】",
            "釋義": [
                {
                    "def": "稱含說話對象的「我們」",
                    "example": [
                        [
                            "<U+FFF9>{[F307]}兜係同班同學。",
                            "<U+FFFB>（我們是同班同學。）"
                        ]
                    ]
                }
            ],
            "饒平音": "\n\n\n\nen11deu11",
        }
        self.kiatko = ('𫣆兜', 'en24 deu24')

    def test_文白(self):
        self.pit = {
            "南四縣": "\n\n\n\ngiog2iang55",
            "又音": "",
            "反義詞": "",
            "四縣音": "\n\n\n\ngiog2iang55白",
            "多音字": "",
            "大埔音": "\n\n\n\ngiog21rhang53",
            "對應華語": "腳印",
            "文白讀": "◆giog2in55四　文 giog5rhang11海　白",
            "檔名": "detail_4178.html",
            "海陸音": "\n\n\n\ngiog5rhin11文",
            "詔安音": "\n\n\n\ngio24rhin31",
            "詞性": "名",
            "詞目": "【腳印】",
            "近義詞": "【腳跡】",
            "釋義": [],
            "饒平音": "\n\n\n\ngiog2rhin53"
        }
        self.kiatko = ('腳印', 'giog2 iang55')


class 其他無愛ê(TestCase):
    def tearDown(self):
        with self.assertRaises(ValueError):
            theh(self.pit)

    def test_空ê(self):
        self.pit = {
            "檔名": "detail_8219.html"
        }

    def test_標點(self):
        self.pit = {
            "南四縣": "\n\n\n\nsu55tai55ca55a24，zii31tai55bun24ga24",
            "又音": "",
            "反義詞": "",
            "四縣音": "\n\n\n\nsu55tai55ca55a24，zii31tai55bun24ga24",
            "多音字": "",
            "大埔音": "\n\n\n\nshu53tai53ca53va33，zii31tai53bun33ga33",
            "對應華語": "",
            "文白讀": "",
            "檔名": "detail_12236.html",
            "海陸音": "\n\n\n\nshu33tai33ca11a53，zii24tai33bun53ga53",
            "詔安音": "",
            "詞性": "諺",
            "詞目": "【樹大杈椏，子大分家】",
            "近義詞": "",
            "釋義": [
                {
                    "def": "樹木越大枝椏也越多，兒女成年後就要分家",
                    "example": [
                        [
                            "<U+FFF9>樹大杈椏，子大分家，細人仔成家後愛分佢出去戴。",
                            "<U+FFFB>（樹木越大枝椏越多，子女成年後就要分家，小孩成家後要讓他出去住。）"
                        ]
                    ]
                }
            ],
            "饒平音": "\n\n\n\nshu24tai24ca53va11，zii53tai24bun11ga11"
        }

    def test_無唸法(self):
        self.pit = {
            "南四縣": "\n\n\n\nid2xid2xid2",
            "又音": "",
            "反義詞": "",
            "四縣音": "",
            "多音字": "",
            "大埔音": "",
            "對應華語": "一點點",
            "文白讀": "",
            "檔名": "detail_5839.html",
            "海陸音": "\n\n\n\nrhid5sid2sid2",
            "詔安音": "",
            "詞性": "副",
            "詞目": "【一息息】",
            "近義詞": "【一滴】、【一息】、【少少仔】",
            "釋義": [
                {
                    "def": "四縣不說「一息息」，說成「一息息仔（音id2 xid5 xid5 e31）」。一點點、一些些，形容極少",
                    "example": [
                        [
                            "<U+FFF9>今晡日个人客恁多，這一息息（仔）菜一定毋罅食。",
                            "<U+FFFB>（今天的客人那麼多，這一點點菜一定不夠吃。）"
                        ]
                    ]
                }
            ],
            "饒平音": "\n\n\n\nrhid2sid5sid5"
        }
