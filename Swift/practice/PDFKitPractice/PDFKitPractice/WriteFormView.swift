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
    @State var currentStep: Step = .one
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
                    OnbomTextField(question: "이름",content: $name)
                    OnbomTextField(question: "주민등록번호",content: $idNumber)
                    Button("다음") {
                        currentStep = .two
                    }
                }
            case .two:
                VStack {
                    OnbomTextField(question: "주소",content: $address)
                    OnbomTextField(question: "핸드폰 번호",content: $phoneNumber)
                    Button("완료") {
                        addText()
                    }
                }
            }
        }
    }
    
    func addText() {
        if !name.isEmpty {
            pdfManager.createPDF(documentURL: formURL, newText: name, at: CGRect(x: 150, y: 650, width: 140, height: 20))
            presentationMode.wrappedValue.dismiss()
        }
    }
}

struct WriteFormView_Previews: PreviewProvider {
    static var previews: some View {
        WriteFormView()
    }
}
