//
//  AddAlarmView.swift
//  Alarm
//
//  Created by Sebin Kwon on 11/4/23.
//

import SwiftUI


struct AddAlarmView: View {
    @EnvironmentObject var viewModel: AlarmViewModel
    @Binding var isAdd: Bool
    @State private var lable = ""
    @State private var isRestart = true
    @State private var currentTime = Date()
    var body: some View {
        NavigationStack {
            DatePicker("", selection: $currentTime, displayedComponents: .hourAndMinute)
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
//                        .fixedSize()
//                        .border(.pink)
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
                        isAdd = false
                    }
                }
                ToolbarItem(placement: .topBarTrailing) {
                    Button("저장") {
                        addAlarm()
                    }
                }
                
            }
        }

    }
    
    private func addAlarm() {
        if lable == "" {
            lable = "알람"
        }
        viewModel.createAlarm(repeatWeek: nil, lable: lable, time: currentTime, sound: nil, isRestart: isRestart)
        isAdd = false
    }
}

struct RepeatWeekView: View {
    @EnvironmentObject var viewModel: AlarmViewModel
    @State private var isSelected: [Bool] = Array(repeating: false, count: 7)
    var body: some View {
        List {
            ForEach(RepeatWeek.allCases, id: \.self) { item in
                HStack {
                    Text(item.rawValue)
                    Spacer()
                }
            }
        }
    }
}

struct SoundView: View {
    @EnvironmentObject var viewModel: AlarmViewModel
    var body: some View {
        Text("안녕")
    }
}

#Preview {
    AddAlarmView(isAdd: .constant(true))
        .environmentObject(AlarmViewModel())
}
