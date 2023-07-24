import os
import webbrowser
import time
import random
import datetime

def menu():
   print("""\n==== MENU PRINCIPAL ====
   [1] Dar comida 
   [2] Brincar
   [3] Dormir
   [4] Ir lá fora
   [5] Mostrar estatísticas 
   [6] Ir ao mercado
   [7] Navegar na internet
   [0] Sair do jogo""")

   user_choice = int(input("\nSua opção: "))
   return user_choice

def randomDecrease():
   return random.randint(1, 20) 

def randomIncrease():
   return random.randint(0, 10)

def clr():
   os.system("clear")

def waterThePlants():
   plants = [True, False]
   return random.choice(plants)
   

clr()
print("Tou: Olá eu sou seu bichinho virtual, meu nome é TOU!")
input("Press ENTER -> ")

plant_watered = False

level = 0
level_bar = 0

refrigerator = []

statistics = []
with open("status.txt", "r") as statusis:
   numbers = statusis.readlines()
   for n in numbers:
      statistics.append(n.replace("\n", ""))

hungry = int(statistics[1])
happiness = int(statistics[2])
sleepy = int(statistics[3])
health = int(statistics[4])
money = int(statistics[5])
is_night = statistics[6]


# level == statistics[0]
# hungry == statistics[1]
# happiness == statistics[2]
# sleepy == statistics[3]
# health == statistics[4]
# money == statistics[5]
# is_night == statistics[6]

# Main loop
while True:
 
   value = menu()
   
   if value == 0:
      break

   elif value == 1:
      clr()
      if hungry > 60:
         print("Tou: Não estou com fome!!")

      elif hungry <= 60:
         if len(refrigerator) == 0:
            print("Tou: A geladeira está vazia ._.")

         else:
            for n in range(len(refrigerator)):
               print(f"[{n}] - {refrigerator[n]}")
            print("[99] - Sair da geladeira")
            
            food = int(input("Sua opção: "))
            if food == 99:
               continue
      
            try:         
               print("Você escolheu: ", refrigerator[food])
               if refrigerator[food] == "Dipirona em comprimidos":
                  print("Tou: Eca! Remédio não!")
                  health = 100
                  refrigerator.pop(food)

               else:
                  refrigerator.pop(food)
                  print("Tou: Muito bom!")
                  hungry = 100
                  level_bar += 0.1

            except:
               print("Não há essa comida na geladeira")

   elif value == 2:
      clr()
      if happiness > 70:
         print("Tou: Não quero brincar agora!")
      
      elif happiness <= 70:

         webbrowser.open_new_tab("https://emupedia.net/beta/emuos/")
         try:
            while True:
               win_money = randomIncrease()
               clr()
               print("Pressione Ctrl + c quando quiser parar!")
               print(f"Você ganhou: R${win_money:.2f}")
               time.sleep(5)
               money += win_money
         except:
            print()      
         
         print("Tou: Que divertido!")
         happiness += randomIncrease()
         level_bar += 0.1

   elif value == 3:
      clr()
      if sleepy > 40:
         print("Tou: Não estou com sono!!")
      
      elif sleepy <= 40:
         
         sleep_time = random.randint(5, 30)
         print("Tou: Eu vou dormir, mas eu não estou com sono!")
         print(f"Volto daqui {sleep_time} segundos!")
         time.sleep(sleep_time)
         print("ACORDEI!!")
         
         sleepy += randomIncrease()

   elif value == 4:
      clr()
     
      if statistics[6] == "True":
         print("Tou: Não vou sair lá fora! Está escuro!")
      
      elif statistics[6] == "False":
         print("Tou: Que dia lindo para ir lá fora!")

         while True:

            if waterThePlants() and plant_watered == False:
               time.sleep(2)
               print("Tou: Ó não, as plantas estão secas!")
               water = str(input("Deseja regar as plantas? (S/N): ")).lower()
               if water == "s":
                  print("Que legal, você ganhou 50 centavos por ter regado a planta!")
                  plant_watered = True
                  money += 0.5
               
               else:
                  print("Ok")
                  print("Tou: Olha meu pet ali!")
                  pet = str(input("Deseja fazer carinho nele? (S/N): ")).lower()
                  if pet == "s":
                     print("Tou: Que fofinho!")
                     happiness += 10

                  back_home = str(input("Deseja voltar para casa? (S/N): ")).lower()
                  if back_home == "s":
                     plant_watered = False
                     break
                  else:
                     continue

            elif waterThePlants() == False:
               print("Tou: Olha meu pet ali!")
               pet = str(input("Deseja fazer carinho nele? (S/N): ")).lower()
               if pet == "s":
                  print("Tou: Que fofinho!")
                  happiness += 10
            
               back_home = str(input("Deseja voltar para casa? (S/N): ")).lower()
               if back_home == "s":
                  plant_watered = False
                  break
               else:
                  continue
         level_bar += 0.1

   elif value == 5:
      clr()
      with open("status.txt", "r") as archive:
         status = archive.readlines()
         
         for n in status:
            statistics.append(n.replace("\n", "")) 

         if len(statistics) == 0:
            print("Nenhuma estatística salva ainda, recarregue o jogo para acessá-la \n(Dica: no menu principal, pressione 0)")

         else:
            print("Nível: \t\t", statistics[0], "%")
            print("Fome: \t\t", statistics[1], "%")
            print("Felicidade: \t", statistics[2], "%")
            print("Sono: \t\t", statistics[3], "%")
            print("Saúde: \t\t", statistics[4], "%")
            print(f"Dinheiro: \t R${int(statistics[5]):.2f}")

   elif value == 6:
      products = ["Macarrão", "Feijão tropeiro", "Salpicão", "Feijoada", "Galinhada", "Pão de queijo", "Dipirona em comprimidos"]
      prices = [5, 10, 10, 12, 9, 5, 17]
      while True:
         clr()
         print("Sua carteira: ", money)
         # print to show the options
         print("[1] Macarrão - R$5,00\n[2] Feijão tropeiro - R$10,00\n[3] Salpicão - R$10,00\n[4] Feijoada - R$12,00\n[5] Galinhada - R$9,00\n[6] Pão de queijo - R$5,00\n[7] Dipirona em comprimidos - R$17,00 \n[0] Sair do mercado")
         
         choose = int(input("Sua opção: "))
         
         if choose == 0:
            clr()
            break
         else:
            if money <= 0:
               print("Você não possui dinheiro suficiente!")
               break
            else:
               choose -= 1
               print("Você escolheu: ", products[choose])
               refrigerator.append(products[choose])
               money -= prices[choose]
               print("Sua carteira atual: ", money)

   elif value == 7:
      webbrowser.open_new_tab("https://www.youtube.com")

   if level_bar == 1:
      level += 1
      level_bar = 0
      clr()
      print("O Tou subiu de nivel!")
      input("Pressione ENTER para continuar ->")

if is_night == "True":
   is_night = "False"

elif is_night == "False":
   is_night = "True"

hungry -= randomDecrease()
happiness -= randomDecrease()
sleepy -= randomDecrease()
health -= randomDecrease()


with open("status.txt", "+w") as arquivo:
   arquivo.write(f"{level}\n")
   arquivo.write(f"{hungry}\n")
   arquivo.write(f"{happiness}\n")
   arquivo.write(f"{sleepy}\n")
   arquivo.write(f"{health}\n")
   arquivo.write(f"{money}\n")
   arquivo.write(f"{is_night}\n")