import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables if needed (e.g., for HuggingFace API keys)
load_dotenv()

# side bar ha 
st.sidebar.title("📌 Useful Financial Resources")
st.sidebar.markdown("---")

st.sidebar.page_link("https://www.nseindia.com/", label="NSE")
st.sidebar.page_link("https://web.sensibull.com/option-chain?tradingsymbol=NIFTY&view=ltp&expiry=2025-07-24", label="Option chain")

st.sidebar.markdown("---")

st.sidebar.markdown(
    "<h2 style='color:#338;'>📞 Get in Touch</h2>",
    unsafe_allow_html=True
)

st.sidebar.write("#### Multiple ways to reach our team")
st.sidebar.badge("📩 Email")
st.sidebar.markdown("vroo877@gmail.com")
st.sidebar.badge("☎️Phone")
st.sidebar.markdown("+91-6398465336")
st.sidebar.badge("🏠Loction")
st.sidebar.markdown("Seohara, Bijnor, Uttar Pradesh, India 🇮🇳")

st.sidebar.markdown("---")
st.sidebar.caption("Made with ❤️ Vishal Rajput")
# home page desige


st.markdown("""
    <style>
        .nav {
            background-color: #333;
            overflow: hidden;
            display: flex;
            justify-content: center;
        }
        .nav a {
            float: left;
            display: block;
            color: white;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
        }
        .nav a:hover {
            background-color: #ddd;
            color: black;
        }
    </style>

    <div class="nav">
        <a href="#">🏠Home</a>
        <a href="#">Live Stock Data</a>
        <a href="#">Market News</a>
        <a href="http://localhost:8501/?page=Home#company-analysis">Company Analysis</a>
        <a href="http://localhost:8501/?page=Home#contact-us">📞Contact</a>
        
            
    </div>
""", unsafe_allow_html=True)













# --- UI: Title and Subheader ---
st.markdown("""
    <h1 style='text-align: center; color: #00BFFF;'>AI Research Analyst</h1>
    <p style='text-align: center; color: #00BFFF; font-size: 25px;'>
        🔍 Professional equity research powered by AI. Get comprehensive company analysis, legal case reviews, and risk assessments in minutes.
    </p>
""", unsafe_allow_html=True)

# --- Background Style ---


# --- Model Temperature Slider ---
temperature = st.number_input("Efficiency Improvement", min_value=0.1, max_value=2.0, step=0.2, value=0.8)

# --- Setup LLM Model ---
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    temperature=temperature
)
model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

