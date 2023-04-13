from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
def caesar(start_text,shift_amount,cipher_direction):
  end_text = ""
  
  if cipher_direction == "decode":
      shift_amount *= -1
  
  
  for letter in start_text:
    if letter not in alphabet:
      end_text += letter
    elif letter in alphabet:
      
      index = alphabet.index(letter)
      encrypted_index = index + shift_amount  
      if encrypted_index > 25:
          encrypted_index = (index + shift_amount) % 26
      if encrypted_index < -26:
         encrypted_index = (index + shift_amount) % 26
      end_text += alphabet[encrypted_index]   
  print(f"The {cipher_direction} text is {end_text}")
  
print(logo)


while should_continue == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)

  cont = input("If you want to continue press 'Y', else press 'N'.\n ").lower()
  
  if cont == "n":
    should_continue = False



  

  

          
  
  