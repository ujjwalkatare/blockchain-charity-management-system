🔗 Blockchain-Based Charity Donation & Utilization Tracking System

A full-stack Django-based charity management system that leverages Blockchain technology to ensure transparent, secure, and traceable donations and fund utilization.

This project demonstrates real-world blockchain integration, secure role-based authentication, transaction verification, and end-to-end donation tracking, making it suitable for academic projects, portfolios, and interviews.

---

🚀 Key Features

🔐 Secure Role-Based Authentication

Donor, Trust (NGO), and Super Admin login system  
Session-based Super Admin authentication  
Prevents unauthorized access to sensitive dashboards  

💰 Blockchain-Verified Donations

Ethereum-based donations verified using MetaMask and Ganache  
Real-time transaction validation via Web3  
Duplicate transaction prevention  
Donation stored in ETH as the source of truth  

🔗 Blockchain Integrity & Transparency

Cryptographic hash generation for each donation  
Immutable donation records  
Blockchain ledger integration for trust-to-user transfers  

🏥 Trust Fund Utilization Tracking

Trusts can utilize received donations  
Purpose, category, and proof (bill/image) upload required  
Prevents fund misuse  

✅ Super Admin Approval System

Admin can approve or reject fund utilization  
Verification timestamp maintained  
Ensures accountability and compliance  

📊 Real-Time Dashboards & Analytics

Donor dashboard with donation history and utilization trace  
Trust dashboard showing balance, donors, and utilization  
Super Admin dashboard with system-wide statistics  

🔍 Donation-to-Utilization Traceability

Complete tracking from donor → trust → utilization  
Donors can view how their funds are spent  
Builds transparency and trust  

---

🧩 How the System Works

![Uploading ChatGPT Image Jan 29, 2026, 11_46_41 AM.png…]()



Donor registers and logs in  
Trust (NGO) registers with verified Ethereum address  
Donor makes a donation using MetaMask  
System verifies the transaction from the blockchain  
Donation is stored securely with integrity hash  
Trust utilizes funds by submitting proof and purpose  
Super Admin verifies or rejects utilization  
Donor can view utilization details in real time  

---

🛠 Tech Stack

Backend  
Python  
Django  
Django ORM  

Blockchain  
Ethereum  
Web3.py  
Ganache  

Frontend  
HTML  
CSS  
Bootstrap  

Database  
SQLite (development)  

Other Tools  
Git & GitHub  
VS Code  
MetaMask  
Ganache 
---

🎯 Real-World Use Case

This system can be used by NGOs, charitable trusts, and social organizations to ensure donation transparency, prevent fund misuse, and build donor confidence using blockchain-backed verification.

---

👤 Author

Ujjwal
