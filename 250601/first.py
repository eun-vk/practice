# 실무에서 자주 사용하는 클래스 예제들

# 1. 데이터베이스 연결 클래스 (Database Connection)
class DatabaseConnection:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connection = None
    
    def connect(self):
        print(f"데이터베이스 연결: {self.host}:{self.port}")
        self.connection = f"connected_to_{self.host}"
        return self.connection
    
    def execute_query(self, query):
        if not self.connection:
            raise Exception("데이터베이스에 연결되지 않았습니다")
        print(f"쿼리 실행: {query}")
        return f"결과: {query}_executed"
    
    def close(self):
        if self.connection:
            print("데이터베이스 연결 종료")
            self.connection = None