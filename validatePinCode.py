def validate_pin(pin):
    if((len(pin)==4 or (len(pin)==6)) and pin.find('-')==-1):
        if(pin.isdigit() == True):
            if(int(pin)>=0):
                return True
            else: 
                return False
        else: 
            return False;
    else:
        return False;
