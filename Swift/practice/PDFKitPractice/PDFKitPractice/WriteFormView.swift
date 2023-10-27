//
//  WriteFormView.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/19.
//

import SwiftUI

struct WriteFormView: View {
    enum Step {
        case one
        case two
    }
    
    @Environment(\.presentationMode) var presentationMode
    @EnvironmentObject var pdfManager: PDFManager
    @EnvironmentObject var dictClass: DictClass
 
    @State private var patientQuestionInputs: [String] = ["신청인 성명", "신청인 주민등록번호", "신청인 주민등록지", "신청인 실제 거주지", "신청인 전화번호"]
    @State private var agentQuestionInputs: [String] = ["대리인 성명", "대리인 주민등록번호", "대리인 주소", "대리인 전화번호", "대리인 유형"]
    @State private var patientAnswerInputs: [String] = ["김순옥", "370627-2345678", "경기 성남시 분당구 판교역로 4 (백현동) 행복아파트 104호 310호", "경기 성남시 분당구 판교역로 4 (백현동) 행복아파트 104호 310호", "010-2918-3515"]
    @State private var agentAnswerInputs: [String] = ["김유진", "901203-2345678", "경기 성남시 분당구 서현로 237번길 27 (서현동) 403동 130호", "010-1234-5678", "친족"]
    @State var currentStep: Step = .one
    
    
    var body: some View {
        VStack {
            HStack {
                Button("<") {
                    currentStep = .one
                }.padding()
                Spacer()
            }
            switch currentStep {
            case .one:
                VStack {
                    OnbomTextField(question: "이름",content: $dictClass.name)
                    OnbomTextField(question: "핸폰",content: $dictClass.phoneNumber)
                    OnbomTextField(question: "민증",content: $dictClass.idCard)
                    OnbomTextField(question: "주소",content: $dictClass.adress)
                    OnbomTextField(question: "실주소",content: $dictClass.realAdress)
//                    OnbomTextField(question: "주민등록번호",content: $answerInputs[1])
//                    OnbomTextField(question: "핸폰",content: $answerInputs[0])
//                    OnbomTextField(question: "주소",content: $answerInputs[1])
//                    OnbomTextField(question: "실주소",content: $answerInputs[1])
//                    ForEach(0..<patientQuestionInputs.count, id: \.self) { index in
//                        OnbomTextField(question: patientQuestionInputs[index],content: $patientAnswerInputs[index])
//                    }
                    Button("다음") {
                        currentStep = .two
                    }
                }
            case .two:
                VStack {
                    ForEach(0..<agentQuestionInputs.count, id: \.self) { index in
                        OnbomTextField(question: agentQuestionInputs[index],content: $agentAnswerInputs[index])
                    }
//                    OnbomTextField(question: "주소",content: $answerInputs[2])
//                    OnbomTextField(question: "핸드폰 번호",content: $answerInputs[3])
                    Button("완료") {
                        addText()
                    }
                }
            }
        }
    }
    
    func addText() {
//        guard !answerInputs.contains(where: { $0.isEmpty }) else { return }
//        pdfManager.createPDF(documentURL: formURL, patientNewText: patientAnswerInputs, agentNewText:agentAnswerInputs)
        dictClass.updateDictionary()
        pdfManager.createPDF(documentURL: formURL, patientNewText: dictClass.patientDictionary, agentNewText:dictClass.agentDictionary)
        
        presentationMode.wrappedValue.dismiss()
    }
}

struct WriteFormView_Previews: PreviewProvider {
    static var previews: some View {
        WriteFormView()
            .environmentObject(DictClass())
    }
}
