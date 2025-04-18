import Foundation

let input = Array(readLine()!)
var dict : [Character:Int] = [:]

for i in input {
    if i == "6" || i == "9" {
        dict["6", default: 0] += 1
    } else {
        dict[i, default: 0] += 1
    }
}

if let sixCnt = dict["6"] {
    dict["6"] = (sixCnt / 2) + (sixCnt % 2)
}

print(dict.values.max()!)
