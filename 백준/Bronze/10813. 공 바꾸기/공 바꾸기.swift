var input = readLine()!.split(separator: " ").map {Int($0)!}
var basket = [Int](1...input[0])
var temp = 0
for _ in 1...input[1] {
    let change = readLine()!.split(separator: " ").map {Int($0)!}
    temp = basket[change[0] - 1]
    basket[change[0] - 1] = basket[change[1] - 1]
    basket[change[1] - 1] = temp
}
basket.forEach {
    print($0, terminator: " ")
}