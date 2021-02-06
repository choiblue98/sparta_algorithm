class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))

# 충돌
# 해쉬함수를 쓰다보면 8로 나누어도 인덱스값이 동일해질 때가 있음!
# 이렇게 되면 똑같은 배열 위치에 value를 업데이트 시키게 됨 -> 덮어씌워짐
# 해결1. 링크드 리스트를 사용하는 방법: 충돌이 나도 다음 노드로 편입시켜줌
# -> key도 같이 저장해주어야
# 해결2.