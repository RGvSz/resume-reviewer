# ResumeAI — AI Resume Reviewer

An AI-powered resume reviewer that scores your resume against job descriptions, finds missing keywords, and rewrites weak bullet points.

## Setup (5 minutes)

### 1. Install dependencies
pip install -r requirements.txt

### 2. Get your free Groq API key
Go to https://console.groq.com, sign up free (no credit card), and create an API key.

### 3. Create a .env file
Create a file called .env in your project folder and add:
GROQ_API_KEY=your_groq_key_here

### 4. Run locally
uvicorn main:app --reload

Open http://localhost:8000 in your browser. That's it!

## Deploy to Vercel 

### 1. Push to GitHub
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/YOUR_USERNAME/resume-reviewer.git
git push -u origin main

### 2. Deploy on Vercel
1. Go to https://vercel.com and sign up free
2. Click "New Project" → Import your GitHub repo
3. Add environment variable: GROQ_API_KEY = your key
4. Click Deploy

Your app will be live at yourapp.vercel.app in 2 minutes!
