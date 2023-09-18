//
//  PDFKitStore.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/18.
//

import Foundation
import PDFKit

class PDFKitStore {
    let pdfView = PDFView()
    
    func createDocument() {
        guard let url = Bundle.main.url(forResource: "form", withExtension: "pdf") else { return }
        guard let document = PDFDocument(url: url) else { return }
        pdfView.document = document
    }
    
    
}

