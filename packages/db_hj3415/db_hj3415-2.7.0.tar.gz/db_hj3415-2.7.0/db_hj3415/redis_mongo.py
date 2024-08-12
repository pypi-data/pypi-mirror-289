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






