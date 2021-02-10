print("This is a converter which changes celcius to farenhiet and vise versa")
celcius_farenheit = input(" Do you want a) celcius to farenheit or  b) farenheit to celcius:  ")
def cel_to_far():
    if celcius_farenheit == "a" or celcius_farenheit == "a)" or celcius_farenheit == " a) celcius to farenheit" or celcius_farenheit == " a celcius to farenheit" or celcius_farenheit == " celcius to farenheit":
        celcius = float(input("Enter your degrees in celcius:  "))
        calculations = str((celcius * 1.8) + 32)
        print("The answer in farenhiet is ",calculations)
        #calculations = (celcius * 1.8) + 32
        #print("The answer in farenhiet is ",str(celcius))

    elif celcius_farenheit == "b" or celcius_farenheit == "b)" or celcius_farenheit == " b) farenheit to celcius" or celcius_farenheit == " a farenheit to celcius" or celcius_farenheit == "farenheit to celcius":
        farenhite = float(input("Enter your ferenhite:  "))
        yahoo = str((farenhite - 32) * 0.555555556)
        print("The answer in celcius is ", yahoo)
    else:
        print("I did not understand you. Please run program again.")
cel_to_far()