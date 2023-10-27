//
//  MirrorPracticeView.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/10/18.
//

import SwiftUI

class DictClass: ObservableObject {
    var patientDictionary: [String:(answer:String,position:CGRect)] = [
        "name":("name",CGRect(x: 158, y: 605, width: 140, height: 20)),
        "phoneNumber":("phoneNumber",CGRect(x: 158, y: 479, width: 140, height: 20)),
        "idCard":("idCard",CGRect(x: 395, y: 605, width: 150, height: 20)),
        "adress":("adress",CGRect(x: 158, y: 565, width: 380, height: 20)),
        "realAdress":("realAdress",CGRect(x: 158, y: 520, width: 380, height: 20)),
    ]
    var agentDictionary: [String:(answer:String,position:CGRect)] = [
        "name":("name", CGRect(x: 158, y: 450, width: 140, height: 20)),
        "phoneNumber":("phoneNumber", CGRect(x: 158, y: 368, width: 140, height: 20)),
        "idCard":("idCard", CGRect(x: 395, y: 450, width: 150, height: 20)),
        "adress":("adress", CGRect(x: 158, y: 413, width: 380, height: 20)),
        "relationship":("친족", CGRect(x: 183, y: 320, width: 140, height: 20)),
    ]
    
    @Published var name: String = "딕셔너리환자명"
    @Published var phoneNumber: String = "010-3333-5678"
    @Published var idCard: String = "232323-1234567"
    @Published var adress: String = "주소"
    @Published var realAdress: String = "실주소"
    
    func updateDictionary() {
        patientDictionary["name"]?.answer = name
        patientDictionary["phoneNumber"]?.answer = phoneNumber
        patientDictionary["idCard"]?.answer = idCard
        patientDictionary["adress"]?.answer = adress
        patientDictionary["realAdress"]?.answer = realAdress
    }
//    func processClass(_ inputClass: DictClass) {
//        let mirror = Mirror(reflecting: inputClass)
//        for (label, value) in mirror.children {
//            if let label = label, let publishedValue = value as? Published<String?> {
//                // Published 프로퍼티에 접근하여 값을 가져옴
//                let propertyValue = inputClass[keyPath: publishedValue]
//                print("Property: \(label), Value: \(propertyValue ?? "nil")")
//            }
////        for case let (_?, value) in mirror.children {
////            print("\(value)")
////        }
//    }
}

struct MyStruct {
    var property1: Int
    var property2: String
}

func processStruct(_ inputStruct: MyStruct) {
    let mirror = Mirror(reflecting: inputStruct)
    for case let (_?, value) in mirror.children {
        print("\(value)")
    }
}


struct DictPracticeView: View {
    @EnvironmentObject var dictClass: DictClass
    var body: some View {
        Button("Mirror") {
//            dictClass.name = "권세빈"
//            dictClass.phoneNumber = "010-7399-9999"
//            dictClass.dictionary["name"]?.answer = "권세빈"
//            dictClass.dictionary["phoneNumber"]?.answer = "010-7399-9999"
////            print("\(mirrorClass.dictionary.values)")
//            for value in dictClass.patientDictionary.values {
//                print(type(of:dictClass.patientDictionary.values))
//                print("답변 : \(value.answer)")
//                print("위치 : \(value.position)")
//            }
//            let myInstance = MyStruct(property1: 42, property2: "property2")
//            processStruct(myInstance)
//            dictClass.processClass(dictClass)
        }
    }
}

struct DictPracticeView_Previews: PreviewProvider {
    static var previews: some View {
        DictPracticeView()
            .environmentObject(DictClass())
    }
}
