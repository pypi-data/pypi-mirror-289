# %%

import requests
import pandas as pd
from datetime import datetime
import pytz

class PolymarketDataFetcher:
    def __init__(self):
        self.base_url = "https://gamma-api.polymarket.com"
        self.clob_url = "https://clob.polymarket.com"

    def get_outcome_ids(self, slug):
        '''
        returns asset ids for an outcome slug in a market
        '''
        url = f"{self.base_url}/markets?active=true&closed=false&limit=-1"
        r = requests.get(url).json()
        df = pd.DataFrame(r)
        market = df[df['slug'] == slug]
        if not market.empty:
            outcomes = market['outcomes'].iloc[0]
            clob_token_ids = market['clobTokenIds'].iloc[0]
            if isinstance(outcomes, str):
                outcomes = eval(outcomes)
            if isinstance(clob_token_ids, str):
                clob_token_ids = eval(clob_token_ids)
            return dict(zip(outcomes, clob_token_ids))
        else:
            return None

    def _get_historical_data(self, asset_id, startTs, fidelity):
        '''
        returns historical data for an single asset id
        '''
        url = f"{self.clob_url}/prices-history?startTs={startTs}&market={asset_id}&earliestTimestamp=1704096000&fidelity={fidelity}"
        return requests.get(url).json()["history"]

    def _generate_df(self, data, name):
        '''
        converts response to dataframe and formats
        '''
        df = pd.DataFrame(data)
        pt_timezone = pytz.timezone('US/Pacific')
        et_timezone = pytz.timezone('US/Eastern')
        df['timestamp'] = df['t'].apply(
            lambda x: datetime.fromtimestamp(x, pt_timezone)
            .astimezone(et_timezone)
            .strftime('%m/%d/%Y')
        )
        df[name] = df['p'].apply(lambda x: f"{x:.4f}")
        df = df[['timestamp', name]]
        return df

    def get_historical_data_for_outcomes(self, outcome_ids, startTs, fidelity):
        '''
        retunrs historical data for an outcome_id dictionary
        '''
        dfs = []
        for outcome, asset_id in outcome_ids.items():
            data = self._get_historical_data(asset_id, startTs, fidelity)
            df = self._generate_df(data, outcome)
            dfs.append(df)
        final_df = dfs[0]
        for df in dfs[1:]:
            final_df = final_df.merge(df, on='timestamp', how='outer')
        final_df = final_df.sort_values(by='timestamp').reset_index(drop=True)
        return final_df

    def convert_date_format(self, date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return int(date_obj.timestamp())


    def get_historical_odds(self, slug, start_date, fidelity="1440"):
        '''
        returns historical odds for a market outcome slug
        '''
        start_ts = self.convert_date_format(start_date)
        outcome_ids = self.get_outcome_ids(slug)
        if outcome_ids:
            try:
                return self.get_historical_data_for_outcomes(outcome_ids, start_ts, fidelity)
            except Exception as e:
                print(f"Error fetching historical odds: {e}")
                return None
        else:
            print(f"No matching market found for slug: {slug}")
            return None

if __name__ == "__main__":
    # Example usage
    pm = PolymarketDataFetcher()
    slug = "will-donald-trump-win-the-2024-us-presidential-election"
    start_date = "2024-01-01"  # yyyy-mm-dd format
    fidelity = "1440" 


    # Fetch historical odds for a market
    odds = pm.get_historical_odds(slug, start_date, fidelity)

# %%
