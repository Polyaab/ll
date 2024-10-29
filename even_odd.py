   def is_even(num):
       return num % 2 == 0

   if __name__ == "__main__":
       number = int(input("Введите число: "))
       if is_even(number):
           print(f"{number} - четное")
       else:
           print(f"{number} - нечетное")
   
