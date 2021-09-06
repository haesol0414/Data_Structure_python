
#210904



	# 트리 (Tree)
	# 데이터의 상-하관계를 저장하는 자료 구조 = 계층적 관계
	# 예시로 컴퓨터 폴더 구조, 클래스 상속 관계 역시 계층적 관계에 속한다.
	# 배열이나 링크드 리스트는 선형적 자료 구조로 계층적 데이터를 저장하기에는 적합하지 않다.
	# 딕셔너리, 세트, 우선순위 큐 처럼 다양한 추상 자료형들을 트리를 이용해서 구현 가능하다.
	# 링크드 리스트에서는 한 노드에 데이터와 데이터의 다음 노드를 가리키는 레퍼런스를 저장하는 속성이 담겨있었다.
	# 트리노드는 하위 관계가 있는 노드들을 가리키는 레퍼런스들을 갖는다. (특정 노드의 하위 노드를 자식 노드라고 한다.)
	# 링크드 리스트에서 가장 앞에있는 노드를 haed노드 라고 부르는 것 처럼,
	# 트리에서 가장 상위계층에 있는 노드를 root노드 라고 부른다.


	# 트리 용어
	# root 노드(뿌리 노드): 트리의 시작 노드, 뿌리가 되는 노드. 보통 트리를 표현할 때 가장 위에 root 노드를 놓는 방식으로 나타냅니다.
	# 부모 노드: 특정 노드의 직속 상위 노드.
	# 자식 노드: 특정 노드의 직속 하위 노드.
	# 형제 노드: 같은 부모를 갖는 노드입니다. D와 E는 둘다 그 부모가 B죠? 이럴 때 D와 E는 서로 형제 노드입니다.
	# leaf 노드 (잎/말단 노드): 자식 노드를 갖고 있지 않은, 가장 말단에 있는 노드. 
	# 						트리의 끝에 있다고 해서 root(뿌리) 노드와 반대되는 표현으로 leaf(잎) 노드라고 부른다.
	# 깊이: 특정 노드가 root 노드에서 떨어져 있는 거리. 깊이는 해당 노드로 가기 위해서 root 노드에서 몇 번 아래로 내려와야 하는지를 나타냄.
	#	   결국 깊이라는 건 특정 노드가 root 노드로부터 얼마나 멀리 떨어져 있는지를 나타내는 것이다. 깊이는 리스트의 인덱스처럼 0 이라는 값이 존재한다.
	# 레벨: 깊이 + 1. 깊이랑 거의 똑같은 개념입. 그냥 깊이에 1을 더한 값. 레벨 1에 있는 노드들, 레벨 2에 있는 노드들… 이런식으로 특정 깊이인 노드들을 묶어서 표현할 때 사용하는 용어.
	# 높이: 트리에서 가장 깊이 있는 노드의 깊이.
	# 부분 트리 (sub-tree): 트리의 일부분을 이루고 있는 더 작은 트리. 특정 노드를 root 노드라고 생각하고 바라본다면 여러 가지 부분 트리들을 발견할 수 있다. 하나의 전체 트리에 여러 부분 트리들이 존재하는 것.



	# 이진 트리 (Binary Tree)
	# 각 노드가 최대 2개의 자식만 가질 수 있으면 이진트리라고 부른다.
	# 왼쪽 자식(Left child) & 오른쪽 자식(Right child)으로 구분한다.

	class Node:							# 이진 트리 노드 클래스
		def __init__(self,data):		# 데이터와 두 자식 노드에 대한 레퍼런스를 갖는다
			self.data = data
			self.Lchild = None			# 왼쪽 자식 레퍼런스
			self.Rchild = None			# 오른쪽 자식 레퍼런스


	# 노드 인스턴스 생성		
	root_node = Node(2)
	node_B = Node(3)
	node_C = Node(5)
	node_D = Node(7)
	node_E = Node(11)

	# B와 C를 root노드의 자식 노드로 지정 (B = 왼쪽 자식, C = 오른쪽 자식)
	root_node.Lchild = node_B
	root_node.Rchild = node_B
	# D와 E를 B노드의 자식 노드로 지정 (D = 왼쪽 자식, E = 오른쪽 자식)
	node_B.Lchild = node_D
	node_B.Rchild = node_E



	# 이진 트리의 종류
	# 정 이진 트리 (full binary tree) : 모든 노드가 2개 또는 0개의 자식을 갖는 이진 트리
	# 포화 이진 트리(Perfect binary tree) : 트리의 각 레벨에 노드가 꽉 차있는 이진 트리.
	# 완전 이진 트리(complete binary tree) : 높이가 k일 때 레벨 1부터 k-1까지는 노드가 모두 채워져있고, 마지막 레벨에서는 노드가 꽉 차있지 않아도 되지만 중간에 빈 곳이 있어서는 안된다.
	#									  = 마지막 레벨을 제외한 모든 레벨이 채워지고, 마지막 레벨은 노드가 왼쪽에서 오른쪽으로 채워져있다.
	# 포화이진트리는 항상 완전이진트리이지만 그 역은 항상 성립하지 않는다.


	# 순회 : 자료 구조에 저장된 모든 데이터를 도는 것
	# 트리를 순회하면 계층적인 관계로 저장된 노드들을 선형적으로 나열할 수 있다.
	# pre-order 순회 ( pre : ~ 전에. 데이터를 출력하는 동작이 순회 동작 전에 있다. )
	# pre-order 순회 순서 : 현재 노드의 데이터 출력 -> 재귀적으로 왼쪽 부분 트리 순회 -> 재귀적으로 오른쪽 부분 트리 순회.
	# 전체적으로는 root 노드 출력 -> 왼쪽 부분 트리 모두 출력 -> 오른쪽 부분 트리 모두 출력
	# post-order 순회 ( post : ~ 후에. 데이터를 출력하는 동작이 순회 동작 이후에 있다. )
	# post-order 순회 순서 : 재귀적으로 왼쪽 부분 트리 순회 -> 재귀적으로 오른쪽 부분 트리 순회 -> 현재 노드의 데이터 출력
	# root 노드가 가장 마지막에 출력된다.
	# in-order 순회 ( in : ~ 안에. 데이터를 출력하는 동작이 순회 동작 사이에 있다. )
	# in-order 순회 순서 : 재귀적으로 왼쪽 부분 트리 순회 -> 현재 노드의 데이터 출력 -> 재귀적으로 오른쪽 부분 트리 순회
	# 왼쪽 부분 트리가 모두 출력 된 후 root 노드가 출력되고, 오른쪽 부분 트리가 모두 출력된다.


	# in-order 순회 함수
	def traverse_in_order(node):
	    if node is not None:	# 넘어온 파라미터 node가 None인 경우란, 현재 노드의 왼쪽 자식 노드 또는 오른쪽 자식 노드가 없다는 뜻이므로, 파라미터로 받은 node가 None이 아닐 때만 in-order 순회를 진행하면 됨.
	        traverse_in_order(node.Lchild)  # 재귀적으로 왼쪽 부분 트리 순회
	        print(node.data)  				# 데이터 출력
	        traverse_in_order(node.Rchild)  # 재귀적으로 오른쪽 부분 트리 순회
    
    
	# 힙 (Heap)
	# 힙이 되기 위한 두가지 조건
	# 1. 형태 속성 : 힙은 완전 이진 트리여야 한다. (마지막 레벨 빼고 노드가 모두 채워져 있어야 함, 마지막 레벨은 왼쪽에서 오른쪽으로 노드가 채워져 있어야 함.)
	# 2. 힙 속성 : 모든 부모 노드의 데이터는 자식 노드들의 데이터보다 크거나 같아야 한다.

	# 정렬 : 순서 없는 데이터를 특정 순서에 맞게 재배치 하는 것
	# 정렬 알고리즘 : 데이터를 재배치하는 구체적인 방법 (삽입 정렬, 선택 정렬, 퀵 정렬, 합병 정렬, 힙 정렬 ...)
	
	# 힙 구현하기
	# 힙도 완전 이진트리이므로 동적배열로 구현한다.
	# 왼쪽 자식 인덱스 찾기 : 인덱스 * 2
	# 오른쪽 자식 인덱스 찾기 : 인덱스 * 2 + 1
	# 형태 속성과 힙 속성을 지키고 있는지 확인하고 지키고 있지 않다면 데이터들을 재배치하며 힙을 구현한다.
	# 힙 속성을 지키기 위해 힙을 재배치하는 알고리즘을 heapify 라고 한다.
	# heapify 알고리즘의 최악의 경우는 root노드 부터 맨 밑에 leap노드까지 내려가는 경우이다.
	# 이러한 최악의 경우 시간 복잡도는 O(lg(n))이 된다.
	
	# heapify 함수 구현
	def swap(tree, index_1, index_2): 	# 완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다
	    temp = tree[index_1]
	    tree[index_1] = tree[index_2]
	    tree[index_2] = temp

	def heapify(tree, index, tree_size): # 완전 이진 트리를 나타내는 리스트 tree, heapify하려는 노드의 인덱스 index, 트리로 사용하는 리스트의 길이 tree_size (배열의 0번째 인덱스는 None으로 설정했기 때문에 실제로 총 노드 수보다 1이 크다.)

	    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
	    Lchild_index = 2 * index
	    Rchild_index = 2 * index + 1

	    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

	    # 왼쪽 자식 노드의 값과 비교. 왼쪽 자식 노드의 인덱스가 유효한 범위 내에 있는지 체크하고(and) 데이터의 크기 비교. 
	    # 유효한 범위가 아니라면 노드가 없다는 뜻, 즉 왼쪽 자식 노드가 없다는 뜻이다. 
	    if 0 < Lchild_index < tree_size and tree[largest] < tree[Lchild_index]:
	        largest = Lchild_index

	    # 오른쪽 자식 노드의 값과 비교 (위와 동일)
	    if 0 < Rchild_index < tree_size and tree[largest] < tree[Rchild_index]:
	        largest = Rchild_index

		# 위 코드를 실행한 후에도 largest의 값이 그대로라면
		# 부모 노드가 최댓값을 갖고 있다는 뜻이니까 힙 속성을 만족하고 있다는 뜻이고 더 이상 할 작업이 없음.
	    # 하지만 largest 의 값이 변했다면? -> 맨처음 부모 노드의 값이 가장 클 것이라 가정하고 largest에 부모노드를 넣어 뒀는데, 그 값이 크기 비교 후 더 큰 자식노드의 값으로 바뀌었다면
	    # 왼쪽 자식 노드 또는 오른쪽 자식 노드 중에서 가장 큰 값을 가진 노드가 있었다는 뜻. 그러므로 swap 함수를 사용해서 그 자식 노드와 부모 노드의 위치를 바꿔줘야 한다.
	    if largest != index: 					# 부모 노드의 값이 자식 노드의 값보다 작으면 (largest의 값이 변했다면)
	        swap(tree, index, largest)  		# 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
	        heapify(tree, largest, tree_size)   # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다 (재귀 호출)

	# 실행 코드
	tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
	heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
	print(tree) 

	# 결과 출력
    # [None, 15, 14, 12, 11, 9, 10, 6, 2, 5, 1]


    # 힙 정렬 알고리즘 ( 오름차순 ver. )
    # 1. 힙을 만든다
    # 2. root 노드와 마지막 노드를 바꿔준다
    # 3. 바꾼 노드는 없는 노드 취급한다
    # 4. 새로운 root 노드가 힙 속성을 지킬 수 있게 heapfiy 호출
    # 5. 모든 인덱스를 돌 때 까지 반복
    # ( Q. 내림차순으로 정렬하고 싶으면?
    # 힙 속성을 부모 노드의 데이터가 자식 노드의 데이터보다 커야햔다고 가정한 위의 알고리즘에서,
    # 반대로 부모 노드의 데이터가 자식 노드의 데이터보다 작아야 한다고 가정한 후 실행하면 됨. )


    # 힙 정렬 함수
	def heapsort(tree):
	    tree_size = len(tree)		# tree의 길이를 len함수를 이용해서 받은 후 tree_size 변수에 저장

	    for index in range(tree_size-1, 0, -1): 	# 힙 만들기. 마지막 노드부터 root 노드까지 heapify를 해준다 
													# 첫번째 파라미터가 tree_size-1 이므로 이 값부터 시작하며
													# 두번째 파라미터가 0 이므로 0 까지 동작하고
													# 세번째 파라미터가 -1 이므로 1씩 감소하며
	        heapify(tree, index, tree_size)			# 마지막 노드부터 root 노드까지 heapify를 해준다
	        
	    for i in range(tree_size-1, 0, -1):
	        swap(tree, 1, i) 						 # root 노드와 마지막 인덱스를 바꿔준 후
	        heapify(tree, 1, i)  					 # root 노드에 heapify를 호출한다


	# 우선순위 큐
	# 큐나 스택처럼 추상 자료형이다.
	# 데이터를 저장 하는데, 저장한 데이터가 우선순위 순서대로 나온다.

	# 최대 우선순위 큐 생성
	priority_Q = MaxPriorityQueue()

	# 우선순위 큐에 데이터 삽입
	priority_Q.add(5)
	priority_Q.add(2)
	priority_Q.add(8)

	# 우선순위 큐 데이터 삭제(삭제와 동시에 리턴되므로 추출이라고 부르기도 함)
	print(priority_Q.pop())
	print(priority_Q.pop())
	print(priority_Q.pop())
	# 출력 결과 -> 8 5 2
	# MaxPriorityQueue() 이므로 가장 높은 값의 데이터부터 추출된다.
	# 이처럼 우선순위 큐는 가장 불만도가 높은 문의부터 처리하고 싶을 때, 가장 등급이 높은 고객의 문의부터 처리하고 싶을 때 등
	# 우선순위에 따라 작업을 수행해야 할 때 유용하다.
	# 힙을 사용하면 효율적으로 구현할 수 있다.


	# 힙에 데이터 삽입하기
	# 1. 힙의 마지막 인덱스에 데이터를 삽입한다
	# 2. 삽입한 데이터와 부모 노드의 데이터를 비교한다
	# 3. 부모 노드의 데이터가 더 작으면 둘의 위치를 바꿔준다
	# 4. 새로 삽입한 노드가 힙 속성을 어기지 않는 제 위치를 찾을 때 까지 반복


	# 힙 데이터 삽입 구현하기
	def swap(tree, index_1, index_2): # 완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다
	    temp = tree[index_1]
	    tree[index_1] = tree[index_2]
	    tree[index_2] = temp

	def reverse_heapify(tree, index):   # 파라미터로 받은 자식 노드를 부모노드와 비교해서 자식노드가 부모노드보다 데이터(값)가 크다면 위치를 바꿔주는 함수
										# 2개의 노드(삽입된 index번째의 노드 A, A의 부모 노드)의 값만 비교하면 되기 때문에 구현하는 것이 더 간단함.
	    Pindex = index // 2  			# 삽입된 노드의 인덱스를 이용해 부모 노드의 인덱스 계산

	    if 0 < Pindex < len(tree) and tree[index] > tree[Pindex]:	# 부모 노드가 존재하고(유효 범위 내에 있는지), 부모 노드의 값이 삽입된 노드의 값보다 작을 때
	        swap(tree, index, Pindex) 	   # 만약 부모 노드의 값이 삽입된 노드(자식 노드)의 값보다 작다면, 부모 노드와 삽입된 노드의 위치 교환
	        reverse_heapify(tree, Pindex)  # 삽입된 노드(기존 부모노드보다 더 큰 자식노드를 대상으로 다시 reverse_heapify 호출   


	class PriorityQueue: 			# 힙으로 구현한 우선순위 큐 클래스

	    def __init__(self):
	        self.heap = [None]  	# 파이썬 리스트로 구현한 힙

	    def insert(self, data):		# 삽입 메소드
	        self.heap.append(data) 	# 힙의 마지막에 데이터 추가
	        reverse_heapify(self.heap, len(self.heap)-1)
	        
	    def __str__(self):
	        return str(self.heap)


	# 힙에서 root노드 데이터 추출하기
	# 1. root노드와 마지막 노드(=leaf노드)를 서로 바꿔준다
	# 2. 마지막 노드(=기존의 root노드)의 데이터를 변수에 따로 저장해준다.
	# 3. 마지막 노드(=기존의 root노드)를 삭제한다
	# 4. 새로 지정된 root노드(=기존의 leaf노드)에 heapify를 호출해서 망가진 힙 속성을 바로잡는다.
	# 5. 변수에 저장한 데이터(=최고 우선순위 데이터)를 리턴한다.

    def extract_max(self):  					 # 최우선순위 데이터 추출 메소드
        swap(self.heap, 1, len(self.heap)-1)     # root 노드와 마지막 노드의 위치 바꿈
        max_value = self.heap.pop()              # 힙에서 마지막 노드 추출(삭제)해서 변수에 저장 (list.pop 에 매개변수를 넘겨주지 않으면 default로 -1이 들어감.)
        heapify(self.heap, 1, len(self.heap))    # 새로운 root 노드를 대상으로 heapify 호출해서 힙 속성 유지
        return max_value                         # 최우선순위 데이터 리턴
    




     # 이진 탐색 트리
     # 딕셔너리나 세트 자료형을 구현할 때 사용할 수 있다
     # 이진 탐색 트리는 이진 트리이면서 어떤 속성을 지켜야 한다.
     # * 루트 노드를 기준으로 왼쪽 부분 노드들은 루트 노드의 값보다 작아야 하고
     # * 오른쪽 부분 노드들은 루트 노드의 값보다 커야한다.
     # 이 속성이 바로 이진 탐색 트리 속성이다.
     


     # 이진 탐색 트리 노드와 클래스 구현
     # 힙은 항상 완전 이진 트리이기 때문에 배열로 구현했지만,
     # 이진 탐색 트리는 항상 완전 이진 트리라는 보장이 없다.
     # 그러므로 이진 탐색 트리는 노드 클래스를 정의하여 인스턴스들을 생성하고 연결시켜서 구현한다.

     class Node:			# 이진 탐색 트리 노드 클래스
     	def __init__(self, data):
     		self.data = data
     		self.parent = None
     		self.Lchild = None
     		self.Rchild = None


	def print_inorder(node):
	    if node is not None:	# 넘어온 파라미터 node가 None인 경우란, 현재 노드의 왼쪽 자식 노드 또는 오른쪽 자식 노드가 없다는 뜻이므로, 파라미터로 받은 node가 None이 아닐 때만 in-order 순회를 진행하면 됨.
	        print_inorder(node.Lchild)  # 재귀적으로 왼쪽 부분 트리 순회
	        print(node.data)  				# 데이터 출력
	        print_inorder(node.Rchild)  # 재귀적으로 오른쪽 부분 트리 순회
   

     class BinarySearchTree:	# 이진 탐색 트리 클래스
     	def __init__(self):
     		self.root = None


	    def print_sorted_tree(self):  # 이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드
	        print_inorder(self.root)  # root 노드를 in-order로 출력한다

		     
	    def insert(self, data):	# 이진 탐색 트리 삽입 메소드
	        """이진 탐색 트리 삽입 메소드"""
	        New_node = Node(data)  		# 삽입할 데이터를 갖는 노드를 New_node에 담는다.

	        if self.root is None: 		# 트리가 비었으면 새로운 노드를 root 노드로 만든다
	            self.root = New_node
	            return					# 메소드 종료역할. return이 실행되면 메소드가 종료된다.
       									# return문은 값을 반환하기 위해 쓰이기도 하지만, 메소드나 함수를 종료시키기 위해 쓰이기도 한다.
	        temp = self.root  		  # 저장하려는 위치를 찾기 위해 사용할 변수. root노드로 초기화한다
	        
	        while temp is not None:                      
	            
	            if data > temp.data:  				# 삽입하려는 데이터가 현재 노드 데이터보다 크다면 -> 오른쪽 자식 노드로
	                if temp.Rchild is None:			# 오른쪽 자식이 없으면, 새로운 노드를 현재 노드 오른쪽 자식으로 만듦
	                    New_node.parent = temp		# 새로운 노드의 부모를 temp로 지정 (초기 temp = root노드)
	                    temp.Rchild = New_node		# temp의 오른쪽 자식 노드를 새로운 노드로 지정
	                    return						# 메소드 종료	
	                else:    						# 오른쪽 자식이 있으면 오른쪽 자식으로 간다
	                    temp = temp.Rchild			# 이미 있는 오른쪽 자식을 대상을 temp로 지정해서 다시 New_node와 데이터 크기 비교하고 작업 수행
	            
	            else:  				  				# 삽입하려는 데이터가 현재 노드 데이터보다 작다면 -> 왼쪽 자식 노드로
	                if temp.Lchild is None:     	# 왼쪽 자식이 없으면, 새로운 노드를 현재 노드 왼쪽 자식으로 만듦
	                    New_node.parent = temp		# 새로운 노드의 부모를 temp로 지정 (초기 temp = root노드)
	                    temp.Lchild = New_node  	# temp의 왼쪽 자식 노드를 새로운 노드로 지정
	                    return						# 메소드 종료
	                else:  							# 왼쪽 자식이 있다면 왼쪽 자식으로 간다
	                    temp = temp.Lchild		    # 이미 있는 왼쪽 자식을 대상을 temp로 지정해서 다시 New_node와 데이터 크기 비교하고 작업 수행




  		# 이진 탐색 트리의 탐색 연산 메소드
  		# 1. 주어진 노드의 데이터와 탐색하려는 데이터 비교 (root노드에서 시작)
  		# 2. 탐색하려는 데이터가 더 크면 노드의 오른쪽 자식으로 간다
  		# 2-2. 탐색하려는 데이터가 더 작으면 노드의 왼쪽 자식으로 간다.
  		# 3. 탐색하는 노드를 찾을 때 까지 위 과정을 반복하고 탐색하려는 노드를 찾으면 리턴한다
  		# 이진 탐색 트리의 탐색 연산의 시간 복잡도
  		# 트리의 높이인 h보다 한 단계 더 내려가게 되는 경우 최악의 경우가 되므로,
  		# 최악의 경우 시간 복잡도는 O(h+1), 즉 O(h)가 된다.

	    def search(self, data): 	# 이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다
	        
	        temp = self.root
	        
	        while temp is not None:				
	            if data == temp.data:			# temp.data가 찾고자하는 data이면 
	                return temp 				# temp를 리턴함으로써 메소드를 종료한다.		

	            elif data > temp.data:			# 데이터가 temp(초기엔 root노드)에 있는 data보다 크다면
	                temp = temp.Rchild 			# temp에 오른쪽 자식 노드를 넣는다. (temp의 data가 찾고자하는 data와 같을 때 까지 반복 할 것이기 때문에)

	            elif data < temp.data:			# 데이터가 temp(초기엔 root노드)에 있는 data보다 작다면
	                temp = temp.Lchild 			# temp에 왼쪽 자식 노드를 넣는다. (temp의 data가 찾고자하는 data와 같을 때 까지 반복 할 것이기 때문에)

	            else:
	                return None      			# 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다


	    
	    # 이진 탐색 트리에서 가장 작은 데이터를 가진 노드를 찾아주는 find_min 메소드 - (부분)이진 탐색 트리의 가장 작은 노드 리턴
        # 내가 쓴 메소드 ( 실행 결과 정답 )
	    @staticmethod
	    def find_min(node):
	        if node.Lchild is not None:
	            Ltemp = node.Lchild
	        else:
	            return node
	        while node is not None:
	            if Ltemp.Lchild is None:
	                return Ltemp
	            else:
	                Ltemp = Ltemp.Lchild
	    # 우선 파라미터로 받은 노드의 왼쪽 노드를 새로운 변수 Ltemp에 담아줬다.    
	    # 여기서 Ltemp는 현재 노드의 왼쪽 자식 노드를 의미한다.(이진 탐색 트리이므로 왼쪽 자식은 항상 더 작은 값일 것이기 때문에)      
	    # 처음 if문 : 만약 파라미터로 받은 노드에 왼쪽 자식이 존재한다면 Ltemp에 왼쪽 자식 노드를 담고, 
	    # 그렇지 않다면 파라미터로 받은 노드가 그 트리 안에서 가장 작은 노드일 것이기 때문에 node를 그대로 리턴한다.
	    # while문 안쪽 : 루프를 하나 생성한다. 그리고 Ltemp안에 왼쪽 자식이 존재하지 않을 경우, 처음 파라미터로 받은 노드의 Ltemp가 마지막 왼쪽 자식,
	    # 즉 그 트리 안에서 데이터가 가장 작은 노드일 것이기 때문에 Ltemp를 리턴한다.
	    # 그렇지 않다면 Ltemp에 왼쪽 자식이 또 있다는 뜻이므로, Ltemp에 기존 Ltemp의 왼쪽 자식을 다시 대입하여
	    # Ltemp가 그 트리 안에서의 leaf노드, 즉 가장 작은 노드를 찾을 때 까지 반복된다.
	    # 찾게되면 while문 안 쪽의 if문에 걸리므로, return문을 만나 메소드가 종료된다.


	    # 코드잇 해석 정답 메소드
		def find_min(node):
		    temp = node  # 도우미 변수. 파라미터 node로 초기화

		    while temp.left_child is not None:
		        temp = temp.left_child      # temp가 node를 뿌리로 갖는 부분 트리에서 가장 작은 노드일 때까지 (왼쪽 자식 노드가 존재하는 동안에는 계속) 왼쪽 자식 노드로 간다

		    return temp 					# 왼쪽 자식 노드가 없는경우, None일 경우 temp 리턴
		# 내 코드에 비해서 간략하다. 이렇게 해도 temp노드가 처음이자 마지막 노드일 경우에도 while문 조건을 통해
		# 바로 걸러지기 때문에 내 코드의 if문을 적을 필요가 없이 간결하게 쓸 수 있다. 코드를 더욱 간략화해서 쓸 수있도록 고민해야겠다.



