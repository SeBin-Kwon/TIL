//
//  WriteFormView.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/19.
//

import SwiftUI

struct WriteFormView: View {
    @State var name = ""
    var body: some View {
        TextField("이름을 작성하세요", text: $name)
            .padding()
            .background() {
                Capsule()
                    .stroke(lineWidth: 1)
                    .foregroundColor(.gray)
            }
            .padding()
    }
}

struct WriteFormView_Previews: PreviewProvider {
    static var previews: some View {
        WriteFormView()
    }
}
