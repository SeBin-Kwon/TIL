import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let (e, s, m) = (input[0], input[1], input[2])
var answer = 0, earth = 0, sun = 0, moon = 0

while true {
    if earth == e && sun == s && moon == m {
        print(answer)
        break
    }

    earth = earth >= 15 ? 1 : earth + 1
    sun = sun >= 28 ? 1 : sun + 1
    moon = moon >= 19 ? 1 : moon + 1
    answer += 1
}