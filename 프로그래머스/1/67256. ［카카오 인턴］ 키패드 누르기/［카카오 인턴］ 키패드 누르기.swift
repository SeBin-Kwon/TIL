import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    // 왼 * (3,0), 오 # (3,2)
    var answer = ""
    var rLocation: (Int, Int) = (3,0)
    var lLocation: (Int, Int) = (3,2)
    var mLocation: (Int, Int) = (3,1)
    for num in numbers {
        switch num {
        case 1, 4, 7:
            let row = num / 3
            lLocation = (row, 0)
            answer += "L"
        case 3, 6, 9:
            let row = num / 4
            rLocation = (row, 2)
            answer += "R"
        case 2, 5, 8, 0:
            var row = num / 3
            if num == 0 { row = 3 }
            mLocation = (row, 1)
            
            let rDistance = abs(rLocation.0 - mLocation.0) + abs(rLocation.1 - mLocation.1)
            let lDistance = abs(lLocation.0 - mLocation.0) + abs(lLocation.1 - mLocation.1)
            // print("왼손 거리", lDistance, "오른손 거리", rDistance)
            if rDistance > lDistance {
                answer += "L"
                lLocation = mLocation
            } else if rDistance < lDistance {
                answer += "R"
                rLocation = mLocation
            } else {
                if hand == "right" {
                    answer += "R"
                    rLocation = mLocation
                } else {
                    answer += "L"
                    lLocation = mLocation
                }
            }
        default:
            break
        }
        // print("번호:", num, "왼손 위치:", lLocation, "오른손 위치:", rLocation, "가운데 위치:", mLocation, "답:", answer)
    }
    return answer
}