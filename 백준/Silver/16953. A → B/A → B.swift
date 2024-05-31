import Foundation
let n = readLine()!.split(separator: " ").map{Int(String($0))!}
let (A,B) = (n[0], n[1])
func makeNum(_ A: Int, _ B: Int) -> Int {
    var queue: [(num: Int,count: Int)] = [(A, 1)]
    while !queue.isEmpty {
        let target = queue.removeLast()
        if target.num == B {
            return target.count
        }
        if target.num > B {
            continue
        }
        queue.append(((target.num * 10 + 1), target.count + 1))
        queue.append((target.num*2, target.count + 1))
    }
    return -1
}
print(makeNum(A, B))