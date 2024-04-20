import Foundation

func solution(_ edges:[[Int]]) -> [Int] {

    var dic:[Int:[[Int]]] = [:]
    var answer = [0,0,0,0]
    for i in 0..<edges.count {
        dic[edges[i][0], default: [[],[]]][0].append(edges[i][1])
        dic[edges[i][1], default: [[],[]]][1].append(edges[i][0])
    }

    for i in dic {
        if i.value[0].count >= 2 {
            (i.value[1].count == 0) ?  (answer[0] = i.key) : (answer[3] += 1)
        }

        if i.value[0].isEmpty || i.value[0].count == 0  {
            answer[2] += 1
        }
    }

    answer[1] = dic[answer[0]]![0].count - answer[2] - answer[3]

    return answer
}