//
//  AlarmModel.swift
//  Alarm
//
//  Created by Sebin Kwon on 11/3/23.
//

import SwiftUI

class AlarmViewModel: ObservableObject {
    @Published var alarms: [Alarm] = []

    func createAlarm(repeatWeek: RepeatWeek?, lable: String = "알람", time: Date, sound: Sound?, isRestart: Bool = true) {
        let alarm = Alarm(repeatWeek: repeatWeek, lable: lable, time: time, sound: sound, isRestart: isRestart)
        alarms.append(alarm)
    }
}

struct Alarm: Identifiable {
    var id = UUID()
    var repeatWeek: RepeatWeek?
    var lable = "알람"
    var time = Date()
    var sound: Sound? = .없음
    var isRestart = true
}

enum RepeatWeek: String, CaseIterable, Hashable {
    case 일요일마다
    case 월요일마다
    case 화요일마다
    case 수요일마다
    case 목요일마다
    case 금요일마다
    case 토요일마다
}

enum Sound: String, CaseIterable {
    case 전파탐지기
    case 공상음
    case 공지음
    case 녹차
    case 없음
}

