from Motion_Detector import df
from bokeh.plotting import figure, show, output_file, Figure
from bokeh.models import HoverTool,  ColumnDataSource

df["start_string"] = df["start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["end_string"] = df["end"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)
p=figure(x_axis_type='datetime', height = 100, width = 500, title = "MotionGraph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks=1

hover = HoverTool(tooltips = [("start","@start_string"),("end","@end_string")])
p.add_tools(hover)

q = p.quad(left = "start", right = "end", bottom=0, top=1, color = "red", source=cds)

output_file("graph.html")
show(p)