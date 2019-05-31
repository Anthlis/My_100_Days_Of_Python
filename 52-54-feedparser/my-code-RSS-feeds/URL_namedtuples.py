import collections

Measurement = collections.namedtuple(
    'Measurement',
    'temp, lat, long, quality')

def get_meas():
    data = [
        Measurement(11.2, 19.2, 11.1, 'hard'),
        Measurement(22.5, 44.234, 19.02, 'strong'),
        Measurement(13.5, 2, 3, 'soft'),
        ]
    return data

def main():
    for i, idx in enumerate(get_meas(), start=1):
        print(f"{i}. temp={idx.temp}, lat={idx.lat}, long={idx.long} and quality={idx.quality}")
        
if __name__ == '__main__':
    main()