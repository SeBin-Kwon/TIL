import sys
input = sys.stdin.readline

class Node:
# 클래스 생성
    def __init__(self, item, left, right):
    #?생성자 메소드:인스턴스 변수들의 초기값을 설정, 첫번째 인수는 반드시 self
        #? 인스턴스 변수 정의, self.<name>으로 정의
        self.item = item # 순회하는 현재 위치
        self.left = left # 현재 위치의 왼쪽
        self.right = right # 현재 위치의 오른쪽

#? 전위 순회 : 루트 - 왼쪽 - 오른쪽
def preorder(node):
    # 순회하기 전, 현재 위치 출력
    print(node.item, end='')

    # 왼쪽 자식이 있다면
    if node.left != '.':
        # 왼쪽으로 이동하기
        preorder(tree[node.left])

    if node.right != '.':
        preorder(tree[node.right])

#? 중위 순회 : 왼쪽 - 루트 - 오른쪽
def inorder(node):
  if node.left != '.':
    inorder(tree[node.left])

  print(node.item, end='')

  if node.right != '.':
    inorder(tree[node.right])

#? 후위 순회 : 왼쪽 - 오른쪽 - 루트
def postorder(node):
  if node.left != '.':
    postorder(tree[node.left])

  if node.right != '.':
    postorder(tree[node.right])

  print(node.item, end='')


n = int(input())
tree = {} #? { A : B, C } A가 부모, B,C가 자식인 관계 설정 위함
for i in range(n):
    node, left, right = map(str,input().split())
    tree[node] = Node(item=node, left=left, right=right)
    #! 클래스를 이용해 인스턴스를 생성

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])