# --- Prompt Template ---
prompt = PromptTemplate(
    input_variables=["name"],  
    template="""
You are a world-class AI trained as a **Professional Equity Research Analyst**. Your job is to generate an in-depth, structured, investment-grade research report on a company.

Target Audience:  
- Institutional Investors  
- Research Analysts  
- PE/VC Analysts  
- Strategic Consultants  

---

### 🔎 Company Name: {name}

Follow this advanced format. Use **markdown headers**, **bullet points**, and a **factual, analytical tone**. Keep the report within 750 words. Prioritize recent information if available.

---

### 🏢 1. Company Overview
- Full company name, type, ticker (if listed)
- Short description of core business
- Key business units or segments
- Industry/sector classification (e.g., IT, Infra, Pharma)
-Ideal length: 600–750 words classifiction in deeply

---

### 🌐 2. Geographical & Market Presence
- HQ location, country of incorporation
- Operational countries & international footprint
- % revenue from top markets or regions
- Key customer base or industry verticals served

---

### 🧱 3. History & Evolution
- Founding year, founders/promoters
- IPO/funding history
- Key historical events (M&A, splits, pivot points)
- Ownership or holding structure

---

### 💰 4. Financial & Valuation Highlights cuurent
- Market cap, P/E, P/B, EV/EBITDA
- 3–5 year financials: revenue, EBITDA, net profit, margins
- Debt profile, liquidity, dividend policy
- Profit growth, ROE/ROCE trend

---

### 🧑‍💼 5. Leadership & Governance
- CEO, MD, Chairperson & key executives
- Management background and tenure
- Board structure, promoter/institutional holding
- Governance strengths or red flags

---

### ⚙️ 6. Business Model & Client Base
- Monetization model: B2B, SaaS, etc.
- Product/service revenue breakdown
- Top clients (if known), contracts, or churn rate
- Technology stack, IP, or key assets

---

### 🧩 7. SWOT Analysis
- **Strengths**: brand, technology, team, growth
- **Weaknesses**: financial, regulatory, operational
- **Opportunities**: sector expansion, new markets
- **Threats**: competition, policy changes, FX risks

---

### 🚧 8. Current Key Projects & Work Pipeline
- Ongoing major projects or product developments
- R&D pipelines or digital transformation initiatives
- Key partnerships, contracts under execution
- Industry collaborations or public-private ventures

---

### 🎯 9. Next Strategic Objectives
- Short-term strategic plans (next 1–2 years)
- Capex, product expansion, new client focus
- International expansion or new vertical entry
- Technological upgradation or automation initiatives

---

### 🔮 10. Vision & Long-Term Goals
- Company's mission and 5–10 year outlook
- Future focus areas (AI, ESG, digital, global scale)
- Statements from leadership on company trajectory
- Analyst/market consensus about direction

---

### 📰 11. Recent Developments & News
- Latest earnings report, investor calls
- New acquisitions, exits, or regulatory updates
- Hiring or leadership transitions
- Press mentions, controversies, or achievements

---

📌 **Final Notes**:
- Use markdown formatting
- Make tone neutral, detailed, and analysis-driven
- Keep it concise but information-dense
- Ideal length: 600–750 words
"""
)
# propmt 2  case
prompt2=PromptTemplate(
    input_variables=["name"],
    template="""

 Ideal length: 500–800 words

You are a world-class AI trained in financial forensics, regulatory law, and equity research.

Your task is to perform a **deep legal case analysis** for the company: **{name}**.



### 🔍 Deep Legal Case Report: {name}

Your analysis should follow this detailed structure:

---

### ⚖️ 1. Case Discovery & Background
- Identify **any recent or ongoing legal, regulatory, or compliance cases** involving {name}
- Type of case: Civil / Criminal / Regulatory
- Authority or Court involved (SEBI, ED, CCI, NCLT, US SEC, etc.)
- When was the case filed or reported?
- Source of discovery (investigation, whistleblower, audit, regulatory probe, etc.)

---

### 📑 2. Nature of Allegations
- Detailed summary of allegations or violations
- Laws, sections, or regulatory frameworks violated
- Named individuals, directors, or promoters (if applicable)
- Any link to previous compliance failures
 Ideal length: 500–800 words

---

### 💣 3. Legal Risk Assessment
- Severity of charges: minor, moderate, or high impact
- Estimated penalties: fines, bans, jail terms, disqualification, asset seizure
- Are key leadership figures (CEO, CFO) involved?
- Does this case have cross-border implications?
 Ideal length: 500–800 words

---

### 💼 4. Operational & Business Impact
- Could this impact licenses, projects, or revenue streams?
- Effect on banking access, government approvals, or supply chain
- Possible disruption to client contracts or vendor relationships
- Is there risk of suspension, blacklisting, or shutdown?
 Ideal length: 500–800 words

---

### 📉 5. Financial & Market Fallout
- Stock price movement after case disclosure (1-day, 1-week, YTD)
- Volume spikes, delivery % changes
- Institutional exits, FII/DII behavior
- Analyst downgrades or changes in earnings forecast
 Ideal length: 500–800 words

---

### 🧠 6. Company’s Legal Strategy & Defense
- Has the company acknowledged the case publicly?
- Any legal firms hired or responses given?
- Early settlement, delay tactics, or compliance effort?
- Leadership or board changes due to the issue
 Ideal length: 500–800 words

---

### 🔮 7. Strategic & Long-Term Outlook
- Best-case vs base-case vs worst-case scenario
- How long might resolution take (based on similar past cases)?
- Likelihood of fines vs full acquittal vs forced restructuring
- Reputational risk in global or institutional markets
 Ideal length: 500–800 words

---

### ✅ 8. Conclusion: Investor Risk Summary
- Risk Score (Low / Moderate / High)
- Investment outlook (Buy / Hold / Exit)
- Top red flags to monitor (e.g., court dates, leadership exits, regulator signals)
 Ideal length: 500–800 words
---

📌 **Instructions:**
- Focus on facts and publicly known information
- Be structured, risk-aware, and analytical
- Use markdown format and bullet points
- Ideal length: 600–900 words for in-depth insight
"""
)
#risk_management_
prompt3 = PromptTemplate(
    input_variables=["name"],
    template="""
You are a world-class AI trained in **risk management, equity analysis, and corporate strategy**. Your task is to generate a detailed and structured **Risk Management Report** for the company: **{name}**.

This report will help investors, strategic consultants, and internal risk teams understand the key risks faced by the company and how it mitigates them.
 Ideal length: 500–800 words
---

### 🧷 Company Risk Profile: {name}

Structure your analysis using the following sections:

---

### 🔍 1. Core Business Risks
- Identify major operational, strategic, and financial risks specific to {name}'s business model
- Supply chain risks, dependency on key vendors, or single-product reliance
- Industry-specific risks (e.g., for pharma, infra, banking, etc.)
 Ideal length: 500–800 words

---

### 🧾 2. Regulatory & Legal Risks
- Exposure to changing laws, compliance burdens, or regulatory penalties
- History of legal or regulatory actions (if any)
- Global vs domestic regulatory risk
 Ideal length: 500–800 words

---

### 💰 3. Financial & Credit Risks
- Leverage and debt profile
- Liquidity position, cash reserves, or working capital cycle
- Exposure to currency, interest rate, or credit risk
 Ideal length: 500–800 words

---

### 🌐 4. Market & Economic Risks
- Risks from economic slowdown, inflation, or FX fluctuations
- Sector cyclicality or geopolitical tensions
- Customer concentration or competitive disruption
 Ideal length: 500–800 words

---

### 👨‍💼 5. Leadership & Governance Risks
- Stability of top leadership and board
- Succession planning, promoter issues, or governance red flags
- Auditor or shareholder conflicts
 Ideal length: 500–800 words

---

### 🧠 6. Cybersecurity & Operational Resilience
- Exposure to data breaches, IT failures, or ransomware
- Business continuity preparedness (e.g., COVID-like events)
- Technology redundancy and risk posture
 Ideal length: 500–800 words

---

### 🛡️ 7. Risk Mitigation Strategy
- Internal controls, policies, or audit mechanisms
- Insurance coverage or hedging strategies
- Proactive steps taken recently to manage key risks
 Ideal length: 500–800 words

---

### 🔮 8. Forward-Looking Risk Forecast
- Risks likely to grow over the next 1–2 years
- Risk rating by area (Low, Moderate, High)
- Suggested watchpoints for investors
 Ideal length: 500–800 words

---

📌 **Instructions:**
- Use recent data where possible  
- Be analytical, structured, and objective  
- Use bullet points or markdown formatting  
- Ideal length: 500–800 words
"""
)
prompt4=PromptTemplate(
    input_variables=["name"],
    template="""
You are an expert equity research analyst working for a top-tier investment firm. Your task is to conduct a detailed peer comparison of a publicly listed company and its key competitors within the same industry.

### Objective:
Perform a relative valuation and fundamental performance analysis comparing the target company with its closest listed peers. Provide actionable insights for long-term investors.

### Details:
- **Target Company:** {name}
- **Sector/Industry:** 
### Include the following metrics for each company:
1. **Market Capitalization** (in ₹ Cr or USD Bn)
2. **Total Revenue** and **Net Profit** (latest fiscal year)
3. **Valuation Multiples:**
   - P/E Ratio (TTM)
   - P/B Ratio
   - EV/EBITDA (if available)
4. **Profitability Ratios:**
   - Return on Equity (ROE)
   - Return on Capital Employed (ROCE)
   - Net Profit Margin (%)
5. **Leverage:**
   - Debt-to-Equity Ratio
6. **Earnings Metrics:**
   - EPS (TTM)
   - 3-year EPS CAGR
7. **Stock Performance:**
   - 1-year and 3-year return (%)
8. **Analyst Ratings & Target Price** (if available)

### Deliverables:
- Present the comparison in a structured and readable table.
- Highlight the **strengths and weaknesses** of each company based on the metrics.
- Provide a **brief written analysis**, comparing performance, valuation, and growth potential.
- End with a concise **investment verdict** on whether the target company appears undervalued, fairly valued, or overvalued compared to its peers, along with rationale.

### Output Format:
1. 📊 Comparison Table  
2. 🧠 Peer Analysis (2-3 paragraphs)  
3. 💡 Investment Verdict (1 paragraph with recommendation)
"""

)
# analysis
st.markdown("---")
st.title("🏢Company Analysis")

