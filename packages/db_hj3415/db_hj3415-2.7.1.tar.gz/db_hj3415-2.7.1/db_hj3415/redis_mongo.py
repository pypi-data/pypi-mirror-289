import redis
import mongo
import json


class Redis:
    redis_client: redis.Redis | None = None

    @classmethod
    def initialize_client(cls, client: redis.Redis):
        # 클래스를 사용하기전에 클라이언트를 연결하여 초기화해준다.
        cls.redis_client = client
        print(f"Redis Base class client initialized.")

    def __init__(self, name: str = ''):
        self.redis_name = name

    @classmethod
    def delete(self, redis_name: str):
        """
        redis_name 에 해당하는 키/값을 삭제하며 원래 없으면 아무일 없음
        :param redis_name:
        :return:
        """
        # print(Redis.list_redis_names())
        self.redis_client.delete(redis_name)
        # print(Redis.list_redis_names())

    @classmethod
    def delete_all_with_pattern(self, pattern: str):
        """
        pattern에 해당하는 모든 키를 찾아서 삭제한다.
        :param pattern: ex) 005930.c101* - 005930.c101로 시작되는 모든키 삭제
        :return:
        """
        # print(Redis.list_redis_names())
        # SCAN 명령어를 사용하여 패턴에 맞는 키를 찾고 삭제
        cursor = '0'
        while cursor != 0:
            cursor, keys = self.redis_client.scan(cursor=cursor, match=pattern, count=1000)
            if keys:
                self.redis_client.delete(*keys)
        # print(Redis.list_redis_names())

    @classmethod
    def list_redis_names(cls) -> list:
        return cls.redis_client.keys('*')


class C101(mongo.C101, Redis):
    def __init__(self, code: str):
        mongo.C101.__init__(self, code)
        Redis.__init__(self)
        self.set_redis_name()

    def set_redis_name(self, *args):
        """
        redis의 저장 이름값을 설정하며 기본 코드명.c101에 접미사를 추가할수 있다.
        :param args: 접미사 추가시 코드명.c101_접미사
        :return:
        """
        self.redis_name = self.code + '.' + 'c101'
        for arg in args:
            self.redis_name += '_' + arg

    def get_recent(self, merge_intro=False) -> dict:
        if merge_intro:
            self.set_redis_name('recent', 'merged')
        else:
            self.set_redis_name('recent')

        try:
            cached_data = self.redis_client.get(self.redis_name).decode('utf-8')
        except AttributeError:
            # self.redis_name에 해당하는 값이 없는 경우
            # print("MongoDB에서 데이터 가져오기")
            # Redis 캐시에 데이터가 없으면 MongoDB에서 가져오기
            data = super().get_recent(merge_intro=merge_intro)
            if data:
                # 데이터를 Redis에 캐싱
                self.redis_client.set(self.redis_name, json.dumps(data))
            return data
        else:
            # print("Redis 캐시에서 데이터 가져오기")
            return json.loads(cached_data)






