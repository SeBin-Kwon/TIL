//
//  MainAlarmView.swift
//  Alarm
//
//  Created by Sebin Kwon on 11/2/23.
//

import SwiftUI

struct MainAlarmView: View {
    @State var isOn = false
    @Binding var selection : Int
    var body: some View {
        VStack(alignment: .leading) {
            Text("수면 | 기상")
            Text("기타")
            Cell(isOn: $isOn)
        }
        
        .toolbar {
            if selection == 1 {
                ToolbarItemGroup(placement: .topBarLeading) {
                    Button("편집") {
                        print("tap first button")
                    }
                }
                ToolbarItemGroup(placement: .topBarTrailing) {
                    Button {
                        //                isAdd.toggle()
                    } label: {
                        Label("Add a Todo", systemImage: "plus")
                    }
                }
            }
        }
    }
}

struct Cell: View {
    var time = "오전 10:35"
    var lable = "레이블"
    @Binding var isOn : Bool
    var body: some View {
        VStack(alignment: .leading) {
            HStack {
                Text(time)
                Toggle("온오프", isOn: $isOn)
            }
            Text(lable)
        }
    }
}

#Preview {
    MainAlarmView(selection: .constant(1))
}
