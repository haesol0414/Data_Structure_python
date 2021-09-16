


#210913

	# 그래프 (Graph)
	# 연결 데이터를 저장할 수 있는 자료구조
	# 연결 관계를 컴퓨터로 표현하기 위한 자료구조이다.

	# 그래프의 용도
	# 자료구조는 데이터 사이의 관계에 따라 어느것이 더 효율적인지 따져본 후 선택해야한다. 
	# 앞과 뒤라는 관계를 저장하고 싶으면 배열이나 링크드 리스트, 계층 관계를 저장하고 싶으면 트리를 사용하면 되는데,
	# 그래프는 데이터 간의 연결관계를 저장하고 싶을 때 유용하게 쓰인다. 
	# (ex. 페이스북 알만한 친구 추천, 위치에서 가장 빠른 경로 찾기)

	# 그래프 용어
	# 링크드 리스트와 같이 그래프도 노드를 하나의 데이터 단위로 활용한다. = 그래프 노드
	# 그래프에서 노드들 사이에 있는 연결 관계를 '엣지' 라고 한다.
	# (A, B)엣지 / (B, A)엣지
	# 두 데이터가 엣지가 존재할 때, 서로 '인접해있다'고 표현한다. 반대로 직접적인 엣지가 없다면 '인접해있지 않다'라는 말과 같다.
	# 두 데이터가 인접해있지는 않지만, 다른 하나의 공통된 데이터로 엣지가 연결되어 있다면, 인접해있지 않은 두 데이터를 연결해주는 엣지들을 '경로' 라고 한다.
	# 경로에 있는 모든 엣지의 수는 '거리'라고 한다. 거리가 가장 적은 경로가 최단경로이다.
	# 한 노드에서 시작해서 같은 노드에서 끝나는 것을 '싸이클'이라고 한다. (한 노드에서 시작해서 같은 노드로 돌아오는 경로)
	# '차수'는 한 노드에 연결된 엣지의 갯수를 말한다.

	# 방향 그래프
	# 그래프의 엣지는 연결되어있을 뿐만 아니라 방향 그래프로도 나타낼 수 있다. (ex. 인스타그램 팔로우)
	# 방향 그래프에서는 엣지들이 방향을 갖기 때문에, 엣지가 양방향이 아닐 수도 있다.
	# 방향 그래프에서 경로에도 방향이 있는데, 쌍방향이 아닐 수도 있기 때문에 어떤 데이터에 한해서는 경로가 아예 없을 수도 있다.
	# 방향 그래프에서 차수는 출력차수와 입력차수로 나뉜다.
	# 노드에서 나가는 엣지의 수(ex. 팔로잉)를 출력 차수, 들어오는 엣지의 수(ex. 팔로워)를 입력 차수라고 한다.

	# 가중치 그래프
	# 엣지에 특정 숫자값을 지정
	# 경로의 거리 개념이 바뀐다. 가중치 그래프에서 거리는 경로에 있는 모든 엣지 가중치의 합이다.



