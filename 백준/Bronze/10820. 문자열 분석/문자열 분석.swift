import Foundation
while let line = readLine() {
    var answer = ""
    answer += "\(line.filter { $0.isLowercase }.count) "
    answer += "\(line.filter { $0.isUppercase }.count) "
    answer += "\(line.filter { Int(String($0)) != nil }.count) "
    answer += "\(line.filter { $0 == " " }.count)"
    print(answer)
}