#!/usr/bin/env python

import sys
import cPickle

import numpy as np
import matplotlib.pyplot as plt
from scipy import spatial
import networkx as nx

import const

def main():
    GRID_SIZE = 2.5 # in meters
    # Target location and radius
    # test_point_cloud.dat
    LOC = (447772, 4424300)
    R = 500

    # test_point_cloud1.dat
    #LOC = (446458, 4422150)
    #R = 500

    # San Francisco
    #LOC = (551281, 4180430) 
    #R = 500

    if len(sys.argv) != 3:
        print "ERROR! Correct usage is:"
        print "\tpython sample_hog_feature.py [sample_point_cloud.dat] [sample_direction.dat]"
        return

    with open(sys.argv[1], 'rb') as fin:
        sample_point_cloud = cPickle.load(fin)
    
    with open(sys.argv[2], 'rb') as fin:
        sample_directions = cPickle.load(fin)

    sample_kdtree = spatial.cKDTree(sample_point_cloud.locations)

    pt_idx = 17
    search_R = 200
    nearby_idxs = sample_kdtree.query_ball_point(sample_point_cloud.locations[pt_idx], search_R)


    fig = plt.figure(figsize=const.figsize)
    ax = fig.add_subplot(121, aspect='equal')
    ax.plot(sample_point_cloud.locations[:,0],
            sample_point_cloud.locations[:,1], '.', color='gray')
    ax.plot(sample_point_cloud.locations[true_nearby_idxs,0],
            sample_point_cloud.locations[true_nearby_idxs,1],'.b')
    ax.plot(sample_point_cloud.locations[pt_idx,0],
            sample_point_cloud.locations[pt_idx,1], 'or')
    ax = fig.add_subplot(122, aspect='equal')
    ax.hist(dist_list, bins=N_bins, normed=1)
    plt.show()

    return

    N_pt = 100
    sampling_rate = 0.5
    N_sample = int(N_pt*sampling_rate)**2

    x = np.linspace(-np.pi, np.pi, N_pt)
    y = 1.5*(np.random.rand(N_pt) - 0.5)
    #y1 = np.linspace(0, 1, N_pt)
    #x1 = 0.1*np.random.rand(N_pt)
    #x = np.append(x0, x1)
    #y = np.append(y0, y1)

    dist_list = []
    
    for i in range(0, N_sample):
        pt_idx0 = np.random.randint(0, N_pt)
        pt_idx1 = np.random.randint(0, N_pt)
        vec = np.array([x[pt_idx1], y[pt_idx1]]) - np.array([x[pt_idx0], y[pt_idx0]])
        dist_list.append(np.linalg.norm(vec))
    dist_list = np.array(dist_list) / max(dist_list)

    fig = plt.figure(figsize=const.figsize)
    ax = fig.add_subplot(121, aspect='equal')
    ax.plot(x, y, '.')
    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax = fig.add_subplot(122)
    ax.hist(dist_list, bins=16, normed=1)
    plt.show()

if __name__ == "__main__":
    sys.exit(main())
