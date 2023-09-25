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
    @State var name = ""
    @State var address = ""
    @State var phoneNumber = ""
    @State var idNumber = ""
    @State private var questionInputs: [String] = ["이름", "주민등록번호", "주소", "핸드폰 번호"]
    @State private var answerInputs: [String] = Array(repeating: "", count: 4)
    @State var currentStep: Step = .one
    let cgRectArray: [CGRect] = [CGRect(x: 150, y: 650, width: 140, height: 20),CGRect(x: 350, y: 650, width: 140, height: 20),CGRect(x: 150, y: 600, width: 140, height: 20),CGRect(x: 350, y: 565, width: 140, height: 20)]
//    @State var formQuestions: [FormQuestion] = [
//        FormQuestion(question: "이름", answer: ""),
//        FormQuestion(question: "주민등록번호", answer: ""),
//        FormQuestion(question: "주소", answer: ""),
//        FormQuestion(question: "핸드폰 번호", answer: ""),
//    ]
    
    
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
//                    OnbomTextField(question: "이름",content: $answerInputs[0])
//                    OnbomTextField(question: "주민등록번호",content: $answerInputs[1])
                    ForEach(0..<questionInputs.count - 2, id: \.self) { index in
                        OnbomTextField(question: questionInputs[index],content: $answerInputs[index])
                    }
                    Button("다음") {
                        currentStep = .two
                    }
                }
            case .two:
                VStack {
                    ForEach(2..<questionInputs.count, id: \.self) { index in
                        OnbomTextField(question: questionInputs[index],content: $answerInputs[index])
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
        guard !answerInputs.contains(where: { $0.isEmpty }) else { return }
        pdfManager.createPDF(documentURL: formURL, newText: answerInputs, at: cgRectArray)
        presentationMode.wrappedValue.dismiss()
    }
}

struct WriteFormView_Previews: PreviewProvider {
    static var previews: some View {
        WriteFormView()
    }
}
