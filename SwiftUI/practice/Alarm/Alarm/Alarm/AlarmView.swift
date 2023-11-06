//
//  AlarmView.swift
//  Alarm
//
//  Created by Sebin Kwon on 11/2/23.
//

import SwiftUI

struct AlarmView: View {
    @EnvironmentObject var viewModel: AlarmViewModel
    @Binding var selection: SelectedTab
    @State private var isAdd = false

    var body: some View {
        VStack(alignment: .leading) {
            VStack {
                HStack {
                    Image(systemName: "bed.double.fill")
                    Text("수면 | 기상")
                        .font(.title3)
                        .bold()
                    Spacer()
                }
                Cell(type: .basic)
            }
            .padding(.horizontal)
            List {
                Text("기타")
                    .font(.title3)
                    .bold()
                ForEach(viewModel.alarms) { alarm in
                    Cell(type: .etc, alarm: alarm)
                }
                .onDelete(perform: delete)
            }
            .listStyle(.plain)
            .sheet(isPresented: $isAdd) {
                AddAlarmView(isAdd: $isAdd)
            }
            
            .toolbar {
                if selection == .alarm {
                    ToolbarItem(placement: .topBarLeading) {
                        EditButton()
                    }
                    ToolbarItem(placement: .topBarTrailing) {
                        Button {
                            isAdd.toggle()
                        } label: {
                            Label("Add a Alarm", systemImage: "plus")
                        }
                    }
                }
            }
        }
    }
    
    func delete(at offsets: IndexSet) {
        viewModel.alarms.remove(atOffsets: offsets)
    }
}

#Preview {
    AlarmView(selection: .constant(.alarm))
        .environmentObject(AlarmViewModel())
}
