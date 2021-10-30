from brownie import FundMe
from scripts.helpers import get_account


def fundMe():
  fund_me = FundMe[-1]
  account = get_account()
  entrance_fee = fund_me.getEntranceFee()
  print(f"Entrance fee: {entrance_fee} gwei")
  print(f"Ether price: {fund_me.getPrice()}")
  print(f"getConversionRate: {fund_me.getConversionRate(entrance_fee)}")
  fund_me.fund({'from': account, 'value': entrance_fee})
  print('Funded!')

  return fund_me

def withdraw():
  fund_me = FundMe[-1]
  account = get_account()
  fund_me.withdraw({'from': account})
  print('Withdrawed!')

def main():
  fundMe()
  withdraw()