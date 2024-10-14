This week, I focused on Voronoi diagrams, which was a fun shift from the previous work. The main goal was to generate random points, compute their Voronoi diagram using the scipy library, and visualize the result.

First, I created a function to generate random points in 2D. I made it flexible so I can control the number of points and added an option to set a random seed to keep the results consistent for testing.

Next, I used scipy.spatial.Voronoi to compute the actual diagram. The function takes the points and divides the space into regions, where each region is closest to one specific point. The computation is efficient even with larger sets of points.

The most fun part was visualizing the Voronoi diagram. Using matplotlib, I was able to plot it and really see how the space is split up by each point. Each point claims its own region, and the visuals made it much easier to grasp what’s going on.

One small challenge was dealing with points that are super close together. This can make some of the Voronoi regions really tiny or oddly shaped. I’m thinking of adding some logic to handle this better, maybe by filtering out points that are too close.

Next week, I’ll probably do Delaunay triangulations, which are closely related to Voronoi diagrams. I’m excited to see how they tie together and build on this week’s work.

I also maybe want to start using a random set of data points going forward. Add one to the data folder and then route all of my notebooks to that. We'll see though.