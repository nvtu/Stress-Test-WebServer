import redis


class ReadingTestDB:


    def __init__(self):
        REDIS_HOST = 'localhost'
        REDIS_PORT = 6379
        self.r = redis.Redis(host = REDIS_HOST, port = REDIS_PORT)
    

    def update_redis_db(self, user_id: str, session_id: str, reading_test_id: int, ):
        self.r.set(f"{user_id}_{session_id}", reading_test_id)

    
    def retrieve_redis_db(self, user_id: str, session_id: str):
        retrieved_value = self.r.get(f"{user_id}_{session_id}")
        return retrieved_value