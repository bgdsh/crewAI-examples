from crewai import Agent

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

class SmartContractAnalysisAgents():
  def crypto_currency_analyst(self):
    return Agent(
      role='The Best Crypto Currency Analyst',
      goal="""Impress all customers with your crypto currency data 
      and market trends analysis""",
      backstory="""The most seasoned crypto currency analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate,
        SECTools.search_10q,
        SECTools.search_10k
      ]
    )

  def research_analyst(self):
    return Agent(
      role='Staff Crypto Currency Research Analyst',
      goal="""Being the best at gather, interpret crypto currency and blockchain data and amaze
      your customer with it""",
      backstory="""Known as the BEST crypto currency research analyst, you're
      skilled in sifting through news, company announcements, 
      and market sentiments. Now you're working on a super 
      important customer""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        YahooFinanceNewsTool(),
        SECTools.search_10q,
        SECTools.search_10k
      ]
  )

  def investment_advisor(self):
    return Agent(
      role='Private Crypto Currency Investment Advisor',
      goal="""Impress your customers with full analyses over crypto currencies
      and completer investment recommendations""",
      backstory="""You're the most experienced crypto currency investment advisor
      and you combine various analytical insights to formulate
      strategic investment advice. You are now working for
      a super important customer you need to impress.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        CalculatorTools.calculate,
        YahooFinanceNewsTool()
      ]
    )

  def smart_contract_analyst(self):
    return Agent(
      role="Smart Contract Code Analyst",
      goal="Analyse the smart contract code and find any vulnerabilities / bugs and other uncommon patterns",
      backstory="""You're the most experienced smart contract developer and you combine various security incidents to formulate
      the audit report that list all the vulnerabilities / bugs and other uncommon patterns. You are now working for
      a super important customer you need to impress.""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        CalculatorTools.calculate,
        YahooFinanceNewsTool()
      ]
    )