#210830


    # 해시 테이블 (Hash Table)
    # key - value : 하나의 key는 하나의 value만 저장할 수 있다
    # Direct Asses Table : key 값으로 인덱스를 설정한다. key 값의 범위가 커질수록 메모리 공간이 낭비될 수 있다.
    # 해시 함수 : 특정 값을 원하는 범위의 자연수로 바꿔주는 함수
    # 해시 테이블은, 고정된 크기의 배열을 만들고, 해시 함수를 이용해서 key를 원하는 범위의 자연수로 바꾼다
    # 그 후 해시 함수 결과값 인덱스에 key-value 쌍을 저장한다. (주어진 key를 원하는 범위의 자연수로 바꿔서 리턴해줌)

    # 두 키를 해시 함수에 넣었을 때, 결과가 똑같이 나오는 경우 충돌이 일어날 수 있다.
    # 해시 함수 충돌 해결 1. Chaning - 쇠사슬처럼 엮기
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

            i = i.next

        return None     # 찾고 있는 키가 없을 경우 None 리턴


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



#210831


    # Chaning을 쓰는 해시 테이블의 연산별 시간 복잡도

    # - 해시 테이블 탐색 연산 시간복잡도
    # 1단계 : 해시 함수 계산 = O(1)
    # 2단계 : 해시 함수의 결과를 이용해서 인덱스 접근 = O(1)
    # 3단계 : 링크드 리스트 탐색 = (선형 탐색이기 때문에 최악의 경우) O(n)
    # 총 합 : O(1+1+n) = O(n)

    # - 해시 테이블 삽입 연산 시간복잡도
    # 1단계 : 해시 함수 계산 = O(1)
    # 2단계 : 해시 함수의 결과를 이용해서 인덱스 접근 = O(1)
    # 3단계 : 링크드 리스트 노드 탐색 = (선형 탐색이기 때문에 최악의 경우) O(n)
    # 삽입 연산과정에서 탐색 시 같은 key를 삽입한다면 value를 삽입할 값으로 수정한다. 탐색 후에 삽입하려는 key가 없을 경우에 맨 끝에 노드 추가.
    # 4단계 : 링크드 리스트 노드 삽입 / 노드 수정 = O(1)
    # 총 합 : O(1+1+n+1) = O(n)

    # - 해시 테이블 삭제 연산 시간복잡도
    # 1단계 : 해시 함수 계산 = O(1)
    # 2단계 : 해시 함수의 결과를 이용해서 인덱스 접근 = O(1)
    # 3단계 : 링크드 리스트 노드 탐색 = (선형 탐색이기 때문에 최악의 경우) O(n)
    # 4단계 : 링크드 리스트 노드 삭제 = O(1)
    # 총 합 : O(1+1+n+1) = O(n)


    # 각 배열의 인덱스에 저장된 링크드 리스트들의 평균 길이
    # 총 들어 있는 key - value 쌍 수를 배열 인덱스 수로 나눔.
    # 해시 테이블에 총 들어가 있는 key - value 쌍의 수: n
    # 해시 테이블이 사용하는 배열의 크기: m 일 경우,
    # 링크드 리스트들의 평균 길이는 m분의 n


    # 해시 테이블 평균 시간 복잡도
    # 즉, 각 연산들은 평균적으로 "O(m분의 n)이 걸린다"고 표현할 수 있음.
    # 해시 테이블을 만들 때 총 저장하는 key - value 쌍 수와 해시 테이블이 사용하는 배열의 크기를 비슷하거나 작다고 가정을 함
    # 해시 테이블을 사용할 때는 항상 어느 정도까지는 n = m 이렇게 유지 시켜준다면 
    # 해시 테이블 연산들의 평균 시간 복잡도는 O(1)이라고 표현할 수 있다.
    # 다시 한번 정확하게 표현한다면 "해시 테이블 삽입, 삭제, 탐색 연산들은 최악의 경우 O(n)이 걸리지만, 평균적으로는 O(1)이 걸린다"라고 할 수 있다.



    # Chaning을 쓰는 해시테이블 구현
    from HDLL import LinkedList  # 해시 테이블에서 사용할 링크드 리스트 임포트

    class HashTable:             # 해시 테이블 클래스


        def __init__(self, capacity):
            
            self._capacity = capacity                                    # 파이썬 리스트 수용 크기 저장
            self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 빈 링크드 리스트 저장



        def _hash_function(self, key):              # 주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드 (주의: key는 파이썬 불변 타입이여야 한다.)
            
            return hash(key) % self._capacity
            
            
            
        def _get_linked_list_for_key(self, key):    # 파라미터로 key를 받아서 그 key에 해당하는 인덱스에 있는 링크드 리스트를 리턴
            hashed_index = self._hash_function(key) # 해시 함수에 key를 넣어서 나온 결과 값을 변수 hashed_index에 저장

            return self._table[hashed_index]        # 내부적으로 배열로 사용하는 self._table의 hashed_index 인덱스에 있는 링크드 리스트를 리턴       
            
            

        def _look_up_node(self, key):               # 파라미터로 받은 key를 갖고 있는 링크드 리스트 노드를 리턴하는 메소드
            
            linked_list = self._get_linked_list_for_key(key) # 배열의 원하는 인덱스에 있는 링크드 리스트를 가져옴
            
            return linked_list.find_node_with_key(key)       # 이 링크드 리스트 안에서 원하는 key를 갖고 있는 노드를 탐색해서 리턴
            

            
        def look_up_value(self, key):                # 주어진 key에 해당하는 데이터를 리턴하는 메소드
            
            return self._look_up_node(key).value
            # 찾으려는 key를 파라미터로 받은 후 _look_up_node 메소드를 이용해서 원하는 key에 해당하는 노드를 찾고
            # 이 노드의 value 변수를 리턴

            
            
        def insert(self, key, value):                # 새로운 key - value 쌍을 삽입시켜주는 메소드 (이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다)
            
            existing_node = self._look_up_node(key)  # 이미 저장된 key인지 확인한다

            if existing_node is not None:
                existing_node.value = value          # 이미 저장된 key면 데이터만 바꿔주고
            else:                                    
                linked_list = self._get_linked_list_for_key(key)
                linked_list.append(key, value)       # 없는 key면 링크드 리스트에 새롭게 삽입시켜준다



        def delete_by_key(self, key):                 # 주어진 key에 해당하는 key - value 쌍을 삭제하는 메소드
            
            node_to_delete = self._look_up_node(key)  # 이미 저장된 key인지 확인한다


            if node_to_delete is not None:            # 저장되어 있는 key면 삭제한다
                linked_list = self._get_linked_list_for_key(key)
                linked_list.delete(node_to_delete)



        def __str__(self):  # 해시 테이블 문자열 메소드
            res_str = ""

            for linked_list in self._table:
                res_str += str(linked_list)

            return res_str[:-1]

        


    # 해시 함수 충돌 해결 2. Open Addressing
    # 해시 함수가 같은 인덱스 값으로 충돌했을 때 Chaning 처럼 한 인덱스에 링크드 리스트로 연결하는 것이 아닌,
    # 비어있는 다른 인덱스를 찾는다.
    # 선형 탐사(Linear probing) : 충돌이 일어났을 때, 바로 뒤 인덱스들을 한 칸씩 보며 빈 인덱스를 찾는 방법 - 빈 인덱스를 찾을 때 하나씩 순서대로, 선형적으로 찾음.
    # 제곱 탐사(Quadratic Probing) : 선형적으로 바로 다음 인덱스들을 하나씩 확인하지 않고, 제곱을 한 값들을 이용해서 인덱스를 찾음. (1의 제곱은 1이므로 한칸 뒤, 2의 제곱은 4이므로 4칸 뒤 ...)
    # Open Addressing 탐색/삭제 연산 주의사항
    # 탐색 하다가 빈 익덱스가 나오면 데이터가 저장되지 않았다고 인식하여, 뒤에 찾고자 하는 데이터가 저장되어 있어도 탐색을 종료해버린다.
    # 그렇기 때문에 데이터가 삭제된 빈 자리에는 'DELETE' 등의 약속된 표시를 해주어야 한다.

    

    # 해시테이블을 기반으로 구현된 파이썬의 자료형 딕셔너리
    # 데이터 간 순서 관계에 구애받지 않음.
    # 1. key-value 데이터 쌍 삽입
    # 2. key를 이용한 데이터 탐색
    # 3. key를 이용한 데이터 삭제

    grade = {}           # {}를 이용해서 딕셔너리 사용하기

    grade["어피치"] = 90   # key - value 데이터 삽입
    grade["무지"] = 80
    grade["라이언"] = 70

    print(grade["무지"])  # key를 이용해서 value 탐색 (key[무지]의 data인 80이 출력됨.)

    grade.pop("라이언")    # key를 이용한 삭제. 라이언 key-value 쌍이 삭제됨.

    # 딕셔너리 연산에 따른 시간 복잡도
    # 연산종류    코드                        시간복잡도
    # 탐색       dict1["키이름"]             O(1) (평균)
    # 삽입       dict1["키이름"] = 데이터      O(1) (평균)
    # 삭제       del dict1["키이름"]         O(1) (평균)
    #           dict1.pop("키이름")
    # 길이 확인   len(dict1)                 O(1)



    # 해시테이블을 기반으로 구현된 파이썬의 자료형 set
    # 데이터 간 순서 관계에 구애받지 않음.
    # 접근, 삽입, 삭제 연산이 가능함.

    classes = set()           # 세트 자료형 사용하기
    
    classes.add("컴퓨터개론")    # 세트에 데이터 추가
    classes.add("자료구조")

    print("자료구조" in classes) # 세트 안 데이터 탐색 (true/false 리턴)

    classes.remove("컴퓨터개론") # 데이터 삭제 (.remove 메소드 이용)

    # 세트 연산에 따른 시간 복잡도
    # 연산종류    코드                        시간복잡도
    # 탐색  "데이터" in set1                O(1) (평균)
    # 삽입  set1.add("데이터")              O(1) (평균)
    # 삭제  set1.remove("데이터")           O(1) (평균)
    #      set1.pop("데이터")              
    # 길이 확인   len(set1)                 O(1)














