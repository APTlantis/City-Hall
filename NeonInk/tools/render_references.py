"""Generate deterministic SVG reference plates from compiled NeonInk tokens."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render():
    d = json.loads((ROOT/'generated/NeonInk.Tokens.json').read_text())
    p = {k:v['hex'] for k,v in d['palette'].items()}
    s = {k:p[v] for k,v in d['semantic'].items()}
    def text(x,y,value,size=18,color='text',weight=400):
        return f'<text x="{x}" y="{y}" fill="{s.get(color,color)}" font-size="{size}" font-weight="{weight}">{html.escape(str(value))}</text>'
    def rect(x,y,w,h,color,rx=0):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{s.get(color,color)}"/>'
    def line(x1,y1,x2,y2,color='border'):
        return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{s.get(color,color)}"/>'
    def board(title,desc,body):
        return ('<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="960" viewBox="0 0 1440 960" role="img" aria-labelledby="title desc">'
                f'<title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(desc)}</desc>'
                '<g font-family="Segoe UI, Arial, sans-serif">'+rect(0,0,1440,960,'canvas')+
                rect(48,44,40,4,'info')+text(104,55,'NEONINK / DATA PRESENTATION / 0.2',15,'muted',600)+body+
                line(48,888,1392,888)+text(48,921,'SYNTHETIC DESIGN FIXTURE • Not production metrics • Source: examples/reference-data.json',16,'muted')+
                '</g></svg>\n')
    fixture = json.loads((ROOT/'examples/reference-data.json').read_text())
    rows=fixture['coverage']; counts=[r['records'] for r in rows]; total=sum(counts)
    out={}
    b=text(48,132,'Where the collection is concentrated',40,'text',600)+text(48,174,'Coverage by source family · fixture snapshot · 27 September 2026',19,'muted')
    b+=rect(48,212,920,610,'panel',12)+rect(992,212,400,610,'surface',12)
    b+=text(80,256,'Records by family',23,'text',600)+text(80,287,'Count · baseline zero · sorted descending',16,'muted')
    for val in range(0,501,100):
        x=270+val
        b+=line(x,322,x,730,'border')+text(x,766,val,15,'muted')
    for i,row in enumerate(rows):
        y=340+i*78
        b+=text(80,y+28,row['family'],18,'secondary')+rect(270,y,row['records'],42,'info' if i==0 else 'process',3)+text(290+row['records'],y+28,row['records'],18,'text',600)
    b+=text(1024,265,'READ THE DISTRIBUTION',15,'info',600)+text(1024,329,f'{counts[0]/total:.0%}',64,'text',600)
    b+=text(1024,366,'of records are in Reference.',18,'secondary')+text(1024,420,f'{total:,} total records',25,'text',600)
    for y,t in [(469,'This is coverage, not quality.'),(511,'Counts do not establish accuracy,'),(539,'license clearance, or usefulness.'),(601,'CAVEAT'),(640,'Five invented source families.'),(670,'No production conclusion follows.')]: b+=text(1024,y,t,17,'warning' if t=='CAVEAT' else 'muted')
    out['Analytical-Report.svg']=board('NeonInk analytical report','Synthetic counts: '+', '.join(f'{r["family"]} {r["records"]}' for r in rows)+'. Reference is the largest family. Coverage does not establish quality.',b)
    b=text(48,132,'A dataset profile with context intact',40,'text',600)+text(48,174,'Demonstration collection / v0.0-fixture / synthetic records',19,'muted')
    for x,label,value,note in [(48,'RECORDS',f'{total:,}','Five source families'),(504,'COVERAGE WINDOW','6 months','Illustrative period only'),(960,'VALIDATION','Unknown','No production checks supplied')]:
        b+=rect(x,216,432,156,'panel',12)+text(x+24,254,label,15,'info',600)+text(x+24,306,value,36,'text',600)+text(x+24,344,note,17,'muted')
    b+=rect(48,396,844,442,'panel',12)+text(76,440,'Schema sample',24,'text',600)
    for i,(a,c,e) in enumerate([('Field','Type','Meaning'),('record_id','string','Stable source identifier'),('family','enum','Source family label'),('observed_at','date','Observation date'),('value','number | null','Measured value; null is missing')]):
        y=492+i*58
        b+=text(76,y,a,18,'info' if i==0 else 'text')+text(306,y,c,18,'secondary')+text(480,y,e,17,'secondary')+line(76,y+18,864,y+18,'border')
    b+=rect(916,396,476,442,'surface',12)+text(944,443,'Before interpreting',24,'text',600)
    for y,t in [(494,'Coverage is not representativeness.'),(533,'Missing values remain explicit.'),(572,'No license for a real corpus is implied.'),(634,'PROVENANCE'),(672,'Local synthetic fixture; no private data.'),(711,'Inspect the companion JSON for values.'),(775,'A pilot still needs real source evidence.')]: b+=text(944,y,t,17,'warning' if t=='PROVENANCE' else 'muted')
    out['Dataset-Profile.svg']=board('NeonInk dataset profile','Synthetic dataset profile with record count, unknown validation, schema and provenance limitations.',b)
    b=text(48,132,'Three color systems. Three different jobs.',40,'text',600)+text(48,174,'Series identity, ordered magnitude, and deviation from a meaningful center',19,'muted')
    for idx,(key,title,subtitle) in enumerate([('categorical','01  Categorical','Stable series keys; pair each hue with labels or distinct marks.'),('sequential-cyan','02  Sequential','Low → high; increasing lightness. Publish numeric bin boundaries.'),('diverging','03  Diverging','Below → center → above. Sign alone does not mean good or bad.')]):
        y=218+idx*210
        b+=rect(48,y,1344,190,'panel',10)+text(76,y+40,title,24,'text',600)+text(420,y+39,subtitle,18,'muted')
        for i,ref in enumerate(d['scales'][key]):
            x=76+i*260;h=p[ref]
            b+=rect(x,y+64,236,60,h,5)+text(x,y+155,h,17,'secondary')
            labels=['A • circle','B • square','C • triangle','D • diamond','E • cross'] if idx==0 else (['Low','2','3','4','High'] if idx==1 else ['Below','Below','Center','Above','Above'])
            b+=text(x+130,y+155,labels[i],15,'muted')
    b+=text(48,872,'Missing = gap or hatch + “No data”. Status = explicit label + evidence. Neither is a scale midpoint.',18,'secondary')
    out['Color-Scale-Guide.svg']=board('NeonInk color scale guide','Three labeled palettes: categorical identity, increasing lightness sequential cyan, and violet neutral cyan divergence. Missing data is separate.',b)
    return out


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    output=ROOT/'spec/references/boards'
    stale=[]
    for name,body in render().items():
        path=output/name;payload=body.encode('utf-8')
        if args.check:
            if not path.exists() or path.read_bytes()!=payload:stale.append(name)
        else:
            output.mkdir(parents=True,exist_ok=True);path.write_bytes(payload)
    if stale:raise SystemExit('Stale boards: '+', '.join(stale))
    print('PASS: 3 reference SVGs '+('verified' if args.check else 'generated'))


if __name__=='__main__':main()
