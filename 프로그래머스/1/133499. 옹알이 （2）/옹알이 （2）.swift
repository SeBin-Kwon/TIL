import Foundation

func solution(_ babbling:[String]) -> Int {
    let possible = ["aya", "ye", "woo", "ma"]
    var count = 0

    for babble in babbling {
        var word = babble

        for i in 0..<possible.count {
            word = word.replacingOccurrences(of: possible[i], with: "\(i+1)")
        }
        if Int(word) != nil && !(word.contains("11") || word.contains("22")
                                 || word.contains("33") || word.contains("44"))  {
            count += 1
        }
    }

    return count
}