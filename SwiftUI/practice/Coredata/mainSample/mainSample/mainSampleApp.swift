//
//  mainSampleApp.swift
//  mainSample
//
//  Created by Sebin Kwon on 2023/05/03.
//

import SwiftUI

@main
struct mainSampleApp: App {
    let persistenceController = PersistenceController.shared
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
