# 해시 테이블 (Hash Table)
# key - value : 하나의 key는 하나의 value만 저장할 수 있다
# Direct Asses Table : key 값으로 인덱스를 설정한다. key 값의 범위가 커질수록 메모리 공간이 낭비될 수 있다.
# 해시 함수 : 특정 값을 원하는 범위의 자연수로 바꿔주는 함수
# 해시 테이블은, 고정된 크기의 배열을 만들고, 해시 함수를 이용해서 key를 원하는 범위의 자연수로 바꾼다
# 그 후 해시 함수 결과값 인덱스에 key-value 쌍을 저장한다. (주어진 key를 원하는 범위의 자연수로 바꿔서 리턴해줌)



# CHANING - 쇠사슬처럼 엮기
# 해시 테이블은 한 인덱스에 하나의 key만 저장할 수 있다
# 하나의 인덱스에 두 개 이상의 key 값이 들어갈 경우 충돌이 일어나는데, 
# 이 충돌을 해결하는 것을 Chaining 아라고 한다
# Chaning : 배열 인덱스에 링크드 리스트를 연결해서 충돌을 해결
# Chaning에서 사용하는 링크드 리스트는 data가 아닌,
# key와 value를 값으로 저장한다. (다음 레퍼런스를 담는 것은 동일)
# Chaning 링크드 리스트
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
		self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


# 탐색 메소드
# 탐색 메소드는 특정 데이터를 갖는 노드를 찾는 게 아니라 특정 key를 갖는 노드를 찾는다
# 이에 맞게 링크드 리스트를 처음부터 끝까지 돌면서 원하는 key를 갖는 노드를 리턴해주도록 작성
def find_node_with_key(self, key):
	i = self.head   # 링크드 리스트를 돌기 위해 필요한 노드 변수

    while i is not None:
        if i.key == key:
            return i

        i = iterator.next

    return None


# 추가 메소드 (tail 노드로)
def append(self, key, value):
    New_node = Node(key, value)

    if self.head is None:          # 빈 링크드 리스트라면 head와 tail을 New_node로 지정
        self.head = New_node
        self.tail = New_node
    else:			     	       # 링크드 리스트가 비어있지 않다면
        self.tail.next = New_node  # 기존 tail 노드의 다음 노드로 추가
        New_node.prev = self.tail
        self.tail = New_node  	   # New_node를 새로운 tail 노드로 설정


# 삭제 메소드 (원래 링크드 리스트 삭제 메소드에서 노드를 삭제할 때 삭제하는 노드의 데이터를 리턴하던 부분은 생략)
def delete(self, node_to_delete):

    if node_to_delete is self.head and node_to_delete is self.tail: # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
        self.tail = None
        self.head = None

    elif node_to_delete is self.head: # head 노드를 삭제할 때
        self.head = self.head.next
        self.head.prev = None

    elif node_to_delete is self.tail: # tail 노드를 삭제할 떄
        self.tail = self.tail.prev
        self.tail.next = None

    else:   						  # 두 노드 사이에 있는 데이터 삭제할 때
        node_to_delete.prev.next = node_to_delete.next
        node_to_delete.next.prev = node_to_delete.prev


# 링크드 리스트를 문자열로 표현해서 리턴하는 메소드
def __str__(self):
    res_str = ""

    i = self.head     		# 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.

    while i is not None: 	# 링크드 리스트 끝까지 돌기
        res_str += "{}: {}\n".format(i.key, i.value) # 이 링크드 리스트를 출력했을 때 한 줄에 한 key, value 쌍 하나씩 나오도록
        i = i.next 			# 다음 노드로 넘어간다

    return res_str










