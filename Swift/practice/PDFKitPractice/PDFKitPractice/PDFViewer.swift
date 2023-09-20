//
//  PDFViewer.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/19.
//

import SwiftUI
import PDFKit
import UIKit

struct PDFViewer: UIViewRepresentable {
    let documentURL: URL
    
    init(documentURL: URL) {
        self.documentURL = documentURL
    }

    func makeUIView(context: Context) -> some UIView {
        let pdfView = PDFView()
        
        pdfView.document = PDFDocument(url: self.documentURL)
        pdfView.autoScales = true
        pdfView.displayDirection = .horizontal
        pdfView.minScaleFactor = 0.6
        pdfView.maxScaleFactor = 5.0
        
        return pdfView
    }
    
    func updateUIView(_ uiView: UIViewType, context: Context) -> Void {
        
    }
}

func modifyPDF(documentURL: URL, newText: String, at rect: CGRect) {
    guard let pdfDocument = PDFDocument(url: documentURL) else { return }

    if let firstPage = pdfDocument.page(at: 0) {
        let textAnnotation = PDFAnnotation(bounds: rect, forType: .freeText, withProperties: nil)
        textAnnotation.contents = newText
//        textAnnotation.font = UIFont.systemFont(ofSize: 12.0)
        textAnnotation.font = UIFont(name: "Helvetica", size: 12.0)
        textAnnotation.interiorColor = UIColor.clear

        firstPage.addAnnotation(textAnnotation)
    }

    guard let newData = pdfDocument.dataRepresentation() else { return }
    // newData로 새로운 인스턴트 생성하기
//    let pdfView = PDFView()
//    pdfView.document = PDFDocument(data: newData)
    let newURL = formURL
    do {
        try newData.write(to: newURL)
    } catch {
        print("Failed to save the modified PDF: \(error)")
    }
}


struct PDFViewer_Previews: PreviewProvider {
    static var previews: some View {
        PDFViewer(documentURL: formURL)
    }
}
