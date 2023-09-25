//
//  PDFViewer.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/19.
//

import SwiftUI
import PDFKit

struct PDFViewer: UIViewRepresentable {
//    let documentURL: URL
    var pdfData: Data?
    
//    init(documentURL: URL) {
//        self.documentURL = documentURL
//    }
    func makeUIView(context: Context) -> some UIView {
        let pdfView = PDFView()
        
        if let pdfData {
//            pdfView.document = PDFDocument(url: self.documentURL)
            pdfView.document = PDFDocument(data: pdfData)
            pdfView.autoScales = true
//            pdfView.displayDirection = .horizontal
            pdfView.minScaleFactor = 0.6
            pdfView.maxScaleFactor = 5.0
        }
        
        return pdfView
    }
    
    func updateUIView(_ uiView: UIViewType, context: Context) {
        if let pdfView = uiView as? PDFView, let pdfData {
                pdfView.document = PDFDocument(data: pdfData)
            }
    }
}
//
//struct PDFViewer_Previews: PreviewProvider {
//    static var previews: some View {
//        PDFViewer(documentURL: formURL)
//    }
//}
