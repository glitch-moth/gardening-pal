import json

def generate_bed(veg, vegs):
    extended_foes = set([i for lis in [vegs[friend]['foes'] for friend in vegs[veg]['friends'] if friend in vegs] for i in lis])
    return (veg, [friend for friend in vegs[veg]['friends'] if friend in vegs and not friend in extended_foes])

def generate_bed_depth_two(veg, vegs):
    #beds = {}
    #for veg_2 in vegs[veg]['friends']:

if __name__=='__main__':
    with open("vegetables.json", 'r') as file:
        data = json.load(file)['vegetables']
        beds = [generate_bed(i, data) for i in data]
        beds_dict = {}
        for b in beds:
            beds_dict[b[0]] = b[1]
        with open("single_depth_beds.json", 'w') as out:
            json.dump(beds_dict, out, sort_keys=True, indent=2)
