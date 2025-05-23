import json
import os
import re




class AccountManager:
    def __init__(self):
        self.next_account_no = 1001  # 시작 번호를 그냥 1001로 고정
        self.accounts = {}
        self.balances = {}
 
    def create_account(self, user_name, resident_id): #계좌 생성
        account_no = self.next_account_no
        self.accounts[account_no] = {
            "user_name": user_name,
            "resident_id": resident_id}

        print(f"{account_no}번 계좌가 생성되었습니다.")
        self.next_account_no += 1 #다음 계좌 준비

    def close_account(self, account_no):  #계좌 삭제(잔액이 일 때)
        if account_no not in self.accounts:
            print("존재하지 않는 계좌번호입니다.")
            return
        balance = self.balances.get(account_no, 0)
        if balance == 0:
            del self.accounts[account_no]
            del self.balances[account_no]
            print(f"{account_no}번 계좌가 해지되었습니다.")
        else:
            print("잔액이 남아있습니다.")

    def verify_account(self, account_no):  # 계좌 존재 여부 확인
        if account_no in self.accounts:
            print(f"✅ {account_no}번 계좌가 존재합니다.")
            return True
        else:
            print(f"❌ {account_no}번 계좌가 존재하지 않습니다.")
            return False

    def validate_resident_id(self, resident_id):
        # 주민번호 형식: YYYYMMDD-XXXXXXX (총 14자리, 하이픈 포함)
        pattern = r'^\d{6}-\d{7}$'
        if re.match(pattern, resident_id):
            return True
        else:
            return False