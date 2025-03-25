class VendingMachineDFA:
    def __init__(self):
        self.states = {
            'S0': {'1000': 'S1000', '2000': 'S2000', '5000': 'S5000', '10000': 'S10000'},
            'S1000': {'1000': 'S2000', '2000': 'S3000', '5000': 'S6000', '10000': 'S11000'},
            'S2000': {'1000': 'S3000', '2000': 'S4000', '5000': 'S7000', '10000': 'S12000'},
            'S3000': {'1000': 'S4000', '2000': 'S5000', '5000': 'S8000', '10000': 'S13000'},
            'S4000': {'1000': 'S5000', '2000': 'S6000', '5000': 'S9000', '10000': 'S14000'},
            'S5000': {'1000': 'S6000', '2000': 'S7000', '5000': 'S10000', '10000': 'S15000'},
            'S6000': {'1000': 'S7000', '2000': 'S8000', '5000': 'S11000', '10000': 'S16000'},
            'S7000': {'1000': 'S8000', '2000': 'S9000', '5000': 'S12000', '10000': 'S17000'},
            'S8000': {'1000': 'S9000', '2000': 'S10000', '5000': 'S13000', '10000': 'S18000'},
            'S9000': {'1000': 'S10000', '2000': 'S11000', '5000': 'S14000', '10000': 'S19000'},
            'S10000': {'1000': 'S11000', '2000': 'S12000', '5000': 'S15000', '10000': 'S20000'}
        }
        self.current_state = 'S0'
        self.accepting_states = {'S3000', 'S4000', 'S6000'}
        self.path = ['S0']
        self.total_money = 0
        self.drink_prices = {'A': 3000, 'B': 4000, 'C': 6000}
        
    def reset(self):
        self.current_state = 'S0'
        self.path = ['S0']
        self.total_money = 0
        
    def process_input(self, input_value):
        if input_value in {'1000', '2000', '5000', '10000'}:
            money = int(input_value)
            if self.total_money + money > 10000:
                print("Error: Jumlah uang melebihi Rp10.000")
                return False
            
            self.total_money += money
            if self.current_state in self.states and input_value in self.states[self.current_state]:
                self.current_state = self.states[self.current_state][input_value]
                self.path.append(self.current_state)
                return True
            else:
                return False
        elif input_value in {'A', 'B', 'C'}:
            return self.process_purchase(input_value)
        else:
            print("Input tidak valid")
            return False
    
    def process_purchase(self, drink):
        price = self.drink_prices[drink]
        if self.total_money >= price:
            change = self.total_money - price
            print(f"Lintasan DFA: {' → '.join(self.path)}")
            print(f"Minuman {drink} dapat dibeli. Status: ACCEPTED.")
            if change > 0:
                print(f"Kembalian: {change}")
            self.reset()
            return True
        else:
            print(f"Lintasan DFA: {' → '.join(self.path)}")
            print(f"Uang tidak cukup. Status: REJECTED.")
            self.reset()
            return False
    
    def check_drink_availability(self):
        available = []
        if self.total_money >= 3000:
            available.append('A')
        if self.total_money >= 4000:
            available.append('B')
        if self.total_money >= 6000:
            available.append('C')
        
        if available:
            print(f"ON: Minuman {', '.join(available)}")
        return available

def main():
    print('Pilihan Minuman :')
    print('Minuman A : Rp3.000')
    print('Minuman B : Rp4.000')
    print('Minuman C : Rp6.000')
    print(' ')
    vending_machine = VendingMachineDFA()
    valid_inputs = ['1000', '2000', '5000', '10000', 'A', 'B', 'C']
    
    while True:
        user_input = input(f"Masukkan uang atau beli minuman ({', '.join(valid_inputs)}): ").strip().upper()
        
        if user_input == 'EXIT':
            break
            
        if user_input not in valid_inputs:
            print("Input tidak valid. Masukkan pecahan uang atau pilihan minuman.")
            continue
            
        if vending_machine.process_input(user_input):
            if user_input in {'1000', '2000', '5000', '10000'}:
                vending_machine.check_drink_availability()

if __name__ == "__main__":
    main()