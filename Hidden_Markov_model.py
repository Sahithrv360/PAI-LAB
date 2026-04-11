states = ['Rainy','Sunny']

observations = ['walk','shop','clean']

ini_prob = {
    'Rainy' : 0.6,
    'Sunny' : 0.4
}

transition_probabilities = {
    'Rainy' : {
        'Rainy' : 0.7,
        'Sunny' : 0.3
    },
    'Sunny' :{
        'Rainy' : 0.4,
        'Sunny' : 0.6
    }
}

emission_probabilities = {
    'Rainy' : {
        'walk' : 0.1,
        'shop' : 0.4,
        'clean' :0.5
    },
    'Sunny' :{
        'walk' : 0.6,
        'shop' : 0.3,
        'clean' :0.1
    }
}

observation_sequence = ['walk','shop','clean']

def forward_algorithm(states,observations,ini_prob,transition_probabilities,emission_probabilities,observation_sequence):
    forward = []
    f0 = {}
    for state in states:
        f0[state] = ini_prob[state]*emission_probabilities[state][observation_sequence[0]]
    forward.append(f0)
    print(f0)
    for t in range(1,len(observation_sequence)):
        ft = {}
        for current_state in states:
            prob = 0
            for previous_state in states:
                prob += forward[t-1][previous_state] * transition_probabilities[previous_state][current_state]
            ft[current_state] = prob * emission_probabilities[current_state][observation_sequence[t]]
        forward.append(ft)
    for t, fwd in enumerate(forward):
        print(f"\nTime step {t}:")
        for state, value in fwd.items():
            print(f"{state} : {value}")
    total_probability = sum(forward[-1][state] for state in states)
    return total_probability
result = forward_algorithm(states,observations,ini_prob,transition_probabilities,emission_probabilities,
                           observation_sequence)

print('Total Probability for the given sequence is : ',result)