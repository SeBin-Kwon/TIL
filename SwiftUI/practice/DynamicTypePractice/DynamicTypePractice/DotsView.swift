//
//  DotsView.swift
//  DynamicTypePractice
//
//  Created by Sebin Kwon on 2023/09/26.
//

import SwiftUI

struct DotsView: View {
    let datas = Array(repeating: "f", count: 9)
    let columns = [
            GridItem(.adaptive(minimum: 100)),
        ]
    var body: some View {
        VStack {
            Text("A")
                .font(.title)
                .fontWeight(.black)
//            Spacer()
            LazyVGrid(columns: columns, spacing: 20) {
                ForEach(datas, id: \.self) { data in
                    Text(data)
                }
            }
        }
    }
}

struct DotsView_Previews: PreviewProvider {
    static var previews: some View {
        DotsView()
    }
}
