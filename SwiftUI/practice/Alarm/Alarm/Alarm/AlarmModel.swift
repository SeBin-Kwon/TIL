//
//  AlarmModel.swift
//  Alarm
//
//  Created by Sebin Kwon on 11/3/23.
//

import SwiftUI

class AlarmViewModel: ObservableObject {
    @Published var alarms: [Alarm] = []
    
    func createAlarm() {
        
    }
}

struct Alarm: Hashable {
    var title = ""
    var time = ""
    var label = ""
    var isRepeat = ""
}
