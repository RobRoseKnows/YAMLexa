#!bin/python3
# I used this to mass import things into the Skill Builder.
import json
import sys


def foo():
    if(len(sys.argv) >= 1):
        input_name = sys.argv[1]
    else:
        return

    try:
        output_name = "{}.json".format(input_name)

        arr = []

        with open(input_name) as fileIn:
            arr = fileIn.readlines()
      
        arrStrip = []

        for line in arr:
            arrStrip.append(construct_value(line.rstrip('\n')))

        d = {
                "name": input_name,
                "values": arrStrip
            }

        fileOut = open(output_name, 'w')
        fileOut.write(json.dumps(d, indent=4))
        fileOut.close()

    except:
        e = sys.exc_info()[0]
        print(e)

    return
    
def construct_value(person_name):
    return { "name": { "value": person_name}}


def main():
    foo()

main()

