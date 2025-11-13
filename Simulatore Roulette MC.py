import numpy as np
import matplotlib.pyplot as plt

# STRATEGIA D'ALEMBERT
def siml(days, start_bal=10000, win_rate=0.486,base_stake=0.05,avg_pay=1):
    balance = start_bal
    stake_unit = balance * base_stake
    stake = stake_unit
    #balances = [] #lista per tracciare i bilanci nel tempo (serve per plottare la singola simulazione)

    for _ in range(days):

        if stake <= 0:  
            stake = stake_unit

        if np.random.rand() < win_rate: 
            balance += stake * avg_pay
            stake -= stake_unit
        else:
            balance -= stake
            stake += stake_unit
        
        if balance <= 0: 
            break
        #balances.append(balance)
    
    return balance

#SINGOLA SIMULAZIONE + PLOT
#days = 365
#balances_over_time = siml(days)
#plt.figure(figsize=(10, 6))
#plt.plot(balances_over_time, label="Balance over time", color='blue', linewidth=12)
#plt.title(f"Balance evolution in {days} days", fontsize=14)
#plt.xlabel("Days", fontsize=12)
#plt.ylabel("Balance", fontsize=12)
#plt.grid(True)
#plt.legend()
#plt.show()

#SIMULAZIONE MONTECARLO

def MC_sim(num, days, start_balance=10000, win_rate=0.486): 
    final_balances = []
    for _ in range(num):
        final_bal = siml(days, start_balance, win_rate)
        final_balances.append(final_bal)
    
    return final_balances

# days può anche essere visto come il numero di scommesse in quanto la simulazione è discreta e non continua
num_sim = 1000
days = 100
final_bals = MC_sim(num_sim, days)
avg_bal = np.mean(final_bals)
print(f"Avg final account balance after {days} spins: {avg_bal:.2f}")

plt.figure(figsize=(10,6))
plt.hist(final_bals,bins=50,edgecolor='black',alpha=0.7)
plt.axvline(avg_bal,color="green",linestyle='--',label=f"Mean: {avg_bal:.2f}")
plt.title(f"Distr of final account balances after {days} spins ({num_sim} simulations)", fontsize=16)
plt.xlabel("Final account balance (euros)", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.legend()
plt.show()


