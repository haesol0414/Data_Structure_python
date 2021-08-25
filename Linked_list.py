# 210825
# 링크드 리스트 (linked list)


class Node:
	"""링크드 리스트의 노드 클래스"""
	def __init__(self, data):
		self.data = data # 노드가 저장하는 데이터
		self.next = None # 다음 노드에 대한 레퍼런스



''' -> 링크드 리스트 클래스 구현으로 대체
# 데이터 2,3,5,7,11을 담는 노드 만들기
# 노드 클래스를 이용하여 데이터 삽입 = 노드 인스턴스 생성
# 가장 첫 노드는 헤드노드, 끝 노드는 테일노드라고 부른다.
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)


# 레퍼런스를 활용해서 노드들을 연결하기
head_node.next = node_1   # 첫 노드(헤드 노드)가 가리키는 지점에 두 번째 Node(data, next를 포함하는) 삽입
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node   # 세 번째 Node가 가리키는 지점에 끝 Node(테일노드)를 삽입하여 마지막 노드가 되도록 만듬


# 연결된 노드들을 순서대로 출력
i = head_node   # iterator를 헤드노드로 설정

while i is not None:  # tail 노드는 next 속성이 None 이기 때문에, tail 노드의 값을 출력한 다음에는 i가 None으로 바뀌고, while문이 종료된다.
	print(i.data)
	i = i.next    # 기존 i의 next 레퍼런스 속성이 가리키고 있는 값을 다시 i에 넣어주고, 조건 검사 후 출력

'''



class LinkedList:
	"""링크드 리스트 클래스"""

	def __init__(self): 		# 인스턴스 변수(첫 노드와 끝 노드)들의 기본 값 설정
		self.head = None
		self.tail = None


	# 값 추가 연산 메소드
	def append(self, data):   # 추가하려는 값을 data 파라미터로 받는다
		New_node = Node(data)

		if self.head is None:      # 링크드 리스트가 비어있는 경우
			self.head = New_node   # 처음이자 마지막 노드 New_node 를 삽입
			self.tail = New_node
		else:                            # 링크드 리스트가 비어 있지 않은 경우
			self.tail.next = new_node    # 1. self.tail.next 속성에 New_node 노드를 삽입
			self.tail = new_node         # 2. New_node 기존 끝 노드의 다음에 추가되어 새로운 끝 노드가 되었으므로, 새로운 tail 노드로 설정해준다.


	# 링크드 리스트 인스턴스 생성
	myList_1 = LinkedList()

	# 링크드 리스트 인스턴스에 값 저장하기
	myList_1.append(2)     # 링크드 리스트 클래스의 추가 연산 메소드를 이용해서 값을 삽입
	myList_1.append(3)
	myList_1.append(5)
	myList_1.append(7)
	myList_1.append(11)



	''' -> __str__ 매소드 구현으로 대체
	# 연결된 노드들을 순서대로 출력
	i = myList_1.head   # iterator를 헤드노드로 설정

	while i is not None:  # tail 노드는 next 속성이 None 이기 때문에, tail 노드의 값을 출력한 다음에는 i가 None으로 바뀌고, while문이 종료된다.
		print(i.data)
		i = i.next    # 기존 i의 next 레퍼런스 속성이 가리키고 있는 값을 다시 i에 넣어주고, 조건 검사 후 출력

	'''



	# 링크드 리스트 클래스의 __str__ 메소드
	# 링크드 리스트를 출력할 때 
	# 자동으로 링크드 리스트의 내용을 사람들이 이해할 수 있는 문자열로 리턴해주는 메소드

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|" 	# 처음 출력 문자열 (구분선)
        i = self.head 	# 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 헤드노드로 정의한다.
        
        while i is not None:
            res_str += f" {i.data} |"		 # 각 노드의 데이터를(현재 i에 담겨있는 데이터를) 리턴하는 문자열에 더해준다
            i = i.next  					 # 다음 노드로 넘어간다

        return res_str						 # 리턴하는 문자열




    # 인덱스 번호를 이용해서 원하는 인덱스 번호에 있는 값을 알아내는 메소드. 해당 인덱스 번호의 데이터를 리턴한다
	def find_node_at(self, index): # 파라미터로 원하는 노드의 위치를 나타내는 인덱스를 받는다 (파라미터 인덱스는 항상 있다고 가정)
		i = self.head			   # 원하는 인덱스 번호까지 순차적으로 접근하기 위해 처음 iterator를 헤드노드로 설정 

		for _ in range(index):	   # 원하는 인덱스 번호까지 순차접근
			i = i.next

		return i




	# 출력을 통해 결과 확인하기
	print(myList_1.find_node_at(3).data)       # 3번 인덱스 노드에 접근하여 그 위치의 데이터(.data) 출력
	myList_1.find_node_at(4).data = 13			# 4번 인덱스 노드에 접근하여 그 위치의 데이터(.data) 변경
	print(myList_1)							# myList_1의 데이터 모두 출력
		


	# *링크드 리스트 접근 연산의 시간 복잡도*
	# 인덱스 x에 있는 노드에 접근하려면, 헤드노드에서 다음 노드로 x번 가면 됨
	# 순차적으로 접근하기 때문에 더 뒤에 있는 노드에 접근 할수록, 드는 시간도 늘어난다. 
	# 즉 링크드 리스트 안의 데이터 수가 n개인 경우 : 최악의 경우 = 마지막 인덱스 번호의 데이터에 접근할 때 = 링크드리스트를 처음부터 끝까지 거쳐 가야할 때
	# = 헤드노드에서 다음 노드로 n-1번을 가야함
	# 드는 시간이 n에 비례하기 때문에, 최악의 경우 시간복잡도는 O(n)이 된다.



	# 링크드 리스트의 탐색 연산 메소드 (단, 원하는 데이터가 담긴 노드가 없으면 None을 리턴한다.)
	def find_node_data(self, data):		# 찾고자 하는 데이터를 data 파라미터로 받는다		
		i = self.head 					# 링크드 리스트를 돌기 위해 필요한 노드 변수
        
        while i is not None:
            if i.data == data:			# 만약 i노드의 데이터속성에 찾는 데이터(파라미터로 받은)가 맞다면 i를 리턴한다
                return i
            i = i.next
        return None						# 끝까지 돌았을 때도 원하는 데이터가 없을 경우, None을 리턴한다.
        


    # 노드 삽입 메소드1 (1. 링크드 리스트의 가장 뒤로 삽입 2. 어떠한 두 노드 사이에 삽입)
    def insert_after(self, previous_node, data):
    	New_node = Node(data)				# 새로운 데이터를 저장할 New 노드 생성, 이 노드를 삽입한다

    	if previous_node is self.tail:		# 가장 마지막 순서 노드로 삽입
    		self.tail.next = New_node       # 1. tail노드의 다음 노드로 New_node를 설정
    		self.tail = New_node			# 2. 그 다음, New_node를 tail노드로 설정해준다.
    	else:										# 두 노드 사이에 삽입 
    		New_node.next = previous_node.next		# 1. 삽입할 노드의 앞,뒤 노드 중 앞의 노드(파라미터로 받은 previous_node)가 가리키고 있는 곳(원래 previous_node의 next 속성)이 삽입하고자 하는 노드의 next 속성이 되도록 바꿔준다.
    												# 이 경우 previous_node의 next 속성이 담고 있는 것은 삽입할 노드의 앞,뒤 노드 중 뒤에있는 노드이다. 이것을 previous_node 대신 삽입할 노드(New_node)가 가리킬 수 있도록 바꿔주는 코드이다. 
    		previous_node.next = New_node			# 2. 원래 previous_node의 next에 New_node를 넣는다. (삽입할 노드의 앞,뒤 노드 중 앞의 노드의 next가 삽입할 노드가 되도록)


 
    # 노드 삽입 메소드2 (3. 링크드 리스트의 가장 앞으로 삽입)
    def prepend(self, data):				# 추가할 data를 파라미터로 받는다
    	New_node = Node(data)				# 파라미터로 받은 data를 Node 클래스를 통해 구현한 뒤 New_node에 넣는다 (새로운 노드 인스턴스 생성)

    	if self.head is None:				# 링크드 리스트가 비어있을 경우, New_node를 처음이자 마지막 노드로 생성
    		self.haed = New_node
    		self.tail = New_node
    	else:								# 링크드 리스트가 비어있지 않은 경우
    		New_node.next = self.head
    		self.head = New_node


