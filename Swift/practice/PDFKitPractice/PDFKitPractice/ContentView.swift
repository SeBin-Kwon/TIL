//
//  ContentView.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/18.
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var pdfManager: PDFManager
    @EnvironmentObject var dictClass: DictClass
    var body: some View {
        NavigationView {
            VStack {
                NavigationLink {
                    WriteFormView()
                } label: {
                    Text("신청서 작성하기")
                }.padding()
//                NavigationLink {
//                    FindStringTestView()
//                } label: {
//                    Text("자동으로 위치시켜보기")
//                }
                ForEach(Array(pdfManager.PDFDatas.enumerated()), id:\.1) { index, pdfdata in
                    NavigationLink {
                        PDFViewer(pdfData: pdfdata)
                    } label: {
                        Text("PDF 보기 \(index)")
                    }.padding()
                }
//                Text("신청한 수 : \(pdfManager.PDFDatas.count)")
//                    .padding()
                NavigationLink {
                    PDFViewer()
                } label: {
                    Text("PDF 원본")
                }.padding()
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .environmentObject(PDFManager())
            .environmentObject(DictClass())
    }
}
