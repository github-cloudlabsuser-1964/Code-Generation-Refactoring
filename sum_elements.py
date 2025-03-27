MAX = 100

def calculate_sum(arr):
   return sum(arr)

def get_integer_input(prompt, error_message="Invalid input. Please enter a valid integer."):
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         print(error_message)

def main():
   try:
      n = get_integer_input("Enter the number of elements (1-100): ")
      if not 1 <= n <= MAX:
         print("Invalid input. Please provide a number ranging from 1 to 100.")
         return

      print(f"Enter {n} integers:")
      arr = [get_integer_input(f"Element {_ + 1}: ") for _ in range(n)]

      total = calculate_sum(arr)
      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")

if __name__ == "__main__":
   main()
