#!/usr/bin/env python3

sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
flat  = ["C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭", "A", "B♭", "B"]

print("Scale\t\tSa\tRe\tGa\tMa\tPa\tDha\tNi\tSa\n")

for starting_note in range(len(sharp)):
    print(sharp[starting_note], end = "\t\t")
    for i in range(8):
        match i:
            case 0:
                print(sharp[(starting_note + 0) % 12], end = '\t')
            case 1:
                print(sharp[(starting_note + 2) % 12], end = '\t')
            case 2:
                print(sharp[(starting_note + 4) % 12], end = '\t')
            case 3:
                print(sharp[(starting_note + 5) % 12], end = '\t')
            case 4:
                print(sharp[(starting_note + 7) % 12], end = '\t')
            case 5:
                print(sharp[(starting_note + 9) % 12], end = '\t')
            case 6:
                print(sharp[(starting_note + 11) % 12], end = '\t')
            case 7:
                print(sharp[(starting_note + 0) % 12])

print("\nFlat Notes:\n")

print("Scale\t\tSa\tRe\tGa\tMa\tPa\tDha\tNi\tSa\n")

for starting_note in range(len(flat)):
    print(flat[starting_note], end = "\t\t")
    for i in range(8):
        match i:
            case 0:
                print(flat[(starting_note + 0) % 12], end = '\t')
            case 1:
                print(flat[(starting_note + 2) % 12], end = '\t')
            case 2:
                print(flat[(starting_note + 4) % 12], end = '\t')
            case 3:
                print(flat[(starting_note + 5) % 12], end = '\t')
            case 4:
                print(flat[(starting_note + 7) % 12], end = '\t')
            case 5:
                print(flat[(starting_note + 9) % 12], end = '\t')
            case 6:
                print(flat[(starting_note + 11) % 12], end = '\t')
            case 7:
                print(flat[(starting_note + 0) % 12])
