//
//  main.swift
//  RandomBingo
//
//  Created by Sebin Kwon on 1/18/24.
//

import Foundation

//print("Start Bingo!")
//let answer = Int.random(in: 1...100)
//for i in 0..<10 {
//    let input = readLine()
//    if let input {
//        if let intInput = Int(input) {
//            if intInput == answer {
//                print("Bingo!")
//                break
//            } else if intInput > answer {
//                print("Down")
//                if i == 8 {
//                    print("마지막 기회입니다.")
//                }
//            } else {
//                print("Up")
//                if i == 8 {
//                    print("마지막 기회입니다.")
//                }
//            }
//        } else {
//            print("숫자를 입력해주세요.")
//            continue
//        }
//    }
//}

while true {
    var computerChoice = Int.random(in: 1...100)
    var myChoice: Int = 0
    
    var userInput = readLine()
    if let input = userInput {
        if let number = Int(input) {
            myChoice = number
        }
    }
    
    if computerChoice > myChoice {
        print("Up")
    } else if computerChoice < myChoice {
        print("Down")
    } else {
        print("Bingo")
        break
    }
}
