func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    let row = arr1.count
    let column = arr1[0].count
    var answer = Array(repeating: Array(repeating: 0, count: column), count: row)
    for i in 0..<row {
        for j in 0..<column {
            answer[i][j] = arr1[i][j] + arr2[i][j]
        }
    }
    return answer
}