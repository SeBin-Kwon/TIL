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
    @State private var selection = SelectedTab.alarm
    @State private var isAddAlarm = false
    
    var body: some View {
        NavigationStack {
            TabView(selection: $selection) {
                Text("세계 시계")
                    .tabItem {
                        Image(systemName: "2.square.fill")
                        Text("세계 시계")
                    }.tag(SelectedTab.worldClock)
                AlarmView(selection: $selection, isAdd: $isAddAlarm)
                    .tabItem {
                        Image(systemName: "1.square.fill")
                        Text("알람")
                    }.tag(SelectedTab.alarm)
                Text("스톱워치")
                    .tabItem {
                        Image(systemName: "2.square.fill")
                        Text("스톱워치")
                    }.tag(SelectedTab.stopWatch)
                Text("타이머")
                    .tabItem {
                        Image(systemName: "3.square.fill")
                        Text("타이머")
                    }.tag(SelectedTab.timer)
            }
            .navigationTitle(selection == .alarm ? "알람" : "")
            .padding()
            .toolbar {
                if selection == .alarm {
                    ToolbarItemGroup(placement: .topBarLeading) {
                        Button("편집") {
                            print("tap first button")
                        }
                    }
                    ToolbarItemGroup(placement: .topBarTrailing) {
                        Button {
                            isAddAlarm.toggle()
                        } label: {
                            Label("Add a Alarm", systemImage: "plus")
                        }
                    }
                }
            }
        }
    }
}

#Preview {
    ContentView()
}