company = st.text_input("Enter a company name to generate detailed research reports")


if st.button("Genrated ⇅"):

    with st.spinner("Generating analysis..."):
        chain = prompt | model | parser
        ch=prompt2|model|parser
        cha=prompt3|model|parser
        
        r=ch.invoke({"name":company})
        ra=cha.invoke({"name":company})
        result = chain.invoke({"name": company})  
        st.success("Succefully Excuted")
        st.write("🤖 Response:")
        st.markdown(result)
        st.write(" Legal Case Report")
        st.markdown(r)
        st.write("Risk_Management_")

        st.markdown(ra)
st.markdown("---")

st.title("peer compare")
company_name=st.text_input("company")
if st.button("Peer Compare"):
    chainpeer=prompt4 |model|parser
    rep=chainpeer.invoke({"name":company_name})
    st.markdown(rep)





# yfinanace new

st.markdown("---")

import yfinance as yf
import pandas as pd

# Define sector-wise company tickers


import yfinance as yf

st.title("📊 Company Financial Ratios & Insights")

company_name = st.text_input("Enter Company Name (e.g. TCS, HDFC, Infosys, ITC):")

def find_ticker_by_name(name):
    # Try common NSE tickers with .NS suffix
    possible_tickers = [
        name.upper() + ".NS", name.upper() + ".BO", name.upper()
    ]
    for ticker in possible_tickers:
        try:
            info = yf.Ticker(ticker).info
            if "shortName" in info and name.lower() in info["shortName"].lower():
                return ticker, info
        except:
            continue
    return None, None

