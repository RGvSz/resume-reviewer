# ResumeAI — AI Resume Reviewer

An AI-powered resume reviewer that scores your resume against job descriptions, finds missing keywords, and rewrites weak bullet points.

## Setup (5 minutes)

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your Claude API key
Open `main.py` and replace `your_api_key_here` with your key from https://console.anthropic.com

Or set it as an environment variable:
```bash
export ANTHROPIC_API_KEY=your_key_here
```

### 3. Run locally
```bash
uvicorn main:app --reload
```

Open http://localhost:8000 in your browser. That's it!

## Deploy to Vercel (Free)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/YOUR_USERNAME/resume-reviewer.git
git push -u origin main
```

### 2. Deploy on Vercel
1. Go to https://vercel.com and sign up free
2. Click "New Project" → Import your GitHub repo
3. Add environment variable: `ANTHROPIC_API_KEY` = your key
4. Click Deploy

Your app will be live at `yourapp.vercel.app` in 2 minutes!

## Monetization
- Offer 3 free reviews/month
- Charge ₹299/month for unlimited reviews
- Add payments via Gumroad or Lemon Squeezy

## Tech Stack
- Backend: Python + FastAPI
- Frontend: HTML/CSS/JS
- AI: Claude API (claude-sonnet-4-6)
- Hosting: Vercel (free)
