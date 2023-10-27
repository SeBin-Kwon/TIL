//
//  PDFViewer.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/19.
//

import SwiftUI
import PDFKit

struct PDFViewer: UIViewRepresentable {
    let documentURL = formURL
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
//            pdfView.minScaleFactor = 0.6
//            pdfView.maxScaleFactor = 5.0
        } else {
            pdfView.document = PDFDocument(url: self.documentURL)
            pdfView.autoScales = true
        }
        
        return pdfView
    }
    
    func updateUIView(_ uiView: UIViewType, context: Context) {
        if let pdfView = uiView as? PDFView, let pdfData {
                pdfView.document = PDFDocument(data: pdfData)
            }
    }
    
//    func searchBarSearchButtonClicked(_ text: String) {
//        let pdfView = PDFView()
//        let searchText = text
//        let selectionList = pdfView.document?.findString(searchText, withOptions: NSString.CompareOptions.caseInsensitive)
//        
//        guard let page = selectionList?.first?.pages.first else { return }
//        selectionList?.forEach({ selection in
//            selection.pages.forEach { page in
//                let highlight = PDFAnnotation(bounds: selection.bounds(for: page), forType: .highlight, withProperties: nil)
//                    highlight.endLineStyle = .square
//                    highlight.color = UIColor.orange.withAlphaComponent(0.5)
//                    page.addAnnotation(highlight)
//            }
//            
//        })
//    }
}
//
//struct PDFViewer_Previews: PreviewProvider {
//    static var previews: some View {
//        PDFViewer(documentURL: formURL)
//    }
//}
