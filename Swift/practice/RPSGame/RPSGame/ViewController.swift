//
//  ViewController.swift
//  RPSGame
//
//  Created by Sebin Kwon on 2023/08/15.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var mainLabel: UILabel!
    
    @IBOutlet weak var comImageView: UIImageView!
    @IBOutlet weak var myImageView: UIImageView!
    
    
    @IBOutlet weak var comChoiceLabel: UILabel!
    @IBOutlet weak var myChoiceLabel: UILabel!
    
    var comChoice: Rps = Rps(rawValue: Int.random(in: 0...2))!
    var myChoice: Rps = Rps.rock

    
    override func viewDidLoad() {
        super.viewDidLoad()
        comImageView.image = UIImage(named: "ready.png")
        myImageView.image = UIImage(named: "ready.png")
        
        comChoiceLabel.text = "준비"
        myChoiceLabel.text = "준비"
    }

    @IBAction func rpsButtonTapped(_ sender: UIButton) {
//        guard let title = sender.currentTitle else {
//            return
//        }
        let title = sender.currentTitle!
        switch title {
        case "가위":
            myChoice = Rps.scissors
        case "바위":
            myChoice = Rps.rock
        case "보":
            myChoice = Rps.paper
        default:
            break
        }
        
    }
    
    @IBAction func selectButtonTapped(_ sender: UIButton) {
        
        switch comChoice {
        case .rock:
            comImageView.image = UIImage(named: "rock.png")
            comChoiceLabel.text = "바위"
        case .paper:
            comImageView.image = UIImage(named: "paper.png")
            comChoiceLabel.text = "바위"
        case .scissors:
            comImageView.image = UIImage(named: "scissors.png")
            comChoiceLabel.text = "가위"
        }
        
        switch myChoice {
        case .rock:
            myImageView.image = UIImage(named: "rock.png")
            myChoiceLabel.text = "바위"
        case .paper:
            myImageView.image = UIImage(named: "paper.png")
            myChoiceLabel.text = "바위"
        case .scissors:
            myImageView.image = UIImage(named: "scissors.png")
            myChoiceLabel.text = "가위"
        }
        
        if comChoice == myChoice {
            mainLabel.text = "비겼다"
        } else if comChoice == .rock && myChoice == .paper {
            mainLabel.text = "이겼다"
        } else if comChoice == .paper && myChoice == .scissors {
            mainLabel.text = "이겼다"
        } else if comChoice == .scissors && myChoice == .rock {
            mainLabel.text = "이겼다"
        } else {
            mainLabel.text = "졌다"
        }
    }
    
    @IBAction func resetButtonTapped(_ sender: UIButton) {
        comImageView.image = UIImage(named: "ready.png")
        comChoiceLabel.text = "준비"
        
        myImageView.image = UIImage(named: "ready.png")
        myChoiceLabel.text = "준비"
        
        mainLabel.text = "선택하세요"
        
        comChoice = Rps(rawValue: Int.random(in: 0...2))!
    }
    
}
