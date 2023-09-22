//
//  QuestionView.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/22.
//

import SwiftUI

struct QuestionView: View {
    @State private var answer = ""
    @Binding var formQuestion: [FormQuestion]
    let question: FormQuestion
    
    var body: some View {
        VStack {
            Text(question.question)
                .padding()
            
            TextField("Enter your answer", text: $answer)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            Spacer()
        }
        .padding()
        //        .navigationBarTitle("Question", displayMode: .inline)
        //        .navigationBarItems(trailing: Button("Submit") {
        //            saveAnswer()
        //        })
    }
}
//struct QuestionView_Previews: PreviewProvider {
//    static var previews: some View {
//        QuestionView()
//    }
//}
