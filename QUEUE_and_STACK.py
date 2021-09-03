

    # QUEUE and STACK



#210901



    # 기능과 구현?
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
    # 많은 경우 프로그래밍을 할 때 각 단계에서 “무엇”을 할지를 “어떻게” 할지 보다 먼저 떠올리게 되는 경우가 대부분이다.
    # 순수하게 “무엇”에 해당하는 개념이 추상 자료형, 
    # “어떻게”에 해당하는 개념이 자료 구조기 때문에 자료 구조 보다 추상 자료형을 먼저 떠올리게 되는 경우가 많음.


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




#210902


    

    # 스택 (STACK)
    # 접시를 쌓을 때를 생각 해보면, 맨 위에 쌓고, 뺄 때도 맨 위에서 부터 뺀다.
    # 스택도 접시를 쌓을 때와 마찬가지로 데이터가 가장 위로 쌓이고, 삭제 될 때는 가장 위에 있는 데이터부터 삭제된다.
    # LIFO : Last-In-First-Out (가장 마지막에 들어온 데이터가 가장 먼저 삭제된다)
    # 스택의 연산들
    # 1. 맨 뒤 데이터 추가
    # 2. 맨 뒤 데이터 삭제
    # 3. 맨 뒤 데이터 접근


    # 파이썬에서 스택을 사용할 때도 deque를 사용한다.
    from collections import deque
    stack = deque().    # 사용할 스택 정의

    stack.append("일")  # 맨 뒤 데이터 추가
    print(stack[-1])   # 맨 뒤 데이터 접근
    stack.pop()        # pop 메소드로 맨 끝 데이터를 삭제한다. popleft 메소드와 마찬가지로 삭제된 데이터를 삭제와 동시에 리턴한다.
    # stack을 사용 할 때 시간복잡도의 효율성은 동적배열(List)로 구현하나 더블리 링크드 리스트(Deque)로 구현하나 별 차이가 없다.
    


#210903



    # stack을 이용한 괄호 짝 찾기 프로그램 (코드 출처 : 코드잇)


    from collections import deque

    def parentheses_checker(string):            # 주어진 문자열의 모든 괄호가 짝이 있는지 확인해주는 메소드

        print(f"테스트하는 문자열: {string}")        # 파라미터로 받은 문자열 출력
        stack = deque()                         # 사용할 스택 정의

        for i in range(len(string)):
            if string[i] == "(":                # 여는 괄호를 찾았을 때
                stack.append(i)                 # 스택에 여는 괄호의 위치를 저장한다
            elif string[i] == ")":              # 닫는 괄호를 찾았을 때
                if stack:                       # 스택에 데이터가 있다면(=여는 괄호가 저장되어 있다면)
                    stack.pop()                 # 그 데이터를 지운다. (가장 마지막으로 저장된 여는 괄호)
                else:                           # 만약 닫는괄호를 찾았는데, 여는 괄호 위치가 스택에 저장되어있지 않다면
                    print(f"문자열 {i} 번째 위치에 닫는 괄호에 맞는 여는 괄호가 없습니다") # 출력

        while stack:                            # 모든 작업을 수행한 후 스택에 데이터가 (=여는 괄호 위치가 삭제되지 않고)남아있다면?
            print(f"문자열 {stack.pop()} 번째 위치에 있는 괄호가 닫히지 않았습니다")
                                                # 데이터를 삭제하면서 리턴하는 pop메소드의 특성을 이용해서
                                                # stack에 남아있는 여는 괄호 위치를 삭제함과 동시에 그 위치에 있는 여는 괄호의 짝이 없다는 문장을 출력한다.

    # 프로그램 테스트용 코드
    case3 = "((1+4)-(3*12)/3"           # 괄호 짝이 있는지 검사할 문자열 저장
    case4 = "(12-3)*(56/3))"

    parentheses_checker(case3)          # 메소드 호출
    parentheses_checker(case4)

    # [ 출력 결과 ]
    # 테스트하는 문자열: ((1+4)-(3*12)/3
    # 문자열 0 번째 위치에 있는 괄호가 닫히지 않았습니다
    # 테스트하는 문자열: (12-3)*(56/3))
    # 문자열 13 번째 위치에 있는 닫는 괄호에 맞는 여는 괄호가 없습니다








