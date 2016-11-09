# A list to hold all of the election results
# The format should be:
# 1. State abbreviation
# 2. ':'
# 3. List of results (separated by ','):
#   1. Candidate name
#   2. '='
#   3. Vote count (integer)
RESULTS = [
    'CA:CLINTON=80,TRUMP=20',
    'FL:CLINTON=48,TRUMP=49',
    'TX:CLINTON=30,TRUMP=70'
]


def parse_results_by_state(results):
    '''
    Takes a list of string results, and returns a dictionary that looks
    like:

    {
        'STATE_NAME': {
            'CANDIDATE_NAME_1': NUM_VOTES_1,
            'CANDIDATE_NAME_2': NUM_VOTES_2,
            ...
        },
        ...
    }


    '''
    results_by_state = {}
    for result in results:
        # TODO: Actually parse out results into my dictionary
        pass
    return results_by_state


def main():
    '''
    Prints out which states each candidate won
    '''
    results_by_state = parse_results_by_state(RESULTS)
    for state, results in results_by_state.items():
        if results['CLINTON'] > results['TRUMP']:
            print('Hillary Clinton takes %s' % state)
        elif results['CLINTON'] < results['TRUMP']:
            print('Donald Trump takes %s' % state)
        else:
            print('%s is too close to call' % state)


if __name__ == '__main__':
    main()
