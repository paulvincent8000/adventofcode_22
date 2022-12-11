######################
## Imports

import numpy
import pandas

######################
## Functions



######################
## Part 1

def part_1(input_file: str) :

  # Ingest file into dataframe
  df_input = pandas.read_csv(input_file, header=None, names=["instruction","value"], sep=" ")

  # Add instruction ID
  df_input["instruction_id"] = df_input.index
  
  # Investigate dataframe
  # print(df_input)
  # df_input.head(15)
  
  # Duplicate rows for addx
  df_input_1 = df_input.copy()
  df_input_1["instruction_sub_id"] = 1
  df_input_2 = df_input[df_input["instruction"] == "addx"].copy()
  df_input_2["instruction_sub_id"] = 2
  df_instructions = pandas.concat([df_input_1, df_input_2]).sort_index()

  # Sort and reindex
  df_instructions.sort_values(["instruction_id", "instruction_sub_id"], inplace=True)
  df_instructions.reset_index(drop=False, inplace=True)

  # Determine cycle and cycle value
  df_instructions["cycle"] = df_instructions.index + 2
  df_instructions["cycle_value"] = numpy.where(df_instructions["instruction_sub_id"] == 2, df_instructions["value"], 0)

  # X and signal strength for current value
  df_instructions["X"] =  df_instructions["cycle_value"].cumsum() + 1
  df_instructions["signal_strength"] =  numpy.where((df_instructions["cycle"]+20)%40 == 0, df_instructions["X"] * df_instructions["cycle"], 0)
  print(df_instructions.iloc[0:20])
  return

  # Investigate dataframe
  # print(df_instructions)
  # df_instructions.head(21)

  print(df_instructions[df_instructions["signal_strength"] != 0])

  total_signal_strength = df_instructions["signal_strength"].sum()

  return total_signal_strength

part_1(input_file="input.txt")
#part_1(input_file="10/input.txt")
