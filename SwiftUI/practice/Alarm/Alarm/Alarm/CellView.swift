//
//  CellView.swift
//  Alarm
//
//  Created by Sebin Kwon on 11/4/23.
//

import SwiftUI

struct Cell: View {
    enum CellType {
        case basic
        case etc
    }
    var type: CellType
    var time = "오전 10:35"
    var lable = "레이블"
    @Binding var isOn : Bool
    
    var body: some View {
        switch type {
        case .basic:
            VStack(alignment: .leading) {
                HStack {
                    Text(time)
                    Toggle("온오프", isOn: $isOn)
                }
                Text(lable)
            }
        default:
            VStack(alignment: .leading) {
                HStack {
                    Text(time)
                    Toggle("온오프", isOn: $isOn)
                }
                Text("etc")
            }
        }
        
    }
}

#Preview {
    Cell(type: .basic, isOn: .constant(false))
}
