import Foundation

func solution(_ new_id:String) -> String {
    var answer = ""
    //1단계 완료
    var id = new_id.lowercased()
    
    //2단계 완료
    for i in id {
        if i >= "a" && i <= "z" {
            answer.append(i)
        }
        else if i >= "0" && i <= "9" {
            answer.append(i)
        }
        else if i == "." || i == "-" || i == "_" {
            answer.append(i)
        }
    }
    
    //3단계
    while let finds = answer.range(of: "..") {
        answer = answer.replacingOccurrences(of: "..", with: ".")
    }
    
    //4단계
    while answer.first == "."{
        answer.removeFirst()
    }
    
    while answer.last == "." {
        answer.removeLast()
    }
    
    //5단계
    if answer == "" {
        answer = "a"
    }
    
    //6단계
    answer = String(answer.prefix(15))
    
    if answer.last == "." {
        answer.removeLast()
    }

    while answer.count < 3 {
        answer.append(answer.last!)
    }
    
    return answer
}