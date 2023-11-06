//
//  ContentView.swift
//  Alarm
//
//  Created by Sebin Kwon on 11/2/23.
//

import SwiftUI

enum SelectedTab {
    case worldClock
    case alarm
    case stopWatch
    case timer
}

struct ContentView: View {
    @StateObject private var viewModel = AlarmViewModel()
    @State private var selection = SelectedTab.alarm

    var body: some View {
        NavigationStack {
            TabView(selection: $selection) {
                Text("세계 시계")
                    .tabItem {
                        Image(systemName: "globe")
                        Text("세계 시계")
                    }.tag(SelectedTab.worldClock)
                AlarmView(selection: $selection)
                    .tabItem {
                        Image(systemName: "alarm.fill")
                        Text("알람")
                    }.tag(SelectedTab.alarm)
                    .environmentObject(viewModel)
                Text("스톱워치")
                    .tabItem {
                        Image(systemName: "stopwatch.fill")
                        Text("스톱워치")
                    }.tag(SelectedTab.stopWatch)
                Text("타이머")
                    .tabItem {
                        Image(systemName: "timer")
                        Text("타이머")
                    }.tag(SelectedTab.timer)
            }
            .navigationTitle(selection == .alarm ? "알람" : "")
        }
    }
}

#Preview {
    ContentView()
}
