import requests


class OptimismApi:
    def __init__(self):
        self.url_base = 'https://optimism.blockscout.com/api/v2/'
        self.api_key = None

    def set_api_key_token(self, api_key: str):
        self.api_key = api_key

    def api_request(self, endpoint, method="GET", request_data=None):
        try:
            headers = {
                "x-api-key": self.api_key
            }
            response = requests.request(url=self.url_base + endpoint, method=method, headers=headers, data=request_data)
            if response.status_code == 200:
                response_object = response.json()
                # response_object['status_code'] = 200
                return response_object
            elif response.status_code == 404:
                return f'{self.url_base}{endpoint} is not found'
            else:
                return response.json()
        except Exception as err:
            print(f'Got Exception :{err}')

    def search(self, query: str):
        endpoint = f'/search?q={query}'
        return self.api_request(endpoint)

    def search_check_redirect(self, query: str):
        endpoint = f'/search/check-redirect?q={query}'
        return self.api_request(endpoint)

    def get_transactions(self, filters: str = '', typ: str = '', method: str = ''):
        base_endpoint = '/transactions'
        query_params = []

        if filters:
            query_params.append(f'filter={filters}')
        if typ:
            query_params.append(f'type={typ}')
        if method:
            query_params.append(f'method={method}')

        if query_params:
            query_string = '&'.join(query_params)
            endpoint = f'{base_endpoint}?{query_string}'
        else:
            endpoint = base_endpoint

        return self.api_request(endpoint)

    def get_blocks(self, typ: str = ''):
        base_endpoint = '/blocks'
        if len(typ):
            base_endpoint += f'?type={typ}'
        return self.api_request(base_endpoint)

    def get_main_page_txs(self):
        endpoint = '/main-page/transactions'
        return self.api_request(endpoint)

    def get_main_page_blocks(self):
        endpoint = '/main-page/blocks'
        return self.api_request(endpoint)

    def get_indexing_status(self):
        endpoint = '/main-page/indexing-status'
        return self.api_request(endpoint)

    def get_stats_counter(self):
        endpoint = '/stats'
        return self.api_request(endpoint)

    def get_txs_charts(self):
        endpoint = '/stats/charts/transactions'
        return self.api_request(endpoint)

    def get_market_charts(self):
        endpoint = '/stats/charts/market'
        return self.api_request(endpoint)

    def get_txs_info(self, txs_hash: str):
        endpoint = f'/transactions/{txs_hash}'
        return self.api_request(endpoint)

    def get_token_txs(self, txs_hash: str, typ: str):
        endpoint = f'/transactions/{txs_hash}/token-transfers'
        if len(typ):
            endpoint += f'?type={typ}'
        return self.api_request(endpoint)

    def get_internal_txs(self, txs_hash: str):
        endpoint = f'/transactions/{txs_hash}/internal-transactions'
        return self.api_request(endpoint)

    def get_txs_logs(self, txs_hash: str):
        endpoint = f'/transactions/{txs_hash}/logs'
        return self.api_request(endpoint)

    def get_raw_trace(self, txs_hash: str):
        endpoint = f'/transactions/{txs_hash}/raw-trace'
        return self.api_request(endpoint)

    def get_state_changes(self, txs_hash: str):
        endpoint = f'/transactions/{txs_hash}/state-changes'
        self.api_request(endpoint)
        return self.api_request(endpoint)

    def get_block_info(self, block_hash: str):
        endpoint = f'/blocks/{block_hash}'
        return self.api_request(endpoint)

    def get_block_txs(self, block_hash: str):
        endpoint = f'/blocks/{block_hash}/transactions'
        return self.api_request(endpoint)

    def get_block_withdrawals(self, block_hash: str):
        endpoint = f'/blocks/{block_hash}/withdrawals'
        return self.api_request(endpoint)

    def get_addresses(self):
        endpoint = '/addresses'
        return self.api_request(endpoint)

    def get_address_info(self, address_hash: str):
        endpoint = f'/addresses/{address_hash}'
        return self.api_request(endpoint)

    def get_address_counters(self, address_hash: str):
        endpoint = f'/addresses/{address_hash}/counters'
        return self.api_request(endpoint)

    def get_address_transactions(self, address_hash: str, filters: str = ''):
        endpoint = f'/addresses/{address_hash}/transactions'
        if len(filters):
            endpoint += f'?filter={filters}'
        return self.api_request(endpoint)

    def get_address_token_transfer(self, address_hash: str, filters: str = '', typ: str = '', token: str = ''):
        endpoint = f'/addresses/{address_hash}/transactions'
        query_params = []
        if len(filters):
            query_params.append(f'filter={filters}')
        if len(typ):
            query_params.append(f'type={typ}')
        if len(token):
            query_params.append(f'token={token}')
        if len(query_params):
            query = '&'.join(query_params)
            endpoint += f'?{query}'
        return self.api_request(endpoint)

    def get_address_internal_txs(self, address_hash: str, filters: str = ''):
        endpoint = f'/addresses/{address_hash}/internal-transactions'
        if len(filters):
            endpoint += f'?filter={filters}'
        return self.api_request(endpoint)

    def get_address_logs(self, address_hash: str):
        endpoint = f'/addresses/{address_hash}/logs'
        return self.api_request(endpoint)

    def get_blocks_validated_by_address(self, address_hash: str):
        endpoint = f'/addresses/{address_hash}/blocks-validate'
        return self.api_request(endpoint)

    def get_token_balance_for_address(self, address_hash: str):
        endpoint = f'/addresses/{address_hash}/token-balances'
        return self.api_request(endpoint)

    def get_coin_balance_history(self, address_hash: str):
        endpoint = f'/addresses/{address_hash}/coin-balance-history'
        return self.api_request(endpoint)

    def get_coin_balance_history_by_day(self, address_hash: str):
        endpoint = f'/addresses/{address_hash}/coin-balance-history-by-day'
        return self.api_request(endpoint)

    def get_address_withdrawal(self, address_hash: str):
        endpoint = f'/addresses/{address_hash}/withdrawals'
        return self.api_request(endpoint)

    def get_list_of_NFT_by_address(self, address_hash: str, typ: str = ''):
        endpoint = f'/addresses/{address_hash}/nft'
        if len(typ):
            endpoint += f'?type={typ}'
        return self.api_request(endpoint)

    def get_list_of_NFT_collections_by_address(self, address_hash: str, typ: str = ''):
        endpoint = f'/addresses/{address_hash}/nft/collections'
        if len(typ):
            endpoint += f'?type={typ}'
        return self.api_request(endpoint)

    def get_tokens_list(self, query: str = '', typ: str = ''):
        endpoint = f'/tokens'
        query_params = []
        if len(query):
            query_params.append(f'q={query}')
        if len(typ):
            query_params.append(f'type={typ}')
        if len(query_params):
            q = '&'.join(query_params)
            endpoint += q
        return self.api_request(endpoint)

    def get_token_info(self, address_hash: str):
        endpoint = f'/tokens/{address_hash}'
        return self.api_request(endpoint)

    def get_token_transfers(self, address_hash: str):
        endpoint = f'/tokens/{address_hash}/transfers'
        return self.api_request(endpoint)

    def get_token_holders(self, address_hash: str):
        endpoint = f'/tokens/{address_hash}/holders'
        return self.api_request(endpoint)

    def get_token_counters(self, address_hash: str):
        endpoint = f'/tokens/{address_hash}/counters'
        return self.api_request(endpoint)

    def get_nft_instances(self, address_hash: str):
        endpoint = f'/tokens/{address_hash}/instances'
        return self.api_request(endpoint)

    def get_nft_instances_by_id(self, address_hash: str, id: int):
        endpoint = f'/tokens/{address_hash}/instances/{id}'
        return self.api_request(endpoint)

    def get_transfer_of_nft_instance(self, address_hash: str, id: int):
        endpoint = f'/tokens/{address_hash}/instances/{id}/transfers'
        return self.api_request(endpoint)

    def get_token_instance_holders(self, address_hash: str, id: int):
        endpoint = f'/tokens/{address_hash}/instances/{id}/holders'
        return self.api_request(endpoint)

    def get_transfer_count_of_nft_instance(self, address_hash: str, id: int):
        endpoint = f'/tokens/{address_hash}/instances/{id}/transfers-count'
        return self.api_request(endpoint)

    def get_smart_contracts(self, query: str = '', typ: str = ''):
        endpoint = f'//smart-contracts'
        query_params = []
        if len(query):
            query_params.append(f'q={query}')
        if len(typ):
            query_params.append(f'type={typ}')
        if len(query_params):
            q = '&'.join(query_params)
            endpoint += q
        return self.api_request(endpoint)

    def get_verified_smart_contracts_counters(self):
        endpoint = f'/smart-contracts/counters'
        return self.api_request(endpoint)

    def get_smart_contract(self, address_hash:str):
        endpoint = f'/smart-contracts/{address_hash}'
        return self.api_request(endpoint)

    def get_read_methods(self,address_hash:str, is_custom_abi: str = '', frm: str = ''):
        endpoint = f'/smart-contracts/{address_hash}/methods-read'
        query_params = []
        if len(is_custom_abi):
            query_params.append(f'is_custom_abi={is_custom_abi}')
        if len(frm):
            query_params.append(f'from={frm}')
        if len(query_params):
            q = '&'.join(query_params)
            endpoint += q
        return self.api_request(endpoint)

    def get_read_methods_proxy(self,address_hash:str, is_custom_abi: str = '', frm: str = ''):
        endpoint = f'/smart-contracts/{address_hash}/methods-read-proxy'
        query_params = []
        if len(is_custom_abi):
            query_params.append(f'is_custom_abi={is_custom_abi}')
        if len(frm):
            query_params.append(f'from={frm}')
        if len(query_params):
            q = '&'.join(query_params)
            endpoint += q
        return self.api_request(endpoint)

    def get_write_methods(self,address_hash:str, is_custom_abi: str = ''):
        endpoint = f'/smart-contracts/{address_hash}/methods-read'
        if len(is_custom_abi):
            endpoint += f'is_custom_abi={is_custom_abi}'
        return self.api_request(endpoint)

    def get_write_methods_proxy(self,address_hash:str, is_custom_abi: str = ''):
        endpoint = f'/smart-contracts/{address_hash}/methods-read-proxy'
        if len(is_custom_abi):
            endpoint += f'is_custom_abi={is_custom_abi}'
        return self.api_request(endpoint)

    def get_json_rpc_url(self):
        endpoint = '/config/json-rpc-url'
        return self.api_request(endpoint)

    def get_withdrawals(self):
        endpoint = '/withdrawals'
        return self.api_request(endpoint)

