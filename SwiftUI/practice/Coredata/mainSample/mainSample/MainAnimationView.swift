//
//  MainAnimationView.swift
//  mainSample
//
//  Created by Sebin Kwon on 2023/05/03.
//

import SwiftUI

struct MainAnimationView: View {
    let shapes = ["circle", "rectangle", "pentagon"]
    let colors = [Color.red, Color.green, Color.blue]

    var body: some View {
        VStack {
            ZStack {
                GeometryReader { geometry in
                    ForEach(0..<shapes.count, id: \.self) { index in
                        Image(shapes[index])
                            .resizable()
                            .aspectRatio(contentMode: .fit)
                            .frame(width: 200, height: 200)
                            .foregroundColor(colors[index])
                            .offset(y: -geometry.size.height)
                            .animation(Animation.linear(duration: 1.0).delay(Double(index) * 0.2))
                            .zIndex(Double(index))
                    }
                }
                .frame(width: 200, height: 200)
            }
            Text("하이")
                
        }
    }
}


struct MainAnimationView_Previews: PreviewProvider {
    static var previews: some View {
        MainAnimationView()
    }
}
