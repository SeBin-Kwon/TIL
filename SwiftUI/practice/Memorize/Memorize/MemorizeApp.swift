//
//  MemorizeApp.swift
//  Memorize
//
//  Created by Sebin Kwon on 2023/03/23.
//

import SwiftUI

@main
struct MemorizeApp: App {
    let game = EmogiMemoryGame()
    
    var body: some Scene {
        WindowGroup {
            ContentView(viewModel: game)
        }
    }
}