if st.button("Get Company Insights"):
    ticker, info = find_ticker_by_name(company_name)

    if ticker and info:
        st.success(f"✅ Found: {info.get('shortName')} ({ticker})")

        st.markdown("### 🧠 Key Financial Ratios & Metrics")

        st.write({
            "Market Cap (Cr)": round(info.get("marketCap", 0) / 1e7, 2),
            "Sector": info.get("sector"),
            "Industry": info.get("industry"),
            "P/E Ratio": info.get("trailingPE"),
            "Forward P/E": info.get("forwardPE"),
            "EPS": info.get("trailingEps"),
            "Price to Book (PB)": info.get("priceToBook"),
            "Return on Equity (ROE %)": round(info.get("returnOnEquity", 0) * 100, 2) if info.get("returnOnEquity") else None,
            "Return on Assets (ROA %)": round(info.get("returnOnAssets", 0) * 100, 2) if info.get("returnOnAssets") else None,
            "Debt to Equity": info.get("debtToEquity"),
            "Dividend Yield (%)": round(info.get("dividendYield", 0) * 100, 2) if info.get("dividendYield") else None,
            "Profit Margin (%)": round(info.get("profitMargins", 0) * 100, 2) if info.get("profitMargins") else None,
            "Operating Margin (%)": round(info.get("operatingMargins", 0) * 100, 2) if info.get("operatingMargins") else None
        })

        st.markdown("### 🏢 Business Summary")
        st.info(info.get("longBusinessSummary", "No summary available."))
    else:
        st.error("❌ Company not found.")

# new
import feedparser
import urllib.parse

st.title("📰 Google News for Companies")

company_name = st.text_input("Enter Company Name")

def get_google_news(company_name):
    query = urllib.parse.quote(company_name)
    url = f"https://news.google.com/rss/search?q={query}"
    feed = feedparser.parse(url)
    return feed.entries

if st.button("Get News"):
    with st.spinner("Fetching news..."):
        news = get_google_news(company_name)
        if news:
            for entry in news[:10]:  # Show top 10 news
                st.markdown(f"### [{entry.title}]({entry.link})")
                st.markdown(f"📅 {entry.published}")
                st.write("---")
        else:
            st.warning("No news found.")

# contract 
st.markdown("---")
import smtplib
from email.message import EmailMessage

st.title("📬 Contact Us")

# Contact form
with st.form(key="contact_form_name"):
    name = st.text_input("Name")
    sender_email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
            st.success(f"Thank you, {name}! Your message has been received.")






# about
st.markdown("---")
st.title("ℹ️ About Us")

st.markdown("""
<h3 style='text-align: center;'>🎯 Our Mission</h3>
""", unsafe_allow_html=True)

st.markdown("""
<div class="mission-box">
    <p style="margin: 0;">
        Welcome to <strong>Stoxly</strong>, your trusted platform for real-time stock market insights and investments. 
        We believe in making stock trading <strong>simple</strong>, <strong>accessible</strong>, and <strong>transparent</strong> for everyone. 
        With live stock data, expert market analysis, and seamless trading tools, we empower investors to make informed decisions. 
        <strong>Join us</strong> and take control of your financial future with confidence!
    </p>
</div>
""", unsafe_allow_html=True)



st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; opacity: 0.7;">
    <p>© 2025 Stoxly AI Insights.  ❤️</p>
    <p style="font-size: 0.9rem;">Professional Stock Market Analysis Platform</p>
</div>
""", unsafe_allow_html=True)




   
    



   #streamlit run c:\Users\vrooo\OneDrive\Desktop\GenAi\Langchain\project.py
   




