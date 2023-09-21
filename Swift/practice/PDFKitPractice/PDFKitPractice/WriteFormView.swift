//
//  WriteFormView.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/19.
//

import SwiftUI

struct WriteFormView: View {
    @State var name = ""
    @State var phoneNumber = ""
    @State var address = ""
    @EnvironmentObject var pdfManager: PDFManager
    @Environment(\.presentationMode) var presentationMode
    
    var body: some View {
        VStack {
            TextField("이름을 작성하세요", text: $name)
                .padding()
                .background() {
                    Capsule()
                        .stroke(lineWidth: 1)
                        .foregroundColor(.gray)
                }
                .padding()
//            TextField("핸드폰 번호를 작성하세요", text: $phoneNumber)
//                .padding()
//                .background() {
//                    Capsule()
//                        .stroke(lineWidth: 1)
//                        .foregroundColor(.gray)
//                }
//                .padding()
//            TextField("주소를 작성하세요", text: $address)
//                .padding()
//                .background() {
//                    Capsule()
//                        .stroke(lineWidth: 1)
//                        .foregroundColor(.gray)
//                }
//                .padding()
            Button("완료") {
                addText()
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
