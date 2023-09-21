//
//  PDFManager.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/21.
//

import Foundation
import PDFKit

class PDFManager: ObservableObject {
    @Published var PDFDatas: [Data] = []
    
    func addPDFData(_ pdfData: Data) {
        PDFDatas.append(pdfData)
        }
    
    func createPDF(documentURL: URL, newText: String, at rect: CGRect) {
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
        addPDFData(newData)
        
        //    let newURL = 서버 URL이 들어갈 예정
        //    do {
        //        try newData.write(to: newURL)
        //    } catch {
        //        print("Failed to save the modified PDF: \(error)")
        //    }
    }
}
