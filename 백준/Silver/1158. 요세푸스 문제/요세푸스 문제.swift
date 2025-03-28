import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
var (n, k) = (input[0], input[1])
var linkedList = LinkedList<Int>()
var answer = "<\(k)"
var index = k - 1

for i in 1...n {
    if i == k { continue }
    linkedList.append(i)
}

while !linkedList.isEmpty {
    n -= 1
    index -= 1
    let next = (index + k) % n
    let removeNode = linkedList.remove(at: next)
    answer += ", \(removeNode ?? 0)"
    index = next
}

answer += ">"
print(answer)

final class Node<T: Equatable> {
    var value: T
    var prev: Node?
    var next: Node?
    
    init(value: T,
         prev: Node? = nil,
         next: Node? = nil) {
        self.value = value
        self.prev = prev
        self.next = next
    }
}

extension Node: Equatable {
    static func == (lhs: Node<T>, rhs: Node<T>) -> Bool {
        lhs.value == rhs.value && lhs.next == rhs.next
    }
}

struct LinkedList<T: Equatable> {
    private var head: Node<T>?
    private var tail: Node<T>?
    private var _count: Int = 0
    
    var count: Int {
        _count
    }
    
    var isEmpty: Bool {
        head == nil
    }
}

// MARK: - Head, Tail 위치 기반 삽입,삭제 로직
extension LinkedList {
    /// Head가 가리키는곳(=첫번째 위치) 데이터 추가
    /// - Complexity: O(1)
    mutating func prepend(_ value: T) {
        let newNode = Node(value: value)
        
        if isEmpty {
            head = newNode
            tail = newNode
        } else {
            newNode.next = head
            head?.prev = newNode
            head = newNode
        }
        
        _count += 1
    }
    
    /// Tail이 가리키는곳(=마지막 위치) 데이터 추가
    /// - Complexity: O(1)
    mutating func append(_ value: T) {
        let newNode = Node(value: value)
        
        if isEmpty {
            head = newNode
            tail = newNode
        } else {
            newNode.prev = tail
            tail?.next = newNode
            tail = newNode
        }
        
        _count += 1
    }
    
    
    /// Head가 가리키는곳(=첫번째 위치) 데이터 삭제
    /// - Complexity: O(1)
    @discardableResult
    mutating func removeFirst() -> T? {
        if isEmpty { return nil }
        
        let value = head?.value
        if head === tail { // 데이터가 하나만 있는 경우
            head = nil
            tail = nil
        } else {
            head = head?.next
            head?.prev = nil
        }
        
        _count -= 1
        return value
    }
    
    /// Tail이 가리키는곳(=마지막 위치) 데이터 삭제
    /// - Complexity: O(1)
    @discardableResult
    mutating func removeLast() -> T? {
        if isEmpty { return nil }
        
        let value = tail?.value
        if head === tail { // 노드가 하나만 있는 경우
            head = nil
            tail = nil
        } else {
            tail = tail?.prev
            tail?.next = nil
        }
        
        _count -= 1
        return value
    }
}

// MARK: - 임의의 위치 기반 삽입, 삭제 로직
extension LinkedList {
    /// 임의의 위치에 노드 추가
    /// - Complexity: 임의의 위치의 이전 노드를 찾는 과정 O(N) + 이전 노드의 next / 다음 노드의 prev를 바꾸는 과정 O(1)
    mutating func insert(_ value: T, at index: Int) {
        if index < 0 || index > count { return }
        
        if index == 0 {
            prepend(value)
            return
        }
        
        if index == count {
            append(value)
            return
        }
        
        let newNode = Node(value: value)
        var currentNode = head
        var currentIndex = 0
        
        // 삽입하려는 이전 노드까지 이동
        while currentIndex < index - 1 {
            currentNode = currentNode?.next
            currentIndex += 1
        }
        
        newNode.next = currentNode?.next
        newNode.prev = currentNode
        currentNode?.next?.prev = newNode
        currentNode?.next = newNode
        
        _count += 1
    }
    
    /// 임의의 위치에 노드 삭제
    /// - Complexity: 임의의 위치의 노드를 찾는 과정 O(N) + 이전 노드의 next / 다음 노드의 prev를 바꾸는 과정 O(1)
    @discardableResult
    mutating func remove(at index: Int) -> T? {
        if index < 0 || index >= count { return nil }
        
        var nodeToRemove: Node<T>?
        if index == 0 {
            nodeToRemove = head
            head = head?.next
            head?.prev = nil
            
            if count == 1 {
                tail = nil
            }
            
            _count -= 1
            return nodeToRemove?.value
        }
        
        if index == count - 1 {
            nodeToRemove = tail
            tail = tail?.prev
            tail?.next = nil
            
            _count -= 1
            return nodeToRemove?.value
        }
        
        nodeToRemove = head
        var currentIndex = 0
        // 삭제하려는 노드까지 이동
        while currentIndex < index {
            nodeToRemove = nodeToRemove?.next
            currentIndex += 1
        }
        nodeToRemove?.prev?.next = nodeToRemove?.next
        nodeToRemove?.next?.prev = nodeToRemove?.prev
        
        _count -= 1
        return nodeToRemove?.value
    }
}