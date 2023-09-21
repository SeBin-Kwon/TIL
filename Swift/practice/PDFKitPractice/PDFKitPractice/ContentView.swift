//
//  ContentView.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/18.
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var pdfManager: PDFManager
    @State var index = 0
    
    var body: some View {
        NavigationView {
            VStack {
                NavigationLink {
                    WriteFormView()
                } label: {
                    Text("신청서 작성하기")
                }
                ForEach(Array(pdfManager.PDFDatas.enumerated()), id:\.1) { index, pdfdata in
                    NavigationLink {
                        PDFViewer(pdfData: pdfdata)
                    } label: {
                        Text("PDF 보기 \(index)")
                    }.padding()
                }
                Text("신청한 수 : \(pdfManager.PDFDatas.count)")
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .environmentObject(PDFManager())
    }
}