#210826


    # 노드 삭제 메소드 (1. 링크드 리스트의 테일 노드 삭제 2. 어떠한 두 노드 사이에 있는 노드 삭제)
    def delete_after(self, previous_node):
    	deleted_data = previous_node.next.data      # 메소드 끝에서 리턴해줄 삭제 데이터


    	if previous_node.next is self.tail: 	 	# 지우려는 노드(파라미터로 받은 previous_node의 다음 노드)가 tail 노드일 때
    		previous_node.next = None			 	# 노드를 삭제할 때는 우선 연결관계를 끊어주면 된다. previous_node의 next속성에 아무것도 담기지 않도록 만든다 
    		self.tail = previous_node				# 그 후 previous_node를 tail 노드로 만들어준다.
		else:										# 어떠한 두 노드 사이의 노드를 지울 때
			previous_node.next = previous_node.next.next	# previous_ndoe의 next 속성이 담고있는 것을 삭제할 데이터의 다음, 즉 previous_node의 *다다음 노드*로 설정해준다.


		return deleted_data	 # 링크드 리스트에서 노드를 삭제할 때는 지워주는 노드의 data를 리턴해주는 것이 관습이다



	# 노드 삭제 메소드2 (3. 링크드 리스트의 헤드 노드 삭제)    
	def pop_left(self):
    	deleted_head_data = self.head  # 삭제된 헤드 노드를 리턴해주기 위해 삭제 되기 전 미리 헤드노드를 임의 변수에 담아놓는 코드
    	
    	if self.head is self.tail:     # 링크드 리스트에 노드가 하나만 남아있는 경우
    		self.head = None           # 더 이상 링크드 리스트에서 지우려는 노드를 가리키는 노드는 없다.
    		self.tail = None           # 링크드 리스트의 처음이자 마지막 데이터를 삭제
    	else:						   # 두 개 이상의 노드 링크드 리스트 중 헤드 노드만 삭제할 경우
    		self.head = self.head.next # 헤드 노드의 next 속성 값을 헤드 노드로 설정한다
    		
    	return deleted_head_data		# 삭제된 맨 처음 헤드노드의 데이터 리턴














