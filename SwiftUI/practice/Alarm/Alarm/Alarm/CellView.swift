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
   
    let type: CellType
    @State var alarm: Alarm?
    @State var isOn = true
    @State var isEdit = false

    var body: some View {
        switch type {
        case .basic:
            VStack(alignment: .leading) {
                HStack {
                    Text("알람 없음")
                        .font(.title)
                    Spacer()
                    Button {} label: {
                        Text("변경")
                            .padding(5)
                            .background {
                                Capsule()
                                    .foregroundStyle(.gray)
                                    .opacity(0.4)
                            }
                    }
                       
                }
                Text("내일 아침")
            }
        default:
            if let alarm {
                VStack(alignment: .leading) {
                    HStack {
                        Text(dateFormatter(date: alarm.time))
                            .font(.title)
                        Toggle("", isOn: $isOn)
                    }
                    Text(alarm.lable)
                }
                .background {
                    Rectangle().foregroundStyle(Color.black)
                        .onTapGesture {
                            isEdit.toggle()
                        }
                }
                .sheet(isPresented: $isEdit) {
                    EditAlarmView(alarm: $alarm, isEdit: $isEdit)
                }
            }
        }
    }
    
    func dateFormatter(date: Date) -> String {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "a h:mm"
        let dateFormat = dateFormatter.string(from: date)
        return dateFormat
    }
}



#Preview {
    VStack {
        Cell(type: .basic)
        Cell(type: .etc, alarm: Alarm())
    }
    .environmentObject(AlarmViewModel())
}
