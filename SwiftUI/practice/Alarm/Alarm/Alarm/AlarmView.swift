//
//  AlarmView.swift
//  Alarm
//
//  Created by Sebin Kwon on 11/2/23.
//

import SwiftUI

struct AlarmView: View {
    @ObservedObject var alarmModel = AlarmViewModel()
    @Binding var selection: SelectedTab
    @State var isOn = false
    @Binding var isAdd: Bool
    
    var body: some View {
        VStack(alignment: .leading) {
            Text("수면 | 기상")
            Text("기타")
            ForEach(alarmModel.alarms, id: \.self) { alarm in
                Cell(type: .basic, isOn: $isOn)
            }
        }
    }
    
    func addAlarm() {
        alarmModel.createAlarm()
    }
}

#Preview {
    AlarmView(selection: .constant(.alarm), isAdd: .constant(false))
}
