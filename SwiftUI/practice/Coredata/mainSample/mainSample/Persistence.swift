//
//  Persistence.swift
//  mainSample
//
//  Created by Sebin Kwon on 2023/05/23.
//

import CoreData

struct PersistenceController {
    static let shared = PersistenceController()
    
    let container: NSPersistentContainer

     init(inMemory: Bool = false) {
       container = NSPersistentContainer(name: "Model")
       container.loadPersistentStores { _, error in
         if let error = error as NSError? {
           fatalError("Unresolved error \(error), \(error.userInfo)")
         }
       }
     }
    
    func saveContext() {
        let context = container.viewContext
        if context.hasChanges {
            do {
                try context.save()
            } catch {
                let nserror = error as NSError
                fatalError("Unresolved error \(nserror), \(nserror.userInfo)")
            }
        }
    }
}
