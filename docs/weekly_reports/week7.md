This week, I shifted focus from Voronoi diagrams to Delaunay triangulations, which are closely related. The goal was to understand how Delaunay triangulation works and how it connects with the Voronoi diagram I worked on last week.

The first step was setting up the Delaunay triangulation. I used scipy.spatial.Delaunay to compute it from the same set of points I used for the Voronoi diagram. The triangulation works by connecting points to form triangles, making sure no point is inside the circumcircle of any triangle. It was interesting to see how the triangulation divides the space into these clean triangles.

One challenge this week was handling degenerate cases, where points are collinear or very close together. In these cases, the triangulation can fail or produce weird results, so I’ll need to add some checks to handle these edge cases better. I plan to address that next week.

I keep finding problems with my code and saying "I'll address it next week" and never do. Lol. I think I'll just devote an entire week to debugging everything thoroughly at some point (not next week though)(I'm too excited about arrangements)