//
//  AddMovieView.swift
//  mainSample
//
//  Created by Sebin Kwon on 2023/05/23.
//
import CoreData
import SwiftUI

struct AddMovieView: View {
    @Environment(\.managedObjectContext) var managedObjectContext
    @Environment(\.dismiss) var dismiss
    
    @State private var title = ""
    @State private var rating = 3
    @State private var review = ""
    @State private var genre = "Fantasy"
    
    let genres = ["Fantasy", "Horror", "Mystery", "Romence"]
    
    var body: some View {
        NavigationView {
            Form {
                Section {
                    TextField("Name of Movie", text: $title)
                    Picker("Genre", selection: $genre) {
                        ForEach(genres, id: \.self) {
                            Text($0)
                        }
                    }
                }
                
                Section {
                    TextField("Review of Movie", text: $review)
                    Picker("Rating", selection: $rating) {
                        ForEach(0..<6) {
                            Text(String($0))
                        }
                    }
                } header: {
                    Text("Write a review")
                }
                
                Section {
                    Button("Save") {
                        addMovie(title: title, rating: Int16(rating), review: review, genre: genre, id: UUID())
                        dismiss()
                    }
                }
            }
            .navigationTitle("Add Movie")
        }
    }

    func addMovie(title: String, rating: Int16, review: String, genre: String, id: UUID) {
        let newMovie = Movie(context: managedObjectContext)
        let order = fetchLatestOrder() + 1
        newMovie.title = title
        newMovie.rating = rating
        newMovie.review = review
        newMovie.genre = genre
        newMovie.id = id
        newMovie.order = Int16(order)
        PersistenceController.shared.saveContext()
    }
    
    private func fetchLatestOrder() -> Int16 {
        let fetchRequest: NSFetchRequest<Movie> = Movie.fetchRequest()
        fetchRequest.sortDescriptors = [NSSortDescriptor(keyPath: \Movie.order, ascending: false)]
        fetchRequest.fetchLimit = 1

        do {
            let lastCompliment = try managedObjectContext.fetch(fetchRequest).first
            return lastCompliment?.order ?? 0
        } catch {
            print("Failed to fetch last order: \(error)")
            return 0
        }
    }
}

struct AddMovieView_Previews: PreviewProvider {
    static var previews: some View {
        AddMovieView()
    }
}
