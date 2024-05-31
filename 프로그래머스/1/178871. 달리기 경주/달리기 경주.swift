import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var result = players
    var rank = [String:Int]()
    
    for (i,player) in players.enumerated() {
        rank[player, default: 0] = i
    }
    
    for calling in callings {
        var indax = rank[calling]!
        result.swapAt(indax, indax-1)
        rank[result[indax]] = indax
        rank[result[indax-1]] = indax-1
    }
    
    return result
}