#210914



	# 지하철 역 노드
	class StationNode:
		def __init__(self, name, num_exits):
			self.name = name
			self.num_exits = num_exits

	# 지하철 역 노드 인스턴스 생성
	station_0 = StationNode("교대역", 14)
	station_1 = StationNode("사당역", 14)
	station_2 = StationNode("종로3가역", 14)
	station_3 = StationNode("서울역", 14)

	# 노드들을 리스트에 저장하기
	stations = [station_0, station_1, station_2, station_3]

	# 노드들을 딕셔너리에 저장하기
	stations = {
				"교대역": station_0
				"사당역": station_1
				"종로3가역": station_2
				"서울역": station_3
				}
    # 단, 이 방법을 쓸 때는 키가 중복되지 않도록 주의해야 한다.



    # 엣지 구현 : 인접 행렬
    # 인접 : 두 노드가 연결 되었다. 인접해있다.
    # 행렬 : 2차원 배열. 2차원 리스트. ( = 리스트 안에 리스트가 있다. )
    # 즉 인접 행렬이란, 노드들의 연결관계를 나타내는 2차원 리스트.
    # 인덱스를 이용해 표현된 2차원 배열에서 인접해있다면 1, 인접해있지 않다면 0을 표시한다.
    # 가중치가 있는 그래프라면, 1대신에 가중치 값을 저장하면 된다. 
    # 방향이 있는 그래프라면, 방향이 있는 엣지는 1로, 그렇지 않은 엣지는 0으로 표기하면 된다.
    # 각 노드들을 리스트에 저장해 고유 정수 인덱스를 준다.
    # 노드 수 X 노드 수 크기의 행렬을 만든다.
    # 노드들의 엣지 유무 혹은 가중치에 따라 행렬의 요소를 채운다.



    # 엣지 구현 : 인접 리스트
    # 그래프 노드가 연결된 노드들에 대한 레퍼런스를 저장한다.
    # 방향 그래프에서 엣지가 떠나는 노드의 인접 리스트에만 엣지가 들어가는 노드를 저장해준다.
    # 여러개의 노드가 있고 하나의 노드는 각자 자신이 인접한 노드들에 대한 레퍼런스를 저장하고 있는 것이다.
    


#210915



	# 그래프 탐색(= 순회)
	# : 하나의 시작점 노드에서 연결된 노드들을 모두 찾는 것
	# 그래프 탐색 알고리즘은 각 노드들을 어떤 순서로 탐색하는지에 따라 두 종류로 나뉜다.
	# 1. Breadth First Search (BFS) / 2. Depth First Search (DFS)


	# Breadth First Search (BFS)
	# Breadth 너비 First 우선 Search 탐색
	# 너비를 우선적으로, 즉 수평적으로 탐색함 (--> 방향) 


	# BFS 알고리즘
	# 큐는 BFS 알고리즘에서 굉장히 중요한 역할을 함. ( 큐 = FIFO )
	# 단계 ::
	# 시작 노드를 방문 표시 후, 큐에 넣음
	# 큐에 아무 노드가 없을 때 까지 :
	# 			큐 가장 앞 노드를 꺼낸다
	#			꺼낸 노드에 인접한 노드들을 모두 보면서 :
	#								처음 방문한 노드면 :
	#										방문한 노드 표시를 해준다
	#										큐에 넣어준다
	# 노드들을 모두 방문했고, 큐에 아무 노드가 없을 때 까지 이 과정을 반복한다.


	# BFS로 연결된 역 찾기 (연결 되었다면 True, 연결되지 않았다면 False를 출력함)
	# 지하철 역을 나타내는 클래스
	class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name			# 역 이름
        self.adjacent_stations = []					# 인접한 역
        self.visited = False						# 노드 방문 여부

    def add_connection(self, station): 			    # 파라미터로 받은 역과 엣지를 만들어주는 메소드
        self.adjacent_stations.append(station)
        station.adjacent_stations.append(self)


	# 시작 노드에서 BFS를 실행하는 함수
	def bfs(graph, start_node):
    queue = deque()  # 빈 큐 생성

    for station_node in graph.values(): 	# 모든 노드를 방문하지 않은 노드로 표시
        station_node.visited = False

    start_node.visited = True   		# 시작점 노드를 방문 표시한 후 큐에 넣어준다
    queue.append(start_node)
    
    while queue:  										 	 # 큐에 노드가 있는 동안
        current_station = queue.popleft() 					 # 큐의 가장 앞 데이터를 갖고 온다
        for neighbor in current_station.adjacent_stations:   # 인접한 노드를 돌면서
            if not neighbor.visited:  						 # 방문하지 않은 노드면
                neighbor.visited = True  					 # 방문 표시를 하고
                queue.append(neighbor) 						 # 큐에 넣는다
	# 노드들을 모두 방문했고, 큐에 아무 노드가 없을 때 까지 이 과정을 반복.



    # ** popleft() 메소드는 가장 앞에서부터 데이터를 삭제 및 추출하고 (큐에 적합),
    # pop() 메소드는 가장 뒤에서부터 데이터를 삭제 및 추출한다 (스택에 적합).



	# Depth First Search (DFS)
	# Depth 깊이 First 우선 Search 탐색
	# 깊이를 우선적으로 탐색함 ( 시작 노드에서부터 아래로 )


	# DFS 알고리즘
	# DFS 알고리즘에선 스택이 중요한 역할을 함. ( 스택 = LIFO )
	# 시작 노드와 인접한 노드들을 스택에 넣고, 마지막으로 삽입된 노드부터 순서대로 꺼내서 깊이 우선으로 처리함.
	# 단계 ::
	# 시작 노드를 방문 표시 후, 스택에 넣음.
	# 스택에 아무 노드가 없을 때 까지 :
	# 			스택의 가장 위 노드를 꺼낸다
	#			노드를 방문 처리 한다
	#					인접한 노드들을 모두 보면서 : 
	#							처음 방문하거나 스택에 없는 노드면 :
	#											 		스택에 넣어준다
	# 노드들을 모두 방문했고, 스택에 아무 노드가 없을 때 까지 이 과정을 반복한다.


	# DFS로 연결된 역 찾기 ( visited 가 0이면 연결되지 않은 노드, 1이면 스택에 들어가 있는 노드, 2면 연결된 노드 )
	def dfs(graph, start_node):
	    stack = deque()  # 빈 스택 생성

	    for station_node in graph.values():  		# 모든 노드를 처음 보는 노드로 초기화
	        station_node.visited = 0

	    start_node.visited = 1  				# 시작 노드를 스택에 넣는다는 표시(옅은 회색)를 하고
	    stack.append(start_node)  				# 스택에 넣음

	    while stack: 							 # 스택에 노드가 남아 있을 때까지
	        current_node = stack.pop()  		 # 스택 가장 위(뒤) 데이터를 갖고 온다
	        current_node.visited = 2  			 # 현재 노드를 방문 표시한다
	        for neighbor in current_node.adjacent_stations:		# 인접한 노드들을 모두 보면서
	            if neighbor.visited == 0:  		# 처음 보는 노드들만
	                neighbor.visited = 1  		# 스택에 넣는다는 표시를 하고
	                stack.append(neighbor)  	# 스택에 넣음
	# 노드들을 모두 방문했고, 스택에 아무 노드가 없을 때 까지 이 과정을 반복.




