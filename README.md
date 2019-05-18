# rime-hakka
客家輸入法詞表

### wip2.json 來源
1. [moedict-data-hakka](https://github.com/g0v/moedict-data-hakka/blob/master/Makefile)先掠資料`make download`
2. Tī`moedict-data-hakka`產生wip.json  
```bash
$ docker run -ti -v `pwd`:/opt python:2.7-stretch bash

apt-get  update && apt-get install python-virtualenv -y
make parse
```
3. 來到這專案`整理wip.py`產生`wip2.json`
