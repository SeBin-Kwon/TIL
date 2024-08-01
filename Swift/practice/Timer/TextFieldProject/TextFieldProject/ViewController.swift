//
//  ViewController.swift
//  TextFieldProject
//
//  Created by Sebin Kwon on 7/31/24.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var textField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setup()
    }
    
    func setup() {
        view.backgroundColor = UIColor.gray
        textField.keyboardType = .emailAddress
        textField.placeholder = "이메일 입력"
        textField.borderStyle = .roundedRect
        textField.clearButtonMode = .always
        textField.returnKeyType = .next
    }

    @IBAction func doneButtonTapped(_ sender: UIButton) {
    }
    
}

