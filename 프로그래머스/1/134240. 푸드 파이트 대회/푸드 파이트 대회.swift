import Foundation

func solution(_ food:[Int]) -> String {
    var answer = ""
    for i in 1..<food.count {
        if food[i] % 2 == 0 {
            answer += String(repeating:String(i), count:food[i]/2)
        } else {
            if food[i] > 1 {
                answer += String(repeating:String(i), count:(food[i]-1)/2)
         }
        }
    }
    answer += "0" + answer.reversed()
    return answer
}