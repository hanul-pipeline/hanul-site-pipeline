# config
: 환경 변수 정보를 담은 ini 파일이 위치하는 공간

# .ini structure

### main
``` bash
; explanation
[<Theme>]
<VAR> = <VALUE>
```

### example
``` bash
; mysql 관련 변수
[MYSQL]
MYSQL_HOST = 34.64.200.xxx
MYSQL_PWD = xxxxxxx
MYSQL_PORT = xxxx
MYSQL_USER = root
MYSQL_DB = pipeline_xxxx
```