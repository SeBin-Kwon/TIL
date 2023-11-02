//
//  ContentView.swift
//  Alarm
//
//  Created by Sebin Kwon on 11/2/23.
//

import SwiftUI

struct ContentView: View {
    @State private var selection = 1
    var body: some View {
        NavigationStack {
            TabView(selection: $selection) {
                Text("세계 시계")
                    .tabItem {
                        Image(systemName: "2.square.fill")
                        Text("세계 시계")
                    }.tag(0)
                MainAlarmView(selection: $selection)
                    .tabItem {
                        Image(systemName: "1.square.fill")
                        Text("알람")
                    }.tag(1)
                Text("스톱워치")
                    .tabItem {
                        Image(systemName: "2.square.fill")
                        Text("스톱워치")
                    }.tag(2)
                Text("타이머")
                    .tabItem {
                        Image(systemName: "3.square.fill")
                        Text("타이머")
                    }.tag(3)
            }
            .navigationTitle(selection == 1 ? "알람" : "")
            .padding()
        }
    }
}

#Preview {
    ContentView()
}
