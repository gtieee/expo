import csv

def main():
    with open('raw.csv', encoding='utf-8', newline='') as rawFile:
        rows = []
        reader = csv.reader(rawFile)
        for row in reader:
            output = ''
            if (row[14] == 'yes'):
                output += 'Design, '
            if (row[15] == 'yes'):
                output += 'Body, '
            if (row[16] == 'yes'):
                output += 'Circuitry, '
            if (row[17] == 'yes'):
                output += 'Software, '
            print(output[:len(output)-2])

main()