//
//  Data.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/21.
//

import Foundation

struct FormQuestion: Identifiable {
    let id = UUID()
    var question: String
    var answer: String
}

