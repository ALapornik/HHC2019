import sys
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timezone

keyLength = 8  # DES
inputFileName = "ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf.enc"
outputFileName = "Decoded.pdf"
startTime = int(datetime(2019,12,6,19,0,0,tzinfo=timezone.utc).timestamp())
endTime = int(datetime(2019,12,6,21,0,0,tzinfo=timezone.utc).timestamp())

def generateKey(seed):
    """
    Generates a DES encryption key

    Args:
        seed: A seed value based on UNIX Epoch time

    Returns:
        A string containing the DES encryption key
    """
    key = ''
    for x in range(0,keyLength):
        seed *= 0x343FD
        seed += 0x269EC3
        key += '{:02x}'.format((seed >> 0x10 & 0x7fff) & 0xff)        
    return key

def isPDF(decrypted):
    if b'PDF-1' in decrypted:
        return True
    else:
        return False

def openFile(inputFileName):
    with open(inputFileName, 'rb') as f:
        data = f.read()
        f.close()
    return data

def writeFile(data, outputFileName):
    with open(outputFileName, 'wb') as f:
        f.write(data)
        f.close()

def update_progress(progress):
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(progress * 50), progress*100), end="", flush=True)

def decryptDES(key, data, outputFileName):
    key0 = DES.new(bytes.fromhex(key),DES.MODE_CBC,iv=b'\0\0\0\0\0\0\0\0')
    
    try:
        decrypted = unpad(key0.decrypt(data), 8)
        if isPDF(decrypted):            
            writeFile(decrypted, outputFileName)
            return True # decrypted
        else:
            return False # not decrypted
    except:
        return False # not decrypted

def main():
    print("The application will now iterate over each of the possible seed values until the file is decrypted.")
    data = openFile(inputFileName)
    for seed in range(startTime,endTime):
        progress = (seed - startTime) / (endTime - startTime)
        update_progress(progress)
        
        key = generateKey(seed)
        if (decryptDES(key, data, outputFileName)):
            print(f"\nDecrypted file with key: {key}")
            sys.exit(0)  # file decrypted, exit normally

if __name__ == "__main__":
    main()