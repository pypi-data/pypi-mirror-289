import numpy as np
import pandas as pd
import igraph
import leidenalg as la


def pearsonr_ixs(x, ixs):
    """
    Calculate Pearson correlation between time series in x for indexes in ixs.

    Only the correlations between indexes in ixs is calculated and returned.
    Order of correlations returned matches order of indexes supplied.

    Parameters
    ----------
    x : NumPy Array
        Time series of page views.
    ixs : NumPy Array
        Array of indexes where edge is present and correlation is calculated.

    Returns
    -------
    NumPy Array
        Pearson correlation between time series at index combinations (1D).

    """
    xm = (x - x.mean(axis=0))
    xmn = xm/np.sqrt((xm*xm).sum(axis=0))

    return (xmn[:, ixs][:, :, 0] * xmn[:, ixs][:, :, 1]).sum(axis=0)

def rolling_sim_ixs(timeseries, adj, w, sim=pearsonr_ixs, corr_mode='centered'):
    """
    Calculate rolling general correlation between time series for indexes in ixs.

    Only the correlations between indexes in ixs is calculated and returned.
    Order of correlations returned at each time step matches order of indexes
    supplied.

    Parameters
    ----------
    timeseries : NumPy Array
        Time series of page views for articles in network.
    adj : NumPy Array
        (Temporal) Adjacency matrix of network. If temporal, dimensions should be
        (n_timesteps, n_nodes, n_nodes)
    w : int
        Rolling window size
    sim : Function
        Pairwise similarity function
    corr_mode : str, 'centered' or 'backward', optional
        Whether to base correlations on a centered window, or one that looks back.
        The default is 'centered'.

    Returns
    -------
    NumPy Array
        Rolling (7 day) Pearson correlation between time series at index
        combinations at each time step (2D). An edgelist for each time step.
    ixs : NumPy Array
        Array of indexes where edge is present and correlation is calculated.

    """
    if len(adj.shape) == 3:
        cmd = {'centered': w//2, 'backward': w-1}
        ixs = [np.argwhere(adj[n+cmd[corr_mode]]) for n in
               range(adj.shape[0]-(w-1))]
        return [sim(timeseries[x:x+w], ixs[x])
                     for x in range(0, len(timeseries)-(w-1))], ixs
    else:
        ixs = np.argwhere(adj)
        return np.array([sim(timeseries[x:x+w], ixs)
                     for x in range(0, len(timeseries)-(w-1))]), ixs


def rolling_sims_to_igraph(el, ixs, artixdict):
    """
    Convert rolling similarity edge scores to a temporal network. In this case
    a list of igraph graphs.

    Parameters
    ----------
    el : NumPy Array
        Edgelist weights.
    ixs : NumPy Array
        Index pairs representing edgelist source/targets.
    artixdict : dict
        Mapping of indexes to article names.

    Returns
    -------
    glist : list
        List of igraph graphs.

    """
    
    if type(ixs)==np.ndarray:
        ixslist = len(el)*[ixs]
    else:
        ixslist = ixs
    glist = []
    for n in range(len(el)):
        sel = pd.DataFrame(np.append(ixslist[n],
                                     np.nan_to_num(el[n].reshape(len(el[n]), 1)),
                                     axis=1))
        sel.columns = ['source', 'target', 'weight']
        sel['source'] = sel['source'].map(artixdict)
        sel['target'] = sel['target'].map(artixdict)
        tuples = [tuple(x) for x in sel.values]
        glist.append(igraph.Graph.TupleList(tuples, directed=False,
                                            edge_attrs=['weight']))
        glist[n].vs["slice"] = n

    return glist

def community_detection(timeseries, network, similarity_metric=pearsonr_ixs, window_size=7,
            algorithm=la.find_partition_temporal,
            alg_kwargs={'partition_type': la.CPMVertexPartition,
                        'vertex_id_attr': 'name',
                        'interslice_weight': 1, 'resolution_parameter': 1},
            res=None, tau=None, nodenames=None, corr_mode='centered', mode='igraph', output_mode=1):
    """
    Performs node process community detection on desired network and time series.

    Parameters
    ----------
    timeseries : Pandas DataFrame / Numpy Array
        Scaled time series for page views of each article.
    network : Numpy array / Pandas DataFrame / igraph
        Representing the network. If temporal array, dimensions should be
        (n_timesteps, n_nodes, n_nodes)
    similarity_metric : Function, optional
        Function to calculate time series similarity.
        The default is pearsonr_ixs.
    window_size : int, optional
        Correlation window size.
        The default is 7 (i.e. 1 week with daily data)
    sim_kwargs : dict, optional
        Arguments for similarity measure. The default is {}.
    algorithm : Function, optional
        Community detection algorithm to be applied to temporal network.
        The default is la.find_partition_temporal.
    alg_kwargs : dict, optional
        Arguments for community detection algorithm.
        The default is {'partition_type': la.CPMVertexPartition,
                        'vertex_id_attr': 'name', 'interslice_weight': 1,
                        'resolution_parameter': 1}.
    res : float, optional
        Resolution parameter, overrides alg_kwargs. The default is None.
    tau : float, optional
        Interlayer coupling parameter, overrides alg_kwargs. The default is None.
    nodenames : list, optional:
        List of nodenames to supply when network is supplied as NumPy array.
        The default is None.
    corr_mode : str, 'centered' or 'backward', optional
        Whether to base correlations on a centered window, or one that looks back.
        The default is 'centered'.
    mode : str, optional
        Future parameter to adapt for networkx & other input.
        The default is 'igraph'.
    output_mode : int, 1 or 0, optional
        Whether to output the membership DataFrame (1), or the raw output (0)

    Returns
    -------
    cd_output :
        Output of the supplied temporal community detection function.
    nodename_dict : dict
        Mapping of node index to names for each network layer.

    """

    for k, v in {'resolution_parameter': res, 'interslice_weight': tau}.items():
        if v:
            alg_kwargs[k] = v

    if type(network) == np.ndarray:
        if len(nodenames) != network.shape[1]:
            raise ValueError
        adj = network.copy()
    elif type(network) == pd.DataFrame:
        adj = network.values.copy()
        if not nodenames:
            nodenames = list(network.columns)
    elif mode == 'igraph':
        adj = np.array(network.get_adjacency().data)  # upper/lower/both?
        if not nodenames:
            nodenames = list(network.vs['name'])
    # elif mode == 'networkx': # future: add nx support
    #     adj = nx.to_numpy_array(network)
    #     nodenames = list(network.nodes)
    else:
        raise ValueError("Invalid mode / not yet implemented.")

    if type(timeseries) == np.ndarray:
        ts_array = timeseries.copy()
    elif type(timeseries) == pd.DataFrame:
        ts_array = np.array(timeseries[nodenames])
    else:
        raise

    nodename_idx_dict = {n: x for n, x in enumerate(nodenames)}

    # future: integrate edge weights here somehow?
    el, ixs = rolling_sim_ixs(ts_array, adj, w=window_size, sim=similarity_metric)

    if mode == 'igraph':
        processed_net = rolling_sims_to_igraph(el, ixs, nodename_idx_dict)
        nodename_dict = {n: processed_net[n].vs['name'] for n in range(len(processed_net))}
    # elif mode == 'networkx': # future: add nx support
        # processed_net = rolling_sims_to_networkx(el, ixs, nodename_idx_dict)
        # pass
    else:
        raise

    cd_output = algorithm(processed_net, **alg_kwargs)

    # decide on type of output
    if output_mode:
        if corr_mode == 'centered':
            offset = window_size // 2 # TODO: check this works ok with even window size?
        elif corr_mode == 'backward':
            offset = window_size - 1
        else:
            raise ValueError

        membership_df = pd.concat([pd.Series(x, index=nodename_dict[n],
                                            name=timeseries.index[n+offset])
                                for n, x in enumerate(cd_output[0])],
                            axis=1, sort=True)
        return membership_df
    else:
        return cd_output, nodename_dict
