import Foundation

let n = Int(readLine()!)!
let input = readLine()!.split(separator: " ").map { Int($0)! }
var answer = 0
recursive(n, input, 0)
print(answer)

func recursive(_ m: Int, _ arr: [Int], _ e: Int) {
    if m == 2 {
        answer = max(answer, e)
        return
    }
    for i in 1..<m-1 {
        var temp = arr
        temp.remove(at: i)
        recursive(m - 1, temp, e + arr[i-1] * arr[i+1])
    }   
}