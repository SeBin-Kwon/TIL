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
//    let patientCGRectArray: [CGRect] = [CGRect(x: 150, y: 550, width: 140, height: 20),
//                                        CGRect(x: 350, y: 500, width: 140, height: 20),
//                                        CGRect(x: 150, y: 450, width: 240, height: 20),
//                                        CGRect(x: 150, y: 405, width: 240, height: 20),
//                                        CGRect(x: 150, y: 350, width: 140, height: 20),]
//    let agentCGRectArray: [CGRect] = [CGRect(x: 158, y: 450, width: 140, height: 20),
//                                      CGRect(x: 395, y: 450, width: 150, height: 20),
//                                      CGRect(x: 158, y: 413, width: 380, height: 20),
//                                      CGRect(x: 158, y: 368, width: 140, height: 20),
//                                      CGRect(x: 158, y: 250, width: 140, height: 20),]
//    func addPDFData(_ pdfData: Data) {
//        PDFDatas.append(pdfData)
//        }
    enum FixedPositionItems: CaseIterable {
            case apply
            case protector
            case mailReceive
            case mailAddress
            case todayDate
            case signature
        }
    func createPDF(documentURL: URL, patientNewText: [String:(answer:String,position:CGRect)], agentNewText: [String:(answer:String,position:CGRect)]) {
        guard let pdfDocument = PDFDocument(url: documentURL) else { return }
        var textAnnotation: PDFAnnotation
        
        if let firstPage = pdfDocument.page(at: 0) {
            for item in Array(FixedPositionItems.allCases.prefix(2)) {
                switch item {
                case .apply:
                    textAnnotation = PDFAnnotation(bounds: CGRect(x: 168, y: 742, width: 140, height: 20), forType: .freeText, withProperties: nil)
                    textAnnotation.contents = "✓"
                    
                case .protector:
                    textAnnotation = PDFAnnotation(bounds: CGRect(x: 378, y: 208, width: 140, height: 20), forType: .freeText, withProperties: nil)
                    textAnnotation.contents = "✓"
                default:
                    continue
                }
                textAnnotation.color = .clear
                firstPage.addAnnotation(textAnnotation)
            }
                    
            for value in patientNewText.values {
                textAnnotation = PDFAnnotation(bounds: value.position, forType: .freeText, withProperties: nil)
                textAnnotation.contents = value.answer
                //                textAnnotation.font = UIFont.systemFont(ofSize: 12.0)
                                textAnnotation.font = UIFont(name: "Helvetica", size: 12.0)
                                textAnnotation.color = .clear
                firstPage.addAnnotation(textAnnotation)
            }
            for value in agentNewText.values {
                switch value.answer {
                case "가족":
                    textAnnotation = PDFAnnotation(bounds: value.position, forType: .freeText, withProperties: nil)
                    textAnnotation.contents = "✓"
                    
                case "친족":
                    textAnnotation = PDFAnnotation(bounds: CGRect(x: 245, y: 320, width: 140, height: 20), forType: .freeText, withProperties: nil)
                    textAnnotation.contents = "✓"
                    //                textAnnotation.font = UIFont.systemFont(ofSize: 12.0)
                    //                textAnnotation.font = UIFont(name: "Helvetica", size: 12.0)
                    //                    textAnnotation.color = .clear
                    //                    firstPage.addAnnotation(textAnnotation)
                default:
                    textAnnotation = PDFAnnotation(bounds: value.position, forType: .freeText, withProperties: nil)
                    textAnnotation.contents = value.answer
                    //                textAnnotation.font = UIFont.systemFont(ofSize: 12.0)
                    //                    textAnnotation.font = UIFont(name: "Helvetica", size: 12.0)
                    //                    textAnnotation.color = .clear
                    //                    firstPage.addAnnotation(textAnnotation)
                }
                //                textAnnotation.font = UIFont.systemFont(ofSize: 12.0)
                textAnnotation.font = UIFont(name: "Helvetica", size: 12.0)
                textAnnotation.color = .clear
                firstPage.addAnnotation(textAnnotation)
            }
        }
        
        if let secondPage = pdfDocument.page(at: 1) {
            let formatter = DateFormatter()
            formatter.dateFormat = "yyyy        MM        dd"
            let currentDate = formatter.string(from: Date())
            for item in Array(FixedPositionItems.allCases.suffix(4)) {
                switch item {
                case .mailReceive:
                    textAnnotation = PDFAnnotation(bounds: CGRect(x: 342, y: 733, width: 140, height: 20), forType: .freeText, withProperties: nil)
                    textAnnotation.contents = "✓"
                case .mailAddress:
                    textAnnotation = PDFAnnotation(bounds: CGRect(x: 429, y: 690, width: 140, height: 20), forType: .freeText, withProperties: nil)
                    textAnnotation.contents = "✓"
                case .todayDate:
                    textAnnotation = PDFAnnotation(bounds: CGRect(x: 400, y: 482, width: 140, height: 20), forType: .freeText, withProperties: nil)
                    textAnnotation.contents = currentDate
                case .signature:
                    textAnnotation = PDFAnnotation(bounds: CGRect(x: 424, y: 430, width: 140, height: 20), forType: .freeText, withProperties: nil)
                    textAnnotation.contents = "사인사인"
                default:
                    continue
                }
                textAnnotation.color = .clear
                secondPage.addAnnotation(textAnnotation)
            }
            
            // 전염성, 정신질환, 예/아니오
            let InfectiousYestextAnnotation = PDFAnnotation(bounds: CGRect(x: 301, y: 601, width: 140, height: 20), forType: .freeText, withProperties: nil)
            InfectiousYestextAnnotation.contents = "✓"
            InfectiousYestextAnnotation.color = .clear
            secondPage.addAnnotation(InfectiousYestextAnnotation)
            let InfectiousNotextAnnotation = PDFAnnotation(bounds: CGRect(x: 352, y: 601, width: 140, height: 20), forType: .freeText, withProperties: nil)
            InfectiousNotextAnnotation.contents = "✓"
            InfectiousNotextAnnotation.color = .clear
            secondPage.addAnnotation(InfectiousNotextAnnotation)
            let MentalYestextAnnotation = PDFAnnotation(bounds: CGRect(x: 301, y: 580, width: 140, height: 20), forType: .freeText, withProperties: nil)
            MentalYestextAnnotation.contents = "✓"
            MentalYestextAnnotation.color = .clear
            secondPage.addAnnotation(MentalYestextAnnotation)
            let MentalNotextAnnotation = PDFAnnotation(bounds: CGRect(x: 352, y: 580, width: 140, height: 20), forType: .freeText, withProperties: nil)
            MentalNotextAnnotation.contents = "✓"
            MentalNotextAnnotation.color = .clear
            secondPage.addAnnotation(MentalNotextAnnotation)
        }
        
        guard let newData = pdfDocument.dataRepresentation() else { return }
        PDFDatas.append(newData)
//        addPDFData(newData)
        
        //    let newURL = 서버 URL이 들어갈 예정
        //    do {
        //        try newData.write(to: newURL)
        //    } catch {
        //        print("Failed to save the modified PDF: \(error)")
        //    }
    }
    
}
