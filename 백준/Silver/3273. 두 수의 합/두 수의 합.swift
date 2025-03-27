let n = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map { Int($0)! }
let x = Int(readLine()!)!

let sortedArray = arr.sorted()

var left = 0
var right = n - 1
var count = 0

while left < right {
    let sumResult = sortedArray[left] + sortedArray[right]
    if x == sumResult {
        count += 1
        left += 1
    } else if x < sumResult {
        right -= 1
    } else {
        left += 1
    }
}

print(count)