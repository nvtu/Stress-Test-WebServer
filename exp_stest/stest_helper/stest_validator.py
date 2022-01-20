from .stest_db import STestDB


class STestValidator():


    def __init__(self):
        self.db = STestDB()


    def validate(self, user_id: str, user_answer: int):
        retrieved_value = self.db.retrieve_redis_db(user_id).decode('utf-8')
        _, answer = retrieved_value.split('_')
        answer = int(answer)
        if answer == user_answer:
            return True
        return False



    