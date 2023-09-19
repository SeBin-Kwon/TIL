//
//  ContentView.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/18.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            VStack {
                NavigationLink {
                    WriteFormView()
                } label: {
                    Text("신청서 작성하기")
                }
                NavigationLink {
                    PDFViewer()
                } label: {
                    Text("PDF 보기")
                }.padding()
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
