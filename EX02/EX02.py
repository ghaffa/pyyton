def encode(message, shift):
    pikkus = int(len(message))
    rida = []

    if shift < 0:
        return -1        
    else:
        while shift >= 26:
            shift = shift - 26

        for i in range(0,pikkus):
            taht = ord(message[i])
            if 65 <= taht <= 90:
                taht = taht + shift
                if taht > 90:
                    taht = ord(message[i])
                    shiftk = (90 - taht)
                    shiftx = shift - shiftk
                    taht = 64 + shiftx
                    taht = chr(taht)
                    rida.insert(i, taht)
                else:
                    taht = chr(taht)
                    rida.insert(i, taht)
            elif 97 <= taht <= 122:
                taht = taht + shift
                if taht > 122:
                    taht = ord(message[i])
                    shiftk = (122 - taht)
                    shiftx = shift - shiftk
                    taht = 96 + shiftx
                    taht = chr(taht)
                    rida.insert(i, taht)
                else:
                    taht = chr(taht)
                    rida.insert(i, taht)
            else:
                taht = chr(taht)
                rida.insert(i, taht)
                
    encoded_message = "".join(rida)
    
    return encoded_message

def crack(encoded_message, phrase):
    pikkusyks = int(len(encoded_message))
    pikkuskaks = int(len(phrase))
    ridayks = []
    rida = []
    ridakolm = []
    shift = 0
    fraas=["1", "2", "3"]

    for i in range(pikkuskaks):
        taht = phrase[i]
        rida.insert(i, taht)
        fraas = "".join(rida)
        
    for i in range(pikkusyks):
        taht = encoded_message[i]
        ridayks.insert(i, taht)
        sonum = "".join(ridayks)

    if pikkusyks == 0:
        return None

    if phrase in encoded_message:
        if pikkuskaks == 0:
            decoded_message = encoded_message + " (fraasis ei olnud ühtegi tähte)"
            print(decoded_message)
            return decoded_message
        else:
            decoded_message = encoded_message + " (shift: 0)"
            print(decoded_message)
            return decoded_message
    elif pikkuskaks > pikkusyks:
        return None
    elif pikkusyks >= pikkuskaks:
        while fraas[0:pikkuskaks] not in encoded_message:
            shift = shift + 1
            for i in range(pikkuskaks):
                taht = ord(phrase[i])
                if 65 <= taht <= 90:
                    taht = taht + shift
                    if taht > 90:
                        taht = ord(phrase[i])
                        shiftk = (90 - taht)
                        shiftx = shift - shiftk
                        taht = 64 + shiftx
                        taht = chr(taht)
                        rida.insert(i, taht)
                    else:
                        taht = chr(taht)
                        rida.insert(i, taht)
                elif 97 <= taht <= 122:
                    taht = taht + shift
                    if taht > 122:
                        taht = ord(phrase[i])
                        shiftk = (122 - taht)
                        shiftx = shift - shiftk
                        taht = 96 + shiftx
                        taht = chr(taht)
                        rida.insert(i, taht)
                    else:
                        taht = chr(taht)
                        rida.insert(i, taht)
                else:
                    taht = chr(taht)
                    rida.insert(i, taht)
            if shift >= 26:
                return -1
            fraas = "".join(rida)
        if fraas[0:pikkuskaks] in encoded_message:
            shift = str(shift)
            ridakolm = list(set(rida).intersection(set(ridayks)))
            print(ridakolm)
            print(len(ridakolm))
            print(ridayks)
            sonum.replace(      
            decoded_message = fraas[0:pikkuskaks] + " (shift: " + shift + ")"
            print(decoded_message)
            return decoded_message
        else:
            return None

            
crack("dc", "b")
    
