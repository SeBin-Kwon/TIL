//
//  Data.swift
//  PDFKitPractice
//
//  Created by Sebin Kwon on 2023/09/21.
//

import Foundation

struct Patient {
    let id: UUID = UUID()
    let name: String
    let phoneNumber: String
    let address: String
    
    init(name: String, phoneNumber: String, address: String) {
        self.name = name
        self.phoneNumber = phoneNumber
        self.address = address
    }
}
