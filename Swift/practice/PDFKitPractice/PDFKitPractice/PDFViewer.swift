//
//  PDFViewer.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/19.
//

import SwiftUI
import PDFKit

struct PDFViewer: UIViewRepresentable {
    let documentURL = Bundle.main.url(forResource: "form", withExtension: "pdf")!
//    let documentURL: URL

    func makeUIView(context: Context) -> some UIView {
        let pdfView = PDFView()
        
        pdfView.document = PDFDocument(url: self.documentURL)
        pdfView.autoScales = true
        pdfView.displayDirection = .horizontal
        pdfView.minScaleFactor = 0.5
        pdfView.maxScaleFactor = 5.0
        
        return pdfView
    }
    
    func updateUIView(_ uiView: UIViewType, context: Context) -> Void {
        
    }
}

struct PDFViewer_Previews: PreviewProvider {
    static var previews: some View {
        PDFViewer()
    }
}
