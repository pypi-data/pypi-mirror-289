# cliquest/cliquest/cli.py

from cdlib import algorithms
def estimate_cli(net):
    coms = algorithms.hierarchical_link_community(net)
    community = coms.communities 

    return community