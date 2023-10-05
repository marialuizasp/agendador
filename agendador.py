import schedule
import time as tm
from datetime import time
from schedule import repeat, every


@repeat(every().second)
def tarefa():
    print("escreva aqui")

# schedule.every(5).seconds.do(tarefa)
# schedule.every().hour.at(":59").do(tarefa)
# schedule.every().hour.until(time(14, 22, 10)).do(tarefa)



while True: 
    schedule.run_pending()
    tm.sleep(1)