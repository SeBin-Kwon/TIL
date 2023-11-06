//
//  EditAlarmView.swift
//  Alarm
//
//  Created by Sebin Kwon on 11/6/23.
//

import SwiftUI

struct EditAlarmView: View {
    @EnvironmentObject var viewModel: AlarmViewModel
    @Binding var alarm: Alarm?
    @Binding var isEdit: Bool
    @State private var lable = ""
    @State private var isRestart = true
    @State private var newTime = Date()
    var body: some View {
        NavigationStack {
            DatePicker("", selection: $newTime, displayedComponents: .hourAndMinute)
                        .labelsHidden()
                        .datePickerStyle(WheelDatePickerStyle())
            List {
                NavigationLink {
                    RepeatWeekView()
                } label: {
                    HStack {
                        Text("반복")
                        Spacer()
                        Text("안함")
                    }
                }
                HStack {
                    Text("레이블")
                    TextField("알람", text: $lable)
                        .multilineTextAlignment(.trailing)
                }
                NavigationLink {
                    SoundView()
                } label: {
                    HStack {
                        Text("사운드")
                        Spacer()
                        Text("없음")
                    }
                }
                HStack {
                    Toggle("다시 알림", isOn: $isRestart)
                }
            }
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button("취소") {
                        isEdit = false
                    }
                }
                ToolbarItem(placement: .topBarTrailing) {
                    Button("저장") {
                        UpdateAlarm()
                    }
                }
                
            }
        }
        .onAppear {
            if let alarm {
                lable = alarm.lable
                isRestart = alarm.isRestart
                newTime = alarm.time
            }
        }
    }
    
        private func UpdateAlarm() {
            alarm?.lable = lable
            alarm?.isRestart = isRestart
            alarm?.time = newTime
            isEdit = false
        }
}

#Preview {
    EditAlarmView(alarm: .constant(Alarm()), isEdit: .constant(true))
}
