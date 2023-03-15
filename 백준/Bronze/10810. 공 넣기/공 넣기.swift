var input = readLine()!.split(separator: " ").map {Int($0)!} //map
var result = Array(repeating: 0, count: input[0])
for _ in 1...input[1] {
    var ball = readLine()!.split(separator: " ").map {Int($0)!}
    for i in ball[0]...ball[1] {
        result[i-1] = ball[2]
    }
}
result.forEach {
    print($0, terminator:" ")
}