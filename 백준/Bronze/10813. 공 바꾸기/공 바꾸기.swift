let input = readLine()!.split(separator: " ").map {Int($0)!}
var basket = [Int](1...input[0])
for _ in 1...input[1] {
    let change = readLine()!.split(separator: " ").map {Int($0)!}
    basket.swapAt(change[0]-1, change[1]-1)
}
basket.forEach {
    print($0, terminator: " ")
}