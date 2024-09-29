import Foundation

func solution(_ X:String, _ Y:String) -> String {
    var dictX = Dictionary(grouping: X, by: {$0})
    var dictY = Dictionary(grouping: Y, by: {$0})

    var result = ""
    
    for (k,v) in dictX.sorted{$0.key > $1.key} {
        if dictY[k] != nil {
            let minCnt = v.count < dictY[k]!.count ? v.count : dictY[k]!.count
            result += String(repeating: k, count: minCnt)
        }
    }
    
    if result.isEmpty { return "-1" } 
    if result.first! == "0" { return "0" }
    
    return result
}
