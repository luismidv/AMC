def menu_starter():
    option = input(f"What algorithms will you run: \n"
          f"    1. Exhaustive. \n"
          f"    2. Bidirectiontal. \n"
          f"    3. Exhaustive with pode strategy. \n"
          f"    4. Bidirectional with pode strategy.\n"
          f"Choose your option: ")

    match option:
       case "1":
             import algorithms
       case "2":
             import bidrectional
       case "3":
             import bidirectionalpode
       case "4":
             import exhaustivepode


menu_starter()