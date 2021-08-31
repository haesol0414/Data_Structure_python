


#210901



    # 기능과 구현
    # 기능 : 연산이 '무엇'을 하는지 (ex. 삽입 연산의 기능 = 순서 데이터에서 원하는 위치에 데이터를 저장)
    # 구현 : 기능을 '어떻게' 하는지 (ex. 동적배열에서의 삽입 연산 방법이 다르고, 링크드리스트에서의 삽입 연산 방법이 다르듯이 삽입 이라는 '기능'을 '어떻게' 처리하는지)
    
    # 추상화
    # '기능'은 알아도 '구현'을 어떻게 하는지는 몰라도 되는 것.
    # 파이썬은 추상화가 많이된 고수준 언어이다. 즉, 개발자들이 구현보다 기능에 더 집중할 수 있게 해줌.
    # 그렇기 때문에 많은 자료형의 이름이 추상 자료형 이름과 같은 경우가 많다. (ex. List[] - 파이썬의 리스트는 내부적으로 동적 배열로 구현되어 있음.)

    # 추상 자료형 (Abstruct Data Type)
    # 자료 구조를 추상화 한 것
    # 데이터를 저장하거나 사용할 때 '기능'만 생각

    # 추상 자료형 vs 자료 구조 ?
    # 기능을 중점적으로 얘기하고 싶을 때나, 흐름을 생각할 때와 같이 구현에 집중할 필요가 없을 때 추상 자료형을
    # 코드의 성능을 분석하거나 최적화 시켜야 될 때(성능을 최대로 끌어올리고 싶을 때)는 자료 구조를 중심적으로 생각하면 된다.





    # 큐 (Queue)
    # 마트에서 물건을 살 때 줄을 서는 것을 생각 해보면, 맨 앞 사람부터 계산을 한 뒤 밖으로 나가고, 맨 뒤부터 줄을 선다.
    # 큐는 마트에서 줄을 서는 것 처럼, 데이터를 삭제할 때는 맨 앞에서만 삭제하고, 데이터를 삽입할 때는 맨 뒤에 삽입 해주는 추상 자료형이다.
    # 이것을 FIFO : First-in-First-out 라고도 한다.
    # 큐의 연산들
    # 1. 맨 뒤 데이터 추가
    # 2. 맨 앞 데이터 삭제
    # 3. 맨 앞 데이터 접근
    # 더블리 링크드 리스트의 맨 앞 데이터 삭제, 맨 뒤 데이터 삽입, 맨 뒤 데이터 접근 연산의 시간 복잡도가 O(1)이기 때문에,
    # 큐가 가지고 있는 3가지 연산들은 더블리 링크드 리스트로 구현하면 가장 빠르고 효율적이게 사용할 수 있다.


    # 파이썬에서는 * deque * 라는 자료형을 사용해서 큐를 쓸 수 있다 (deque : doubly-ended-queue의 약자. 즉 양면 큐)

    from collections import deque          # deque는 파이썬 collections모듈에서 import해온다

    queue = deque()       # 비어있는 deque 생성

    queue.append("일")     # 큐의 맨 끝에 데이터 삽입
    queue.append("이")     # 큐의 맨 끝에 데이터 삽입
    queue.append("삼")     # 큐의 맨 끝에 데이터 삽입

    queue.popleft()        # popleft()메소드를 사용해서 큐의 맨 잎 데이터를 삭제. 가장 앞에있는 데이터인 "일"이 삭제된다.
                           # popleft() 메소드는 맨 앞 데이터를 삭제하기도 하지만, 삭제하는 데이터를 리턴하기도 한다.



    # 서비스 센터 문의 처리 프로그램 (코드 출처 : 코드잇)
    # 접수 순서대로 처리

    from collections import deque

    class CustomerComplaint:            # 문의를 나타내는 클래스
        def __init__(self, name, email, content):
            self.name = name
            self.email = email
            self.content = content

            
    class CustomerServiceCenter:        # 호텔 서비스 센터 클래스
        def __init__(self):
            self.queue = deque()        # 대기 중인 문의를 저장할 큐 생성


        def process_complaint(self):    # 접수된 고객 센터 문의 내용 처리하는 메소드

            if self.queue:                                            # 대기 중인 문의가 있는지 확인 (다른 여러 데이터 항목을 담는 자료형과 마찬가지로 deque가 비었는지 확인하는 방법은 if 뒤에 deque로 만든 인스턴스를 넣으면 됨)
                complaint = self.queue.popleft()                      # 가장 오래된 문의 먼저 처리
                print(f"{complaint.name}님의 {complaint.content} 문의 내용 접수 되었습니다. 담당자가 배정되면 {complaint.email}로 연락드리겠습니다!")
                # deque에 popleft() 메소드를 사용하면 큐의 가장 앞에 저장되어 있는 데이터를 삭제하는 동시에 큐에서 삭제하는 데이터를 리턴받을 수 있음
                # 큐에서 삭제하면서 리턴받는 데이터의 속성을 이용하여 문의 처리 메시지를 출력
            else:
                print("더 이상 대기 중인 문의가 없습니다!")


        def add_complaint(self, name, email, content):                 # 새로운 문의를 큐에 추가 시켜주는 메소드
            New_complaint = CustomerComplaint(name, email, content)    # CustomerComplaint 클래스를 활용해서 새 문의 인스턴스 생성
            self.queue.append(New_complaint)                           # 문의 대기 큐에 추가 시켜준다























