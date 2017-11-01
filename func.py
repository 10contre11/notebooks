# -*- coding: utf-8 -*-

"""
Draws a line.
  @param plot
  @param startX
  @param startY
  @param endX
  @param endY
"""
def drawLine(plot, startX, startY, endX, endY, lineWidth, color):
    line = [(startX, startY), (endX, endY)]
    (line_xs, line_ys) = zip(*line)
    plot.add_line(lines.Line2D(line_xs, line_ys, linewidth=lineWidth, color=color, zorder=1))

"""
Draws a soccer field.
"""
def soccerfield():
    drawLine(ax, 0, 0, 100, 100, 1, "blue")
