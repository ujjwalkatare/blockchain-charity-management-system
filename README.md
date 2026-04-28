# 🤝 CharityChain — Blockchain-Powered Charity & Donation Management System

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Blockchain-Ethereum-purple?style=for-the-badge&logo=ethereum" />
  <img src="https://img.shields.io/badge/Web3-MetaMask-orange?style=for-the-badge&logo=metamask" />
  <img src="https://img.shields.io/badge/Ganache-Local%20Chain-brown?style=for-the-badge" />
  <img src="https://img.shields.io/badge/SHA--256-Integrity%20Hash-red?style=for-the-badge" />
</p>

<p align="center">
  <b>A transparent, tamper-proof charity donation platform where every ETH donation is verified on the Ethereum blockchain and every rupee of utilization is tracked and approved.</b>
</p>

---

## 🚀 Features

- 🔐 **Multi-role System** — Super Admin, Trust (NGO/Charity), and Donor portals
- 💰 **MetaMask Donations** — Donors send ETH directly to trust wallets via MetaMask
- 🔗 **Blockchain Verification** — Every transaction is verified on-chain via web3.py before being recorded
- 🔒 **SHA-256 Integrity Hash** — Each donation gets a unique integrity hash (sender + receiver + amount + tx hash)
- 📋 **Utilization Tracking** — Trusts record how donated funds are spent (with proof images/bills)
- ✅ **Super Admin Approval** — Every utilization must be approved by Super Admin before it's visible to donors
- 📊 **Donor Transparency** — Donors can see exactly how their money was used (only approved utilizations)
- 💹 **ETH → INR Conversion** — All amounts displayed in INR for easy understanding
- 🏛️ **Super Admin Dashboard** — Full oversight: all donors, all trusts, all transactions, approval stats
- 📁 **Proof Upload** — Trusts upload receipts/bills as proof of fund utilization
- 🚫 **Duplicate TX Protection** — Same transaction hash cannot be recorded twice

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.x (Python) |
| Frontend | Bootstrap 5, HTML, CSS, JS |
| Database | SQLite3 |
| Blockchain | Ethereum (Ganache local chain) |
| Web3 Library | web3.py |
| Wallet | MetaMask |
| Integrity | SHA-256 (hashlib) |

---

## 🔗 Blockchain & Donation Flow

```
DONATION FLOW:
Donor selects a Trust
    → MetaMask popup opens
    → Donor sends ETH to Trust's Ethereum wallet address
    → TX hash sent to Django backend
    → Backend connects to Ganache via web3.py
    → Verifies TX on-chain (sender, receiver, amount)
    → SHA-256 integrity hash generated
    → Donation saved to DB with TX hash + integrity hash

UTILIZATION FLOW:
Trust logs fund usage
    → Enters amount (INR), purpose, category
    → Uploads proof image or bill
    → Utilization saved as "Pending"
    → Super Admin reviews and approves/rejects
    → Approved utilizations become visible to donors

TRANSPARENCY FLOW:
Donor views their donation history
    → Sees each donation (ETH + INR)
    → Sees only APPROVED utilizations for their donations
    → Full traceability from donation → spending → proof
```

---

## 👥 Roles & Access

| Role | Login | Capabilities |
|------|-------|-------------|
| **Super Admin** | `Superadmin@gmail.com` / `Superadmin@123` | View all donors & trusts, approve/reject utilizations, full analytics |
| **Trust** | Register via form | Receive donations, record fund utilization, upload proofs, view donor list |
| **Donor** | Register via form | Browse trusts, donate via MetaMask, view donation history + approved utilizations |

---

## 🛠️ Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/ujjwalkatare/blockchain-charity-management-system.git
cd blockchain-charity-management-system
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install django web3
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start Ganache
- Download [Ganache](https://trufflesuite.com/ganache/)
- Start a new workspace on port **7545**
- Note down account addresses (used as Trust ETH addresses)

### 6. Configure MetaMask
- Add custom network: `http://127.0.0.1:7545` — Chain ID: `1337`
- Import a Ganache account using its private key
- The active MetaMask account should be the **donor's** wallet

### 7. Run the server
```bash
python manage.py runserver
```

### 8. Open in browser
```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
blockchain-charity-management-system/
├── app/
│   ├── models.py          # trust_profile, Donation, Utilization
│   ├── views.py           # All views including donation verification + utilization logic
│   ├── auth.py            # Custom validation helpers
│   ├── urls.py            # URL routing
│   └── admin.py           # Django admin registration
├── templates/
│   ├── index.html                    # Home / landing page
│   ├── log_in.html                   # Unified login page
│   ├── donor_register.html           # Donor registration
│   ├── trust_register.html           # Trust registration with ETH address
│   ├── user_dashboard.html           # Donor dashboard
│   ├── donation.html                 # MetaMask donation page
│   ├── show_donation.html            # Donor's donation history + utilizations
│   ├── trust_dashboard.html          # Trust portal
│   ├── utilize_donation.html         # Trust fund utilization form
│   ├── show_utilization.html         # Trust utilization history
│   ├── super_admin_dashboard.html    # Super Admin overview
│   └── super_admin_transactions.html # Full transaction trace + approval
├── static/                # CSS, JS, images
├── manage.py
└── requirements.txt
```

---

## 📦 Requirements

```
django
web3
```

Install:
```bash
pip install django web3
```

---

## 🔐 Environment Notes

- Ganache must be running on `http://127.0.0.1:7545` before starting the server
- Each Trust must register with a **unique Ganache wallet address** as their ETH address
- The donor's MetaMask account must be connected to the Ganache network (Chain ID: 1337)
- MetaMask active account should be different from the Trust's wallet address
- Never commit private keys to a public repository

---

## 💡 How Transparency Works

1. **Donor donates** → ETH sent on-chain → TX verified → saved with SHA-256 hash
2. **Trust utilizes funds** → records purpose + uploads proof bill/image
3. **Super Admin reviews** → approves or rejects each utilization
4. **Donor views history** → can only see **approved** utilizations → knows exactly where money went

This creates a full accountability chain: every rupee donated is traceable to a blockchain transaction, and every rupee spent is verified by the admin with proof.

---

## 👨‍💻 Author

**Ujjwal Katare**

---

## ⭐ Give a Star

If this project helped you or you found it interesting, please consider giving it a ⭐ on GitHub!
