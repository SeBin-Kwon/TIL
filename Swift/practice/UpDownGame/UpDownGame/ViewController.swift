//
//  ViewController.swift
//  UpDownGame
//
//  Created by Sebin Kwon on 1/24/24.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var mainLabel: UILabel!
    @IBOutlet weak var numberLabel: UILabel!
    
    var comNumber = Int.random(in: 1...10)
//    var myNumber: Int = 1
    
    override func viewDidLoad() {
        super.viewDidLoad()
        mainLabel.text = "선택하세요"
        numberLabel.text = ""
    }

    @IBAction func buttonTapped(_ sender: UIButton) {
        guard let numString = sender.currentTitle else { return }
        numberLabel.text = numString
//        guard let num = Int(numString) else { return }
//        myNumber = num
    }
    
    @IBAction func selectButtonTapped(_ sender: UIButton) {
        guard let myNumString = numberLabel.text else { return }
        guard let myNumber = Int(myNumString) else { return }
        
        if comNumber > myNumber {
            mainLabel.text = "Up"
        } else if comNumber < myNumber {
            mainLabel.text = "Down"
        } else {
            mainLabel.text = "Bingo😎"
        }
    }
    
    @IBAction func resetButtonTapped(_ sender: UIButton) {
        mainLabel.text = "선택하세요"
        numberLabel.text = ""
        comNumber = Int.random(in: 1...10)
    }
}

