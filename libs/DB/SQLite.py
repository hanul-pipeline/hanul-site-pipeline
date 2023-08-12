import sqlite3

# SQLite 파일에 QUERY 동작
def SQLite_UPDATE(PATH, QUERY):
    connection = sqlite3.connect(PATH)
    cursor = connection.cursor()
    cursor.execute("PRAGMA journal_mode = WAL")
    cursor.execute(QUERY)
    connection.commit()

def create_table(PATH):
    # 데이터베이스 연결 생성 또는 기존 데이터베이스 연결
    conn = sqlite3.connect(PATH)

    # 커서 생성
    cursor = conn.cursor()

    # 테이블 생성 쿼리
    QUERY = '''
    CREATE TABLE IF NOT EXISTS measurement (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id TEXT,
            date TEXT,
            time TEXT,
            measurement REAL,
            rank TEXT);
    '''

    # 테이블 생성 쿼리 실행
    cursor.execute(QUERY)

    # 변경사항 저장 및 연결 종료
    conn.commit()

if __name__ == "__main__":
    create_table("/Users/kimdohoon/git/hooniegit/FastAPI-demo/datas/SQLite/sensors")