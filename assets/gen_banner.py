# Regenerates banner-{light,dark}.svg and social-preview.svg: python3 assets/gen_banner.py assets
# social-preview.png is a Chrome headless screenshot of social-preview.svg (1280x640).
import sys, os
out = sys.argv[1]
themes = {
  "light": dict(bg="#FFFFFF", fg="#0F172A", mut="#475569", line="#EEF2F6", acc="#2563EB", acc2="#7C3AED", chip="#EFF6FF", chipfg="#1D4ED8"),
  "dark":  dict(bg="#0D1117", fg="#F0F6FC", mut="#9DA7B3", line="#1B2129", acc="#58A6FF", acc2="#A371F7", chip="#132339", chipfg="#79C0FF"),
}
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
CHIPS = ["AI-in-DevOps", "Platform Engineering", "AWS", "Kubernetes", "Terraform"]
def svg(t, social=False):
    w, h = (1280, 640) if social else (1280, 280)
    grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>' for x in range(0, w+1, 40)) + \
           "".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>' for y in range(0, h+1, 40))
    if social:
        nodes = [(1000,160),(1150,120),(1100,280),(1210,330),(960,380),(1160,470),(1050,520)]
        edges = [(0,1),(0,2),(1,2),(2,3),(0,4),(2,4),(3,5),(4,6),(5,6),(2,5)]
        ty, sy, gy, ns, ss, gs = 250, 310, 360, 72, 34, 26
        cy, fs, ch, ck, pad = 410, 20, 44, 10.6, 40
    else:
        nodes = [(1040,80),(1150,60),(1110,150),(1210,170),(1000,190),(1170,240)]
        edges = [(0,1),(0,2),(1,2),(2,3),(0,4),(2,4),(3,5),(4,5)]
        ty, sy, gy, ns, ss, gs = 100, 142, 178, 48, 24, 18
        cy, fs, ch, ck, pad = 206, 15, 32, 8.4, 30
    eg = "".join(f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}"/>' for a,b in edges)
    nd = "".join(f'<circle cx="{x}" cy="{y}" r="{7 if i%2 else 5}" fill="{t["acc"] if i%2 else t["acc2"]}"/>' for i,(x,y) in enumerate(nodes))
    cx, chips = 64, ""
    for c in CHIPS:
        cw = pad + len(c)*ck
        chips += f'<rect x="{cx:.0f}" y="{cy}" width="{cw:.0f}" height="{ch}" rx="{ch//2}" fill="{t["chip"]}"/><text x="{cx+cw/2:.0f}" y="{cy+ch/2+fs*0.36:.0f}" text-anchor="middle" font-size="{fs}" font-weight="600" fill="{t["chipfg"]}">{c}</text>'
        cx += cw + 10
    r = 0 if social else 16
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Yuri Timerkhanov, Senior Platform / DevOps Engineer">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t["acc"]}"/><stop offset="1" stop-color="{t["acc2"]}"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t["bg"]}"/><stop offset="0.55" stop-color="{t["bg"]}" stop-opacity="0.6"/><stop offset="1" stop-color="{t["bg"]}" stop-opacity="0"/></linearGradient>
<clipPath id="c"><rect width="{w}" height="{h}" rx="{r}"/></clipPath></defs>
<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="{t["bg"]}"/>
<g stroke="{t["line"]}" stroke-width="1">{grid}</g>
<rect width="{w}" height="{h}" fill="url(#fade)"/>
<g stroke="{t["mut"]}" stroke-opacity="0.45" stroke-width="1.5">{eg}</g>{nd}</g>
<rect x="64" y="{ty-ns-8}" width="56" height="5" rx="2.5" fill="url(#g)"/>
<g font-family="{FONT}">
<text x="64" y="{ty}" font-size="{ns}" font-weight="700" fill="{t["fg"]}" letter-spacing="-0.5">Yuri Timerkhanov</text>
<text x="64" y="{sy}" font-size="{ss}" font-weight="600" fill="url(#g)">Senior Platform / DevOps Engineer</text>
<text x="64" y="{gy}" font-size="{gs}" fill="{t["mut"]}">Shipping AI tools for infrastructure teams · 20 years in tech · Malaysia, remote</text>
{chips}
</g>
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="{r}" fill="none" stroke="{t["line"]}"/>
</svg>
'''
for k,t in themes.items():
    open(os.path.join(out, f"banner-{k}.svg"),"w").write(svg(t))
open(os.path.join(out, "social-preview.svg"),"w").write(svg(themes["dark"], social=True))
