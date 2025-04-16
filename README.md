# 100-days-of-AI
## Day 1 : AI text summarizer
Welcome to my Day 1 of the #100DaysOfAI challenge!
In this mini-project, I built a simple AI-powered Text Summarizer that reads long texts (like research articles, blogs, essays) and produces concise, meaningful summaries.

### What it does?
Paste any long-form text (essay, article, research intro) and get a quick summary using AI!

 Paste any long text into the UI

 Split the text smartly into manageable chunks

 Summarize using a pre-trained transformer model

 Get a clean summary output in a simple UI

 ### Tech Stack
Transformers
NLTK
Gradio
Google Colab
### How it works?
User pastes the long text into the Gradio textbox

The app splits it into chunks (to avoid token size errors)

Each chunk is passed to the summarization model

AI generates concise summaries for each chunk

All summaries are combined and shown to the user



## DAY2 : EDA Agent
In this mini-project, I built an AI-powered Exploratory Data Analysis (EDA) Agent that takes a dataset and automatically generates detailed insights, summaries, and visualizations.

### What it does?
Upload any CSV file and get an instant overview of the dataset:

✅ Understand data types and structure
✅ Identify missing values and outliers
✅ See summary 

### Tech Stack
Pandas
Matplotlib / Seaborn
Scikit-learn
Streamlit
OpenAI API

### How it works?
📁 User uploads a CSV file
📊 The app reads and analyzes the dataset
🧠 Performs:

Data profiling

Null value detection

Statistical summaries

Visualizations 

## DAY 5: Sales Copilot
In this mini-project, I built a Sales CoPilot – an AI-powered assistant that helps sales professionals research leads, generate insights, and craft outreach strategies using real-time data.

### What it does?
The Sales CoPilot helps streamline and supercharge sales workflows:

✅ Scrapes relevant data from lead websites
✅ Uses AI to generate lead summaries and talking points
✅ Acts as a research assistant for sales prospecting

### Tech Stack
Relevance AI
Firecrawl (for smart web scraping)
OpenAI (for summarization and generation)


### How it works?
🌐 User inputs a lead/company URL
🕸️ Firecrawl scrapes the content from the site
🧠 Relevance AI & OpenAI analyze the content to extract key insights
🚀 Empowers sales reps with instant, AI-curated info

## DAY 6 : Lead Qualification Agent
Today, I built a Lead Qualification Agent that works alongside the Sales CoPilot from Day 5. It automates the process of qualifying leads submitted via a form, using real-time company data and AI-driven logic to decide whether a lead is a good fit—and then sends personalized email responses accordingly.

### What it does?
The Lead Qualification Agent takes in basic lead info (name, email, company URL), analyzes the company using AI, and automates communication:

✅ Scrapes and summarizes company data using the Sales CoPilot
✅ Decides if the lead fits the criteria to work with us
✅ Sends a “Qualified” or “Not Qualified” email via Gmail
✅ All built using n8n workflows and integrated AI agents

### Tech Stack
OpenAI
Relevance AI
Firecrawl
n8n 
Gmail
HTTP + Webhook APIs

###  How it works?
🧾 Lead Qualification Workflow
Triggered on form submission

Sends data to Sales CoPilot via HTTP Request

Company info is enriched and passed to an AI Agent

The AI determines qualification status using the OpenAI chat model

Based on decision, calls a second n8n workflow



✉️ Lead Notifier & Checker Workflow
Executes when called by the previous workflow

Re-evaluates and classifies the lead type (e.g., SaaS vs Agency)

Sends a Gmail message depending on the lead type and qualification

✅ Qualified: Sends a warm outreach email

❌ Not Qualified: Sends a polite rejection or deferment email







 


