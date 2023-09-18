//
//  ContentView.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/18.
//

import SwiftUI

struct ContentView: View {
    let pdfStore = PDFKitStore()
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, world!")
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
