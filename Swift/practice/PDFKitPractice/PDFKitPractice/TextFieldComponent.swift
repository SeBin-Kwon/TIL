//
//  TextFieldComponent.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/22.
//

import SwiftUI

struct OnbomTextField: View {
    var question: String
    @Binding var content: String
    var body: some View {
        VStack(alignment:.leading) {
            Text("\(question)")
                .bold()
            TextField("입력", text: $content)
                .padding()
                .background() {
                    Capsule()
                        .stroke(lineWidth: 1)
                        .foregroundColor(.gray)
                }
        }.padding()
    }
}

struct TextFieldComponent_Previews: PreviewProvider {
    static var previews: some View {
        OnbomTextField(question: "이름",content: Binding.constant(""))
    }
}
