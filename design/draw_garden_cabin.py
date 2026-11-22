"""Dimension-led schematic for discussion, not construction documentation."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc
from pathlib import Path
R=Path(__file__).parent
fig=plt.figure(figsize=(15,12),facecolor='#f4f1e9')
ax=fig.add_axes([.05,.1,.65,.8]);ax.set_aspect('equal');ax.set_xlim(-1,11);ax.set_ylim(10.8,-1);ax.axis('off')
wall='#263e34';line='#7d796c'
def box(x,y,w,h,c='#dfd6c5',ec=line,lw=1):ax.add_patch(Rectangle((x,y),w,h,facecolor=c,edgecolor=ec,linewidth=lw))
def txt(x,y,s,size=10,weight='normal',color=wall):ax.text(x,y,s,ha='center',va='center',fontsize=size,fontweight=weight,color=color)
def ln(xs,ys,c=line,lw=1):ax.plot(xs,ys,color=c,lw=lw)
box(0,0,10,7.5,'#fffdf8');box(0,7.5,10,2.2,'#e4d9bd')
box(6.4,.2,1.2,2.4,'#e5e2d9');box(7.8,.2,2,2.4,'#dae7e1');box(6.4,2.8,3.4,.9,'#eee9dc');box(6.4,3.9,3.4,3.4,'#e8e2d4')
# Walls, with explicit openings for front doors, windows and circulation.
for x,y,w,h in [(0,0,10,.2),(0,0,.2,7.5),(9.8,0,.2,7.5),(0,7.3,1.1,.2),(4.9,7.3,2.6,.2),(9.3,7.3,.7,.2),(6.2,.2,.2,2.6),(6.2,3.7,.2,3.6),(7.6,.2,.2,2.4),(6.4,2.6,.2,.2),(7.4,2.6,.6,.2),(8.8,2.6,1,.2),(6.4,3.7,.2,.2),(7.4,3.7,2.4,.2)]:box(x,y,w,h,wall,wall)
# Glazing and slider indications.
for y in [7.34,7.43]:ln([1.1,4.9],[y,y],'#70a4ac',2);ln([7.5,9.3],[y,y],'#70a4ac',2)
ln([3,3],[7.3,7.5],'#70a4ac',2)
ln([9.85,9.85],[.7,1.7],'#70a4ac',3)
# Bedroom pocket door, hall entry left open, bathroom and storage pocket doors.
ln([6.6,7.4],[3.79,3.79],line,.8)
ln([8,8.8],[2.69,2.69],line,.8);ln([6.6,7.4],[2.69,2.69],line,.8)
# Kitchen 3.6 m counter plus refrigerator.
box(2,.2,3.6,.65);box(5.6,.2,.6,.65,'#bfc7bd')
box(4.8,.3,.7,.45,'#fffdf8');box(2.3,.3,.6,.45,'#626c64')
txt(3.9,1.2,'KITCHEN',11,'bold');txt(3.9,1.57,'3.6 m counter + tall storage',9)
# Indoor dining 1.1 m diameter table.
ax.add_patch(Circle((3.9,3.1),.55,fc='#c4a97c',ec=line))
for x,y,w,h in [(3.65,2.15,.5,.35),(3.65,3.7,.5,.35),(2.95,2.85,.35,.5),(4.5,2.85,.35,.5)]:box(x,y,w,h,'#e7dbc2')
txt(3.9,4.42,'INDOOR DINING',10,'bold')
# Lounge, comfortably away from front doors.
box(.45,4.3,.9,2.3,'#c6d3c2');box(2,4.8,.75,1.1,'#ccb68d');box(3.65,5.1,.85,.85,'#c6d3c2')
txt(2.9,6.55,'LIVING / GARDEN ENTRY',10,'bold')
# Bedroom and queen bed.
box(7.3,4.15,1.6,2,'#fffaf0');box(7.3,4.15,1.6,.16,'#b7986a')
box(7.4,4.38,.6,.38,'#e9e0ce');box(8.2,4.38,.6,.38,'#e9e0ce')
for x in [6.8,9]:box(x,4.2,.4,.45)
txt(8.1,6.7,'BEDROOM',11,'bold');txt(8.1,7.03,'3.4 × 3.4 m clear',9)
# Bath: shower, WC and basin.
box(8.8,.2,1,1,'#b8d0c5');ln([8.8,9.8],[.2,1.2],'#fffdf8');ln([8.8,9.8],[1.2,.2],'#fffdf8');txt(9.3,.7,'SHOWER',7)
box(7.85,.35,.55,.7,'#fffdf8');ax.add_patch(Circle((9.3,1.85),.25,fc='white',ec=line));box(9.05,1.45,.5,.25,'white')
txt(8.3,2.15,'BATH',9,'bold');txt(7,1.2,'STORE /\nWARDROBE',8,'bold');txt(8.1,3.23,'0.9 m PASSAGE',9,'bold')
# Veranda furniture and posts.
for x in [.2,3.3,6.2,9.6]:box(x,7.6,.18,2.0,'#e4d9bd',ec='none');box(x,9.35,.2,.2,wall)
box(.8,8.1,.75,.8,'#c6d3c2');box(2.3,8.1,.75,.8,'#c6d3c2');ax.add_patch(Circle((1.95,8.5),.25,fc='#c4a97c',ec=line))
ax.add_patch(Circle((8.2,8.55),.4,fc='#c4a97c',ec=line));txt(5.3,8.65,'COVERED VERANDA\n10.0 × 2.2 m',11,'bold')
# Dimensions.
def dim(x1,y1,x2,y2,label):
 ax.annotate('',(x1,y1),(x2,y2),arrowprops={'arrowstyle':'|-|','color':line,'lw':.8})
 txt((x1+x2)/2,(y1+y2)/2-.19,label,10)
dim(0,-.45,10,-.45,'10.0 m external');dim(0,10.15,10,10.15,'GARDEN FRONTAGE')
ax.annotate('',(-.5,0),(-.5,7.5),arrowprops={'arrowstyle':'|-|','color':line,'lw':.8});ax.text(-.72,3.75,'7.5 m enclosed depth',rotation=90,ha='center',va='center',color=wall,fontsize=10)
fig.text(.06,.95,'GARDEN CABIN',fontsize=25,fontweight='bold',color=wall)
fig.text(.06,.915,'One-bedroom concept  •  Preliminary spatial study  •  22 November 2026',fontsize=11,color=line)
notes=[('75 m²','Gross enclosed footprint'),('22 m²','Covered veranda, additional'),('PRIVATE BEDROOM','Full-height wall separates it\nfrom kitchen and living space.'),('BATHROOM BEHIND','Rear-right corner, reached\nfrom the shared passage.\nNo access through the bedroom.'),('EVERYDAY STORAGE','Rear wardrobe / utility store\nkeeps the bedroom uncluttered.'),('NEXT DESIGN PASS','Confirm wall construction,\nventilation, structure, door\nclearances and site levels.\nFurniture is drawn to scale;\nthis is not a finalized plan.')]
y=.84
for h,b in notes:
 fig.text(.74,y,h,fontsize=15 if h.endswith('m²') else 11,fontweight='bold',color=wall)
 fig.text(.74,y-.025,b,fontsize=10,color=line,va='top',linespacing=1.5)
 y-=.12 if h.endswith('m²') else .135
fig.text(.06,.045,'Dimensions in meters. Indicative 200 mm walls; construction thicknesses and net areas require architectural review.',fontsize=9,color=line)
fig.savefig(R/'garden-cabin-layout.png',dpi=150,facecolor=fig.get_facecolor())
fig.savefig(R/'garden-cabin-layout.pdf',facecolor=fig.get_facecolor())
