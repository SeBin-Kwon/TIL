//
//  ContentView.swift
//  mainSample
//
//  Created by Sebin Kwon on 2023/05/03.
//

import SwiftUI

struct ContentView: View {
    
    @Environment(\.managedObjectContext) var managedObjectContext
    @FetchRequest(entity: Movie.entity(), sortDescriptors: [NSSortDescriptor(keyPath: \Movie.order, ascending: true)]) var movies: FetchedResults<Movie>
    @State private var showingAddScreen = false
    
    var body: some View {
        NavigationView {
            List {
                ForEach(movies, id: \.self) { movie in
                    VStack(alignment: .leading){
                        Text("\(movie.title ?? "")" )
                        Text("\(movie.review ?? "")" )
                    }
                    .contextMenu {
                        Button(action: { deleteMovie(at: IndexSet(integer: movies.firstIndex(of: movie)!)) }) {
                            Label("Delete", systemImage: "trash")
                        }
                    }
                }
                .onDelete(perform: deleteMovie)
            }
            .navigationTitle("Movie")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button {
                        showingAddScreen.toggle()
                    } label: {
                        Label("Add movie", systemImage: "plus")
                    }
                }
            }
            .sheet(isPresented: $showingAddScreen) {
                AddMovieView()
            }
        }
    }

    func deleteMovie(at offsets: IndexSet) {
      offsets.forEach { index in
        let movie = self.movies[index]
        self.managedObjectContext.delete(movie)
      }
        PersistenceController.shared.saveContext()
    }
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            ContentView()
        }
    }
}
