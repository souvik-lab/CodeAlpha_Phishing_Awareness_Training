def run_quiz():
    print("=" * 65)
    print("       PHISHING AWARENESS & SOCIAL ENGINEERING QUIZ          ")
    print("=" * 65)
    
    questions = [
        {
            "q": "1. You receive an email from 'support@micros0ft.com' requesting an urgent password update. What is the main red flag?",
            "options": [
                "A) The email contains a link",
                "B) The domain uses typosquatting ('0' instead of 'o')",
                "C) The email was sent during business hours"
            ],
            "ans": "B",
            "explanation": "Attackers frequently use typosquatted look-alike domains to mimic legitimate organizations."
        },
        {
            "q": "2. Does an HTTPS padlock icon confirm that a website is legitimate and safe?",
            "options": [
                "A) Yes, HTTPS ensures the organization has been verified",
                "B) No, HTTPS only encrypts the connection; attackers can obtain SSL certs for phishing domains",
                "C) Yes, malicious sites cannot use encryption"
            ],
            "ans": "B",
            "explanation": "HTTPS only encrypts data in transit. Phishing sites commonly use valid SSL certificates."
        },
        {
            "q": "3. What is the primary objective of a Business Email Compromise (BEC) attack?",
            "options": [
                "A) Injecting ransomware into a database",
                "B) Tricking employees into making unauthorized wire transfers or sharing sensitive data",
                "C) Overloading network bandwidth with ICMP packets"
            ],
            "ans": "B",
            "explanation": "BEC attacks impersonate executives or trusted partners to facilitate fraudulent financial transfers."
        }
    ]

    score = 0
    for item in questions:
        print(f"\n{item['q']}")
        for opt in item['options']:
            print(f"  {opt}")
        
        choice = input("\nYour Answer (A/B/C): ").strip().upper()
        if choice == item['ans']:
            print(" Correct!")
            score += 1
        else:
            print(f" Incorrect! The correct answer was {item['ans']}.")
        print(f"Explanation: {item['explanation']}\n" + "-" * 55)

    print(f"\nQuiz Completed! Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("Excellent! You passed the phishing awareness evaluation.")
    else:
        print("Review the awareness slides to strengthen your phishing detection skills.")

if __name__ == "__main__":
    run_quiz()