import requests
import json
import argparse
from pytuft.pytuft_config import BLOCKCHAIN_URL, DEPLOYER_ADDRESS

def calculate_fee(transaction_data, transaction_type):
    payload = {'transaction_data': transaction_data, 'transaction_type': transaction_type}
    response = requests.post(f'{BLOCKCHAIN_URL}/calculate_fee', json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to calculate fee: {response.json()['error']}")

def get_account_balance(address):
    payload = {'address': address}
    response = requests.post(f'{BLOCKCHAIN_URL}/omc_balance', json=payload)
    if response.status_code == 200:
        return response.json()['balance_float']
    else:
        raise Exception(f"Failed to retrieve account balance: {response.json()}")

def compile_contract(contract_name):
    try:
        contract_module = __import__(f'contracts.{contract_name}', fromlist=[''])
        return contract_module, None
    except Exception as e:
        return None, str(e)

def deploy_contract(contract_name):
    contract_code = open(f'contracts/{contract_name}.py').read()
    transaction_data = {'code': contract_code}
    fee_info = calculate_fee(transaction_data, 'deploy')
    print(f"Calculated deployment fee: {fee_info['cost']}")

    balance = get_account_balance(DEPLOYER_ADDRESS)
    print(f"Current balance: {balance}")
    
    if balance < fee_info['cost']:
        print(f"Insufficient balance to deploy contract. Required: {fee_info['cost']}, Available: {balance}")
        return

    data = {
        'contract_code': contract_code,
        'deployer_address': DEPLOYER_ADDRESS
    }

    response = requests.post(f'{BLOCKCHAIN_URL}/deploy', json=data)
    if response.status_code == 200:
        print(f"Contract deployed: {response.json()['contract_id']}")
    else:
        print(f"Deployment failed: {response.json()['error']}")

def execute_contract(contract_id, function_name, args):
    transaction_data = {'contract_id': contract_id, 'function_name': function_name, 'args': args}
    fee_info = calculate_fee(transaction_data, 'execute')
    print(f"Calculated execution fee: {fee_info['cost']}")

    balance = get_account_balance(DEPLOYER_ADDRESS)
    print(f"Current balance: {balance}")

    if balance < fee_info['cost']:
        print(f"Insufficient balance to execute contract. Required: {fee_info['cost']}, Available: {balance}")
        return

    data = {
        'contract_id': contract_id,
        'function_name': function_name,
        'args': args
    }

    response = requests.post(f'{BLOCKCHAIN_URL}/execute', json=data)
    if response.status_code == 200:
        print(f"Execution result: {response.json()['result']}")
    else:
        print(f"Execution failed: {response.json()['error']}")

def run_tests():
    # This function should contain logic to run tests for smart contracts
    print("Running tests...")

def main():
    parser = argparse.ArgumentParser(description='Truffle-like tool for Python smart contracts')
    parser.add_argument('command', choices=['compile', 'deploy', 'execute', 'test'], help='Command to execute')
    parser.add_argument('contract', nargs='?', help='Contract name for compile and deploy commands')
    parser.add_argument('--contract_id', help='Contract ID for execution')
    parser.add_argument('--function_name', help='Function name for execution')
    parser.add_argument('--args', nargs='*', help='Arguments for the function')
    args = parser.parse_args()

    if args.command == 'compile':
        if args.contract:
            compile_contract(args.contract)
        else:
            print("Please provide a contract name for compilation")
    elif args.command == 'deploy':
        if args.contract:
            deploy_contract(args.contract)
        else:
            print("Please provide a contract name for deployment")
    elif args.command == 'execute':
        if args.contract_id and args.function_name:
            execute_contract(args.contract_id, args.function_name, args.args)
        else:
            print("Please provide contract ID and function name for execution")
    elif args.command == 'test':
        run_tests()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
