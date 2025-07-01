from tonpy import Wallet, TonlibClient
from pathlib import Path

client = TonlibClient(lite_servers=["https://toncenter.com/api/v2/jsonRPC"])

# Load your contract cell
contract_cell = Path("build/my_contract.cell").read_bytes()

# Create new wallet or load existing
wallet = Wallet.from_mnemonic(["your", "mnemonic", "here"])

# Deploy contract
contract_address = wallet.deploy_contract(contract_cell, workchain=0)

print(f"Deployed contract to: {contract_address}")

