# Import all necessary libraries
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient
import base64
import json

# This SDK works for testnet 
def filter_response_only(response, network, APP_ID):

    if network == "localnet":
        print("Localnet client and indexer created !!!")
        algod_address_local = "http://localhost:4001"
        algod_token = "a" * 64
        indexer_url_local = "http://localhost:8980"
        algod_client = AlgodClient(algod_token, algod_address_local)
        indexer_client = IndexerClient("", indexer_url_local)


    elif network == "testnet":
        print("Testnet client and indexer created !!!")
        algod_address_testnet = "https://testnet-api.algonode.cloud"
        algod_token = "a" * 64
        indexer_url_testnet = "https://testnet-idx.algonode.cloud"
        algod_client = AlgodClient(algod_token, algod_address_testnet)
        indexer_client = IndexerClient("", indexer_url_testnet)


    elif network == "mainnet":
        print("Mainnet functionalities are yet to be implemented !!!!")


    else:
        print("Please select either 'localnet' or 'testnet'")
        raise Exception("Invalid network name !!!")



    # Filter all data from response
    application_id = response.tx_info["txn"]["txn"]["apid"]
    gas_fees = response.tx_info["txn"]["txn"]["fee"]
    block_num = response.confirmed_round
    transaction_id = response.tx_id
    sender_wallet = response.tx_info['txn']['txn']['snd']
    block_info = algod_client.block_info(block_num)
    block_timestamp = block_info["block"]["ts"]

    print(f"Application ID: {application_id}, Gas Fees: {gas_fees}, Block Number: {block_num}, Transaction ID: {transaction_id}")
    print(f"Sender Wallet: {sender_wallet}")
    print(f"Application ID: {application_id}")
    print(f"Gas Fees: {gas_fees}")
    print(f"Block Number: {block_num}")
    print(f"Transaction ID: {transaction_id}")
    print(f"Block Timestamp :- {block_timestamp}")

    def fetch_transactions(address):
        # all_transaction_details = []
        response = indexer_client.search_transactions(address=address, application_id=APP_ID)
        transactions = response["transactions"]
        print("--------------------------------------------------")
        print(f"All the transactions :- ")
        print("--------------------------------------------------")
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
            else:
                print("There is not data in the Global Storage !!!")
        return json.dumps(data_dictionary)

                
        # return all_transaction_details

    filtered_transaction = fetch_transactions(sender_wallet)
    return filtered_transaction


    