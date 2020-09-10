import random
def main():
  drolls = 2
  dsum = 0
  for i in range (0,drolls):
    roll = random.randint(1,6)
    print(f"You rolled a {roll}")
    dsum += roll

if __name__== "__main__":
  main()
