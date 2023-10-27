//
//  FindStringTestView.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/10/06.
//

import SwiftUI

struct FindStringTestView: View {
    @EnvironmentObject var pdfManager: PDFManager
    @State var name = ""
    @State var address = ""
    @State var phoneNumber = ""
    @State var idNumber = ""
    @State private var questionInputs: [String] = ["이름", "주민등록번호"]
    @State private var answerInputs: [String] = Array(repeating: "", count: 2)
    let cgRectArray: [CGRect] = [CGRect(x: 150, y: 650, width: 140, height: 20),CGRect(x: 350, y: 650, width: 140, height: 20)]
    
    
    var body: some View {
        VStack {
            ForEach(0..<questionInputs.count, id: \.self) { index in
                OnbomTextField(question: questionInputs[index],content: $answerInputs[index])
            }
            Button("완료") {
                addText()
            }
        }
    }
    
    func addText() {
//        guard !answerInputs.contains(where: { $0.isEmpty }) else { return }
//        pdfManager.createPDF(documentURL: formURL, newText: answerInputs, at: cgRectArray)
    }
}

struct FindStringTestView_Previews: PreviewProvider {
    static var previews: some View {
        FindStringTestView()
    }
}
