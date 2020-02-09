# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:54:25 2020

@author: dnsta
"""

import osmnx as ox

graph = ox.graph_from_place("Bialystok,Poland")
type(graph)

fig,ax = ox.plot_graph(graph)

area = ox.gdf_from_place("Bialystok,Poland")

type(area)

buildings = ox.footprints_from_place("Bialystok,Poland")
len(buildings)
buildings.head(3)
buildings.columns

restaurants = ox.pois_from_place("Bialystok,Poland",amenities=['restaurant'])
len(restaurants)
restaurants.columns

cols = ['name','opening_hours','addr:city', 'addr:country', 
        'addr:housenumber', 'addr:postcode', 'addr:street']

restaurants[cols].head(10)

nodes,edges = ox.graph_to_gdfs(graph)

nodes.head(3)
edges.head(3)



import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12,8))

# Plot the footprint
area.plot(ax=ax, facecolor='black')

# Plot street edges
edges.plot(ax=ax, linewidth=1, edgecolor='#BC8F8F')

# Plot buildings
buildings.plot(ax=ax, facecolor='khaki', alpha=0.7)

# Plot restaurants
restaurants.plot(ax=ax, color='green', alpha=0.7, markersize=10)
plt.tight_layout()


from pyproj import CRS

# Set projection
projection = CRS.from_epsg(3067)

# Re-project layers
area = area.to_crs(projection)
edges = edges.to_crs(projection)
buildings = buildings.to_crs(projection)
restaurants = restaurants.to_crs(projection)


fig, ax = plt.subplots(figsize=(12,8))

# Plot the footprint
area.plot(ax=ax, facecolor='black')

# Plot street edges
edges.plot(ax=ax, linewidth=1, edgecolor='dimgray')

# Plot buildings
buildings.plot(ax=ax, facecolor='silver', alpha=0.7)

# Plot restaurants
restaurants.plot(ax=ax, color='yellow', alpha=0.7, markersize=10)
plt.tight_layout()


#add parks

leisure = ox.footprints_from_place("Bialystok, Poland",footprint_type="leisure")
leisure.head(3)

leisure['leisure'].value_counts()
parks = leisure[leisure['leisure'].isin(['park','playground'])]

parks.plot(color="green")
parks = parks.to_crs(projection)

fig, ax = plt.subplots(figsize=(12,8))

# Plot the footprint
area.plot(ax=ax, facecolor='black')

# Plot the parks
parks.plot(ax=ax, facecolor="green")

# Plot street edges
edges.plot(ax=ax, linewidth=1, edgecolor='dimgray')

# Plot buildings
buildings.plot(ax=ax, facecolor='silver', alpha=0.7)

# Plot restaurants
restaurants.plot(ax=ax, color='yellow', alpha=0.7, markersize=10)
plt.tight_layout()
















