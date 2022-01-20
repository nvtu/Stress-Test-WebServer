import redis


class STestDB:


    def __init__(self):
        REDIS_HOST = 'localhost'
        REDIS_PORT = 6379
        self.r = redis.Redis(host = REDIS_HOST, port = REDIS_PORT)
    

    def update_redis_db(self, user_id: str, formula: str, answer: int):
        self.r.set(f"{user_id}_stest", f"{formula}_{answer}")

    
    def retrieve_redis_db(self, user_id: str):
        retrieved_value = self.r.get(f"{user_id}_stest")
        return retrieved_value