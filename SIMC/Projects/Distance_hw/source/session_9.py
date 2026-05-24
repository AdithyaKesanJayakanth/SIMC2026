import math


def euclidean_distance(p1, p2):
    """
    Calculate the Euclidean distance between two n-dimensional points.

    Formula: d = sqrt( (p1[0]-p2[0])^2 + (p1[1]-p2[1])^2 + ... )

    Parameters
    ----------
    p1 : list or tuple of numbers
        First point. Example: [1, 2, 3]
    p2 : list or tuple of numbers
        Second point. Must have same number of dimensions as p1.

    Returns
    -------
    float or None
        The Euclidean distance. Returns None if inputs are invalid.
    """
    # Check that both inputs exist
    if p1 is None or p2 is None:
        print("Error: points cannot be None.")
        return None

    # Check both are iterable (list, tuple, etc.)
    if not hasattr(p1, '__iter__') or not hasattr(p2, '__iter__'):
        print("Error: both inputs must be lists or tuples.")
        return None

    # Check dimensions match
    if len(p1) != len(p2):
        print(f"Error: dimension mismatch. p1 has {len(p1)}, p2 has {len(p2)}.")
        return None

    # Check all coordinates are numbers
    for i, (a, b) in enumerate(zip(p1, p2)):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            print(f"Error: non-numeric coordinate at index {i}.")
            return None

    # Core formula: sqrt of sum of squared differences
    total = 0
    for a, b in zip(p1, p2):
        total += (a - b) ** 2

    return math.sqrt(total)


def all_pairwise_distances(points):
    """
    Calculate the Euclidean distance between every unique pair
    of points in a list.

    Complexity: O(n^2) — unavoidable since there are n*(n-1)/2 pairs.

    Parameters
    ----------
    points : list of lists/tuples
        A collection of points. Example: [[0,0], [3,4], [0,4]]

    Returns
    -------
    dict or None
        Keys are (i, j) index tuples, values are distances.
        Returns None if inputs are invalid.
    """
    # Check input exists
    if points is None:
        print("Error: input cannot be None.")
        return None

    # Check input is iterable
    if not hasattr(points, '__iter__'):
        print("Error: input must be a list or sequence of points.")
        return None

    points = list(points)

    # Check there are at least 2 points
    if len(points) == 0:
        print("Error: the list of points is empty.")
        return None
    if len(points) == 1:
        print("Error: need at least 2 points to compute a distance.")
        return None

    # Check all elements are valid points
    for i, point in enumerate(points):
        if not hasattr(point, '__iter__'):
            print(f"Error: element at index {i} is not a valid point.")
            return None

    # Compute all unique pairs - O(n^2)
    results = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist is None:
                print(f"Warning: skipping pair ({i}, {j}).")
                continue
            results[(i, j)] = dist

    return results


def path_length(distances, num_points):
    """
    Calculate the total length of a path through consecutive points,
    using distances already computed by all_pairwise_distances.

    For points [P0, P1, P2, P3], the path length is:
        dist(P0,P1) + dist(P1,P2) + dist(P2,P3)

    Parameters
    ----------
    distances : dict
        Output of all_pairwise_distances. Keys are (i, j) tuples.
    num_points : int
        Number of points in the original list.

    Returns
    -------
    float or None
        Total path length. Returns None if a consecutive pair is missing.
    """
    if distances is None or num_points < 2:
        print("Error: need a valid distances dict and at least 2 points.")
        return None

    total = 0
    for i in range(num_points - 1):
        key = (i, i + 1)
        if key not in distances:
            print(f"Error: missing distance for consecutive pair {key}.")
            return None
        total += distances[key]

    return total


if __name__ == "__main__":
    # --- Example ---
    points = [ [ 0 , 0 ] , [ 1 , 0 ] , [ 1 , 1 ] , [ 2 , 1 ] , [ 2 , 2 ] , [ 2 , 0 ] ]

    dists = all_pairwise_distances(points)
    print(dists)
    print("All pairwise distances:", dists)

    length = path_length(dists, len(points))
    print("Path length:", length)

