from environment import GridWorldEnv

def value_function(env, policy, theta=1e-5):
    """
    Find the value function of policy using an iterative strategy
    
    Returns a dictionary of the expected reward of being in each state
    """
    prev_V = {s: 0.0 for s in env.states}
    
    while True:
        V = {s: 0.0 for s in env.states}
        # loop through all states
        # if terminal skip
        for s in env.states:
            if env.is_terminal(s):
                continue

            # loop through probabilties of next possible states
            for probability, next_state in env.get_transitions(s, policy[s]):
                reward = env.reward(next_state)
                done = env.is_terminal(next_state)
                # multiply by not done because if finished only include reward
                V[s] += probability * (reward + env.gamma * prev_V[next_state] * (not done))

        delta = max([abs(prev_V[s] - V[s]) for s in env.states])
        if delta < theta:
            break

        prev_V = V.copy()
    return V
            

# Use the value function
def policy_improvement(env, V):
    """
    Using the value function, greedily choose the optimal action in each state.
    This will improve upon the previous policy.
    
    Returns a dictionary containing a policy table.
    """
    Q = {s: {} for s in env.states}
    new_policy = {}

    for s in env.states:
        if env.is_terminal(s):
            continue
        best_action = None
        best_value = float("-INF")
        for a in env.actions:
            Q_val = 0
            for probability, next_state in env.get_transitions(s, a):
                reward = env.reward(next_state)
                done = env.is_terminal(next_state)
                Q_val += probability * (reward + env.gamma * 
                                            V[next_state] * (not done))
            Q[s][a] = Q_val
            if Q_val > best_value:
                best_value = Q_val
                best_action = a
        new_policy[s] = best_action
    return new_policy
            
def policy_iteration(env, initial_policy_table):
    current_policy_table = initial_policy_table.copy()

    while True:
        
        V = value_function(env, initial_policy_table)

        new_policy = policy_improvement(env, V)

        current_policy_table = new_policy

        if current_policy_table == new_policy:
            break
    return new_policy



test_policy_table = {
    0: "RIGHT",
    1: "RIGHT",
    2: "DOWN",
    3: "LEFT",

    4: "DOWN",
    6: "DOWN",

    8: "RIGHT",
    9: "DOWN",
    10: "DOWN",

    13: "RIGHT",
    14: "RIGHT"
}

env = GridWorldEnv()
nathans_policy = value_function(env, test_policy_table)
optimal_policy = policy_iteration(env, test_policy_table)
optimal_V = value_function(env, optimal_policy)
print(f"Nathan's V: : {nathans_policy}")
print(f"Optimal policy: {optimal_policy}")
print(f"Optimal V: {optimal_V}")