import os

import requests

from langchain.tools import tool

from unstructured.partition.html import partition_html

class CoinGeckoTools():
    @tool("Search Crypto Currency By Keyword")
    def search_crypto_currency_by_keyword(keyword):
        """
        Useful to search crypto currency by keyword.
        """
        url = f"https://api.coingecko.com/api/v3/search?query={keyword}"
        response = requests.request("GET", url)
        res_body = response.json()['coins']
        string = []
        for result in res_body:
            try:
                string.append('\n'.join([
                    f"CoinGecko Id: {result['id']}",
                    f"Name: {result['name']}", 
                    f"Symbol: {result['symbol']}",
                    f"Market Cap Rank: {result['market_cap_rank']}",
                    "\n-----------------"
                ]))
            except KeyError:
                next
        return '\n'.join(string)
    
    @tool("Get Crypto Currency Details by CoinGecko ID")
    def get_crypto_details_by_id(id):
        """
        Useful to get crypto details by id.
        """
        url = f"https://api.coingecko.com/api/v3/coins/{id}"
        response = requests.request("GET", url)
        res_body = response.json()
        string = []
        try:
            string.append('\n'.join([
                f"CoinGecko Id: {res_body['id']}",
                f"Name: {res_body['name']}", 
                f"Symbol: {res_body['symbol']}",
                f"Market Cap Rank: {res_body['market_cap_rank']}",
                # f"Hashing Algorithm: {res_body['hashing_algorithm']}",
                f"Market Data: {res_body['market_data']}",
                f"Description: {res_body['description']['en']}",
                f"Categories: {','.join(res_body['categories'])}",
                f"Contract Address: {res_body['contract_address']}",
                f"Homepage: {','.join(res_body['links']['homepage'])}",
                f"Tiwtter: {res_body['links']['twitter_screen_name']}",
                f"Blockchain Site: {','.join(res_body['links']['blockchain_site'])}",
                f"Current Price: {res_body['market_data']['current_price']['usd']}",
                f"High 24h: {res_body['market_data']['high_24h']['usd']}",
                f"Low 24h: {res_body['market_data']['low_24h']['usd']}",
                f"All Time High: {res_body['market_data']['ath']['usd']}@{res_body['market_data']['ath_date']['usd']}",
                f"All Time Low: {res_body['market_data']['atl']['usd']}@{res_body['market_data']['atl_date']['usd']}",
                f"Total Supply: {res_body['market_data']['total_supply']}",
                f"Max Supply: {res_body['market_data']['max_supply']}",
                f"Circulating Supply: {res_body['market_data']['circulating_supply']}",
                f"Market Cap: {res_body['market_data']['market_cap']['usd']}",
                f"Total Value Locked: {res_body['market_data']['total_value_locked']['usd']}",
                f"Last Updated: {res_body['last_updated']}",
            ]))
            platforms = []
            for platform, contract in res_body['platforms'].items():
                platforms.append(f"{platform} address: {contract}")
            string.append('\n'.join(platforms))
        except KeyError:
            next
        return '\n'.join(string)
        
