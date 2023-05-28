//
//  EmogiMemoryGame.swift
//  Memorize
//
//  Created by Sebin Kwon on 2023/04/30.
//

import SwiftUI

class EmogiMemoryGame {
   static var emojis = ["🚗", "🚕", "🚙", "🚌", "🚎", "🏎️", "🚓", "🚑", "🚒", "🛻", "🚚", "🚛", "🚜", "🛵", "🏍️", "🛺", "🚠", "🚡", "🚟", "🚃", "🚋", "🚞", "🚝", "🚄", "🚅", "🚈", "🚂", "⛵️", "🚤"]
    
    static func createMemoryGame() -> MemoryGame<String> {
        MemoryGame<String>(numberOfPairsOfCards: 4) {pairIndex in EmogiMemoryGame.emojis[pairIndex]
        }
    }
    
    private var model: MemoryGame<String> = EmogiMemoryGame.createMemoryGame()
    
    var cards: Array<MemoryGame<String>.Card> {
        return model.cards
    }
}
