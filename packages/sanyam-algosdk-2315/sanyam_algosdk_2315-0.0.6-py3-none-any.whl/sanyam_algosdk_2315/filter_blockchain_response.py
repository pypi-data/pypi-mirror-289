# Import all necessary libraries
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient
import base64
import json

# This SDK works for testnet 
def filter_response_only(response,APP_ID):
    
    print("Testnet client and indexer created !!!")
    algod_address_testnet = "https://testnet-api.algonode.cloud"
    algod_token = "a" * 64
    indexer_url_testnet = "https://testnet-idx.algonode.cloud"
    algod_client = AlgodClient(algod_token, algod_address_testnet)
    indexer_client = IndexerClient("", indexer_url_testnet)




    # Filter all data from response
    application_id = response.tx_info["txn"]["txn"]["apid"]
    gas_fees = response.tx_info["txn"]["txn"]["fee"]
    block_num = response.confirmed_round
    transaction_id = response.tx_id
    sender_wallet = response.tx_info['txn']['txn']['snd']
    block_info = algod_client.block_info(block_num)
    block_timestamp = block_info["block"]["ts"]

    def fetch_transactions(address):
        # all_transaction_details = []
        response = indexer_client.search_transactions(address=address, application_id=APP_ID)
        transactions = response["transactions"]
        data_dictionary = {}
        for txn in transactions:
            if 'global-state-delta' in txn:
                global_storage_data = txn['global-state-delta']

                for single_data in global_storage_data:
                    key = single_data['key']
                    string_data = single_data['value']['bytes']
                    int_data = single_data['value']['uint']

                    decoded_key = base64.b64decode(key).decode("utf-8") # These are bytes
                    decoded_string = base64.b64decode(string_data).decode("utf-8")
                    # print(f"Decoded data : \n Key :- {decoded_key} , Bytes:{decoded_string} , intValue:-{int_data} ")
                    if data_dictionary.get(decoded_key) == None:
                        data_dictionary[decoded_key] = {'String_data':[] , "Integer_data":[]}

                    else:
                        data_dictionary[decoded_key]['String_data'].append(decoded_string)
                        data_dictionary[decoded_key]['Integer_data'].append(int_data)
        return json.dumps(data_dictionary)

                
        # return all_transaction_details

    filtered_transaction = fetch_transactions(sender_wallet)


    all_transaction_data = {
        "AppID":application_id,
        "GasFees" : gas_fees,
        "TransactionID":transaction_id,
        "SenderWallet":sender_wallet,
        "BlockNumber": block_num,
        "BlockTimestamp" : block_timestamp,
        "Blockchain_data":filtered_transaction
    }
    
    return all_transaction_data


    