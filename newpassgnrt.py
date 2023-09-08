import random
import array
import pandas as pd
from datetime import datetime

def passgenerator(length=30):
    # maximum length of password needed
    # this can be changed to suit your password length
    MAX_LEN = length

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '*', '{', '_', '~', '^',
            '+', '=', '?']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    COMBINED_LIST_1 = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rand_digit + rand_symbol + rand_upper + rand_lower
    print(type(temp_pass))


    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 6):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        #(MAX_LEN-6) will generate 24 caharachters
        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        #random.shuffle(temp_pass_list)
    tmp_pass = ""
    #To generate two more charachters which are not symbols to avaoid special charachters at the end
    for y in range(2):
        tmp_pass = tmp_pass + random.choice(COMBINED_LIST_1)
        # Generated two random charachter not symbols
        tmp_pass_list = array.array('u',tmp_pass)
        # Coverting to array list
    print("temp",temp_pass_list,len(temp_pass_list))
    print("tmp",tmp_pass_list)
    final_temp_pass_list = temp_pass_list + tmp_pass_list
    # Final password after adding two arrays
    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in final_temp_pass_list:
            password = password + x
            
    # print out password
    print(password,"printing length as well",len(password))
    return password

passgenerator(30)

def read_csv():
  # Date time in proper fomat to append to output file name
  dt = datetime.now().strftime("%Y-%m-%d-%H%M%S")
  str_current_datetime = str(dt)
  print("Current datetime is "+str_current_datetime)
  # Reading excel file
  df = pd.read_excel("/Users/pratik.yadav/Downloads/CRED_CUST.xlsx",sheet_name='cred')
  print(df)
  # Iterating through excel
  for index, row in df.iterrows():
    #print(row["user"], row["password"])
    #if row["password"] == string.empty:
    #if "".__eq__(row["password"]):
    # Checking for emty password filelds
    if not row["value"] or pd.isnull(row["value"]):
      print("printing old values",row["name"],row["value"])
      #a = []
      pass1 = passgenerator(30)
      #a.append(pass1)
      # After generating password checking if it is not already there in column if it is there againg generating random passowrd
      while (row.isin(list(pass1))).any():
        pass1 = passgenerator(30)
      # Fillimg the empty password fields
      df.iloc[index,2] = pass1
      print(row["name"],row["value"])
    else:
      print("CSV is already updated....")
  print(df)
  # Creating output Excel with current timestamp
  df.to_excel("CRED_CUST_output"+str_current_datetime+".xlsx",index=False,header=True)

read_csv()

