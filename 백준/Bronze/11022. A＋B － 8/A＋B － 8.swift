let t = Int(readLine()!)!
for i in 1...t {
    let array = readLine()!.split(separator: " ").map { Int($0)! }
    print("Case #\(i): \(array[0]) + \(array[1]) = \(array[0] + array[1])")
}