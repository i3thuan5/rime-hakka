import json
import re
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 做字表 import 造字


def main():
    #
    # 程式頭
    #
    with open('hakka.dict.yaml', 'w', encoding='utf-8') as f:
        # 輸出字典踏話頭
        print(dict_header, file=f)
        # 印教典詞
        supio, tsuanpoo_lo = 提教典表()
        # 印傳統調號的羅馬字音節表
        for im in sorted(tsuanpoo_lo):
                # 一般
            print('{}\t{}\t1'.format(im, im), file=f)
        for han, lo in sorted(supio, key=lambda tup: (tup[1], tup[0])):
            print('{}\t{}\t2'.format(han, lo), file=f)


def 提教典表():
    with open('wip2.json') as 檔:
        資料 = json.load(檔)
    tsuanpoo_lo = set()
    supio = set()
    for pit in 資料:
        try:
            han, lo = theh(pit)
            for l in lo.split():
                tsuanpoo_lo.add(l)
            supio.add((han, lo))
        except ValueError:
            pass
    return supio, tsuanpoo_lo


造字標記 = re.compile(r'\{\[([A-Z0-9]{4})\]\}')


def theh(pit):
    try:
        han = 造字標記.sub(
            lambda m: 造字[m.group(1)],
            pit['詞目'].strip().lstrip('【').rstrip('】')
        )
        lo = (
            文章粗胚.數字英文中央全加分字符號(pit['四縣音'].strip().rstrip('文白').split('）')[-1])
        ).replace('-', ' ')
    except KeyError:
        raise ValueError('無資料！')
    if lo=='':
        raise ValueError('無唸法！')
    if '，' in han or '－－' in han or '、' in han:
        raise ValueError('有標點先莫收')

    return han, lo


dict_header = '''# Rime dictionary
# encoding: utf-8

---
name: hakka-xi-ien
version: "0.1"
sort: by_weight
use_preset_vocabulary: false
...'''

if __name__ == '__main__':
    main()