#210916



	# 최단경로 알고리즘
	# 최단경로 : 경로에 있는 모든 엣지의 수는 '거리' 라고 한다. 거리가 가장 적은 경로가 최단경로이다.
	# 즉, 두 노드 사이 경로 중 거리가 가장 짧은 경로가 최단경로이다.
	# 그래프도 방향, 무방향, 가중치, 비가중치, 음수 엣지 유무, 싸이클 유무에 따라 최단경로가 다르다.
	# 최단경로 알고리즘은 그래프의 특성에 따라 다를 수 있다.
	# 비 가중치 그래프에서 사용할 수 있는 최단경로 알고리즘은 BFS, 가중치 그래프에서는 Dijkstra 알고리즘을 사용할 수 있다.


	# 그래프를 탐색할 때 사용한 BFS 알고리즘을 조금만 수정해주면 최단경로 알고리즘으로 사용할 수 있다.
	# 탐색 BFS 알고리즘에서는 노드 방문 여부를 visited 변수에 저장했었다.
	# 최단경로 알고리즘에서는 여기에 predecessor 변수를 추가로 저장한다. (predecessor : ~이전의 것)
	# predecessor 변수는 현재 방문중인 노드가 어떤 노드를 통해 왔는지를 저장한다. (시작 노드의 predecessor는 None이다)
	# 큐를 통한 BFS 알고리즘으로 노드 방문 여부와 그 노드가 어떤 노드를 통해 왔는지를 모두 저장하고 나면,
	# 최단 경로를 알고싶은 두 노드가 있을 때, 도착 노드에서부터 시작 노드까지 predecessor를 찾아간다.
	# 이 경로가 최단경로가 된다. 도착점부터 시작점까지 Backtracking하는 것.


	# 최단경로용 BFS - 비가중치 그래프의 최단경로
	# 단계 ::
	# 시작 노드를 방문 표시 후, 큐에 넣음
	# 큐에 아무 노드가 없을 때 까지 :
	# 			큐 가장 앞 노드를 꺼낸다
	#			꺼낸 노드에 인접한 노드들을 모두 보면서 :
	#								처음 방문한 노드면 :
	#										방문한 노드 표시를 해준다
	# 										predecessor 변수를 큐에서 꺼낸 노드로 설정한다
	#										큐에 넣어준다
	# 노드들을 모두 방문했고, 큐에 아무 노드가 없을 때 까지 이 과정을 반복한다.
	# Backtracking 과정
	# 현재 노드를 경로에 추가한다
	# 현재 노드의 predecessor로 간다
	# predecessor가 없을 때 까지 위 단계들을 반복


	# 최단 경로용 BFS 함수
	def bfs(graph, start_node):
	    queue = deque()  # 빈 큐 생성

	    for station_node in graph.values():		# 모든 노드를 방문하지 않은 노드로 표시, 모든 predecessor는 None으로 초기화
	        station_node.visited = False
	        station_node.predecessor = None

	    start_node.visited = True		 # 시작점 노드를 방문 표시한 후 큐에 넣어준다
	    queue.append(start_node)
	    
	    while queue:  									# 큐에 노드가 있을 때까지
	        current_station = queue.popleft()  			# 큐의 가장 앞 데이터를 갖고 온다
	        for neighbor in current_station.adjacent_stations:  # 인접한 노드를 돌면서
	            if not neighbor.visited: 			    # 방문하지 않은 노드면
	                neighbor.visited = True  			# 방문 표시를 하고
	                neighbor.predecessor = current_station  # 이 노드가 어디서 왔는지 표시 
	                queue.append(neighbor)  				# 큐에 넣는다


	def back_track(destination_node ): 	# 최단 경로를 찾기 위한 back tracking 함수
	    res_str = ""  					# 리턴할 결과 문자열
	    temp = destination_node  		# 도착 노드에서 시작 노드까지 찾아가는 데 사용할 변수

	    while temp is not None: 		# 시작 노드까지 갈 때까지
	        res_str = f"{temp.station_name} {res_str}"  # 결과 문자열에 역 이름을 더하고
	        temp = temp.predecessor  	# temp를 다음 노드로 바꿔준다

	    return res_str
	    


	# Dijkstra 알고리즘 - 가중치 그래프의 최단경로
	# distance 변수 : 특정 노드까지의 최단 거리 예상치 ( 현재까지 아는 정보로 계산한 최단거리 )
	# predecessor 변수 : 현재까지 찾은 최단 경로에서 바로 직전의 노드
	# complete 변수 : 노드까지의 최단 경로를 찾았다고 표시하기 위한 변수 (boolean)
	# 엣지 Relaxation
	# Dijkstra 알고리즘에서 노드들을 방문하면서 해당 노드들의 distance와 predecessor를 바꾸는 것을 엣지를 Relax한다고 표현한다.
	# 최단거리 예상 값을 줄여나가는 것이라고 이해하면 됨
	# Dijkstra 알고리즘
	# 단계 ::
	# 시작점의 distance를 0으로, predecessor를 None으로 설정
	# 모든 노드가 complete일 때 까지 :
	# 			complete하지 않은 노드 중 distance가 가장 작은 노드 선택
	#			이 노드에 인접한 노드 중 complete하지 않은 노드를 돌면서 :
	#								각 엣지를 relax한다
	#			현재 노드를 complete 처리한다

