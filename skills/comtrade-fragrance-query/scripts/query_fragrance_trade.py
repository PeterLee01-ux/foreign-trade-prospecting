#!/usr/bin/env python3
import argparse, csv, datetime as dt, difflib, json, os, pathlib, re, subprocess, time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError

CODES=[
 ("Equipment","Motorized domestic aroma diffuser","850980"),
 ("Equipment","Electronic/piezoelectric scent diffuser","854370"),
 ("Equipment","Commercial spray/dispersing scent machine","842489"),
 ("Equipment","Electrothermic fragrance warmer","851679"),
 ("Equipment parts","Parts for heading 8509 equipment","850990"),
 ("Human perfume","Perfumes and toilet waters","330300"),
 ("Room fragrance","Non-burning room-fragrance preparations","330749"),
 ("Industrial fragrance","Other odoriferous mixtures for industry","330290"),
 ("Burning fragrance","Incense and burning odoriferous preparations","330741"),
 ("Other fragrance","Other perfumery preparations n.e.s.","330790")]
REPORTERS_URL="https://comtradeapi.un.org/files/v1/app/reference/Reporters.json"
RESTCOUNTRIES_URL="https://restcountries.com/v3.1/all?fields=name,cca2,cca3,translations"
API="https://comtradeapi.un.org/data/v1/get/C/A/HS"

def get_json(url,headers=None,retries=3):
 last_error=None
 for attempt in range(retries):
  try:
   with urlopen(Request(url,headers=headers or {}),timeout=90) as r:return json.loads(r.read().decode("utf-8")),r.status
  except HTTPError as e:
   if e.code==429 and attempt+1<retries:time.sleep(2**attempt);continue
   raise
  except Exception as e:
   last_error=e
   if attempt+1<retries:time.sleep(2**attempt)
 cmd=["curl","-fsSL","--retry","3"]
 for k,v in (headers or {}).items():cmd += ["-H",f"{k}: {v}"]
 cmd.append(url)
 try:return json.loads(subprocess.run(cmd,check=True,capture_output=True).stdout.decode("utf-8")),200
 except Exception:raise last_error

def norm(s):return re.sub(r"[^0-9a-z\u4e00-\u9fff]","",s.casefold())

def resolve_country(query):
 rep,_=get_json(REPORTERS_URL);reporters=[x for x in rep.get("results",[]) if not x.get("isGroup")];aliases={}
 for x in reporters:
  for v in (x.get("text"),x.get("reporterDesc"),x.get("reporterCodeIsoAlpha2"),x.get("reporterCodeIsoAlpha3"),str(x.get("reporterCode"))):
   if v:aliases[norm(v)]=x
 try:
  countries,_=get_json(RESTCOUNTRIES_URL);by_iso={x.get("reporterCodeIsoAlpha2"):x for x in reporters}
  for c in countries:
   r=by_iso.get(c.get("cca2"))
   if not r:continue
   z=c.get("translations",{}).get("zho",{});vals=[c.get("name",{}).get("common"),c.get("name",{}).get("official"),z.get("common"),z.get("official")]
   for v in vals:
    if v:aliases[norm(v)]=r
 except Exception:pass
 for k,v in {"美国":"US","英国":"GB","中国":"CN","韩国":"KR","朝鲜":"KP","俄罗斯":"RU","越南":"VN","阿联酋":"AE","台湾":"TW"}.items():
  if aliases.get(norm(v)):aliases[norm(k)]=aliases[norm(v)]
 q=norm(query)
 if q in aliases:return aliases[q]
 matches=difflib.get_close_matches(q,list(aliases),n=8,cutoff=.55);names=[]
 for m in matches:
  x=aliases[m];label=f"{x['reporterDesc']} ({x.get('reporterCodeIsoAlpha2')}, {x['reporterCode']})"
  if label not in names:names.append(label)
 raise ValueError("Country not resolved. Candidates: "+", ".join(names[:5]))

def main():
 p=argparse.ArgumentParser();p.add_argument("country");p.add_argument("--years");p.add_argument("--flows",default="M,X");p.add_argument("--partner",default="0");p.add_argument("--output-dir",required=True);a=p.parse_args()
 key=os.getenv("COMTRADE_API_KEY")
 if not key:raise SystemExit("COMTRADE_API_KEY is not set")
 reporter=resolve_country(a.country);now=dt.datetime.now(dt.timezone.utc);years=a.years.split(",") if a.years else [str(now.year-i) for i in range(1,6)];flows=[x.strip().upper() for x in a.flows.split(",") if x.strip()]
 out=pathlib.Path(a.output_dir);out.mkdir(parents=True,exist_ok=True);rows=[];log=[];headers={"Ocp-Apim-Subscription-Key":key,"User-Agent":"comtrade-fragrance-query/1.0"}
 for group,product,code in CODES:
  for flow in flows:
   params={"reporterCode":reporter["reporterCode"],"period":",".join(years),"partnerCode":a.partner,"flowCode":flow,"cmdCode":code,"partner2Code":"0","customsCode":"C00","motCode":"0","maxRecords":"500"};url=API+"?"+urlencode(params);status=None;data=[];error=""
   try:obj,status=get_json(url,headers);data=obj.get("data",[]) or []
   except HTTPError as e:status=e.code;error=str(e)
   except Exception as e:error=str(e)
   for x in data:
    x["industry_group"]=group;x["product_scope"]=product;x["query_hs6"]=code;x["retrieved_at"]=now.isoformat();x["source_url"]=url;pv=x.get("primaryValue");nw=x.get("netWgt");x["usd_per_kg"]=(pv/nw if isinstance(pv,(int,float)) and isinstance(nw,(int,float)) and nw else None);rows.append(x)
   log.append({"group":group,"product":product,"cmdCode":code,"flowCode":flow,"periods":",".join(years),"url":url,"http_status":status,"row_count":len(data),"error":error,"retrieved_at":now.isoformat()})
 preferred=["industry_group","product_scope","query_hs6","period","reporterCode","reporterDesc","flowCode","flowDesc","partnerCode","partnerDesc","cmdCode","cmdDesc","primaryValue","netWgt","qty","qtyUnitAbbr","usd_per_kg","isAggregate","isReported","isEstimated","retrieved_at","source_url"];extra=sorted({k for r in rows for k in r if k not in preferred});fields=preferred+extra
 with open(out/"trade_data.csv","w",newline="",encoding="utf-8-sig") as f:w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(rows)
 with open(out/"query_log.csv","w",newline="",encoding="utf-8-sig") as f:w=csv.DictWriter(f,fieldnames=log[0].keys());w.writeheader();w.writerows(log)
 manifest={"input_country":a.country,"reporter":reporter,"years":years,"flows":flows,"partner":a.partner,"rows":len(rows),"output_dir":str(out),"created_at":now.isoformat()};(out/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8");print(json.dumps(manifest,ensure_ascii=False))

if __name__=="__main__":main()
