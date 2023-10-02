//
//  ContentView.swift
//  DynamicTypePractice
//
//  Created by Sebin Kwon on 2023/09/26.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            List {
                Section {
                    HStack {
                        VStack(alignment: .leading) {
                            Text("QR코드 스캔")
                                .font(.title3)
                                .fontWeight(.semibold)
                                .padding(0.5)
                            Text("결제, 본인확인, 로그인")
                                .font(.callout)
                                .foregroundColor(Color.gray)
                        }
                        Spacer()
                        Image(systemName: "gear")
                    }
                    .padding(1)
                }
                Section {
                    HStack {
                        VStack(alignment: .leading) {
                            Text("숫자코드 입력")
                                .font(.title3)
                                .fontWeight(.semibold)
                                .padding(0.5)
                            Text("결제, 본인확인, 로그인")
                                .font(.callout)
                                .foregroundColor(Color.gray)
                        }
                        Spacer()
                        Image(systemName: "gear")
                    }
                    .padding(1)
                }
                Section {
                    HStack {
                        VStack(alignment: .leading) {
                            Text("바코드 결제")
                                .font(.title3)
                                .fontWeight(.semibold)
                                .padding(0.5)
                            Text("결제, 본인확인, 로그인")
                                .font(.callout)
                                .foregroundColor(Color.gray)
                        }
                        Spacer()
                        Image(systemName: "gear")
                    }
                    .padding(1)
                }
                Section {
                    HStack {
                        VStack(alignment: .leading) {
                            Text("QR코드 스캔")
                                .font(.title2)
                                .bold()
                                .padding(0.5)
                            Text("결제, 본인확인, 로그인")
                                .font(.callout)
                                .foregroundColor(Color.secondary)
                        }
                        Spacer()
                        Image(systemName: "gear")
                    }
                    .padding(1)
                }
            }
            .navigationTitle("Card")
            .toolbar {
                Image(systemName: "gear")
                    .foregroundColor(.gray)
            }
        }
        
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
