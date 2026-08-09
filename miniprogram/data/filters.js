// 童行小程序 - 筛选器配置
// 自动生成：由 scripts/generate_filters.py 从 venue_info.json 生成
// 城市列表(cities)手动维护，其余映射表自动生成

// 城市列表（手动维护，新增城市需确认）
const cities = [
  {
    key: 'beijing',
    name: '北京'
  },
  {
    key: 'shanghai',
    name: '上海'
  },
  {
    key: 'guangzhou',
    name: '广州'
  },
  {
    key: 'shenzhen',
    name: '深圳'
  },
  {
    key: 'hangzhou',
    name: '杭州'
  },
  {
    key: 'chengdu',
    name: '成都'
  },
  {
    key: 'chongqing',
    name: '重庆'
  },
  {
    key: 'nanjing',
    name: '南京'
  },
  {
    key: 'wuhan',
    name: '武汉'
  },
  {
    key: 'xian',
    name: '西安'
  },
  {
    key: 'zhuhai',
    name: '珠海'
  }
];

// 时间筛选
const timeFilters = [
  { key: 'upcoming', name: '最近活动' },
  { key: 'today', name: '今天' },
  { key: 'tomorrow', name: '明天' },
  { key: 'week', name: '本周' },
  { key: 'month', name: '本月' },
  { key: 'next_month', name: '下月' },
  { key: 'all', name: '全部活动' }
];

// 亲子筛选
const familyFilters = [
  { key: 'all', name: '全部活动' },
  { key: 'family', name: '适合亲子' },
  { key: 'other', name: '其他活动' }
];

// 类型筛选
const typeFilters = [
  { key: 'all', name: '全部类型' },
  { key: '展览', name: '展览' },
  { key: '讲座阅读', name: '讲座阅读' },
  { key: '科普活动', name: '科普活动' },
  { key: '演出', name: '演出' },
  { key: '影视放映', name: '影视放映' },
  { key: '体育赛事', name: '体育赛事' },
  { key: '亲子活动', name: '亲子活动' }
];

// 费用筛选
const feeFilters = [
  { key: 'all', name: '全部' },
  { key: 'free', name: '免费' },
  { key: 'paid', name: '收费' }
];

// 活动持续时长筛选（按 end_date - start_date + 1 天数）
const durationFilters = [
  { key: 'all', name: '全部时长活动' },
  { key: 'week', name: '1周内' },
  { key: '3months', name: '3个月内' },
  { key: 'long', name: '3个月以上' }
];

// 区县映射（自动生成）
const districtMapping = {
  szlib: '福田区',
  sz_children_lib: '福田区',
  szmuseum: '福田区',
  szstm: '光明区',
  szbo: '宝安区',
  szconcert: '福田区',
  szmocap: '福田区',
  szsports: '福田区',
  szmassart: '福田区',
  sznm: '坪山区',
  nslib: '南山区',
  nsmuseum: '南山区',
  nswhg: '南山区',
  nsqsng: '南山区',
  nswtzx: '南山区',
  nsaqjy: '南山区',
  skhykpg: '南山区',
  sarc: '南山区',
  ntgc: '南山区',
  zsjbwg: '南山区',
  nssxf: '南山区',
  oct_wetland: '南山区',
  szwty: '南山区',
  hlgw: '宝安区',
  ftlib: '福田区',
  ftwhg: '福田区',
  ftart: '福田区',
  lh_paleo: '罗湖区',
  lhlib: '罗湖区',
  lhwhg2: '罗湖区',
  lhtheatre: '罗湖区',
  szdjy: '罗湖区',
  balib: '宝安区',
  bamuseum: '宝安区',
  baoan_1990: '宝安区',
  baoan_kjg: '宝安区',
  baoan_ty: '宝安区',
  baoan_qsng: '宝安区',
  baoan_guihua: '宝安区',
  bayarea_eye: '宝安区',
  lglib: '龙岗区',
  lgmuseum: '龙岗区',
  lgwhg: '龙岗区',
  lgqsng: '龙岗区',
  lg_hakka: '龙岗区',
  lgtyzx: '龙岗区',
  lg_arts: '龙岗区',
  lgkjg: '龙岗区',
  lgpark: '龙岗区',
  lhxqlib: '龙华区',
  lhqsng: '龙华区',
  lhwhg: '龙华区',
  lh_printmaking: '龙华区',
  lh_ecology: '龙华区',
  lhkjg: '龙华区',
  lhbljng: '龙华区',
  gmlib: '光明区',
  gm_kjg: '光明区',
  gmwhg: '光明区',
  gmarts: '光明区',
  gmqsng: '光明区',
  gmtyzx: '光明区',
  gmhbgy: '光明区',
  gmtysq: '光明区',
  pslib: '坪山区',
  psart: '坪山区',
  psthtr: '坪山区',
  pskjg: '坪山区',
  pstyzx: '坪山区',
  psdjng: '坪山区',
  pszxgy: '坪山区',
  mlsgy: '坪山区',
  jlsgy: '坪山区',
  yhzgz: '坪山区',
  ytlib: '盐田区',
  ytwhg: '盐田区',
  yt_history: '盐田区',
  ytkjg: '盐田区',
  yttyzx: '盐田区',
  ytzgy: '盐田区',
  dpgeopark: '大鹏新区',
  dp_nuclear: '大鹏新区',
  dplib: '大鹏新区',
  dpgcbwg: '大鹏新区',
  dpwhg: '大鹏新区',
  xcart: '大鹏新区',
  dchss: '大鹏新区',
  bghsl: '大鹏新区',
  mgha: '大鹏新区',
  ymk: '大鹏新区',
  qns: '大鹏新区',
  ghysq: '大鹏新区',
  jsgjly: '大鹏新区',
  dpkjg: '大鹏新区',
  jcw: '大鹏新区',
  kcsigy: '大鹏新区',
  sz_safety: '福田区',
  opower: '南山区',
  psqsng: '坪山区',
  gdmuseum: '天河区',
  gzmuseum: '越秀区',
  gzlib: '天河区',
  shanghaimuseum: '黄浦区',
  shstm: '浦东新区',
  chnmuseum: '东城区',
  gugong: '东城区',
  hxngallery: '南山区',
  gsyart: '福田区',
  szartm: '罗湖区',
  polytheatre: '南山区',
  szcec: '福田区',
  shenzhen_world: '宝安区',
  theme_park: '南山区',
  szcp: '福田区',
  szaac: '福田区',
  szbook: '福田区',
  szhbgy: '南山区',
  hssjwh: '南山区',
  szzybwg: '福田区',
  szjewg: '盐田区',
  hlgj: '南山区',
  hoha: '南山区',
  szworld: '南山区',
  hhgy: '罗湖区',
  dshslc: '南山区',
  tjsgd: '罗湖区',
  xwhsl: '宝安区',
  mzohbd: '光明区',
  sysgy: '宝安区',
  sywhzx: '宝安区',
  hhsgy: '坪山区',
  dyzx: '龙岗区',
  dzxgy: '龙岗区',
  atszx: '福田区',
  bzgx: '龙华区',
  kxgny: '光明区',
  rcgy: '南山区',
  jhwtz: '龙岗区',
  nwwtz: '龙岗区',
  pdwtz: '龙岗区',
  ylwh: '福田区',
  tywh: '南山区',
  fhwh: '光明区',
  jlwh: '坪山区',
  jkwh: '光明区',
  zjam: '西湖区',
  北京本地宝: '密云区',
  成都本地宝: '双流区',
  重庆本地宝: '渝北区',
  广州本地宝: '白云区',
  杭州本地宝: '西湖区',
  浙江自然博物院: '下城区',
  浙江省博物馆: '下城区',
  南京本地宝: '栖霞区',
  上海本地宝: '虹口区',
  baoan: '宝安区',
  武汉本地宝: '江汉区',
  西安本地宝: '长安区',
  zhmuseum: '香洲区',
  zhlib: '香洲区',
  zhwhg: '香洲区',
  gymuseum: '香洲区',
  zhtheatre: '香洲区',
  xsart: '香洲区',
  zhplan: '香洲区',
  fzg: '香洲区',
  zhqsng: '香洲区',
  zhgrwhg: '香洲区',
  ymxy: '香洲区',
  mxpf: '香洲区',
  zhcec: '香洲区',
  hfsd: '香洲区',
  hbgy: '香洲区',
  jwlib: '金湾区',
  jwwhg: '金湾区',
  jwmuseum: '金湾区',
  jwart: '金湾区',
  tcbj: '金湾区',
  zhairshow: '金湾区',
  hqw: '金湾区',
  jwtyzx: '金湾区',
  szwhzx: '金湾区',
  jhawhys: '金湾区',
  dmlib: '斗门区',
  dmmuseum: '斗门区',
  dmwhg: '斗门区',
  dmjj: '斗门区',
  jts: '斗门区',
  ywq: '斗门区',
  dmtyzx: '斗门区',
  jawhzx: '斗门区',
  hys: '斗门区',
  dmfy: '斗门区',
  hqwhys: '横琴新区',
  zhlh: '横琴新区',
  zhfclc: '横琴新区',
  zhhqtj: '横琴新区',
  hqwlqzx: '横琴新区',
  xld: '横琴新区',
  hqsdgy: '横琴新区',
  hqhchl: '横琴新区',
  hqka: '横琴新区',
  hqjrd: '横琴新区',
  zhyn: '香洲区',
  yld: '香洲区',
  zhtyzx: '香洲区',
  xzwhg: '香洲区',
  szwt_12865898: '龙岗区',
  szwt_12865897: '龙岗区',
  szwt_12864965: '龙岗区',
  szwt_12864964: '龙岗区',
  szwt_12864963: '龙岗区',
  szwt_12863189: '龙岗区',
  szwt_12861229: '龙岗区',
  szwt_12861228: '龙岗区',
  szwt_12861227: '龙岗区',
  szwt_12861226: '龙岗区',
  szwt_12861225: '龙岗区',
  szwt_12374186: '龙岗区',
  szwt_12364958: '光明区',
  szwt_12095611: '坪山区',
  szwt_11671562: '福田区',
  szwt_11644501: '南山区',
  szwt_11668510: '南山区',
  szwt_11485498: '福田区',
  szwt_11485497: '福田区',
  szwt_11485496: '福田区',
  szwt_11485494: '福田区',
  szwt_11485500: '福田区',
  szwt_11171158: '大鹏新区',
  szwt_11170215: '坪山区',
  szwt_11170203: '坪山区',
  szwt_11170204: '坪山区',
  szwt_11168520: '龙华区',
  szwt_11168444: '龙华区',
  szwt_11166909: '龙华区',
  szwt_11166908: '龙华区',
  szwt_11166901: '龙华区',
  szwt_11167831: '龙岗区',
  szwt_11167822: '龙岗区',
  szwt_11167080: '龙岗区',
  szwt_11153449: '宝安区',
  szwt_11132724: '南山区',
  szwt_11132704: '南山区',
  szwt_11145352: '龙华区',
  szwt_11131232: '南山区',
  szwt_11129404: '南山区',
  szwt_11128382: '光明区',
  szwt_11128585: '光明区',
  szwt_11128370: '光明区',
  szwt_11127123: '深汕特别合作区',
  szwt_11116977: '宝安区',
  szwt_11116976: '宝安区',
  szwt_11114637: '坪山区',
  szwt_11114636: '坪山区',
  szwt_11114635: '坪山区',
  szwt_11111303: '福田区',
  szwt_12766454: '光明区',
  szwt_12699929: '罗湖区',
  szwt_12699821: '罗湖区',
  szwt_12699826: '罗湖区',
  szwt_12502724: '龙岗区',
  szwt_12490550: '龙岗区',
  szwt_12490551: '龙岗区',
  szwt_12364970: '光明区',
  szwt_12364975: '光明区',
  szwt_11999373: '福田区',
  szwt_11197294: '龙华区',
  szwt_11169238: '大鹏新区',
  szwt_11169235: '大鹏新区',
  szwt_11169234: '大鹏新区',
  szwt_11169233: '大鹏新区',
  szwt_11168746: '大鹏新区',
  szwt_11168745: '大鹏新区',
  szwt_11168743: '大鹏新区',
  szwt_11168742: '大鹏新区',
  szwt_11167839: '龙岗区',
  szwt_11151909: '盐田区',
  szwt_11151908: '盐田区',
  szwt_11151907: '盐田区',
  szwt_11145432: '龙华区',
  szwt_11136104: '南山区',
  szwt_11135809: '南山区',
  szwt_11133787: '大鹏新区',
  szwt_11133687: '福田区',
  szwt_11131701: '南山区',
  szwt_11129884: '南山区',
  szwt_11129883: '南山区',
  szwt_11129790: '南山区',
  szwt_11129541: '南山区',
  szwt_11129527: '南山区',
  szwt_11128645: '南山区',
  szwt_11126064: '龙华区',
  szwt_11117341: '宝安区',
  szwt_11117342: '宝安区',
  szwt_11117343: '宝安区',
  szwt_11117344: '宝安区',
  szwt_11114606: '坪山区',
  szwt_11111766: '福田区',
  szwt_11111767: '福田区',
  szwt_11111768: '福田区',
  szwt_11111769: '福田区',
  szwt_11111305: '福田区',
  szwt_11111306: '福田区',
  beijing_gov_wwj_546081: '怀柔区',
  beijing_gov_wwj_546090: '西城区',
  beijing_gov_wwj_546099: '朝阳区',
  beijing_gov_wwj_546102: '西城区',
  beijing_gov_wwj_546114: '东城区',
  beijing_gov_wwj_546117: '通州区',
  beijing_gov_wwj_546123: '延庆区',
  beijing_gov_wwj_546120: '大兴区',
  beijing_gov_wwj_546129: '海淀区',
  beijing_gov_wwj_546132: '西城区',
  beijing_gov_wwj_546135: '怀柔区',
  beijing_gov_wwj_546150: '怀柔区',
  beijing_gov_wwj_546162: '朝阳区',
  beijing_gov_wwj_546174: '朝阳区',
  beijing_gov_wwj_546171: '朝阳区',
  beijing_gov_wwj_546183: '朝阳区',
  beijing_gov_wwj_546186: '东城区',
  beijing_gov_wwj_546195: '海淀区',
  beijing_gov_wwj_546198: '平谷区',
  beijing_gov_wwj_546192: '朝阳区',
  beijing_gov_wwj_546204: '朝阳区',
  beijing_gov_wwj_546213: '东城区',
  beijing_gov_wwj_546210: '海淀区',
  beijing_gov_wwj_546219: '通州区',
  beijing_gov_wwj_662437: '延庆区',
  beijing_gov_wwj_662465: '海淀区',
  beijing_gov_wwj_10877380: '东城区',
  beijing_gov_wwj_10877385: '海淀区',
  beijing_gov_wwj_10877395: '朝阳区',
  beijing_gov_wwj_10877405: '怀柔区，东城区',
  beijing_gov_wwj_10877415: '大兴区',
  beijing_gov_wwj_10877420: '通州区',
  beijing_gov_wwj_10877425: '石景山区',
  beijing_gov_wwj_10877430: '房山区',
  beijing_gov_wwj_11077312: '朝阳区',
  beijing_gov_wwj_11077317: '通州区',
  beijing_gov_wwj_11077327: '西城区',
  beijing_gov_wwj_11077332: '石景山区',
  beijing_gov_wwj_11077337: '海淀区',
  beijing_gov_wwj_11077342: '东城区',
  beijing_gov_wwj_11186650: '西城区',
  beijing_gov_wwj_21228162: '房山区',
  beijing_gov_wwj_21228167: '海淀区',
  beijing_gov_wwj_325729805: '延庆区',
  beijing_gov_wwj_325822216: '东城区',
  beijing_gov_wwj_325822223: '东城区',
  beijing_gov_wwj_325880511: '朝阳区',
  beijing_gov_wwj_325880521: '顺义区',
  beijing_gov_wwj_325880527: '朝阳区',
  beijing_gov_wwj_325968712: '朝阳区',
  beijing_gov_wwj_546027: '东城区',
  beijing_gov_wwj_545811: '西城区',
  beijing_gov_wwj_10877390: '昌平区',
  beijing_gov_wwj_662468: '朝阳区',
  beijing_gov_wwj_10877410: '大兴区',
  beijing_gov_wwj_545940: '朝阳区',
  beijing_gov_wwj_545964: '房山区',
  beijing_gov_wwj_326114740: '朝阳区',
  beijing_gov_wwj_21228156: '顺义区',
  beijing_gov_wwj_546072: '西城区',
  beijing_gov_wwj_545895: '东城区',
  beijing_gov_wwj_325729820: '房山区',
  beijing_gov_wwj_546156: '房山区',
  beijing_gov_wwj_546084: '通州区',
  beijing_gov_wwj_545982: '海淀区',
  beijing_gov_wwj_325729837: '海淀区',
  beijing_gov_wwj_546147: '海淀区',
  beijing_gov_wwj_546021: '朝阳区',
  beijing_gov_wwj_546015: '朝阳区',
  beijing_gov_wwj_545853: '朝阳区',
  beijing_gov_wwj_546024: '东城区',
  beijing_gov_wwj_326128383: '丰台区',
  beijing_gov_wwj_743627558: '昌平区',
  beijing_gov_wwj_743627668: '通州区',
  beijing_gov_wwj_743627673: '西城区',
  beijing_gov_wwj_743627719: '顺义区',
  beijing_gov_wwj_743627734: '石景山区',
  beijing_gov_wwj_743627785: '丰台区',
  beijing_gov_wwj_743627797: '朝阳区',
  beijing_gov_wwj_743627807: '西城区',
  beijing_gov_wwj_743627813: '朝阳区',
  beijing_gov_wwj_743627828: '东城区',
  beijing_gov_wwj_743627844: '西城区',
  beijing_gov_wwj_743627862: '西城区',
  beijing_gov_wwj_743627885: '石景山区',
  beijing_gov_wwj_743627911: '朝阳区',
  beijing_gov_wwj_743627928: '西城区',
  beijing_gov_wwj_743627936: '朝阳区',
  beijing_gov_wwj_743627941: '大兴区',
  beijing_gov_wwj_545763: '西城区',
  beijing_gov_wwj_545784: '海淀区',
  beijing_gov_wwj_743627946: '海淀区',
  beijing_gov_wwj_743627951: '大兴区',
  beijing_gov_wwj_743627956: '海淀区',
  beijing_gov_wwj_743627961: '西城区',
  beijing_gov_wwj_743627969: '朝阳区',
  beijing_gov_wwj_743627974: '房山区',
  beijing_gov_wwj_743627979: '西城区',
  beijing_gov_wwj_743627987: '怀柔区',
  beijing_gov_wwj_743627996: '延庆区',
  beijing_gov_wwj_743628001: '大兴区',
  beijing_gov_wwj_743628006: '朝阳区',
  beijing_gov_wwj_743628012: '门头沟区',
  beijing_gov_wwj_743628017: '海淀区',
  beijing_gov_wwj_545793: '西城区',
  beijing_gov_wwj_545796: '朝阳区',
  beijing_gov_wwj_545799: '昌平区',
  beijing_gov_wwj_545808: '西城区',
  beijing_gov_wwj_545817: '东城区',
  beijing_gov_wwj_545829: '丰台区',
  beijing_gov_wwj_545832: '海淀区',
  beijing_gov_wwj_545835: '西城区',
  beijing_gov_wwj_545838: '海淀区',
  beijing_gov_wwj_545841: '延庆区',
  beijing_gov_wwj_545844: '顺义区',
  beijing_gov_wwj_545847: '海淀区',
  beijing_gov_wwj_545850: '海淀区',
  beijing_gov_wwj_545856: '房山区',
  beijing_gov_wwj_545859: '密云区',
  beijing_gov_wwj_545862: '昌平区',
  beijing_gov_wwj_545865: '通州区',
  beijing_gov_wwj_545868: '延庆区',
  beijing_gov_wwj_545871: '丰台区',
  beijing_gov_wwj_545874: '平谷区',
  beijing_gov_wwj_545877: '西城区',
  beijing_gov_wwj_545880: '石景山区',
  beijing_gov_wwj_545883: '房山区',
  beijing_gov_wwj_545886: '大兴区',
  beijing_gov_wwj_545889: '朝阳区',
  beijing_gov_wwj_545892: '西城区',
  beijing_gov_wwj_545898: '东城区',
  beijing_gov_wwj_545901: '东城区',
  beijing_gov_wwj_545904: '海淀区',
  beijing_gov_wwj_545907: '东城区',
  beijing_gov_wwj_545910: '门头沟区',
  beijing_gov_wwj_545913: '东城区',
  beijing_gov_wwj_545916: '石景山区',
  beijing_gov_wwj_545919: '海淀区',
  beijing_gov_wwj_545922: '海淀区',
  beijing_gov_wwj_545925: '海淀区',
  beijing_gov_wwj_545931: '朝阳区',
  beijing_gov_wwj_545934: '朝阳区',
  beijing_gov_wwj_545937: '西城区',
  beijing_gov_wwj_545943: '西城区',
  beijing_gov_wwj_545949: '西城区',
  beijing_gov_wwj_545952: '朝阳区',
  beijing_gov_wwj_545958: '西城区',
  beijing_gov_wwj_545955: '海淀区',
  beijing_gov_wwj_545967: '延庆区',
  beijing_gov_wwj_545961: '丰台区',
  beijing_gov_wwj_545976: '海淀区',
  beijing_gov_wwj_545970: '门头沟区',
  beijing_gov_wwj_545973: '朝阳区',
  beijing_gov_wwj_545979: '海淀区',
  beijing_gov_wwj_545991: '昌平区',
  beijing_gov_wwj_545994: '西城区',
  beijing_gov_wwj_546003: '东城区',
  beijing_gov_wwj_546006: '朝阳区',
  beijing_gov_wwj_546009: '大兴区',
  beijing_gov_wwj_546018: '海淀区',
  beijing_gov_wwj_546030: '东城区',
  beijing_gov_wwj_546033: '朝阳区',
  beijing_gov_wwj_546045: '朝阳区',
  beijing_gov_wwj_546048: '东城区',
  beijing_gov_wwj_546054: '东城区',
  beijing_gov_wwj_546057: '昌平区',
  beijing_gov_wwj_546069: '昌平区',
  beijing_gov_wwj_546063: '东城区',
  beijing_gov_wwj_546066: '海淀区',
  beijing_gov_wwj_545736: '东城区',
  beijing_gov_wwj_545742: '西城区',
  beijing_gov_wwj_545748: '朝阳区',
  beijing_gov_wwj_545754: '丰台区',
  beijing_gov_tyj_1: '东城区',
  beijing_gov_tyj_2: '东城区',
  beijing_gov_tyj_3: '东城区',
  beijing_gov_tyj_4: '东城区',
  beijing_gov_tyj_5: '西城区',
  beijing_gov_tyj_6: '西城区',
  beijing_gov_tyj_7: '西城区',
  beijing_gov_tyj_8: '西城区',
  beijing_gov_tyj_9: '西城区',
  beijing_gov_tyj_10: '西城区',
  beijing_gov_tyj_12: '朝阳区',
  beijing_gov_tyj_13: '朝阳区',
  beijing_gov_tyj_14: '海淀区',
  beijing_gov_tyj_15: '丰台区',
  beijing_gov_tyj_16: '丰台区',
  beijing_gov_tyj_17: '门头沟区',
  beijing_gov_tyj_18: '房山区',
  beijing_gov_tyj_19: '房山区',
  beijing_gov_tyj_20: '房山区',
  beijing_gov_tyj_21: '通州区',
  beijing_gov_tyj_22: '顺义区',
  beijing_gov_tyj_23: '顺义区',
  beijing_gov_tyj_24: '昌平区',
  beijing_gov_tyj_25: '昌平区',
  beijing_gov_tyj_26: '昌平区',
  beijing_gov_tyj_27: '昌平区',
  beijing_gov_tyj_28: '大兴区',
  beijing_gov_tyj_29: '平谷区',
  beijing_gov_tyj_30: '怀柔区',
  beijing_gov_tyj_31: '密云区',
  beijing_gov_tyj_32: '延庆区',
  beijing_gov_tyj_33: '北京经济技术开发区',
  beijing_gov_tyj_34: '燕山地区',
  chongqing_gov_bowuguan_1: '渝中区',
  chongqing_gov_bowuguan_2: '渝中区',
  chongqing_gov_bowuguan_3: '沙坪坝区',
  chongqing_gov_bowuguan_4: '大足区',
  chongqing_gov_bowuguan_6: '渝中区',
  chongqing_gov_bowuguan_8: '渝中区',
  chongqing_gov_bowuguan_9: '渝中区',
  chongqing_gov_bowuguan_10: '渝中区',
  chongqing_gov_bowuguan_11: '渝中区',
  chongqing_gov_bowuguan_12: '渝中区',
  chongqing_gov_bowuguan_13: '渝中区',
  chongqing_gov_bowuguan_14: '渝中区',
  chongqing_gov_bowuguan_16: '两江新区',
  chongqing_gov_bowuguan_17: '两江新区',
  chongqing_gov_bowuguan_19: '沙坪坝区',
  chongqing_gov_bowuguan_20: '九龙坡区',
  chongqing_gov_bowuguan_21: '南岸区',
  chongqing_gov_bowuguan_22: '北碚区',
  chongqing_gov_bowuguan_23: '北碚区',
  chongqing_gov_bowuguan_24: '两江新区',
  chongqing_gov_bowuguan_25: '两江新区',
  chongqing_gov_bowuguan_26: '涪陵区',
  chongqing_gov_bowuguan_27: '万州区',
  chongqing_gov_bowuguan_28: '万州区',
  chongqing_gov_bowuguan_29: '万州区',
  chongqing_gov_bowuguan_30: '万州区',
  chongqing_gov_bowuguan_31: '万州区',
  chongqing_gov_bowuguan_32: '万州区',
  chongqing_gov_bowuguan_33: '黔江区',
  chongqing_gov_bowuguan_34: '黔江区',
  chongqing_gov_bowuguan_35: '黔江区',
  chongqing_gov_bowuguan_36: '涪陵区',
  chongqing_gov_bowuguan_37: '渝中区',
  chongqing_gov_bowuguan_38: '渝中区',
  chongqing_gov_bowuguan_39: '渝中区',
  chongqing_gov_bowuguan_40: '渝中区',
  chongqing_gov_bowuguan_41: '渝中区',
  chongqing_gov_bowuguan_42: '渝中区',
  chongqing_gov_bowuguan_43: '渝中区',
  chongqing_gov_bowuguan_44: '渝中区',
  chongqing_gov_bowuguan_45: '渝中区',
  chongqing_gov_bowuguan_46: '渝中区',
  chongqing_gov_bowuguan_47: '大渡口区',
  chongqing_gov_bowuguan_48: '两江新区',
  chongqing_gov_bowuguan_49: '两江新区',
  chongqing_gov_bowuguan_50: '两江新区',
  chongqing_gov_bowuguan_51: '沙坪坝区',
  chongqing_gov_bowuguan_52: '沙坪坝区',
  chongqing_gov_bowuguan_53: '沙坪坝区',
  chongqing_gov_bowuguan_54: '沙坪坝区',
  chongqing_gov_bowuguan_55: '沙坪坝区',
  chongqing_gov_bowuguan_56: '沙坪坝区',
  chongqing_gov_bowuguan_57: '九龙坡区',
  chongqing_gov_bowuguan_58: '九龙坡区',
  chongqing_gov_bowuguan_59: '九龙坡区',
  chongqing_gov_bowuguan_60: '九龙坡区',
  chongqing_gov_bowuguan_61: '九龙坡区',
  chongqing_gov_bowuguan_62: '九龙坡区',
  chongqing_gov_bowuguan_63: '九龙坡区',
  chongqing_gov_bowuguan_64: '九龙坡区',
  chongqing_gov_bowuguan_65: '南岸区',
  chongqing_gov_bowuguan_66: '南岸区',
  chongqing_gov_bowuguan_67: '南岸区',
  chongqing_gov_bowuguan_68: '南岸区',
  chongqing_gov_bowuguan_69: '北碚区',
  chongqing_gov_bowuguan_70: '北碚区',
  chongqing_gov_bowuguan_71: '北碚区',
  chongqing_gov_bowuguan_72: '北碚区',
  chongqing_gov_bowuguan_73: '北碚区',
  chongqing_gov_bowuguan_74: '北碚区',
  chongqing_gov_bowuguan_75: '北碚区',
  chongqing_gov_bowuguan_76: '北碚区',
  chongqing_gov_bowuguan_78: '北碚区',
  chongqing_gov_bowuguan_79: '北碚区',
  chongqing_gov_bowuguan_80: '两江新区',
  chongqing_gov_bowuguan_81: '两江新区',
  chongqing_gov_bowuguan_82: '两江新区',
  chongqing_gov_bowuguan_83: '两江新区',
  chongqing_gov_bowuguan_84: '巴南区',
  chongqing_gov_bowuguan_85: '巴南区',
  chongqing_gov_bowuguan_86: '巴南区',
  chongqing_gov_bowuguan_87: '长寿区',
  chongqing_gov_bowuguan_88: '长寿区',
  chongqing_gov_bowuguan_89: '江津区',
  chongqing_gov_bowuguan_90: '江津区',
  chongqing_gov_bowuguan_91: '江津区',
  chongqing_gov_bowuguan_92: '江津区',
  chongqing_gov_bowuguan_93: '合川区',
  chongqing_gov_bowuguan_94: '合川区',
  chongqing_gov_bowuguan_95: '合川区',
  chongqing_gov_bowuguan_96: '合川区',
  chongqing_gov_bowuguan_97: '合川区',
  chongqing_gov_bowuguan_98: '永川区',
  chongqing_gov_bowuguan_99: '永川区',
  chongqing_gov_bowuguan_100: '永川区',
  chongqing_gov_bowuguan_101: '南川区',
  chongqing_gov_bowuguan_102: '南川区',
  chongqing_gov_bowuguan_103: '綦江区',
  chongqing_gov_bowuguan_104: '綦江区',
  chongqing_gov_bowuguan_105: '大足区',
  chongqing_gov_bowuguan_106: '大足区',
  chongqing_gov_bowuguan_107: '璧山区',
  chongqing_gov_bowuguan_108: '铜梁区',
  chongqing_gov_bowuguan_109: '铜梁区',
  chongqing_gov_bowuguan_110: '铜梁区',
  chongqing_gov_bowuguan_111: '潼南区',
  chongqing_gov_bowuguan_112: '潼南区',
  chongqing_gov_bowuguan_113: '荣昌区',
  chongqing_gov_bowuguan_114: '荣昌区',
  chongqing_gov_bowuguan_115: '荣昌区',
  chongqing_gov_bowuguan_116: '荣昌区',
  chongqing_gov_bowuguan_117: '开州区',
  chongqing_gov_bowuguan_118: '开州区',
  chongqing_gov_bowuguan_119: '开州区',
  chongqing_gov_bowuguan_120: '梁平区',
  chongqing_gov_bowuguan_121: '武隆区',
  chongqing_gov_bowuguan_122: '武隆区',
  chongqing_gov_bowuguan_123: '武隆区',
  chongqing_gov_bowuguan_124: '城口县',
  chongqing_gov_bowuguan_125: '城万旧址：城口县',
  chongqing_gov_bowuguan_126: '丰都县',
  chongqing_gov_bowuguan_130: '云阳县',
  chongqing_gov_bowuguan_131: '云阳县',
  chongqing_gov_bowuguan_132: '云阳县',
  chongqing_gov_bowuguan_133: '云阳县',
  chongqing_gov_bowuguan_134: '云阳县',
  chongqing_gov_bowuguan_135: '奉节县',
  chongqing_gov_bowuguan_136: '奉节县',
  chongqing_gov_bowuguan_137: '奉节县',
  chongqing_gov_bowuguan_138: '奉节县',
  chongqing_gov_bowuguan_139: '巫山县',
  chongqing_gov_bowuguan_140: '巫山县',
  chongqing_gov_bowuguan_141: '巫山县',
  chongqing_gov_bowuguan_142: '巫山县',
  chongqing_gov_bowuguan_143: '巫溪县',
  chongqing_gov_bowuguan_144: '石柱县',
  chongqing_gov_bowuguan_147: '酉阳县',
  chongqing_gov_bowuguan_148: '酉阳自治县',
  chongqing_gov_bowuguan_149: '酉阳县',
  chongqing_gov_bowuguan_151: '彭水县',
  chongqing_gov_bowuguan_152: '万盛经开区',
  chongqing_gov_tushuguan_2: '两江新区',
  chongqing_gov_tushuguan_3: '万州区',
  chongqing_gov_tushuguan_4: '黔江区',
  chongqing_gov_tushuguan_5: '涪陵区',
  chongqing_gov_tushuguan_6: '渝中区',
  chongqing_gov_tushuguan_7: '大渡口区',
  chongqing_gov_tushuguan_8: '鸿恩寺馆:重庆市',
  chongqing_gov_tushuguan_9: '沙坪坝区',
  chongqing_gov_tushuguan_10: '九龙坡区',
  chongqing_gov_tushuguan_11: '南岸区',
  chongqing_gov_tushuguan_12: '北碚区',
  chongqing_gov_tushuguan_13: '两江新区',
  chongqing_gov_tushuguan_14: '巴南区',
  chongqing_gov_tushuguan_15: '长寿区',
  chongqing_gov_tushuguan_16: '江津区',
  chongqing_gov_tushuguan_17: '合川区',
  chongqing_gov_tushuguan_18: '南川区',
  chongqing_gov_tushuguan_19: '大足区',
  chongqing_gov_tushuguan_20: '大足区',
  chongqing_gov_tushuguan_21: '万盛经济技术开发区',
  chongqing_gov_tushuguan_22: '綦江区',
  chongqing_gov_tushuguan_23: '永川区',
  chongqing_gov_tushuguan_24: '潼南区',
  chongqing_gov_tushuguan_25: '璧山区',
  chongqing_gov_tushuguan_26: '铜梁区',
  chongqing_gov_tushuguan_27: 'A馆:重庆市',
  chongqing_gov_tushuguan_28: '梁平区',
  chongqing_gov_tushuguan_29: '武隆区',
  chongqing_gov_tushuguan_30: '开州区',
  chongqing_gov_tushuguan_31: '城口县',
  chongqing_gov_tushuguan_32: '丰都县',
  chongqing_gov_tushuguan_33: '垫江县',
  chongqing_gov_tushuguan_35: '云阳县',
  chongqing_gov_tushuguan_36: '奉节县',
  chongqing_gov_tushuguan_37: '巫山县',
  chongqing_gov_tushuguan_38: '巫溪县',
  chongqing_gov_tushuguan_39: '石柱县',
  chongqing_gov_tushuguan_41: '酉阳县',
  chongqing_gov_wenhuaguan_1: '两江新区',
  chongqing_gov_wenhuaguan_2: '万州区',
  chongqing_gov_wenhuaguan_3: '涪陵区',
  chongqing_gov_wenhuaguan_4: '渝中区',
  chongqing_gov_wenhuaguan_5: '大渡口区',
  chongqing_gov_wenhuaguan_6: '江北区',
  chongqing_gov_wenhuaguan_7: '沙坪坝区',
  chongqing_gov_wenhuaguan_8: '九龙坡区',
  chongqing_gov_wenhuaguan_9: '南岸区',
  chongqing_gov_wenhuaguan_10: '北碚区',
  chongqing_gov_wenhuaguan_11: '綦江区',
  chongqing_gov_wenhuaguan_12: '大足区',
  chongqing_gov_wenhuaguan_13: '大足区',
  chongqing_gov_wenhuaguan_14: '渝北区',
  chongqing_gov_wenhuaguan_15: '巴南区',
  chongqing_gov_wenhuaguan_16: '黔江区',
  chongqing_gov_wenhuaguan_17: '长寿区',
  chongqing_gov_wenhuaguan_18: '江津区',
  chongqing_gov_wenhuaguan_19: '合川区',
  chongqing_gov_wenhuaguan_20: '永川区',
  chongqing_gov_wenhuaguan_21: '南川区',
  chongqing_gov_wenhuaguan_22: '璧山区',
  chongqing_gov_wenhuaguan_23: '万盛经开区',
  chongqing_gov_wenhuaguan_24: '铜梁区',
  chongqing_gov_wenhuaguan_25: '潼南区',
  chongqing_gov_wenhuaguan_26: '荣昌区',
  chongqing_gov_wenhuaguan_27: '开州区',
  chongqing_gov_wenhuaguan_29: '武隆区',
  chongqing_gov_wenhuaguan_30: '城口县',
  chongqing_gov_wenhuaguan_31: '丰都县',
  chongqing_gov_wenhuaguan_32: '垫江县',
  chongqing_gov_wenhuaguan_34: '云阳县',
  chongqing_gov_wenhuaguan_35: '奉节县',
  chongqing_gov_wenhuaguan_36: '巫山县',
  chongqing_gov_wenhuaguan_37: '巫溪县',
  chongqing_gov_wenhuaguan_38: '石柱县',
  chongqing_gov_wenhuaguan_39: '秀山县',
  chongqing_gov_wenhuaguan_40: '酉阳县',
  chongqing_gov_tiyu_1: '市体育馆',
  chongqing_gov_tiyu_2: '大田湾体育场',
  chongqing_gov_tiyu_3: '奥体中心体育场',
  chongqing_gov_tiyu_4: '奥体中心体育场',
  chongqing_gov_tiyu_6: '万州区',
  chongqing_gov_tiyu_7: '万州区',
  chongqing_gov_tiyu_8: '万州区',
  chongqing_gov_tiyu_9: '涪陵区',
  chongqing_gov_tiyu_10: '涪陵区',
  chongqing_gov_tiyu_11: '大渡口区',
  chongqing_gov_tiyu_12: '南岸区',
  chongqing_gov_tiyu_13: '南岸区',
  chongqing_gov_tiyu_14: '南岸区',
  chongqing_gov_tiyu_15: '南岸区',
  chongqing_gov_tiyu_16: '北陪区',
  chongqing_gov_tiyu_17: '北陪区',
  chongqing_gov_tiyu_18: '綦江区',
  chongqing_gov_tiyu_19: '綦江区',
  chongqing_gov_tiyu_20: '綦江区',
  chongqing_gov_tiyu_21: '綦江区',
  chongqing_gov_tiyu_22: '綦江区',
  chongqing_gov_tiyu_23: '綦江区',
  chongqing_gov_tiyu_24: '大足区',
  chongqing_gov_tiyu_25: '大足区',
  chongqing_gov_tiyu_26: '大足区',
  chongqing_gov_tiyu_27: '黔江区',
  chongqing_gov_tiyu_28: '黔江区',
  chongqing_gov_tiyu_29: '黔江区',
  chongqing_gov_tiyu_30: '长寿区',
  chongqing_gov_tiyu_31: '长寿区',
  chongqing_gov_tiyu_32: '江津区',
  chongqing_gov_tiyu_33: '江津区',
  chongqing_gov_tiyu_34: '江津区',
  chongqing_gov_tiyu_35: '江津区',
  chongqing_gov_tiyu_36: '合川区',
  chongqing_gov_tiyu_37: '永川区',
  chongqing_gov_tiyu_38: '永川区',
  chongqing_gov_tiyu_39: '永川区',
  chongqing_gov_tiyu_40: '南川区',
  chongqing_gov_tiyu_41: '南川区',
  chongqing_gov_tiyu_43: '璧山区',
  chongqing_gov_tiyu_44: '璧山区',
  chongqing_gov_tiyu_45: '铜梁区',
  chongqing_gov_tiyu_46: '铜梁区',
  chongqing_gov_tiyu_47: '铜梁区',
  chongqing_gov_tiyu_48: '铜梁区',
  chongqing_gov_tiyu_49: '潼南区',
  chongqing_gov_tiyu_50: '潼南区',
  chongqing_gov_tiyu_51: '荣昌区',
  chongqing_gov_tiyu_52: '荣昌区',
  chongqing_gov_tiyu_53: '荣昌区',
  chongqing_gov_tiyu_54: '荣昌区',
  chongqing_gov_tiyu_55: '武隆区',
  chongqing_gov_tiyu_56: '城口县',
  chongqing_gov_tiyu_57: '城口县',
  chongqing_gov_tiyu_58: '城口县',
  chongqing_gov_tiyu_59: '城口县',
  chongqing_gov_tiyu_61: '丰都县',
  chongqing_gov_tiyu_62: '丰都县',
  chongqing_gov_tiyu_64: '垫江县',
  chongqing_gov_tiyu_65: '垫江县',
  chongqing_gov_tiyu_66: '垫江县',
  chongqing_gov_tiyu_67: '忠县',
  chongqing_gov_tiyu_68: '云阳县',
  chongqing_gov_tiyu_69: '云阳县',
  chongqing_gov_tiyu_70: '云阳县',
  chongqing_gov_tiyu_71: '云阳县',
  chongqing_gov_tiyu_72: '巫山县',
  chongqing_gov_tiyu_73: '巫山县',
  chongqing_gov_tiyu_74: '巫山县',
  chongqing_gov_tiyu_75: '巫山县',
  chongqing_gov_tiyu_76: '石柱县',
  chongqing_gov_tiyu_77: '石柱县',
  chongqing_gov_tiyu_78: '秀山县',
  chongqing_gov_tiyu_79: '秀山县',
  chongqing_gov_tiyu_80: '彭水县',
  chongqing_gov_tiyu_81: '彭水县',
  chongqing_gov_tiyu_82: '彭水县',
  chongqing_gov_tiyu_83: '开州区',
  chongqing_gov_tiyu_84: '开州区',
  chongqing_gov_tiyu_85: '开州区',
  chongqing_gov_tiyu_86: '梁平区',
  chongqing_gov_tiyu_87: '梁平区',
  chongqing_gov_tiyu_88: '酉阳县',
  hangzhou_gov_杭州市西湖区文化馆: '西湖区',
  hangzhou_gov_杭州市西湖区图书馆: '西湖区',
  hangzhou_gov_余杭区文化馆: '余杭区',
  hangzhou_gov_余杭区图书馆: '余杭区',
  hangzhou_gov_仓前街道图书分馆: '余杭区',
  hangzhou_gov_良渚街道图书分馆: '余杭区',
  hangzhou_gov_仁和街道图书分馆: '余杭区',
  hangzhou_gov_五常街道图书分馆: '余杭区',
  hangzhou_gov_闲林街道图书分馆: '余杭区',
  hangzhou_gov_余杭街道图书分馆: '余杭区',
  hangzhou_gov_中泰街道图书分馆: '余杭区',
  hangzhou_gov_百丈镇图书分馆: '余杭区',
  hangzhou_gov_黄湖镇图书分馆: '余杭区',
  hangzhou_gov_径山镇图书分馆: '余杭区',
  hangzhou_gov_鸬鸟镇图书分馆: '余杭区',
  hangzhou_gov_瓶窑镇图书分馆: '余杭区',
  hangzhou_gov_余杭章太炎故居纪念馆_章太炎研究中心: '余杭区',
  hangzhou_gov_余杭小百花越剧艺术中心_苕溪大剧院: '余杭区',
  hangzhou_gov_余杭区非遗馆: '余杭区',
  hangzhou_gov_良渚街道综合文化站: '余杭区',
  hangzhou_gov_鸬鸟镇乡镇综合文化站: '余杭区',
  hangzhou_gov_黄湖镇综合文化站: '余杭区',
  hangzhou_gov_瓶窑镇综合文化站: '余杭区',
  hangzhou_gov_中泰街道综合文化站: '余杭区',
  hangzhou_gov_径山镇乡镇综合文化站: '余杭区',
  hangzhou_gov_仁和街道综合文化站: '余杭区',
  hangzhou_gov_仓前街道综合文化站: '余杭区',
  hangzhou_gov_闲林街道综合文化站: '余杭区',
  hangzhou_gov_百丈镇综合文化站: '余杭区',
  hangzhou_gov_五常街道综合文化站: '余杭区',
  hangzhou_gov_余杭街道综合文化站: '余杭区',
  hangzhou_gov_杭州市滨江区文化馆: '滨江区',
  hangzhou_gov_杭州市滨江区图书馆: '滨江区',
  hangzhou_gov_杭州市滨江区非物质文化遗产馆: '滨江区',
  hangzhou_gov_区文化馆: '临平区',
  hangzhou_gov_区图书馆: '临平区',
  hangzhou_gov_临平博物馆: '临平区',
  hangzhou_gov_图书馆临平街道分馆_智慧分馆: '临平区',
  hangzhou_gov_图书馆运河街道分馆: '临平区',
  hangzhou_gov_图书馆南苑街道分馆: '临平区',
  hangzhou_gov_图书馆星桥街道分馆: '临平区',
  hangzhou_gov_图书馆乔司街道分馆: '临平区',
  hangzhou_gov_图书馆崇贤街道分馆: '临平区',
  hangzhou_gov_图书馆东湖街道分馆_北沙书房: '临平区',
  hangzhou_gov_图书馆塘栖镇分馆: '临平区',
  shanghai_gov_museum_1: '浦东新区',
  shanghai_gov_museum_2: '浦东新区',
  shanghai_gov_museum_3: '浦东新区',
  shanghai_gov_museum_5: '浦东新区',
  shanghai_gov_museum_6: '浦东新区',
  shanghai_gov_museum_7: '浦东新区',
  shanghai_gov_museum_8: '浦东新区',
  shanghai_gov_museum_9: '浦东新区',
  shanghai_gov_museum_10: '浦东新区',
  shanghai_gov_museum_11: '浦东新区',
  shanghai_gov_museum_12: '浦东新区',
  shanghai_gov_museum_13: '浦东新区',
  shanghai_gov_museum_14: '浦东新区',
  shanghai_gov_museum_15: '浦东新区',
  shanghai_gov_museum_16: '浦东新区',
  shanghai_gov_museum_17: '浦东新区',
  shanghai_gov_museum_18: '浦东新区',
  shanghai_gov_museum_19: '浦东新区',
  shanghai_gov_museum_20: '浦东新区',
  shanghai_gov_museum_21: '浦东新区',
  shanghai_gov_museum_22: '浦东新区',
  shanghai_gov_museum_24: '浦东新区',
  shanghai_gov_museum_27: '黄浦区',
  shanghai_gov_museum_29: '黄浦区',
  shanghai_gov_museum_30: '黄浦区',
  shanghai_gov_museum_31: '黄浦区',
  shanghai_gov_museum_32: '黄浦区',
  shanghai_gov_museum_33: '黄浦区',
  shanghai_gov_museum_34: '黄浦区',
  shanghai_gov_museum_35: '黄浦区',
  shanghai_gov_museum_36: '黄浦区',
  shanghai_gov_museum_37: '黄浦区',
  shanghai_gov_museum_38: '黄浦区',
  shanghai_gov_museum_39: '黄浦区',
  shanghai_gov_museum_41: '黄浦区',
  shanghai_gov_museum_42: '黄浦区',
  shanghai_gov_museum_43: '黄浦区',
  shanghai_gov_museum_44: '黄浦区',
  shanghai_gov_museum_46: '黄浦区',
  shanghai_gov_museum_47: '静安区',
  shanghai_gov_museum_48: '静安区',
  shanghai_gov_museum_49: '静安区',
  shanghai_gov_museum_50: '静安区',
  shanghai_gov_museum_51: '静安区',
  shanghai_gov_museum_52: '静安区',
  shanghai_gov_museum_53: '静安区',
  shanghai_gov_museum_54: '静安区',
  shanghai_gov_museum_55: '静安区',
  shanghai_gov_museum_57: '静安区',
  shanghai_gov_museum_58: '静安区',
  shanghai_gov_museum_59: '静安区',
  shanghai_gov_museum_60: '静安区',
  shanghai_gov_museum_61: '静安区',
  shanghai_gov_museum_62: '静安区',
  shanghai_gov_museum_63: '静安区',
  shanghai_gov_museum_64: '静安区',
  shanghai_gov_museum_65: '徐汇区',
  shanghai_gov_museum_66: '徐汇区',
  shanghai_gov_museum_67: '徐汇区',
  shanghai_gov_museum_68: '徐汇区',
  shanghai_gov_museum_69: '徐汇区',
  shanghai_gov_museum_72: '徐汇区',
  shanghai_gov_museum_73: '徐汇区',
  shanghai_gov_museum_74: '徐汇区',
  shanghai_gov_museum_75: '徐汇区',
  shanghai_gov_museum_76: '徐汇区',
  shanghai_gov_museum_77: '徐汇区',
  shanghai_gov_museum_79: '徐汇区',
  shanghai_gov_museum_80: '徐汇区',
  shanghai_gov_museum_81: '徐汇区',
  shanghai_gov_museum_82: '徐汇区',
  shanghai_gov_museum_83: '徐汇区',
  shanghai_gov_museum_84: '长宁区',
  shanghai_gov_museum_86: '长宁区',
  shanghai_gov_museum_88: '长宁区',
  shanghai_gov_museum_89: '长宁区',
  shanghai_gov_museum_90: '长宁区',
  shanghai_gov_museum_91: '长宁区',
  shanghai_gov_museum_92: '长宁区',
  shanghai_gov_museum_93: '普陀区',
  shanghai_gov_museum_94: '普陀区',
  shanghai_gov_museum_95: '普陀区',
  shanghai_gov_museum_96: '普陀区',
  shanghai_gov_museum_97: '普陀区',
  shanghai_gov_museum_98: '普陀区',
  shanghai_gov_museum_99: '普陀区',
  shanghai_gov_museum_100: '虹口区',
  shanghai_gov_museum_101: '虹口区',
  shanghai_gov_museum_102: '虹口区',
  shanghai_gov_museum_103: '虹口区',
  shanghai_gov_museum_104: '虹口区',
  shanghai_gov_museum_105: '虹口区',
  shanghai_gov_museum_106: '虹口区',
  shanghai_gov_museum_107: '虹口区',
  shanghai_gov_museum_108: '杨浦区',
  shanghai_gov_museum_109: '杨浦区',
  shanghai_gov_museum_110: '杨浦区',
  shanghai_gov_museum_111: '杨浦区',
  shanghai_gov_museum_112: '杨浦区',
  shanghai_gov_museum_113: '杨浦区',
  shanghai_gov_museum_114: '杨浦区',
  shanghai_gov_museum_115: '杨浦区',
  shanghai_gov_museum_116: '杨浦区',
  shanghai_gov_museum_117: '杨浦区',
  shanghai_gov_museum_118: '杨浦区',
  shanghai_gov_museum_119: '宝山区',
  shanghai_gov_museum_120: '宝山区',
  shanghai_gov_museum_122: '宝山区',
  shanghai_gov_museum_123: '宝山区',
  shanghai_gov_museum_124: '宝山区',
  shanghai_gov_museum_125: '宝山区',
  shanghai_gov_museum_126: '宝山区',
  shanghai_gov_museum_127: '宝山区',
  shanghai_gov_museum_128: '宝山区',
  shanghai_gov_museum_129: '宝山区',
  shanghai_gov_museum_130: '宝山区',
  shanghai_gov_museum_131: '闵行区',
  shanghai_gov_museum_132: '闵行区',
  shanghai_gov_museum_133: '闵行区',
  shanghai_gov_museum_135: '闵行区',
  shanghai_gov_museum_136: '闵行区',
  shanghai_gov_museum_137: '闵行区',
  shanghai_gov_museum_138: '闵行区',
  shanghai_gov_museum_139: '闵行区',
  shanghai_gov_museum_141: '嘉定区',
  shanghai_gov_museum_142: '嘉定区',
  shanghai_gov_museum_144: '嘉定区',
  shanghai_gov_museum_145: '嘉定区',
  shanghai_gov_museum_146: '嘉定区',
  shanghai_gov_museum_147: '嘉定区',
  shanghai_gov_museum_148: '金山区',
  shanghai_gov_museum_149: '金山区',
  shanghai_gov_museum_150: '金山区',
  shanghai_gov_museum_151: '松江区',
  shanghai_gov_museum_152: '松江区',
  shanghai_gov_museum_153: '松江区',
  shanghai_gov_museum_154: '松江区',
  shanghai_gov_museum_155: '松江区',
  shanghai_gov_museum_156: '松江区',
  shanghai_gov_museum_157: '松江区',
  shanghai_gov_museum_158: '松江区',
  shanghai_gov_museum_159: '青浦区',
  shanghai_gov_museum_160: '青浦区',
  shanghai_gov_museum_161: '青浦区',
  shanghai_gov_museum_162: '青浦区',
  shanghai_gov_museum_163: '青浦区',
  shanghai_gov_museum_164: '青浦区',
  shanghai_gov_museum_165: '青浦区',
  shanghai_gov_museum_166: '奉贤区',
  shanghai_gov_museum_167: '奉贤区',
  shanghai_gov_museum_168: '奉贤区',
  shanghai_gov_museum_169: '奉贤区',
  shanghai_gov_museum_170: '奉贤区',
  shanghai_gov_museum_171: '崇明区',
  shanghai_gov_museum_172: '崇明区',
  shanghai_gov_museum_173: '崇明区',
  shanghai_gov_museum_174: '崇明区',
  shanghai_gov_library_1: '上海市',
  shanghai_gov_library_2: '上海市',
  shanghai_gov_library_3: '上海市',
  shanghai_gov_library_4: '上海市',
  shanghai_gov_library_5: '浦东新区',
  shanghai_gov_library_6: '浦东新区',
  shanghai_gov_library_7: '浦东新区',
  shanghai_gov_library_8: '浦东新区',
  shanghai_gov_library_9: '浦东新区',
  shanghai_gov_library_10: '浦东新区',
  shanghai_gov_library_11: '浦东新区',
  shanghai_gov_library_12: '浦东新区',
  shanghai_gov_library_13: '浦东新区',
  shanghai_gov_library_14: '浦东新区',
  shanghai_gov_library_15: '浦东新区',
  shanghai_gov_library_16: '浦东新区',
  shanghai_gov_library_17: '浦东新区',
  shanghai_gov_library_18: '浦东新区',
  shanghai_gov_library_19: '浦东新区',
  shanghai_gov_library_20: '浦东新区',
  shanghai_gov_library_21: '浦东新区',
  shanghai_gov_library_22: '浦东新区',
  shanghai_gov_library_23: '浦东新区',
  shanghai_gov_library_24: '浦东新区',
  shanghai_gov_library_25: '浦东新区',
  shanghai_gov_library_26: '浦东新区',
  shanghai_gov_library_27: '浦东新区',
  shanghai_gov_library_28: '浦东新区',
  shanghai_gov_library_29: '浦东新区',
  shanghai_gov_library_30: '浦东新区',
  shanghai_gov_library_31: '浦东新区',
  shanghai_gov_library_32: '浦东新区',
  shanghai_gov_library_33: '浦东新区',
  shanghai_gov_library_34: '浦东新区',
  shanghai_gov_library_35: '浦东新区',
  shanghai_gov_library_36: '浦东新区',
  shanghai_gov_library_37: '浦东新区',
  shanghai_gov_library_38: '浦东新区',
  shanghai_gov_library_39: '浦东新区',
  shanghai_gov_library_40: '浦东新区',
  shanghai_gov_library_41: '浦东新区',
  shanghai_gov_library_42: '浦东新区',
  shanghai_gov_library_43: '浦东新区',
  shanghai_gov_library_44: '浦东新区',
  shanghai_gov_library_45: '浦东新区',
  shanghai_gov_library_46: '浦东新区',
  shanghai_gov_library_47: '浦东新区',
  shanghai_gov_library_48: '浦东新区',
  shanghai_gov_library_49: '浦东新区',
  shanghai_gov_library_50: '浦东新区',
  shanghai_gov_library_51: '浦东新区',
  shanghai_gov_library_52: '浦东新区',
  shanghai_gov_library_53: '浦东新区',
  shanghai_gov_library_54: '浦东新区',
  shanghai_gov_library_55: '浦东新区',
  shanghai_gov_library_56: '浦东新区',
  shanghai_gov_library_57: '黄浦区',
  shanghai_gov_library_58: '黄浦区',
  shanghai_gov_library_59: '黄浦区',
  shanghai_gov_library_60: '黄浦区',
  shanghai_gov_library_61: '黄浦区',
  shanghai_gov_library_62: '黄浦区',
  shanghai_gov_library_63: '黄浦区',
  shanghai_gov_library_64: '黄浦区',
  shanghai_gov_library_65: '黄浦区',
  shanghai_gov_library_66: '黄浦区',
  shanghai_gov_library_67: '黄浦区',
  shanghai_gov_library_68: '黄浦区',
  shanghai_gov_library_69: '静安区',
  shanghai_gov_library_70: '静安区',
  shanghai_gov_library_71: '静安区',
  shanghai_gov_library_72: '静安区',
  shanghai_gov_library_73: '静安区',
  shanghai_gov_library_74: '静安区',
  shanghai_gov_library_75: '静安区',
  shanghai_gov_library_76: '静安区',
  shanghai_gov_library_77: '静安区',
  shanghai_gov_library_78: '静安区',
  shanghai_gov_library_79: '静安区',
  shanghai_gov_library_80: '静安区',
  shanghai_gov_library_81: '静安区',
  shanghai_gov_library_82: '静安区',
  shanghai_gov_library_83: '静安区',
  shanghai_gov_library_84: '静安区',
  shanghai_gov_library_85: '静安区',
  shanghai_gov_library_86: '静安区',
  shanghai_gov_library_87: '静安区',
  shanghai_gov_library_88: '静安区',
  shanghai_gov_library_89: '静安区',
  shanghai_gov_library_90: '静安区',
  shanghai_gov_library_91: '静安区',
  shanghai_gov_library_92: '静安区',
  shanghai_gov_library_93: '静安区',
  shanghai_gov_library_94: '徐汇区',
  shanghai_gov_library_95: '徐汇区',
  shanghai_gov_library_96: '徐汇区',
  shanghai_gov_library_97: '徐汇区',
  shanghai_gov_library_98: '徐汇区',
  shanghai_gov_library_99: '徐汇区',
  shanghai_gov_library_100: '徐汇区',
  shanghai_gov_library_101: '徐汇区',
  shanghai_gov_library_102: '徐汇区',
  shanghai_gov_library_103: '徐汇区',
  shanghai_gov_library_104: '徐汇区',
  shanghai_gov_library_105: '徐汇区',
  shanghai_gov_library_106: '徐汇区',
  shanghai_gov_library_107: '徐汇区',
  shanghai_gov_library_108: '徐汇区',
  shanghai_gov_library_109: '长宁区',
  shanghai_gov_library_110: '长宁区',
  shanghai_gov_library_111: '长宁区',
  shanghai_gov_library_112: '长宁区',
  shanghai_gov_library_113: '长宁区',
  shanghai_gov_library_114: '长宁区',
  shanghai_gov_library_115: '长宁区',
  shanghai_gov_library_116: '长宁区',
  shanghai_gov_library_117: '长宁区',
  shanghai_gov_library_118: '长宁区',
  shanghai_gov_library_119: '长宁区',
  shanghai_gov_library_120: '长宁区',
  shanghai_gov_library_121: '长宁区',
  shanghai_gov_library_122: '长宁区',
  shanghai_gov_library_124: '普陀区',
  shanghai_gov_library_125: '普陀区',
  shanghai_gov_library_126: '普陀区',
  shanghai_gov_library_127: '普陀区',
  shanghai_gov_library_128: '普陀区',
  shanghai_gov_library_129: '普陀区',
  shanghai_gov_library_130: '普陀区',
  shanghai_gov_library_131: '普陀区',
  shanghai_gov_library_132: '普陀区',
  shanghai_gov_library_133: '普陀区',
  shanghai_gov_library_134: '虹口区',
  shanghai_gov_library_135: '虹口区',
  shanghai_gov_library_136: '虹口区',
  shanghai_gov_library_137: '虹口区',
  shanghai_gov_library_138: '虹口区',
  shanghai_gov_library_139: '虹口区',
  shanghai_gov_library_140: '虹口区',
  shanghai_gov_library_141: '虹口区',
  shanghai_gov_library_142: '虹口区',
  shanghai_gov_library_143: '虹口区',
  shanghai_gov_library_144: '虹口区',
  shanghai_gov_library_145: '虹口区',
  shanghai_gov_library_147: '杨浦区',
  shanghai_gov_library_148: '杨浦区',
  shanghai_gov_library_149: '杨浦区',
  shanghai_gov_library_150: '杨浦区',
  shanghai_gov_library_151: '杨浦区',
  shanghai_gov_library_152: '杨浦区',
  shanghai_gov_library_153: '杨浦区',
  shanghai_gov_library_154: '杨浦区',
  shanghai_gov_library_155: '杨浦区',
  shanghai_gov_library_156: '杨浦区',
  shanghai_gov_library_157: '杨浦区',
  shanghai_gov_library_158: '杨浦区',
  shanghai_gov_library_159: '杨浦区',
  shanghai_gov_library_160: '杨浦区',
  shanghai_gov_library_161: '杨浦区',
  shanghai_gov_library_162: '杨浦区',
  shanghai_gov_library_163: '杨浦区',
  shanghai_gov_library_164: '杨浦区',
  shanghai_gov_library_166: '宝山区',
  shanghai_gov_library_167: '宝山区',
  shanghai_gov_library_168: '宝山区',
  shanghai_gov_library_169: '宝山区',
  shanghai_gov_library_170: '宝山区',
  shanghai_gov_library_171: '宝山区',
  shanghai_gov_library_172: '宝山区',
  shanghai_gov_library_173: '宝山区',
  shanghai_gov_library_174: '宝山区',
  shanghai_gov_library_175: '宝山区',
  shanghai_gov_library_176: '宝山区',
  shanghai_gov_library_177: '宝山区',
  shanghai_gov_library_178: '宝山区',
  shanghai_gov_library_179: '宝山区',
  shanghai_gov_library_180: '宝山区',
  shanghai_gov_library_181: '宝山区',
  shanghai_gov_library_182: '宝山区',
  shanghai_gov_library_183: '宝山区',
  shanghai_gov_library_184: '宝山区',
  shanghai_gov_library_185: '宝山区',
  shanghai_gov_library_186: '宝山区',
  shanghai_gov_library_188: '闵行区',
  shanghai_gov_library_189: '闵行区',
  shanghai_gov_library_190: '闵行区',
  shanghai_gov_library_191: '闵行区',
  shanghai_gov_library_192: '闵行区',
  shanghai_gov_library_193: '闵行区',
  shanghai_gov_library_194: '闵行区',
  shanghai_gov_library_195: '闵行区',
  shanghai_gov_library_196: '闵行区',
  shanghai_gov_library_197: '闵行区',
  shanghai_gov_library_198: '闵行区',
  shanghai_gov_library_199: '闵行区',
  shanghai_gov_library_200: '闵行区',
  shanghai_gov_library_201: '闵行区',
  shanghai_gov_library_202: '闵行区',
  shanghai_gov_library_203: '闵行区',
  shanghai_gov_library_204: '闵行区',
  shanghai_gov_library_205: '嘉定区',
  shanghai_gov_library_206: '嘉定区',
  shanghai_gov_library_207: '嘉定区',
  shanghai_gov_library_208: '嘉定区',
  shanghai_gov_library_209: '嘉定区',
  shanghai_gov_library_210: '嘉定区',
  shanghai_gov_library_211: '嘉定区',
  shanghai_gov_library_212: '嘉定区',
  shanghai_gov_library_213: '嘉定区',
  shanghai_gov_library_214: '嘉定区',
  shanghai_gov_library_215: '嘉定区',
  shanghai_gov_library_216: '嘉定区',
  shanghai_gov_library_217: '嘉定区',
  shanghai_gov_library_218: '嘉定区',
  shanghai_gov_library_219: '嘉定区',
  shanghai_gov_library_220: '嘉定区',
  shanghai_gov_library_221: '嘉定区',
  shanghai_gov_library_222: '嘉定区',
  shanghai_gov_library_223: '嘉定区',
  shanghai_gov_library_224: '金山区',
  shanghai_gov_library_225: '金山区',
  shanghai_gov_library_226: '金山区',
  shanghai_gov_library_227: '金山区',
  shanghai_gov_library_228: '金山区',
  shanghai_gov_library_229: '金山区',
  shanghai_gov_library_230: '金山区',
  shanghai_gov_library_231: '金山区',
  shanghai_gov_library_232: '金山区',
  shanghai_gov_library_233: '金山区',
  shanghai_gov_library_234: '金山区',
  shanghai_gov_library_235: '金山区',
  shanghai_gov_library_236: '金山区',
  shanghai_gov_library_237: '金山区',
  shanghai_gov_library_238: '金山区',
  shanghai_gov_library_239: '金山区',
  shanghai_gov_library_240: '松江区',
  shanghai_gov_library_241: '松江区',
  shanghai_gov_library_242: '松江区',
  shanghai_gov_library_243: '松江区',
  shanghai_gov_library_244: '松江区',
  shanghai_gov_library_245: '松江区',
  shanghai_gov_library_246: '松江区',
  shanghai_gov_library_247: '松江区',
  shanghai_gov_library_248: '松江区',
  shanghai_gov_library_249: '松江区',
  shanghai_gov_library_250: '松江区',
  shanghai_gov_library_251: '松江区',
  shanghai_gov_library_252: '松江区',
  shanghai_gov_library_253: '松江区',
  shanghai_gov_library_254: '松江区',
  shanghai_gov_library_255: '松江区',
  shanghai_gov_library_256: '松江区',
  shanghai_gov_library_257: '松江区',
  shanghai_gov_library_258: '松江区',
  shanghai_gov_library_259: '松江区',
  shanghai_gov_library_260: '松江区',
  shanghai_gov_library_261: '青浦区',
  shanghai_gov_library_262: '青浦区',
  shanghai_gov_library_263: '青浦区',
  shanghai_gov_library_264: '青浦区',
  shanghai_gov_library_265: '青浦区',
  shanghai_gov_library_266: '青浦区',
  shanghai_gov_library_267: '青浦区',
  shanghai_gov_library_268: '青浦区',
  shanghai_gov_library_269: '青浦区',
  shanghai_gov_library_270: '青浦区',
  shanghai_gov_library_271: '青浦区',
  shanghai_gov_library_272: '青浦区',
  shanghai_gov_library_273: '青浦区',
  shanghai_gov_library_274: '青浦区',
  shanghai_gov_library_275: '青浦区',
  shanghai_gov_library_276: '青浦区',
  shanghai_gov_library_277: '青浦区',
  shanghai_gov_library_278: '青浦区',
  shanghai_gov_library_279: '奉贤区',
  shanghai_gov_library_280: '奉贤区',
  shanghai_gov_library_281: '奉贤区',
  shanghai_gov_library_282: '奉贤区',
  shanghai_gov_library_283: '奉贤区',
  shanghai_gov_library_284: '奉贤区',
  shanghai_gov_library_285: '奉贤区',
  shanghai_gov_library_286: '奉贤区',
  shanghai_gov_library_287: '奉贤区',
  shanghai_gov_library_288: '奉贤区',
  shanghai_gov_library_289: '奉贤区',
  shanghai_gov_library_290: '奉贤区',
  shanghai_gov_library_291: '奉贤区',
  shanghai_gov_library_292: '奉贤区',
  shanghai_gov_library_293: '崇明区',
  shanghai_gov_library_294: '崇明区',
  shanghai_gov_library_295: '崇明区',
  shanghai_gov_library_296: '崇明区',
  shanghai_gov_library_297: '崇明区',
  shanghai_gov_library_298: '崇明区',
  shanghai_gov_library_299: '崇明区',
  shanghai_gov_library_300: '崇明区',
  shanghai_gov_library_301: '崇明区',
  shanghai_gov_library_302: '崇明区',
  shanghai_gov_library_303: '崇明区',
  shanghai_gov_library_304: '崇明区',
  shanghai_gov_library_305: '崇明区',
  shanghai_gov_library_306: '崇明区',
  shanghai_gov_library_307: '崇明区',
  shanghai_gov_library_308: '崇明区',
  shanghai_gov_library_309: '崇明区',
  shanghai_gov_library_310: '崇明区',
  shanghai_gov_library_311: '崇明区',
  shanghai_gov_art_3: '浦东新区',
  shanghai_gov_art_5: '浦东新区',
  shanghai_gov_art_6: '浦东新区',
  shanghai_gov_art_7: '浦东新区',
  shanghai_gov_art_8: '浦东新区',
  shanghai_gov_art_9: '浦东新区',
  shanghai_gov_art_10: '浦东新区',
  shanghai_gov_art_11: '浦东新区',
  shanghai_gov_art_12: '浦东新区',
  shanghai_gov_art_13: '浦东新区',
  shanghai_gov_art_14: '浦东新区',
  shanghai_gov_art_15: '浦东新区',
  shanghai_gov_art_16: '浦东新区',
  shanghai_gov_art_18: '黄浦区',
  shanghai_gov_art_19: '黄浦区',
  shanghai_gov_art_20: '黄浦区',
  shanghai_gov_art_21: '黄浦区',
  shanghai_gov_art_22: '黄浦区',
  shanghai_gov_art_23: '黄浦区',
  shanghai_gov_art_24: '黄浦区',
  shanghai_gov_art_25: '黄浦区',
  shanghai_gov_art_26: '静安区',
  shanghai_gov_art_27: '静安区',
  shanghai_gov_art_28: '静安区',
  shanghai_gov_art_29: '静安区',
  shanghai_gov_art_30: '静安区',
  shanghai_gov_art_31: '静安区',
  shanghai_gov_art_32: '静安区',
  shanghai_gov_art_33: '徐汇区',
  shanghai_gov_art_34: '徐汇区',
  shanghai_gov_art_35: '徐汇区',
  shanghai_gov_art_36: '徐汇区',
  shanghai_gov_art_37: '徐汇区',
  shanghai_gov_art_38: '徐汇区',
  shanghai_gov_art_39: '徐汇区',
  shanghai_gov_art_40: '徐汇区',
  shanghai_gov_art_41: '长宁区',
  shanghai_gov_art_42: '长宁区',
  shanghai_gov_art_43: '长宁区',
  shanghai_gov_art_44: '长宁区',
  shanghai_gov_art_45: '长宁区',
  shanghai_gov_art_46: '长宁区',
  shanghai_gov_art_47: '长宁区',
  shanghai_gov_art_48: '长宁区',
  shanghai_gov_art_49: '普陀区',
  shanghai_gov_art_50: '普陀区',
  shanghai_gov_art_51: '虹口区',
  shanghai_gov_art_52: '虹口区',
  shanghai_gov_art_53: '虹口区',
  shanghai_gov_art_54: '虹口区',
  shanghai_gov_art_55: '杨浦区',
  shanghai_gov_art_56: '杨浦区',
  shanghai_gov_art_57: '杨浦区',
  shanghai_gov_art_58: '宝山区',
  shanghai_gov_art_59: '宝山区',
  shanghai_gov_art_60: '宝山区',
  shanghai_gov_art_61: '闵行区',
  shanghai_gov_art_62: '闵行区',
  shanghai_gov_art_63: '闵行区',
  shanghai_gov_art_64: '闵行区',
  shanghai_gov_art_65: '闵行区',
  shanghai_gov_art_66: '闵行区',
  shanghai_gov_art_67: '闵行区',
  shanghai_gov_art_68: '闵行区',
  shanghai_gov_art_69: '闵行区',
  shanghai_gov_art_70: '嘉定区',
  shanghai_gov_art_71: '嘉定区',
  shanghai_gov_art_72: '嘉定区',
  shanghai_gov_art_73: '嘉定区',
  shanghai_gov_art_74: '嘉定区',
  shanghai_gov_art_75: '嘉定区',
  shanghai_gov_art_76: '嘉定区',
  shanghai_gov_art_77: '金山区',
  shanghai_gov_art_78: '金山区',
  shanghai_gov_art_79: '松江区',
  shanghai_gov_art_80: '松江区',
  shanghai_gov_art_81: '松江区',
  shanghai_gov_art_82: '松江区',
  shanghai_gov_art_83: '松江区',
  shanghai_gov_art_84: '松江区',
  shanghai_gov_art_85: '松江区',
  shanghai_gov_art_86: '松江区',
  shanghai_gov_art_87: '松江区',
  shanghai_gov_art_88: '松江区',
  shanghai_gov_art_89: '松江区',
  shanghai_gov_art_90: '松江区',
  shanghai_gov_art_91: '青浦区',
  shanghai_gov_art_92: '青浦区',
  shanghai_gov_art_93: '青浦区',
  shanghai_gov_art_94: '青浦区',
  shanghai_gov_art_95: '青浦区',
  shanghai_gov_art_96: '奉贤区',
  shanghai_gov_art_97: '崇明区',
  shanghai_gov_culture_2: '浦东新区',
  shanghai_gov_culture_3: '浦东新区',
  shanghai_gov_culture_4: '浦东新区',
  shanghai_gov_culture_5: '浦东新区',
  shanghai_gov_culture_6: '浦东新区',
  shanghai_gov_culture_7: '浦东新区',
  shanghai_gov_culture_8: '黄浦区',
  shanghai_gov_culture_9: '徐汇区',
  shanghai_gov_culture_10: '长宁区',
  shanghai_gov_culture_12: '静安区',
  shanghai_gov_culture_13: '静安区',
  shanghai_gov_culture_14: '虹口区',
  shanghai_gov_culture_15: '杨浦区',
  shanghai_gov_culture_16: '普陀区',
  shanghai_gov_culture_18: '闵行区',
  shanghai_gov_culture_20: '金山区',
  shanghai_gov_culture_21: '松江区',
  shanghai_gov_culture_22: '青浦区',
  shanghai_gov_culture_23: '奉贤区',
  shanghai_gov_culture_24: '崇明区',
  shanghai_gov_community_1: '浦东新区',
  shanghai_gov_community_2: '浦东新区',
  shanghai_gov_community_3: '浦东新区',
  shanghai_gov_community_4: '浦东新区',
  shanghai_gov_community_5: '浦东新区',
  shanghai_gov_community_6: '浦东新区',
  shanghai_gov_community_7: '浦东新区',
  shanghai_gov_community_8: '浦东新区',
  shanghai_gov_community_9: '浦东新区',
  shanghai_gov_community_10: '浦东新区',
  shanghai_gov_community_11: '浦东新区',
  shanghai_gov_community_12: '浦东新区',
  shanghai_gov_community_13: '浦东新区',
  shanghai_gov_community_14: '浦东新区',
  shanghai_gov_community_15: '浦东新区',
  shanghai_gov_community_16: '浦东新区',
  shanghai_gov_community_17: '浦东新区',
  shanghai_gov_community_18: '浦东新区',
  shanghai_gov_community_20: '浦东新区',
  shanghai_gov_community_21: '浦东新区',
  shanghai_gov_community_22: '浦东新区',
  shanghai_gov_community_23: '浦东新区',
  shanghai_gov_community_24: '浦东新区',
  shanghai_gov_community_25: '浦东新区',
  shanghai_gov_community_26: '浦东新区',
  shanghai_gov_community_27: '浦东新区',
  shanghai_gov_community_28: '浦东新区',
  shanghai_gov_community_29: '浦东新区',
  shanghai_gov_community_30: '浦东新区',
  shanghai_gov_community_31: '浦东新区',
  shanghai_gov_community_32: '浦东新区',
  shanghai_gov_community_33: '浦东新区',
  shanghai_gov_community_34: '浦东新区',
  shanghai_gov_community_35: '浦东新区',
  shanghai_gov_community_36: '浦东新区',
  shanghai_gov_community_37: '浦东新区',
  shanghai_gov_community_38: '浦东新区',
  shanghai_gov_community_39: '浦东新区',
  shanghai_gov_community_40: '浦东新区',
  shanghai_gov_community_41: '浦东新区',
  shanghai_gov_community_42: '浦东新区',
  shanghai_gov_community_43: '浦东新区',
  shanghai_gov_community_44: '浦东新区',
  shanghai_gov_community_45: '浦东新区',
  shanghai_gov_community_46: '浦东新区',
  shanghai_gov_community_47: '浦东新区',
  shanghai_gov_community_48: '浦东新区',
  shanghai_gov_community_49: '黄浦区',
  shanghai_gov_community_50: '黄浦区',
  shanghai_gov_community_51: '黄浦区',
  shanghai_gov_community_52: '黄浦区',
  shanghai_gov_community_53: '黄浦区',
  shanghai_gov_community_54: '黄浦区',
  shanghai_gov_community_55: '黄浦区',
  shanghai_gov_community_56: '黄浦区',
  shanghai_gov_community_57: '黄浦区',
  shanghai_gov_community_58: '黄浦区',
  shanghai_gov_community_59: '静安区',
  shanghai_gov_community_60: '静安区',
  shanghai_gov_community_61: '静安区',
  shanghai_gov_community_62: '静安区',
  shanghai_gov_community_63: '静安区',
  shanghai_gov_community_64: '静安区',
  shanghai_gov_community_65: '静安区',
  shanghai_gov_community_66: '静安区',
  shanghai_gov_community_67: '静安区',
  shanghai_gov_community_68: '静安区',
  shanghai_gov_community_69: '静安区',
  shanghai_gov_community_70: '静安区',
  shanghai_gov_community_71: '静安区',
  shanghai_gov_community_72: '静安区',
  shanghai_gov_community_73: '静安区',
  shanghai_gov_community_74: '徐汇区',
  shanghai_gov_community_75: '徐汇区',
  shanghai_gov_community_76: '徐汇区',
  shanghai_gov_community_77: '徐汇区',
  shanghai_gov_community_78: '徐汇区',
  shanghai_gov_community_79: '徐汇区',
  shanghai_gov_community_80: '徐汇区',
  shanghai_gov_community_81: '徐汇区',
  shanghai_gov_community_82: '徐汇区',
  shanghai_gov_community_83: '徐汇区',
  shanghai_gov_community_84: '徐汇区',
  shanghai_gov_community_85: '徐汇区',
  shanghai_gov_community_86: '徐汇区',
  shanghai_gov_community_87: '徐汇区',
  shanghai_gov_community_88: '徐汇区',
  shanghai_gov_community_89: '长宁区',
  shanghai_gov_community_90: '长宁区',
  shanghai_gov_community_91: '长宁区',
  shanghai_gov_community_92: '长宁区',
  shanghai_gov_community_93: '长宁区',
  shanghai_gov_community_94: '长宁区',
  shanghai_gov_community_95: '长宁区',
  shanghai_gov_community_96: '长宁区',
  shanghai_gov_community_97: '长宁区',
  shanghai_gov_community_98: '长宁区',
  shanghai_gov_community_99: '长宁区',
  shanghai_gov_community_100: '长宁区',
  shanghai_gov_community_101: '普陀区',
  shanghai_gov_community_102: '普陀区',
  shanghai_gov_community_103: '普陀区',
  shanghai_gov_community_104: '普陀区',
  shanghai_gov_community_105: '普陀区',
  shanghai_gov_community_106: '普陀区',
  shanghai_gov_community_107: '普陀区',
  shanghai_gov_community_108: '普陀区',
  shanghai_gov_community_109: '普陀区',
  shanghai_gov_community_110: '普陀区',
  shanghai_gov_community_111: '虹口区',
  shanghai_gov_community_112: '虹口区',
  shanghai_gov_community_113: '虹口区',
  shanghai_gov_community_114: '虹口区',
  shanghai_gov_community_115: '虹口区',
  shanghai_gov_community_116: '虹口区',
  shanghai_gov_community_117: '虹口区',
  shanghai_gov_community_118: '虹口区',
  shanghai_gov_community_119: '虹口区',
  shanghai_gov_community_120: '杨浦区',
  shanghai_gov_community_121: '杨浦区',
  shanghai_gov_community_122: '杨浦区',
  shanghai_gov_community_123: '杨浦区',
  shanghai_gov_community_125: '杨浦区',
  shanghai_gov_community_126: '杨浦区',
  shanghai_gov_community_127: '杨浦区',
  shanghai_gov_community_128: '杨浦区',
  shanghai_gov_community_129: '杨浦区',
  shanghai_gov_community_130: '杨浦区',
  shanghai_gov_community_131: '杨浦区',
  shanghai_gov_community_133: '杨浦区',
  shanghai_gov_community_134: '杨浦区',
  shanghai_gov_community_135: '杨浦区',
  shanghai_gov_community_136: '杨浦区',
  shanghai_gov_community_137: '杨浦区',
  shanghai_gov_community_138: '杨浦区',
  shanghai_gov_community_139: '杨浦区',
  shanghai_gov_community_140: '杨浦区',
  shanghai_gov_community_141: '宝山区',
  shanghai_gov_community_142: '宝山区',
  shanghai_gov_community_145: '宝山区',
  shanghai_gov_community_146: '宝山区',
  shanghai_gov_community_147: '宝山区',
  shanghai_gov_community_148: '宝山区',
  shanghai_gov_community_149: '宝山区',
  shanghai_gov_community_150: '宝山区',
  shanghai_gov_community_151: '宝山区',
  shanghai_gov_community_152: '宝山区',
  shanghai_gov_community_153: '宝山区',
  shanghai_gov_community_154: '宝山区',
  shanghai_gov_community_155: '宝山区',
  shanghai_gov_community_156: '宝山区',
  shanghai_gov_community_157: '宝山区',
  shanghai_gov_community_158: '宝山区',
  shanghai_gov_community_159: '宝山区',
  shanghai_gov_community_160: '宝山区',
  shanghai_gov_community_161: '宝山区',
  shanghai_gov_community_162: '宝山区',
  shanghai_gov_community_163: '闵行区',
  shanghai_gov_community_164: '闵行区',
  shanghai_gov_community_165: '闵行区',
  shanghai_gov_community_166: '闵行区',
  shanghai_gov_community_167: '闵行区',
  shanghai_gov_community_168: '闵行区',
  shanghai_gov_community_169: '闵行区',
  shanghai_gov_community_170: '闵行区',
  shanghai_gov_community_171: '闵行区',
  shanghai_gov_community_172: '闵行区',
  shanghai_gov_community_173: '闵行区',
  shanghai_gov_community_174: '闵行区',
  shanghai_gov_community_175: '闵行区',
  shanghai_gov_community_176: '闵行区',
  shanghai_gov_community_177: '闵行区',
  shanghai_gov_community_178: '闵行区',
  shanghai_gov_community_179: '闵行区',
  shanghai_gov_community_180: '嘉定区',
  shanghai_gov_community_181: '嘉定区',
  shanghai_gov_community_182: '嘉定区',
  shanghai_gov_community_183: '嘉定区',
  shanghai_gov_community_184: '嘉定区',
  shanghai_gov_community_185: '嘉定区',
  shanghai_gov_community_186: '嘉定区',
  shanghai_gov_community_187: '嘉定区',
  shanghai_gov_community_188: '嘉定区',
  shanghai_gov_community_189: '嘉定区',
  shanghai_gov_community_190: '嘉定区',
  shanghai_gov_community_191: '嘉定区',
  shanghai_gov_community_192: '嘉定区',
  shanghai_gov_community_193: '嘉定区',
  shanghai_gov_community_194: '金山区',
  shanghai_gov_community_195: '金山区',
  shanghai_gov_community_196: '金山区',
  shanghai_gov_community_197: '金山区',
  shanghai_gov_community_198: '金山区',
  shanghai_gov_community_199: '金山区',
  shanghai_gov_community_200: '金山区',
  shanghai_gov_community_201: '金山区',
  shanghai_gov_community_202: '金山区',
  shanghai_gov_community_203: '金山区',
  shanghai_gov_community_204: '金山区',
  shanghai_gov_community_205: '金山区',
  shanghai_gov_community_206: '金山区',
  shanghai_gov_community_207: '金山区',
  shanghai_gov_community_208: '金山区',
  shanghai_gov_community_209: '松江区',
  shanghai_gov_community_210: '松江区',
  shanghai_gov_community_211: '松江区',
  shanghai_gov_community_212: '松江区',
  shanghai_gov_community_213: '松江区',
  shanghai_gov_community_214: '松江区',
  shanghai_gov_community_215: '松江区',
  shanghai_gov_community_216: '松江区',
  shanghai_gov_community_217: '松江区',
  shanghai_gov_community_218: '松江区',
  shanghai_gov_community_219: '松江区',
  shanghai_gov_community_220: '松江区',
  shanghai_gov_community_221: '松江区',
  shanghai_gov_community_222: '松江区',
  shanghai_gov_community_223: '松江区',
  shanghai_gov_community_224: '松江区',
  shanghai_gov_community_225: '松江区',
  shanghai_gov_community_226: '松江区',
  shanghai_gov_community_227: '松江区',
  shanghai_gov_community_228: '青浦区',
  shanghai_gov_community_229: '青浦区',
  shanghai_gov_community_230: '青浦区',
  shanghai_gov_community_231: '青浦区',
  shanghai_gov_community_232: '青浦区',
  shanghai_gov_community_233: '青浦区',
  shanghai_gov_community_234: '青浦区',
  shanghai_gov_community_235: '青浦区',
  shanghai_gov_community_236: '青浦区',
  shanghai_gov_community_237: '青浦区',
  shanghai_gov_community_238: '青浦区',
  shanghai_gov_community_239: '青浦区',
  shanghai_gov_community_240: '青浦区',
  shanghai_gov_community_241: '青浦区',
  shanghai_gov_community_242: '青浦区',
  shanghai_gov_community_243: '青浦区',
  shanghai_gov_community_244: '青浦区',
  shanghai_gov_community_245: '青浦区',
  shanghai_gov_community_246: '青浦区',
  shanghai_gov_community_247: '奉贤区',
  shanghai_gov_community_248: '奉贤区',
  shanghai_gov_community_249: '奉贤区',
  shanghai_gov_community_250: '奉贤区',
  shanghai_gov_community_251: '奉贤区',
  shanghai_gov_community_252: '奉贤区',
  shanghai_gov_community_253: '奉贤区',
  shanghai_gov_community_254: '奉贤区',
  shanghai_gov_community_255: '奉贤区',
  shanghai_gov_community_256: '奉贤区',
  shanghai_gov_community_257: '奉贤区',
  shanghai_gov_community_258: '奉贤区',
  shanghai_gov_community_259: '奉贤区',
  shanghai_gov_community_260: '奉贤区',
  shanghai_gov_community_261: '奉贤区',
  shanghai_gov_community_262: '奉贤区',
  shanghai_gov_community_263: '奉贤区',
  shanghai_gov_community_264: '崇明区',
  shanghai_gov_community_265: '崇明区',
  shanghai_gov_community_266: '崇明区',
  shanghai_gov_community_267: '崇明区',
  shanghai_gov_community_268: '崇明区',
  shanghai_gov_community_269: '崇明区',
  shanghai_gov_community_270: '崇明区',
  shanghai_gov_community_271: '崇明区',
  shanghai_gov_community_272: '崇明区',
  shanghai_gov_community_273: '崇明区',
  shanghai_gov_community_274: '崇明区',
  shanghai_gov_community_275: '崇明区',
  shanghai_gov_community_276: '崇明区',
  shanghai_gov_community_277: '崇明区',
  shanghai_gov_community_278: '崇明区',
  shanghai_gov_community_279: '崇明区',
  shanghai_gov_community_280: '崇明区',
  shanghai_gov_community_281: '崇明区',
  shanghai_gov_theatre_1: '黄浦',
  shanghai_gov_theatre_2: '黄浦',
  shanghai_gov_theatre_3: '黄浦',
  shanghai_gov_theatre_4: '黄浦',
  shanghai_gov_theatre_5: '黄浦',
  shanghai_gov_theatre_6: '黄浦',
  shanghai_gov_theatre_7: '黄浦',
  shanghai_gov_theatre_8: '黄浦',
  shanghai_gov_theatre_9: '黄浦',
  shanghai_gov_theatre_10: '黄浦',
  shanghai_gov_theatre_11: '黄浦',
  shanghai_gov_theatre_12: '黄浦',
  shanghai_gov_theatre_13: '黄浦',
  shanghai_gov_theatre_14: '黄浦',
  shanghai_gov_theatre_16: '黄浦',
  shanghai_gov_theatre_17: '黄浦',
  shanghai_gov_theatre_18: '黄浦',
  shanghai_gov_theatre_19: '黄浦',
  shanghai_gov_theatre_20: '黄浦',
  shanghai_gov_theatre_21: '黄浦',
  shanghai_gov_theatre_22: '黄浦',
  shanghai_gov_theatre_23: '黄浦',
  shanghai_gov_theatre_24: '黄浦',
  shanghai_gov_theatre_25: '黄浦',
  shanghai_gov_theatre_26: '黄浦',
  shanghai_gov_theatre_27: '静安',
  shanghai_gov_theatre_28: '静安',
  shanghai_gov_theatre_29: '静安',
  shanghai_gov_theatre_30: '静安',
  shanghai_gov_theatre_31: '静安',
  shanghai_gov_theatre_32: '静安',
  shanghai_gov_theatre_33: '静安',
  shanghai_gov_theatre_34: '静安',
  shanghai_gov_theatre_35: '静安',
  shanghai_gov_theatre_36: '静安',
  shanghai_gov_theatre_37: '静安',
  shanghai_gov_theatre_38: '静安',
  shanghai_gov_theatre_39: '静安',
  shanghai_gov_theatre_40: '静安',
  shanghai_gov_theatre_41: '静安',
  shanghai_gov_theatre_42: '静安',
  shanghai_gov_theatre_43: '静安',
  shanghai_gov_theatre_44: '静安',
  shanghai_gov_theatre_45: '静安',
  shanghai_gov_theatre_46: '徐汇',
  shanghai_gov_theatre_47: '徐汇',
  shanghai_gov_theatre_48: '徐汇',
  shanghai_gov_theatre_49: '徐汇',
  shanghai_gov_theatre_51: '徐汇',
  shanghai_gov_theatre_52: '徐汇',
  shanghai_gov_theatre_53: '徐汇',
  shanghai_gov_theatre_54: '徐汇',
  shanghai_gov_theatre_55: '徐汇',
  shanghai_gov_theatre_56: '徐汇',
  shanghai_gov_theatre_57: '徐汇',
  shanghai_gov_theatre_58: '虹口',
  shanghai_gov_theatre_59: '虹口',
  shanghai_gov_theatre_60: '虹口',
  shanghai_gov_theatre_61: '虹口',
  shanghai_gov_theatre_62: '虹口',
  shanghai_gov_theatre_63: '虹口',
  shanghai_gov_theatre_64: '虹口',
  shanghai_gov_theatre_65: '虹口',
  shanghai_gov_theatre_66: '虹口',
  shanghai_gov_theatre_67: '虹口',
  shanghai_gov_theatre_68: '长宁',
  shanghai_gov_theatre_69: '长宁',
  shanghai_gov_theatre_70: '长宁',
  shanghai_gov_theatre_71: '长宁',
  shanghai_gov_theatre_72: '闵行',
  shanghai_gov_theatre_73: '闵行',
  shanghai_gov_theatre_74: '闵行',
  shanghai_gov_theatre_75: '闵行',
  shanghai_gov_theatre_76: '闵行',
  shanghai_gov_theatre_77: '闵行',
  shanghai_gov_theatre_78: '闵行',
  shanghai_gov_theatre_79: '闵行',
  shanghai_gov_theatre_80: '闵行',
  shanghai_gov_theatre_81: '青浦',
  shanghai_gov_theatre_82: '青浦',
  shanghai_gov_theatre_83: '青浦',
  shanghai_gov_theatre_84: '青浦',
  shanghai_gov_theatre_85: '青浦',
  shanghai_gov_theatre_86: '青浦',
  shanghai_gov_theatre_87: '青浦',
  shanghai_gov_theatre_88: '青浦',
  shanghai_gov_theatre_89: '青浦',
  shanghai_gov_theatre_90: '青浦',
  shanghai_gov_theatre_91: '杨浦',
  shanghai_gov_theatre_92: '杨浦',
  shanghai_gov_theatre_93: '杨浦',
  shanghai_gov_theatre_94: '杨浦',
  shanghai_gov_theatre_95: '浦东',
  shanghai_gov_theatre_96: '浦东',
  shanghai_gov_theatre_97: '浦东',
  shanghai_gov_theatre_98: '浦东',
  shanghai_gov_theatre_99: '浦东',
  shanghai_gov_theatre_100: '浦东',
  shanghai_gov_theatre_101: '浦东',
  shanghai_gov_theatre_102: '浦东',
  shanghai_gov_theatre_103: '浦东',
  shanghai_gov_theatre_104: '浦东',
  shanghai_gov_theatre_105: '浦东',
  shanghai_gov_theatre_106: '浦东',
  shanghai_gov_theatre_107: '浦东',
  shanghai_gov_theatre_108: '浦东',
  shanghai_gov_theatre_109: '浦东',
  shanghai_gov_theatre_110: '浦东',
  shanghai_gov_theatre_111: '浦东',
  shanghai_gov_theatre_112: '浦东',
  shanghai_gov_theatre_114: '浦东',
  shanghai_gov_theatre_115: '浦东',
  shanghai_gov_theatre_116: '浦东',
  shanghai_gov_theatre_117: '浦东',
  shanghai_gov_theatre_118: '浦东',
  shanghai_gov_theatre_119: '浦东',
  shanghai_gov_theatre_120: '浦东',
  shanghai_gov_theatre_121: '浦东',
  shanghai_gov_theatre_122: '浦东',
  shanghai_gov_theatre_123: '浦东',
  shanghai_gov_theatre_124: '浦东',
  shanghai_gov_theatre_126: '浦东',
  shanghai_gov_theatre_127: '浦东',
  shanghai_gov_theatre_128: '浦东',
  shanghai_gov_theatre_129: '浦东',
  shanghai_gov_theatre_130: '浦东',
  shanghai_gov_theatre_131: '普陀',
  shanghai_gov_theatre_132: '奉贤',
  shanghai_gov_theatre_133: '奉贤',
  shanghai_gov_theatre_134: '奉贤',
  shanghai_gov_theatre_135: '奉贤',
  shanghai_gov_theatre_136: '奉贤',
  shanghai_gov_theatre_137: '奉贤',
  shanghai_gov_theatre_138: '奉贤',
  shanghai_gov_theatre_139: '奉贤',
  shanghai_gov_theatre_140: '奉贤',
  shanghai_gov_theatre_141: '奉贤',
  shanghai_gov_theatre_142: '奉贤',
  shanghai_gov_theatre_143: '奉贤',
  shanghai_gov_theatre_145: '宝山',
  shanghai_gov_theatre_146: '宝山',
  shanghai_gov_theatre_147: '嘉定',
  shanghai_gov_theatre_148: '嘉定',
  shanghai_gov_theatre_149: '嘉定',
  shanghai_gov_theatre_150: '崇明',
  shanghai_gov_theatre_151: '崇明',
  shanghai_gov_theatre_152: '崇明',
  shanghai_gov_theatre_153: '临港',
  shanghai_gov_theatre_154: '临港',
  shanghai_gov_theatre_155: '临港',
  shanghai_gov_theatre_156: '临港',
  shanghai_gov_theatre_157: '临港',
  shanghai_gov_theatre_158: '临港',
  shanghai_gov_theatre_159: '临港',
  shanghai_gov_theatre_160: '松江',
  wuhan_gov_1437233: '江岸区',
  wuhan_gov_1437239: '江岸区',
  wuhan_gov_1437243: '江汉区',
  wuhan_gov_1437246: '江汉区',
  wuhan_gov_1437249: '江岸区',
  wuhan_gov_1437250: '江岸区',
  wuhan_gov_1437254: '江汉区',
  xian_gov_62d8ba0ef8fd1c4c210ae016: '鄠邑区',
  xian_gov_1716741181564076033: '临潼区',
  xian_gov_5fbb551ff8fd1c59664b3711: '西安市临潼',
  xian_gov_1767090210230796290: '西安市莲湖',
  xian_gov_144: '西安市莲湖',
  xian_gov_232: '西安市莲湖',
  xian_gov_38: '西安市莲湖',
  xian_gov_1998584920184258561: '西安市鄠邑',
  xian_gov_1716743219733606401: '临潼区',
  xian_gov_25: '蓝田县',
  xian_gov_61a43e9bf8fd1c0bdc700bfa: '蓝田县',
  zhuhai_gov_tsg_xiangzhou: '香洲区',
  zhuhai_gov_bwg_xiangzhou: '香洲区',
  zhuhai_gov_bwg_shengbao: '香洲区',
  zhuhai_gov_bwg_handong: '香洲区',
  zhuhai_gov_bwg_yuhai: '香洲区',
  zhuhai_gov_bwg_puji: '香洲区',
  zhuhai_gov_bwg_luoxini: '高新区',
  zhuhai_gov_bwg_yuandao: '横琴新区',
  zhuhai_gov_bwg_fuhua: '横琴新区',
  zhuhai_gov_msg_guyuan: '香洲区',
  zhuhai_gov_tycg_doumen_gym: '斗门区',
  zhuhai_gov_tycg_doumen_gym2: '斗门区',
  zhuhai_gov_tycg_doumen_fitness: '斗门区',
  zhuhai_gov_tycg_jinwan_square: '金湾区',
  zhuhai_gov_tycg_hengqin_square: '横琴新区',
  zhuhai_gov_tycg_tangjiawan_square: '高新区',
  zhuhai_gov_tycg_nanshui_square: '高栏港区',
  zhuhai_gov_tycg_pingsha_square: '高栏港区',
  zhuhai_gov_tycg_guishan_square: '万山区',
  zhuhai_gov_tycg_dangan_square: '万山区',
  zhuhai_gov_tycg_wanshan_dawan: '万山区',
  zhuhai_gov_tycg_wanshan_dongao: '万山区'
};

// source key 到场馆名映射（自动生成）
const sourceToVenue = {
  szlib: '深圳图书馆',
  sz_children_lib: '深圳少年儿童图书馆',
  szmuseum: '深圳博物馆',
  szstm: '深圳科学技术馆',
  szbo: '深圳滨海艺术中心',
  szconcert: '深圳音乐厅',
  szmocap: '深圳市当代艺术与城市规划馆',
  szsports: '深圳市体育中心',
  szmassart: '深圳市文化馆',
  sznm: '深圳自然博物馆',
  nslib: '南山图书馆',
  nsmuseum: '南山博物馆',
  nswhg: '南山区文化馆',
  nsqsng: '南山区青少年活动中心',
  nswtzx: '南山文体中心',
  nsaqjy: '南山安全教育体验馆',
  skhykpg: '蛇口海洋科普馆',
  sarc: '深爱人才馆',
  ntgc: '南头古城博物馆群',
  zsjbwg: '招商局历史博物馆',
  nssxf: '南山书房',
  oct_wetland: '华侨城湿地',
  szwty: '深圳湾体育中心',
  hlgw: '欢乐港湾',
  ftlib: '福田区图书馆',
  ftwhg: '福田区文化馆',
  ftart: '福田美术馆',
  lh_paleo: '深圳古生物博物馆',
  lhlib: '罗湖区图书馆',
  lhwhg2: '罗湖区文化馆',
  lhtheatre: '深圳戏院',
  szdjy: '深圳大剧院',
  balib: '宝安图书馆',
  bamuseum: '宝安区博物馆',
  baoan_1990: '宝安1990文化馆',
  baoan_kjg: '宝安科技馆',
  baoan_ty: '宝安体育中心',
  baoan_qsng: '宝安区青少年宫',
  baoan_guihua: '宝安城市规划展览馆',
  bayarea_eye: '湾区之眼',
  lglib: '龙岗区图书馆',
  lgmuseum: '龙岗区博物馆',
  lgwhg: '龙岗区文化馆',
  lgqsng: '龙岗区青少年宫',
  lg_hakka: '龙岗客家民俗博物馆',
  lgtyzx: '龙岗体育中心',
  lg_arts: '深圳龙岗国际艺术中心',
  lgkjg: '龙岗区科技馆',
  lgpark: '龙岗儿童公园',
  lhxqlib: '龙华区图书馆',
  lhqsng: '龙华区青少年宫',
  lhwhg: '龙华区文化馆',
  lh_printmaking: '中国版画博物馆',
  lh_ecology: '龙华生态文明展览馆',
  lhkjg: '龙华区科技馆',
  lhbljng: '龙华白石龙纪念馆',
  gmlib: '光明区图书馆',
  gm_kjg: '光明区科技馆',
  gmwhg: '光明区文化馆',
  gmarts: '光明文化艺术中心',
  gmqsng: '光明区青少年活动中心',
  gmtyzx: '光明区群众体育中心',
  gmhbgy: '光明虹桥公园',
  gmtysq: '玉塘文体中心',
  pslib: '坪山区图书馆',
  psart: '坪山美术馆',
  psthtr: '坪山大剧院',
  pskjg: '坪山区科技馆',
  pstyzx: '坪山体育中心',
  psdjng: '坪山东江纵队纪念馆',
  pszxgy: '坪山中心公园',
  mlsgy: '马峦山郊野公园',
  jlsgy: '聚龙山生态公园',
  yhzgz: '燕子湖国际会展中心',
  ytlib: '盐田区图书馆',
  ytwhg: '盐田区文化馆',
  yt_history: '中英街历史博物馆',
  ytkjg: '盐田科技馆',
  yttyzx: '盐田体育中心',
  ytzgy: '盐田中央公园',
  dpgeopark: '大鹏地质公园博物馆',
  dp_nuclear: '大亚湾核能科技馆',
  dplib: '大鹏新区图书馆',
  dpgcbwg: '大鹏古城博物馆',
  dpwhg: '大鹏新区文化馆',
  xcart: '深圳西涌天文台',
  dchss: '东涌红树林湿地公园',
  bghsl: '坝光红树林湿地公园',
  mgha: '玫瑰海岸',
  ymk: '杨梅坑',
  qns: '七娘山',
  ghysq: '官湖村艺象艺术区',
  jsgjly: '金沙湾国际乐园',
  dpkjg: '大鹏新区科学馆',
  jcw: '大鹏较场尾沙滩',
  kcsigy: '葵涌生态公园',
  sz_safety: '深圳市安全教育基地',
  opower: 'OPOWER文化艺术中心',
  psqsng: '坪山区青少年宫',
  gdmuseum: '广东省博物馆',
  gzmuseum: '广州博物馆',
  gzlib: '广州图书馆',
  shanghaimuseum: '上海博物馆',
  shstm: '上海科技馆',
  chnmuseum: '中国国家博物馆',
  gugong: '故宫博物院',
  hxngallery: '何香凝美术馆',
  gsyart: '关山月美术馆',
  szartm: '深圳美术馆',
  polytheatre: '深圳保利剧院',
  szcec: '深圳会展中心',
  shenzhen_world: '深圳国际会展中心',
  theme_park: '锦绣中华民俗村',
  szcp: '深圳市少年宫',
  szaac: '深圳市青少年活动中心',
  szbook: '深圳书城',
  szhbgy: '深圳湾公园',
  hssjwh: '海上世界文化艺术中心',
  szzybwg: '深圳中医药博物馆',
  szjewg: '深圳珠宝博物馆',
  hlgj: '深圳欢乐谷',
  hoha: '深圳欢乐海岸',
  szworld: '深圳世界之窗',
  hhgy: '洪湖公园',
  dshslc: '大沙河生态长廊',
  tjsgd: '淘金山绿道',
  xwhsl: '西湾红树林公园',
  mzohbd: '茅洲河碧道',
  sysgy: '石岩湖湿地公园',
  sywhzx: '石岩文化艺术中心',
  hhsgy: '红花山公园',
  dyzx: '深圳大运中心',
  dzxgy: '大运中心公园',
  atszx: '安托山公共文化中心',
  bzgx: '北站中心公园',
  kxgny: '深圳科学公园（南翼）',
  rcgy: '人才公园',
  jhwtz: '吉华街道文化站',
  nwwtz: '南湾街道文化站',
  pdwtz: '坪地街道文化站',
  ylwh: '园岭街道综合性文化服务中心',
  tywh: '桃源街道综合性文化服务中心',
  fhwh: '凤凰街道综合性文化服务中心',
  jlwh: '江岭社区公共文化服务中心',
  jkwh: '迳口社区综合性文化服务中心',
  zjam: '浙江省博物馆',
  北京本地宝: '北京密云区科技馆',
  圆明园: '圆明园',
  manual: '杨浦体育活动中心',
  centuryaltar: '中华世纪坛',
  中国人民革命军事博物馆: '中国人民革命军事博物馆',
  首都博物馆: '北京大运河博物馆',
  bjry: '北京国际戏剧中心·人艺小剧场',
  国家图书馆: '国家图书馆少年儿童馆',
  清华大学艺术博物馆: '清华大学艺术博物馆',
  '北京鲁迅博物馆（北京新文化运动纪念馆）': '北京鲁迅博物馆（北京新文化运动纪念馆）',
  中国电影博物馆: '中国电影博物馆',
  '北京艺术博物馆（万寿寺）': '北京艺术博物馆（万寿寺）',
  三山五园文化艺术中心: '三山五园文化艺术中心',
  bjmuseum: '北京大运河博物馆（首都博物馆东馆）',
  中山公园音乐堂: '中山公园音乐堂',
  成都本地宝: '成都双流区体育馆',
  重庆本地宝: '重庆渝北区文化中心',
  广州本地宝: '广州白云区植物园',
  腾讯新闻: '星海音乐厅',
  从化温泉旅游度假区: '从化温泉旅游度假区',
  南沙天后宫: '南沙天后宫',
  增城1978文化创意园: '增城1978文化创意园',
  广东省文化和旅游厅: '广东民间工艺博物馆（陈家祠）',
  gdartmuseum: '广东美术馆（二沙岛本馆）',
  新瑞金票: '正佳大剧院',
  广州市文化广电旅游局: '广州市文化馆',
  增城区图书馆: '增城区图书馆',
  花都湖公园: '花都湖公园',
  南沙区图书馆: '南沙区图书馆',
  农讲所纪念馆: '毛泽东同志主办农民运动讲习所旧址纪念馆',
  花都区图书馆: '花都区图书馆',
  南沙湿地景区: '南沙湿地景区',
  '广州民俗博物馆（花都）': '广州民俗博物馆（花都）',
  羊城晚报: '广东省立中山图书馆',
  '百度百家号（广州科普Citywalk）': '中国科学院华南植物园',
  从化区图书馆: '从化区图书馆',
  黄埔军校旧址纪念馆: '黄埔军校旧址纪念馆',
  孙中山大元帅府纪念馆: '孙中山大元帅府纪念馆',
  长隆官方: '长隆旅游度假区',
  nanyuewang: '南越王博物院（王墓展区）',
  南汉二陵博物馆: '南汉二陵博物馆',
  杭州本地宝: '西湖音乐节',
  西泠印社: '中国印学博物馆',
  宋城演艺: '杭州宋城',
  杭州市文化广电旅游局: '浙江省博物馆之江馆',
  浙江自然博物院: '浙江自然博物院',
  浙江省博物馆: '浙江省博物馆武林馆区',
  浙江省文化馆: '浙江省文化馆',
  浙江交响乐团: '杭州运河大剧院',
  杭州图书馆官网: '杭州图书馆少儿分馆',
  南京本地宝: '南京栖霞区美术馆',
  上海本地宝: '上海虹口区创意园',
  上海迪士尼度假区: '上海迪士尼度假区',
  上观新闻: '中华艺术宫',
  shcstheatre: '上海文化广场',
  浦东美术馆: '浦东美术馆',
  中共一大纪念馆: '中共一大纪念馆',
  上海世博会博物馆: '上海世博会博物馆',
  上海展览中心: '上海展览中心',
  chinaartmuseum: '上海美术馆（中华艺术宫）',
  上海当代艺术博物馆: '上海当代艺术博物馆',
  misa: '捷豹上海交响音乐厅',
  shhistorymuseum: '上海市历史博物馆',
  '中华艺术宫（上海美术馆）': '中华艺术宫（上海美术馆）',
  南山博物馆: '南山博物馆一层一号专题展厅',
  深圳博物馆官网: '深圳博物馆（历史民俗馆）',
  光明区马田街道综合性文化服务中心: '光明区马田街道综合性文化服务中心',
  深圳科学技术馆官网: '深圳科学技术馆（光明新馆）',
  龙城街道文化站: '龙城街道文化站',
  光明区公明街道综合性文化服务中心: '光明区公明街道综合性文化服务中心',
  横岗街道文化站: '横岗街道文化站',
  光明文化艺术中心: '光明文化艺术中心·演艺中心·大剧院',
  宝安区文化馆: '宝安区文化馆',
  宝安区文化馆新桥街道分馆: '宝安区文化馆新桥街道分馆',
  宝安区文化馆燕罗分馆: '宝安区文化馆燕罗街道分馆',
  坂田街道文化站: '坂田街道文化站',
  深圳市体育中心: '深圳市体育中心体育场',
  大鹏办事处公共事业服务中心: '大鹏办事处公共事业服务中心',
  '中轴云廊·顶上空间': '中轴云廊·顶上空间',
  光明区光明街道综合性文化服务中心: '光明区光明街道综合性文化服务中心',
  龙岗街道文化站: '龙岗街道文化站',
  深圳市坪山区石井街道公共文化服务中心: '深圳市坪山区石井街道公共文化服务中心',
  福田戏剧馆: '福田戏剧馆',
  大浪街道综合文化服务中心: '大浪街道综合文化服务中心',
  深圳图书馆: '深圳图书馆 (深圳图书馆北馆)',
  福田音乐馆: '福田音乐馆',
  白花社区综合性文化服务中心: '白花社区综合性文化服务中心',
  园山街道文化站: '园山街道文化站',
  深圳音乐厅官网: '深圳音乐厅五楼小剧场',
  baoan: '上合孝德园',
  武汉本地宝: '武汉江汉区植物园',
  西安本地宝: '西安长安区剧院',
  zhmuseum: '珠海博物馆',
  zhlib: '珠海市图书馆',
  zhwhg: '珠海市文化馆',
  gymuseum: '古元美术馆',
  zhtheatre: '珠海大剧院',
  xsart: '香山文化艺术中心',
  zhplan: '珠海规划展览馆',
  fzg: '国家方志馆粤港澳大湾区分馆',
  zhqsng: '珠海市青少年妇女儿童活动中心',
  zhgrwhg: '珠海市工人文化宫',
  ymxy: '圆明新园',
  mxpf: '梅溪牌坊',
  zhcec: '珠海国际会展中心',
  hfsd: '华发商都',
  hbgy: '珠海海滨公园',
  jwlib: '金湾区图书馆',
  jwwhg: '金湾区文化馆',
  jwmuseum: '金湾区博物馆',
  jwart: '金湾艺术中心',
  tcbj: '汤臣倍健透明工厂',
  zhairshow: '珠海航展馆',
  hqw: '珠海海泉湾度假区',
  jwtyzx: '金湾体育中心',
  szwhzx: '三灶镇文化中心',
  jhawhys: '金海岸文化艺术中心',
  dmlib: '斗门区图书馆',
  dmmuseum: '斗门区博物馆',
  dmwhg: '斗门区文化馆',
  dmjj: '斗门旧街',
  jts: '金台寺',
  ywq: '御温泉',
  dmtyzx: '斗门体育中心',
  jawhzx: '井岸镇文化中心',
  hys: '黄杨山',
  dmfy: '斗门非遗展示馆',
  hqwhys: '横琴文化艺术中心',
  zhlh: '珠海长隆海洋王国',
  zhfclc: '珠海长隆飞船乐园',
  zhhqtj: '珠海长隆横琴剧院',
  hqwlqzx: '横琴国际网球中心',
  xld: '星乐度露营小镇',
  hqsdgy: '横琴湿地公园',
  hqhchl: '横琴花海长廊',
  hqka: '横琴口岸',
  hqjrd: '横琴金融岛',
  zhyn: '珠海渔女景区',
  yld: '野狸岛音乐广场',
  zhtyzx: '珠海市体育中心',
  xzwhg: '香洲区文化馆',
  szwt_12865898: '龙岗国际艺术中心·D+数字艺术馆',
  szwt_12865897: '龙岗国际艺术中心·国际演艺中心',
  szwt_12864965: '深圳市龙岗区怡利翡翠博物馆',
  szwt_12864964: '深圳市龙岗区龙岭邮票博物馆',
  szwt_12864963: '深圳市龙岗区万国珠宝汇矿物博物馆',
  szwt_12863189: '龙岗区图书馆少儿馆',
  szwt_12861229: '深圳市百师园非物质文化遗产博物馆',
  szwt_12861228: '深圳市丁全匠作博物馆',
  szwt_12861227: '深圳市梵亚艺术博物馆',
  szwt_12861226: '深圳市龙岗区东江潮红色文化博物馆（新生主馆）',
  szwt_12861225: '深圳市隐秀高尔夫博物馆',
  szwt_12374186: '深圳·红立方',
  szwt_12364958: '茅洲河体育艺术中心',
  szwt_12095611: '深圳市坪山区文化馆',
  szwt_11671562: '深圳市工业展览馆',
  szwt_11644501: '南山区天后博物馆',
  szwt_11668510: '风华大剧院',
  szwt_11485498: '福田文体中心·戏剧主题馆',
  szwt_11485497: '福田文体中心·舞蹈主题馆',
  szwt_11485496: '福田文体中心·音乐主题馆',
  szwt_11485494: '福田文体中心·梦工场',
  szwt_11485500: '福田文体中心·非遗主题馆',
  szwt_11171158: '大鹏新区博物馆',
  szwt_11170215: '金龟自然书房分馆',
  szwt_11170203: '坪山儿童公园分馆',
  szwt_11170204: '坪山图书馆·客家特藏馆',
  szwt_11168520: '深圳红木家具博物馆',
  szwt_11168444: '深圳望野博物馆',
  szwt_11166909: '深圳市龙华区美联红木艺术博物馆',
  szwt_11166908: '深圳市艺之卉百年时尚博物馆',
  szwt_11166901: '中国文化名人大营救纪念馆',
  szwt_11167831: '龙岗文化中心音乐厅',
  szwt_11167822: '龙岗文化中心大剧院',
  szwt_11167080: '深圳市龙岗区文化馆',
  szwt_11153449: '世纪琥珀博物馆',
  szwt_11132724: '华润大厦艺术中心美术馆',
  szwt_11132704: '南头古城博物馆',
  szwt_11145352: '龙华图书馆',
  szwt_11131232: '蛇口海上世界文化艺术中心',
  szwt_11129404: '深圳南山文体中心剧院聚橙剧院',
  szwt_11128382: '依波钟表文化博物馆',
  szwt_11128585: '惜物博物馆',
  szwt_11128370: '光明区少年儿童图书馆',
  szwt_11127123: '深汕西文体中心',
  szwt_11116977: '深圳（宝安）劳务工博物馆',
  szwt_11116976: '至美术馆',
  szwt_11114637: '深圳市坪山区美术馆',
  szwt_11114636: '深圳市坪山区图书馆',
  szwt_11114635: '深圳市坪山区东江纵队纪念馆',
  szwt_11111303: '深圳市福田区图书馆',
  szwt_12766454: '光明国际马术中心',
  szwt_12699929: '罗湖体育馆',
  szwt_12699821: '罗湖体育休闲公园',
  szwt_12699826: '罗湖网球中心',
  szwt_12502724: '横岗文体中心',
  szwt_12490550: '宝龙文体中心',
  szwt_12490551: '深圳布吉文体中心',
  szwt_12364970: '深圳市青少年足球训练基地',
  szwt_12364975: '光明区红花山体育中心',
  szwt_11999373: '北京大学附属中学深圳学校(集团)黄埔学校(小学部)',
  szwt_11197294: '民治体育公园',
  szwt_11169238: '葵涌中学体育场',
  szwt_11169235: '南澳中学体育场',
  szwt_11169234: '南澳中心小学体育场',
  szwt_11169233: '人大附中深圳学校高中部体育场',
  szwt_11168746: '葵涌第二小学体育场',
  szwt_11168745: '溪涌小学体育场',
  szwt_11168743: '葵涌中心小学体育场',
  szwt_11168742: '大鹏第二小学体育场',
  szwt_11167839: '深圳市龙岗区体育中心',
  szwt_11151909: '沙头角体育馆',
  szwt_11151908: '盐田区游泳馆',
  szwt_11151907: '盐田区体育发展服务中心网球场',
  szwt_11145432: '九龙山体育公园',
  szwt_11136104: '冰纷万象滑雪场',
  szwt_11135809: '锡才体育公园',
  szwt_11133787: '大鹏新区葵涌中心小学',
  szwt_11133687: '景鹏小学',
  szwt_11131701: '南海足球公园',
  szwt_11129884: '荔香公园网球场',
  szwt_11129883: '桃源群众篮球网球体育公园',
  szwt_11129790: '大沙河公园体育中心',
  szwt_11129541: '蛇口体育中心',
  szwt_11129527: '深圳湾体育训练基地',
  szwt_11128645: '深圳中山公园棒球场',
  szwt_11126064: '简上体育综合体',
  szwt_11117341: '综合训练馆（室内网球馆）',
  szwt_11117342: '宝安游泳场馆',
  szwt_11117343: '宝安体育场',
  szwt_11117344: '宝安体育馆',
  szwt_11114606: '深圳市坪山区坪山体育中心体育馆',
  szwt_11111766: '香蜜体育中心',
  szwt_11111767: '黄木岗网球中心',
  szwt_11111768: '莲花体育中心',
  szwt_11111769: '福田体育公园',
  szwt_11111305: '福田区景田网球中心',
  szwt_11111306: '福田海滨生态体育公园',
  gu_gov_9589386: '广东省科技图书馆',
  gu_gov_9497366: '广东省人民体育场',
  gu_gov_9511671: '广州大学城体育中心',
  gu_gov_9513274: '沙面体育俱乐部',
  gu_gov_9512915: '广州棋院',
  gu_gov_9513134: '广州海角红楼游泳场',
  gu_gov_9512996: '广东省奥林匹克体育中心',
  gu_gov_9513170: '广州亚运城综合体育馆',
  gu_gov_9589229: '南越王博物馆',
  gu_gov_9375725: '广州艺术博物院（广州美术馆）新馆',
  gu_gov_9587900: '广东民间工艺博物馆',
  gu_gov_9589240: '广州货币金融博物馆',
  gu_gov_9589231: '粤剧艺术博物馆',
  gu_gov_9588085: '岭南金融博物馆',
  gu_gov_9589224: '广东华侨博物馆',
  gu_gov_6533843: '陈李济中药博物馆',
  gu_gov_6533840: '荔湾博物馆',
  gu_gov_6533841: '广东中医药博物馆',
  gu_gov_6533842: '广州市东平典当博物馆',
  gu_gov_6533839: '番禺博物馆',
  gu_gov_6533838: '从化博物馆',
  beijing_gov_wwj_546081: '北京老爷车博物馆',
  beijing_gov_wwj_546090: '北京李大钊故居',
  beijing_gov_wwj_546099: '北京励志堂科举匾额博物馆',
  beijing_gov_wwj_546102: '历代帝王庙',
  beijing_gov_wwj_546114: '中国法院博物馆',
  beijing_gov_wwj_546117: '北京韩美林艺术馆',
  beijing_gov_wwj_546123: '延庆博物馆',
  beijing_gov_wwj_546120: '北京西瓜博物馆',
  beijing_gov_wwj_546129: '中国人民大学博物馆',
  beijing_gov_wwj_546132: '北京空竹博物馆',
  beijing_gov_wwj_546135: '北京市怀柔区博物馆',
  beijing_gov_wwj_546150: '北京怀柔喇叭沟门满族民俗博物馆',
  beijing_gov_wwj_546162: '民航博物馆',
  beijing_gov_wwj_546174: '中国传媒大学传媒博物馆',
  beijing_gov_wwj_546171: '西藏文化博物馆',
  beijing_gov_wwj_546183: '和苑博物馆',
  beijing_gov_wwj_546186: '中国海关博物馆',
  beijing_gov_wwj_546195: '北京御仙都皇家菜博物馆',
  beijing_gov_wwj_546198: '北京市平谷区博物馆',
  beijing_gov_wwj_546192: '北京英杰硬石艺术博物馆',
  beijing_gov_wwj_546204: '北京税务博物馆',
  beijing_gov_wwj_546213: '中国华侨历史博物馆',
  beijing_gov_wwj_546210: '中国人民大学家书博物馆',
  beijing_gov_wwj_546219: '北京文旺阁木作博物馆',
  beijing_gov_wwj_662437: '延庆区地质博物馆',
  beijing_gov_wwj_662465: '北京市姜杰钢琴手风琴博物馆',
  beijing_gov_wwj_10877380: '首都粮食博物馆',
  beijing_gov_wwj_10877385: '香山革命纪念馆',
  beijing_gov_wwj_10877395: '北京荣唐连环画博物馆',
  beijing_gov_wwj_10877405: '北京二锅头酒博物馆',
  beijing_gov_wwj_10877415: '北京市大兴区月季博物馆',
  beijing_gov_wwj_10877420: '北京皇城御窑金砖博物馆',
  beijing_gov_wwj_10877425: '北京燕京八绝博物馆',
  beijing_gov_wwj_10877430: '北京东璧堂中医药博物馆',
  beijing_gov_wwj_11077312: '北京市和光书院博物馆',
  beijing_gov_wwj_11077317: '北京大戚收音机电影机博物馆',
  beijing_gov_wwj_11077327: '北京菜百黄金珠宝博物馆',
  beijing_gov_wwj_11077332: '北京市石景山区博物馆',
  beijing_gov_wwj_11077337: '颐和园博物馆',
  beijing_gov_wwj_11077342: '中国共产党早期北京革命活动纪念馆',
  beijing_gov_wwj_11186650: '北京京华茶叶博物馆',
  beijing_gov_wwj_21228162: '北京文景珍本期刊博物馆',
  beijing_gov_wwj_21228167: '国家典籍博物馆',
  beijing_gov_wwj_325729805: '北京航空航天模型博物馆',
  beijing_gov_wwj_325822216: '北京法和律师博物馆',
  beijing_gov_wwj_325822223: '北京龙顺成京作非遗博物馆',
  beijing_gov_wwj_325880511: '中国共产党历史展览馆',
  beijing_gov_wwj_325880521: '北京市顺义区博物馆',
  beijing_gov_wwj_325880527: '北京金漆镶嵌艺术博物馆',
  beijing_gov_wwj_325968712: '北京云汇网球木拍博物馆',
  beijing_gov_wwj_546027: '北京自来水博物馆',
  beijing_gov_wwj_545811: '中国佛教图书文物馆',
  beijing_gov_wwj_10877390: '北京劲飞京作红木文化博物馆',
  beijing_gov_wwj_662468: '西黄寺博物馆',
  beijing_gov_wwj_10877410: '北京中药炮制技术博物馆',
  beijing_gov_wwj_545940: '何扬·吴茜现代绘画馆',
  beijing_gov_wwj_545964: '平西抗日战争纪念馆',
  beijing_gov_wwj_326114740: '北京中梦足球博物馆',
  beijing_gov_wwj_21228156: '北京九鼎灶文化博物馆',
  beijing_gov_wwj_546072: '北京宣南文化博物馆管理处',
  beijing_gov_wwj_545895: '北京文博交流馆（北京市智化寺管理处）',
  beijing_gov_wwj_325729820: '北京莱恩堡葡萄酒文化博物馆',
  beijing_gov_wwj_546156: '北京市房山世界地质公园博物馆',
  beijing_gov_wwj_546084: '北京百年世界老电话博物馆',
  beijing_gov_wwj_545982: '中国电信博物馆',
  beijing_gov_wwj_325729837: '北京市海淀区中关村村史馆',
  beijing_gov_wwj_546147: '中国化工博物馆',
  beijing_gov_wwj_546021: '北京服装学院民族服饰博物馆',
  beijing_gov_wwj_546015: '北京工艺美术博物馆',
  beijing_gov_wwj_545853: '中央美术学院美术馆',
  beijing_gov_wwj_546024: '北京警察博物馆',
  beijing_gov_wwj_326128383: '北京考古遗址博物馆（金中都水关遗址）',
  beijing_gov_wwj_743627558: '十三陵水库展览馆',
  beijing_gov_wwj_743627668: '国家大剧院台湖舞美艺术博物馆',
  beijing_gov_wwj_743627673: '北京天桥印象博物馆',
  beijing_gov_wwj_743627719: '北京牛栏山二锅头酒文化博物馆',
  beijing_gov_wwj_743627734: '石景山区石刻博物馆',
  beijing_gov_wwj_743627785: '北京公交馆',
  beijing_gov_wwj_743627797: '北京天元中医药博物馆',
  beijing_gov_wwj_743627807: '视障文化博物馆',
  beijing_gov_wwj_743627813: '中国木偶艺术剧院博物馆',
  beijing_gov_wwj_743627828: '景泰蓝艺术博物馆',
  beijing_gov_wwj_743627844: '北京六必居博物馆',
  beijing_gov_wwj_743627862: '北京福履布鞋文化博物馆',
  beijing_gov_wwj_743627885: '慈善寺古香道文化陈列馆',
  beijing_gov_wwj_743627911: '科学家博物馆',
  beijing_gov_wwj_743627928: '全聚德博物馆',
  beijing_gov_wwj_743627936: '对外经贸博物馆',
  beijing_gov_wwj_743627941: '瀛海文史馆',
  beijing_gov_wwj_545763: '宋庆龄故居管理中心',
  beijing_gov_wwj_545784: '万寿寺博物馆',
  beijing_gov_wwj_743627946: '北京舞蹈学院舞蹈博物馆',
  beijing_gov_wwj_743627951: '北京市大兴区天宫院乡情文史馆',
  beijing_gov_wwj_743627956: '北京外国语大学校史馆、世界语言艺术博物馆',
  beijing_gov_wwj_743627961: '北京宝翠宫翡翠博物馆',
  beijing_gov_wwj_743627969: '京东方历史展览馆',
  beijing_gov_wwj_743627974: '水峪村生态博物馆',
  beijing_gov_wwj_743627979: '北京神州连环画博物馆',
  beijing_gov_wwj_743627987: '北京果脯博物馆',
  beijing_gov_wwj_743627996: '延庆石刻博物馆',
  beijing_gov_wwj_743628001: '北京市大兴区榆垡镇乡情文史馆',
  beijing_gov_wwj_743628006: '北京遇见艺术博物馆',
  beijing_gov_wwj_743628012: '北京神农农耕文化博物馆',
  beijing_gov_wwj_743628017: '清华大学科学博物馆',
  beijing_gov_wwj_545793: '徐悲鸿纪念馆',
  beijing_gov_wwj_545796: '炎黄艺术馆',
  beijing_gov_wwj_545799: '明十三陵博物馆',
  beijing_gov_wwj_545808: '梅兰芳纪念馆',
  beijing_gov_wwj_545817: '雍和宫藏传佛教艺术博物馆',
  beijing_gov_wwj_545829: '北京考古遗址博物馆（北京大葆台遗址博物馆）',
  beijing_gov_wwj_545832: '北京大学赛克勒考古与艺术博物馆',
  beijing_gov_wwj_545835: '北京市白塔寺管理处',
  beijing_gov_wwj_545838: '李大钊烈士陵园',
  beijing_gov_wwj_545841: '詹天佑纪念馆',
  beijing_gov_wwj_545844: '北京焦庄户地道战遗址纪念馆',
  beijing_gov_wwj_545847: '中央民族大学民族博物馆',
  beijing_gov_wwj_545850: '北京航空航天博物馆',
  beijing_gov_wwj_545856: '北京房山云居寺石经博物馆',
  beijing_gov_wwj_545859: '密云区博物馆',
  beijing_gov_wwj_545862: '昌平区博物馆',
  beijing_gov_wwj_545865: '通州区博物馆',
  beijing_gov_wwj_545868: '山戎文化陈列馆',
  beijing_gov_wwj_545871: '长辛店二·七纪念馆',
  beijing_gov_wwj_545874: '上宅文化陈列馆',
  beijing_gov_wwj_545877: '郭守敬纪念馆',
  beijing_gov_wwj_545880: '中国第四纪冰川遗迹陈列馆',
  beijing_gov_wwj_545883: '周口店北京人遗址博物馆',
  beijing_gov_wwj_545886: '中国印刷博物馆',
  beijing_gov_wwj_545889: '中国工艺美术馆（中国非物质文化遗产馆）',
  beijing_gov_wwj_545892: '北京红楼文化艺术博物馆',
  beijing_gov_wwj_545898: '北京中轴线遗产保护中心（正阳门）',
  beijing_gov_wwj_545901: '北京明城墙遗址公园（东南城角角楼）',
  beijing_gov_wwj_545904: '北京大觉寺与团城管理处（团城演武厅）',
  beijing_gov_wwj_545907: '文天祥祠',
  beijing_gov_wwj_545910: '永定河文化博物馆',
  beijing_gov_wwj_545913: '北京市钟鼓楼文物保管所',
  beijing_gov_wwj_545916: '北京法海寺博物馆',
  beijing_gov_wwj_545919: '中国国家画院美术馆',
  beijing_gov_wwj_545922: '圆明园展览馆',
  beijing_gov_wwj_545925: '北京大觉寺与团城管理处（大觉寺）',
  beijing_gov_wwj_545931: '北京中华民族博物院',
  beijing_gov_wwj_545934: '观复博物馆',
  beijing_gov_wwj_545937: '古陶文明博物馆',
  beijing_gov_wwj_545943: '中国钱币博物馆',
  beijing_gov_wwj_545949: '文化和旅游部恭王府博物馆',
  beijing_gov_wwj_545952: '中国现代文学馆',
  beijing_gov_wwj_545958: '慈悲庵',
  beijing_gov_wwj_545955: '中国蜜蜂博物馆',
  beijing_gov_wwj_545967: '平北抗日战争纪念馆',
  beijing_gov_wwj_545961: '卢沟桥历史博物馆',
  beijing_gov_wwj_545976: '曹雪芹纪念馆',
  beijing_gov_wwj_545970: '冀热察挺进军司令部旧址陈列馆',
  beijing_gov_wwj_545973: '北京中医药大学中医药博物馆',
  beijing_gov_wwj_545979: '香山双清别墅',
  beijing_gov_wwj_545991: '老甲艺术馆',
  beijing_gov_wwj_545994: '北京戏曲博物馆',
  beijing_gov_wwj_546003: '保利艺术博物馆',
  beijing_gov_wwj_546006: '北京中国紫檀博物馆',
  beijing_gov_wwj_546009: '北京南海子麋鹿苑博物馆',
  beijing_gov_wwj_546018: '中华世纪坛艺术馆',
  beijing_gov_wwj_546030: '北京王府井古人类文化遗址博物馆',
  beijing_gov_wwj_546033: '北京金台艺术馆',
  beijing_gov_wwj_546045: '中国铁道博物馆（东郊展馆）',
  beijing_gov_wwj_546048: '中国铁道博物馆正阳门展馆',
  beijing_gov_wwj_546054: '北京皇城艺术馆',
  beijing_gov_wwj_546057: '北京御生堂中医药博物馆',
  beijing_gov_wwj_546069: '居庸关长城博物馆',
  beijing_gov_wwj_546063: '北京人民艺术剧院戏剧博物馆',
  beijing_gov_wwj_546066: '北京市海淀区三山五园文化艺术中心（北京市海淀区博物...',
  beijing_gov_wwj_545736: '毛主席纪念堂',
  beijing_gov_wwj_545742: '民族文化宫博物馆',
  beijing_gov_wwj_545748: '中国农业博物馆',
  beijing_gov_wwj_545754: '中国航天博物馆',
  beijing_gov_tyj_1: '地坛体育中心',
  beijing_gov_tyj_2: '天坛体育中心',
  beijing_gov_tyj_3: '东单体育中心',
  beijing_gov_tyj_4: '地坛体育馆',
  beijing_gov_tyj_5: '广安体育中心',
  beijing_gov_tyj_6: '广安游泳网球馆',
  beijing_gov_tyj_7: '月坛体育馆',
  beijing_gov_tyj_8: '月坛综合训练馆',
  beijing_gov_tyj_9: '月坛体育场',
  beijing_gov_tyj_10: '西城区武术和棋类运动管理中心',
  beijing_gov_tyj_12: '朝阳体育馆',
  beijing_gov_tyj_13: '郡王府体育中心',
  beijing_gov_tyj_14: '海淀温泉体育中心',
  beijing_gov_tyj_15: '北京市网球运动管理中心',
  beijing_gov_tyj_16: '丰台体育中心',
  beijing_gov_tyj_17: '门头沟区体育馆',
  beijing_gov_tyj_18: '良乡训练基地',
  beijing_gov_tyj_19: '房山区体育场',
  beijing_gov_tyj_20: '良乡体育中心',
  beijing_gov_tyj_21: '潞城全民健身中心',
  beijing_gov_tyj_22: '顺义体育中心',
  beijing_gov_tyj_23: '顺义城南体育中心',
  beijing_gov_tyj_24: '昌平体育馆',
  beijing_gov_tyj_25: '昌平区体育运动场',
  beijing_gov_tyj_26: '回龙观体育文化公园',
  beijing_gov_tyj_27: '天通苑体育馆',
  beijing_gov_tyj_28: '大兴区体育中心',
  beijing_gov_tyj_29: '平谷区体育中心',
  beijing_gov_tyj_30: '怀柔区体育中心',
  beijing_gov_tyj_31: '密云区体育中心',
  beijing_gov_tyj_32: '延庆区体育中心',
  beijing_gov_tyj_33: '北京经济技术开发区体育中心',
  beijing_gov_tyj_34: '燕山体育馆',
  beijing_gov_whlyj_lib_1: '北京市东城区图书馆',
  beijing_gov_whlyj_lib_2: '北京市东城区图书馆东总布分馆',
  beijing_gov_whlyj_lib_3: '北京市东城区图书馆角楼分馆',
  beijing_gov_whlyj_lib_4: '北京市东城区图书馆王府井书店分馆',
  beijing_gov_whlyj_lib_5: '北京市东城区图书馆阅想书店分馆',
  beijing_gov_whlyj_lib_6: '北京市东城区图书馆语文书店分馆',
  beijing_gov_whlyj_lib_7: '北京市东城区图书馆北京银行陶然支行分馆',
  beijing_gov_whlyj_lib_8: '北京市西城区图书馆（北址）',
  beijing_gov_whlyj_lib_9: '北京市西城区图书馆（南址）',
  beijing_gov_whlyj_lib_10: '朝阳区图书馆（劲松馆）',
  beijing_gov_whlyj_lib_11: '朝阳区图书馆（小庄馆）',
  beijing_gov_whlyj_lib_13: '海淀区图书馆（北馆）',
  beijing_gov_whlyj_lib_14: '丰台区图书馆
（北大地馆）',
  beijing_gov_whlyj_lib_15: '丰台区图书馆
（大红门馆）',
  beijing_gov_whlyj_lib_16: '石景山区图书馆少儿馆',
  beijing_gov_whlyj_lib_18: '房山区图书馆（新）',
  beijing_gov_whlyj_lib_19: '房山区图书馆城关分馆（老馆）',
  beijing_gov_whlyj_lib_20: '燕山图书馆',
  beijing_gov_whlyj_lib_21: '北京市通州区图书馆',
  beijing_gov_whlyj_lib_22: '顺义区图书馆',
  beijing_gov_whlyj_lib_23: '大兴区图书馆',
  beijing_gov_whlyj_lib_24: '昌平区图书馆',
  beijing_gov_whlyj_lib_25: '平谷区图书馆',
  beijing_gov_whlyj_lib_26: '怀柔区图书馆',
  beijing_gov_whlyj_lib_27: '密云区图书馆',
  beijing_gov_whlyj_lib_28: '延庆区图书馆',
  beijing_gov_whlyj_cc_1: '北京市东城区文化馆',
  beijing_gov_whlyj_cc_2: '北京市西城区文化馆',
  beijing_gov_whlyj_cc_4: '海淀区文化馆',
  beijing_gov_whlyj_cc_5: '海淀区文化馆（北馆）',
  beijing_gov_whlyj_cc_6: '丰台区文化馆',
  beijing_gov_whlyj_cc_7: '石景山区文化馆',
  beijing_gov_whlyj_cc_8: '门头沟区文化馆',
  beijing_gov_whlyj_cc_9: '房山区文化馆（新）',
  beijing_gov_whlyj_cc_10: '房山区文化馆城关分馆（老馆）',
  beijing_gov_whlyj_cc_11: '燕山文化馆',
  beijing_gov_whlyj_cc_12: '通州区文化馆',
  beijing_gov_whlyj_cc_13: '顺义区文化馆',
  beijing_gov_whlyj_cc_14: '大兴区文化馆',
  beijing_gov_whlyj_cc_15: '昌平区文化馆',
  beijing_gov_whlyj_cc_16: '平谷区文化馆',
  beijing_gov_whlyj_cc_17: '怀柔区文化馆',
  beijing_gov_whlyj_cc_18: '密云区文化馆',
  beijing_gov_whlyj_cc_19: '延庆区文化馆',
  beijing_gov_whlyj_street_1: '和平里街道综合文化中心',
  beijing_gov_whlyj_street_2: '安定门街道文体中心',
  beijing_gov_whlyj_street_3: '交道口街道综合文化中心',
  beijing_gov_whlyj_street_4: '景山街道综合文化中心',
  beijing_gov_whlyj_street_5: '东华门街道综合文化中心',
  beijing_gov_whlyj_street_6: '东华门街道图书馆',
  beijing_gov_whlyj_street_7: '建国门街道综合文化中心',
  beijing_gov_whlyj_street_8: '朝阳门街道综合文化中心',
  beijing_gov_whlyj_street_9: '东四街道市民活动中心',
  beijing_gov_whlyj_street_10: '北新桥街道综合文化中心',
  beijing_gov_whlyj_street_11: '东直门街道综合文化中心',
  beijing_gov_whlyj_street_12: '前门街道市民活动中心',
  beijing_gov_whlyj_street_13: '崇文门外街道综合文化中心',
  beijing_gov_whlyj_street_14: '龙潭街道综合文化中心',
  beijing_gov_whlyj_street_15: '龙潭街道图书馆',
  beijing_gov_whlyj_street_16: '体育馆路街道综合文化中心',
  beijing_gov_whlyj_street_17: '东花市街道综合文化中心',
  beijing_gov_whlyj_street_18: '东花市街道图书馆',
  beijing_gov_whlyj_street_19: '天坛街道市民活动中心',
  beijing_gov_whlyj_street_20: '永外街道综合文化中心',
  beijing_gov_whlyj_street_21: '天桥街道',
  beijing_gov_whlyj_street_22: '牛街街道',
  beijing_gov_whlyj_street_23: '什刹海街道',
  beijing_gov_whlyj_street_24: '新街口街道',
  beijing_gov_whlyj_street_25: '月坛街道',
  beijing_gov_whlyj_street_26: '白纸坊街道',
  beijing_gov_whlyj_street_27: '德胜街道',
  beijing_gov_whlyj_street_28: '广外街道',
  beijing_gov_whlyj_street_29: '展览路街道',
  beijing_gov_whlyj_street_30: '广内街道',
  beijing_gov_whlyj_street_31: '椿树街道',
  beijing_gov_whlyj_street_32: '陶然亭街道',
  beijing_gov_whlyj_street_33: '金融街街道',
  beijing_gov_whlyj_street_34: '西长安街街道',
  beijing_gov_whlyj_street_35: '大栅栏街道',
  beijing_gov_whlyj_street_36: '香河园街道',
  beijing_gov_whlyj_street_37: '奥运村街道',
  beijing_gov_whlyj_street_39: '建外街道',
  beijing_gov_whlyj_street_40: '亚运村街道',
  beijing_gov_whlyj_street_41: '和平街街道',
  beijing_gov_whlyj_street_42: '三里屯街道',
  beijing_gov_whlyj_street_43: '望京街道',
  beijing_gov_whlyj_street_44: '朝外街道',
  beijing_gov_whlyj_street_45: '大屯街道',
  beijing_gov_whlyj_street_46: '首都机场街道',
  beijing_gov_whlyj_street_47: '垡头街道',
  beijing_gov_whlyj_street_48: '六里屯街道',
  beijing_gov_whlyj_street_49: '东湖街道',
  beijing_gov_whlyj_street_50: '团结湖街道',
  beijing_gov_whlyj_street_51: '安贞街道',
  beijing_gov_whlyj_street_52: '潘家园街道',
  beijing_gov_whlyj_street_53: '双井街道',
  beijing_gov_whlyj_street_54: '小关街道',
  beijing_gov_whlyj_street_55: '酒仙桥街道',
  beijing_gov_whlyj_street_56: '劲松街道',
  beijing_gov_whlyj_street_57: '八里庄街道',
  beijing_gov_whlyj_street_59: '左家庄街道',
  beijing_gov_whlyj_street_60: '麦子店街道',
  beijing_gov_whlyj_street_61: '太阳宫地区',
  beijing_gov_whlyj_street_62: '黑庄户地区',
  beijing_gov_whlyj_street_63: '十八里店地区',
  beijing_gov_whlyj_street_64: '将台地区',
  beijing_gov_whlyj_street_65: '豆各庄地区',
  beijing_gov_whlyj_street_66: '王四营地区',
  beijing_gov_whlyj_street_67: '常营地区',
  beijing_gov_whlyj_street_68: '金盏地区',
  beijing_gov_whlyj_street_69: '三间房地区',
  beijing_gov_whlyj_street_70: '东坝地区',
  beijing_gov_whlyj_street_71: '来广营地区',
  beijing_gov_whlyj_street_72: '崔各庄地区',
  beijing_gov_whlyj_street_73: '高碑店地区',
  beijing_gov_whlyj_street_74: '管庄地区',
  beijing_gov_whlyj_street_75: '孙河地区',
  beijing_gov_whlyj_street_76: '小红门地区',
  beijing_gov_whlyj_street_77: '平房地区',
  beijing_gov_whlyj_street_78: '东风地区',
  beijing_gov_whlyj_street_79: '南磨房地区',
  beijing_gov_whlyj_street_80: '呼家楼街道',
  beijing_gov_whlyj_street_81: '万寿路街道文化活动中心',
  beijing_gov_whlyj_street_82: '羊坊店地区文体活动中心',
  beijing_gov_whlyj_street_83: '羊坊店街道文化中心',
  beijing_gov_whlyj_street_84: '甘家口街道市民活动中心',
  beijing_gov_whlyj_street_85: '八里庄街道党群文化中心（慧美党群服务中心）',
  beijing_gov_whlyj_street_86: '八里庄街道图书馆',
  beijing_gov_whlyj_street_87: '紫竹院街道综合文化服务中心',
  beijing_gov_whlyj_street_88: '北下关街道综合文化活动中心（评剧团站）',
  beijing_gov_whlyj_street_89: '北下关街道综合文化活动中心（农科院站）',
  beijing_gov_whlyj_street_90: '北太平庄街道综合文化活动中心（蓟门书院）',
  beijing_gov_whlyj_street_91: '海淀街道市民活动中心',
  beijing_gov_whlyj_street_92: '海淀区海淀街道图书分馆',
  beijing_gov_whlyj_street_93: '中关村街道综合文化活动中心',
  beijing_gov_whlyj_street_94: '中关村街道图书馆',
  beijing_gov_whlyj_street_95: '学院路街道综合文化中心',
  beijing_gov_whlyj_street_96: '清河街道综合文化服务中心',
  beijing_gov_whlyj_street_97: '青龙桥街道综合文化活动中心',
  beijing_gov_whlyj_street_98: '香山街道综合文化中心',
  beijing_gov_whlyj_street_99: '香山街道图书馆',
  beijing_gov_whlyj_street_100: '西三旗街道文化活动中心',
  beijing_gov_whlyj_street_101: '马连洼街道综合文化活动中心',
  beijing_gov_whlyj_street_102: '马连洼街道图书馆',
  beijing_gov_whlyj_street_103: '花园路街道市民活动中心',
  beijing_gov_whlyj_street_104: '田村路街道文化活动中心',
  beijing_gov_whlyj_street_105: '上地街道文化活动中心',
  beijing_gov_whlyj_street_106: '上地街道图书馆',
  beijing_gov_whlyj_street_107: '曙光街道市民活动中心',
  beijing_gov_whlyj_street_108: '曙光街道图书馆',
  beijing_gov_whlyj_street_109: '燕园街道文化服务中心',
  beijing_gov_whlyj_street_110: '清华园街道综合文化活动中心',
  beijing_gov_whlyj_street_111: '永定路街道综合文化中心',
  beijing_gov_whlyj_street_112: '东升镇南部文化活动中心',
  beijing_gov_whlyj_street_113: '东升镇东部文化活动中心',
  beijing_gov_whlyj_street_114: '东升镇北部活动中心',
  beijing_gov_whlyj_street_115: '海淀镇综合文化活动中心',
  beijing_gov_whlyj_street_116: 'nan',
  beijing_gov_whlyj_street_117: '四季青镇综合文化活动中心',
  beijing_gov_whlyj_street_118: '西北旺镇市民活动中心',
  beijing_gov_whlyj_street_119: '温泉镇市民活动中心',
  beijing_gov_whlyj_street_120: '苏家坨镇综合文化活动中心',
  beijing_gov_whlyj_street_121: '上庄镇市民活动中心（北京市海淀区上庄镇党群活动中心）',
  beijing_gov_whlyj_street_122: '南苑街道综合文化中心',
  beijing_gov_whlyj_street_123: '丰台区青塔街道综合文化中心',
  beijing_gov_whlyj_street_124: '大红门街道综合文化中心',
  beijing_gov_whlyj_street_125: '北宫镇综合文化活动中心',
  beijing_gov_whlyj_street_126: '东高地街道综合文化中心',
  beijing_gov_whlyj_street_127: '和义街道文化中心',
  beijing_gov_whlyj_street_128: '丰台区太平桥街道市民活动中心',
  beijing_gov_whlyj_street_129: '丰台区新村街道综合文化中心',
  beijing_gov_whlyj_street_130: '长辛店街道综合文化中心',
  beijing_gov_whlyj_street_131: '丰台街道综合文化中心',
  beijing_gov_whlyj_street_132: '花乡街道综合文化中心',
  beijing_gov_whlyj_street_133: '石榴庄街道综合文化中心（原大红门街道综合文化中心）',
  beijing_gov_whlyj_street_134: '石榴庄街道综合文化中心（原东铁匠营街道综合文化活动中心）',
  beijing_gov_whlyj_street_135: '西罗园街道综合文化中心',
  beijing_gov_whlyj_street_136: '右安门街道综合文化中心',
  beijing_gov_whlyj_street_137: '丰台区王佐镇文化服务中心',
  beijing_gov_whlyj_street_138: '云岗街道综合文化中心',
  beijing_gov_whlyj_street_139: '宛平街道文体活动中心',
  beijing_gov_whlyj_street_140: '看丹街道综合文化中心（党群服务中心）',
  beijing_gov_whlyj_street_141: '马家堡街道文化活动中心',
  beijing_gov_whlyj_street_142: '卢沟桥街道市民活动中心',
  beijing_gov_whlyj_street_143: '方庄街道综合文化中心',
  beijing_gov_whlyj_street_144: '玉泉营街道市民活动中心',
  beijing_gov_whlyj_street_145: '东铁匠营街道综合文化中心',
  beijing_gov_whlyj_street_146: '成寿寺街道综合文化中心',
  beijing_gov_whlyj_street_147: '苹果园街道',
  beijing_gov_whlyj_street_148: '老山街道',
  beijing_gov_whlyj_street_149: '鲁谷街道',
  beijing_gov_whlyj_street_150: '八宝山街道',
  beijing_gov_whlyj_street_151: '八角街道',
  beijing_gov_whlyj_street_152: '古城街道',
  beijing_gov_whlyj_street_153: '金顶街街道',
  beijing_gov_whlyj_street_154: '广宁街道',
  beijing_gov_whlyj_street_155: '五里坨街道',
  beijing_gov_whlyj_street_156: '大峪街道',
  beijing_gov_whlyj_street_157: '城子街道',
  beijing_gov_whlyj_street_158: '东辛房街道',
  beijing_gov_whlyj_street_159: '大台街道',
  beijing_gov_whlyj_street_160: '王平镇',
  beijing_gov_whlyj_street_161: '龙泉镇',
  beijing_gov_whlyj_street_162: '潭柘寺镇',
  beijing_gov_whlyj_street_163: '军庄镇',
  beijing_gov_whlyj_street_164: '雁翅镇',
  beijing_gov_whlyj_street_165: '斋堂镇',
  beijing_gov_whlyj_street_166: '清水镇',
  beijing_gov_whlyj_street_167: '妙峰山镇',
  beijing_gov_whlyj_street_168: '永定镇',
  beijing_gov_whlyj_street_169: '城关街道',
  beijing_gov_whlyj_street_170: '拱辰街道',
  beijing_gov_whlyj_street_171: '西潞街道',
  beijing_gov_whlyj_street_172: '长阳镇',
  beijing_gov_whlyj_street_173: '琉璃河镇',
  beijing_gov_whlyj_street_174: '窦店镇1',
  beijing_gov_whlyj_street_175: '窦店镇2',
  beijing_gov_whlyj_street_176: '韩村河镇',
  beijing_gov_whlyj_street_177: '阎村镇',
  beijing_gov_whlyj_street_178: '良乡镇',
  beijing_gov_whlyj_street_179: '青龙湖镇',
  beijing_gov_whlyj_street_180: '周口店镇',
  beijing_gov_whlyj_street_181: '石楼镇',
  beijing_gov_whlyj_street_182: '长沟镇',
  beijing_gov_whlyj_street_183: '大石窝镇',
  beijing_gov_whlyj_street_184: '张坊镇',
  beijing_gov_whlyj_street_185: '河北镇',
  beijing_gov_whlyj_street_186: '佛子庄乡',
  beijing_gov_whlyj_street_187: '十渡镇',
  beijing_gov_whlyj_street_188: '蒲洼乡',
  beijing_gov_whlyj_street_189: '霞云岭乡',
  beijing_gov_whlyj_street_190: '史家营乡',
  beijing_gov_whlyj_street_191: '南窖乡',
  beijing_gov_whlyj_street_192: '大安山乡',
  beijing_gov_whlyj_street_193: '新镇街道',
  beijing_gov_whlyj_street_195: '东风街道',
  beijing_gov_whlyj_street_196: '迎风街道',
  beijing_gov_whlyj_street_197: '向阳街道',
  beijing_gov_whlyj_street_198: '星城街道',
  beijing_gov_whlyj_street_199: '潞城镇综合文化中心',
  beijing_gov_whlyj_street_200: '九棵树街道综合文化中心',
  beijing_gov_whlyj_street_201: '西集镇文体活动中心',
  beijing_gov_whlyj_street_202: '临河里街道综合文化中心',
  beijing_gov_whlyj_street_203: '台湖镇文体活动中心',
  beijing_gov_whlyj_street_204: '北苑街道文体活动中心',
  beijing_gov_whlyj_street_205: '北苑街道文化活动中心',
  beijing_gov_whlyj_street_206: '于家务回族乡综合文化中心',
  beijing_gov_whlyj_street_207: '潞邑街道综合文化中心',
  beijing_gov_whlyj_street_208: '潞源街道综合文化中心',
  beijing_gov_whlyj_street_209: '宋庄镇综合文化中心',
  beijing_gov_whlyj_street_210: '中仓街道综合文化中心',
  beijing_gov_whlyj_street_211: '马驹桥镇综合文化中心',
  beijing_gov_whlyj_street_212: '通运街道综合文化中心',
  beijing_gov_whlyj_street_213: '玉桥街道综合文化中心',
  beijing_gov_whlyj_street_214: '杨庄街道综合文化中心',
  beijing_gov_whlyj_street_215: '张家湾镇综合文化中心',
  beijing_gov_whlyj_street_216: '永顺镇综合文化中心',
  beijing_gov_whlyj_street_217: '新华街道综合文化中心',
  beijing_gov_whlyj_street_218: '漷县书院',
  beijing_gov_whlyj_street_219: '永乐店镇综合文化中心',
  beijing_gov_whlyj_street_220: '文景街道综合文化中心',
  beijing_gov_whlyj_street_221: '梨园镇文化活动中心',
  beijing_gov_whlyj_street_222: '后沙峪镇',
  beijing_gov_whlyj_street_223: '北务镇',
  beijing_gov_whlyj_street_224: '赵全营镇',
  beijing_gov_whlyj_street_225: '张镇',
  beijing_gov_whlyj_street_226: '高丽营镇',
  beijing_gov_whlyj_street_227: '马坡镇',
  beijing_gov_whlyj_street_228: '仁和镇',
  beijing_gov_whlyj_street_229: '天竺镇',
  beijing_gov_whlyj_street_230: '牛栏山镇',
  beijing_gov_whlyj_street_231: '北石槽镇',
  beijing_gov_whlyj_street_232: '南彩镇',
  beijing_gov_whlyj_street_233: '木林镇',
  beijing_gov_whlyj_street_234: '北小营镇',
  beijing_gov_whlyj_street_235: '大孙各庄镇',
  beijing_gov_whlyj_street_236: '龙湾屯镇',
  beijing_gov_whlyj_street_237: '李遂镇',
  beijing_gov_whlyj_street_238: '南法信镇',
  beijing_gov_whlyj_street_239: '李桥镇',
  beijing_gov_whlyj_street_240: '杨镇',
  beijing_gov_whlyj_street_241: '空港街道',
  beijing_gov_whlyj_street_242: '光明街道',
  beijing_gov_whlyj_street_243: '旺泉街道',
  beijing_gov_whlyj_street_244: '双丰街道',
  beijing_gov_whlyj_street_245: '石园街道',
  beijing_gov_whlyj_street_246: '胜利街道',
  beijing_gov_whlyj_street_247: '清源街道',
  beijing_gov_whlyj_street_248: '林校路街道',
  beijing_gov_whlyj_street_250: '兴丰街道',
  beijing_gov_whlyj_street_252: '观音寺街道',
  beijing_gov_whlyj_street_253: '天宫院街道',
  beijing_gov_whlyj_street_255: '高米店街道',
  beijing_gov_whlyj_street_257: '荣华街道',
  beijing_gov_whlyj_street_258: '博兴街道',
  beijing_gov_whlyj_street_259: '黄村镇',
  beijing_gov_whlyj_street_261: '西红门镇',
  beijing_gov_whlyj_street_262: '采育镇',
  beijing_gov_whlyj_street_263: '青云店镇',
  beijing_gov_whlyj_street_264: '瀛海镇',
  beijing_gov_whlyj_street_265: '长子营镇',
  beijing_gov_whlyj_street_266: '旧宫镇',
  beijing_gov_whlyj_street_268: '魏善庄镇',
  beijing_gov_whlyj_street_269: '礼贤镇',
  beijing_gov_whlyj_street_271: '安定镇',
  beijing_gov_whlyj_street_272: '北臧村镇',
  beijing_gov_whlyj_street_273: '庞各庄镇',
  beijing_gov_whlyj_street_274: '榆垡镇',
  beijing_gov_whlyj_street_275: '亦庄镇',
  beijing_gov_whlyj_street_277: '城北街道',
  beijing_gov_whlyj_street_279: '马池口镇',
  beijing_gov_whlyj_street_280: '南邵镇',
  beijing_gov_whlyj_street_281: '天通苑南街道',
  beijing_gov_whlyj_street_282: '东小口镇',
  beijing_gov_whlyj_street_283: '北七家镇',
  beijing_gov_whlyj_street_284: '流村镇',
  beijing_gov_whlyj_street_285: '沙河镇',
  beijing_gov_whlyj_street_286: '霍营街道',
  beijing_gov_whlyj_street_287: '十三陵镇',
  beijing_gov_whlyj_street_288: '天通苑北街道',
  beijing_gov_whlyj_street_289: '崔村镇',
  beijing_gov_whlyj_street_290: '阳坊镇',
  beijing_gov_whlyj_street_292: '延寿镇',
  beijing_gov_whlyj_street_293: '小汤山镇',
  beijing_gov_whlyj_street_294: '百善镇',
  beijing_gov_whlyj_street_295: '南口镇',
  beijing_gov_whlyj_street_296: '回龙观街道',
  beijing_gov_whlyj_street_298: '兴寿镇',
  beijing_gov_whlyj_street_300: '城南街道',
  beijing_gov_whlyj_street_301: '龙泽园街道',
  beijing_gov_whlyj_street_302: '史各庄街道',
  beijing_gov_whlyj_street_303: '东高村镇',
  beijing_gov_whlyj_street_304: '滨河街道',
  beijing_gov_whlyj_street_305: '大华山镇',
  beijing_gov_whlyj_street_306: '大兴庄镇',
  beijing_gov_whlyj_street_307: '黄松峪乡',
  beijing_gov_whlyj_street_308: '金海湖镇',
  beijing_gov_whlyj_street_309: '刘家店镇',
  beijing_gov_whlyj_street_310: '马昌营镇',
  beijing_gov_whlyj_street_311: '马坊镇',
  beijing_gov_whlyj_street_312: '南独乐河镇',
  beijing_gov_whlyj_street_313: '平谷镇',
  beijing_gov_whlyj_street_314: '山东庄镇',
  beijing_gov_whlyj_street_315: '王辛庄镇',
  beijing_gov_whlyj_street_316: '夏各庄镇',
  beijing_gov_whlyj_street_317: '兴谷街道',
  beijing_gov_whlyj_street_318: '熊儿寨乡',
  beijing_gov_whlyj_street_319: '峪口镇',
  beijing_gov_whlyj_street_320: '镇罗营镇',
  beijing_gov_whlyj_street_321: '庙城镇综合文化中心',
  beijing_gov_whlyj_street_322: '雁栖镇综合文化中心',
  beijing_gov_whlyj_street_323: '九渡河综合文化中心',
  beijing_gov_whlyj_street_324: '琉璃庙镇综合文化中心',
  beijing_gov_whlyj_street_325: '宝山镇综合文化中心',
  beijing_gov_whlyj_street_326: '长哨营满族乡综合文化中心',
  beijing_gov_whlyj_street_327: '喇叭沟门满族乡综合文化中心',
  beijing_gov_whlyj_street_328: '怀柔镇综合文化中心',
  beijing_gov_whlyj_street_329: '桥梓镇综合文化中心',
  beijing_gov_whlyj_street_330: '北房镇综合文化中心',
  beijing_gov_whlyj_street_331: '杨宋镇综合文化中心',
  beijing_gov_whlyj_street_332: '怀北镇综合文化中心',
  beijing_gov_whlyj_street_333: '渤海镇综合文化中心',
  beijing_gov_whlyj_street_334: '河口镇综合文化中心',
  beijing_gov_whlyj_street_335: '龙山街道综合文化中心',
  beijing_gov_whlyj_street_336: '泉河街道综合文化中心',
  beijing_gov_whlyj_street_337: '密云区溪翁庄镇综合文化中心',
  beijing_gov_whlyj_street_338: '密云区北庄镇综合文化中心',
  beijing_gov_whlyj_street_339: '密云区冯家峪镇综合文化中心',
  beijing_gov_whlyj_street_340: '密云区巨各庄镇综合文化中心',
  beijing_gov_whlyj_street_341: '密云区穆家峪镇综合文化中心',
  beijing_gov_whlyj_street_342: '密云区大城子镇综合文化中心',
  beijing_gov_whlyj_street_343: '密云区古北口镇综合文化中心',
  beijing_gov_whlyj_street_344: '密云区不老屯镇综合文化中心',
  beijing_gov_whlyj_street_345: '密云区高岭镇综合文化中心',
  beijing_gov_whlyj_street_346: '密云区河南寨镇综合文化中心',
  beijing_gov_whlyj_street_347: '密云区太师屯镇综合文化中心',
  beijing_gov_whlyj_street_348: '密云区东邵渠镇综合文化中心',
  beijing_gov_whlyj_street_349: '密云区石城镇综合文化中心',
  beijing_gov_whlyj_street_350: '密云区新城子镇综合文化中心',
  beijing_gov_whlyj_street_351: '密云区西田各庄镇综合文化中心',
  beijing_gov_whlyj_street_352: '密云区十里堡镇综合文化中心',
  beijing_gov_whlyj_street_353: '密云区密云镇综合文化中心',
  beijing_gov_whlyj_street_354: '檀营地区综合文化中心',
  beijing_gov_whlyj_street_355: '密云区果园街道综合文化中心',
  beijing_gov_whlyj_street_356: '密云区鼓楼街道综合文化中心',
  beijing_gov_whlyj_street_357: '八达岭镇',
  beijing_gov_whlyj_street_358: '百泉街道',
  beijing_gov_whlyj_street_359: '井庄镇',
  beijing_gov_whlyj_street_360: '旧县镇文体中心',
  beijing_gov_whlyj_street_361: '康庄镇',
  beijing_gov_whlyj_street_362: '刘斌堡乡',
  beijing_gov_whlyj_street_363: '千家店镇',
  beijing_gov_whlyj_street_364: '儒林街道',
  beijing_gov_whlyj_street_365: '沈家营镇',
  beijing_gov_whlyj_street_366: '四海镇',
  beijing_gov_whlyj_street_367: '香水园街道',
  beijing_gov_whlyj_street_368: '永宁镇',
  beijing_gov_whlyj_street_369: '张山营镇',
  beijing_gov_whlyj_street_370: '珍珠泉乡',
  beijing_gov_whlyj_street_371: '大庄科乡',
  beijing_gov_whlyj_street_372: '延庆镇文体中心',
  beijing_gov_whlyj_street_373: '香营乡文体中心',
  beijing_gov_whlyj_street_374: '大榆树镇',
  beijing_gov_whlyj_perf_1: '国家大剧院音乐厅',
  beijing_gov_whlyj_perf_2: '国家大剧院戏剧场',
  beijing_gov_whlyj_perf_3: '国家大剧院歌剧院',
  beijing_gov_whlyj_perf_4: '国家大剧院小剧场',
  beijing_gov_whlyj_perf_6: '人艺实验剧场',
  beijing_gov_whlyj_perf_7: '菊隐剧场',
  beijing_gov_whlyj_perf_8: '中国儿童剧场',
  beijing_gov_whlyj_perf_9: '假日经典小剧场',
  beijing_gov_whlyj_perf_11: '北京世纪剧院',
  beijing_gov_whlyj_perf_12: '北京天桥剧场',
  beijing_gov_whlyj_perf_13: '天桥艺术中心大剧场',
  beijing_gov_whlyj_perf_14: '天桥艺术中心中剧场',
  beijing_gov_whlyj_perf_15: '天桥艺术中心小剧场',
  beijing_gov_whlyj_perf_16: '天桥艺术中心多功能剧场',
  beijing_gov_whlyj_perf_17: '保利剧院',
  beijing_gov_whlyj_perf_18: '民族宫大剧院',
  beijing_gov_whlyj_perf_19: '海淀剧院',
  beijing_gov_whlyj_perf_24: '中国木偶艺术剧院大厅',
  beijing_gov_whlyj_perf_25: '中国木偶艺术剧院小铃铛剧场',
  beijing_gov_whlyj_perf_26: '中国评剧大剧院大剧场',
  beijing_gov_whlyj_perf_27: '中国评剧大剧院小剧场',
  beijing_gov_whlyj_perf_28: '德云社天桥剧场',
  beijing_gov_whlyj_perf_29: '东图会议中心剧场',
  beijing_gov_whlyj_perf_30: '北京朝阳剧场',
  beijing_gov_whlyj_perf_31: '刘老根大舞台',
  beijing_gov_whlyj_perf_32: '老舍茶馆(含新京调)',
  beijing_gov_whlyj_perf_33: '湖广会馆大戏楼',
  beijing_gov_whlyj_perf_34: '前门梨园剧场',
  beijing_gov_whlyj_perf_35: '崇文工人文化宫',
  beijing_gov_whlyj_perf_36: '国话先锋剧场',
  beijing_gov_whlyj_perf_37: '繁星戏剧村（2个厅）',
  beijing_gov_whlyj_perf_38: '北京地质礼堂',
  beijing_gov_whlyj_perf_39: '北京蜂巢剧场',
  beijing_gov_whlyj_perf_40: '北京蓬蒿人剧场',
  beijing_gov_whlyj_perf_41: '海淀工人文化宫',
  beijing_gov_whlyj_perf_42: '雷剧场',
  beijing_gov_whlyj_perf_43: '鼓楼西剧场',
  beijing_gov_whlyj_perf_44: '中国儿童中心剧场',
  beijing_gov_whlyj_perf_45: '北京西区剧场',
  beijing_gov_whlyj_perf_46: '国图艺术中心（原国图音乐厅）',
  beijing_gov_whlyj_perf_47: '嘻哈包袱铺交道口店',
  chongqing_gov_bowuguan_1: '重庆中国三峡博物馆(重庆博物馆)',
  chongqing_gov_bowuguan_2: '红岩革命纪念馆（重庆红岩革命历史博物馆）',
  chongqing_gov_bowuguan_3: '重庆歌乐山革命纪念馆（重庆红岩革命历史博物馆）',
  chongqing_gov_bowuguan_4: '大足石刻博物馆',
  chongqing_gov_bowuguan_6: '重庆大韩民国临时政府旧址陈列馆',
  chongqing_gov_bowuguan_8: '重庆特园民主党派历史陈列馆（中国民主党派历史陈列馆）',
  chongqing_gov_bowuguan_9: '重庆历史名人馆',
  chongqing_gov_bowuguan_10: '重庆抗战戏剧博物馆',
  chongqing_gov_bowuguan_11: '重庆史迪威博物馆（史迪威研究中心）',
  chongqing_gov_bowuguan_12: '重庆体育博物馆',
  chongqing_gov_bowuguan_13: '重庆典籍博物馆',
  chongqing_gov_bowuguan_14: '二厂记忆博物馆',
  chongqing_gov_bowuguan_16: '重庆嘉陵江索道博物馆',
  chongqing_gov_bowuguan_17: '重庆自然资源科普馆',
  chongqing_gov_bowuguan_19: '重庆师范大学博物馆',
  chongqing_gov_bowuguan_20: '重庆警察博物馆',
  chongqing_gov_bowuguan_21: '重庆市规划展览馆',
  chongqing_gov_bowuguan_22: '西南大学历史博物馆',
  chongqing_gov_bowuguan_23: '中国西部科学院旧址陈列馆',
  chongqing_gov_bowuguan_24: '重庆电信博物馆',
  chongqing_gov_bowuguan_25: '重庆川剧博物馆',
  chongqing_gov_bowuguan_26: '重庆白鹤梁水下博物馆',
  chongqing_gov_bowuguan_27: '重庆三峡移民纪念馆',
  chongqing_gov_bowuguan_28: '重庆市万州区博物馆',
  chongqing_gov_bowuguan_29: '重庆市万州革命烈士陵园管理中心',
  chongqing_gov_bowuguan_30: '重庆市万州良公祠民俗博物馆',
  chongqing_gov_bowuguan_31: '万县“九五”惨案纪念馆',
  chongqing_gov_bowuguan_32: '重庆市万州区三峡石博物馆',
  chongqing_gov_bowuguan_33: '重庆市民族博物馆',
  chongqing_gov_bowuguan_34: '万涛故居',
  chongqing_gov_bowuguan_35: '黔江区博物馆',
  chongqing_gov_bowuguan_36: '重庆市涪陵区博物馆',
  chongqing_gov_bowuguan_37: '重庆市渝中区博物馆',
  chongqing_gov_bowuguan_38: '重庆“湖广填四川”移民博物馆（重庆湖广会馆）',
  chongqing_gov_bowuguan_39: '王琦美术博物馆',
  chongqing_gov_bowuguan_40: '重庆巴渝民间中医药博物馆',
  chongqing_gov_bowuguan_41: '重庆市巴渝名匾文化艺术博物馆',
  chongqing_gov_bowuguan_42: '重庆市渝中区友好飞虎队博物馆',
  chongqing_gov_bowuguan_43: '重庆市渝中区巴渝民风博物馆',
  chongqing_gov_bowuguan_44: '重庆大轰炸遗址陈列馆',
  chongqing_gov_bowuguan_45: '重庆金融历史博物馆',
  chongqing_gov_bowuguan_46: '渝中区古典戏法魔术博物馆',
  chongqing_gov_bowuguan_47: '重庆市大渡口区博物馆',
  chongqing_gov_bowuguan_48: '明玉珍睿陵陈列馆',
  chongqing_gov_bowuguan_49: '重庆金融博物馆',
  chongqing_gov_bowuguan_50: '重庆旁观者设计博物馆',
  chongqing_gov_bowuguan_51: '重庆市沙坪坝博物馆（重庆市沙坪坝区巴蜀古代建筑博物馆）',
  chongqing_gov_bowuguan_52: '重庆郭沫若纪念馆',
  chongqing_gov_bowuguan_53: '重庆张治中纪念馆',
  chongqing_gov_bowuguan_54: '重庆冯玉祥纪念馆',
  chongqing_gov_bowuguan_55: '重庆抗战教育博物馆',
  chongqing_gov_bowuguan_56: '重庆沙坪坝地质博物馆',
  chongqing_gov_bowuguan_57: '重庆市九龙坡区重庆巴人博物馆',
  chongqing_gov_bowuguan_58: '刘伯承六店旧居纪念馆（刘伯承六店旧居管理中心）',
  chongqing_gov_bowuguan_59: '重庆华岩佛教博物馆',
  chongqing_gov_bowuguan_60: '重庆三耳火锅博物馆',
  chongqing_gov_bowuguan_61: '重庆市九龙坡区黄桷坪钢琴博物馆',
  chongqing_gov_bowuguan_62: '重庆市九龙坡区九龙沉香博物馆',
  chongqing_gov_bowuguan_63: '重庆市九龙坡区建川博物馆',
  chongqing_gov_bowuguan_64: '重庆市九龙坡区周君记火锅调料历史文化博物馆',
  chongqing_gov_bowuguan_65: '重庆抗战遗址博物馆',
  chongqing_gov_bowuguan_66: '南岸区博物馆',
  chongqing_gov_bowuguan_67: '重庆市中医药博物馆',
  chongqing_gov_bowuguan_68: '重庆市南岸区德庄火锅博物馆',
  chongqing_gov_bowuguan_69: '重庆市北碚区博物馆',
  chongqing_gov_bowuguan_70: '卢作孚纪念馆',
  chongqing_gov_bowuguan_71: '四世同堂纪念馆',
  chongqing_gov_bowuguan_72: '梁实秋纪念馆',
  chongqing_gov_bowuguan_73: '抗战时期荣誉军人自治实验区陈列馆（重庆市北碚区博物馆分馆）',
  chongqing_gov_bowuguan_74: '晏阳初纪念馆（重庆市北碚区博物馆分馆）',
  chongqing_gov_bowuguan_75: '国立复旦大学重庆旧址（抗战时期复旦大学校史纪念馆）',
  chongqing_gov_bowuguan_76: '中共中央西南局缙云山办公地旧址陈列馆',
  chongqing_gov_bowuguan_77: '张自忠烈士陵园',
  chongqing_gov_bowuguan_78: '王朴烈士陵园',
  chongqing_gov_bowuguan_79: '北碚教育博物馆',
  chongqing_gov_bowuguan_80: '重庆巴渝民俗博物馆',
  chongqing_gov_bowuguan_81: '重庆宝林博物馆',
  chongqing_gov_bowuguan_82: '重庆市渝北区渝都古典照相机缝纫机博物馆',
  chongqing_gov_bowuguan_83: '重庆御临旅游纪念品博物馆',
  chongqing_gov_bowuguan_84: '重庆市巴南区博物馆',
  chongqing_gov_bowuguan_85: '重庆长江石文化艺术博物馆',
  chongqing_gov_bowuguan_86: '重庆市巴南区江碧波艺术博物馆',
  chongqing_gov_bowuguan_87: '重庆市长寿区博物馆',
  chongqing_gov_bowuguan_88: '重庆市长寿区杨克明故居陈列馆',
  chongqing_gov_bowuguan_89: '江津博物馆',
  chongqing_gov_bowuguan_90: '聂荣臻元帅陈列馆',
  chongqing_gov_bowuguan_91: '重庆市江津区陈独秀旧居陈列馆',
  chongqing_gov_bowuguan_92: '中等师范教育历史陈列馆',
  chongqing_gov_bowuguan_93: '陶行知先生纪念馆',
  chongqing_gov_bowuguan_94: '钓鱼城古战场遗址博物馆',
  chongqing_gov_bowuguan_95: '重庆友军辣椒博物馆',
  chongqing_gov_bowuguan_96: '重庆市合川区三江民俗博物馆',
  chongqing_gov_bowuguan_97: '合川区楠山坊金丝楠木博物馆',
  chongqing_gov_bowuguan_98: '永川博物馆（陈子庄艺术陈列馆）',
  chongqing_gov_bowuguan_99: '重庆市永川堃航博物馆',
  chongqing_gov_bowuguan_100: '重庆市永川区蕴宝博物馆',
  chongqing_gov_bowuguan_101: '南川区博物馆',
  chongqing_gov_bowuguan_102: '重庆市南川区蝶语昆虫博物馆',
  chongqing_gov_bowuguan_103: '綦江博物馆',
  chongqing_gov_bowuguan_104: '重庆市綦江区红军长征纪念馆',
  chongqing_gov_bowuguan_105: '饶国梁纪念馆',
  chongqing_gov_bowuguan_106: '重庆市大足区红岩重型汽车博物馆',
  chongqing_gov_bowuguan_107: '重庆大圆祥博物馆',
  chongqing_gov_bowuguan_108: '铜梁区博物馆',
  chongqing_gov_bowuguan_109: '铜梁木匾博物馆',
  chongqing_gov_bowuguan_110: '重庆市铜梁区邱少云烈士纪念馆',
  chongqing_gov_bowuguan_111: '潼南区博物馆',
  chongqing_gov_bowuguan_112: '杨闇公杨尚昆旧居陈列馆（重庆市潼南区杨尚昆故里管理处）',
  chongqing_gov_bowuguan_113: '荣昌陶博物馆',
  chongqing_gov_bowuguan_114: '张培爵纪念馆',
  chongqing_gov_bowuguan_115: '重庆市荣昌区万灵提琴博物馆',
  chongqing_gov_bowuguan_116: '重庆市荣昌陶窑口博物馆',
  chongqing_gov_bowuguan_117: '刘伯承同志纪念馆',
  chongqing_gov_bowuguan_118: '重庆市开州博物馆',
  chongqing_gov_bowuguan_119: '重庆市开州区雨青博物馆',
  chongqing_gov_bowuguan_120: '重庆市梁平区博物馆',
  chongqing_gov_bowuguan_121: '重庆市武隆博物馆',
  chongqing_gov_bowuguan_122: '后坪坝苏维埃政府史迹展览馆',
  chongqing_gov_bowuguan_123: '和平中学旧址陈列馆',
  chongqing_gov_bowuguan_124: '川陕苏区城口纪念馆',
  chongqing_gov_bowuguan_125: '城口县红三十三军指挥部旧址群陈列馆',
  chongqing_gov_bowuguan_126: '丰都县博物馆',
  chongqing_gov_bowuguan_127: '垫江县博物馆',
  chongqing_gov_bowuguan_128: '忠州博物馆',
  chongqing_gov_bowuguan_129: '忠县石宝寨',
  chongqing_gov_bowuguan_130: '云阳县博物馆',
  chongqing_gov_bowuguan_131: '张桓侯庙博物馆',
  chongqing_gov_bowuguan_132: '云阳古建博物苑',
  chongqing_gov_bowuguan_133: '云阳县彭咏梧纪念馆',
  chongqing_gov_bowuguan_134: '云阳县非物质文化遗产博物馆',
  chongqing_gov_bowuguan_135: '奉节县夔州博物馆',
  chongqing_gov_bowuguan_136: '奉节县白帝城博物馆',
  chongqing_gov_bowuguan_137: '奉节县瞿塘关遗址博物馆',
  chongqing_gov_bowuguan_138: '奉节县诗城博物馆',
  chongqing_gov_bowuguan_139: '巫山博物馆',
  chongqing_gov_bowuguan_140: '巫山县李季达陈列馆',
  chongqing_gov_bowuguan_141: '巫山县下庄人事迹陈列馆',
  chongqing_gov_bowuguan_142: '巫山县长康博物馆',
  chongqing_gov_bowuguan_143: '巫溪县博物馆',
  chongqing_gov_bowuguan_144: '石柱土家族自治县博物馆',
  chongqing_gov_bowuguan_145: '秀山土家族苗族自治县民族博物馆',
  chongqing_gov_bowuguan_146: '刘邓大军挺进大西南司令部旧址陈列馆',
  chongqing_gov_bowuguan_147: '酉阳土家族苗族自治县酉州博物馆',
  chongqing_gov_bowuguan_148: '酉阳土家族苗族自治县赵世炎烈士纪念馆',
  chongqing_gov_bowuguan_149: '南腰界红三军司令部旧址陈列馆',
  chongqing_gov_bowuguan_150: '彭水苗族土家族自治县博物馆',
  chongqing_gov_bowuguan_151: '九黎苗族历史文化博物馆',
  chongqing_gov_bowuguan_152: '重庆市万盛经济技术开发区博物馆',
  chongqing_gov_tushuguan_2: '重庆市少年儿童图书馆',
  chongqing_gov_tushuguan_3: '重庆市万州区图书馆',
  chongqing_gov_tushuguan_4: '重庆市黔江区图书馆',
  chongqing_gov_tushuguan_5: '重庆市涪陵区图书馆',
  chongqing_gov_tushuguan_6: '重庆市渝中区图书馆',
  chongqing_gov_tushuguan_7: '重庆市大渡口区图书馆',
  chongqing_gov_tushuguan_8: '重庆市江北区图书馆',
  chongqing_gov_tushuguan_9: '重庆市沙坪坝区图书馆',
  chongqing_gov_tushuguan_10: '重庆市九龙坡区图书馆',
  chongqing_gov_tushuguan_11: '重庆市南岸区图书馆',
  chongqing_gov_tushuguan_12: '重庆市北碚图书馆',
  chongqing_gov_tushuguan_13: '重庆市渝北区图书馆',
  chongqing_gov_tushuguan_14: '重庆市巴南区图书馆',
  chongqing_gov_tushuguan_15: '重庆市长寿区图书馆',
  chongqing_gov_tushuguan_16: '重庆市江津区图书馆',
  chongqing_gov_tushuguan_17: '重庆市合川区图书馆',
  chongqing_gov_tushuguan_18: '重庆市南川区图书馆',
  chongqing_gov_tushuguan_19: '重庆市大足区图书馆',
  chongqing_gov_tushuguan_20: '重庆市双桥经开区图书馆',
  chongqing_gov_tushuguan_21: '重庆市万盛经济技术开发区图书馆',
  chongqing_gov_tushuguan_22: '重庆市綦江区图书馆',
  chongqing_gov_tushuguan_23: '重庆市永川区图书馆',
  chongqing_gov_tushuguan_24: '重庆市潼南区图书馆（新馆）',
  chongqing_gov_tushuguan_25: '重庆市璧山区图书馆',
  chongqing_gov_tushuguan_26: '重庆市铜梁区图书馆',
  chongqing_gov_tushuguan_27: '重庆市荣昌区图书馆',
  chongqing_gov_tushuguan_28: '重庆市梁平区图书馆',
  chongqing_gov_tushuguan_29: '重庆市武隆区图书馆',
  chongqing_gov_tushuguan_30: '重庆市开州区图书馆',
  chongqing_gov_tushuguan_31: '重庆市城口县图书馆',
  chongqing_gov_tushuguan_32: '重庆市丰都县图书馆',
  chongqing_gov_tushuguan_33: '重庆市垫江县图书馆',
  chongqing_gov_tushuguan_34: '重庆市忠县图书馆',
  chongqing_gov_tushuguan_35: '重庆市云阳县图书馆',
  chongqing_gov_tushuguan_36: '重庆市奉节县图书馆',
  chongqing_gov_tushuguan_37: '重庆市巫山县图书馆',
  chongqing_gov_tushuguan_38: '重庆市巫溪县图书馆',
  chongqing_gov_tushuguan_39: '重庆市石柱土家族自治县图书馆',
  chongqing_gov_tushuguan_40: '重庆市秀山土家族苗族自治县图书馆',
  chongqing_gov_tushuguan_41: '重庆市酉阳土家族苗族自治县图书馆',
  chongqing_gov_tushuguan_42: '重庆市彭水苗族土家族自治县图书馆',
  chongqing_gov_wenhuaguan_1: '重庆市群众艺术馆',
  chongqing_gov_wenhuaguan_2: '重庆市万州区文化馆',
  chongqing_gov_wenhuaguan_3: '重庆市涪陵区文化馆',
  chongqing_gov_wenhuaguan_4: '重庆市渝中区文化馆',
  chongqing_gov_wenhuaguan_5: '重庆市大渡口区文化馆',
  chongqing_gov_wenhuaguan_6: '重庆市江北区文化馆',
  chongqing_gov_wenhuaguan_7: '重庆市沙坪坝区文化馆',
  chongqing_gov_wenhuaguan_8: '重庆市九龙坡区文化馆',
  chongqing_gov_wenhuaguan_9: '重庆市南岸区文化馆',
  chongqing_gov_wenhuaguan_10: '重庆市北碚区文化馆',
  chongqing_gov_wenhuaguan_11: '重庆市綦江区文化馆',
  chongqing_gov_wenhuaguan_12: '重庆市大足区文化馆',
  chongqing_gov_wenhuaguan_13: '重庆市双桥经开区文化馆',
  chongqing_gov_wenhuaguan_14: '重庆市渝北区文化馆',
  chongqing_gov_wenhuaguan_15: '重庆市巴南区文化馆',
  chongqing_gov_wenhuaguan_16: '重庆市黔江区民族文化艺术馆',
  chongqing_gov_wenhuaguan_17: '重庆市长寿区文化馆',
  chongqing_gov_wenhuaguan_18: '重庆市江津区文化馆',
  chongqing_gov_wenhuaguan_19: '重庆市合川区文化馆',
  chongqing_gov_wenhuaguan_20: '重庆市永川区文化艺术馆',
  chongqing_gov_wenhuaguan_21: '重庆市南川区文化馆',
  chongqing_gov_wenhuaguan_22: '重庆市璧山区文化馆',
  chongqing_gov_wenhuaguan_23: '重庆市万盛经开区文化馆',
  chongqing_gov_wenhuaguan_24: '重庆市铜梁区文化馆',
  chongqing_gov_wenhuaguan_25: '重庆市潼南区文化馆',
  chongqing_gov_wenhuaguan_26: '重庆市荣昌区文化馆',
  chongqing_gov_wenhuaguan_27: '重庆市开州区文化馆',
  chongqing_gov_wenhuaguan_28: '重庆市梁平区文化馆',
  chongqing_gov_wenhuaguan_29: '重庆市武隆区文化馆',
  chongqing_gov_wenhuaguan_30: '重庆市城口县文化馆',
  chongqing_gov_wenhuaguan_31: '重庆市丰都县文化馆',
  chongqing_gov_wenhuaguan_32: '重庆市垫江县文化馆',
  chongqing_gov_wenhuaguan_33: '重庆市忠县文化馆',
  chongqing_gov_wenhuaguan_34: '重庆市云阳县文化馆',
  chongqing_gov_wenhuaguan_35: '重庆市奉节县文化馆',
  chongqing_gov_wenhuaguan_36: '重庆市巫山县文化馆',
  chongqing_gov_wenhuaguan_37: '重庆市巫溪县文化馆',
  chongqing_gov_wenhuaguan_38: '重庆市石柱土家族自治县文化馆',
  chongqing_gov_wenhuaguan_39: '重庆市秀山土家族苗族自治县文化馆',
  chongqing_gov_wenhuaguan_40: '重庆市酉阳土家族苗族自治县文化馆',
  chongqing_gov_wenhuaguan_41: '重庆市彭水苗族土家族自治县文化馆',
  chongqing_gov_tiyu_1: '重庆市体育馆',
  chongqing_gov_tiyu_2: '重庆市大田湾体育场',
  chongqing_gov_tiyu_3: '重庆市奥林匹克体育中心体育场',
  chongqing_gov_tiyu_4: '重庆市奥林匹克体育中心游泳跳水馆',
  chongqing_gov_tiyu_6: '万州游泳（跳水）馆',
  chongqing_gov_tiyu_7: '万州区三峡之星体育馆',
  chongqing_gov_tiyu_8: '万州体育场',
  chongqing_gov_tiyu_9: '涪陵区体育场',
  chongqing_gov_tiyu_10: '涪陵区体育馆',
  chongqing_gov_tiyu_11: '大渡口区体育馆',
  chongqing_gov_tiyu_12: '江南体育中心体育训练场',
  chongqing_gov_tiyu_13: '江南体育中心综合馆',
  chongqing_gov_tiyu_14: '江南游泳馆',
  chongqing_gov_tiyu_15: '江南体育馆',
  chongqing_gov_tiyu_16: '北陪区缙云体育中心体育场',
  chongqing_gov_tiyu_17: '北陪区绪云体育中心体育馆',
  chongqing_gov_tiyu_18: '万盛文体中心体育馆',
  chongqing_gov_tiyu_19: '万盛文体中心体育场',
  chongqing_gov_tiyu_20: '万盛滨江路体育馆',
  chongqing_gov_tiyu_21: '万盛游泳馆',
  chongqing_gov_tiyu_22: '綦江体育中心体育场',
  chongqing_gov_tiyu_23: '綦江区体育馆',
  chongqing_gov_tiyu_24: '大足区体育中心游泳馆',
  chongqing_gov_tiyu_25: '大足区体育中心体育馆',
  chongqing_gov_tiyu_26: '大足区体育中心体育场',
  chongqing_gov_tiyu_27: '黔江区游泳馆',
  chongqing_gov_tiyu_28: '黔江区体育场',
  chongqing_gov_tiyu_29: '黔江区体育馆',
  chongqing_gov_tiyu_30: '长寿区体育中心体育馆',
  chongqing_gov_tiyu_31: '长寿区体育场',
  chongqing_gov_tiyu_32: '江津区体育馆',
  chongqing_gov_tiyu_33: '江津区体育场',
  chongqing_gov_tiyu_34: '江津区游泳馆',
  chongqing_gov_tiyu_35: '江津区全民健身指导中心（区羽毛球馆）',
  chongqing_gov_tiyu_36: '合川区体育馆',
  chongqing_gov_tiyu_37: '永川区游泳馆',
  chongqing_gov_tiyu_38: '永川区体育中心体育场',
  chongqing_gov_tiyu_39: '永川区体育馆',
  chongqing_gov_tiyu_40: '南川区体育场',
  chongqing_gov_tiyu_41: '南川区体育馆',
  chongqing_gov_tiyu_43: '璧山区体育馆',
  chongqing_gov_tiyu_44: '璧山区体育中心',
  chongqing_gov_tiyu_45: '铜梁区藕塘湾体育场',
  chongqing_gov_tiyu_46: '铜梁区全民健身中心',
  chongqing_gov_tiyu_47: '铜梁区金龙体育馆',
  chongqing_gov_tiyu_48: '铜梁龙体育场',
  chongqing_gov_tiyu_49: '潼南区体育场',
  chongqing_gov_tiyu_50: '潼南区体育馆',
  chongqing_gov_tiyu_51: '荣昌区体育场',
  chongqing_gov_tiyu_52: '荣昌区体育中心游泳池',
  chongqing_gov_tiyu_53: '荣昌区全民健身活动中心',
  chongqing_gov_tiyu_54: '荣昌区体育馆',
  chongqing_gov_tiyu_55: '武隆区体育馆',
  chongqing_gov_tiyu_56: '庙坝镇全民健身中心',
  chongqing_gov_tiyu_57: '东安镇全民健身中心',
  chongqing_gov_tiyu_58: '城口县岗天乡全民健身中心',
  chongqing_gov_tiyu_59: '城口县体育馆',
  chongqing_gov_tiyu_61: '丰都县体育馆',
  chongqing_gov_tiyu_62: '丰都县体育场',
  chongqing_gov_tiyu_64: '垫江县体育馆',
  chongqing_gov_tiyu_65: '垫江县体育场',
  chongqing_gov_tiyu_66: '垫江县全民健身中心',
  chongqing_gov_tiyu_67: '忠县体育馆',
  chongqing_gov_tiyu_68: '云阳县全民健身活动中心',
  chongqing_gov_tiyu_69: '云阳县体育馆',
  chongqing_gov_tiyu_70: '云阳县体育场',
  chongqing_gov_tiyu_71: '云阳县游泳中心',
  chongqing_gov_tiyu_72: '巫山县章家湾训练中心',
  chongqing_gov_tiyu_73: '重庆市巫山县苟家体育场',
  chongqing_gov_tiyu_74: '巫山县体育馆',
  chongqing_gov_tiyu_75: '巫山县全民健身中心',
  chongqing_gov_tiyu_76: '石柱县体育场',
  chongqing_gov_tiyu_77: '石柱县体育馆',
  chongqing_gov_tiyu_78: '秀山体育场',
  chongqing_gov_tiyu_79: '秀山体育馆',
  chongqing_gov_tiyu_80: '彭水县体育场',
  chongqing_gov_tiyu_81: '彭水县体育馆',
  chongqing_gov_tiyu_82: '彭水县全民健身中心',
  chongqing_gov_tiyu_83: '开州区体育馆',
  chongqing_gov_tiyu_84: '开州区游泳馆',
  chongqing_gov_tiyu_85: '开州区体育场',
  chongqing_gov_tiyu_86: '梁平区东门体育馆',
  chongqing_gov_tiyu_87: '梁平区东门游泳馆',
  chongqing_gov_tiyu_88: '酉阳县体育馆',
  hangzhou_gov_杭州全民健身中心: '杭州全民健身中心',
  hangzhou_gov_杭州游泳健身馆: '杭州游泳健身馆',
  hangzhou_gov_杭州大关游泳健身馆: '杭州大关游泳健身馆',
  hangzhou_gov_杭州体育场: '杭州体育场',
  hangzhou_gov_杭州体育馆: '杭州体育馆',
  hangzhou_gov_杭州市陈经纶体育学校: '杭州市陈经纶体育学校',
  hangzhou_gov_杭州市职工文化中心: '杭州市职工文化中心',
  hangzhou_gov_杭州市体育事业发展中心杭州体育馆_改建中: '杭州市体育事业发展中心杭州体育馆（改建中）',
  hangzhou_gov_杭州市体育事业发展中心杭州体育场: '杭州市体育事业发展中心杭州体育场',
  hangzhou_gov_杭州市体育事业发展中心杭州游泳健身馆: '杭州市体育事业发展中心杭州游泳健身馆',
  hangzhou_gov_杭州市体育事业发展中心杭州大关游泳健身馆: '杭州市体育事业发展中心杭州大关游泳健身馆',
  hangzhou_gov_杭州市体育事业发展中心杭州全民健身中心_在建: '杭州市体育事业发展中心杭州全民健身中心（在建）',
  hangzhou_gov_上城区定安路体育中心: '上城区定安路体育中心',
  hangzhou_gov_下城区体育中心: '下城区体育中心',
  hangzhou_gov_江干区体育中心: '江干区体育中心',
  hangzhou_gov_九堡体育中心: '九堡体育中心',
  hangzhou_gov_丁兰文体中心: '丁兰文体中心',
  hangzhou_gov_西湖区文体中心: '西湖区文体中心',
  hangzhou_gov_拱墅区体育馆: '拱墅区体育馆',
  hangzhou_gov_拱墅区文体中心: '拱墅区文体中心',
  hangzhou_gov_江南体育中心: '江南体育中心',
  hangzhou_gov_滨江区体育馆: '滨江区体育馆',
  hangzhou_gov_萧山区体育中心: '萧山区体育中心',
  hangzhou_gov_萧山区临浦镇文体中心_改建中: '萧山区临浦镇文体中心（改建中）',
  hangzhou_gov_萧山区瓜沥镇文体中心: '萧山区瓜沥镇文体中心',
  hangzhou_gov_萧山区衙前镇文体中心: '萧山区衙前镇文体中心',
  hangzhou_gov_余杭区体育中心_改建中: '余杭区体育中心（改建中）',
  hangzhou_gov_余杭区闲林体艺馆: '余杭区闲林体艺馆',
  hangzhou_gov_富阳区体育中心: '富阳区体育中心',
  hangzhou_gov_临安文体会展中心_改建中: '临安文体会展中心(改建中)',
  hangzhou_gov_桐庐县体育馆: '桐庐县体育馆',
  hangzhou_gov_桐庐县城北体育健身中心: '桐庐县城北体育健身中心',
  hangzhou_gov_桐庐县分水镇文体中心: '桐庐县分水镇文体中心',
  hangzhou_gov_桐庐县横村镇文体中心: '桐庐县横村镇文体中心',
  hangzhou_gov_淳安县体育馆: '淳安县体育馆',
  hangzhou_gov_建德市新安江体育馆: '建德市新安江体育馆',
  hangzhou_gov_杭州市奥体中心: '杭州市奥体中心',
  hangzhou_gov_杭州市西湖区文化馆: '杭州市西湖区文化馆',
  hangzhou_gov_杭州市西湖区图书馆: '杭州市西湖区图书馆',
  hangzhou_gov_余杭区文化馆: '余杭区文化馆',
  hangzhou_gov_余杭区图书馆: '余杭区图书馆',
  hangzhou_gov_仓前街道图书分馆: '仓前街道图书分馆',
  hangzhou_gov_良渚街道图书分馆: '良渚街道图书分馆',
  hangzhou_gov_仁和街道图书分馆: '仁和街道图书分馆',
  hangzhou_gov_五常街道图书分馆: '五常街道图书分馆',
  hangzhou_gov_闲林街道图书分馆: '闲林街道图书分馆',
  hangzhou_gov_余杭街道图书分馆: '余杭街道图书分馆',
  hangzhou_gov_中泰街道图书分馆: '中泰街道图书分馆',
  hangzhou_gov_百丈镇图书分馆: '百丈镇图书分馆',
  hangzhou_gov_黄湖镇图书分馆: '黄湖镇图书分馆',
  hangzhou_gov_径山镇图书分馆: '径山镇图书分馆',
  hangzhou_gov_鸬鸟镇图书分馆: '鸬鸟镇图书分馆',
  hangzhou_gov_瓶窑镇图书分馆: '瓶窑镇图书分馆',
  hangzhou_gov_余杭章太炎故居纪念馆_章太炎研究中心: '余杭章太炎故居纪念馆（章太炎研究中心）',
  hangzhou_gov_余杭小百花越剧艺术中心_苕溪大剧院: '余杭小百花越剧艺术中心（苕溪大剧院）',
  hangzhou_gov_余杭区非遗馆: '余杭区非遗馆',
  hangzhou_gov_良渚街道综合文化站: '良渚街道综合文化站',
  hangzhou_gov_鸬鸟镇乡镇综合文化站: '鸬鸟镇乡镇综合文化站',
  hangzhou_gov_黄湖镇综合文化站: '黄湖镇综合文化站',
  hangzhou_gov_瓶窑镇综合文化站: '瓶窑镇综合文化站',
  hangzhou_gov_中泰街道综合文化站: '中泰街道综合文化站',
  hangzhou_gov_径山镇乡镇综合文化站: '径山镇乡镇综合文化站',
  hangzhou_gov_仁和街道综合文化站: '仁和街道综合文化站',
  hangzhou_gov_仓前街道综合文化站: '仓前街道综合文化站',
  hangzhou_gov_闲林街道综合文化站: '闲林街道综合文化站',
  hangzhou_gov_百丈镇综合文化站: '百丈镇综合文化站',
  hangzhou_gov_五常街道综合文化站: '五常街道综合文化站',
  hangzhou_gov_余杭街道综合文化站: '余杭街道综合文化站',
  hangzhou_gov_杭州市滨江区文化馆: '杭州市滨江区文化馆',
  hangzhou_gov_杭州市滨江区图书馆: '杭州市滨江区图书馆',
  hangzhou_gov_杭州市滨江区非物质文化遗产馆: '杭州市滨江区非物质文化遗产馆',
  hangzhou_gov_区文化馆: '区文化馆',
  hangzhou_gov_区图书馆: '区图书馆',
  hangzhou_gov_临平博物馆: '临平博物馆',
  hangzhou_gov_图书馆临平街道分馆_智慧分馆: '图书馆临平街道分馆（智慧分馆）',
  hangzhou_gov_图书馆运河街道分馆: '图书馆运河街道分馆',
  hangzhou_gov_图书馆南苑街道分馆: '图书馆南苑街道分馆',
  hangzhou_gov_图书馆星桥街道分馆: '图书馆星桥街道分馆',
  hangzhou_gov_图书馆乔司街道分馆: '图书馆乔司街道分馆',
  hangzhou_gov_图书馆崇贤街道分馆: '图书馆崇贤街道分馆',
  hangzhou_gov_图书馆东湖街道分馆_北沙书房: '图书馆东湖街道分馆（北沙书房）',
  hangzhou_gov_图书馆塘栖镇分馆: '图书馆塘栖镇分馆',
  nanjing_gov_njstptglsbwg: '太平天国历史博物馆',
  nanjing_gov_zgdbtmyxcjng: '中共代表团梅园新村纪念馆',
  nanjing_gov_njmsbwg: '南京市民俗博物馆',
  nanjing_gov_cqbwg: '城墙博物馆',
  nanjing_gov_njswhg: '南京市文化馆',
  nanjing_gov_xwqwhg: '玄武区文化馆',
  nanjing_gov_qxqwhg: '栖霞区文化馆',
  nanjing_gov_jnqwhg: '江宁区文化馆',
  nanjing_gov_pkqwhg: '浦口区文化馆',
  nanjing_gov_yhtqwhg: '雨花台区文化馆',
  nanjing_gov_qhqwhg: '秦淮区文化馆',
  nanjing_gov_jqwhg: '建邺区文化馆',
  nanjing_gov_glqwhg: '鼓楼区文化馆',
  nanjing_gov_lhqdewhg: '六合区文化馆',
  nanjing_gov_sqwhg: '溧水区文化馆',
  nanjing_gov_gcqwhg: '高淳区文化馆',
  nanjing_gov_jbxqwhg: '江北新区文化馆',
  nanjing_gov_bjhwhzx: '百家湖文化中心',
  nanjing_gov_yhtqtsg: '雨花台区图书馆',
  nanjing_gov_sqtsg: '溧水区图书馆',
  nanjing_gov_jqtsg: '建邺区图书馆',
  nanjing_gov_glqtsg: '鼓楼区图书馆',
  nanjing_gov_jnqtsg: '江宁区图书馆',
  nanjing_gov_pkqtsg: '浦口区图书馆',
  nanjing_gov_gcqtsg: '高淳区图书馆',
  nanjing_gov_qhqtsg: '秦淮区图书馆',
  nanjing_gov_qxqtsg: '栖霞区图书馆',
  nanjing_gov_lhqdetsg: '六合区第二图书馆',
  nanjing_gov_lhqtsg: '六合区图书馆',
  nanjing_gov_xwqsnettsg: '玄武区少年儿童图书馆',
  nanjing_gov_lsqsnettsg: '溧水区儿童图书馆',
  nanjing_gov_njjbtsg: '南京江北图书馆（新馆）',
  nanjing_gov_jssmsg: '江苏省美术馆',
  nanjing_gov_jlmsg: '金陵美术馆',
  shanghai_gov_museum_1: '黄炎培故居',
  shanghai_gov_museum_2: '张闻天故居',
  shanghai_gov_museum_3: '浦东历史博物馆',
  shanghai_gov_museum_5: '上海中国航海博物馆',
  shanghai_gov_museum_6: '高桥历史文化陈列馆',
  shanghai_gov_museum_7: '新场历史文化陈列馆',
  shanghai_gov_museum_8: '上海吴昌硕纪念馆',
  shanghai_gov_museum_9: '上海美特斯邦威服饰博物馆',
  shanghai_gov_museum_10: '上海动漫博物馆',
  shanghai_gov_museum_11: '上海震旦博物馆',
  shanghai_gov_museum_12: '上海（中医药大学）中医药博物馆',
  shanghai_gov_museum_13: '上海东方地质博物馆',
  shanghai_gov_museum_14: '上海观复博物馆',
  shanghai_gov_museum_15: '上海金刚博物馆',
  shanghai_gov_museum_16: '上海有恒博物馆',
  shanghai_gov_museum_17: '上海海派红木艺术博物馆',
  shanghai_gov_museum_18: '交通银行博物馆',
  shanghai_gov_museum_19: '上海老相机摄影博物馆',
  shanghai_gov_museum_20: '上海火炬众创孵化博物馆',
  shanghai_gov_museum_21: '上海天文馆（上海科技馆分馆）',
  shanghai_gov_museum_22: '上海宝库匠心博物馆',
  shanghai_gov_museum_24: '上海双拥工作展览馆',
  shanghai_gov_museum_27: '上海市历史博物馆（上海革命历史博物馆）',
  shanghai_gov_museum_29: '中共代表团驻沪办事处纪念馆（周公馆）',
  shanghai_gov_museum_30: '中国社会主义青年团中央机关旧址纪念馆',
  shanghai_gov_museum_31: '上海豫园管理处',
  shanghai_gov_museum_32: '上海三山会馆管理处',
  shanghai_gov_museum_33: '上海韬奋纪念馆',
  shanghai_gov_museum_34: '上海孙中山故居纪念馆',
  shanghai_gov_museum_35: '上海周虎臣曹素功笔墨博物馆',
  shanghai_gov_museum_36: '上海琉璃艺术博物馆',
  shanghai_gov_museum_37: '上海电信博物馆',
  shanghai_gov_museum_38: '上海民政博物馆',
  shanghai_gov_museum_39: '上海市外滩历史纪念馆',
  shanghai_gov_museum_41: '童涵春堂中药博物馆',
  shanghai_gov_museum_42: '上海市银行博物馆',
  shanghai_gov_museum_43: '大韩民国临时政府旧址管理处',
  shanghai_gov_museum_44: '国际乒联博物馆（中国乒乓球博物馆）',
  shanghai_gov_museum_46: '上海体育博物馆',
  shanghai_gov_museum_47: '中国劳动组合书记部旧址陈列馆',
  shanghai_gov_museum_48: '上海毛泽东旧居陈列馆',
  shanghai_gov_museum_49: '上海蔡元培故居陈列馆',
  shanghai_gov_museum_50: '中共上海地下组织斗争史陈列馆暨刘长胜故居',
  shanghai_gov_museum_51: '中共二大会址纪念馆',
  shanghai_gov_museum_52: '上海自然博物馆（上海科技馆分馆）',
  shanghai_gov_museum_53: '中共三大后中央局机关历史纪念馆',
  shanghai_gov_museum_54: '中共淞浦特委机关旧址陈列馆',
  shanghai_gov_museum_55: '元利当铺旧址博物馆',
  shanghai_gov_museum_57: '上海眼镜博物馆',
  shanghai_gov_museum_58: '上海四行仓库抗战纪念馆',
  shanghai_gov_museum_59: '上海棋牌文化博物馆',
  shanghai_gov_museum_60: '上海印刷字体展示馆',
  shanghai_gov_museum_61: '上海寰宇铃铛博物馆',
  shanghai_gov_museum_62: '中共中央秘书处机关旧址纪念馆',
  shanghai_gov_museum_63: '中共中央军委机关旧址纪念馆',
  shanghai_gov_museum_64: '中央特科机关旧址纪念馆',
  shanghai_gov_museum_65: '黄道婆纪念馆',
  shanghai_gov_museum_66: '徐光启纪念馆',
  shanghai_gov_museum_67: '上海土山湾博物馆',
  shanghai_gov_museum_68: '上海市龙华烈士纪念馆',
  shanghai_gov_museum_69: '上海宋庆龄故居纪念馆',
  shanghai_gov_museum_72: '中国科学院上海昆虫博物馆',
  shanghai_gov_museum_73: '上海师范大学博物馆',
  shanghai_gov_museum_74: '上海音乐学院东方乐器博物馆',
  shanghai_gov_museum_75: '上海交通大学校史博物馆',
  shanghai_gov_museum_76: '上海交通大学董浩云航运博物馆',
  shanghai_gov_museum_77: '钱学森图书馆',
  shanghai_gov_museum_79: '上海无线电博物馆',
  shanghai_gov_museum_80: '衡复风貌博物馆群',
  shanghai_gov_museum_81: '上海气象博物馆',
  shanghai_gov_museum_82: '上海品牌博物馆',
  shanghai_gov_museum_83: '《义勇军进行曲》灌制地纪念馆 （百代小楼）',
  shanghai_gov_museum_84: '上海市长宁区革命文物陈列馆',
  shanghai_gov_museum_86: '宋庆龄生平事迹陈列馆',
  shanghai_gov_museum_88: '上海（东华大学）纺织服饰博物馆',
  shanghai_gov_museum_89: '上海凝聚力工程博物馆',
  shanghai_gov_museum_90: '上海艺术品博物馆',
  shanghai_gov_museum_91: '上海广播博物馆',
  shanghai_gov_museum_92: '上海对外经贸大学博物馆',
  shanghai_gov_museum_93: '上海元代水闸遗址博物馆',
  shanghai_gov_museum_94: '顾正红纪念馆',
  shanghai_gov_museum_95: '苏州河工业文明展示馆',
  shanghai_gov_museum_96: '上海纺织博物馆',
  shanghai_gov_museum_97: '华东师范大学博物馆',
  shanghai_gov_museum_98: '沪西工人半日学校史料陈列馆',
  shanghai_gov_museum_99: '上海泰迪之家泰迪熊博物馆',
  shanghai_gov_museum_100: '上海鲁迅纪念馆',
  shanghai_gov_museum_101: '中共四大纪念馆',
  shanghai_gov_museum_102: '左联会址纪念馆',
  shanghai_gov_museum_103: '李白烈士故居',
  shanghai_gov_museum_104: '沈尹默故居',
  shanghai_gov_museum_105: '上海邮政博物馆',
  shanghai_gov_museum_106: '上海犹太难民纪念馆',
  shanghai_gov_museum_107: '中国证券博物馆',
  shanghai_gov_museum_108: '国歌展示馆',
  shanghai_gov_museum_109: '上海中国烟草博物馆',
  shanghai_gov_museum_110: '上海院士风采馆',
  shanghai_gov_museum_111: '复旦大学博物馆',
  shanghai_gov_museum_112: '上海理工大学印刷博物馆',
  shanghai_gov_museum_113: '上海海洋大学博物馆',
  shanghai_gov_museum_114: '上海体育大学武术博物馆',
  shanghai_gov_museum_115: '上海财经大学商学博物馆',
  shanghai_gov_museum_116: '同济大学博物馆',
  shanghai_gov_museum_117: '中国近现代新闻出版博物馆',
  shanghai_gov_museum_118: '上海世界技能博物馆',
  shanghai_gov_museum_119: '上海淞沪抗战纪念馆',
  shanghai_gov_museum_120: '上海陈化成纪念馆',
  shanghai_gov_museum_122: '上海市陶行知纪念馆',
  shanghai_gov_museum_123: '上海解放纪念馆',
  shanghai_gov_museum_124: '南京路上好八连事迹陈列馆',
  shanghai_gov_museum_125: '上海大学博物馆（海派文化博物馆）',
  shanghai_gov_museum_126: '上海中国工业设计博物馆',
  shanghai_gov_museum_127: '上海尊木汇木文化博物馆',
  shanghai_gov_museum_128: '上海智慧湾增材制造文化博物馆',
  shanghai_gov_museum_129: '上海百诺巧克力博物馆',
  shanghai_gov_museum_130: '上海杨明洁工业设计博物馆',
  shanghai_gov_museum_131: '闵行区博物馆',
  shanghai_gov_museum_132: '张充仁纪念馆',
  shanghai_gov_museum_133: '上海民族乐器博物馆',
  shanghai_gov_museum_135: '上海航宇科普中心',
  shanghai_gov_museum_136: '上海观止矿晶博物馆',
  shanghai_gov_museum_137: '上海翰林匾额博物馆',
  shanghai_gov_museum_138: '上海交通大学博物馆',
  shanghai_gov_museum_139: '上海乳业博物馆',
  shanghai_gov_museum_141: '嘉定竹刻博物馆',
  shanghai_gov_museum_142: '顾维钧生平陈列馆',
  shanghai_gov_museum_144: '四海壶具博物馆',
  shanghai_gov_museum_145: '上海翥云艺术博物馆',
  shanghai_gov_museum_146: '上海大来时间博物馆',
  shanghai_gov_museum_147: '上海海纳吴觉农茶文化博物馆',
  shanghai_gov_museum_148: '金山区博物馆',
  shanghai_gov_museum_149: '上海南社纪念馆',
  shanghai_gov_museum_150: '上海市沧海盐田盐文化博物馆',
  shanghai_gov_museum_151: '上海市松江区博物馆',
  shanghai_gov_museum_152: '上海中国留学生博物馆',
  shanghai_gov_museum_153: '上海天文博物馆',
  shanghai_gov_museum_154: '上海立信会计学院中国会计博物馆',
  shanghai_gov_museum_155: '上海国际酒文化博物馆',
  shanghai_gov_museum_156: '董其昌书画艺术博物馆',
  shanghai_gov_museum_157: '上海外国语大学语言博物馆',
  shanghai_gov_museum_158: '上海来伊份零食博物馆',
  shanghai_gov_museum_159: '青浦区博物馆',
  shanghai_gov_museum_160: '陈云纪念馆',
  shanghai_gov_museum_161: '上海福寿园人文纪念馆',
  shanghai_gov_museum_162: '上海市青浦区任屯血防陈列馆',
  shanghai_gov_museum_163: '上海崧泽遗址博物馆',
  shanghai_gov_museum_164: '上海中华印刷博物馆',
  shanghai_gov_museum_165: '上海红十字历史文化陈列馆',
  shanghai_gov_museum_166: '奉贤区博物馆',
  shanghai_gov_museum_167: '上海知青博物馆',
  shanghai_gov_museum_168: '上海农垦博物馆',
  shanghai_gov_museum_169: '上海真静传统木作博物馆',
  shanghai_gov_museum_170: '上海电线电缆博物馆',
  shanghai_gov_museum_171: '崇明区博物馆',
  shanghai_gov_museum_172: '上海崇明向化灶文化博物馆',
  shanghai_gov_museum_173: '上海崇明竖新抗日战争博物馆',
  shanghai_gov_museum_174: '江南造船展示馆',
  shanghai_gov_library_1: '上海图书馆（淮海馆）',
  shanghai_gov_library_2: '上海图书馆（东馆）',
  shanghai_gov_library_3: '上海少年儿童图书馆（长风馆）',
  shanghai_gov_library_4: '上海少年儿童图书馆（南西馆）',
  shanghai_gov_library_5: '上海浦东图书馆',
  shanghai_gov_library_6: '上海浦东图书馆南汇分馆',
  shanghai_gov_library_7: '上海浦东图书馆陆家嘴分馆（东方路）',
  shanghai_gov_library_8: '上海浦东图书馆陆家嘴分馆（浦城路）',
  shanghai_gov_library_9: '上海浦东图书馆少儿分馆',
  shanghai_gov_library_10: '南码头路街道图书馆',
  shanghai_gov_library_11: '三林镇图书馆',
  shanghai_gov_library_12: '三林镇图书馆懿德分馆',
  shanghai_gov_library_13: '三林镇图书馆世博分馆',
  shanghai_gov_library_14: '塘桥街道图书馆',
  shanghai_gov_library_15: '北蔡镇图书馆',
  shanghai_gov_library_16: '张江图书馆',
  shanghai_gov_library_17: '张江图书馆孙桥分馆',
  shanghai_gov_library_18: '潍坊街道图书馆',
  shanghai_gov_library_19: '金杨新村街道图书馆',
  shanghai_gov_library_20: '周家渡街道图书馆',
  shanghai_gov_library_21: '上钢图书馆',
  shanghai_gov_library_22: '上钢图书馆综合体分馆',
  shanghai_gov_library_23: '花木街道图书馆',
  shanghai_gov_library_24: '东明路街道图书馆',
  shanghai_gov_library_25: '高东镇图书馆',
  shanghai_gov_library_26: '高桥镇图书馆',
  shanghai_gov_library_27: '高行镇图书馆',
  shanghai_gov_library_28: '南汇新城镇图书馆（芦潮港馆）',
  shanghai_gov_library_29: '南汇新城镇图书馆（申港馆）',
  shanghai_gov_library_30: '宣桥镇图书馆',
  shanghai_gov_library_31: '新场镇图书馆',
  shanghai_gov_library_32: '万祥镇图书馆',
  shanghai_gov_library_33: '合庆镇图书馆',
  shanghai_gov_library_34: '惠南镇图书馆',
  shanghai_gov_library_35: '惠南镇图书馆东城分馆',
  shanghai_gov_library_36: '新川沙图书馆（成人馆）',
  shanghai_gov_library_37: '新川沙图书馆（少儿馆）',
  shanghai_gov_library_38: '曹路镇图书馆',
  shanghai_gov_library_39: '康桥镇图书馆',
  shanghai_gov_library_40: '祝桥镇图书馆',
  shanghai_gov_library_41: '老港镇图书馆',
  shanghai_gov_library_42: '浦兴路街道图书馆',
  shanghai_gov_library_43: '浦兴路街道图书馆金桥湾分馆',
  shanghai_gov_library_44: '周浦镇图书馆',
  shanghai_gov_library_45: '傅雷图书馆',
  shanghai_gov_library_46: '泥城镇图书馆',
  shanghai_gov_library_47: '唐镇图书馆',
  shanghai_gov_library_48: '唐镇图书馆（王港分中心）',
  shanghai_gov_library_49: '航头镇图书馆',
  shanghai_gov_library_50: '航头镇图书馆鹤沙分馆',
  shanghai_gov_library_51: '沪东社区图书馆',
  shanghai_gov_library_52: '陆家嘴街道图书馆',
  shanghai_gov_library_53: '书院镇图书馆',
  shanghai_gov_library_54: '洋泾社区图书馆',
  shanghai_gov_library_55: '金桥镇图书馆',
  shanghai_gov_library_56: '大团镇图书馆',
  shanghai_gov_library_57: '黄浦区图书馆',
  shanghai_gov_library_58: '黄浦区明复图书馆(原卢湾区图书馆)',
  shanghai_gov_library_59: '半淞园路街道图书馆',
  shanghai_gov_library_60: '打浦桥街道图书馆',
  shanghai_gov_library_61: '淮海中路街道图书馆',
  shanghai_gov_library_62: '南京东路街道图书馆',
  shanghai_gov_library_63: '瑞金二路街道图书馆',
  shanghai_gov_library_64: '外滩街道图书馆',
  shanghai_gov_library_65: '五里桥街道图书馆',
  shanghai_gov_library_66: '小东门街道图书馆',
  shanghai_gov_library_67: '豫园街道图书馆',
  shanghai_gov_library_68: '老西门街道图书馆',
  shanghai_gov_library_69: '静安区图书馆（新闸路）',
  shanghai_gov_library_70: '静安区图书馆（天目中路）',
  shanghai_gov_library_71: '静安区图书馆（闻喜路）',
  shanghai_gov_library_72: '静安区少年儿童图书馆',
  shanghai_gov_library_73: '静安区闸北少年儿童图书馆',
  shanghai_gov_library_74: '曹家渡街道图书馆',
  shanghai_gov_library_75: '曹家渡街道达安星之会所图书室',
  shanghai_gov_library_76: '曹家渡街道图书馆（少儿）',
  shanghai_gov_library_77: '静安区图书馆北站街道分馆',
  shanghai_gov_library_78: '江宁路街道图书馆',
  shanghai_gov_library_79: '静安寺街道图书馆',
  shanghai_gov_library_80: '南京西路街道图书馆',
  shanghai_gov_library_81: '南京西路街道少儿图书馆',
  shanghai_gov_library_82: '石门二路街道图书馆',
  shanghai_gov_library_83: '宝山路街道图书馆',
  shanghai_gov_library_84: '北站街道图书馆（艺术图书馆）',
  shanghai_gov_library_85: '大宁路街道图书馆',
  shanghai_gov_library_86: '宁的书房',
  shanghai_gov_library_87: '大宁路街道分馆（社区文化中心）',
  shanghai_gov_library_88: '共和新路街道图书馆',
  shanghai_gov_library_89: '临汾路街道图书馆',
  shanghai_gov_library_90: '彭浦新村街道图书馆',
  shanghai_gov_library_91: '彭浦镇图书馆',
  shanghai_gov_library_92: '天目西路街道图书馆',
  shanghai_gov_library_93: '芷江西路街道图书馆',
  shanghai_gov_library_94: '徐汇区图书馆（徐家汇书院）',
  shanghai_gov_library_95: '徐家汇街道图书馆',
  shanghai_gov_library_96: '天平路街道图书馆',
  shanghai_gov_library_97: '湖南路街道图书馆',
  shanghai_gov_library_98: '枫林路街道图书馆',
  shanghai_gov_library_99: '斜土路街道图书馆',
  shanghai_gov_library_100: '田林街道图书馆',
  shanghai_gov_library_101: '长桥街道图书馆',
  shanghai_gov_library_102: '虹梅路街道图书馆',
  shanghai_gov_library_103: '康健新村街道图书馆',
  shanghai_gov_library_104: '龙华街道图书馆',
  shanghai_gov_library_105: '凌云路街道图书馆',
  shanghai_gov_library_106: '漕河泾街道图书馆',
  shanghai_gov_library_107: '漕河泾街道图书馆 石龙分馆',
  shanghai_gov_library_108: '华泾镇图书馆',
  shanghai_gov_library_109: '长宁区图书馆（天山馆）',
  shanghai_gov_library_110: '长宁区图书馆（愚园馆）',
  shanghai_gov_library_111: '长宁区图书馆（仙霞馆）',
  shanghai_gov_library_112: '北新泾街道图书馆',
  shanghai_gov_library_113: '程家桥街道图书馆',
  shanghai_gov_library_114: '虹桥街道图书馆',
  shanghai_gov_library_115: '虹桥街道图书馆分馆（古北天空书苑）',
  shanghai_gov_library_116: '华阳路街道图书馆',
  shanghai_gov_library_117: '江苏路街道图书馆',
  shanghai_gov_library_118: '天山路街道图书馆',
  shanghai_gov_library_119: '仙霞新村街道图书馆',
  shanghai_gov_library_120: '新华路街道图书馆',
  shanghai_gov_library_121: '新泾镇图书馆',
  shanghai_gov_library_122: '周家桥街道图书馆',
  shanghai_gov_library_124: '曹杨新村街道图书馆',
  shanghai_gov_library_125: '长风新村街道图书馆',
  shanghai_gov_library_126: '长寿路街道图书馆',
  shanghai_gov_library_127: '万里街道图书馆',
  shanghai_gov_library_128: '长征镇图书馆',
  shanghai_gov_library_129: '甘泉街道图书馆',
  shanghai_gov_library_130: '石泉路街道图书馆',
  shanghai_gov_library_131: '桃浦镇图书馆',
  shanghai_gov_library_132: '宜川路街道图书馆',
  shanghai_gov_library_133: '真如镇街道图书馆',
  shanghai_gov_library_134: '虹口区图书馆',
  shanghai_gov_library_135: '虹口区图书馆曲阳分馆',
  shanghai_gov_library_136: '虹口区图书馆和平分馆',
  shanghai_gov_library_137: '广中路街道图书馆',
  shanghai_gov_library_138: '嘉兴路街道图书馆',
  shanghai_gov_library_139: '江湾镇街道图书馆',
  shanghai_gov_library_140: '江湾镇街道图书馆分馆（逸仙会客厅）',
  shanghai_gov_library_141: '凉城新村街道图书馆',
  shanghai_gov_library_142: '欧阳路街道图书馆',
  shanghai_gov_library_143: '曲阳路街道图书馆',
  shanghai_gov_library_144: '北外滩街道图书馆',
  shanghai_gov_library_145: '四川北路街道图书馆',
  shanghai_gov_library_147: '杨浦区图书馆（平凉分馆）',
  shanghai_gov_library_148: '杨浦区图书馆（少儿分馆）',
  shanghai_gov_library_149: '长白新村街道图书馆',
  shanghai_gov_library_150: '大桥街道图书馆',
  shanghai_gov_library_151: '定海路街道图书馆',
  shanghai_gov_library_152: '江浦路街道图书馆',
  shanghai_gov_library_153: '江浦路街道图书馆少儿分馆',
  shanghai_gov_library_154: '控江路街道图书馆',
  shanghai_gov_library_155: '平凉路街道图书馆',
  shanghai_gov_library_156: '四平路街道图书馆',
  shanghai_gov_library_157: '五角场街道图书馆',
  shanghai_gov_library_158: '五角场街道图书馆（国定支路分馆）',
  shanghai_gov_library_159: '长海路街道图书馆（政府路馆）',
  shanghai_gov_library_160: '长海路街道图书馆（翔殷路馆）',
  shanghai_gov_library_161: '长海路街道图书馆（市光路馆）',
  shanghai_gov_library_162: '延吉新村街道图书馆',
  shanghai_gov_library_163: '殷行街道图书馆',
  shanghai_gov_library_164: '新江湾城街道图书馆',
  shanghai_gov_library_166: '大场镇图书馆',
  shanghai_gov_library_167: '高境镇图书馆',
  shanghai_gov_library_168: '顾村镇图书馆',
  shanghai_gov_library_169: '顾村镇图书馆（诗乡广场分馆）',
  shanghai_gov_library_170: '顾村镇图书馆（馨佳园分馆）',
  shanghai_gov_library_171: '顾村镇图书馆（菊泉分馆）',
  shanghai_gov_library_172: '罗店镇图书馆',
  shanghai_gov_library_173: '罗店镇图书馆（塘西街分馆）',
  shanghai_gov_library_174: '罗店镇图书馆（美兰西湖分馆）',
  shanghai_gov_library_175: '罗泾镇图书馆',
  shanghai_gov_library_176: '罗泾镇图书馆分馆',
  shanghai_gov_library_177: '庙行镇图书馆',
  shanghai_gov_library_178: '淞南镇图书馆',
  shanghai_gov_library_179: '吴淞街道图书馆',
  shanghai_gov_library_180: '杨行镇图书馆',
  shanghai_gov_library_181: '友谊路街道图书馆',
  shanghai_gov_library_182: '月浦镇图书馆（盛桥馆）',
  shanghai_gov_library_183: '月浦镇图书馆（庆安路馆）',
  shanghai_gov_library_184: '月浦镇图书馆（龙镇路馆）',
  shanghai_gov_library_185: '月浦镇图书馆（马泾桥馆）',
  shanghai_gov_library_186: '张庙街道图书馆',
  shanghai_gov_library_188: '古美路街道图书馆（东馆）',
  shanghai_gov_library_189: '古美路街道图书馆（西馆）',
  shanghai_gov_library_190: '虹桥镇图书馆',
  shanghai_gov_library_191: '华漕镇图书馆',
  shanghai_gov_library_192: '大零号湾图书馆',
  shanghai_gov_library_193: '马桥镇图书馆',
  shanghai_gov_library_194: '梅陇镇图书馆',
  shanghai_gov_library_195: '梅陇镇图书馆晶城分馆',
  shanghai_gov_library_196: '浦江图书馆',
  shanghai_gov_library_197: '浦江镇图书馆永康分馆',
  shanghai_gov_library_198: '七宝镇图书馆',
  shanghai_gov_library_199: '吴泾镇图书馆',
  shanghai_gov_library_200: '新虹街道图书馆',
  shanghai_gov_library_201: '莘庄工业区图书馆',
  shanghai_gov_library_202: '莘庄镇图书馆',
  shanghai_gov_library_203: '颛桥镇图书馆',
  shanghai_gov_library_204: '浦锦街道图书馆',
  shanghai_gov_library_205: '嘉定区图书馆',
  shanghai_gov_library_206: '嘉定区图书馆清河路分馆',
  shanghai_gov_library_207: '安亭镇图书馆',
  shanghai_gov_library_208: '安亭镇图书馆（黄渡分馆）',
  shanghai_gov_library_209: '安亭镇图书馆（方泰分馆）',
  shanghai_gov_library_210: '华亭镇图书馆',
  shanghai_gov_library_211: '嘉定工业区图书馆',
  shanghai_gov_library_212: '嘉定镇街道图书馆',
  shanghai_gov_library_213: '江桥镇图书馆',
  shanghai_gov_library_214: '江桥镇龙湖图书馆',
  shanghai_gov_library_215: '菊园新区图书馆',
  shanghai_gov_library_216: '马陆镇图书馆',
  shanghai_gov_library_217: '南翔镇图书馆',
  shanghai_gov_library_218: '南翔镇图书馆东社区分馆',
  shanghai_gov_library_219: '外冈镇图书馆',
  shanghai_gov_library_220: '新成路街道图书馆',
  shanghai_gov_library_221: '徐行镇图书馆',
  shanghai_gov_library_222: '真新街道图书馆',
  shanghai_gov_library_223: '真新街道图书馆（新丰分馆）',
  shanghai_gov_library_224: '金山区图书馆',
  shanghai_gov_library_225: '漕泾镇图书馆',
  shanghai_gov_library_226: '枫泾镇图书馆',
  shanghai_gov_library_227: '高新区图书馆',
  shanghai_gov_library_228: '金山卫镇图书馆',
  shanghai_gov_library_229: '金山卫镇图书馆钱圩分馆',
  shanghai_gov_library_230: '廊下镇图书馆',
  shanghai_gov_library_231: '吕巷镇图书馆',
  shanghai_gov_library_232: '吕巷镇图书馆干巷分馆',
  shanghai_gov_library_233: '山阳镇图书馆',
  shanghai_gov_library_234: '山阳镇海璟图书馆',
  shanghai_gov_library_235: '石化街道图书馆',
  shanghai_gov_library_236: '亭林镇图书馆',
  shanghai_gov_library_237: '张堰镇图书馆',
  shanghai_gov_library_238: '朱泾镇图书馆',
  shanghai_gov_library_239: '朱泾镇图书馆新农分馆',
  shanghai_gov_library_240: '人文松江活动中心（松江区图书馆）',
  shanghai_gov_library_241: '车墩镇图书馆',
  shanghai_gov_library_242: '洞泾镇图书馆',
  shanghai_gov_library_243: '方松街道图书馆',
  shanghai_gov_library_244: '九亭镇图书馆',
  shanghai_gov_library_245: '泖港镇图书馆',
  shanghai_gov_library_246: '佘山镇图书馆',
  shanghai_gov_library_247: '佘山镇佘北图书馆',
  shanghai_gov_library_248: '石湖荡镇图书馆',
  shanghai_gov_library_249: '泗泾镇图书馆',
  shanghai_gov_library_250: '泗泾新凯图书馆',
  shanghai_gov_library_251: '泗泾新凯大居图书馆',
  shanghai_gov_library_252: '小昆山镇图书馆',
  shanghai_gov_library_253: '新浜镇图书馆',
  shanghai_gov_library_254: '新桥镇图书馆',
  shanghai_gov_library_255: '叶榭镇图书馆',
  shanghai_gov_library_256: '永丰街道图书馆',
  shanghai_gov_library_257: '岳阳街道图书馆',
  shanghai_gov_library_258: '中山街道图书馆',
  shanghai_gov_library_259: '九里亭街道图书馆',
  shanghai_gov_library_260: '广富林街道图书馆',
  shanghai_gov_library_261: '青浦区图书馆',
  shanghai_gov_library_262: '白鹤镇图书馆',
  shanghai_gov_library_263: '白鹤镇图书馆（赵屯分中心）',
  shanghai_gov_library_264: '华新镇图书馆',
  shanghai_gov_library_265: '华新镇图书馆（凤溪分馆）',
  shanghai_gov_library_266: '金泽镇图书馆',
  shanghai_gov_library_267: '练塘镇图书馆',
  shanghai_gov_library_268: '夏阳街道图书馆',
  shanghai_gov_library_269: '徐泾镇图书馆',
  shanghai_gov_library_270: '徐泾镇图书馆（北大居分馆）',
  shanghai_gov_library_271: '赵巷镇图书馆',
  shanghai_gov_library_272: '赵巷镇图书馆（新城一站分馆）',
  shanghai_gov_library_273: '青溪书房·赵巷公园',
  shanghai_gov_library_274: '重固镇图书馆',
  shanghai_gov_library_275: '朱家角镇图书馆',
  shanghai_gov_library_276: '香花桥街道图书馆',
  shanghai_gov_library_277: '香花桥街道图书馆 （玉兰花园分馆）',
  shanghai_gov_library_278: '盈浦街道图书馆',
  shanghai_gov_library_279: '奉贤区图书馆',
  shanghai_gov_library_280: '奉城镇图书馆',
  shanghai_gov_library_281: '海湾镇图书馆',
  shanghai_gov_library_282: '金汇镇图书馆',
  shanghai_gov_library_283: '南桥镇图书馆',
  shanghai_gov_library_284: '青村镇图书馆',
  shanghai_gov_library_285: '四团镇图书馆',
  shanghai_gov_library_286: '柘林镇图书馆',
  shanghai_gov_library_287: '庄行镇图书馆',
  shanghai_gov_library_288: '奉浦街道图书馆',
  shanghai_gov_library_289: '西渡街道图书馆',
  shanghai_gov_library_290: '金海街道图书馆',
  shanghai_gov_library_291: '海湾旅游区图书馆',
  shanghai_gov_library_292: '头桥街道图书馆',
  shanghai_gov_library_293: '崇明区图书馆',
  shanghai_gov_library_294: '堡镇图书馆',
  shanghai_gov_library_295: '长兴镇图书馆',
  shanghai_gov_library_296: '陈家镇图书馆',
  shanghai_gov_library_297: '城桥镇图书馆',
  shanghai_gov_library_298: '东平镇图书馆',
  shanghai_gov_library_299: '港西镇图书馆',
  shanghai_gov_library_300: '港沿镇图书馆',
  shanghai_gov_library_301: '横沙乡图书馆',
  shanghai_gov_library_302: '建设镇图书馆',
  shanghai_gov_library_303: '绿华镇图书馆',
  shanghai_gov_library_304: '庙镇图书馆',
  shanghai_gov_library_305: '三星镇图书馆',
  shanghai_gov_library_306: '竖新镇图书馆',
  shanghai_gov_library_307: '向化镇图书馆',
  shanghai_gov_library_308: '新村乡图书馆',
  shanghai_gov_library_309: '新海镇图书馆',
  shanghai_gov_library_310: '新河镇图书馆',
  shanghai_gov_library_311: '中兴镇图书馆',
  shanghai_gov_art_3: '上海浦东碧云美术馆',
  shanghai_gov_art_5: '海派连环画艺术馆',
  shanghai_gov_art_6: '上海王狮美术馆',
  shanghai_gov_art_7: '浦东云间美术馆',
  shanghai_gov_art_8: '周浦美术馆',
  shanghai_gov_art_9: '上海浦东林隐美术馆',
  shanghai_gov_art_10: '上海浦东新区库伯美术馆',
  shanghai_gov_art_11: '上海艺仓美术馆',
  shanghai_gov_art_12: '上海昊美术馆',
  shanghai_gov_art_13: '上海浦东新区联明美术馆',
  shanghai_gov_art_14: '上海浦东新区叁柒贰叁美术馆',
  shanghai_gov_art_15: '上海浦东新区越婷惠美术馆',
  shanghai_gov_art_16: '震旦美术馆',
  shanghai_gov_art_18: '上海久事美术馆',
  shanghai_gov_art_19: '春美术馆',
  shanghai_gov_art_20: '胡问遂艺术馆',
  shanghai_gov_art_21: '上海驰翰美术馆',
  shanghai_gov_art_22: '上海民生现代美术馆',
  shanghai_gov_art_23: 'chi K11美术馆',
  shanghai_gov_art_24: '上海外滩美术馆',
  shanghai_gov_art_25: '上海复星艺术中心',
  shanghai_gov_art_26: '华山艺术馆',
  shanghai_gov_art_27: '明当代美术馆',
  shanghai_gov_art_28: '心象艺术馆',
  shanghai_gov_art_29: '上海静安毕加索艺术馆',
  shanghai_gov_art_30: '上海静安大风堂美术馆',
  shanghai_gov_art_31: '上海大学美术馆',
  shanghai_gov_art_32: 'Fotografiska 影像艺术中心',
  shanghai_gov_art_33: '上海中国画院美术馆',
  shanghai_gov_art_34: '上海市徐汇区艺术馆',
  shanghai_gov_art_35: '西岸美术馆',
  shanghai_gov_art_36: '龙美术馆（西岸馆）',
  shanghai_gov_art_37: '上海油罐艺术中心',
  shanghai_gov_art_38: 'START星美术馆',
  shanghai_gov_art_39: '上海明圆美术馆',
  shanghai_gov_art_40: '上海徐汇区九点水美术馆',
  shanghai_gov_art_41: '刘海粟美术馆',
  shanghai_gov_art_42: '上海油画雕塑院美术馆',
  shanghai_gov_art_43: '上海中国画院 程十发美术馆',
  shanghai_gov_art_44: '上海虹桥当代美术馆',
  shanghai_gov_art_45: '上海正好美术馆',
  shanghai_gov_art_46: '上海杨培明宣传画收藏艺术馆',
  shanghai_gov_art_47: '上海长宁华萃当代美术馆',
  shanghai_gov_art_48: '上海长宁王小慧艺术馆',
  shanghai_gov_art_49: '刘海粟美术馆(分馆)',
  shanghai_gov_art_50: '上海苏宁艺术馆',
  shanghai_gov_art_51: '朱屺瞻艺术馆',
  shanghai_gov_art_52: '上海多伦现代美术馆',
  shanghai_gov_art_53: '上海虹口青藤美术馆',
  shanghai_gov_art_54: '趣看美术馆',
  shanghai_gov_art_55: '敦煌当代美术馆',
  shanghai_gov_art_56: '鸿一美术馆',
  shanghai_gov_art_57: '刘小晴艺术馆',
  shanghai_gov_art_58: '上海美术学院美术馆',
  shanghai_gov_art_59: '上海湫光美术馆',
  shanghai_gov_art_60: '上海宝山区龙现代美术馆',
  shanghai_gov_art_61: '上海交通大学 程及美术馆',
  shanghai_gov_art_62: '上海海派艺术馆',
  shanghai_gov_art_63: '蔡兵美术馆',
  shanghai_gov_art_64: '上海宝龙美术馆',
  shanghai_gov_art_65: '上海明珠美术馆',
  shanghai_gov_art_66: '上海闵行区美博美术馆',
  shanghai_gov_art_67: '上海半岛美术馆',
  shanghai_gov_art_68: '中闵虹桥美术馆',
  shanghai_gov_art_69: '上海金臣亦飞鸣美术馆',
  shanghai_gov_art_70: '陆俨少艺术院',
  shanghai_gov_art_71: '上海韩天衡美术馆',
  shanghai_gov_art_72: '上海秦古美术馆',
  shanghai_gov_art_73: '泰美术馆',
  shanghai_gov_art_74: '上海嘉定区北虹桥美术馆',
  shanghai_gov_art_75: '嘉源海美术馆',
  shanghai_gov_art_76: '上海嘉定十方画院',
  shanghai_gov_art_77: '丁聪美术馆',
  shanghai_gov_art_78: '上海金山区海鸥美术馆',
  shanghai_gov_art_79: '云间会堂美术馆',
  shanghai_gov_art_80: '程十发艺术馆',
  shanghai_gov_art_81: '松江美术馆',
  shanghai_gov_art_82: '上海松江云间美术馆',
  shanghai_gov_art_83: '上海艺术百代美术馆',
  shanghai_gov_art_84: '上海YOUNG美术馆',
  shanghai_gov_art_85: '上海松江清控人居美术馆',
  shanghai_gov_art_86: '上海松江区新桥美术馆',
  shanghai_gov_art_87: '上海松江区贤禾美术馆',
  shanghai_gov_art_88: '上海松江云间少儿美术馆',
  shanghai_gov_art_89: '上海国稷美术馆',
  shanghai_gov_art_90: '洙桥美术馆',
  shanghai_gov_art_91: '余德耀美术馆',
  shanghai_gov_art_92: '上海市鹤龙美术馆',
  shanghai_gov_art_93: '上海青浦青渚美术馆',
  shanghai_gov_art_94: '上海青浦区金夜美术馆',
  shanghai_gov_art_95: '上海青浦区练塘可的美术馆',
  shanghai_gov_art_96: '上海吴宜恩美术馆',
  shanghai_gov_art_97: '崇明美术馆',
  shanghai_gov_culture_2: '浦东新区文化艺术指导中心',
  shanghai_gov_culture_3: '浦东新区文化艺术指导中心惠南分中心',
  shanghai_gov_culture_4: '浦东新区文化艺术指导中心外高桥分中心',
  shanghai_gov_culture_5: '浦东新区金海文化艺术中心',
  shanghai_gov_culture_6: '浦东新区浦东文化馆',
  shanghai_gov_culture_7: '浦东新区浦南文化馆',
  shanghai_gov_culture_8: '黄浦区文化馆',
  shanghai_gov_culture_9: '徐汇区文化馆',
  shanghai_gov_culture_10: '长宁文化艺术中心',
  shanghai_gov_culture_12: '静安区文化馆',
  shanghai_gov_culture_13: '静安区文化馆分馆',
  shanghai_gov_culture_14: '虹口区文化馆',
  shanghai_gov_culture_15: '杨浦文化艺术中心',
  shanghai_gov_culture_16: '普陀区文化馆',
  shanghai_gov_culture_18: '上海市闵行区文化和旅游管理事务中心 （上海市闵行区群众艺术馆）',
  shanghai_gov_culture_20: '金山区文化馆',
  shanghai_gov_culture_21: '人文松江活动中心（松江区文化馆）',
  shanghai_gov_culture_22: '青浦区文化馆',
  shanghai_gov_culture_23: '奉贤区文化馆',
  shanghai_gov_culture_24: '崇明区文化馆',
  shanghai_gov_community_1: '周浦镇文化服务中心',
  shanghai_gov_community_2: '三林镇文化服务中心',
  shanghai_gov_community_3: '三林镇懿德文化分中心',
  shanghai_gov_community_4: '三林镇前滩社区文化分中心',
  shanghai_gov_community_5: '泥城镇文化服务中心',
  shanghai_gov_community_6: '金杨社区文化活动中心',
  shanghai_gov_community_7: '金杨社区文化活动中心云山路分中心',
  shanghai_gov_community_8: '唐镇文化体育中心',
  shanghai_gov_community_9: '大团镇文化服务中心',
  shanghai_gov_community_10: '金桥镇文化服务中心',
  shanghai_gov_community_11: '书院镇文化服务中心',
  shanghai_gov_community_12: '曹路镇文化服务中心',
  shanghai_gov_community_13: '曹路社区文化活动中心',
  shanghai_gov_community_14: '曹路社区文化活动中心顾路分中心',
  shanghai_gov_community_15: '花木街道社区文化活动中心',
  shanghai_gov_community_16: '川沙新镇文化服务中心',
  shanghai_gov_community_17: '祝桥镇文化服务中心',
  shanghai_gov_community_18: '惠南镇文化服务中心',
  shanghai_gov_community_20: '新场镇文化服务中心',
  shanghai_gov_community_21: '浦兴社区文化活动中心',
  shanghai_gov_community_22: '浦兴社区文化活动中心金桥湾分中心',
  shanghai_gov_community_23: '高东镇文化服务中心',
  shanghai_gov_community_24: '塘桥社区文化活动中心',
  shanghai_gov_community_25: '老港镇文化服务中心',
  shanghai_gov_community_26: '康桥镇文化服务中心',
  shanghai_gov_community_27: '航头镇文化服务中心',
  shanghai_gov_community_28: '航头镇文化服务中心鹤沙分中心',
  shanghai_gov_community_29: '南汇新城镇社区党群服务中心（文化服务中心）',
  shanghai_gov_community_30: '陆家嘴金融城文化中心',
  shanghai_gov_community_31: '陆家嘴金融城文化分中心',
  shanghai_gov_community_32: '高行镇文化服务中心',
  shanghai_gov_community_33: '万祥镇文化服务中心',
  shanghai_gov_community_34: '宣桥镇社区文化活动中心',
  shanghai_gov_community_35: '周家渡街道文化中心',
  shanghai_gov_community_36: '潍坊社区文化活动中心',
  shanghai_gov_community_37: '上钢社区文化活动中心',
  shanghai_gov_community_38: '南码头社区文化活动中心',
  shanghai_gov_community_39: '洋泾社区文化活动中心',
  shanghai_gov_community_40: '北蔡镇文化服务中心',
  shanghai_gov_community_41: '合庆镇文化服务中心',
  shanghai_gov_community_42: '张江镇文化服务中心',
  shanghai_gov_community_43: '张江镇文化服务中心-孙桥分中心',
  shanghai_gov_community_44: '沪东社区文化活动中心',
  shanghai_gov_community_45: '沪东社区文化分中心',
  shanghai_gov_community_46: '高桥镇文化服务中心',
  shanghai_gov_community_47: '东明社区文化活动中心',
  shanghai_gov_community_48: '东明社区文化活动分中心',
  shanghai_gov_community_49: '五里桥社区文化活动中心',
  shanghai_gov_community_50: '南京东路社区文化活动中心',
  shanghai_gov_community_51: '打浦桥社区文化活动中心',
  shanghai_gov_community_52: '瑞金二路社区文化活动中心',
  shanghai_gov_community_53: '淮海中路社区文化活动中心',
  shanghai_gov_community_54: '外滩社区文化活动中心',
  shanghai_gov_community_55: '小东门街道社区文化活动中心',
  shanghai_gov_community_56: '半淞园路社区文化活动中心',
  shanghai_gov_community_57: '豫园社区文化活动中心',
  shanghai_gov_community_58: '老西门社区文化活动中心',
  shanghai_gov_community_59: '石门二路社区文化活动中心',
  shanghai_gov_community_60: '北站街道社区文化活动中心',
  shanghai_gov_community_61: '临汾社区文化活动中心',
  shanghai_gov_community_62: '江宁路街道社区文化活动中心',
  shanghai_gov_community_63: '江宁路街道社区文化活动中心分中心',
  shanghai_gov_community_64: '南京西路街道社区文化活动中心（福民会馆）',
  shanghai_gov_community_65: '曹家渡街道社区文化活动中心',
  shanghai_gov_community_66: '静安寺街道社区文化活动中心',
  shanghai_gov_community_67: '大宁路街道社区文化活动中心',
  shanghai_gov_community_68: '彭浦镇社区文化活动中心',
  shanghai_gov_community_69: '宝山路街道党群服务中心',
  shanghai_gov_community_70: '共和新路街道社区党群服务中心',
  shanghai_gov_community_71: '彭浦新村街道社区文化活动中心',
  shanghai_gov_community_72: '芷江西路街道社区文化活动中心',
  shanghai_gov_community_73: '天目西路街道社区文化活动中心',
  shanghai_gov_community_74: '徐家汇社区文化活动中心',
  shanghai_gov_community_75: '天平街道社区文化活动中心',
  shanghai_gov_community_76: '天平街道66梧桐院(文化活动分中心)',
  shanghai_gov_community_77: '湖南街道社区文化活动中心',
  shanghai_gov_community_78: '枫林街道社区党群服务中心(文化活动分中心)',
  shanghai_gov_community_79: '枫林街道天龙党群服务中心(文化活动分中心)',
  shanghai_gov_community_80: '斜土社区文化活动中心',
  shanghai_gov_community_81: '田林街道党群服务中心',
  shanghai_gov_community_82: '长桥社区文化活动中心',
  shanghai_gov_community_83: '虹梅街道党群服务中心',
  shanghai_gov_community_84: '康健街道社区党群服务中心',
  shanghai_gov_community_85: '龙华社区党群中心',
  shanghai_gov_community_86: '凌云街道社区文化活动中心',
  shanghai_gov_community_87: '漕河泾街道社区文化活动中心',
  shanghai_gov_community_88: '华泾社区文化活动中心',
  shanghai_gov_community_89: '华阳社区文化活动中心',
  shanghai_gov_community_90: '新泾镇社区文化事务中心',
  shanghai_gov_community_91: '北新泾社区文化活动中心',
  shanghai_gov_community_92: '天山社区文化活动中心',
  shanghai_gov_community_93: '新华社区文化活动中心',
  shanghai_gov_community_94: '仙霞社区文化活动中心（西部）',
  shanghai_gov_community_95: '仙霞社区文化活动中心（东部）',
  shanghai_gov_community_96: '程家桥街道社区文化活动中心',
  shanghai_gov_community_97: '虹桥街道社区文化活动中心',
  shanghai_gov_community_98: '虹桥街道社区文化活动中心（分中心）',
  shanghai_gov_community_99: '周家桥社区文化活动中心',
  shanghai_gov_community_100: '江苏路街道社区文化活动中心',
  shanghai_gov_community_101: '长征社区文化活动中心',
  shanghai_gov_community_102: '曹杨社区文化活动中心',
  shanghai_gov_community_103: '甘泉社区文化活动中心',
  shanghai_gov_community_104: '长风社区文化活动中心',
  shanghai_gov_community_105: '桃浦社区文化活动中心',
  shanghai_gov_community_106: '真如社区文化活动中心',
  shanghai_gov_community_107: '长寿社区文化活动中心',
  shanghai_gov_community_108: '石泉社区文化活动中心',
  shanghai_gov_community_109: '宜川社区文化活动中心',
  shanghai_gov_community_110: '万里社区文化活动中心',
  shanghai_gov_community_111: '嘉兴路街道社区文化活动中心',
  shanghai_gov_community_112: '嘉兴路街道社区文化活动分中心',
  shanghai_gov_community_113: '曲阳路街道社区文化活动中心',
  shanghai_gov_community_114: '江湾镇街道社区文化活动中心',
  shanghai_gov_community_115: '欧阳路街道社区文化活动中心',
  shanghai_gov_community_116: '四川北路街道社区文化活动中心',
  shanghai_gov_community_117: '凉城新村街道社区文化活动中心',
  shanghai_gov_community_118: '北外滩街道社区文化活动中心',
  shanghai_gov_community_119: '广中路街道社区文化活动中心',
  shanghai_gov_community_120: '五角场社区文化活动中心',
  shanghai_gov_community_121: '五角场社区文化活动分中心',
  shanghai_gov_community_122: '大桥街道社区文化活动中心',
  shanghai_gov_community_123: '四平路街道社区文化活动中心',
  shanghai_gov_community_125: '定海路街道社区文化活动中心',
  shanghai_gov_community_126: '定海路街道社区文化活动分中心',
  shanghai_gov_community_127: '平凉社区文化活动中心',
  shanghai_gov_community_128: '长白新村街道社区文化活动中心',
  shanghai_gov_community_129: '228街坊文化活动中心',
  shanghai_gov_community_130: '长海路街道社区文化活动中心',
  shanghai_gov_community_131: '长海路街道社区文化活动分中心',
  shanghai_gov_community_133: '延吉社区文化活动中心',
  shanghai_gov_community_134: '江浦社区文化活动中心',
  shanghai_gov_community_135: '江浦路街道社区文化活动分中心',
  shanghai_gov_community_136: '控江路街道社区文化活动中心',
  shanghai_gov_community_137: '控江路街道社区文化活动分中心',
  shanghai_gov_community_138: '殷行社区文化活动中心',
  shanghai_gov_community_139: '新江湾城社区文化活动中心',
  shanghai_gov_community_140: '政青路文化活动分中心',
  shanghai_gov_community_141: '罗店镇社区文化活动中心',
  shanghai_gov_community_142: '罗店镇社区文化活动分中心',
  shanghai_gov_community_145: '友谊路街道社区事务受理服务中心',
  shanghai_gov_community_146: '友谊路街道社区文化活动分中心',
  shanghai_gov_community_147: '顾村镇社区文化活动中心',
  shanghai_gov_community_148: '顾村镇菊泉文体中心',
  shanghai_gov_community_149: '顾村镇馨佳园社区文化活动中心',
  shanghai_gov_community_150: '罗泾镇社区文化活动中心',
  shanghai_gov_community_151: '罗泾镇社区文化活动分中心',
  shanghai_gov_community_152: '吴淞街道社区文化活动中心',
  shanghai_gov_community_153: '高境镇社区文化活动中心',
  shanghai_gov_community_154: '高境镇社区文化活动分中心',
  shanghai_gov_community_155: '杨行镇社会事业发展服务中心',
  shanghai_gov_community_156: '庙行镇社区文化活动中心',
  shanghai_gov_community_157: '庙行镇社区文化活动分中心',
  shanghai_gov_community_158: '淞南镇社区文化活动中心',
  shanghai_gov_community_159: '月浦镇社区文化活动中心',
  shanghai_gov_community_160: '月浦镇社区文化中心（友间公寓分中心）',
  shanghai_gov_community_161: '张庙街道社区文化活动中心',
  shanghai_gov_community_162: '大场镇社会事业发展服务中心',
  shanghai_gov_community_163: '虹桥镇文化体育事业发展中心',
  shanghai_gov_community_164: '颛桥镇文体中心',
  shanghai_gov_community_165: '江川文化馆',
  shanghai_gov_community_166: '新虹街道社区党群服务中心',
  shanghai_gov_community_167: '古美路街道社区党群服务中心',
  shanghai_gov_community_168: '马桥景城文化中心',
  shanghai_gov_community_169: '华漕镇文化体育事业发展中心',
  shanghai_gov_community_170: '莘庄工业区文化体育事业发展中心',
  shanghai_gov_community_171: '浦江镇社区文化活动中心',
  shanghai_gov_community_172: '浦江镇青少年社区文化活动中心',
  shanghai_gov_community_173: '浦江镇瑞和社区文化活动中心',
  shanghai_gov_community_174: '吴泾镇社区文化活动中心',
  shanghai_gov_community_175: '莘庄镇文化体育事业发展中心',
  shanghai_gov_community_176: '七宝镇文化体育事业发展中心',
  shanghai_gov_community_177: '七宝体育活动中心（航华分中心）',
  shanghai_gov_community_178: '闵行区梅陇镇文化体育事业发展中心',
  shanghai_gov_community_179: '浦锦街道社区党群服务中心（文化体育）',
  shanghai_gov_community_180: '嘉定镇社区党群服务中心',
  shanghai_gov_community_181: '外冈镇文化体育服务中心',
  shanghai_gov_community_182: '菊园新区社区文化活动中心',
  shanghai_gov_community_183: '新成路街道社区党群服务中心',
  shanghai_gov_community_184: '南翔镇文化体育服务中心',
  shanghai_gov_community_185: '华亭镇社区文化活动中心',
  shanghai_gov_community_186: '真新街道社区党群服务中心',
  shanghai_gov_community_187: '徐行镇文化体育服务中心',
  shanghai_gov_community_188: '江桥镇社区文化活动中心',
  shanghai_gov_community_189: '嘉定工业区文化体育服务中心',
  shanghai_gov_community_190: '马陆镇文化体育服务中心',
  shanghai_gov_community_191: '安亭镇文化体育服务中心',
  shanghai_gov_community_192: '安亭镇文化体育服务中心黄渡分中心',
  shanghai_gov_community_193: '安亭镇文化体育服务中心方泰分中心',
  shanghai_gov_community_194: '朱泾镇社区文化活动中心',
  shanghai_gov_community_195: '朱泾镇社区文化活动中心新农分中心',
  shanghai_gov_community_196: '山阳镇社区党群服务中心',
  shanghai_gov_community_197: '漕泾镇社区党群服务中心',
  shanghai_gov_community_198: '枫泾镇社区党群服务中心',
  shanghai_gov_community_199: '枫泾镇社区文化活动中心兴塔分中心',
  shanghai_gov_community_200: '吕巷镇社区党群服务中心',
  shanghai_gov_community_201: '亭林镇社区文化活动中心',
  shanghai_gov_community_202: '亭林镇社区文化活动中心松隐分中心',
  shanghai_gov_community_203: '高新区社区文化活动中心',
  shanghai_gov_community_204: '金山卫镇社区党群服务中心',
  shanghai_gov_community_205: '金山卫镇社区文化活动中心钱圩分中心',
  shanghai_gov_community_206: '廊下镇社区党群服务中心',
  shanghai_gov_community_207: '张堰镇社区党群服务中心',
  shanghai_gov_community_208: '石化街道社区党群服务中心',
  shanghai_gov_community_209: '方松社区文化活动中心',
  shanghai_gov_community_210: '中山街道社区党群服务中心（中山幸福里）',
  shanghai_gov_community_211: '永丰街道社区党群服务中心',
  shanghai_gov_community_212: '佘山镇社区文化活动中心',
  shanghai_gov_community_213: '佘山镇社区文化活动中心佘北分中心',
  shanghai_gov_community_214: '泗泾镇社区文化活动中心',
  shanghai_gov_community_215: '泗泾镇新凯社区文化活动中心',
  shanghai_gov_community_216: '九亭镇社区文化活动中心',
  shanghai_gov_community_217: '新浜镇社区文化活动中心',
  shanghai_gov_community_218: '车墩镇社区文化活动中心',
  shanghai_gov_community_219: '岳阳街道社区党群服务中心',
  shanghai_gov_community_220: '叶榭镇社区文化活动中心',
  shanghai_gov_community_221: '广富林街道社区文化活动中心',
  shanghai_gov_community_222: '洞泾镇社区文化活动中心',
  shanghai_gov_community_223: '新桥镇社区党群服务中心',
  shanghai_gov_community_224: '九里亭街道社区党群服务中心',
  shanghai_gov_community_225: '石湖荡镇社区文化活动中心',
  shanghai_gov_community_226: '泖港镇社区文化活动中心',
  shanghai_gov_community_227: '小昆山镇社区党群服务中心',
  shanghai_gov_community_228: '徐泾社区文化活动中心',
  shanghai_gov_community_229: '徐泾北大居社区文化活动分中心',
  shanghai_gov_community_230: '练塘镇社区文化活动中心',
  shanghai_gov_community_231: '练塘镇社区文化活动中心（小蒸分中心）',
  shanghai_gov_community_232: '练塘镇社区文化活动中心（蒸淀分中心）',
  shanghai_gov_community_233: '白鹤镇社区文化活动中心',
  shanghai_gov_community_234: '白鹤镇社区文化活动中心（赵屯分中心）',
  shanghai_gov_community_235: '朱家角镇社区文化活动中心',
  shanghai_gov_community_236: '朱家角镇沈巷社区文化活动中心',
  shanghai_gov_community_237: '重固镇社区文化活动中心',
  shanghai_gov_community_238: '华新镇文化体育服务中心',
  shanghai_gov_community_239: '凤溪社区文化体育服务中心（凤溪分中心）',
  shanghai_gov_community_240: '赵巷镇社区文化活动中心',
  shanghai_gov_community_241: '赵巷镇新城一站大居社区文化体育服务中心',
  shanghai_gov_community_242: '金泽镇社区文化活动中心',
  shanghai_gov_community_243: '金泽镇社区文化活动服务中心商榻分中心',
  shanghai_gov_community_244: '盈浦街道社区文化活动中心',
  shanghai_gov_community_245: '夏阳街道社区文化活动中心',
  shanghai_gov_community_246: '香花桥街道社区文化活动中心',
  shanghai_gov_community_247: '香花桥街道清河湾U365党群服务中心（社区文化活动分中心）',
  shanghai_gov_community_248: '金汇镇社区文化活动中心',
  shanghai_gov_community_249: '金汇镇社区文化活动中心泰日分中心',
  shanghai_gov_community_250: '徐里桥社区文化活动中心',
  shanghai_gov_community_251: '青村镇社区文化活动中心',
  shanghai_gov_community_252: '青村镇社区文化活动中心钱桥分中心',
  shanghai_gov_community_253: '柘林镇社区文化活动中心',
  shanghai_gov_community_254: '庄行镇社区文化活动中心',
  shanghai_gov_community_255: '庄行镇社区文化活动中心（邬桥分中心）',
  shanghai_gov_community_256: '四团镇社区文化活动中心',
  shanghai_gov_community_257: '海湾镇社区文化活动中心',
  shanghai_gov_community_258: '奉城镇社区文化活动中心',
  shanghai_gov_community_259: '金海街道社区文化活动中心',
  shanghai_gov_community_260: '海湾旅游区社区文化活动中心',
  shanghai_gov_community_261: '奉浦街道社区文化活动中心',
  shanghai_gov_community_262: '西渡街道社区文化活动中心',
  shanghai_gov_community_263: '头桥街道社区文化活动中心',
  shanghai_gov_community_264: '竖新镇社区文化活动中心',
  shanghai_gov_community_265: '横沙乡社区党群服务中心',
  shanghai_gov_community_266: '建设镇社区党群服务中心',
  shanghai_gov_community_267: '堡镇社区文化活动中心',
  shanghai_gov_community_268: '港西镇社区党群服务中心',
  shanghai_gov_community_269: '港沿镇社区党群服务中心',
  shanghai_gov_community_270: '东平镇社区文化活动中心',
  shanghai_gov_community_271: '绿华镇社区文化活动中心',
  shanghai_gov_community_272: '新海镇社区文化活动中心',
  shanghai_gov_community_273: '新村乡社区党群服务中心',
  shanghai_gov_community_274: '新河镇社区党群服务中心',
  shanghai_gov_community_275: '中兴镇社区文化活动中心',
  shanghai_gov_community_276: '三星镇社区文化活动中心',
  shanghai_gov_community_277: '城桥镇社区党群服务中心 （城桥镇文体服务中心）',
  shanghai_gov_community_278: '庙镇社区文化活动中心',
  shanghai_gov_community_279: '陈家镇社区文化活动中心',
  shanghai_gov_community_280: '长兴镇社区党群服务中心',
  shanghai_gov_community_281: '向化镇社区文化活动中心',
  shanghai_gov_theatre_1: '上海黄浦剧场有限公司',
  shanghai_gov_theatre_2: '上海黄浦剧场有限公司（小剧场）',
  shanghai_gov_theatre_3: '上海木偶剧团有限公司',
  shanghai_gov_theatre_4: '上海木偶剧团有限公司（小剧场）',
  shanghai_gov_theatre_5: '上海新光影艺苑有限公司',
  shanghai_gov_theatre_6: '上海共舞台有限公司',
  shanghai_gov_theatre_7: '上海中国大戏院有限公司',
  shanghai_gov_theatre_8: '上海市卢湾体育中心',
  shanghai_gov_theatre_9: '上海儿童国际文化发展有限公司（上海儿童艺术剧场-黑匣子剧场）',
  shanghai_gov_theatre_10: '上海儿童国际文化发展有限公司（上海儿童艺术剧场-中心剧场）',
  shanghai_gov_theatre_11: '上海儿童国际文化发展有限公司（上海儿童艺术剧场-小剧场）',
  shanghai_gov_theatre_12: '上海大剧院-大剧场',
  shanghai_gov_theatre_13: '上海大剧院-中剧场',
  shanghai_gov_theatre_14: '上海大剧院-小剧场',
  shanghai_gov_theatre_16: '上海音乐厅小剧场',
  shanghai_gov_theatre_17: '上海天蟾逸夫舞台',
  shanghai_gov_theatre_18: '上海兰心大戏院',
  shanghai_gov_theatre_19: '上海人民大舞台',
  shanghai_gov_theatre_20: '上海文化广场剧院管理有限公司',
  shanghai_gov_theatre_21: '上海市黄浦区文化馆（上海市雅庐书场）-白玉兰剧场',
  shanghai_gov_theatre_22: '上海市黄浦区文化馆（上海市雅庐书场）-雅庐书场',
  shanghai_gov_theatre_23: '上海长江剧场（红匣子）',
  shanghai_gov_theatre_24: '上海长江剧场（黑匣子）',
  shanghai_gov_theatre_25: '上海豫尚文化传播有限公司',
  shanghai_gov_theatre_26: '上海话剧艺术中心有限公司黄浦分公司（茉莉花剧场）',
  shanghai_gov_theatre_27: '上海八佰秀企业管理有限公司',
  shanghai_gov_theatre_28: '上展中心剧院',
  shanghai_gov_theatre_29: '上海小伙伴剧场',
  shanghai_gov_theatre_30: '上海尚演文化投资管理有限公司',
  shanghai_gov_theatre_31: '上海戏剧学院',
  shanghai_gov_theatre_32: '文艺会堂',
  shanghai_gov_theatre_33: '兰馨影业有限公司-光影车间.静剧场',
  shanghai_gov_theatre_34: '中国福利会儿童艺术剧院(马兰花剧场)',
  shanghai_gov_theatre_35: '静安体育中心',
  shanghai_gov_theatre_36: '上戏实验剧院',
  shanghai_gov_theatre_37: '云峰剧院',
  shanghai_gov_theatre_38: '上海美琪大戏院',
  shanghai_gov_theatre_39: '上海马戏城有限公司',
  shanghai_gov_theatre_40: '上海商城有限公司',
  shanghai_gov_theatre_41: '上海市闸北区宋园茶艺馆（书场）',
  shanghai_gov_theatre_42: '海上文化管理中心-大宁剧院',
  shanghai_gov_theatre_43: '上海铁路工人文化宫',
  shanghai_gov_theatre_44: '上海市沪北电影院有限责任公司',
  shanghai_gov_theatre_45: '上海艺海剧场',
  shanghai_gov_theatre_46: '上海话剧艺术中心-艺术剧院',
  shanghai_gov_theatre_47: '上海话剧艺术中心-戏剧沙龙',
  shanghai_gov_theatre_48: '上海话剧艺术中心-D6空间',
  shanghai_gov_theatre_49: '上海大戏院',
  shanghai_gov_theatre_51: '上海交响乐团音乐厅',
  shanghai_gov_theatre_52: '徐汇区田林街道社区文化活动中心',
  shanghai_gov_theatre_53: '上音歌剧院',
  shanghai_gov_theatre_54: '上海东亚体育文化中心有限公司',
  shanghai_gov_theatre_55: '上海大舞台',
  shanghai_gov_theatre_56: '上海表坊文化发展有限公司-上剧场',
  shanghai_gov_theatre_57: '上海市宛平艺苑',
  shanghai_gov_theatre_58: '虹口足球场',
  shanghai_gov_theatre_59: '上海摩登嘉旋文化发展有限公司',
  shanghai_gov_theatre_60: '虹口区曲阳文化馆',
  shanghai_gov_theatre_61: '1933微剧场',
  shanghai_gov_theatre_62: '虹口区工人文化宫',
  shanghai_gov_theatre_63: '上海丝芭文化传媒有限公司-星梦剧场',
  shanghai_gov_theatre_64: '精武体育馆',
  shanghai_gov_theatre_65: '上海泛景文化传播有限公司-珍珠剧场',
  shanghai_gov_theatre_66: '上海盈寰文化传媒有限公司-BlueNote',
  shanghai_gov_theatre_67: '上海虹口保利大剧院管理有限公司-北外滩友邦大剧院',
  shanghai_gov_theatre_68: '上海市长宁民俗文化中心',
  shanghai_gov_theatre_69: '上海市长宁文化艺术中心',
  shanghai_gov_theatre_70: '上海国际舞蹈中心剧场经营管理有限公司',
  shanghai_gov_theatre_71: '上海东虹桥剧院管理有限公司',
  shanghai_gov_theatre_72: '江川剧场',
  shanghai_gov_theatre_73: '上海新东苑实业有限公司',
  shanghai_gov_theatre_74: '新浦江影剧院',
  shanghai_gov_theatre_75: '旗忠森林体育城',
  shanghai_gov_theatre_76: '吴泾文化馆',
  shanghai_gov_theatre_77: '上海城市剧院管理有限公司',
  shanghai_gov_theatre_78: '上海零聚演出经纪有限公司',
  shanghai_gov_theatre_79: '索石文化传播（上海）有限公司',
  shanghai_gov_theatre_80: '上海零湾美琪剧院管理有限公司',
  shanghai_gov_theatre_81: '上海市青浦区文化馆',
  shanghai_gov_theatre_82: '青浦区赵巷镇文化中心站',
  shanghai_gov_theatre_83: '青浦重固影剧院',
  shanghai_gov_theatre_84: '青浦朱家角影剧院',
  shanghai_gov_theatre_85: '练塘影剧院',
  shanghai_gov_theatre_86: '上海虹馆文化发展有限公司',
  shanghai_gov_theatre_87: '上海释乐文化传播有限公司',
  shanghai_gov_theatre_88: '上海市优演剧场管理有限公司',
  shanghai_gov_theatre_89: '青隐（上海）文化艺术发展有限公司',
  shanghai_gov_theatre_90: '上海乐演优你科技有限公司',
  shanghai_gov_theatre_91: 'YOUNG剧场-大剧院',
  shanghai_gov_theatre_92: 'YOUNG剧场-小剧院',
  shanghai_gov_theatre_93: '东宫剧院',
  shanghai_gov_theatre_94: '上海国际时尚中心园区管理有限公司',
  shanghai_gov_theatre_95: '梅赛德斯-奔驰文化中心',
  shanghai_gov_theatre_96: '梅赛德斯-奔驰文化中心-音乐俱乐部',
  shanghai_gov_theatre_97: '南汇海东影剧院',
  shanghai_gov_theatre_98: '上海南汇周浦影剧场',
  shanghai_gov_theatre_99: '南汇宣桥镇影剧院',
  shanghai_gov_theatre_100: '上海艺晟文化传播有限公司',
  shanghai_gov_theatre_101: '上海浦东新区三墩影剧院',
  shanghai_gov_theatre_102: '上海浦东新区川沙影剧院',
  shanghai_gov_theatre_103: '南汇盐仓影剧院',
  shanghai_gov_theatre_104: '上海浦东新区东方电影院有限公司',
  shanghai_gov_theatre_105: '上海市浦东新区航头镇书场茶馆',
  shanghai_gov_theatre_106: '南汇三灶影剧院',
  shanghai_gov_theatre_107: '上海市南汇大团镇永春演艺厅',
  shanghai_gov_theatre_108: '上海市南汇航头镇陶园春演艺厅',
  shanghai_gov_theatre_109: '上海尚银东艺数字影城管理有限公司',
  shanghai_gov_theatre_110: '上海兰馨影业有限公司',
  shanghai_gov_theatre_111: '上海市澧溪文化艺术有限公司',
  shanghai_gov_theatre_112: '上海野生动物园发展有限公司',
  shanghai_gov_theatre_114: '上海证大喜马拉雅演艺有限公司',
  shanghai_gov_theatre_115: '保利尚悦湾（上海）剧院管理有限公司1862时尚艺术中心',
  shanghai_gov_theatre_116: '上海东方艺术中心管理有限公司-音乐厅',
  shanghai_gov_theatre_117: '上海东方艺术中心管理有限公司-歌剧厅',
  shanghai_gov_theatre_118: '上海东方艺术中心管理有限公司-演奏厅',
  shanghai_gov_theatre_119: '上海笋馨文化传媒有限公司',
  shanghai_gov_theatre_120: '上海冉旭文化娱乐中心',
  shanghai_gov_theatre_121: '上海张江文化控股有限公司-张江戏剧谷',
  shanghai_gov_theatre_122: '上海世博中心有限公司(红厅）',
  shanghai_gov_theatre_123: '迪士尼-大剧院',
  shanghai_gov_theatre_124: '迪士尼-凡迭戈剧院、林间剧场、故事舞台',
  shanghai_gov_theatre_126: '上海浦东新区三林影剧院',
  shanghai_gov_theatre_127: '上海宋城世博演艺发展有限公司-千古情',
  shanghai_gov_theatre_128: '上海宋城世博演艺发展有限公司-百乐门',
  shanghai_gov_theatre_129: '上海外高桥文化传播有限公司',
  shanghai_gov_theatre_130: '信德前滩（上海）文化置业有限公司',
  shanghai_gov_theatre_131: '上海乐来乐好剧院管理有限公司',
  shanghai_gov_theatre_132: '上海市奉贤区机关服务中心',
  shanghai_gov_theatre_133: '上海邬桥牡丹影剧院',
  shanghai_gov_theatre_134: '奉贤区南桥影剧院',
  shanghai_gov_theatre_135: '上海胡桥影剧院',
  shanghai_gov_theatre_136: '上海柘林影剧院',
  shanghai_gov_theatre_137: '上海奉贤钱桥影剧院',
  shanghai_gov_theatre_138: '奉贤县青村文化站',
  shanghai_gov_theatre_139: '上海九棵树文化传媒有限公司—大剧场',
  shanghai_gov_theatre_140: '上海九棵树文化传媒有限公司—小剧场',
  shanghai_gov_theatre_141: '上海九棵树文化传媒有限公司—实验剧场',
  shanghai_gov_theatre_142: '上海九棵树文化传媒有限公司—森林剧场',
  shanghai_gov_theatre_143: '上海九棵树文化传媒有限公司—水岸舞台',
  shanghai_gov_theatre_145: '依弘剧场',
  shanghai_gov_theatre_146: '上海星轶思达爱斯影院管理有限公司',
  shanghai_gov_theatre_147: '上海保利大剧院',
  shanghai_gov_theatre_148: '嘉定影剧院有限责任公司',
  shanghai_gov_theatre_149: '开心麻花剧场',
  shanghai_gov_theatre_150: '上海市崇明影剧院',
  shanghai_gov_theatre_151: '崇明县沪剧团',
  shanghai_gov_theatre_152: '上海风瀛洲文化传播有限公司',
  shanghai_gov_theatre_153: '海昌海洋公园-欢乐剧场',
  shanghai_gov_theatre_154: '海昌海洋公园-海豚表演场',
  shanghai_gov_theatre_155: '海昌海洋公园-大型动物表演场',
  shanghai_gov_theatre_156: '泥城影剧院',
  shanghai_gov_theatre_157: '万祥影剧院',
  shanghai_gov_theatre_158: '上海聆海美琪文化艺术发展有限公司（临港演艺中心）',
  shanghai_gov_theatre_159: '上海展博置业有限公司（滴水湖剧院）',
  shanghai_gov_theatre_160: '上海保利云间剧院管理有限公司',
  wuhan_gov_1437233: '武汉市群众艺术馆（武汉市非物质文化遗产保护中心）',
  wuhan_gov_1437235: '武汉革命博物馆（武昌农民运动讲习所旧址纪念馆，中共五大会址纪念馆）',
  wuhan_gov_1437237: '武汉市中山舰博物馆',
  wuhan_gov_1437239: '武汉中共中央机关旧址纪念馆',
  wuhan_gov_1437243: '武汉汉剧院',
  wuhan_gov_1437246: '武汉博物馆（武汉市文物交流中心）',
  wuhan_gov_1437247: '江汉关博物馆（武汉国民政府旧址纪念馆、詹天佑故居博物馆）',
  wuhan_gov_1437251: '武汉市晴川阁管理处（武汉大禹文化博物馆）',
  wuhan_gov_1437249: '八七会议会址纪念馆',
  wuhan_gov_1437250: '八路军武汉办事处旧址纪念馆（汉口新四军军部旧址纪念馆）',
  wuhan_gov_1437253: '武汉楚剧院有限责任公司(武汉楚剧院)',
  wuhan_gov_1437254: '武汉京剧院有限责任公司(武汉京剧院)',
  xian_gov_1901554530815434753: '经开区文化艺术中心',
  xian_gov_62d8ba0ef8fd1c4c210ae016: '西安市鄠邑区非物质文化遗产博物馆',
  xian_gov_1716741181564076033: '西段遗址文物管理所',
  xian_gov_1712397055545675777: '长安区文化馆',
  xian_gov_4: '4、国家规定的其他免费服务项目',
  xian_gov_1763123354408628225: '蓝田县体育中心',
  xian_gov_5fbb551ff8fd1c59664b3711: '中渭桥遗址',
  xian_gov_25: '红25军军部旧址',
  xian_gov_1767090210230796290: '任家庄门楼',
  xian_gov_144: '北院门144号民居',
  xian_gov_232: '化觉巷232号民居',
  xian_gov_38: '大麦市街38号民居',
  xian_gov_1998584920184258561: '西安市鄠邑区公输堂小木作艺术博物馆',
  xian_gov_1998569549761884162: '鄠邑区文化馆',
  xian_gov_608a5b0df8fd1c20730c5c09: '读等服务',
  xian_gov_618490b1f8fd1c0bdc62ed8e: '代知识分子奋勇前进的磅礴伟力',
  xian_gov_5da6c0c865cbd86d495781e8: '陕西省西安市国家航空高技术产业基地航空二路华宇理想国接待中心',
  xian_gov_61: '新城区新科路61号',
  xian_gov_8: '新城区幸福北路8号',
  xian_gov_26: '新城区西五路26号',
  xian_gov_10: '新城区东站路10号新兴骏景园二期东门',
  xian_gov_158: '未央区渭滨路158号谭家街办文化站隔壁',
  xian_gov_13613110401: '西安市经开区未央路136-1号中讯大厦3幢1单元10401室',
  xian_gov_41: '莲湖区丰禾路41号',
  xian_gov_1351001: '莲湖区西大街135号西京饭店1001号',
  xian_gov_6: '莲湖区群贤路6号（唐延路北段锦都小区内）',
  xian_gov_3916: '雁塔区长安西路39号铭城16号一层商铺',
  xian_gov_3: '雁塔区长安南路华城泊郡3号楼',
  xian_gov_6f: '长安北路草场坡荣城小区商铺6F',
  xian_gov_10113: '周至县燕云府邸商铺一楼10113室',
  xian_gov_1: '长安区王曲街道鱼鲍头村甲子1号',
  xian_gov_1818857916155949058: '西安新梦想影业博物馆',
  xian_gov_07: '传统美术（07）',
  xian_gov_08: '传统技艺 （08）',
  xian_gov_11: '民俗（11）',
  xian_gov_09: '传统医药（09）',
  xian_gov_1716743219733606401: '临潼区图书馆骊阅分馆',
  xian_gov_61a43e9bf8fd1c0bdc700bfa: '汪锋故居及墓园',
  xian_gov_60b5fe19f8fd1c0bdc2dead1: '张云山墓',
  xian_gov_4039: '芦苇荡40号、39号姚家民居',
  xian_gov_85: '西七路85号民居',
  xian_gov_wlj: '西安市群众艺术馆',
  zhuhai_gov_tsg_xiangzhou: '香洲区图书馆',
  zhuhai_gov_bwg_xiangzhou: '香洲区博物馆',
  zhuhai_gov_bwg_shengbao: '珠海市盛宝博物馆',
  zhuhai_gov_bwg_handong: '珠海汉东博物馆',
  zhuhai_gov_bwg_yuhai: '珠海钰海博物馆',
  zhuhai_gov_bwg_puji: '珠海市普济艺术博物馆',
  zhuhai_gov_bwg_luoxini: '罗西尼钟表博物馆',
  zhuhai_gov_bwg_yuandao: '珠海市原道文化博物馆',
  zhuhai_gov_bwg_fuhua: '横琴粤澳深度合作区富华紫檀博物馆',
  zhuhai_gov_msg_guyuan: '珠海市古元美术馆',
  zhuhai_gov_tycg_doumen_gym: '斗门区体育馆',
  zhuhai_gov_tycg_doumen_gym2: '斗门体育馆',
  zhuhai_gov_tycg_doumen_fitness: '斗门全民健身中心',
  zhuhai_gov_tycg_jinwan_square: '金湾全民健身广场',
  zhuhai_gov_tycg_hengqin_square: '横琴镇全民健身广场',
  zhuhai_gov_tycg_tangjiawan_square: '唐家湾镇全民健身广场',
  zhuhai_gov_tycg_nanshui_square: '南水镇全民健身广场',
  zhuhai_gov_tycg_pingsha_square: '平沙镇全民健身广场',
  zhuhai_gov_tycg_guishan_square: '桂山镇全民健身广场',
  zhuhai_gov_tycg_dangan_square: '担杆镇全民健身广场',
  zhuhai_gov_tycg_wanshan_dawan: '万山镇全民健身广场（大万山岛）',
  zhuhai_gov_tycg_wanshan_dongao: '万山镇全民健身广场（东澳岛）'
};

// 场馆地址映射（自动生成）
const venueAddressMap = {
  深圳图书馆: '福田区福中一路2001号',
  深圳少年儿童图书馆: '福田区红荔路1011号',
  深圳博物馆: '福田区福中路市民中心A区',
  深圳科学技术馆: '光明区光明街道',
  深圳滨海艺术中心: '宝安区宝兴路8号',
  深圳音乐厅: '福田区福中一路2016号',
  深圳市当代艺术与城市规划馆: '福田区福中路184号',
  深圳市体育中心: '福田区笋岗西路',
  深圳市文化馆: '福田区燕南路',
  深圳自然博物馆: '坪山区石井街道',
  南山图书馆: '南山区常兴路176号',
  南山博物馆: '南山区南山大道2093号',
  南山区文化馆: '南山区',
  南山区青少年活动中心: '南山区',
  南山文体中心: '南山区南山大道',
  南山安全教育体验馆: '南山区',
  蛇口海洋科普馆: '南山区蛇口',
  深爱人才馆: '南山区',
  南头古城博物馆群: '南山区南山大道3109号',
  招商局历史博物馆: '南山区蛇口',
  南山书房: '南山区',
  华侨城湿地: '南山区白石路',
  深圳湾体育中心: '南山区滨海大道',
  欢乐港湾: '宝安区海天路',
  福田区图书馆: '福田区景田路70号',
  福田区文化馆: '福田区',
  福田美术馆: '福田区',
  深圳古生物博物馆: '罗湖区仙湖植物园内',
  罗湖区图书馆: '罗湖区怡景路1014号',
  罗湖区文化馆: '罗湖区',
  深圳戏院: '罗湖区新园路1号',
  深圳大剧院: '罗湖区深南东路5018号',
  宝安图书馆: '宝安区宝兴路1号',
  宝安区博物馆: '宝安区',
  宝安1990文化馆: '宝安区',
  宝安科技馆: '宝安区',
  宝安体育中心: '宝安区',
  宝安区青少年宫: '宝安区',
  宝安城市规划展览馆: '宝安区',
  湾区之眼: '宝安区',
  龙岗区图书馆: '龙岗区中心城',
  龙岗区博物馆: '龙岗区',
  龙岗区文化馆: '龙岗区',
  龙岗区青少年宫: '龙岗区',
  龙岗客家民俗博物馆: '龙岗区龙岗街道鹤湖新居',
  龙岗体育中心: '龙岗区',
  深圳龙岗国际艺术中心: '龙岗区',
  龙岗区科技馆: '龙岗区',
  龙岗儿童公园: '龙岗区',
  龙华区图书馆: '龙华区',
  龙华区青少年宫: '龙华区',
  龙华区文化馆: '龙华区',
  中国版画博物馆: '龙华区观澜街道',
  龙华生态文明展览馆: '龙华区',
  龙华区科技馆: '龙华区',
  龙华白石龙纪念馆: '龙华区',
  光明区图书馆: '光明区',
  光明区科技馆: '光明区',
  光明区文化馆: '光明区',
  光明文化艺术中心: '光明区',
  光明区青少年活动中心: '光明区',
  光明区群众体育中心: '光明区',
  光明虹桥公园: '光明区',
  玉塘文体中心: '光明区玉塘街道',
  坪山区图书馆: '坪山区坪山街道',
  坪山美术馆: '坪山区',
  坪山大剧院: '坪山区',
  坪山区科技馆: '坪山区',
  坪山体育中心: '坪山区',
  坪山东江纵队纪念馆: '坪山区',
  坪山中心公园: '坪山区',
  马峦山郊野公园: '坪山区马峦山',
  聚龙山生态公园: '坪山区聚龙山',
  燕子湖国际会展中心: '坪山区燕子湖',
  盐田区图书馆: '盐田区',
  盐田区文化馆: '盐田区',
  中英街历史博物馆: '盐田区沙头角中英街',
  盐田科技馆: '盐田区',
  盐田体育中心: '盐田区',
  盐田中央公园: '盐田区',
  大鹏地质公园博物馆: '大鹏新区南澳街道地质公园路7号',
  大亚湾核能科技馆: '大鹏新区大亚湾核电基地',
  大鹏新区图书馆: '大鹏新区大鹏街道',
  大鹏古城博物馆: '大鹏新区大鹏街道',
  大鹏新区文化馆: '大鹏新区大鹏街道',
  深圳西涌天文台: '大鹏新区南澳西涌',
  东涌红树林湿地公园: '大鹏新区南澳东涌',
  坝光红树林湿地公园: '大鹏新区葵涌坝光',
  玫瑰海岸: '大鹏新区溪涌玫瑰海岸',
  杨梅坑: '大鹏新区南澳杨梅坑',
  七娘山: '大鹏新区南澳七娘山',
  官湖村艺象艺术区: '大鹏新区葵涌官湖村',
  金沙湾国际乐园: '大鹏新区金沙湾',
  大鹏新区科学馆: '大鹏新区',
  大鹏较场尾沙滩: '大鹏新区大鹏街道较场尾',
  葵涌生态公园: '大鹏新区葵涌',
  深圳市安全教育基地: '福田区',
  OPOWER文化艺术中心: '南山区华侨城',
  坪山区青少年宫: '坪山区',
  广东省博物馆: '天河区珠江东路2号',
  广州博物馆: '越秀区镇海路',
  广州图书馆: '天河区珠江东路4号',
  上海博物馆: '黄浦区人民大道201号',
  上海科技馆: '浦东新区世纪大道2000号',
  中国国家博物馆: '东城区东长安街16号',
  故宫博物院: '东城区景山前街4号',
  何香凝美术馆: '南山区深南大道9013号',
  关山月美术馆: '福田区红荔路6026号',
  深圳美术馆: '罗湖区爱国路东湖公园内',
  深圳保利剧院: '南山区后海滨路',
  深圳会展中心: '福田区福华三路',
  深圳国际会展中心: '宝安区福海街道',
  锦绣中华民俗村: '南山区深南大道9003号',
  深圳市少年宫: '福田区福中一路2006号',
  深圳市青少年活动中心: '福田区红荔路',
  深圳书城: '福田区福中一路',
  深圳湾公园: '南山区滨海大道',
  海上世界文化艺术中心: '南山区蛇口海上世界',
  深圳中医药博物馆: '福田区',
  深圳珠宝博物馆: '盐田区',
  深圳欢乐谷: '南山区华侨城',
  深圳欢乐海岸: '南山区白石路',
  深圳世界之窗: '南山区深南大道9003号',
  洪湖公园: '罗湖区文锦北路',
  大沙河生态长廊: '南山区大沙河',
  淘金山绿道: '罗湖区淘金山',
  西湾红树林公园: '宝安区西乡',
  茅洲河碧道: '光明区茅洲河',
  石岩湖湿地公园: '宝安区石岩',
  石岩文化艺术中心: '宝安区石岩',
  红花山公园: '坪山区',
  深圳大运中心: '龙岗区龙城街道',
  大运中心公园: '龙岗区大运中心',
  安托山公共文化中心: '福田区安托山',
  北站中心公园: '龙华区深圳北站',
  '深圳科学公园（南翼）': '光明区',
  人才公园: '南山区科苑南路',
  吉华街道文化站: '龙岗区吉华街道',
  南湾街道文化站: '龙岗区南湾街道',
  坪地街道文化站: '龙岗区坪地街道',
  园岭街道综合性文化服务中心: '福田区园岭街道',
  桃源街道综合性文化服务中心: '南山区桃源街道',
  凤凰街道综合性文化服务中心: '光明区凤凰街道',
  江岭社区公共文化服务中心: '坪山区江岭社区',
  迳口社区综合性文化服务中心: '光明区迳口社区',
  浙江省博物馆: '西湖区孤山路',
  中国科学技术馆: '朝阳区北辰东路5号',
  北京天文馆: '西城区西直门外大街138号',
  国家自然博物馆: '东城区天桥南大街126号',
  国家动物博物馆: '朝阳区北辰西路1号院5号',
  中国消防博物馆: '西城区广安门南街70号',
  北京汽车博物馆: '丰台区南四环西路126号',
  北京动物园: '西城区西直门外大街137号',
  北京海洋馆: '西城区西直门外大街137号北京动物园内',
  北京欢乐谷: '朝阳区东四环小武基北路',
  水立方嬉水乐园: '朝阳区天辰东路11号国家游泳中心内',
  欢乐水魔方水上乐园: '丰台区小屯路11号',
  朝阳公园: '朝阳区朝阳公园南路1号',
  世界公园: '丰台区花乡大葆台158号',
  北京野生动物园: '大兴区榆垡镇万亩森林',
  北京科学中心: '西城区北辰路9号院',
  中国地质博物馆: '西城区西四羊肉胡同15号',
  北京奥运博物馆: '朝阳区国家体育场南路1号',
  中国航空博物馆: '昌平区小汤山镇',
  中国考古博物馆: '朝阳区国家体育场北路1号院1号楼',
  中国园林博物馆: '丰台区射击场路15号',
  中国军事博物馆: '海淀区复兴路9号',
  海淀公共安全馆: '海淀区新建宫门路2号',
  乐高探索中心: '普陀区大渡河路196号长风大悦城',
  首都图书馆: '朝阳区东三环南路88号',
  国家图书馆: '海淀区中关村南大街33号',
  中国妇女儿童博物馆: '东城区北极阁路9号',
  中国古动物馆: '西城区西直门外大街142号',
  索尼探梦科技馆: '朝阳区朝阳公园南路1号',
  泡泡玛特城市乐园: '朝阳区朝阳公园南路1号',
  北京植物园: '海淀区香山路',
  颐和园: '海淀区新建宫门路19号',
  天坛公园: '东城区天坛东路甲1号',
  地坛公园: '东城区安定门外大街',
  北海公园: '西城区文津街1号',
  景山公园: '西城区景山西街44号',
  中山公园: '西城区西长安街2号',
  劳动人民文化宫: '东城区太庙路',
  北京天文馆A馆: '西城区西直门外大街138号',
  北京天文馆B馆: '西城区西直门外大街138号',
  北京展览馆: '西城区西直门外大街135号',
  中国美术馆: '东城区五四大街1号',
  北京音乐厅: '西城区北新华街1号',
  国家大剧院: '西城区西长安街2号',
  梅兰芳大剧院: '西城区平安里西大街32号',
  长安大戏院: '东城区建国门内大街7号',
  北京儿艺剧场: '东城区交道口东大街85号',
  北京展览馆剧场: '西城区西直门外大街135号',
  北京工人体育馆: '朝阳区三里屯路11号',
  北京工人体育场: '朝阳区工人体育场北路',
  五棵松体育馆: '海淀区复兴路69号',
  奥林匹克森林公园: '朝阳区科荟路33号',
  元大都城垣遗址公园: '朝阳区安定路',
  奥林匹克公园: '朝阳区国家体育场南路',
  朝阳公园海洋沙滩狂欢节: '朝阳区朝阳公园南路1号',
  蟹岛度假村: '朝阳区蟹岛路1号',
  南宫旅游景区: '丰台区王佐镇',
  北京莲花池公园: '丰台区广安门外大街',
  北京世界花卉大观园: '丰台区南四环中路235号',
  北京园博园: '丰台区射击场路15号',
  北京石景山游乐园: '石景山区石景山路25号',
  八大处公园: '石景山区八大处路3号',
  法海寺: '石景山区模式口大街',
  首钢园: '石景山区首钢大街',
  北京国际雕塑公园: '石景山区石景山路2号',
  百望山森林公园: '海淀区黑山扈北口19号',
  凤凰岭自然风景区: '海淀区苏家坨镇',
  鹫峰国家森林公园: '海淀区苏家坨镇',
  阳台山自然风景区: '海淀区苏家坨镇',
  香山公园: '海淀区买卖街40号',
  北京植物园樱桃沟: '海淀区香山路北京植物园内',
  北京植物园温室: '海淀区香山路北京植物园内',
  北京天文馆天象厅: '西城区西直门外大街138号',
  中国科学技术馆儿童科学乐园: '朝阳区北辰东路5号',
  北京城市图书馆: '通州区新华东街',
  北京环球度假区: '通州区环球大道',
  北京运河奥体公园: '通州区运河奥体公园',
  北京西海子公园: '通州区新华北路',
  北京运河森林公园: '通州区运河西大街',
  北京东郊湿地公园: '通州区宋庄镇',
  北京张家湾公园: '通州区张家湾镇',
  北京台湖公园: '通州区台湖镇',
  北京月亮河公园: '通州区月亮河河滨路',
  北京路县故城遗址: '通州区潞城镇',
  北京通州博物馆: '通州区西大街',
  北京汉石桥湿地: '顺义区杨镇',
  北京奥林匹克水上公园: '顺义区白马路',
  北京顺义公园: '顺义区光明南街',
  北京顺义新城滨河森林公园: '顺义区潮白河',
  北京国际鲜花港: '顺义区杨镇',
  北京张裕爱斐堡国际酒庄: '密云区巨各庄镇',
  北京古北水镇: '密云区古北口镇',
  北京司马台长城: '密云区古北口镇',
  北京黑龙潭景区: '密云区石城镇',
  北京云蒙山景区: '密云区石城镇',
  北京雾灵山景区: '密云区新城子镇',
  北京金海湖景区: '平谷区金海湖镇',
  北京京东大峡谷: '平谷区山东庄镇',
  北京石林峡景区: '平谷区黄松峪乡',
  北京延庆奥林匹克园区: '延庆区',
  北京世园公园: '延庆区',
  北京八达岭国家森林公园: '延庆区八达岭',
  北京野鸭湖国家湿地公园: '延庆区康庄镇',
  北京龙庆峡景区: '延庆区龙庆峡',
  北京云居寺: '房山区张坊镇',
  北京十渡景区: '房山区十渡镇',
  北京房山世界地质公园: '房山区',
  北京上方山国家森林公园: '房山区韩村河镇',
  北京石花洞景区: '房山区河北镇',
  北京银狐洞景区: '房山区佛子庄乡',
  北京百花山景区: '房山区百花山镇',
  北京圣莲山景区: '房山区史家营乡',
  北京青龙湖公园: '房山区青龙湖镇',
  北京蒲洼乡花台景区: '房山区蒲洼乡',
  北京霞云岭国家森林公园: '房山区霞云岭乡',
  广东科学中心: '番禺区大学城科普路168号',
  广州青少年科技馆: '越秀区童心路西胜街42号',
  广州少年儿童图书馆: '越秀区中山四路42号',
  广州地铁博物馆: '海珠区新港东路万胜围地铁站A出口',
  广州市儿童公园: '白云区齐心路61号',
  广州动物园: '越秀区先烈中路120号',
  广州海洋馆: '越秀区先烈中路120号广州动物园内',
  正佳极地海洋世界: '天河区天河路228号正佳广场',
  正佳雨林生态植物园: '天河区天河路228号正佳广场7层',
  正佳自然科学博物馆: '天河区天河路228号正佳广场6楼',
  广州融创文旅城: '花都区凤凰北路78号',
  永庆坊: '荔湾区恩宁路99号',
  陈家祠: '荔湾区中山七路恩龙里34号',
  岭南印象园: '番禺区大学城外环西路',
  海珠国家湿地公园: '海珠区新滘中路',
  华南植物园: '天河区兴科路723号',
  白云山: '白云区广园中路801号',
  大夫山森林公园: '番禺区禺山西路668号',
  海鸥岛: '番禺区石楼镇',
  广州新儿童活动中心: '白云区云城东路509号',
  广州开发区科技馆: '黄埔区萝岗街道萝平路与香雪七路交汇处',
  广州艺术博物院: '越秀区麓湖路13号',
  南越王博物院: '越秀区解放北路867号',
  广州市文化馆新馆: '海珠区新滘中路288号',
  广州大剧院: '天河区珠江新城珠江西路1号',
  广州塔: '海珠区阅江西路222号',
  广州国际金融城: '天河区黄埔大道',
  广州北京路步行街: '越秀区北京路',
  广州上下九步行街: '荔湾区上下九路',
  广州天河城: '天河区天河路208号',
  广州太古汇: '天河区天河路383号',
  广州正佳广场: '天河区天河路228号',
  广州万菱汇: '天河区天河路230号',
  广州凯德广场: '白云区云城西路890号',
  广州白云万达广场: '白云区云城东路501号',
  广州越秀公园: '越秀区解放北路960号',
  广州流花湖公园: '越秀区流花路100号',
  广州荔湾湖公园: '荔湾区龙津西路155号',
  广州海珠湖公园: '海珠区新滘中路',
  广州天河公园: '天河区中山大道西270号',
  广州珠江公园: '天河区金穗路',
  广州麓湖公园: '越秀区麓湖路11号',
  广州东山湖公园: '越秀区东湖路123号',
  广州二沙岛: '越秀区二沙岛',
  广州沙面岛: '荔湾区沙面南街',
  广州长隆野生动物世界: '番禺区大石镇',
  广州长隆欢乐世界: '番禺区大石镇',
  广州长隆水上乐园: '番禺区大石镇',
  广州长隆飞鸟乐园: '番禺区大石镇',
  广州融创雪世界: '花都区凤凰北路78号',
  广州融创水世界: '花都区凤凰北路78号',
  广州融创体育世界: '花都区凤凰北路78号',
  广州花都湖公园: '花都区商业大道',
  广州增城白水寨: '增城区派潭镇',
  广州从化温泉: '从化区温泉镇',
  广州从化溪头村: '从化区良口镇',
  广州南沙湿地公园: '南沙区万顷沙镇',
  广州南沙天后宫: '南沙区大角山东南麓',
  广州黄埔军校旧址: '黄埔区长洲岛',
  广州南海神庙: '黄埔区庙头村',
  广州南越王宫博物馆: '越秀区中山四路316号',
  广州北京路千年古道遗址: '越秀区北京路',
  广州粤剧艺术博物馆: '荔湾区恩宁路127号',
  广州三二九起义指挥部旧址: '越秀区越华路116号',
  广州起义烈士陵园: '越秀区中山三路',
  广州鲁迅纪念馆: '越秀区文明路215号',
  广州近代史博物馆: '越秀区陵园西路2号',
  广州农民运动讲习所旧址: '越秀区中山四路42号',
  广州南越王墓博物馆: '越秀区解放北路867号',
  广州北京路天河城: '越秀区北京路',
  广州天河城百货: '天河区天河路208号',
  广州太古汇商场: '天河区天河路383号',
  广州维多利广场: '天河区体育西路103号',
  广州天河体育中心: '天河区天河路299号',
  广州珠江新城: '天河区珠江新城',
  广州花城广场: '天河区珠江新城',
  广州海心沙: '天河区珠江新城',
  广州琶洲会展中心: '海珠区阅江中路',
  广州塔摩天轮: '海珠区阅江西路222号广州塔',
  广州塔极速云霄: '海珠区阅江西路222号广州塔',
  广州塔户外观景平台: '海珠区阅江西路222号广州塔',
  广州海心桥: '天河区珠江新城',
  广州滨江公园: '海珠区滨江东路',
  广州二沙岛体育公园: '越秀区二沙岛',
  广州二沙岛艺术公园: '越秀区二沙岛',
  广州海印公园: '海珠区滨江东路',
  广州晓港公园: '海珠区前进路',
  广州黄埔公园: '黄埔区黄埔东路',
  广州萝岗香雪公园: '黄埔区萝岗街道',
  广州天鹿湖森林公园: '黄埔区联和街道',
  广州九龙湖度假区: '花都区花东镇',
  广州花都石头记矿物园: '花都区珠宝城',
  广州芙蓉嶂风景区: '花都区狮岭镇',
  广州九龙潭森林公园: '花都区北兴镇',
  广州花都融创乐园: '花都区花城大道',
  广州花都融创雪世界: '花都区花城大道',
  广州花都融创水世界: '花都区花城大道',
  广州花都融创体育世界: '花都区花城大道',
  广州从化流溪河国家森林公园: '从化区良口镇',
  广州从化碧水湾温泉: '从化区良口镇',
  广州增城正果老街: '增城区正果镇',
  '浙江省博物馆（之江馆）': '西湖区江涵路300号',
  '浙江省博物馆（孤山馆）': '西湖区孤山路25号',
  '浙江自然博物院（杭州馆）': '拱墅区西湖文化广场6号',
  浙江省科技馆: '拱墅区西湖文化广场2号',
  浙江省地质博物馆: '西湖区',
  浙江省非物质文化遗产馆: '西湖区江涵路300号之江文化中心',
  浙江图书馆: '西湖区江涵路300号之江文化中心',
  中国杭州低碳科技馆: '滨江区江汉路1888号',
  杭州亚运会博物馆: '滨江区奥体中心体育场地下一层',
  良渚博物院: '余杭区美丽洲路1号',
  中国丝绸博物馆: '西湖区玉皇山路73-1号',
  中国水利博物馆: '萧山区水博大道1号',
  中国茶叶博物馆: '西湖区龙井路88号',
  中国湿地博物馆: '西湖区天目山路402号',
  中国动漫博物馆: '滨江区白马湖路375号',
  杭州博物馆: '上城区粮道山18号',
  良渚古城遗址公园: '余杭区瓶窑镇凤都路',
  杭州野生动物世界: '富阳区受降镇杭富路九龙大道1号',
  杭州植物园: '西湖区桃源岭1号',
  西溪国家湿地公园: '西湖区天目山路518号',
  西湖风景名胜区: '西湖区西湖街道',
  杭州乐园: '萧山区风情大道2555号',
  杭州少年儿童图书馆: '西湖区曙光路75号',
  杭州科技馆: '拱墅区西湖文化广场',
  杭州中国茶叶博物馆龙井馆: '西湖区翁家山268号',
  杭州西湖博物馆: '上城区南山路89号',
  杭州京杭大运河博物馆: '拱墅区金华路88号',
  杭州工艺美术博物馆: '拱墅区小河路334号',
  杭州中国湿地博物馆: '西湖区天目山路402号',
  杭州青少年活动中心: '西湖区昭庆寺里街22号',
  杭州嘟嘟城: '江干区新业路331-399号',
  杭州西湖: '西湖区西湖街道',
  杭州灵隐寺: '西湖区灵隐路法云弄1号',
  杭州雷峰塔: '西湖区南山路15号',
  杭州岳庙: '西湖区北山路80号',
  杭州六和塔: '西湖区之江路16号',
  杭州虎跑公园: '西湖区虎跑路39号',
  杭州九溪烟树: '西湖区九溪路',
  杭州云栖竹径: '西湖区梅灵南路8号',
  杭州龙井村: '西湖区龙井路',
  杭州满陇桂雨: '西湖区满觉陇路',
  杭州太子湾公园: '西湖区南山路5-1号',
  杭州花港观鱼: '西湖区杨公堤',
  杭州苏堤: '西湖区苏堤',
  杭州白堤: '西湖区白堤',
  杭州曲院风荷: '西湖区北山路',
  杭州平湖秋月: '西湖区白堤西端',
  杭州柳浪闻莺: '西湖区南山路',
  杭州南屏晚钟: '西湖区南山路',
  杭州双峰插云: '西湖区灵隐路',
  杭州吴山天风: '上城区吴山路',
  杭州涌金公园: '上城区涌金路',
  杭州钱王祠: '上城区钱王祠路',
  杭州鼓楼: '上城区中山南路200号',
  杭州河坊街: '上城区河坊街',
  杭州南宋御街: '上城区中山中路',
  杭州湖滨银泰: '上城区延安路',
  杭州武林广场: '拱墅区武林广场',
  杭州运河广场: '拱墅区金华路',
  杭州小河直街: '拱墅区小河直街',
  杭州桥西直街: '拱墅区桥西直街',
  杭州拱宸桥: '拱墅区桥弄街',
  杭州西溪湿地东区: '西湖区天目山路518号',
  杭州西溪湿地西区: '西湖区文二西路',
  杭州湘湖: '萧山区湘湖路',
  杭州极地海洋世界: '萧山区湘湖路777号',
  杭州跨湖桥遗址博物馆: '萧山区湘湖路978号',
  杭州奥体中心: '滨江区奥体街',
  杭州滨江公园: '滨江区闻涛路',
  杭州梦想小镇: '余杭区仓前街道',
  杭州未来科技城: '余杭区文一西路',
  杭州临平新城: '临平区迎宾路',
  杭州九堡大桥: '江干区九堡',
  杭州钱江新城: '江干区富春路',
  杭州城市阳台: '江干区富春路',
  杭州大剧院: '江干区新业路39号',
  杭州国际会议中心: '江干区富春路',
  杭州奥体博览城: '滨江区江南大道',
  杭州白马湖国际会展中心: '滨江区长江南路',
  杭州之江文化中心: '西湖区江涵路300号',
  杭州文学馆: '西湖区江涵路300号之江文化中心',
  杭州西湖音乐喷泉: '西湖区湖滨',
  杭州西湖游船: '西湖区西湖',
  杭州西湖三潭印月: '西湖区西湖',
  杭州西湖湖心亭: '西湖区西湖',
  杭州西湖阮公墩: '西湖区西湖',
  杭州西湖杨公堤: '西湖区杨公堤',
  杭州西湖苏堤春晓: '西湖区苏堤',
  杭州西湖断桥残雪: '西湖区白堤',
  杭州西湖雷峰夕照: '西湖区雷峰塔',
  杭州西湖南屏晚钟: '西湖区南屏山',
  杭州西湖曲院风荷: '西湖区北山路',
  杭州西湖花港观鱼: '西湖区杨公堤',
  杭州西湖柳浪闻莺: '西湖区南山路',
  杭州西湖双峰插云: '西湖区灵隐路',
  杭州西湖平湖秋月: '西湖区白堤西端',
  杭州西湖吴山天风: '上城区吴山路',
  杭州运河文化广场: '拱墅区金华路',
  杭州运河夜游: '拱墅区运河',
  杭州运河游船: '拱墅区运河',
  杭州西溪湿地摇橹船: '西湖区西溪湿地',
  杭州西溪湿地龙舟赛: '西湖区西溪湿地',
  杭州西溪湿地植物园: '西湖区西溪湿地',
  杭州西溪湿地博物馆: '西湖区西溪湿地',
  杭州湘湖游船: '萧山区湘湖',
  杭州湘湖音乐喷泉: '萧山区湘湖',
  杭州极地海洋世界海豚表演: '萧山区湘湖路',
  杭州极地海洋世界白鲸表演: '萧山区湘湖路',
  杭州奥体中心体育场: '滨江区江南大道',
  杭州奥体中心游泳馆: '滨江区江南大道',
  杭州奥体中心网球中心: '滨江区江南大道',
  杭州梦想小镇创业大街: '余杭区文一西路',
  杭州未来科技城梦想小镇: '余杭区文一西路',
  杭州未来科技城学术交流中心: '余杭区文一西路',
  杭州未来科技城海创园: '余杭区文一西路',
  杭州未来科技城人才公园: '余杭区文一西路',
  杭州临平新城体育公园: '临平区',
  杭州临平新城文化艺术中心: '临平区',
  杭州临平新城市民广场: '临平区',
  杭州九堡大桥公园: '江干区九堡大桥',
  杭州钱江新城灯光秀: '江干区钱江新城',
  杭州城市阳台灯光秀: '江干区城市阳台',
  杭州大剧院歌剧厅: '江干区新业路',
  杭州大剧院音乐厅: '江干区新业路',
  杭州国际会议中心大剧场: '江干区新业路',
  杭州奥体博览城网球中心: '滨江区江南大道',
  杭州奥体博览城游泳馆: '滨江区江南大道',
  杭州白马湖国际会展中心展览厅: '滨江区长江南路',
  杭州之江文化中心图书馆: '西湖区之江路',
  杭州之江文化中心博物馆: '西湖区之江路',
  杭州之江文化中心美术馆: '西湖区之江路',
  杭州之江文化中心科技馆: '西湖区之江路',
  杭州文学馆展览厅: '西湖区',
  杭州文学馆阅读室: '西湖区',
  上海自然博物馆: '静安区北京西路510号',
  上海天文馆: '浦东新区南汇新城环湖北三路388号',
  上海儿童博物馆: '长宁区宋园路61号',
  上海地铁博物馆: '闵行区吴中路1799-7号',
  上海海洋水族馆: '浦东新区陆家嘴环路1388号',
  上海海昌海洋公园: '浦东新区银飞路166号',
  上海野生动物园: '浦东新区南六公路178号',
  上海欢乐谷: '松江区林湖路888号',
  上海迪士尼乐园: '浦东新区川沙新镇黄赵路310号',
  上海汽车博物馆: '嘉定区安亭博园路7565号',
  东方明珠塔: '浦东新区世纪大道1号',
  上海中心大厦: '浦东新区陆家嘴环路1000号',
  徐家汇书院: '徐汇区漕溪北路158号',
  世纪公园: '浦东新区锦绣路1001号',
  共青森林公园: '杨浦区军工路2000号',
  辰山植物园: '松江区辰花公路3888号',
  徐汇滨江滑板公园: '徐汇区龙腾大道',
  长风海洋世界: '普陀区大渡河路451号',
  上海植物园: '徐汇区龙吴路1111号',
  上海昆虫博物馆: '徐汇区枫林路300号',
  上海消防博物馆: '长宁区中山西路229号',
  上海科技馆分馆: '静安区北京西路510号',
  上海少年儿童图书馆: '长宁区延安西路1538号',
  世界技能博物馆: '杨浦区黄兴路221号',
  上海图书馆: '徐汇区淮海中路1555号',
  上海美术馆: '浦东新区上南路205号',
  上海大剧院: '黄浦区人民大道300号',
  上海音乐厅: '黄浦区延安东路523号',
  上海马戏城: '静安区共和新路2266号',
  上海儿童艺术剧场: '黄浦区苗江路800号',
  上海东方艺术中心: '浦东新区丁香路425号',
  上海梅赛德斯奔驰文化中心: '浦东新区世博大道1200号',
  上海八万人体育场: '徐汇区漕溪北路1111号',
  上海体育馆: '徐汇区漕溪北路1111号',
  上海源深体育中心: '浦东新区源深路655号',
  上海浦东游泳馆: '浦东新区浦东南路3669号',
  上海静安体育中心: '静安区汶水路116号',
  上海长风公园: '普陀区大渡河路189号',
  上海中山公园: '长宁区长宁路780号',
  上海人民公园: '黄浦区南京西路231号',
  上海外滩: '黄浦区中山东一路',
  上海陆家嘴: '浦东新区陆家嘴',
  上海南京东路步行街: '黄浦区南京东路',
  上海淮海中路: '黄浦区淮海中路',
  上海徐家汇商圈: '徐汇区徐家汇',
  上海静安寺: '静安区静安寺',
  上海城隍庙: '黄浦区方浜中路249号',
  上海豫园: '黄浦区豫园路100号',
  上海古猗园: '嘉定区南翔镇',
  上海大观园: '青浦区金商公路701号',
  上海朱家角古镇: '青浦区朱家角镇',
  上海枫泾古镇: '金山区枫泾镇',
  上海七宝古镇: '闵行区七宝镇',
  上海田子坊: '黄浦区泰康路210弄',
  上海新天地: '黄浦区太仓路181弄',
  上海科技馆主馆: '浦东新区世纪大道2000号',
  上海东方明珠太空舱: '浦东新区世纪大道1号',
  上海东方明珠悬空观光廊: '浦东新区世纪大道1号',
  上海中心大厦观光厅: '浦东新区陆家嘴环路1000号',
  上海金茂大厦观光厅: '浦东新区世纪大道88号',
  上海环球金融中心观光厅: '浦东新区世纪大道100号',
  上海长风海洋世界: '普陀区大渡河路451号',
  上海野生动物园车行区: '浦东新区南六公路178号',
  上海野生动物园步行区: '浦东新区南六公路178号',
  上海海昌海洋公园虎鲸馆: '浦东新区银飞路166号',
  上海海昌海洋公园北极熊馆: '浦东新区银飞路166号',
  上海迪士尼乐园城堡: '浦东新区川沙新镇黄赵路310号',
  上海迪士尼乐园明日世界: '浦东新区川沙新镇黄赵路310号',
  上海迪士尼乐园梦幻世界: '浦东新区川沙新镇黄赵路310号',
  上海迪士尼乐园宝藏湾: '浦东新区川沙新镇黄赵路310号',
  上海迪士尼乐园奇想花园: '浦东新区川沙新镇黄赵路310号',
  上海迪士尼乐园探险岛: '浦东新区川沙新镇黄赵路310号',
  上海迪士尼乐园皮克斯玩具总动员: '浦东新区川沙新镇黄赵路310号',
  上海乐高乐园: '金山区',
  上海欢乐谷谷木游龙: '松江区林湖路888号',
  上海欢乐谷玛雅海滩水公园: '松江区林湖路888号',
  上海辰山植物园温室: '松江区辰花公路3888号',
  上海辰山植物园矿坑花园: '松江区辰花公路3888号',
  上海松江大学城: '松江区大学城',
  上海松江方塔园: '松江区中山东路',
  上海松江醉白池: '松江区人民南路',
  上海泰晤士小镇: '松江区三新北路',
  上海欢乐谷魔幻城堡: '松江区林湖路888号',
  上海世纪公园: '浦东新区锦绣路1001号',
  上海陆家嘴中心绿地: '浦东新区陆家嘴环路',
  上海滨江森林公园: '浦东新区高桥镇',
  上海南汇嘴观海公园: '浦东新区南汇新城',
  上海滴水湖: '浦东新区南汇新城',
  上海临港新城: '浦东新区南汇新城',
  上海海洋大学: '浦东新区沪城环路',
  上海上海大学: '宝山区上大路',
  上海同济大学: '杨浦区四平路',
  上海复旦大学: '杨浦区邯郸路',
  上海交通大学: '徐汇区华山路',
  上海华东师范大学: '闵行区东川路',
  上海华东理工大学: '徐汇区梅陇路',
  上海上海师范大学: '徐汇区桂林路',
  上海上海理工大学: '杨浦区军工路',
  上海东华大学: '松江区人民北路',
  上海上海工程技术大学: '松江区龙腾路',
  '宝安区图书馆（总馆）': '宝安区宝兴路1号',
  宝安区城市规划展览馆: '宝安区宝兴路1号（图书馆同栋）',
  '宝安1990文化馆（区文化馆总馆）': '宝安区新湾一路',
  宝安博物馆: '宝安区新湾一路',
  宝安美术馆: '宝安区新湾一路',
  '宝安区青少年宫（滨海）': '宝安区新安街道海滨文化公园内',
  '湾区书城（深圳书城湾区城）': '宝安区宝兴路滨海文化公园',
  茅洲河展示馆: '宝安区燕罗街道燕罗湿地公园旁',
  西湾红树林科普馆: '宝安区西乡金湾大道西湾公园二期',
  福海安全生产警示教育中心: '宝安区福海街道桥和路300号二层',
  福永街道安全警示教育基地: '宝安区福永街道立新湖南门停车场旁',
  宝安图书馆西乡街道分馆: '宝安区前进二路197号桃源居对面',
  新安街道分馆: '宝安区新安街道兴东片区',
  新安中洲分馆: '宝安区中洲中央城邦社区',
  翻身社区阅读中心: '宝安区翻身片区',
  宝民社区阅读中心: '宝安区宝民一路',
  大仟里未来书屋: '宝安区西乡大仟里商场内',
  '宝读书房·旭书店': '宝安区西乡碧海湾片区',
  沙井街道图书馆分馆: '宝安区沙井街道市民广场内',
  松岗街道图书馆分馆: '宝安区松岗文化艺术中心内',
  石岩街道图书馆分馆: '宝安区石岩文化艺术中心',
  福永街道图书馆分馆: '宝安区福永怀德南路福永文化中心',
  燕罗街道图书馆分馆: '宝安区燕罗街道党群服务中心',
  航城街道图书馆分馆: '宝安区航城街道文化中心',
  新桥街道图书馆分馆: '宝安区新桥清平古墟旁',
  '滨海文化公园（欢乐港湾）': '宝安区宝兴路8号',
  '宝安公园（醒狮乐园）': '宝安区上川路493号东门',
  新安公园: '宝安区新安街道公园路',
  西湾公园: '宝安区西乡金湾大道沿线',
  蚝乡湖公园: '宝安区沙井北环路与宝安大道交汇处',
  '立新湖公园（立新湖儿童乐园）': '宝安区福永街道立新湖环湖',
  凤凰山人才林公园: '宝安区福永凤凰山南麓',
  五指耙体育主题公园: '宝安区松岗大田洋六路',
  铁仔山公园: '宝安区西乡片区',
  福海河公园: '宝安区福海街道会展片区',
  钓鱼嘴原木亲子乐园: '宝安区大渡口区大滨路沿江',
  沙井市民广场: '宝安区沙井中心路',
  新桥市民广场: '宝安区沙井中心路29号',
  燕罗湿地公园: '宝安区燕罗街道茅洲河沿岸',
  航城公园: '宝安区航城街道',
  石岩湿地公园: '宝安区石岩河沿岸',
  松岗公园: '宝安区松岗街道',
  桥头公园: '宝安区新桥街道清平古墟旁',
  清平古墟影视小镇: '宝安区新桥街道新颜路',
  王大中丞祠: '宝安区西乡老城区',
  西乡北帝古庙: '宝安区西乡步行街',
  沙井蚝文化博物馆: '宝安区沙井街道蚝乡湖片区',
  福永凤凰古村: '宝安区福永凤凰山脚下',
  '松岗琥珀博物馆（公益展厅）': '宝安区松岗街道琥珀产业园',
  燕罗红色文化纪念馆: '宝安区燕罗街道',
  上合孝德园: '宝安区新安上合社区',
  珠海博物馆: '香洲区海虹路88号',
  珠海市图书馆: '香洲区梅华街道迎宾北路3061号',
  珠海市文化馆: '香洲区兰埔路164号',
  古元美术馆: '香洲区梅华东路388号',
  珠海大剧院: '香洲区情侣路野狸岛海韵城',
  香山文化艺术中心: '香洲区建民路868号',
  珠海规划展览馆: '香洲区海虹路88号',
  国家方志馆粤港澳大湾区分馆: '香洲区',
  珠海市青少年妇女儿童活动中心: '香洲区',
  珠海市工人文化宫: '香洲区',
  圆明新园: '香洲区兰埔路',
  梅溪牌坊: '香洲区前山镇梅溪村',
  珠海国际会展中心: '香洲区湾仔南湾南路',
  华发商都: '香洲区珠海大道8号',
  珠海海滨公园: '香洲区海滨南路',
  金湾区图书馆: '金湾区三灶镇西城社区金河东路530号',
  金湾区文化馆: '金湾区三灶镇',
  金湾区博物馆: '金湾区三灶镇鱼月村',
  金湾艺术中心: '金湾区',
  汤臣倍健透明工厂: '金湾区三灶镇星汉路19号',
  珠海航展馆: '金湾区机场路航展馆',
  珠海海泉湾度假区: '金湾区平沙镇海泉湾路',
  金湾体育中心: '金湾区三灶镇',
  三灶镇文化中心: '金湾区三灶镇',
  金海岸文化艺术中心: '金湾区金海岸大道',
  斗门区图书馆: '斗门区江湾中路2号',
  斗门区博物馆: '斗门区井岸镇',
  斗门区文化馆: '斗门区井岸镇',
  斗门旧街: '斗门区斗门镇',
  金台寺: '斗门区乾务镇黄杨山',
  御温泉: '斗门区斗门镇',
  斗门体育中心: '斗门区井岸镇',
  井岸镇文化中心: '斗门区井岸镇',
  黄杨山: '斗门区乾务镇',
  斗门非遗展示馆: '斗门区斗门镇',
  横琴文化艺术中心: '横琴新区琴朗路与琴政路交叉口东南角',
  珠海长隆海洋王国: '香洲区横琴镇环岛路长隆大道1号',
  珠海长隆飞船乐园: '香洲区环岛东路与长隆大道交叉口西南1500米',
  珠海长隆横琴剧院: '香洲区环岛路富祥海湾长隆度假区内',
  横琴国际网球中心: '横琴新区横琴大道',
  星乐度露营小镇: '横琴新区环岛北路',
  横琴湿地公园: '横琴新区琴海北路',
  横琴花海长廊: '横琴新区环岛北路',
  横琴口岸: '横琴新区琴朗路',
  横琴金融岛: '横琴新区金融岛',
  珠海渔女景区: '香洲区情侣中路',
  野狸岛音乐广场: '香洲区野狸岛',
  珠海市体育中心: '香洲区红山路163号',
  香洲区文化馆: '香洲区',
  '龙岗国际艺术中心·D+数字艺术馆': '深圳市龙岗区坂田街道贝尔路4号',
  '龙岗国际艺术中心·国际演艺中心': '深圳市龙岗区坂田街道贝尔路4号',
  深圳市龙岗区怡利翡翠博物馆: '深圳市龙岗区龙岗街道龙西社区玉湖小区六栋一楼',
  深圳市龙岗区龙岭邮票博物馆: '深圳市龙岗区布吉街道龙岭路27号龙岭初级中学综合楼八楼',
  深圳市龙岗区万国珠宝汇矿物博物馆: '深圳市龙岗区横岗街道牛始铺路中和盛世A区2栋一楼',
  龙岗区图书馆少儿馆: '龙岗区中心城龙翔大道文化中心C座',
  深圳市百师园非物质文化遗产博物馆: '深圳市龙岗区平湖街道新木社区新木大道53号101',
  深圳市丁全匠作博物馆: '深圳市龙岗区平湖街道新木社区新木大道51号',
  深圳市梵亚艺术博物馆: '深圳市龙岗区吉华街道布龙路18号赛格ECO中心5栋12楼',
  '深圳市龙岗区东江潮红色文化博物馆（新生主馆）': '深圳市龙岗区龙岗街道新生路104号二楼',
  深圳市隐秀高尔夫博物馆: '深圳市龙岗区宝龙街道宝荷路158号隐秀山居酒店B1层C区东侧',
  '深圳·红立方': '广东省深圳市龙岗区龙翔大道8028号',
  茅洲河体育艺术中心: '深圳市光明区公明街道北环大道633号',
  深圳市坪山区文化馆: '深圳市坪山区梓平路43号',
  深圳市工业展览馆: '福田区福中三路市民中心B区黄塔2-10楼',
  南山区天后博物馆: '深圳市南山区赤湾六路9号',
  风华大剧院: '深圳市南山区蛇口公园路49号',
  '福田文体中心·戏剧主题馆': '福田区福强路3006号石厦二街交汇处',
  '福田文体中心·舞蹈主题馆': '深圳市福田区园岭五街2号',
  '福田文体中心·音乐主题馆': '福田区景田北路景田东一街2号',
  '福田文体中心·梦工场': '福田区景田路8号',
  '福田文体中心·非遗主题馆': '福田区福华路103号',
  大鹏新区博物馆: '1.大鹏所城场馆：大鹏新区大鹏街道鹏城社区大鹏所城赖府巷10号；2.东江纵队司令部旧址：广东省深圳市大鹏新区葵涌街道土洋社区中心巷16号',
  金龟自然书房分馆: '广东省深圳市坪山区石井街道金龟社区金地西区7号',
  坪山儿童公园分馆: '广东省深圳市坪山区碧岭街道沙湖社区同裕路和黄竹坑路的坪山儿童公园内（靠近坪山儿童公园北门）',
  '坪山图书馆·客家特藏馆': '广东省深圳市坪山区东胜街66号（文武帝宫内）',
  深圳红木家具博物馆: '广东省深圳市龙华区裕新路286号',
  深圳望野博物馆: '深圳市龙华区龙华文化广场三楼',
  深圳市龙华区美联红木艺术博物馆: '广东省深圳市龙华区高尔夫大道348号',
  深圳市艺之卉百年时尚博物馆: '广东省深圳市龙华区大浪服装基地艺之卉创意产业园',
  中国文化名人大营救纪念馆: '广东省深圳市龙华区民治办事处白龙路与民塘路交汇处（白石龙村口）',
  龙岗文化中心音乐厅: '深圳市龙岗区龙翔大道8308号龙岗文化中心A区四楼',
  龙岗文化中心大剧院: '深圳市龙岗区龙翔大道8308号龙岗文化中心A区二楼',
  深圳市龙岗区文化馆: '深圳市龙岗区龙翔大道8308号文化中心B区',
  世纪琥珀博物馆: '广东省深圳市宝安区松瑞路松岗琥珀交易市场3楼3r036号',
  华润大厦艺术中心美术馆: '深圳市南山区粤海街道汀泽一路',
  南头古城博物馆: '深圳市南山区深南大道12036号',
  龙华图书馆: '广东省深圳市龙华区福城街道观澜大道137号',
  蛇口海上世界文化艺术中心: '深圳市南山区蛇口望海路1187号',
  深圳南山文体中心剧院聚橙剧院: '深圳市南山区南山大道2106-3号',
  依波钟表文化博物馆: '深圳市光明区公明街道金安路依波大厦',
  惜物博物馆: '光明区光明街道光侨大道3125号电建洺悦鹏著花园5栋2单元文化活动室',
  光明区少年儿童图书馆: '深圳市光明区公明街道振明路9号',
  深汕西文体中心: '深圳市深汕特别合作区鹅埠街道大德路与创文路交汇处西南',
  '深圳（宝安）劳务工博物馆': '广东省深圳市宝安区石岩街道上屋居委永和路6号',
  至美术馆: '深圳市宝安区沙井街道后亭松安路全至科技创新园',
  深圳市坪山区美术馆: '深圳市坪山区坪山街道汇德路4号',
  深圳市坪山区图书馆: '广东省深圳市坪山区坪山街道汇德路8号',
  深圳市坪山区东江纵队纪念馆: '广东省深圳市坪山区东纵路230-1号',
  深圳市福田区图书馆: '深圳市福田区景田路70号图书馆大厦',
  光明国际马术中心: '光明区光明街道光灿路光明国际马术中心',
  罗湖体育馆: '罗湖区罗沙公路经二路48号',
  罗湖体育休闲公园: '深圳市罗湖区东湖二路',
  罗湖网球中心: '罗湖区罗沙公路经二路48号',
  横岗文体中心: '深圳市龙岗区横岗街道华乐社区红棉一路66号横岗文体中心',
  宝龙文体中心: '龙岗区宝龙大道景园公寓西侧约170米（宝龙文体中心）',
  深圳布吉文体中心: '龙岗区政清路与东西干道交叉口西南80米',
  深圳市青少年足球训练基地: '深圳市光明区公明街道李松蓢社区金蓢路与屋园路交叉口东南',
  光明区红花山体育中心: '深圳市光明区公明街道公明社区兴发路35号',
  '北京大学附属中学深圳学校(集团)黄埔学校(小学部)': '广东省深圳市福田区莲花街道民田路218号(正门进校)',
  民治体育公园: '广东省深圳市龙华区民治街道民治大道和民康路交汇口东南角',
  葵涌中学体育场: '大鹏新区葵涌街道葵新社区葵坪路8号',
  南澳中学体育场: '大鹏新区南澳街道教育路小区37号',
  南澳中心小学体育场: '大鹏新区南澳街道人民路37号',
  人大附中深圳学校高中部体育场: '大鹏新区溪涌社区溪坪南路80号',
  葵涌第二小学体育场: '大鹏新区葵涌街道葵兴西路30号',
  溪涌小学体育场: '大鹏新区葵涌街道溪涌社区深葵路1032号',
  葵涌中心小学体育场: '大鹏新区葵涌街道三溪社区三溪西路29号',
  大鹏第二小学体育场: '大鹏新区大鹏街道鹏城社区银滩路7号',
  深圳市龙岗区体育中心: '深圳市龙岗区龙城街道国际大学园路12号',
  沙头角体育馆: '深圳市盐田区金融路与海涛路交叉口沙头角体育馆(实验幼儿园对面)',
  盐田区游泳馆: '广东省深圳市盐田区沙头角街道海涛路27号盐田区游泳馆',
  盐田区体育发展服务中心网球场: '广东省深圳市盐田区海山街道海山路90号；梧桐路2002号',
  九龙山体育公园: '广东省深圳市龙华区福城街道观光路与观兴东路交界处',
  冰纷万象滑雪场: '深圳市深南大道9072号万象天地',
  锡才体育公园: '深圳市南山区西站前路19号',
  大鹏新区葵涌中心小学: '大鹏新区葵涌街道三溪社区三溪西路29号',
  景鹏小学: '广东省深圳市福田区莲花街道景田南二街8号',
  南海足球公园: '深圳市南山区南头街道南海大道',
  荔香公园网球场: '深圳市南山区南头街道清风路荔香公园内',
  桃源群众篮球网球体育公园: '深圳市南山区桃源街道龙珠三路',
  大沙河公园体育中心: '深圳市南山区桃源街道龙辉社区北环大道8228号',
  蛇口体育中心: '深圳市南山区公园路45号（四海公园旁）',
  深圳湾体育训练基地: '深圳市南山区中心路与科苑路交叉路口附近',
  深圳中山公园棒球场: '深圳市南山区南山大道217号',
  简上体育综合体: '深圳市龙华区民治街道355号（地铁4号线上塘站C出口）',
  '综合训练馆（室内网球馆）': '深圳市宝安区宝安大道与罗田路交汇处',
  宝安游泳场馆: '深圳市宝安区新安街道裕安一路2121号',
  宝安体育场: '深圳市宝安区新安街道裕安一路3021号',
  宝安体育馆: '深圳市宝安区新安街道新湖路2112号',
  深圳市坪山区坪山体育中心体育馆: '坪山区马峦街道体育一路2号',
  香蜜体育中心: '深圳市福田区侨香路与泽田路交界处（香蜜公园西北部区域）',
  黄木岗网球中心: '深圳市福田区笋岗西路3072号（市二医院西行200米）',
  莲花体育中心: '深圳市福田区景田南四街7号（华强职校西侧）',
  福田体育公园: '深圳市福田区沙头街道福强路3030号福田体育公园',
  福田区景田网球中心: '福田区景田北街',
  福田海滨生态体育公园: '深圳市福田区沙头街道白石路5号',
  北京老爷车博物馆: '北京市怀柔区杨宋镇凤翔一园19号',
  北京李大钊故居: '北京市西城区文华胡同24号',
  北京励志堂科举匾额博物馆: '北京市朝阳区高碑店乡高碑店村东街1366号',
  历代帝王庙: '北京市西城区阜成门内大街131号',
  中国法院博物馆: '北京市东城区正义路4号',
  北京韩美林艺术馆: '北京市通州区梨园镇九棵树东路68号',
  延庆博物馆: '北京市延庆区妫水北街24号',
  北京西瓜博物馆: '北京市大兴区庞各庄镇幸福路1号（庞各庄镇政府院内）',
  中国人民大学博物馆: '北京市海淀区中关村大街59号中国人民大学校内',
  北京空竹博物馆: '北京市西城区广内小星胡同9号',
  北京市怀柔区博物馆: '北京市怀柔区府前街9号院12号',
  北京怀柔喇叭沟门满族民俗博物馆: '北京市怀柔区喇叭沟门满族乡喇叭沟门村2号',
  民航博物馆: '北京市朝阳区首都机场辅路200号',
  中国传媒大学传媒博物馆: '北京市朝阳区定福庄东街1号 中国传媒大学49号楼',
  西藏文化博物馆: '北京市朝阳区北四环东路131号',
  和苑博物馆: '北京市朝阳区霄云路18号A10',
  中国海关博物馆: '北京市东城区建国门内大街2号',
  北京御仙都皇家菜博物馆: '北京市海淀区西四环北路117号',
  北京市平谷区博物馆: '北京市平谷区顺平路与洳河交叉口平谷区特色文化体育展示中心5层',
  北京英杰硬石艺术博物馆: '北京市朝阳区东直门外大街26号',
  北京税务博物馆: '北京市朝阳区北四环东路临1号',
  中国华侨历史博物馆: '北京市东城区北新桥三条甲一号',
  中国人民大学家书博物馆: '北京市海淀区中关村大街59号中国人民大学院内',
  北京文旺阁木作博物馆: '通州区台湖镇东下营村南开发区147号',
  延庆区地质博物馆: '北京市延庆区延庆镇妫水北街72号',
  北京市姜杰钢琴手风琴博物馆: '北京市海淀区羊坊店街道茂林居4号楼东侧二层',
  首都粮食博物馆: '北京市东城区永定门外三元街17号大磨坊文创园区内',
  香山革命纪念馆: '北京市海淀区红枫路1号院1号楼',
  北京荣唐连环画博物馆: '北京市朝阳区豆各庄一号易心堂文创园内14幢2层',
  北京二锅头酒博物馆: '北京市怀柔区红星路1号，北京市东城区前门大街99号',
  北京市大兴区月季博物馆: '北京市大兴区魏善庄镇',
  北京皇城御窑金砖博物馆: '北京市通州区漷县镇觅永路1号院',
  北京燕京八绝博物馆: '北京市石景山区模式口大街20号',
  北京东璧堂中医药博物馆: '北京市房山区兴阎街11号院1号楼',
  北京市和光书院博物馆: '北京市朝阳区望京南湖北二街20号院',
  北京大戚收音机电影机博物馆: '北京市通州区大兴庄村北',
  北京菜百黄金珠宝博物馆: '北京市西城区广安门内大街306号',
  北京市石景山区博物馆: '北京市石景山区苹果园南路10号院1号楼;石景山区文化中心4-6层',
  颐和园博物馆: '北京市海淀区新建宫门路19号',
  中国共产党早期北京革命活动纪念馆: '北京市东城区五四大街29号',
  北京京华茶叶博物馆: '北京市西城区马连道14号京华茶业大世界四层',
  北京文景珍本期刊博物馆: '北京市房山区阎村镇兴阎街5号院1号楼2层',
  国家典籍博物馆: '北京市海淀区中关村南大街33号',
  北京航空航天模型博物馆: '北京市延庆区延庆镇百康路1号',
  北京法和律师博物馆: '北京市东城区建国门内大街9号北京国际饭店3层',
  北京龙顺成京作非遗博物馆: '北京市东城区永外大街64号',
  中国共产党历史展览馆: '北京市朝阳区北辰东路9号',
  北京市顺义区博物馆: '北京市顺义区石园大街10号',
  北京金漆镶嵌艺术博物馆: '北京市朝阳区小红门乡红寺村40号（南院）9幢-10幢',
  北京云汇网球木拍博物馆: '北京市朝阳区水碓子北里11号',
  北京自来水博物馆: '北京市东城区东直门外香河园街3号',
  中国佛教图书文物馆: '北京市西城区法源寺前街7号',
  北京劲飞京作红木文化博物馆: '北京市昌平区沙河镇七里渠南村319号',
  西黄寺博物馆: '北京市朝阳区黄寺大街11号',
  北京中药炮制技术博物馆: '北京市大兴区生物医药基地永旺路25号',
  '何扬·吴茜现代绘画馆': '北京市朝阳区金盏乡长店村123号（原1128号）',
  平西抗日战争纪念馆: '北京市房山区十渡平西抗日烈士陵园管理处',
  北京中梦足球博物馆: '北京市朝阳区燕保百湾家园小区6#配套首层、2#架空廊',
  北京九鼎灶文化博物馆: '北京市顺义区林河南大街9号院24号楼2至3层',
  北京宣南文化博物馆管理处: '北京市西城区长椿街9号',
  '北京文博交流馆（北京市智化寺管理处）': '北京市东城区禄米仓胡同5号',
  北京莱恩堡葡萄酒文化博物馆: '北京市房山区长阳镇稻田第一村长周路西侧北京莱恩堡国际酒庄城堡主楼',
  北京市房山世界地质公园博物馆: '北京市房山区长沟镇六甲房村',
  北京百年世界老电话博物馆: '北京市通州区宋庄镇疃里村集体产业就业会所物业3号楼一层108室，201室，301室，401室',
  中国电信博物馆: '北京市海淀区学院路42号',
  北京市海淀区中关村村史馆: '北京市海淀区双榆树西里18号',
  中国化工博物馆: '北京市海淀区北四环西路62号中国化工集团大厦三层',
  北京服装学院民族服饰博物馆: '北京市朝阳区樱花东路甲2号北京服装学院综合楼A座3层',
  北京工艺美术博物馆: '北京市朝阳区天辰东路12号',
  中央美术学院美术馆: '北京市朝阳区花家地南街8号',
  北京警察博物馆: '北京市东城区东交民巷36号',
  '北京考古遗址博物馆（金中都水关遗址）': '北京市丰台区右安门外大街玉林小区甲40号',
  十三陵水库展览馆: '北京市昌平区十三陵水库',
  国家大剧院台湖舞美艺术博物馆: '北京市通州区台湖镇台湖西路6号',
  北京天桥印象博物馆: '北京市西城区天桥南大街7号',
  北京牛栏山二锅头酒文化博物馆: '北京市顺义区鑫牛南路12号楼-1至2层01',
  石景山区石刻博物馆: '北京市石景山区模式口大街80号',
  北京公交馆: '北京市丰台区莲花池西里29号北京公交调度指挥中心西配楼',
  北京天元中医药博物馆: '北京市朝阳区广渠路1号42幢平房42-1室',
  视障文化博物馆: '北京市西城区太平街甲6号富力摩根中心B座',
  中国木偶艺术剧院博物馆: '北京市朝阳区安华西里甲1号',
  景泰蓝艺术博物馆: '北京市东城区永外安乐林路10号',
  北京六必居博物馆: '北京市西城区粮食店街3号院内六必居博物馆',
  北京福履布鞋文化博物馆: '北京市西城区大栅栏街34号',
  慈善寺古香道文化陈列馆: '北京市石景山区五里坨天泰山',
  科学家博物馆: '北京市朝阳区北辰东路3号院',
  全聚德博物馆: '北京市西城区前门西大街14号',
  对外经贸博物馆: '北京市朝阳区惠新东街10号逸夫科研楼一层',
  瀛海文史馆: '北京市大兴区瀛海镇瀛安街45号院',
  宋庆龄故居管理中心: '北京市西城区后海北沿46号',
  万寿寺博物馆: '北京市海淀区苏州街万寿寺内',
  北京舞蹈学院舞蹈博物馆: '北京市海淀区万寿寺路一号',
  北京市大兴区天宫院乡情文史馆: '北京市大兴区新源大街天宫院社区内一层、二层、三层',
  '北京外国语大学校史馆、世界语言艺术博物馆': '北京市海淀区西三环北路19号北京外国语大学西校区国内大厦1号楼至4号楼一层',
  北京宝翠宫翡翠博物馆: '北京市西城区德胜门东滨河路3号白孔雀艺术世界',
  京东方历史展览馆: '北京市朝阳区酒仙桥路10号，B4一层',
  水峪村生态博物馆: '北京市房山区南窖乡水峪村',
  北京神州连环画博物馆: '北京市西城区天桥南大街1号天桥艺术大厦B座509',
  北京果脯博物馆: '北京市怀柔区庙城镇郑重村北637号正南方向80米',
  延庆石刻博物馆: '北京市延庆区湖北西路7号',
  北京市大兴区榆垡镇乡情文史馆: '北京市大兴区榆垡镇党群服务中心',
  北京遇见艺术博物馆: '北京市朝阳区798艺术区陶瓷一街E02-1楼',
  北京神农农耕文化博物馆: '北京市门头沟区琉璃渠大街2号金隅琉璃文化创意产业园15号楼',
  清华大学科学博物馆: '北京市海淀区清华大学蒙民伟人文楼B2层',
  徐悲鸿纪念馆: '北京市西城区新街口北大街5号',
  炎黄艺术馆: '北京市朝阳区亚运村慧忠路9号',
  明十三陵博物馆: '北京市昌平区十三陵特区定陵',
  梅兰芳纪念馆: '北京市西城区护国寺街9号',
  雍和宫藏传佛教艺术博物馆: '北京市东城区雍和宫大街12号',
  '北京考古遗址博物馆（北京大葆台遗址博物馆）': '北京市丰台区花乡郭公庄世界公园东南',
  北京大学赛克勒考古与艺术博物馆: '北京市海淀区颐和园路5号北京大学',
  北京市白塔寺管理处: '北京市西城区阜成门内大街171号',
  李大钊烈士陵园: '北京市海淀区香山万安里1号',
  詹天佑纪念馆: '北京市八达岭特区',
  北京焦庄户地道战遗址纪念馆: '北京市顺义区龙湾屯镇焦庄户村纪念馆路38号',
  中央民族大学民族博物馆: '北京市海淀区中关村南大街27号',
  北京航空航天博物馆: '北京市海淀区学院路37号北京航空航天大学院内',
  北京房山云居寺石经博物馆: '北京市房山区大石窝镇水头村南北京房山云居寺文物管理处',
  密云区博物馆: '北京市密云区西门外大街2号',
  昌平区博物馆: '北京市昌平区府学路10号',
  通州区博物馆: '北京市通州区西大街9号',
  山戎文化陈列馆: '北京市延庆区张山营镇玉皇庙村东',
  '长辛店二·七纪念馆': '北京市丰台区长辛店花园南里甲15号',
  上宅文化陈列馆: '北京市平谷区金海湖镇上宅村南100米',
  郭守敬纪念馆: '北京市西城区德胜门西大街甲60号',
  中国第四纪冰川遗迹陈列馆: '北京市石景山区模式口大街28号',
  周口店北京人遗址博物馆: '北京市房山区周口店大街13号',
  中国印刷博物馆: '北京市大兴区黄村镇兴华北路25号',
  '中国工艺美术馆（中国非物质文化遗产馆）': '北京市朝阳区湖景东路16号',
  北京红楼文化艺术博物馆: '北京市西城区南菜园西街12号',
  '北京中轴线遗产保护中心（正阳门）': '北京市东城区前门大街北端',
  '北京明城墙遗址公园（东南城角角楼）': '北京市东城区东大街东便门外东南城角楼',
  '北京大觉寺与团城管理处（团城演武厅）': '海淀区香山南路红旗村甲一号',
  文天祥祠: '北京市东城区府学胡同63号',
  永定河文化博物馆: '北京市门头沟区门头沟路8号',
  北京市钟鼓楼文物保管所: '北京市东城区钟楼湾胡同临字9号',
  北京法海寺博物馆: '北京市石景山区模式口',
  中国国家画院美术馆: '北京市海淀区西三环北路54号',
  圆明园展览馆: '北京市海淀区清华西路28号长春园西洋楼遗址区内',
  '北京大觉寺与团城管理处（大觉寺）': '北京市海淀区苏家坨镇大觉寺路9号',
  北京中华民族博物院: '北京市朝阳区民族园路1号',
  观复博物馆: '北京市朝阳区大山子张万坟金南路18号',
  古陶文明博物馆: '北京市西城区右安门内西街12号大观园北门',
  中国钱币博物馆: '北京市西城区西交民巷17号',
  文化和旅游部恭王府博物馆: '北京市西城区前海西街17号',
  中国现代文学馆: '北京市朝阳区文学馆路45号',
  慈悲庵: '北京市西城区太平街19号',
  中国蜜蜂博物馆: '北京市海淀区香山植物园卧佛寺西侧中国农业科学院蜜蜂研究所院内',
  平北抗日战争纪念馆: '北京市延庆区张山营镇韩郝庄村',
  卢沟桥历史博物馆: '北京市丰台区卢沟桥城南街77号',
  曹雪芹纪念馆: '北京市海淀区正白旗39号院',
  冀热察挺进军司令部旧址陈列馆: '北京市门头沟区斋堂镇马栏村107号',
  北京中医药大学中医药博物馆: '北京市朝阳区北三环东路11号',
  香山双清别墅: '北京市海淀区香山买卖街香山公园内',
  老甲艺术馆: '北京市昌平区东小口镇霍营',
  北京戏曲博物馆: '北京市西城区虎坊路3号',
  保利艺术博物馆: '北京市东城区朝阳门北大街1号新保利大厦云楼9层',
  北京中国紫檀博物馆: '北京市朝阳区建国路23号',
  北京南海子麋鹿苑博物馆: '北京市大兴南海子麋鹿苑',
  中华世纪坛艺术馆: '北京市海淀区复兴路甲9号中华世纪坛',
  北京王府井古人类文化遗址博物馆: '北京市东城区东方广场东方新天地W1P3号',
  北京金台艺术馆: '北京市朝阳区朝阳公园西一号门内',
  '中国铁道博物馆（东郊展馆）': '北京市朝阳区南春路4号院',
  中国铁道博物馆正阳门展馆: '前门大街东侧原京奉铁路正阳门东车站旧址（北京市东城区前门大街甲2号）',
  北京皇城艺术馆: '北京市东城区菖蒲河沿9号',
  北京御生堂中医药博物馆: '北京市昌平区北七家镇王府街1号王府公寓2-35',
  居庸关长城博物馆: '北京市昌平区南口镇居庸关长城',
  北京人民艺术剧院戏剧博物馆: '北京市东城区王府井大街22号',
  '北京市海淀区三山五园文化艺术中心（北京市海淀区博物...': '北京市海淀区海淀公园路6号',
  毛主席纪念堂: '北京市东城区前门东大街11号',
  民族文化宫博物馆: '北京市西城区复兴门内大街49号',
  中国农业博物馆: '北京市朝阳区东三环北路16号',
  中国航天博物馆: '北京市丰台区万源路1号',
  地坛体育中心: '北京市东城区安定门外大街168号',
  天坛体育中心: '北京市东城区天坛东路13号',
  东单体育中心: '北京市东城区崇文门内大街108号',
  地坛体育馆: '北京市东城区安定门外大街116号',
  广安体育中心: '北京市西城区登莱胡同26号',
  广安游泳网球馆: '北京市西城区登莱胡同26号',
  月坛体育馆: '北京市西城区月坛南街甲1号',
  月坛综合训练馆: '北京市西城区月坛南街1号院8号楼',
  月坛体育场: '北京市西城区月坛南街甲1号',
  西城区武术和棋类运动管理中心: '北京市西城区德胜门外大街教场口街9号院',
  朝阳体育馆: '北京市朝阳区姚家园路10号',
  郡王府体育中心: '北京市朝阳区朝阳公园南路21号',
  海淀温泉体育中心: '北京市海淀区白家疃东路9号院',
  北京市网球运动管理中心: '北京市丰台区光彩路1号',
  丰台体育中心: '北京市丰台区西四环南路55号',
  门头沟区体育馆: '北京市门头沟区新桥大街32号',
  良乡训练基地: '北京市房山区体育场路4号',
  房山区体育场: '北京市房山区燕房路1号',
  良乡体育中心: '北京市房山区政通路26号院',
  潞城全民健身中心: '北京市通州区尚明南街交汇处西南口',
  顺义体育中心: '北京市顺义区光明南街二号',
  顺义城南体育中心: '北京市顺义区石原街道顺康路5号',
  昌平体育馆: '北京市昌平区南环西路1号',
  昌平区体育运动场: '北京市昌平区西环路31号',
  回龙观体育文化公园: '北京市昌平区回龙观西大街与文华西路交叉口东南',
  天通苑体育馆: '北京市昌平区立水桥东二路天通中苑75号',
  大兴区体育中心: '北京市大兴区兴华大街二段15号',
  平谷区体育中心: '北京市平谷区鲁各庄东路60号',
  怀柔区体育中心: '北京市怀柔区青春路湖光小区31号',
  密云区体育中心: '北京市密云区河南寨镇河东路8号',
  延庆区体育中心: '北京市延庆区延庆镇湖北东路118号',
  北京经济技术开发区体育中心: '北京经济技术开发区天宝中街1号',
  燕山体育馆: '北京市房山区燕房路52号',
  北京市东城区图书馆: '北京市东城区交道口东大街85号',
  北京市东城区图书馆东总布分馆: '北京市东城区东总布胡同38号院',
  北京市东城区图书馆角楼分馆: '北京市东城区龙潭东路9号',
  北京市东城区图书馆王府井书店分馆: '北京市东城区王府井大街218号',
  北京市东城区图书馆阅想书店分馆: '北京市东城区青年湖南街13号',
  北京市东城区图书馆语文书店分馆: '北京市东城区朝阳门内南小街51号',
  北京市东城区图书馆北京银行陶然支行分馆: '北京市东城区安乐林中街2号院18号楼101',
  '北京市西城区图书馆（北址）': '西城区后广平胡同26号',
  '北京市西城区图书馆（南址）': '西城区教子胡同8号',
  '朝阳区图书馆（劲松馆）': '朝阳区广渠路66号院3号楼',
  '朝阳区图书馆（小庄馆）': '朝阳区朝外金台里17号',
  '海淀区图书馆（北馆）': '北京市海淀区温泉路47号海淀北部文化中心A座',
  '丰台区图书馆
（北大地馆）': '丰台区西四环南路64号',
  '丰台区图书馆
（大红门馆）': '丰台区南苑路7号',
  石景山区图书馆少儿馆: '石景山区古城南路11号（石景山区图书馆少儿馆）',
  '房山区图书馆（新）': '房山区长阳镇昊天北大街8号A馆',
  '房山区图书馆城关分馆（老馆）': '房山区城关东大街25号',
  燕山图书馆: '北京市房山区燕山岗南路东一巷2号  燕山文化活动中心5/6层',
  北京市通州区图书馆: '北京市通州区通胡大街76-1号',
  顺义区图书馆: '顺义区石园大街10号 顺义区文化中心院内',
  大兴区图书馆: '大兴区黄村西大街11号',
  昌平区图书馆: '昌平区府学路10号',
  平谷区图书馆: '平谷区府前西街1号',
  怀柔区图书馆: '怀柔区富乐大街8号',
  密云区图书馆: '北京市密云区四眼井胡同6号',
  延庆区图书馆: '妫水北街16号',
  北京市东城区文化馆: '北京市东城区交道口东大街111号',
  北京市西城区文化馆: '西城区西直门内大街147号',
  海淀区文化馆: '北京市海淀区中关村大街28-1号，海淀文化艺术大厦A座四层、五层、七层、八层',
  '海淀区文化馆（北馆）': '北京市海淀区温泉路47号海淀北部文化中心B座',
  丰台区文化馆: '丰台区西四环南路64号',
  石景山区文化馆: '石景山区苹果园南路10号院1号楼',
  门头沟区文化馆: '门头沟区新桥大街12号（影剧院北侧）',
  '房山区文化馆（新）': '房山区长阳镇昊天北大街8号B馆',
  '房山区文化馆城关分馆（老馆）': '房山区城关东大街12号',
  燕山文化馆: '房山区迎风街道岗南路东一巷2号（燕山文化活动中心）',
  通州区文化馆: '通州区通胡大街76号院',
  顺义区文化馆: '顺义区石园大街10号 顺义区文化中心院内',
  大兴区文化馆: '大兴区黄村西大街11号',
  昌平区文化馆: '昌平区政府街22号',
  平谷区文化馆: '平谷区府前西街1号',
  怀柔区文化馆: '怀柔区南大街20号',
  密云区文化馆: '密云区新南路101号',
  延庆区文化馆: '妫水北街20号',
  和平里街道综合文化中心: '东城区民旺南胡同甲18号',
  安定门街道文体中心: '东城区郎家胡同11号',
  交道口街道综合文化中心: '东城区交道口土儿胡同10号楼',
  景山街道综合文化中心: '东城区美术馆后街40号',
  东华门街道综合文化中心: '东城区东华门大街62号',
  东华门街道图书馆: '东城区北河沿大街143号',
  建国门街道综合文化中心: '东城区朝阳门南小街14号',
  朝阳门街道综合文化中心: '东城区大方家胡同38号',
  东四街道市民活动中心: '东城区朝阳门北小街14号',
  北新桥街道综合文化中心: '东城区南颂年胡同3号',
  东直门街道综合文化中心: '东城区东直门东中街40号元嘉国际公寓2层',
  前门街道市民活动中心: '东城区西打磨厂街62号',
  崇文门外街道综合文化中心: '东城区新怡家园甲3-3，新怡商务楼B座二层三层',
  龙潭街道综合文化中心: '东城区夕照寺街16号院华城5号写字楼5层',
  龙潭街道图书馆: '东城区幸福17号楼2层',
  体育馆路街道综合文化中心: '东城区东四块玉南街甲11号',
  东花市街道综合文化中心: '东城区东花市街道花市枣苑小区8号楼1层',
  东花市街道图书馆: '东城区东花市北里西区13号楼地下一层',
  天坛街道市民活动中心: '永定门内东大街中里1号',
  永外街道综合文化中心: '东城区景泰西里东区4号楼底商文化活动中心',
  天桥街道: '1：西城区天桥小区北里3号楼地下一层
2：太平街8号院朱雀门30号楼地下一层
3：禄长街头条甲二号地下一层',
  牛街街道: '牛街东里一区18号楼牛街街道党群活动中心',
  什刹海街道: '西城区什刹海街道刘海胡同11号',
  新街口街道: '西城区西直门内大街235号',
  月坛街道: '1：三里河二区B区9-10
2：月坛南街19号院4号楼平房',
  白纸坊街道: '1：白纸坊东街31号院内三层（光源里市民中心）；
2：枣林前街16号（坊间书阁）',
  德胜街道: '1：德外大街教场口9号院戊9号
2：新明胡同甲1号',
  广外街道: '车站西街2号院17号楼二层',
  展览路街道: '1：中共西城区委党校展览路街道工委分校（北京市西城区南礼士路与南营房路交叉口东南40米）
2：北营房中街33号（街道图书馆）',
  广内街道: '1：广义街4号
2：下斜街1号（街道图书馆）',
  椿树街道: '1：北京市西城区椿树园小区7号楼甲1号(椿树街道百姓文化之家）
2：北京市西城区骡马市大街9号（椿树书苑）',
  陶然亭街道: '1：菜市口大街甲2号院9号楼（陶然书苑）
2：粉房琉璃街160-9（街道图书馆）
3南华里小区5号楼地下二层（文体中心）',
  金融街街道: '1闹市口南街26号
2太平桥大街107号地下二层',
  西长安街街道: '西城区东斜街53号',
  大栅栏街道: '1西城区大栅栏街道杨梅竹斜街甲125号
2西城区樱桃斜街5号',
  香河园街道: '朝阳区光熙家园小区2号和3号楼之间下沉广场',
  奥运村街道: '朝阳区清林路世茂奥临一号院七号楼三层文化中心',
  建外街道: '朝阳区建国路88号，建外街道文化教育活动中心',
  亚运村街道: '朝阳区安慧里一区24号',
  和平街街道: '朝阳区和平西苑甲10号地下2层',
  三里屯街道: '朝阳区幸福二村38号楼四单元',
  望京街道: '望京西园四区425号楼',
  朝外街道: '朝阳区吉庆里一号楼朝外街道市民活动中心',
  大屯街道: '朝阳区大屯里社区金泉家园1号楼',
  首都机场街道: '朝阳区首都机场街道市民活动中心（体育场西门南侧50米院内A座）',
  垡头街道: '朝阳区垡头街道翠城102楼二层',
  六里屯街道: '延静里2号楼六里屯文化中心',
  东湖街道: '朝阳区东湖街道利泽西园一区107楼',
  团结湖街道: '团结湖中路北一条6号楼',
  安贞街道: '安华里二区11号楼',
  潘家园街道: '松榆西里甲26号楼、松榆里3号楼（图书馆）、松榆里公园内（文体中心）',
  双井街道: '广渠门外大街富力城D区24号楼',
  小关街道: '惠新西街16号蓝珏苑地下一层',
  酒仙桥街道: '朝阳区酒仙桥街道驼房营西里邻甲8号',
  劲松街道: '劲松八区甲813楼3层劲松文体协会',
  八里庄街道: '朝阳区十里堡甲3号院4号楼',
  左家庄街道: '左家庄东里9号楼2层',
  麦子店街道: '朝阳区枣营北里26号楼',
  太阳宫地区: '芍药居北里2013、219楼',
  黑庄户地区: '朝阳区黑庄户乡政府第二办公区党群活动中心（黑庄户乡大鲁店二村村东口）',
  十八里店地区: '十八里店地区市民活动中心分中心
（周庄嘉园东里C区周家庄村党群活动中心）
十八里店地区图书馆（老君堂路308号）',
  将台地区: '朝阳区驼房营路甲1号将台地区市民活动中心',
  豆各庄地区: '豆各庄乡天达路朝丰家园8号院4号楼',
  王四营地区: '朝阳区王四营村4号',
  常营地区: '朝阳区三间房东路甲九号',
  金盏地区: '朝阳区金盏乡金盏嘉园B区西南角裙楼金盏地区市民活动中心',
  三间房地区: '朝阳区三间房地区康惠园2号院9号楼',
  东坝地区: '朝阳区东坝乡东坝家园A区综合楼五层',
  来广营地区: '朝阳区水岸庄园1010号商业楼4层',
  崔各庄地区: '朝阳区崔各庄乡京旺家园六区底商',
  高碑店地区: '朝阳区康家园小区1号楼北侧',
  管庄地区: '朝阳区新天地5号院12号楼管庄地区市民服务中心',
  孙河地区: '朝阳区孙河乡康营家园D区文化服务中心',
  小红门地区: '朝阳区鸿博家园二期D区5号楼',
  平房地区: '朝阳区雅成一里甲2号',
  东风地区: '朝阳区星火西路17号东风地区市民活动中心东风驿',
  南磨房地区: '紫南家园208楼',
  呼家楼街道: '呼家楼北里小区西门东110米殷金凤工作室',
  万寿路街道文化活动中心: '万寿路乙14号楼',
  羊坊店地区文体活动中心: '海淀区吴家场路31号',
  羊坊店街道文化中心: '海淀区木樨地茂林居6号',
  甘家口街道市民活动中心: '车公庄西路花园村甲10号',
  '八里庄街道党群文化中心（慧美党群服务中心）': '海淀区阜成路97号',
  八里庄街道图书馆: '海淀区八里庄街道恩济西街8号楼底商',
  紫竹院街道综合文化服务中心: '厂洼东二街',
  '北下关街道综合文化活动中心（评剧团站）': '海淀区高梁桥斜街30号院（交大南门）',
  '北下关街道综合文化活动中心（农科院站）': '海淀区中关村南大街12号院东区58幢综合楼半地下一层',
  '北太平庄街道综合文化活动中心（蓟门书院）': '海淀区蓟门里小区东三楼北侧',
  海淀街道市民活动中心: '海淀区南路22号',
  海淀区海淀街道图书分馆: '海淀区小南庄31号',
  中关村街道综合文化活动中心: '科学院南路中关村958楼3层',
  中关村街道图书馆: '中关村黄庄小区818楼6层',
  学院路街道综合文化中心: '海淀区志新西路志新村小区西门内',
  清河街道综合文化服务中心: '海淀区清河安宁庄东路8号',
  青龙桥街道综合文化活动中心: '海淀区黑山扈红山口8号A座三层',
  香山街道综合文化中心: '香山一棵松2号',
  香山街道图书馆: '海淀区煤厂街香山第一社区服务站旁图书馆',
  西三旗街道文化活动中心: '海淀区永泰中路50号',
  马连洼街道综合文化活动中心: '天秀路5号古月园',
  马连洼街道图书馆: '马连洼北路菊花盛苑小白楼101室
目前馆址即将搬迁，新馆位于如缘居南里1号楼底商（马连洼街道西北旺三街如园）将于2025年9月22日开放。',
  花园路街道市民活动中心: '花园北路46号',
  田村路街道文化活动中心: '海淀区西四环北路137号院西木学堂',
  上地街道文化活动中心: '上地宏达大厦A座',
  上地街道图书馆: '上地宏达大厦C座2层图书馆',
  曙光街道市民活动中心: '海淀区板井路59号',
  曙光街道图书馆: '蓝晴路世纪城下沉广场012号',
  燕园街道文化服务中心: '清溪书屋路1号（诚和敬养老驿站）',
  清华园街道综合文化活动中心: '双清苑1号楼308',
  永定路街道综合文化中心: '海淀区金沟河路5号院805楼',
  东升镇南部文化活动中心: '海淀区八家嘉苑小区19号楼地下一层',
  东升镇东部文化活动中心: '海淀区宝盛东路兴华产业楼南楼',
  东升镇北部活动中心: '海淀区文龙家园9号楼',
  海淀镇综合文化活动中心: '厢黄旗东路柳浪家园南里15号楼三层',
  nan: '柳浪家园中街底商B4',
  四季青镇综合文化活动中心: '海淀区杏石口路65号益园文创基地C区6号楼',
  西北旺镇市民活动中心: '海淀区唐家岭北环路2号院14号楼',
  温泉镇市民活动中心: '海淀区温泉镇颐阳山水居西区10号楼对面',
  苏家坨镇综合文化活动中心: '海淀区苏家坨镇北安河路39号院',
  '上庄镇市民活动中心（北京市海淀区上庄镇党群活动中心）': '上庄镇李家坟村',
  南苑街道综合文化中心: '丰台区西红门南一街206号院公园懿府小区22号楼3层活动室',
  丰台区青塔街道综合文化中心: '丰台区青塔街心公园南侧',
  大红门街道综合文化中心: '丰台区大红门南里12号(大红门南地铁站C东南口步行80米)',
  北宫镇综合文化活动中心: '丰台区杜家坎南路8号',
  东高地街道综合文化中心: '丰台区东高地斜街5号',
  和义街道文化中心: '丰台区南苑北里一区六号楼瑞荣大厦负一层',
  丰台区太平桥街道市民活动中心: '太平桥小区8号楼甲1号',
  丰台区新村街道综合文化中心: '恒丰路1号院刘孟家园社区南门',
  长辛店街道综合文化中心: '长辛店大街128号',
  丰台街道综合文化中心: '丰台区新华街一里桥南社区服务站二层',
  花乡街道综合文化中心: '丰台区鑫润路1号院15号楼
丰台区鑫润路2号院5号楼
丰台区高立庄北路10号院燕保康润家园11号楼',
  '石榴庄街道综合文化中心（原大红门街道综合文化中心）': '丰台区金桥东街9号院1号楼',
  '石榴庄街道综合文化中心（原东铁匠营街道综合文化活动中心）': '丰台区宋庄路顺八条8号院一区3号楼下沉广场',
  西罗园街道综合文化中心: '丰台区西罗园北路12号院',
  右安门街道综合文化中心: '丰台区右安门外玉林里37号楼；丰台区右安门外大街糖果幼儿园二层多功能演艺厅',
  丰台区王佐镇文化服务中心: '丰台区王佐镇南宫迎宾路京石高速出口200米路西',
  云岗街道综合文化中心: '丰台区云岗北区西里11号',
  宛平街道文体活动中心: '丰台区晓月苑五里1号楼地下二层
丰台区宛平镇晓月中路24号
丰台区城内街与城南街交叉口东300米',
  '看丹街道综合文化中心（党群服务中心）': '丰台区韩庄子二里26号楼',
  马家堡街道文化活动中心: '马家堡街道政务服务中心东侧',
  卢沟桥街道市民活动中心: '北京市丰台区新丰路甲一号卢沟桥乡史规划馆',
  方庄街道综合文化中心: '芳群园一区7号楼二层',
  玉泉营街道市民活动中心: '丰台区玉泉营街道纪家庙产业园西200米',
  东铁匠营街道综合文化中心: '东木樨园11号楼北侧、顺八条东口北阳晨光大厦底商',
  成寿寺街道综合文化中心: '合雅金苑小区内西北侧',
  苹果园街道: '苹果园二区西门西侧30米',
  老山街道: '东区：上庄大街18号郎园Park 新芽生长书店
西区：老山东里小区东侧入口
图书分馆：老山东里49栋北侧东里北居委会一层',
  鲁谷街道: '南部：重聚园北门底商
中部：鲁谷南路18号院1号（图书分馆）
北部：鲁谷双锦园16号楼底商',
  八宝山街道: '北区：玉泉西里一区2号楼
南区：玉泉西里一区26号楼',
  八角街道: '活动中心：八角南路社区2号楼南侧平房
图书分馆：八角街道景颂街社区服务站2层',
  古城街道: '燕堤西街7号院1号楼三、四层',
  金顶街街道: '金顶街五区甲9号',
  广宁街道: '高井路东侧12-16号（电厂路小学前）',
  五里坨街道: '图书分馆：五里坨西街9号院2号楼
活动中心：黑陈路炮厂小区8号西山机械厂社区居委会',
  大峪街道: '门头沟区大峪街道龙山家园四区（西南角）',
  城子街道: '门头沟区龙门新区B9-14号',
  东辛房街道: '门头沟区石园南路与紫金路交叉口西100米',
  大台街道: '北京市门头沟区大台街道文化中心（大台火车站后50米',
  王平镇: '门头沟区王平镇西大街18号',
  龙泉镇: '门头沟区高家园新区1号院5号楼3层',
  潭柘寺镇: '门头沟区潭柘新区1号院1号楼',
  军庄镇: '门头沟区三温路20号（门头沟区军庄镇惠通新苑8号楼底商二层）',
  雁翅镇: '门头沟雁翅镇付家台村车站南20米',
  斋堂镇: '门头沟区斋堂镇斋堂大街45号',
  清水镇: '门头沟区清水镇上清水村河西60号',
  妙峰山镇: '北京市门头沟区妙峰山镇妙峰山路与桃园村路交叉路口北桃园村东口二层红楼',
  永定镇: '北京市门头沟区永定镇惠康嘉园六区北侧',
  城关街道: '城关街道西大街23号',
  拱辰街道: '房山区拱辰街道白杨东路辅路拱辰街道综合文化中心（瑞雪春堂社区对面）',
  西潞街道: '房山区苏庄大街北京工商大学附属小学（原良乡中心小学）西门南侧楼西潞街道党群服务中心内（西潞街道综合文化中心）',
  长阳镇: '房山区长阳镇保合庄村成人教育学校',
  琉璃河镇: '房山区琉璃河镇洄城村中区76号（琉璃河镇政府西侧100米）',
  窦店镇1: '窦店镇窦店村中心幼儿园旁',
  窦店镇2: '窦店镇大高舍村委会向西100米',
  韩村河镇: '房山区韩村河镇韩村河十字路口北100米路东侧',
  阎村镇: '北京市房山区阎村镇紫园路12号',
  良乡镇: '房山区良乡镇官道十字路口东南角（官融小区底商）',
  青龙湖镇: '房山区青龙湖镇豆各庄村东南（原青龙湖镇中心幼儿园）',
  周口店镇: '周口店镇政府西50米',
  石楼镇: '石楼镇坨头村村委会后院3区84号',
  长沟镇: '长沟镇政府南300米路西党群文化活动中心（原长沟地税所，注：综合文化活动中心暂时与镇党群文化活动中心合用）',
  大石窝镇: '大石窝镇派出所后院',
  张坊镇: '张坊镇政府东南100米',
  河北镇: '河北镇河南村',
  佛子庄乡: '房山区佛子庄乡佛子庄村           （成人学校内）',
  十渡镇: '房山区十渡大街167号院',
  蒲洼乡: '蒲洼村村委会（原幼儿园）',
  霞云岭乡: '北京市房山区霞云岭乡社区成人职业学校院内',
  史家营乡: '房山区史家营乡人民政府大院前100米',
  南窖乡: '南窖乡党群服务中心',
  大安山乡: '大安山乡大安山村大安山乡人民政府西侧文化广场',
  新镇街道: '房山区新镇原新街文体中心',
  东风街道: '北京市房山区燕山双泉东路5号燕和园小区9号楼东侧',
  迎风街道: '北京市房山区燕山迎风街道迎风四巷一号',
  向阳街道: '燕山地区北庄路6号',
  星城街道: '北京市房山区星城三里工商银行后',
  潞城镇综合文化中心: '潞城镇武兴路7号',
  九棵树街道综合文化中心: '云景东路1号贵友大厦后身',
  西集镇文体活动中心: '通州区西集镇郎东村北(苏望路与任郎路交叉路口西南约90米)',
  临河里街道综合文化中心: '通州区金隅7090小区净水园14号楼下沉广场',
  台湖镇文体活动中心: '通州区台湖镇铺大路25号',
  北苑街道文体活动中心: '通州区中山大街56号院2号楼三层',
  北苑街道文化活动中心: '通州区新城南街83号住宅小区（金禧花园）
东区沿街商业西侧一门',
  于家务回族乡综合文化中心: '通州区于家务回族乡西里社区26号',
  潞邑街道综合文化中心: '通州区潞邑街道东都国际10号楼底商',
  潞源街道综合文化中心: '通州区兆善大街与清风路交叉口东南角50米',
  宋庄镇综合文化中心: '通州区宋庄镇老政府路南50米（通州区宋庄镇成人技术学校内）',
  中仓街道综合文化中心: '通州区玉带河大街428号',
  马驹桥镇综合文化中心: '市国土资源局通州分局第四国土资源管理所东侧',
  通运街道综合文化中心: '通州区潞通大街191号',
  玉桥街道综合文化中心: '通州区运河大街葛布店东里小区13号楼临1',
  杨庄街道综合文化中心: '通州区京铁潞园7号楼二层',
  张家湾镇综合文化中心: '通州张家湾镇三间房村成人学校',
  永顺镇综合文化中心: '通州区永顺镇潞苑北里四区8号楼3层4层',
  新华街道综合文化中心: '通州区月亮河综治中心北侧居委会2层',
  漷县书院: '通州区漷县镇漷兴一街社保所院内',
  永乐店镇综合文化中心: '通州区孔东路东张各庄村西',
  文景街道综合文化中心: '北京市通州区永丰里小区D区12号楼',
  梨园镇文化活动中心: '通州区怡乐中路与怡乐南街交叉口南120米',
  后沙峪镇: '顺义区后沙峪镇裕安路九重汇六层',
  北务镇: '北务镇商业街23号',
  赵全营镇: '2-1：赵全营镇昌金路段牛板路101号（政府对面）；
2-2北郎中科技文化活动中心（展厅）',
  张镇: '2-1张镇林秀西路1号院一区15号楼底商（综合文化中心、张镇图书馆），
2-2张镇聂庄村温馨家园（综合文化中心）',
  高丽营镇: '2-1文化营村委会东侧；
2-2文化营村委会对面',
  马坡镇: '2-1马坡镇庙卷村花园路2号；
2-2马坡镇原十佳运动衣厂外（白各庄村口南50米）',
  仁和镇: '2-1仁和镇文体广场；
2-2东方太阳城会所二层',
  天竺镇: '2-1天竺印象馆
2-2黄花梨艺术馆',
  牛栏山镇: '香堤中路2号院1号楼',
  北石槽镇: '北石槽镇北武路1号（政务服务中心院内）',
  南彩镇: '2-1河北村河北村东路1号（村委会）；
2-2后郝家疃村',
  木林镇: '2-1木林镇大韩庄村东路98号
2-2木林镇陈各庄村中街79号
2-3顺焦路36号（图书馆）',
  北小营镇: '北小营镇政府对面',
  大孙各庄镇: '大孙各庄镇大孙各庄村北新街甲1号',
  龙湾屯镇: '3-1焦庄户村焦庄街103号；
3-2焦庄户地道战遗址纪念馆；
3-3山里辛庄村中心街187号（图书馆）',
  李遂镇: '李遂村遂太路2号',
  南法信镇: '2-1顺捷大厦一层；
2-2焦各庄村西北胡同临甲8号',
  李桥镇: '4-1后桥村委会；
4-2王家场村；
4-3沿河村；
4-4张辛村',
  杨镇: '杨镇双阳南区居委会同址',
  空港街道: '三山新新家园4区1号楼',
  光明街道: '2-1滨河一区甲20号楼西侧；
2-2裕龙五区爱e空间13号楼玻璃房',
  旺泉街道: '澜西园四区6号楼',
  双丰街道: '2-1双丰街道香悦西区5号楼一层；
2-2双丰街道香悦西区12号楼1号底商',
  石园街道: '2-1石园大街12号一层西大厅
2-2石园东区16号楼北侧车棚',
  胜利街道: '胜利街道建新南区甲八号楼',
  清源街道: '大兴区圣和巷8号院2号楼地下一层、三层',
  林校路街道: '大兴区林校路街道义和庄南里一区12号楼',
  兴丰街道: '大兴区三合北巷2号院1号楼',
  观音寺街道: '大兴区双河南里社区甲15号楼地下空间',
  天宫院街道: '大兴区华佗路1号院11号楼西侧底商（综合文化中心）',
  高米店街道: '大兴区双高路与兴华大街交叉路口西南200米（党群服务中心）',
  荣华街道: '北京经济技术开发区天华南街3号院长新花园会所B1',
  博兴街道: '北京亦庄经济技术开发区凉水河二街亦城茗苑18-19号楼3层',
  黄村镇: '大兴区黄村镇安顺北路1号院11号楼（格林雅苑分中心）',
  西红门镇: '大兴区西红门镇宏福路兴海公园内',
  采育镇: '大兴区采育镇采华路10号',
  青云店镇: '大兴区青云店镇政府南侧200米',
  瀛海镇: '大兴区瀛海镇党群服务中心东楼一层、二层',
  长子营镇: '大兴区长子营镇郑二营路口西20米',
  旧宫镇: '大兴区旧宫镇紫郡府南区北侧（综合文化中心）',
  魏善庄镇: '大兴区魏善庄镇羊坊村200号泓文博雅艺术馆',
  礼贤镇: '大兴区礼贤镇龙头村（文化活动中心）',
  安定镇: '大兴区安定镇政府路东200米',
  北臧村镇: '大兴区北臧村镇新立村成人学校',
  庞各庄镇: '大兴区庞各庄镇民生路4号院2号楼（党群活动中心）',
  榆垡镇: '大兴区榆垡镇榆瑞路空港新苑11号院党群服务中心',
  亦庄镇: '大兴区亦庄镇贵园北路2号（宣传文体中心）',
  城北街道: '昌平区振兴路新悦家园南侧城北街道永安活动中心',
  马池口镇: '昌平区马池口镇奤夿屯新区北侧',
  南邵镇: '昌平区南邵镇人民政府东侧约30米（镇政府后院）',
  天通苑南街道: '昌平区天通苑四区29号楼',
  东小口镇: '昌平区东小口镇龙锦一街37号院悦府家园社区物业三层',
  北七家镇: '昌平区北七家镇天机街与天权路交叉路口往西南约150米',
  流村镇: '昌平区流村镇政府北侧文化中心',
  沙河镇: '昌平区沙河镇巩华家园东一村北侧底商2-3层',
  霍营街道: '北京市昌平区首开LONG街商业街南区S07栋3层、4层',
  十三陵镇: '昌平区泰胡路2号十三陵镇政府后院（有专属通道直达）',
  天通苑北街道: '天通苑北街道党群服务中心（昌平区-立水桥东一路天通中苑一区-西区）',
  崔村镇: '昌平区崔村镇西崔村1号崔村镇政府东院',
  阳坊镇: '昌平区阳坊镇中心街29号',
  延寿镇: '原昌平区黑山寨乡政府院内',
  小汤山镇: '前蔺沟村委会西侧',
  百善镇: '昌平区百善镇泥洼村村委会百钟路北50米',
  南口镇: '昌平区南口镇南雁路与G6京藏高速出口交叉口南150米老政府后院',
  回龙观街道: '昌平区回龙观街道昌平路410号',
  兴寿镇: '昌平区怀昌路兴寿镇半壁店凯德麓语1号院一区42号',
  城南街道: '昌平区北郝庄村西南北庄路211号北侧',
  龙泽园街道: '昌平区龙泽园街道龙禧二街龙禧苑北店嘉园社区活动站',
  史各庄街道: '昌平区农学院北路9号院一区2号楼',
  东高村镇: '平谷区东高村镇东高村育才西街45号',
  滨河街道: '1.平谷区中卫世纪城1号楼地下一层2.平谷区都丽豪廷1号楼1单元101',
  大华山镇: '大华山大街267号',
  大兴庄镇: '平谷区大兴庄镇白各庄村西路5号',
  黄松峪乡: '北京市平谷区黄松峪乡黄松峪乡村东街402号',
  金海湖镇: '金海湖镇禧瑞金海小区35号楼',
  刘家店镇: '刘家店镇银店大街1号',
  马昌营镇: '马昌营镇南定福东路201号院西马昌营镇文化服务中心（马昌营镇密三路与南定福庄路路西50米定福新村）',
  马坊镇: '北京市平谷区马坊镇金平北街2号',
  南独乐河镇: '平谷区南独乐河镇南山村石马子',
  平谷镇: '北京市平谷区乐园西小区8号',
  山东庄镇: '北京市平谷区山东庄镇山东庄村府前街9号',
  王辛庄镇: '王辛庄镇校园路20号',
  夏各庄镇: '夏各庄镇由山由谷六号院北侧50米',
  兴谷街道: '上纸寨中路7号院3号楼',
  熊儿寨乡: '熊儿寨乡熊儿寨东路14号/熊儿寨乡熊儿寨东路4号/熊儿寨乡政府后院',
  峪口镇: '峪口镇峪阳路18号',
  镇罗营镇: '镇罗营镇上营村南街68号',
  庙城镇综合文化中心: '北京市怀柔区庙城镇庙城村怀长路与庙城路交叉路口西南庙城镇庙城村临300号',
  雁栖镇综合文化中心: '北京市怀柔区雁栖大街17号',
  九渡河综合文化中心: '北京市怀柔区九渡河镇黄坎村西',
  琉璃庙镇综合文化中心: '北京市怀柔区琉璃庙镇琉璃庙村165号',
  宝山镇综合文化中心: '北京市怀柔区宝山镇转年村',
  长哨营满族乡综合文化中心: '北京市怀柔区长哨营满族乡长哨营村东政府北街',
  喇叭沟门满族乡综合文化中心: '北京市怀柔区喇叭沟门满族乡喇叭沟门村2号',
  怀柔镇综合文化中心: '北京市怀柔区迎宾南路9号',
  桥梓镇综合文化中心: '北京市怀柔区桥梓镇前桥梓村兴桥大街1号',
  北房镇综合文化中心: '北京市怀柔区北房镇幸福西街3号',
  杨宋镇综合文化中心: '北京市怀柔区和平路与安平路交叉口往东100米',
  怀北镇综合文化中心: '北京市怀柔区怀北镇消防基础建设队',
  渤海镇综合文化中心: '北京市怀柔区渤海镇沙峪村536号',
  河口镇综合文化中心: '北京市怀柔区汤河口镇东帽湾村村委会旁',
  龙山街道综合文化中心: '北京市怀柔区青春路27号',
  泉河街道综合文化中心: '北京市怀柔区青春路27号',
  密云区溪翁庄镇综合文化中心: '密云区溪翁庄镇文体中心',
  密云区北庄镇综合文化中心: '密云区北庄华盛路142号',
  密云区冯家峪镇综合文化中心: '灾毁待重建',
  密云区巨各庄镇综合文化中心: '密云区巨各庄镇政府院南',
  密云区穆家峪镇综合文化中心: '密云区穆家峪镇国华小学道西',
  密云区大城子镇综合文化中心: '密云区大城子镇大城子村西',
  密云区古北口镇综合文化中心: '密云区古北口镇古北口大街主街',
  密云区不老屯镇综合文化中心: '密云区不老屯镇不老屯村',
  密云区高岭镇综合文化中心: '密云区高岭镇高岭村政府路8号',
  密云区河南寨镇综合文化中心: '北京市密云区河南寨镇政府院内',
  密云区太师屯镇综合文化中心: '密云区葡萄园村永安大街143号',
  密云区东邵渠镇综合文化中心: '密云区东邵渠镇政府路南',
  密云区石城镇综合文化中心: '密云区石城镇文化服务中心',
  密云区新城子镇综合文化中心: '密云区新城子镇新城子村',
  密云区西田各庄镇综合文化中心: '密云区雁密路99号',
  密云区十里堡镇综合文化中心: '密云区西大桥路69号',
  密云区密云镇综合文化中心: '密云镇李各庄小区北侧',
  檀营地区综合文化中心: '北京市密云区国际生态城南区底商、密云区石桥西区12号楼东侧',
  密云区果园街道综合文化中心: '密云区新西路2号、密云区果园街道新北路30号院5层（大唐庄综合楼）、密云区西门外大街8号建设银行南侧幼儿防疫二层、密云区康居居委会二层图书馆',
  密云区鼓楼街道综合文化中心: '鼓楼街道沿湖小区2号楼南侧、密云区新北路沿湖北区9号楼南侧、鼓楼街道花园小区46号楼南侧、鼓楼街道阳光街385号院10号楼底商10-5和10-6',
  八达岭镇: '延庆区八达岭镇营城子村委会东侧100米',
  百泉街道: '延庆区百泉街道振兴北社区西门57号楼地下一层',
  井庄镇: '延庆区井庄镇政府后院',
  旧县镇文体中心: '延庆区旧县镇政府东100米',
  康庄镇: '延庆区康庄镇西官路北消防站西侧50米',
  刘斌堡乡: '刘斌堡乡政府南院',
  千家店镇: '延庆区千家店镇后沟村32号',
  儒林街道: '延庆区北街6号（儒林街道综合服务中心院内）',
  沈家营镇: '延庆区沈家营镇镇政府东侧',
  四海镇: '延庆区四海镇四海村北街东一区70号',
  香水园街道: '延庆区香水园街道香苑街5号',
  永宁镇: '北京市延庆区永宁镇幼儿园墻西',
  张山营镇: '延庆区张山营镇张山营村南',
  珍珠泉乡: '延庆区珍珠泉乡珍珠泉村村东（乡政府对面）',
  大庄科乡: '延庆区大庄科乡大庄科村',
  延庆镇文体中心: '延庆区妫水北街20号（区文化馆小剧场）',
  香营乡文体中心: '延庆区香营乡政府东院',
  大榆树镇: '延庆区大榆树镇府前街1号',
  '重庆中国三峡博物馆(重庆博物馆)': '渝中区人民路236号',
  '红岩革命纪念馆（重庆红岩革命历史博物馆）': '渝中区红岩村52号',
  '重庆歌乐山革命纪念馆（重庆红岩革命历史博物馆）': '沙坪坝区烈士墓政法三村63号',
  大足石刻博物馆: '大足区宝顶镇香山街2号',
  重庆大韩民国临时政府旧址陈列馆: '渝中区莲花池38号',
  '重庆特园民主党派历史陈列馆（中国民主党派历史陈列馆）': '渝中区嘉陵桥东村35号',
  重庆历史名人馆: '渝中区经纬大道333号康德国际2幢18层',
  重庆抗战戏剧博物馆: '渝中区中山一路181号',
  '重庆史迪威博物馆（史迪威研究中心）': '渝中区嘉陵新路63号',
  重庆体育博物馆: '渝中区两路口体育村34号跳伞塔旁',
  重庆典籍博物馆: '渝中区两路口长江1路11号（罗斯福图书馆旧址）',
  二厂记忆博物馆: '渝中区鹅岭正街1号',
  重庆嘉陵江索道博物馆: '两江新区嘉陵江索道北站房旧址',
  重庆自然资源科普馆: '两江新区天宫殿街道恒明路 1 号',
  重庆师范大学博物馆: '沙坪坝区大学城中路37号',
  重庆警察博物馆: '九龙坡区科园六路42号',
  重庆市规划展览馆: '南岸区弹子石广场南滨路131号',
  西南大学历史博物馆: '北碚区西南大学荟文楼西侧',
  中国西部科学院旧址陈列馆: '北碚区文星湾42号',
  重庆电信博物馆: '两江新区星光五路189号',
  重庆川剧博物馆: '两江新区人和金山大道2号',
  重庆白鹤梁水下博物馆: '涪陵区白鹤梁大道二段185号',
  重庆三峡移民纪念馆: '万州区南滨大道1469号',
  重庆市万州区博物馆: '万州区南滨大道1469号一楼',
  重庆市万州革命烈士陵园管理中心: '万州区红光村7社',
  重庆市万州良公祠民俗博物馆: '万州区长岭镇凉水村二组',
  '万县“九五”惨案纪念馆': '万州区兰池沟10号',
  重庆市万州区三峡石博物馆: '万州区南滨大道一支路2号A22栋',
  重庆市民族博物馆: '黔江区新华大道西段512号',
  万涛故居: '黔江区冯家街道办事处桂花路32号',
  黔江区博物馆: '黔江区城西街道河滨路北段29号',
  重庆市涪陵区博物馆: '涪陵区兴华中路72号',
  重庆市渝中区博物馆: '渝中区人民公园3号（二府衙19号、人民路117号、四新路19号、天官府8号）',
  '重庆“湖广填四川”移民博物馆（重庆湖广会馆）': '渝中区长滨路芭蕉园一号',
  王琦美术博物馆: '渝中区中山四路75号',
  重庆巴渝民间中医药博物馆: '渝中区李子坝正街90号',
  重庆市巴渝名匾文化艺术博物馆: '渝中区李子坝正街90号',
  重庆市渝中区友好飞虎队博物馆: '渝中区嘉陵新路62号',
  重庆市渝中区巴渝民风博物馆: '渝中区解放西路16号',
  重庆大轰炸遗址陈列馆: '渝中区解放碑磁器街较场口87号附4号',
  重庆金融历史博物馆: '渝中区新华路74号四川美丰银行旧址负1层—3层',
  渝中区古典戏法魔术博物馆: '渝中区鹅岭正街1号34幢、35幢',
  重庆市大渡口区博物馆: '大渡口区钢花路302号附5号',
  明玉珍睿陵陈列馆: '两江新区江北城街道中央商务公园内',
  重庆金融博物馆: '两江新区江北嘴重庆银行总部大楼北楼第3层（临街）—5层',
  重庆旁观者设计博物馆: '两江新区平和路5号',
  '重庆市沙坪坝博物馆（重庆市沙坪坝区巴蜀古代建筑博物馆）': '沙坪坝区陈家桥街道学城大道160号附1号',
  重庆郭沫若纪念馆: '沙坪坝区西永街道西科三路',
  重庆张治中纪念馆: '沙坪坝区土主街道三圣宫村',
  重庆冯玉祥纪念馆: '沙坪坝区陈家桥街道学城大道160号附3号',
  重庆抗战教育博物馆: '沙坪坝区磁器口重庆市二十八中内',
  重庆沙坪坝地质博物馆: '沙坪坝区覃家岗街道梨树湾临泉路5号',
  重庆市九龙坡区重庆巴人博物馆: '九龙坡区红狮大道6号',
  '刘伯承六店旧居纪念馆（刘伯承六店旧居管理中心）': '九龙坡区渝州路街道烟灯山公园内',
  重庆华岩佛教博物馆: '九龙坡区华岩村152号',
  重庆三耳火锅博物馆: '九龙坡区金凤镇海含路1号',
  重庆市九龙坡区黄桷坪钢琴博物馆: '九龙坡区杨家坪天鹅花园22号附22号',
  重庆市九龙坡区九龙沉香博物馆: '九龙坡区九滨路9号8号3层',
  重庆市九龙坡区建川博物馆: '九龙坡区谢家湾鹤皋村一号',
  重庆市九龙坡区周君记火锅调料历史文化博物馆: '九龙坡区九龙园区华龙大道 16号',
  重庆抗战遗址博物馆: '南岸区南山植物园路1号',
  南岸区博物馆: '南岸区文化艺术中心（茶园）D区',
  重庆市中医药博物馆: '南岸区南山路34号',
  重庆市南岸区德庄火锅博物馆: '南岸区长电路10号',
  重庆市北碚区博物馆: '北碚区云清路77号B座一楼',
  卢作孚纪念馆: '北碚区朝阳街道文星湾一巷1—33号',
  四世同堂纪念馆: '北碚区天生街道天生新村63号',
  梁实秋纪念馆: '北碚区天生街道梨园村18号',
  '抗战时期荣誉军人自治实验区陈列馆（重庆市北碚区博物馆分馆）': '北碚区澄江镇运河村',
  '晏阳初纪念馆（重庆市北碚区博物馆分馆）': '北碚区歇马街道桃园村26号',
  '国立复旦大学重庆旧址（抗战时期复旦大学校史纪念馆）': '北碚区东阳街道夏坝路79号',
  中共中央西南局缙云山办公地旧址陈列馆: '北碚区澄江镇缙云山杉木园内',
  张自忠烈士陵园: '北碚高速路口下道处双柏树516号',
  王朴烈士陵园: '北碚区桥亭村',
  北碚教育博物馆: '北碚区望月村43号（北碚区教师进修学院内）',
  重庆巴渝民俗博物馆: '两江新区双龙大道97号',
  重庆宝林博物馆: '两江新区金开大道龙展路99号',
  重庆市渝北区渝都古典照相机缝纫机博物馆: '两江新区龙兴镇迎龙大道19号“两江国际影视城”',
  重庆御临旅游纪念品博物馆: '两江新区龙兴镇两江国际影视城一期B6',
  重庆市巴南区博物馆: '巴南区龙洲湾公园北路18号巴南文化艺术中心6楼',
  重庆长江石文化艺术博物馆: '巴南区鱼洞新农街56号2单元1—1',
  重庆市巴南区江碧波艺术博物馆: '巴南区龙洲湾街道道角村21社',
  重庆市长寿区博物馆: '长寿区菩提街道桃兴三路5号',
  重庆市长寿区杨克明故居陈列馆: '长寿区云集镇青丰村二组',
  江津博物馆: '江津区圣泉街道圣泉路95号',
  聂荣臻元帅陈列馆: '江津区几江街道办事处鼎山大道386号',
  重庆市江津区陈独秀旧居陈列馆: '江津区几江街道石墙村8组96号',
  中等师范教育历史陈列馆: '江津区白沙镇陈家坡',
  陶行知先生纪念馆: '合川区草街办事处古圣村8社',
  钓鱼城古战场遗址博物馆: '合川区钓鱼城大道中段',
  重庆友军辣椒博物馆: '合川区龙市镇龙腾大道1号附—1号',
  重庆市合川区三江民俗博物馆: '合川区合阳办事处利川村',
  合川区楠山坊金丝楠木博物馆: '合川区文峰塔公园',
  '永川博物馆（陈子庄艺术陈列馆）': '永川区文昌路801号',
  重庆市永川堃航博物馆: '永川区昌州大道中段6号63幢',
  重庆市永川区蕴宝博物馆: '永川区文昌路801号',
  南川区博物馆: '南川区东街文旅小镇',
  重庆市南川区蝶语昆虫博物馆: '南川区南城街道三汇村（金佛山西大门）',
  綦江博物馆: '綦江区古南街道农场社区三社',
  重庆市綦江区红军长征纪念馆: '綦江区石壕镇交通路104号',
  饶国梁纪念馆: '大足区国梁镇云路街74号',
  重庆市大足区红岩重型汽车博物馆: '大足区双桥经开区车城大道39号市民文化中心',
  重庆大圆祥博物馆: '璧山区健龙镇龙江新石村5社',
  铜梁区博物馆: '铜梁区巴川街道龙门路169号',
  铜梁木匾博物馆: '铜梁区巴川街道迎宾路148号',
  重庆市铜梁区邱少云烈士纪念馆: '铜梁区巴川镇民主路64号',
  潼南区博物馆: '潼南区大佛街道涪江路360号',
  '杨闇公杨尚昆旧居陈列馆（重庆市潼南区杨尚昆故里管理处）': '潼南区大佛街道石院街159号（杨闇公旧居位于双江镇正街48号，杨尚昆旧居位于双江镇金龙社区长滩子）',
  荣昌陶博物馆: '荣昌区安富街道洗布潭村3组',
  张培爵纪念馆: '荣昌区昌元街道公园路158号',
  重庆市荣昌区万灵提琴博物馆: '荣昌区万灵镇沱湾街10号1幢',
  重庆市荣昌陶窑口博物馆: '荣昌区安富镇和平路151号',
  刘伯承同志纪念馆: '开州区汉丰街道盛山社区781号',
  重庆市开州博物馆: '开州区滨湖中路开州博物馆',
  重庆市开州区雨青博物馆: '开州区城区东部新区',
  重庆市梁平区博物馆: '梁平区行政中心1号楼（梁平区都梁广场下广场）',
  重庆市武隆博物馆: '武隆区芙蓉街道芙蓉中路81号',
  后坪坝苏维埃政府史迹展览馆: '武隆区后坪乡文凤村高峰槽6号',
  和平中学旧址陈列馆: '武隆区平桥镇和平路42号',
  川陕苏区城口纪念馆: '城口县葛城街道土城半月池2号',
  城口县红三十三军指挥部旧址群陈列馆: '城万旧址：城口县双河乡余坪村四社刘家院子。红三十三军旧址：城口县庙坝镇政府旁、城口县坪坝镇议学村。',
  丰都县博物馆: '丰都县名山街道景区路2号',
  垫江县博物馆: '三合湖湿地公园内',
  忠州博物馆: '忠县白公街道白公路28号',
  忠县石宝寨: '忠县石宝镇临江街94号',
  云阳县博物馆: '云阳县双江街道两江广场西侧',
  张桓侯庙博物馆: '云阳县盘龙镇龙安社区',
  云阳古建博物苑: '云阳县青龙街道',
  云阳县彭咏梧纪念馆: '云阳县红狮镇咏梧社区红七街',
  云阳县非物质文化遗产博物馆: '云阳县两江广场西侧（市民文化活动中心三楼文化馆）',
  奉节县夔州博物馆: '奉节县夔门街道诗城东路83号',
  奉节县白帝城博物馆: '奉节县夔门街道瞿塘峡社区白帝城·瞿塘峡风景区内',
  奉节县瞿塘关遗址博物馆: '奉节县夔门街道瞿塘峡社区白帝城·瞿塘峡风景区内',
  奉节县诗城博物馆: '奉节县诗城东路136号',
  巫山博物馆: '巫山县高唐街道平湖西路369号',
  巫山县李季达陈列馆: '巫山县龙门街道龙江社区',
  巫山县下庄人事迹陈列馆: '巫山县竹贤乡下庄村3组',
  巫山县长康博物馆: '巫山县巫峡镇白水村10社',
  巫溪县博物馆: '巫溪县柏杨街道文景路15号',
  石柱土家族自治县博物馆: '石柱县南宾街道城东社区干溪子路5号民族文化中心1楼',
  秀山土家族苗族自治县民族博物馆: '秀山土家族苗族自治县乌杨街道渝秀大道186号',
  刘邓大军挺进大西南司令部旧址陈列馆: '秀山土家族苗族自治县洪安镇边城居委会',
  酉阳土家族苗族自治县酉州博物馆: '酉阳县桃花源街道源泉新路2号',
  酉阳土家族苗族自治县赵世炎烈士纪念馆: '酉阳自治县龙潭镇赵庄大道133号',
  南腰界红三军司令部旧址陈列馆: '酉阳县南腰界镇南界村5组',
  彭水苗族土家族自治县博物馆: '彭水苗族土家族自治县汉葭街道民族路88号',
  九黎苗族历史文化博物馆: '彭水县靛水街道张家坝社区一组',
  重庆市万盛经济技术开发区博物馆: '万盛经开区西城大道414号',
  重庆市少年儿童图书馆: '重庆市两江新区鸳鸯街道龙景路3号2幢（园博园东门旁）',
  重庆市万州区图书馆: '重庆市万州区白岩路159号',
  重庆市黔江区图书馆: '重庆市黔江区舟白街道学府一路一号',
  重庆市涪陵区图书馆: '重庆市涪陵区崇义街道白鹤梁大道666号',
  重庆市渝中区图书馆: '重庆市渝中区中山三路32号文图大厦',
  重庆市大渡口区图书馆: '重庆市大渡口区松青路98号',
  重庆市江北区图书馆: '鸿恩寺馆:重庆市两江新区鸿恩二路鸿恩寺公园南门（3号门）内；金源路馆:重庆市两江新区金源路64号文化艺术中心内',
  重庆市沙坪坝区图书馆: '重庆市沙坪坝区渝碚路街道222号',
  重庆市九龙坡区图书馆: '重庆市九龙坡区杨家坪街道西郊支路19号',
  重庆市南岸区图书馆: '重庆市南岸区南城大道199号',
  重庆市北碚图书馆: '重庆市北碚区公园村26号',
  重庆市渝北区图书馆: '重庆市两江新区仙桃街道百果路55号',
  重庆市巴南区图书馆: '重庆市巴南区龙洲湾街道公园北路18号',
  重庆市长寿区图书馆: '重庆市长寿区菩提街道文苑大道6号',
  重庆市江津区图书馆: '重庆市江津区圣泉街道圣泉路57号',
  重庆市合川区图书馆: '重庆市合川区涪滨路1068号',
  重庆市南川区图书馆: '重庆市南川区西城街道办事处凤江北路3号',
  重庆市大足区图书馆: '重庆市大足区棠香街道龙景路121号附3号',
  重庆市双桥经开区图书馆: '重庆市大足区双路街道双龙西路23号附1号',
  重庆市万盛经济技术开发区图书馆: '重庆市万盛经济技术开发区滨江西路501号附2号',
  重庆市綦江区图书馆: '重庆市綦江区通惠街道登瀛大道6号',
  重庆市永川区图书馆: '重庆市永川区文昌路801号',
  '重庆市潼南区图书馆（新馆）': '重庆市潼南区桂林街道巴蜀大道1003号',
  重庆市璧山区图书馆: '重庆市璧山区璧泉街道双星大道43号旁',
  重庆市铜梁区图书馆: '重庆市铜梁区南城街道迎宾路148号',
  重庆市荣昌区图书馆: 'A馆:重庆市荣昌区昌元街道广场路55号；B馆:重庆市荣昌区昌元街道广场路52号',
  重庆市梁平区图书馆: '重庆市梁平区梁山街道石马路449号',
  重庆市武隆区图书馆: '重庆市武隆区芙蓉中路81号',
  重庆市开州区图书馆: '重庆市开州区汉丰月潭街52附2号',
  重庆市城口县图书馆: '重庆市城口县葛城街道后南街12号附4号（010街坊）',
  重庆市丰都县图书馆: '重庆市丰都县三合街道滨江西路8号（老馆）；重庆市丰都县三合街道秀才路6号（新馆）',
  重庆市垫江县图书馆: '重庆市垫江县桂溪街道文化西路86号',
  重庆市忠县图书馆: '重庆市忠县忠州街道红星梯道8号',
  重庆市云阳县图书馆: '重庆市云阳县双江街道两江广场市民文化活动中心4楼',
  重庆市奉节县图书馆: '重庆市奉节县夔州街道清水社区二组',
  重庆市巫山县图书馆: '重庆市巫山县高唐街道广东东路333号',
  重庆市巫溪县图书馆: '重庆市巫溪县柏杨街道丰益路300号',
  重庆市石柱土家族自治县图书馆: '重庆市石柱县南宾街道干溪子路5号民族文化中心',
  重庆市秀山土家族苗族自治县图书馆: '重庆市秀山土家族苗族自治县乌杨街道渝秀大道195号',
  重庆市酉阳土家族苗族自治县图书馆: '重庆市酉阳县桃花源镇桃花源北路综合文体中心五楼',
  重庆市彭水苗族土家族自治县图书馆: '重庆市彭水苗族土家族自治县汉葭街道民族路88号',
  重庆市群众艺术馆: '重庆市两江新区鸿恩路25号',
  重庆市万州区文化馆: '重庆市万州区白岩路190号',
  重庆市涪陵区文化馆: '重庆市涪陵区马鞍街道站前大道新涪会城市公园内(涪陵北站站前广场对面）',
  重庆市渝中区文化馆: '重庆市渝中区中山三路32号',
  重庆市大渡口区文化馆: '重庆市大渡口区文体支路224号',
  重庆市江北区文化馆: '重庆市江北区金源路64号江北区文化艺术中心',
  重庆市沙坪坝区文化馆: '重庆市沙坪坝区小新街83号',
  重庆市九龙坡区文化馆: '重庆市九龙坡区杨家坪街道西郊支路19号',
  重庆市南岸区文化馆: '重庆市南岸区弹子石新街28号',
  重庆市北碚区文化馆: '重庆市北碚区中山路58号',
  重庆市綦江区文化馆: '重庆市綦江区文龙街道九龙大道52号',
  重庆市大足区文化馆: '重庆市大足区龙景路121号',
  重庆市双桥经开区文化馆: '重庆市大足区通桥街道车城大道41号附2号',
  重庆市渝北区文化馆: '重庆市渝北区仙桃街道百果路55号',
  重庆市巴南区文化馆: '重庆市巴南区龙洲湾街道公园北路18号',
  重庆市黔江区民族文化艺术馆: '重庆市黔江区城西街道新华大道西段1555号',
  重庆市长寿区文化馆: '重庆市长寿区桃园大道9号科技文化中心',
  重庆市江津区文化馆: '重庆市江津区圣泉街道西江大道175号',
  重庆市合川区文化馆: '重庆市合川区希尔安大道225号',
  重庆市永川区文化艺术馆: '重庆市永川区人民东路329号',
  重庆市南川区文化馆: '重庆市南川区西城街道凤江北路3号',
  重庆市璧山区文化馆: '重庆市璧山区双星大道47号',
  重庆市万盛经开区文化馆: '重庆市万盛经开区万东镇滨江西路501号附2号',
  重庆市铜梁区文化馆: '重庆市铜梁区巴川街道龙门街207号',
  重庆市潼南区文化馆: '重庆市潼南区桂林街道巴渝大道1002号',
  重庆市荣昌区文化馆: '重庆市荣昌区昌州街道昌龙大道162号',
  重庆市开州区文化馆: '重庆市开州区汉丰街道月潭街54号附2号',
  重庆市梁平区文化馆: '重庆市梁山街道石马路478号西池广场处（市民文化中心）',
  重庆市武隆区文化馆: '重庆市武隆区芙蓉街道芙蓉西路52号',
  重庆市城口县文化馆: '重庆市城口县葛城街道塔子梁63号',
  重庆市丰都县文化馆: '重庆市丰都县三合街道河北路25号',
  重庆市垫江县文化馆: '重庆市垫江县桂西大道北段1号垫江县文化馆',
  重庆市忠县文化馆: '重庆市忠县忠州街道红星路3号',
  重庆市云阳县文化馆: '重庆市云阳县双江街道两江广场市民文化活动中心3楼',
  重庆市奉节县文化馆: '重庆市奉节县鱼复街道人和街48号',
  重庆市巫山县文化馆: '重庆市巫山县广东东路333号',
  重庆市巫溪县文化馆: '重庆市巫溪县春申大道167号',
  重庆市石柱土家族自治县文化馆: '重庆市石柱县南宾街道干溪子路5号三楼',
  重庆市秀山土家族苗族自治县文化馆: '重庆市秀山县乌杨街道渝秀大道196号',
  重庆市酉阳土家族苗族自治县文化馆: '重庆市酉阳县桃花源北路文体中心4楼',
  重庆市彭水苗族土家族自治县文化馆: '重庆市彭水苗族土家族自治县汉葭街道绸缎街55号附12号',
  重庆市体育馆: '重庆市渝中区两路口街道体育村32号',
  重庆市大田湾体育场: '渝中区两路口体育村34号',
  重庆市奥林匹克体育中心体育场: '重庆市九龙坡区渝州街道奥体路7号',
  重庆市奥林匹克体育中心游泳跳水馆: '重庆市九龙坡区渝州街道奥体街7号',
  '万州游泳（跳水）馆': '重庆市万州区北滨大道一段150号',
  万州区三峡之星体育馆: '万州区北滨大道二段西山公园旁',
  万州体育场: '重庆市万州区牌楼街道北滨大道一段街150号',
  涪陵区体育场: '重庆市涪陵区荔枝街道兴华中路48号',
  涪陵区体育馆: '重庆市涪陵区荔枝街道兴华中路41号',
  大渡口区体育馆: '重庆市大渡口区新山村街道文体路18号',
  江南体育中心体育训练场: '重庆市南岸区海棠溪街道烟雨路1号',
  江南体育中心综合馆: '重庆市南岸区海棠溪街道烟雨路1号',
  江南游泳馆: '重庆市南岸区海棠溪街道烟雨路1号',
  江南体育馆: '重庆市南岸区海棠溪街道烟雨路1号',
  北陪区缙云体育中心体育场: '重庆市北碚区歇马街道冯时行路',
  北陪区绪云体育中心体育馆: '北碚区龙凤溪冯时行路',
  万盛文体中心体育馆: '重庆市綦江区万东镇乡乡镇滨江西路501号',
  万盛文体中心体育场: '重庆市綦江区万东镇乡乡镇滨江西路502号',
  万盛滨江路体育馆: '重庆市綦江区万盛街道体育路7号',
  万盛游泳馆: '重庆市綦江区万东镇乡乡镇滨江西路551号',
  綦江体育中心体育场: '重庆市綦江区通惠街道通惠大道街25号',
  綦江区体育馆: '重庆市綦江区文龙街道九龙大道街61号',
  大足区体育中心游泳馆: '重庆市大足区棠香街道五星大道中段街154号',
  大足区体育中心体育馆: '大足区双桥经济技术开发区双龙西路41号',
  大足区体育中心体育场: '重庆市大足区棠香街道五星大道中段街154号',
  黔江区游泳馆: '重庆市黔江区城西街道河滨西路北段29号',
  黔江区体育场: '重庆市黔江区城西街道河滨西路北段19号',
  黔江区体育馆: '重庆市黔江区城西街道河滨西路北段9号',
  长寿区体育中心体育馆: '重庆市长寿区菩提街道桃花大道文苑南路2号',
  长寿区体育场: '重庆市长寿区菩提街道桃花大道文苑南路2号',
  江津区体育馆: '重庆市江津区鼎山街道鼎山街45号',
  江津区体育场: '重庆市江津区鼎山街道鼎山街45号',
  江津区游泳馆: '重庆市江津区德感街道鼎康路28号',
  '江津区全民健身指导中心（区羽毛球馆）': '重庆市江津区鼎山街道江洲街88号',
  合川区体育馆: '重庆市合川区南街道南屏路183号',
  永川区游泳馆: '重庆市永川区红河大道街道中山路539号',
  永川区体育中心体育场: '重庆市永川区中山路街道红河大道路539号',
  永川区体育馆: '重庆市永川区胜利路街道萱花路275号',
  南川区体育场: '重庆市南川区西城街道渝南大道街东方红居委3组号',
  南川区体育馆: '重庆市南川区西城街道渝南大道街东方红居委3组号',
  璧山区体育馆: '重庆市璧山区璧泉街道文星路133号',
  璧山区体育中心: '重庆市璧山区璧泉街道金剑街430号',
  铜梁区藕塘湾体育场: '重庆市铜梁区巴川街道龙山社区街82号',
  铜梁区全民健身中心: '重庆市铜梁区南城街道金龙大道街21号',
  铜梁区金龙体育馆: '重庆市铜梁区东城街道迎宾东路159号',
  铜梁龙体育场: '重庆市铜梁区巴川街道龙门街498号',
  潼南区体育场: '重庆市潼南区桂林街道五湖路538号',
  潼南区体育馆: '重庆市潼南区梓潼街道大同街399号',
  荣昌区体育场: '重庆市荣昌区昌元街道宝城支路7号',
  荣昌区体育中心游泳池: '重庆市荣昌区昌元街道海棠大道街78号',
  荣昌区全民健身活动中心: '重庆市荣昌区昌州街道荣昌大道路118号',
  荣昌区体育馆: '重庆市荣昌区昌元街道海棠大道街78号',
  武隆区体育馆: '重庆市武隆区芙蓉街道芙蓉中路83附8号',
  庙坝镇全民健身中心: '重庆市城口县庙坝镇乡镇石兴村19社号',
  东安镇全民健身中心: '重庆市城口县东安乡镇兴田村10号',
  城口县岗天乡全民健身中心: '重庆市城口县复兴街道友谊社区街便民服务中心',
  城口县体育馆: '重庆市城口县葛城街道建学路5号',
  丰都县体育馆: '重庆市丰都县三合街道名山大道街86号',
  丰都县体育场: '重庆市丰都县三合街道名山大道街86号',
  垫江县体育馆: '重庆市垫江县桂溪街道桂西街北段1号',
  垫江县体育场: '重庆市垫江县桂溪街道桂西街北段1号',
  垫江县全民健身中心: '重庆市垫江县桂溪街道北段街1号',
  忠县体育馆: '重庆市忠县忠州街道巴王路8号',
  云阳县全民健身活动中心: '重庆市云阳县双江街道体育路289号',
  云阳县体育馆: '重庆市云阳县青龙街道滨江大道街877号',
  云阳县体育场: '重庆市云阳县双江街道体育路289号',
  云阳县游泳中心: '重庆市云阳县双江街道体育路289号',
  巫山县章家湾训练中心: '重庆市巫山县高唐街道净坛社区街老体委综合楼号',
  重庆市巫山县苟家体育场: '重庆市巫山县高唐街道起云社区街巫峡路号',
  巫山县体育馆: '重庆市巫山县高唐街道起云社区巫峡路500号',
  巫山县全民健身中心: '重庆市巫山县高唐街道登龙社区街333号',
  石柱县体育场: '重庆市石柱土家族自治县南宾街道城东北路4号',
  石柱县体育馆: '重庆市石柱土家族自治县南宾街道城东北路4号',
  秀山体育场: '重庆市秀山土家族苗族自治县乌杨街道郭园社区街A号',
  秀山体育馆: '重庆市秀山土家族苗族自治县乌杨街道郭园社区街A号',
  彭水县体育场: '重庆市彭水苗族土家族自治县靛水街道体育街11号',
  彭水县体育馆: '重庆市彭水苗族土家族自治县绍庆街道插旗街247号',
  彭水县全民健身中心: '重庆市彭水苗族土家族自治县靛水街道体育街党校后门号',
  开州区体育馆: '重庆市开县云枫街道滨湖西路45号',
  开州区游泳馆: '重庆市开县汉丰街道滨湖中路390号',
  开州区体育场: '重庆市开县云枫街道街道云枫街道街长青社区花仙路19号',
  梁平区东门体育馆: '梁平区梁山街道东池巷51号',
  梁平区东门游泳馆: '重庆市梁平区梁山街道东池路51号',
  酉阳县体育馆: '重庆市酉阳土家族苗族自治县桃花源街道源泉新路2号',
  杭州全民健身中心: '上城区富春路80号',
  杭州游泳健身馆: '拱墅区中山北路572号',
  杭州大关游泳健身馆: '拱墅区大关小区东四苑18号',
  杭州体育场: '拱墅区体育场路169号',
  杭州体育馆: '拱墅区体育场路210号',
  杭州市陈经纶体育学校: '西湖区曙光路126号',
  杭州市职工文化中心: '上城区东宁路501号',
  '杭州市体育事业发展中心杭州体育馆（改建中）': '下城区体育场路210号',
  杭州市体育事业发展中心杭州体育场: '下城区体育场路169号',
  杭州市体育事业发展中心杭州游泳健身馆: '下城区中山北路572号',
  杭州市体育事业发展中心杭州大关游泳健身馆: '拱墅区大关小区东四苑18号',
  '杭州市体育事业发展中心杭州全民健身中心（在建）': '上城区富春路甬江路交叉口北侧',
  上城区定安路体育中心: '定安路20号',
  下城区体育中心: '杭州市潮王路8号',
  江干区体育中心: '江干区钱潮路12号至16号',
  九堡体育中心: '江干区九睦路109号',
  丁兰文体中心: '江干区临丁路1180号',
  西湖区文体中心: '西湖区晴川街217号',
  拱墅区体育馆: '拱墅区双荡弄120号',
  拱墅区文体中心: '拱墅区草营巷8号',
  江南体育中心: '滨江区春晓路411号',
  滨江区体育馆: '滨江区江虹路996号',
  萧山区体育中心: '萧山区城厢街道市心南路398号',
  '萧山区临浦镇文体中心（改建中）': '萧山区临浦镇人民路22号',
  萧山区瓜沥镇文体中心: '萧山区建设四路10778号',
  萧山区衙前镇文体中心: '萧山区衙前镇萧明线与农运路的西南角。',
  '余杭区体育中心（改建中）': '余杭区南苑街道东湖南路177号',
  余杭区闲林体艺馆: '闲林街道方家山路88号',
  富阳区体育中心: '富阳区富春街道桂花西路201号',
  '临安文体会展中心(改建中)': '锦南新城九州街599号',
  桐庐县体育馆: '城南街道大联路505号',
  桐庐县城北体育健身中心: '桐君街道康乐路348号',
  桐庐县分水镇文体中心: '桐庐县分水镇玉华路315号',
  桐庐县横村镇文体中心: '桐庐县横村镇市场路99号',
  淳安县体育馆: '淳安县千岛湖镇开发路435号',
  建德市新安江体育馆: '建德市新安江街道新安东路700号',
  杭州市奥体中心: '杭州市萧山区飞虹路',
  杭州市西湖区文化馆: '杭州市西湖区曙光路184号',
  杭州市西湖区图书馆: '杭州市西湖区古墩路413-1号',
  余杭区文化馆: '杭州市余杭区瓶窑镇崇北街9号',
  余杭区图书馆: '杭州市余杭区瓶窑镇崇北街9号',
  仓前街道图书分馆: '杭州市余杭区仓兴街300号太炎未来社区梦想中心4楼',
  良渚街道图书分馆: '杭州市余杭区良平街750号',
  仁和街道图书分馆: '仁和街道幸福综合体二楼（和旺街22号）',
  五常街道图书分馆: '五常街道党群服务中心西坝路59号2号楼3楼大厅',
  闲林街道图书分馆: '闲林街道方家山路88号闲林体艺馆二楼',
  余杭街道图书分馆: '杭州市余杭区余杭街道安乐路236号',
  中泰街道图书分馆: '杭州市余杭区中泰街道中泰路370号',
  百丈镇图书分馆: '百丈镇文体活动中心三楼',
  黄湖镇图书分馆: '余杭区黄湖镇迂前南路157-5号',
  径山镇图书分馆: '径山镇文体活动中心4楼',
  鸬鸟镇图书分馆: '鸬鸟镇雅城村245号文体大楼二楼',
  瓶窑镇图书分馆: '余杭区瓶窑镇新窑路288号',
  '余杭章太炎故居纪念馆（章太炎研究中心）': '杭州市余杭区仓前街道仓前塘路59号',
  '余杭小百花越剧艺术中心（苕溪大剧院）': '杭州市余杭区瓶窑镇崇北街9号',
  余杭区非遗馆: '崇北街9号余杭文化中心2楼',
  良渚街道综合文化站: '杭州市余杭区良渚街道良平街750号',
  鸬鸟镇乡镇综合文化站: '杭州市余杭区鸬鸟镇雅城街道245号',
  黄湖镇综合文化站: '杭州市余杭区黄湖镇迂前南路157-5号',
  瓶窑镇综合文化站: '杭州市余杭区瓶窑镇新窑路288号',
  中泰街道综合文化站: '杭州市余杭区中泰街道中泰路370号',
  径山镇乡镇综合文化站: '杭州市余杭区径山镇府后街5号',
  仁和街道综合文化站: '杭州市余杭区仁和街道和旺街22号',
  仓前街道综合文化站: '杭州市余杭区仓前街道仓兴街300号文体活动中心',
  闲林街道综合文化站: '杭州市余杭区闲林街道方家山路88号',
  百丈镇综合文化站: '杭州市余杭区百丈镇百兴路24号',
  五常街道综合文化站: '杭州市余杭区五常街道西坝路59号2号楼',
  余杭街道综合文化站: '杭州市余杭区余杭街道安乐路236号',
  杭州市滨江区文化馆: '杭州市滨江区泰安路200号滨江区文化中心5楼',
  杭州市滨江区图书馆: '杭州市滨江区泰安路200号滨江区文化中心6-8楼',
  杭州市滨江区非物质文化遗产馆: '杭州市滨江区天官路8号',
  区文化馆: '杭州市临平区乔司街道汀兰街239号',
  区图书馆: '临平区藕花洲大街231号、233-241号',
  临平博物馆: '杭州市临平区南苑街道南大街95号',
  '图书馆临平街道分馆（智慧分馆）': '临平街道景山路与邱山大街交叉口',
  图书馆运河街道分馆: '运河街道鹿溪路141号',
  图书馆南苑街道分馆: '南苑街道南大街263-5号',
  图书馆星桥街道分馆: '星桥街道文体中心二楼（藕花洲大街西段620号）',
  图书馆乔司街道分馆: '乔司街道保庆街74号乔司综合文化大楼二楼',
  图书馆崇贤街道分馆: '崇贤街道尚德路39号',
  '图书馆东湖街道分馆（北沙书房）': '东湖街道荷花路150号-158号',
  图书馆塘栖镇分馆: '塘栖镇人民路与文苑路交叉口塘栖镇文体活动中心大楼',
  太平天国历史博物馆: '南京秦淮区（夫子庙）瞻园路128号',
  中共代表团梅园新村纪念馆: '南京玄武区汉府街18-1号',
  南京市民俗博物馆: '南京秦淮区南捕厅15号',
  城墙博物馆: '南京市秦淮区新民坊路边营1号',
  南京市文化馆: '南京市玄武区长江路101号',
  玄武区文化馆: '太平北路120-2号',
  栖霞区文化馆: '栖霞区艺术中心南门旁',
  江宁区文化馆: '南京市江宁区上元大街168号',
  浦口区文化馆: '南京市浦口区江浦街道象山路4号市民中心C座4-6楼',
  雨花台区文化馆: '雨花台区竹影路5号',
  秦淮区文化馆: '秦淮区苜蓿园大街112号二、三楼',
  建邺区文化馆: '南京市建邺区沙洲街道雨润大街99号双和园办公区4号楼',
  鼓楼区文化馆: '南京市鼓楼区二板桥486号',
  六合区文化馆: '南京市六合区雄州街道王桥路168号',
  溧水区文化馆: '溧水区西坛路89号中山书院内',
  高淳区文化馆: '南京市高淳区固城湖北路60号',
  江北新区文化馆: '江北新区大厂街道新华路386号',
  百家湖文化中心: '江宁区西门子路6号',
  雨花台区图书馆: '竹影路5号3号楼2-6层',
  溧水区图书馆: '溧水区中山西路14号',
  建邺区图书馆: '南京市建邺区沙洲街道雨润大街99号双和园办公区5号楼',
  鼓楼区图书馆: '南京市鼓楼区二板桥486号',
  江宁区图书馆: '南京市江宁区土山路46号',
  浦口区图书馆: '浦口区江浦街道象山路4号市民中心A栋1-2层',
  高淳区图书馆: '南京市高淳区淳溪镇石臼湖南路7号2幢',
  秦淮区图书馆: '南京市秦淮区钞库街21号',
  栖霞区图书馆: '南京市栖霞区尧化门尧辰路',
  六合区第二图书馆: '六合区新华路178号',
  六合区图书馆: '南京市六合区王桥路155号',
  玄武区少年儿童图书馆: '南京市太平北路120-2号（玄武区少年宫旁）',
  溧水区儿童图书馆: '溧水区永阳街道大东门街81号',
  '南京江北图书馆（新馆）': '南京江北新区石佛大街131号',
  江苏省美术馆: '南京市长江路333号',
  金陵美术馆: '南京市秦淮区剪子巷50号',
  黄炎培故居: '新川路218号',
  张闻天故居: '川南奉公路4398号',
  浦东历史博物馆: '惠南镇文师街18号',
  上海中国航海博物馆: '申港大道197号',
  高桥历史文化陈列馆: '高桥镇义王路1号',
  新场历史文化陈列馆: '新场镇海泉街128号',
  上海吴昌硕纪念馆: '陆家嘴东路15号',
  上海美特斯邦威服饰博物馆: '环桥路208号2号楼',
  上海动漫博物馆: '张江路69号',
  上海震旦博物馆: '富城路99号',
  '上海（中医药大学）中医药博物馆': '蔡伦路1200号',
  上海东方地质博物馆: '祝桥镇江镇路100号',
  上海观复博物馆: '银城中路501号上海中心大厦37层',
  上海金刚博物馆: '园顺路89号',
  上海有恒博物馆: '浦东大道288号1楼',
  上海海派红木艺术博物馆: '万灵路99号',
  交通银行博物馆: '银城中路188号47层',
  上海老相机摄影博物馆: '五星路676弄39号',
  上海火炬众创孵化博物馆: '秀浦路2388号1号楼',
  '上海天文馆（上海科技馆分馆）': '临港大道380号',
  上海宝库匠心博物馆: '银城中路501号上海中心大厦38层',
  上海双拥工作展览馆: '浦东大道2601号',
  '上海市历史博物馆（上海革命历史博物馆）': '南京西路325号',
  '中共代表团驻沪办事处纪念馆（周公馆）': '思南路73号',
  中国社会主义青年团中央机关旧址纪念馆: '淮海中路567弄1-6号',
  上海豫园管理处: '福佑路168号',
  上海三山会馆管理处: '中山南路1551号',
  上海韬奋纪念馆: '重庆南路205弄53-54号',
  上海孙中山故居纪念馆: '香山路7号',
  上海周虎臣曹素功笔墨博物馆: '福州路429号',
  上海琉璃艺术博物馆: '泰康路25号',
  上海电信博物馆: '延安东路34号',
  上海民政博物馆: '普育西路105号1号楼',
  上海市外滩历史纪念馆: '中山东一路475号',
  童涵春堂中药博物馆: '豫园新路20号3楼（豫园商城内）',
  上海市银行博物馆: '复兴中路301号',
  大韩民国临时政府旧址管理处: '马当路306弄4号',
  '国际乒联博物馆（中国乒乓球博物馆）': '局门路796号',
  上海体育博物馆: '南京西路150号',
  中国劳动组合书记部旧址陈列馆: '成都北路893弄1-11号',
  上海毛泽东旧居陈列馆: '茂名北路120弄',
  上海蔡元培故居陈列馆: '华山路303弄16号',
  中共上海地下组织斗争史陈列馆暨刘长胜故居: '愚园路81号',
  中共二大会址纪念馆: '老成都北路7弄30号',
  '上海自然博物馆（上海科技馆分馆）': '北京西路510号',
  中共三大后中央局机关历史纪念馆: '浙江北路118号',
  中共淞浦特委机关旧址陈列馆: '山海关路339号（静安雕塑公园北侧）',
  元利当铺旧址博物馆: '武定路203号',
  上海眼镜博物馆: '宝昌路533号',
  上海四行仓库抗战纪念馆: '光复路21号',
  上海棋牌文化博物馆: '南京西路595号上海棋院1楼',
  上海印刷字体展示馆: '新闸路1209弄60号',
  上海寰宇铃铛博物馆: '西康路538号1幢2楼',
  中共中央秘书处机关旧址纪念馆: '江宁路673弄10号',
  中共中央军委机关旧址纪念馆: '新闸路613弄12号',
  中央特科机关旧址纪念馆: '武定路930弄14号',
  黄道婆纪念馆: '徐梅路700号',
  徐光启纪念馆: '南丹路17号',
  上海土山湾博物馆: '蒲汇塘路55号',
  上海市龙华烈士纪念馆: '龙华西路180号',
  上海宋庆龄故居纪念馆: '淮海中路1843号',
  中国科学院上海昆虫博物馆: '枫林路300号',
  上海师范大学博物馆: '桂林路100号东部校区艺苑楼一楼',
  上海音乐学院东方乐器博物馆: '淮海中路1189号',
  上海交通大学校史博物馆: '华山路1954号',
  上海交通大学董浩云航运博物馆: '华山路1954号',
  钱学森图书馆: '华山路1800号',
  上海无线电博物馆: '田林路200号B幢1楼',
  衡复风貌博物馆群: '衡复风貌馆（复兴西路62号）夏衍旧居（乌鲁木齐南路178号2号楼）、草婴书房（乌鲁木齐南路178号3号楼）、张乐平故居（五原路288弄3号）、柯灵故居（复兴西路147号）、衡复艺术中心（乌鲁木齐南路178号1号楼）',
  上海气象博物馆: '蒲西路166号',
  上海品牌博物馆: '漕宝路650号1号楼2楼',
  '《义勇军进行曲》灌制地纪念馆 （百代小楼）': '衡山路811号',
  上海市长宁区革命文物陈列馆: '愚园路1376弄34号',
  宋庆龄生平事迹陈列馆: '宋园路21号',
  '上海（东华大学）纺织服饰博物馆': '延安西路1882号',
  上海凝聚力工程博物馆: '长宁路878号',
  上海艺术品博物馆: '延安西路1731号',
  上海广播博物馆: '虹桥路1376号广播大厦',
  上海对外经贸大学博物馆: '古北路620号',
  上海元代水闸遗址博物馆: '延长西路619号',
  顾正红纪念馆: '澳门路300号',
  苏州河工业文明展示馆: '光复西路2690号',
  上海纺织博物馆: '澳门路128号',
  华东师范大学博物馆: '中山北路3663号',
  沪西工人半日学校史料陈列馆: '西苏州路1037号',
  上海泰迪之家泰迪熊博物馆: '泸定路46弄3号2层',
  上海鲁迅纪念馆: '甜爱路200号',
  中共四大纪念馆: '四川北路1468号',
  左联会址纪念馆: '多伦路201弄2号',
  李白烈士故居: '黄渡路107弄15号',
  沈尹默故居: '海伦路504号',
  上海邮政博物馆: '天潼路395号2楼',
  上海犹太难民纪念馆: '长阳路62号',
  中国证券博物馆: '黄浦路15号',
  国歌展示馆: '荆州路151号',
  上海中国烟草博物馆: '长阳路728号',
  上海院士风采馆: '国顺东路369号',
  复旦大学博物馆: '邯郸路220号',
  上海理工大学印刷博物馆: '水丰路100号',
  上海海洋大学博物馆: '军工路318号',
  上海体育大学武术博物馆: '长海路399号',
  上海财经大学商学博物馆: '国定路777号',
  同济大学博物馆: '四平路1239号同济大学一·二九大楼',
  中国近现代新闻出版博物馆: '周家嘴路3678号',
  上海世界技能博物馆: '杨树浦路1578号',
  上海淞沪抗战纪念馆: '友谊路1号',
  上海陈化成纪念馆: '友谊路1号',
  上海市陶行知纪念馆: '武威东路76号',
  上海解放纪念馆: '宝杨路599号',
  南京路上好八连事迹陈列馆: '上大路55号',
  '上海大学博物馆（海派文化博物馆）': '上大路99号（南陈路333号）',
  上海中国工业设计博物馆: '逸仙路3000号3号楼二层',
  上海尊木汇木文化博物馆: '沪太路2751号',
  上海智慧湾增材制造文化博物馆: '蕰川路6号',
  上海百诺巧克力博物馆: '锦秋路117号',
  上海杨明洁工业设计博物馆: '长江路258号中成智谷C8栋',
  闵行区博物馆: '闵行区新镇路1538号',
  张充仁纪念馆: '七宝古镇蒲溪广场75号',
  上海民族乐器博物馆: '七宝镇联明路400号',
  上海航宇科普中心: '沪闵路7900号',
  上海观止矿晶博物馆: '先锋街66号阿拉城26幢一、二层',
  上海翰林匾额博物馆: '虹许路731号8号楼1楼',
  上海交通大学博物馆: '东川路800号文博楼',
  上海乳业博物馆: '万源路2729号',
  嘉定竹刻博物馆: '南大街321号',
  顾维钧生平陈列馆: '南大街349号',
  四海壶具博物馆: '曹安公路1978号百佛园',
  上海翥云艺术博物馆: '新源路1375号',
  上海大来时间博物馆: '和静路981号',
  上海海纳吴觉农茶文化博物馆: '曹安公路1978号1号楼103室',
  金山区博物馆: '金山大道1800号',
  上海南社纪念馆: '张堰镇新建路130号',
  上海市沧海盐田盐文化博物馆: '漕泾镇蒋庄路2067号',
  上海市松江区博物馆: '中山东路233号',
  上海中国留学生博物馆: '茸梅路1177弄7号',
  上海天文博物馆: '西佘山顶',
  上海立信会计学院中国会计博物馆: '文翔路2800号',
  上海国际酒文化博物馆: '佘天昆公路辰山植物园内（辰山植物园3号门）',
  董其昌书画艺术博物馆: '人民南路64号',
  上海外国语大学语言博物馆: '文翔路1550号',
  上海来伊份零食博物馆: '九新公路855号',
  青浦区博物馆: '华青南路1000号',
  陈云纪念馆: '练塘镇老朱枫公路3516号',
  上海福寿园人文纪念馆: '外青松公路7270弄600号',
  上海市青浦区任屯血防陈列馆: '金泽镇任屯村111号',
  上海崧泽遗址博物馆: '沪青平公路3993号',
  上海中华印刷博物馆: '汇金路889号',
  上海红十字历史文化陈列馆: '赵重公路135号',
  奉贤区博物馆: '奉贤区湖畔路333号',
  上海知青博物馆: '海乐路200号',
  上海农垦博物馆: '海湾镇随塘河路1677号',
  上海真静传统木作博物馆: '南桥镇南桥路839号',
  上海电线电缆博物馆: '青村镇青伟路233号2-3楼',
  崇明区博物馆: '城桥镇鳌山路696号',
  上海崇明向化灶文化博物馆: '向化镇向中路91号',
  上海崇明竖新抗日战争博物馆: '前竖公路2773号三楼',
  江南造船展示馆: '长兴岛长兴江南大道988号',
  '上海图书馆（淮海馆）': '徐汇区淮海中路1555号',
  '上海图书馆（东馆）': '浦东新区迎春路300号、合欢路300号',
  '上海少年儿童图书馆（长风馆）': '普陀区光复西路2500号',
  '上海少年儿童图书馆（南西馆）': '静安区南京西路962号',
  上海浦东图书馆: '前程路88号',
  上海浦东图书馆南汇分馆: '惠南镇人民西路326号',
  '上海浦东图书馆陆家嘴分馆（东方路）': '东方路38号',
  '上海浦东图书馆陆家嘴分馆（浦城路）': '浦城路150号',
  上海浦东图书馆少儿分馆: '张杨路3680弄1号楼5-8楼',
  南码头路街道图书馆: '南码头路400号',
  三林镇图书馆: '三林路338号',
  三林镇图书馆懿德分馆: '和融路51号',
  三林镇图书馆世博分馆: '东书房路629弄8号',
  塘桥街道图书馆: '蓝村路86号',
  北蔡镇图书馆: '陈春路101号3楼',
  张江图书馆: '中科路2329号B座3楼',
  张江图书馆孙桥分馆: '孙建路480弄98号5号楼5楼',
  潍坊街道图书馆: '南泉路269号2楼',
  金杨新村街道图书馆: '云山路1080弄2号一楼',
  周家渡街道图书馆: '齐河路508号2楼',
  上钢图书馆: '历城路75号',
  上钢图书馆综合体分馆: '成山路66号2号楼3楼',
  花木街道图书馆: '梅花路289号401室',
  东明路街道图书馆: '东明路2616号4楼',
  高东镇图书馆: '光烁路39号',
  高桥镇图书馆: '张杨北路5425号',
  高行镇图书馆: '新行路340号4楼',
  '南汇新城镇图书馆（芦潮港馆）': '芦硕路298号2楼',
  '南汇新城镇图书馆（申港馆）': '古棕路211号5楼',
  宣桥镇图书馆: '下盐路3824号',
  新场镇图书馆: '新环东路276号',
  万祥镇图书馆: '万祥路95号',
  合庆镇图书馆: '东川公路7777号2号楼一楼',
  惠南镇图书馆: '川南奉公路6193号3楼',
  惠南镇图书馆东城分馆: '惠东路268号4号楼4楼',
  '新川沙图书馆（成人馆）': '川黄路157号',
  '新川沙图书馆（少儿馆）': '新川路555号',
  曹路镇图书馆: '川沙路582号',
  康桥镇图书馆: '康沈路686号',
  祝桥镇图书馆: '航亭环路158号',
  老港镇图书馆: '建中路458号',
  浦兴路街道图书馆: '博兴路1473号204',
  浦兴路街道图书馆金桥湾分馆: '长岛路1280弄70号3楼',
  周浦镇图书馆: '周东路266号',
  傅雷图书馆: '沈梅东路800号',
  泥城镇图书馆: '鸿音路3156弄8号',
  唐镇图书馆: '顾唐路3150号1楼',
  '唐镇图书馆（王港分中心）': '宏雅路8号2楼',
  航头镇图书馆: '航鹤路388号文体楼二楼',
  航头镇图书馆鹤沙分馆: '鹤韵路385号',
  沪东社区图书馆: '柳埠路135弄25号二楼',
  陆家嘴街道图书馆: '乳山路153-155号',
  书院镇图书馆: '老芦公路861号',
  洋泾社区图书馆: '博山路51弄60号',
  金桥镇图书馆: '金高路1777号4楼',
  大团镇图书馆: '南团公路3330号',
  黄浦区图书馆: '福州路655号',
  '黄浦区明复图书馆(原卢湾区图书馆)': '陕西南路235号',
  半淞园路街道图书馆: '西藏南路1360号2楼',
  打浦桥街道图书馆: '蒙自路223号2楼、3楼',
  淮海中路街道图书馆: '马当路349号5楼',
  南京东路街道图书馆: '江阴路101号103室、201室、204室',
  瑞金二路街道图书馆: '陕西南路245号4楼',
  外滩街道图书馆: '河南中路578号3楼、4楼',
  五里桥街道图书馆: '龙华东路600号215室',
  小东门街道图书馆: '黄家路88弄10号二楼',
  豫园街道图书馆: '傅家街65号4楼',
  老西门街道图书馆: '中华路990号2楼、3楼',
  '静安区图书馆（新闸路）': '新闸路1708号',
  '静安区图书馆（天目中路）': '天目中路2号',
  '静安区图书馆（闻喜路）': '闻喜路800号',
  静安区少年儿童图书馆: '康定东路28号',
  静安区闸北少年儿童图书馆: '汾西路261弄24号',
  曹家渡街道图书馆: '万航渡路676弄46号',
  曹家渡街道达安星之会所图书室: '长寿路999弄15号2楼',
  '曹家渡街道图书馆（少儿）': '万航渡路767弄56号2号楼二楼',
  静安区图书馆北站街道分馆: '浙江北路389号',
  江宁路街道图书馆: '昌平路710号2楼',
  静安寺街道图书馆: '新闸路1855号3楼',
  南京西路街道图书馆: '升平街33号',
  南京西路街道少儿图书馆: '延安中路602号',
  石门二路街道图书馆: '康定东路85号',
  宝山路街道图书馆: '宝昌路533号6楼',
  '北站街道图书馆（艺术图书馆）': '山西北路108弄13号2楼（预计今年4月下旬开）',
  大宁路街道图书馆: '共和新路1700弄70号甲',
  宁的书房: '共和新路1928号大宁国际商业广场12座2楼',
  '大宁路街道分馆（社区文化中心）': '平型关路1179号3楼',
  共和新路街道图书馆: '延长中路755号2楼',
  临汾路街道图书馆: '安业路76号南厅（暂时搬至该点位，仅阅览）',
  彭浦新村街道图书馆: '共和新路4666弄城市新汇5号楼3楼',
  彭浦镇图书馆: '彭浦镇灵石路745号2楼',
  天目西路街道图书馆: '沪太路150号2楼',
  芷江西路街道图书馆: '芷江西路151号3楼',
  '徐汇区图书馆（徐家汇书院）': '漕溪北路158号',
  徐家汇街道图书馆: '南丹东路109号',
  天平路街道图书馆: '临时服务点：岳阳路77弄20号二楼',
  湖南路街道图书馆: '乌鲁木齐中路164号',
  枫林路街道图书馆: '临时服务点：双峰路400号枫林党群服务中心一楼',
  斜土路街道图书馆: '大木桥路461号二楼',
  田林街道图书馆: '田林东路588号',
  长桥街道图书馆: '罗香路237号',
  虹梅路街道图书馆: '全州路81号',
  康健新村街道图书馆: '浦北路988号3楼',
  龙华街道图书馆: '临时服务点：徐汇区龙水南路322号龙南邻里汇一楼',
  凌云路街道图书馆: '梅陇路415号',
  漕河泾街道图书馆: '康健路135号二楼',
  '漕河泾街道图书馆 石龙分馆': '龙川北路777号',
  华泾镇图书馆: '华泾镇华泾路505号',
  '长宁区图书馆（天山馆）': '天山路356号',
  '长宁区图书馆（愚园馆）': '愚园路1188号',
  '长宁区图书馆（仙霞馆）': '仙霞路700弄41号',
  北新泾街道图书馆: '新泾一村144号3楼',
  程家桥街道图书馆: '哈密路1955号5楼',
  虹桥街道图书馆: '虹桥路1115弄19号',
  '虹桥街道图书馆分馆（古北天空书苑）': '富贵东道99号',
  华阳路街道图书馆: '安化路500号三楼',
  江苏路街道图书馆: '安西路45号',
  天山路街道图书馆: '天山四村122号',
  仙霞新村街道图书馆: '仙霞路435弄5号',
  新华路街道图书馆: '法华镇路453号3楼',
  新泾镇图书馆: '哈密路1358号4楼',
  周家桥街道图书馆: '玉屏南路560弄78号3楼',
  曹杨新村街道图书馆: '杏山路317号',
  长风新村街道图书馆: '枣阳路251弄100号',
  长寿路街道图书馆: '长寿路505弄6号3楼',
  万里街道图书馆: '真金路51号3楼',
  长征镇图书馆: '梅川路1255号北4楼 成人馆 梅川路1255号南1楼 少儿馆',
  甘泉街道图书馆: '延长西路400号',
  石泉路街道图书馆: '宁强路33号',
  桃浦镇图书馆: '桃浦镇红棉路188号',
  宜川路街道图书馆: '华阴路200号2楼',
  真如镇街道图书馆: '兰溪路968号3楼',
  虹口区图书馆: '水电路1412号',
  虹口区图书馆曲阳分馆: '临时服务点：大连西路199号欧阳路街道社区文化活动中心（北部）一楼',
  虹口区图书馆和平分馆: '大连路1391号 综合馆 大连路1375号 少儿馆',
  广中路街道图书馆: '恒业路300号',
  嘉兴路街道图书馆: '瑞虹路400号4楼',
  江湾镇街道图书馆: '凉城路2130号 北楼3楼（少儿馆）、南楼7楼（成人馆）',
  '江湾镇街道图书馆分馆（逸仙会客厅）': '场中路4弄15号',
  凉城新村街道图书馆: '车站南路340号4楼',
  欧阳路街道图书馆: '四平路621弄甲100号',
  曲阳路街道图书馆: '中山北一路998号3楼',
  北外滩街道图书馆: '通州路99号2楼',
  四川北路街道图书馆: '吴淞路669号3楼',
  '杨浦区图书馆（平凉分馆）': '长阳路1687号西2号楼1楼',
  '杨浦区图书馆（少儿分馆）': '嫩江路民星二村38号',
  长白新村街道图书馆: '延吉东路105号四楼',
  大桥街道图书馆: '平凉路1730号',
  定海路街道图书馆: '长阳路3066号',
  江浦路街道图书馆: '许昌路1150号5楼',
  江浦路街道图书馆少儿分馆: '辽源西路143号2楼',
  控江路街道图书馆: '凤城二村19号',
  平凉路街道图书馆: '怀德路399号',
  四平路街道图书馆: '抚顺路360号',
  五角场街道图书馆: '政化路257号5楼',
  '五角场街道图书馆（国定支路分馆）': '国定支路27号菜场旁边',
  '长海路街道图书馆（政府路馆）': '政府路78号',
  '长海路街道图书馆（翔殷路馆）': '翔殷路505弄3号',
  '长海路街道图书馆（市光路馆）': '民京路823号甲',
  延吉新村街道图书馆: '靖宇东路267号地下一楼',
  殷行街道图书馆: '市光三村164号',
  新江湾城街道图书馆: '国秀路700号',
  大场镇图书馆: '沪太路2010号-1',
  高境镇图书馆: '高境路371号5楼',
  顾村镇图书馆: '共富二路122号',
  '顾村镇图书馆（诗乡广场分馆）': '富联路368号',
  '顾村镇图书馆（馨佳园分馆）': '潘广路1445号',
  '顾村镇图书馆（菊泉分馆）': '菊盛路99弄70号3号楼',
  罗店镇图书馆: '美诺路131号',
  '罗店镇图书馆（塘西街分馆）': '塘西街366-370号',
  '罗店镇图书馆（美兰西湖分馆）': '美文路211号',
  罗泾镇图书馆: '陈功路799号',
  罗泾镇图书馆分馆: '萧月路153号',
  庙行镇图书馆: '长江西路2697号',
  淞南镇图书馆: '淞发路578号',
  吴淞街道图书馆: '淞浦路492号',
  杨行镇图书馆: '松兰路826号',
  友谊路街道图书馆: '同济路990号（益友空间党群服务中心二楼）',
  '月浦镇图书馆（盛桥馆）': '盛桥三村48号',
  '月浦镇图书馆（庆安路馆）': '庆安路51弄6号楼',
  '月浦镇图书馆（龙镇路馆）': '龙镇路88号',
  '月浦镇图书馆（马泾桥馆）': '蕰川路4051号',
  张庙街道图书馆: '一二八纪念路728弄58号2号楼',
  '古美路街道图书馆（东馆）': '平阳路256号',
  '古美路街道图书馆（西馆）': '合川路366号3楼（成人区）、4楼（少儿区）',
  虹桥镇图书馆: '虹桥镇万源路2800号',
  华漕镇图书馆: '华漕镇纪翟路550号',
  大零号湾图书馆: '兰坪路158号',
  马桥镇图书馆: '马桥镇富卓路120号',
  梅陇镇图书馆: '梅陇镇高兴路108号',
  梅陇镇图书馆晶城分馆: '兴南路385号3楼',
  浦江图书馆: '浦涛路252号',
  浦江镇图书馆永康分馆: '浦江镇永寨路375号',
  七宝镇图书馆: '七宝镇沪松公路450号4楼',
  吴泾镇图书馆: '尚义路39弄3号楼401室（宝龙广场）',
  新虹街道图书馆: '宁虹路1122号A栋',
  莘庄工业区图书馆: '颛盛路745号一楼',
  莘庄镇图书馆: '莘庄镇龙茗路128号2楼',
  颛桥镇图书馆: '都市路2699号一楼',
  浦锦街道图书馆: '江桦路651号',
  嘉定区图书馆: '裕民南路1288号',
  嘉定区图书馆清河路分馆: '清河路34弄40号',
  安亭镇图书馆: '安亭镇墨玉路149号',
  '安亭镇图书馆（黄渡分馆）': '嘉定区博园路4800号',
  '安亭镇图书馆（方泰分馆）': '嘉松北路4355弄88号',
  华亭镇图书馆: '嘉行公路3198号',
  嘉定工业区图书馆: '汇源路188号二号楼',
  嘉定镇街道图书馆: '嘉定镇街道清河路196号',
  江桥镇图书馆: '江桥镇华江路129弄2号楼',
  江桥镇龙湖图书馆: '江桥镇海波路1020号',
  菊园新区图书馆: '菊园新区棋盘路1255号',
  马陆镇图书馆: '马陆镇宝安公路3322号',
  南翔镇图书馆: '南翔镇古猗园路737号',
  南翔镇图书馆东社区分馆: '南翔镇仲秋路168号',
  外冈镇图书馆: '外冈镇中泉路76号',
  新成路街道图书馆: '仓场路335号3楼',
  徐行镇图书馆: '徐行镇新建一路1568号',
  真新街道图书馆: '新郁路755弄55号',
  '真新街道图书馆（新丰分馆）': '金沙江路2823弄2号',
  金山区图书馆: '蒙山北路280号',
  漕泾镇图书馆: '漕泾镇富漕路239号',
  枫泾镇图书馆: '枫泾镇枫丽路127号',
  高新区图书馆: '恒顺路280弄39号',
  金山卫镇图书馆: '金山卫镇古城路295号',
  金山卫镇图书馆钱圩分馆: '金山卫镇钱圩建圩路20弄38号',
  廊下镇图书馆: '廊下镇景钱路1708号',
  吕巷镇图书馆: '吕巷镇朱吕公路6858号',
  吕巷镇图书馆干巷分馆: '干新路7号',
  山阳镇图书馆: '山阳镇体育路53号',
  山阳镇海璟图书馆: '龙湾路66弄11号201室',
  石化街道图书馆: '石化街道象州路238号',
  亭林镇图书馆: '亭林镇亭升路550弄33号',
  张堰镇图书馆: '张堰镇东贤路961号',
  朱泾镇图书馆: '朱泾镇人民路360号',
  朱泾镇图书馆新农分馆: '朱泾镇新农贸易路55号',
  '人文松江活动中心（松江区图书馆）': '人民南路6弄69号',
  车墩镇图书馆: '车墩镇影视路28弄1号227室',
  洞泾镇图书馆: '洞泾镇长兴路466号',
  方松街道图书馆: '北翠路1077号204室',
  九亭镇图书馆: '九亭镇易富路25号',
  泖港镇图书馆: '泖港镇新宾路300号',
  佘山镇图书馆: '佘山镇外青松公路8888弄1号',
  佘山镇佘北图书馆: '贡嘎山路200号佘北党群服务中心106室',
  石湖荡镇图书馆: '石湖荡镇育新路333号2楼',
  泗泾镇图书馆: '泗泾镇鼓浪路588号',
  泗泾新凯图书馆: '泗凯路400号',
  泗泾新凯大居图书馆: '泗泾镇城鸿路222弄',
  小昆山镇图书馆: '小昆山镇文翔路6201号1楼',
  新浜镇图书馆: '新浜镇新颖路1031号205室',
  新桥镇图书馆: '新桥镇新站路460号',
  叶榭镇图书馆: '叶榭镇张泽滟东路84号',
  永丰街道图书馆: '仓华路269弄1-4号永丰街道社区党群服务中心2楼',
  岳阳街道图书馆: '人民北路171弄30号4楼',
  中山街道图书馆: '中山街道茸梅路200号中山社区文化中心2楼',
  九里亭街道图书馆: '滨亭路355弄1号',
  广富林街道图书馆: '谷阳北路2760号三楼',
  青浦区图书馆: '青龙路60号',
  白鹤镇图书馆: '白鹤镇外青松公路2951号',
  '白鹤镇图书馆（赵屯分中心）': '青赵公路6666弄86号',
  华新镇图书馆: '华新镇新府中路1868号',
  '华新镇图书馆（凤溪分馆）': '华新镇凤强塘路1081号',
  金泽镇图书馆: '金泽镇迎祥街33号',
  练塘镇图书馆: '练塘镇文化路85号',
  夏阳街道图书馆: '青浦区青昆路100号',
  徐泾镇图书馆: '徐泾镇诚爱路58号',
  '徐泾镇图书馆（北大居分馆）': '徐泾镇尚鸿路858',
  赵巷镇图书馆: '赵巷镇赵华路507号',
  '赵巷镇图书馆（新城一站分馆）': '华科东路41号',
  '青溪书房·赵巷公园': '青浦区巷业路259号2号楼',
  重固镇图书馆: '重固镇福贸路260号',
  朱家角镇图书馆: '朱家角镇沙家埭路28号(市民中心)',
  香花桥街道图书馆: '青浦区新胜路580号',
  '香花桥街道图书馆 （玉兰花园分馆）': '香花桥街道清河湾路1635弄1号4层',
  盈浦街道图书馆: '青浦区海盈路48号',
  奉贤区图书馆: '南桥镇解放东路889号',
  奉城镇图书馆: '奉城镇奉海公路8号',
  海湾镇图书馆: '海湾镇星中路45号',
  金汇镇图书馆: '金汇镇中心路10号',
  南桥镇图书馆: '南桥镇南星路333号5楼',
  青村镇图书馆: '青村镇南明路58号',
  四团镇图书馆: '四团镇新四平公路2089号',
  柘林镇图书馆: '柘林镇新塘路286弄柘邻坊四楼',
  庄行镇图书馆: '奉贤区庄行镇腾庄路6号',
  奉浦街道图书馆: '高州路155号3楼',
  西渡街道图书馆: '奉贤区扶兰路51号201',
  金海街道图书馆: '奉贤区金海社区嘉园路254号',
  海湾旅游区图书馆: '奉炮公路141弄49号3楼',
  头桥街道图书馆: '头桥中路208号3楼',
  崇明区图书馆: '城桥镇崇明大道7897号',
  堡镇图书馆: '堡镇堡兴路85号',
  长兴镇图书馆: '海舸路465号',
  陈家镇图书馆: '陈家镇裕国路388号',
  城桥镇图书馆: '城桥镇大陈路8弄19号',
  东平镇图书馆: '东平镇东冉路886号',
  港西镇图书馆: '港西镇三双公路1573号（镇政府内）',
  港沿镇图书馆: '港沿镇港沿公路1198号',
  横沙乡图书馆: '横沙乡新环路57号',
  建设镇图书馆: '建设镇建设公路1259号',
  绿华镇图书馆: '绿华镇嘉华路8号',
  庙镇图书馆: '庙镇剧场路12号',
  三星镇图书馆: '三星镇宏海公路4291号',
  竖新镇图书馆: '竖新镇团城公路1918号',
  向化镇图书馆: '向化镇陈仿公路4927号',
  新村乡图书馆: '新村乡星村公路2128号',
  新海镇图书馆: '新海镇北沿公路3366号',
  新河镇图书馆: '新河镇新开河路877号',
  中兴镇图书馆: '中兴镇兴工路57号',
  上海浦东碧云美术馆: '浦东新区红枫路135号',
  海派连环画艺术馆: '浦东新区川沙路1058号',
  上海王狮美术馆: '浦东新区潍坊路328号',
  浦东云间美术馆: '浦东新区世纪大道100号29楼',
  周浦美术馆: '浦东新区周浦镇周邓路6851号',
  上海浦东林隐美术馆: '浦东新区祝桥镇江镇西街71号3幢',
  上海浦东新区库伯美术馆: '浦东新区沈梅路123弄57号',
  上海艺仓美术馆: '浦东新区滨江大道 4777 号',
  上海昊美术馆: '浦东新区祖冲之路2277弄1号',
  上海浦东新区联明美术馆: '浦东新区民唐路202号2幢',
  上海浦东新区叁柒贰叁美术馆: '浦东新区银城路66号2层206单元、207a单元、207b单元、208单元。',
  上海浦东新区越婷惠美术馆: '浦东新区陈春路109号一楼106B-1-2铺与115A铺',
  震旦美术馆: '浦东新区富城路99号主楼2-3层',
  上海久事美术馆: '黄浦区中山东一路27号6层、黄浦区中山东一路18号2层、黄浦区北京东路230号1层',
  春美术馆: '黄浦区福州路655号2楼',
  胡问遂艺术馆: '黄浦区福佑路199号',
  上海驰翰美术馆: '黄浦区西藏南路765号1503室',
  上海民生现代美术馆: '黄浦区威海路48号5-6F',
  'chi K11美术馆': '黄浦区淮海中路300号B3',
  上海外滩美术馆: '黄浦区虎丘路20号',
  上海复星艺术中心: '黄浦区中山东二路600号',
  华山艺术馆: '静安区延安中路955弄、巨鹿路700号',
  明当代美术馆: '静安区永和东路436号',
  心象艺术馆: '静安区汶水路40号宏慧视界BOX一号库2号楼',
  上海静安毕加索艺术馆: '静安区北京西路1394号',
  上海静安大风堂美术馆: '静安区恒丰北路100号26楼',
  上海大学美术馆: '静安区延长路149号',
  'Fotografiska 影像艺术中心': '静安区光复路127号',
  上海中国画院美术馆: '徐汇区岳阳路197号',
  上海市徐汇区艺术馆: '徐汇区淮海中路1413号',
  西岸美术馆: '徐汇区龙腾大道2600号',
  '龙美术馆（西岸馆）': '徐汇区龙腾大道3398号',
  上海油罐艺术中心: '徐汇区龙腾大道2380号',
  START星美术馆: '徐汇区瑞宁路111号',
  上海明圆美术馆: '徐汇区复兴中路1199号A座B1层',
  上海徐汇区九点水美术馆: '徐汇区桂林路406号',
  刘海粟美术馆: '长宁区延安西路1609号',
  上海油画雕塑院美术馆: '长宁区金珠路111号',
  '上海中国画院 程十发美术馆': '长宁区虹桥路1398号',
  上海虹桥当代美术馆: '长宁区仙霞路650号',
  上海正好美术馆: '长宁区番禺路300弄7号3幢',
  上海杨培明宣传画收藏艺术馆: '长宁区延安西路726号7楼K座',
  上海长宁华萃当代美术馆: '长宁区长宁路1978号',
  上海长宁王小慧艺术馆: '长宁区威宁路369号',
  '刘海粟美术馆(分馆)': '普陀区铜川路1869号',
  上海苏宁艺术馆: '普陀区丹巴路99号C3座',
  朱屺瞻艺术馆: '虹口区欧阳路580号',
  上海多伦现代美术馆: '虹口区多伦路27号',
  上海虹口青藤美术馆: '虹口区同心路1号3幢3109室',
  趣看美术馆: '虹口区四川北路939号1613单元',
  敦煌当代美术馆: '杨浦区长阳路1687号',
  鸿一美术馆: '杨浦区黄兴路1818号11F',
  刘小晴艺术馆: '杨浦区惠民路379弄9、11号',
  上海美术学院美术馆: '宝山区上大路路99号',
  上海湫光美术馆: '宝山区罗新东路800号5幢1、2楼',
  上海宝山区龙现代美术馆: '宝山区黄海路888号',
  '上海交通大学 程及美术馆': '闵行区东川路800号',
  上海海派艺术馆: '闵行区新镇路1536号',
  蔡兵美术馆: '闵行区伟业路881号',
  上海宝龙美术馆: '闵行区漕宝路3055号',
  上海明珠美术馆: '闵行区区吴中路路1588号',
  上海闵行区美博美术馆: '闵行区黎明路88号',
  上海半岛美术馆: '闵行区澄建路600号',
  中闵虹桥美术馆: '闵行区华漕镇申长北路156号',
  上海金臣亦飞鸣美术馆: '闵行区甬虹路88号',
  陆俨少艺术院: '嘉定区东大街358号',
  上海韩天衡美术馆: '嘉定区博乐路70号',
  上海秦古美术馆: '嘉定区曹安公路2888号',
  泰美术馆: '嘉定区曹安公路4058号艺河湾艺术区',
  上海嘉定区北虹桥美术馆: '嘉定区江桥镇景域大道88号13幢',
  嘉源海美术馆: '嘉定区大治路39号',
  上海嘉定十方画院: '嘉定区南翔镇解放街230号檀园内(西南门)',
  丁聪美术馆: '金山区枫泾镇青枫街49号',
  上海金山区海鸥美术馆: '金山区卫清西路55号2楼',
  云间会堂美术馆: '松江区人民南路6弄69号、人民南路26号',
  程十发艺术馆: '松江区中山中路458号',
  松江美术馆: '松江区三新北路900弄601号',
  上海松江云间美术馆: '松江区秀南街106号',
  上海艺术百代美术馆: '松江区王家厍路885弄云堡未来市艺术文创园区3号楼',
  上海YOUNG美术馆: '松江区三新北路900弄910号',
  上海松江清控人居美术馆: '松江区新桥镇新腾路9号1幢1层108室',
  上海松江区新桥美术馆: '松江区泗砖南路255弄193号',
  上海松江区贤禾美术馆: '松江区泗泾镇开江东路173号',
  上海松江云间少儿美术馆: '松江区人民北路1503号二层',
  上海国稷美术馆: '松江区泗泾镇泗陈公路 3388 弄 16 号',
  洙桥美术馆: '松江区洙桥村696号',
  余德耀美术馆: '青浦区蟠鼎路123弄8号',
  上海市鹤龙美术馆: '青浦区夏阳街道轻松路361号、青浦区朱家角镇北大街222号',
  上海青浦青渚美术馆: '青浦区北青公路7203号',
  上海青浦区金夜美术馆: '青浦区徐泾镇汇龙路168号',
  上海青浦区练塘可的美术馆: '青浦区练塘镇金前村金田路428号',
  上海吴宜恩美术馆: '奉贤区海湾旅游区海马路5818号',
  崇明美术馆: '崇明区崇明大道7897号',
  浦东新区文化艺术指导中心: '锦绣路2769号',
  浦东新区文化艺术指导中心惠南分中心: '惠南镇靖海路509号',
  浦东新区文化艺术指导中心外高桥分中心: '高桥镇慈善街69号3-4楼',
  浦东新区金海文化艺术中心: '金群路28号',
  浦东新区浦东文化馆: '南泉北路150号',
  浦东新区浦南文化馆: '杨新路61号',
  黄浦区文化馆: '中华路980号',
  徐汇区文化馆: '罗香路237号',
  长宁文化艺术中心: '仙霞路650号',
  静安区文化馆: '乌鲁木齐北路459号',
  静安区文化馆分馆: '恒丰北路98号',
  虹口区文化馆: '水电路1412号4楼',
  杨浦文化艺术中心: '中原路188号',
  普陀区文化馆: '兰溪路138号',
  '上海市闵行区文化和旅游管理事务中心 （上海市闵行区群众艺术馆）': '莘松路350号',
  金山区文化馆: '金山区蒙山北路280号',
  '人文松江活动中心（松江区文化馆）': '松江区人民南路26号',
  青浦区文化馆: '公园路78号',
  奉贤区文化馆: '南桥镇解放东路889号',
  崇明区文化馆: '城桥镇崇明大道7887号',
  周浦镇文化服务中心: '周浦镇周东路266号',
  三林镇文化服务中心: '三林路338号',
  三林镇懿德文化分中心: '和融路51号',
  三林镇前滩社区文化分中心: '芋秋路196号',
  泥城镇文化服务中心: '泥城镇鸿音路3156弄8号',
  金杨社区文化活动中心: '友林路169号',
  金杨社区文化活动中心云山路分中心: '云山路1080弄2号楼',
  唐镇文化体育中心: '顾唐路3150号',
  大团镇文化服务中心: '南团公路3330号',
  金桥镇文化服务中心: '金高路1777号',
  书院镇文化服务中心: '书院镇老芦公路861号',
  曹路镇文化服务中心: '川沙路582号',
  曹路社区文化活动中心: '民区路9号',
  曹路社区文化活动中心顾路分中心: '顾路老街110号',
  花木街道社区文化活动中心: '梅花路289号',
  川沙新镇文化服务中心: '新川路300号（总部）',
  祝桥镇文化服务中心: '祝桥镇航亭环路158号',
  惠南镇文化服务中心: '惠南镇拱秀路241号',
  新场镇文化服务中心: '新场镇新环东路276号',
  浦兴社区文化活动中心: '博兴路1473号',
  浦兴社区文化活动中心金桥湾分中心: '长岛路1280弄70号',
  高东镇文化服务中心: '高东镇光烁路39号',
  塘桥社区文化活动中心: '蓝村路86号',
  老港镇文化服务中心: '老港镇建中路458号',
  康桥镇文化服务中心: '康沈路686号',
  航头镇文化服务中心: '航头镇航鹤路388号',
  航头镇文化服务中心鹤沙分中心: '航头镇鹤韵路385号',
  '南汇新城镇社区党群服务中心（文化服务中心）': '芦硕路298号',
  陆家嘴金融城文化中心: '东昌路498弄15号',
  陆家嘴金融城文化分中心: '张杨路707号4F',
  高行镇文化服务中心: '新行路340号',
  万祥镇文化服务中心: '万祥镇万祥路101号',
  宣桥镇社区文化活动中心: '下盐公路3824号',
  周家渡街道文化中心: '齐河路508号',
  潍坊社区文化活动中心: '南泉路269号',
  上钢社区文化活动中心: '昌里路335号',
  南码头社区文化活动中心: '南码头路400号',
  洋泾社区文化活动中心: '巨野路717号',
  北蔡镇文化服务中心: '陈春路101号',
  合庆镇文化服务中心: '合庆镇东川公路7777号',
  张江镇文化服务中心: '张江镇中科路2329号',
  张江镇文化服务中心-孙桥分中心: '张江镇孙建路与孙耀路交叉口西南100米',
  沪东社区文化活动中心: '柳埠路135弄25号',
  沪东社区文化分中心: '博兴路200号2楼',
  高桥镇文化服务中心: '张杨北路5425号',
  东明社区文化活动中心: '东明路2616号',
  东明社区文化活动分中心: '凌兆路555弄20号',
  五里桥社区文化活动中心: '龙华东路600号',
  南京东路社区文化活动中心: '江阴路101号',
  打浦桥社区文化活动中心: '蒙自路223号',
  瑞金二路社区文化活动中心: '陕西南路245号',
  淮海中路社区文化活动中心: '马当路349号',
  外滩社区文化活动中心: '河南中路578号',
  小东门街道社区文化活动中心: '黄家路88弄10号',
  半淞园路社区文化活动中心: '保屯路38号',
  豫园社区文化活动中心: '傅家街65号',
  老西门社区文化活动中心: '中华路990号2-5楼',
  石门二路社区文化活动中心: '康定东路85号',
  北站街道社区文化活动中心: '天目中路383号3-5层',
  临汾社区文化活动中心: '保德路181号',
  江宁路街道社区文化活动中心: '昌平路710号',
  江宁路街道社区文化活动中心分中心: '西苏州路71号',
  '南京西路街道社区文化活动中心（福民会馆）': '富民路197弄69号',
  曹家渡街道社区文化活动中心: '万航渡路767弄56号2楼',
  静安寺街道社区文化活动中心: '新闸路1855号',
  大宁路街道社区文化活动中心: '平型关路1179号',
  彭浦镇社区文化活动中心: '灵石路745号',
  宝山路街道党群服务中心: '宝昌路533号',
  共和新路街道社区党群服务中心: '延长中路755号',
  彭浦新村街道社区文化活动中心: '彭浦新村58号',
  芷江西路街道社区文化活动中心: '芷江西路151号2楼至6楼',
  天目西路街道社区文化活动中心: '沪太路150号',
  徐家汇社区文化活动中心: '南丹东路109号',
  天平街道社区文化活动中心: '广元路153号',
  '天平街道66梧桐院(文化活动分中心)': '乌鲁木齐南路66号',
  湖南街道社区文化活动中心: '乌鲁木齐中路164号',
  '枫林街道社区党群服务中心(文化活动分中心)': '双峰路400号',
  '枫林街道天龙党群服务中心(文化活动分中心)': '中山南二路930号',
  斜土社区文化活动中心: '大木桥路461号',
  田林街道党群服务中心: '田林东路588号',
  长桥社区文化活动中心: '罗香路237号',
  虹梅街道党群服务中心: '全州路81号',
  康健街道社区党群服务中心: '浦北路988号',
  龙华社区党群中心: '龙华西路21弄80号',
  凌云街道社区文化活动中心: '梅陇路415号',
  漕河泾街道社区文化活动中心: '康健路135号',
  华泾社区文化活动中心: '华泾路505号2-5楼',
  华阳社区文化活动中心: '安化路500号',
  新泾镇社区文化事务中心: '哈密路1358号',
  北新泾社区文化活动中心: '新泾一村144号',
  天山社区文化活动中心: '天山四村122号1号楼',
  新华社区文化活动中心: '法华镇路453号',
  '仙霞社区文化活动中心（西部）': '仙霞路579弄38号',
  '仙霞社区文化活动中心（东部）': '仙霞路435弄5号',
  程家桥街道社区文化活动中心: '哈密路1955号',
  虹桥街道社区文化活动中心: '虹桥路1115弄19号',
  '虹桥街道社区文化活动中心（分中心）': '富贵东道99号',
  周家桥社区文化活动中心: '玉屏南路560弄78号',
  江苏路街道社区文化活动中心: '宣化路3号',
  长征社区文化活动中心: '梅川路1255号',
  曹杨社区文化活动中心: '杏山路317号',
  甘泉社区文化活动中心: '延长西路350号',
  长风社区文化活动中心: '枣阳路251弄100号',
  桃浦社区文化活动中心: '红棉路188号',
  真如社区文化活动中心: '兰溪路968号',
  长寿社区文化活动中心: '长寿路505弄6号新大楼',
  石泉社区文化活动中心: '宁强路33号',
  宜川社区文化活动中心: '华阴路200号',
  万里社区文化活动中心: '真金路51号',
  嘉兴路街道社区文化活动中心: '瑞虹路400号',
  嘉兴路街道社区文化活动分中心: '香烟桥路87号',
  曲阳路街道社区文化活动中心: '中山北一路998号',
  江湾镇街道社区文化活动中心: '丰镇路21号',
  欧阳路街道社区文化活动中心: '四平路621弄甲100号',
  四川北路街道社区文化活动中心: '海伦路505号',
  凉城新村街道社区文化活动中心: '车站南路340号4楼',
  北外滩街道社区文化活动中心: '通州路99号',
  广中路街道社区文化活动中心: '广中路123号',
  五角场社区文化活动中心: '政化路257号',
  五角场社区文化活动分中心: '仁德路100弄10支弄',
  大桥街道社区文化活动中心: '平凉路1730号',
  四平路街道社区文化活动中心: '抚顺路360号',
  定海路街道社区文化活动中心: '长阳路3066号',
  定海路街道社区文化活动分中心: '周家嘴路4214弄26号',
  平凉社区文化活动中心: '怀德路399号',
  长白新村街道社区文化活动中心: '延吉东路105号',
  '228街坊文化活动中心': '长白路160号228街坊4号楼',
  长海路街道社区文化活动中心: '翔殷路505弄3号',
  长海路街道社区文化活动分中心: '佳木斯路315弄7号',
  延吉社区文化活动中心: '延吉中路77号',
  江浦社区文化活动中心: '许昌路1150号',
  江浦路街道社区文化活动分中心: '辽源西路143号',
  控江路街道社区文化活动中心: '凤城二村19号',
  控江路街道社区文化活动分中心: '黄兴路566、572号3-4楼',
  殷行社区文化活动中心: '市光三村164号',
  新江湾城社区文化活动中心: '国秀路700号',
  政青路文化活动分中心: '民府路1279号',
  罗店镇社区文化活动中心: '罗店镇美诺路131号',
  罗店镇社区文化活动分中心: '塘西街366-370号',
  友谊路街道社区事务受理服务中心: '永清路899号',
  友谊路街道社区文化活动分中心: '同济路990号',
  顾村镇社区文化活动中心: '富联路368号',
  顾村镇菊泉文体中心: '菊盛路99弄70号',
  顾村镇馨佳园社区文化活动中心: '潘广路1445-1号',
  罗泾镇社区文化活动中心: '陈功路799号',
  罗泾镇社区文化活动分中心: '萧月路153号',
  吴淞街道社区文化活动中心: '淞浦路470号',
  高境镇社区文化活动中心: '高境路371号',
  高境镇社区文化活动分中心: '共康东路129号',
  杨行镇社会事业发展服务中心: '松兰路826号',
  庙行镇社区文化活动中心: '长江西路2697号',
  庙行镇社区文化活动分中心: '三泉路1501弄',
  淞南镇社区文化活动中心: '淞南镇淞发路578号',
  月浦镇社区文化活动中心: '蕰川路4051号',
  '月浦镇社区文化中心（友间公寓分中心）': '庆安路51号6号楼',
  张庙街道社区文化活动中心: '一二八纪念路728弄58号',
  大场镇社会事业发展服务中心: '沪太路2010-1号',
  虹桥镇文化体育事业发展中心: '万源路2800号',
  颛桥镇文体中心: '都市路2699号',
  江川文化馆: '鹤庆路366号',
  新虹街道社区党群服务中心: '宁虹路1122号',
  古美路街道社区党群服务中心: '平阳路258号',
  马桥景城文化中心: '富卓路120号',
  华漕镇文化体育事业发展中心: '纪翟路550号',
  莘庄工业区文化体育事业发展中心: '莘庄工业区颛盛路745号',
  浦江镇社区文化活动中心: '浦涛路252号',
  浦江镇青少年社区文化活动中心: '永寨路375号',
  浦江镇瑞和社区文化活动中心: '鲁坤路359号',
  吴泾镇社区文化活动中心: '龙吴路5533号',
  莘庄镇文化体育事业发展中心: '龙茗路128号',
  七宝镇文化体育事业发展中心: '沪松公路450号',
  '七宝体育活动中心（航华分中心）': '航新路228号',
  闵行区梅陇镇文化体育事业发展中心: '高兴路108号',
  '浦锦街道社区党群服务中心（文化体育）': '浦锦街道浦锦路400号',
  嘉定镇社区党群服务中心: '清河路196号',
  外冈镇文化体育服务中心: '外冈镇中泉路76号',
  菊园新区社区文化活动中心: '棋盘路1255号',
  新成路街道社区党群服务中心: '仓场路335号',
  南翔镇文化体育服务中心: '古猗园路737号',
  华亭镇社区文化活动中心: '嘉行公路3198号',
  真新街道社区党群服务中心: '真新街道新郁路755弄55号',
  徐行镇文化体育服务中心: '新建一路1568号',
  江桥镇社区文化活动中心: '江桥镇华江路129弄1号楼',
  嘉定工业区文化体育服务中心: '汇源路188号',
  马陆镇文化体育服务中心: '宝安公路3322号',
  安亭镇文化体育服务中心: '墨玉路621号',
  安亭镇文化体育服务中心黄渡分中心: '博园路4800号',
  安亭镇文化体育服务中心方泰分中心: '嘉松北路4355弄88号',
  朱泾镇社区文化活动中心: '朱泾镇人民路360号',
  朱泾镇社区文化活动中心新农分中心: '朱泾镇新农贸易路55号',
  山阳镇社区党群服务中心: '山阳镇体育路53号',
  漕泾镇社区党群服务中心: '漕泾镇富漕路239号',
  枫泾镇社区党群服务中心: '枫泾镇枫丽路147号',
  枫泾镇社区文化活动中心兴塔分中心: '兴塔社区兰兴路100弄2216号',
  吕巷镇社区党群服务中心: '朱吕公路6858号',
  亭林镇社区文化活动中心: '亭林镇亭升路550弄33号',
  亭林镇社区文化活动中心松隐分中心: '亭林镇亭枫公路1919号',
  高新区社区文化活动中心: '恒顺路280弄35号',
  金山卫镇社区党群服务中心: '金山卫镇古城路295号',
  金山卫镇社区文化活动中心钱圩分中心: '金山卫镇钱圩建圩路20弄38号',
  廊下镇社区党群服务中心: '廊下镇景钱路1708号',
  张堰镇社区党群服务中心: '张堰镇东贤路961号',
  石化街道社区党群服务中心: '象州路238号',
  方松社区文化活动中心: '北翠路1077号',
  '中山街道社区党群服务中心（中山幸福里）': '沪松路255弄18号',
  永丰街道社区党群服务中心: '仓华路269弄1-4号',
  佘山镇社区文化活动中心: '外青松公路8888弄',
  佘山镇社区文化活动中心佘北分中心: '贡嘎山路200号',
  泗泾镇社区文化活动中心: '鼓浪路588号',
  泗泾镇新凯社区文化活动中心: '泗凯路400号',
  九亭镇社区文化活动中心: '易富路25号',
  新浜镇社区文化活动中心: '新浜镇新颖路1031号',
  车墩镇社区文化活动中心: '车墩镇影视路28弄1号楼',
  岳阳街道社区党群服务中心: '人民北路171弄30号',
  叶榭镇社区文化活动中心: '叶榭镇滟东路84号',
  广富林街道社区文化活动中心: '文翔路3588弄41号',
  洞泾镇社区文化活动中心: '长兴路466号',
  新桥镇社区党群服务中心: '新桥镇新站路460号',
  九里亭街道社区党群服务中心: '九里亭街道滨亭路355弄1号',
  石湖荡镇社区文化活动中心: '育新路333号',
  泖港镇社区文化活动中心: '泖港镇新宾路300号',
  小昆山镇社区党群服务中心: '小昆山镇文翔路6201号',
  徐泾社区文化活动中心: '诚爱路58号',
  徐泾北大居社区文化活动分中心: '徐泾镇尚鸿路858号',
  练塘镇社区文化活动中心: '文化路85号',
  '练塘镇社区文化活动中心（小蒸分中心）': '小蒸社区三官桥路128号',
  '练塘镇社区文化活动中心（蒸淀分中心）': '蒸淀社区蒸发路88号（街心公园内）',
  白鹤镇社区文化活动中心: '外青松公路2953号',
  '白鹤镇社区文化活动中心（赵屯分中心）': '青赵公路6666弄86号',
  朱家角镇社区文化活动中心: '河畔路49号',
  朱家角镇沈巷社区文化活动中心: '沈巷泖溪路51号',
  重固镇社区文化活动中心: '福贸路260号',
  华新镇文化体育服务中心: '新府中路1868号',
  '凤溪社区文化体育服务中心（凤溪分中心）': '凤强塘路1081号',
  赵巷镇社区文化活动中心: '赵巷镇赵华路507号',
  赵巷镇新城一站大居社区文化体育服务中心: '华科东路41号',
  金泽镇社区文化活动中心: '青浦区金泽镇迎祥街33号',
  金泽镇社区文化活动服务中心商榻分中心: '金泽镇商前路2001号',
  盈浦街道社区文化活动中心: '青浦区海盈路48号',
  夏阳街道社区文化活动中心: '青浦区青昆路100号',
  香花桥街道社区文化活动中心: '新胜路580号',
  '香花桥街道清河湾U365党群服务中心（社区文化活动分中心）': '清河湾路1635弄1号3-4层',
  金汇镇社区文化活动中心: '金汇镇中心路10号',
  金汇镇社区文化活动中心泰日分中心: '金汇镇泰青公路231号',
  徐里桥社区文化活动中心: '清朗路298号',
  青村镇社区文化活动中心: '青村镇南明路58号',
  青村镇社区文化活动中心钱桥分中心: '青村镇振水路40号',
  柘林镇社区文化活动中心: '柘林镇新塘路286弄',
  庄行镇社区文化活动中心: '庄行镇腾庄路6号',
  '庄行镇社区文化活动中心（邬桥分中心）': '大叶公路2675号',
  四团镇社区文化活动中心: '四团镇新四平公路2089号',
  海湾镇社区文化活动中心: '海湾镇星中路45号',
  奉城镇社区文化活动中心: '奉城镇奉海公路8号',
  金海街道社区文化活动中心: '嘉园路254号',
  海湾旅游区社区文化活动中心: '奉炮公路141弄49号',
  奉浦街道社区文化活动中心: '高州路155号',
  西渡街道社区文化活动中心: '扶兰路51号',
  头桥街道社区文化活动中心: '头桥中路208号',
  竖新镇社区文化活动中心: '竖新镇团城公路1918号',
  横沙乡社区党群服务中心: '横沙乡新环路57号',
  建设镇社区党群服务中心: '建设公路1259号',
  堡镇社区文化活动中心: '堡镇正大街118号',
  港西镇社区党群服务中心: '港西镇三双公路1573号',
  港沿镇社区党群服务中心: '港沿公路1198号',
  东平镇社区文化活动中心: '东冉路886号',
  绿华镇社区文化活动中心: '嘉华路8号',
  新海镇社区文化活动中心: '新海镇北沿公路3366号',
  新村乡社区党群服务中心: '新村乡星村公路2128号',
  新河镇社区党群服务中心: '新河镇新开河路877号',
  中兴镇社区文化活动中心: '中兴镇兴工路57号',
  三星镇社区文化活动中心: '宏海公路4291号',
  '城桥镇社区党群服务中心 （城桥镇文体服务中心）': '城桥镇大陈路8弄19号',
  庙镇社区文化活动中心: '庙镇剧场路12号',
  陈家镇社区文化活动中心: '陈家镇裕国路388号',
  长兴镇社区党群服务中心: '长兴镇海舸路465号',
  向化镇社区文化活动中心: '向化镇陈彷公路4927号',
  上海黄浦剧场有限公司: '上海市北京东路780号',
  '上海黄浦剧场有限公司（小剧场）': '上海市北京东路780号',
  上海木偶剧团有限公司: '上海市南京西路388号五楼',
  '上海木偶剧团有限公司（小剧场）': '上海市南京西路388号五楼',
  上海新光影艺苑有限公司: '上海市黄浦区宁波路586号',
  上海共舞台有限公司: '延安东路433号',
  上海中国大戏院有限公司: '上海市黄浦区牛庄路704号',
  上海市卢湾体育中心: '肇嘉浜路128号',
  '上海儿童国际文化发展有限公司（上海儿童艺术剧场-黑匣子剧场）': '上海市黄浦区苗江路800号',
  '上海儿童国际文化发展有限公司（上海儿童艺术剧场-中心剧场）': '上海市黄浦区苗江路800号',
  '上海儿童国际文化发展有限公司（上海儿童艺术剧场-小剧场）': '上海市黄浦区苗江路800号',
  上海大剧院-大剧场: '人民大道300号',
  上海大剧院-中剧场: '人民大道300号',
  上海大剧院-小剧场: '人民大道300号',
  上海音乐厅小剧场: '黄浦区延安东路523号',
  上海天蟾逸夫舞台: '黄浦区福州路701号',
  上海兰心大戏院: '茂名南路57号',
  上海人民大舞台: '九江路663号',
  上海文化广场剧院管理有限公司: '永嘉路36号',
  '上海市黄浦区文化馆（上海市雅庐书场）-白玉兰剧场': '重庆南路308号',
  '上海市黄浦区文化馆（上海市雅庐书场）-雅庐书场': '重庆南路308号',
  '上海长江剧场（红匣子）': '上海市黄浦区黄河路35号',
  '上海长江剧场（黑匣子）': '上海市黄浦区黄河路35号',
  上海豫尚文化传播有限公司: '上海市黄浦区文昌路10号4楼A',
  '上海话剧艺术中心有限公司黄浦分公司（茉莉花剧场）': '上海市黄浦区北海路247号1幢',
  上海八佰秀企业管理有限公司: '常德路800号8幢101室',
  上展中心剧院: '延安中路1000号',
  上海小伙伴剧场: '延安西路64号11幢4层、5层',
  上海尚演文化投资管理有限公司: '北京西路1013号',
  上海戏剧学院: '华山路630号',
  文艺会堂: '延安西路200号',
  '兰馨影业有限公司-光影车间.静剧场': '乌鲁木齐北路459号3幢101室',
  '中国福利会儿童艺术剧院(马兰花剧场)': '华山路643号',
  静安体育中心: '汶水路116号',
  上戏实验剧院: '华山路630号',
  云峰剧院: '北京西路1700号',
  上海美琪大戏院: '江宁路66号',
  上海马戏城有限公司: '共和新路2266号',
  上海商城有限公司: '南京西路1376号',
  '上海市闸北区宋园茶艺馆（书场）': '共和新路1667号',
  海上文化管理中心-大宁剧院: '平型关路1220号',
  上海铁路工人文化宫: '虬江路1150号',
  上海市沪北电影院有限责任公司: '洛川东路500号',
  上海艺海剧场: '江宁路466号',
  上海话剧艺术中心-艺术剧院: '安福路288号',
  上海话剧艺术中心-戏剧沙龙: '安福路288号',
  上海话剧艺术中心-D6空间: '安福路288号',
  上海大戏院: '复兴中路1186号1幢',
  上海交响乐团音乐厅: '复兴中路1380号',
  徐汇区田林街道社区文化活动中心: '田林东路588号',
  上音歌剧院: '汾阳路6号',
  上海东亚体育文化中心有限公司: '天钥桥路666号',
  上海大舞台: '漕溪北路1111号',
  上海表坊文化发展有限公司-上剧场: '徐汇区美罗城5楼',
  上海市宛平艺苑: '中山南二路859号',
  虹口足球场: '东江湾路444号',
  上海摩登嘉旋文化发展有限公司: '瑞虹路188号309、310、507室',
  虹口区曲阳文化馆: '曲阳路570号',
  '1933微剧场': '沙泾路10号1号楼447幢201室',
  虹口区工人文化宫: '飞虹路528号',
  上海丝芭文化传媒有限公司-星梦剧场: '嘉兴路267号1楼A区',
  精武体育馆: '东体育会路715号',
  上海泛景文化传播有限公司-珍珠剧场: '乍浦路471号',
  上海盈寰文化传媒有限公司-BlueNote: '四川北路867号301室',
  上海虹口保利大剧院管理有限公司-北外滩友邦大剧院: '东大名路889号',
  上海市长宁民俗文化中心: '天山西路201号',
  上海市长宁文化艺术中心: '仙霞路650号',
  上海国际舞蹈中心剧场经营管理有限公司: '虹桥路1650号',
  上海东虹桥剧院管理有限公司: '天山路888号1层—C',
  江川剧场: '江川路344号三层',
  上海新东苑实业有限公司: '金光路225号第3层',
  新浦江影剧院: '浦江镇谈家港叶家桥路288号',
  旗忠森林体育城: '光华路2118号C-117',
  吴泾文化馆: '龙吴路5533号',
  上海城市剧院管理有限公司: '都市路4889号',
  上海零聚演出经纪有限公司: '七莘路1366号2幢201、203室',
  '索石文化传播（上海）有限公司': '七莘路1366号2幢211室',
  上海零湾美琪剧院管理有限公司: '虹梅南路5669号',
  上海市青浦区文化馆: '公园路78号',
  青浦区赵巷镇文化中心站: '赵巷镇赵中路28号',
  青浦重固影剧院: '重固镇通波塘西街28号',
  青浦朱家角影剧院: '朱家角镇新溪路18号',
  练塘影剧院: '练塘镇练新路99号',
  上海虹馆文化发展有限公司: '崧泽大道333号EH馆',
  上海释乐文化传播有限公司: '崧文南路169弄27号301室',
  上海市优演剧场管理有限公司: '嘉松中路6200号1幢3层-A-001、002、003',
  '青隐（上海）文化艺术发展有限公司': '朱家角镇课植园路599弄36号',
  上海乐演优你科技有限公司: '青浦区徐泾镇崧泽大道2229弄66号L3-13',
  YOUNG剧场-大剧院: '控江路1155号',
  YOUNG剧场-小剧院: '控江路1155号',
  东宫剧院: '平凉路1500号',
  上海国际时尚中心园区管理有限公司: '杨树浦路2866号',
  梅赛德斯-奔驰文化中心: '世博大道1200号',
  梅赛德斯-奔驰文化中心-音乐俱乐部: '世博大道1200号',
  南汇海东影剧院: '东海镇盐朝公路869号',
  上海南汇周浦影剧场: '周浦镇年家浜路341号',
  南汇宣桥镇影剧院: '宣桥镇六奉公路236号',
  上海艺晟文化传播有限公司: '航头镇航鹤路388号B幢',
  上海浦东新区三墩影剧院: '大团镇洪通路41号',
  上海浦东新区川沙影剧院: '川沙镇新川路400号',
  南汇盐仓影剧院: '祝桥镇沿路街53号',
  上海浦东新区东方电影院有限公司: '惠南镇人民西路2号',
  上海市浦东新区航头镇书场茶馆: '航头镇镇下沙街163号',
  南汇三灶影剧院: '浦东新区三灶镇',
  上海市南汇大团镇永春演艺厅: '大团镇永春东路100号二楼',
  上海市南汇航头镇陶园春演艺厅: '航头镇下沙街227号',
  上海尚银东艺数字影城管理有限公司: '浦东新区华佗路280弄31号',
  上海兰馨影业有限公司: '张杨路400号',
  上海市澧溪文化艺术有限公司: '周东路266号西一楼',
  上海野生动物园发展有限公司: '宣桥镇南六公路178号',
  上海证大喜马拉雅演艺有限公司: '芳甸路1188弄1号',
  '保利尚悦湾（上海）剧院管理有限公司1862时尚艺术中心': '滨江大道1777号',
  上海东方艺术中心管理有限公司-音乐厅: '丁香路425号',
  上海东方艺术中心管理有限公司-歌剧厅: '丁香路425号',
  上海东方艺术中心管理有限公司-演奏厅: '丁香路425号',
  上海笋馨文化传媒有限公司: '新场镇新环东路276号',
  上海冉旭文化娱乐中心: '惠南镇川南奉公路6193号',
  上海张江文化控股有限公司-张江戏剧谷: '张江路69号',
  '上海世博中心有限公司(红厅）': '世博大道1500号',
  迪士尼-大剧院: '申迪西路255弄800号',
  '迪士尼-凡迭戈剧院、林间剧场、故事舞台': '申迪西路255弄140号、305号、401号',
  上海浦东新区三林影剧院: '杨思镇杨新路60号',
  上海宋城世博演艺发展有限公司-千古情: '世博大道1750号',
  上海宋城世博演艺发展有限公司-百乐门: '世博大道1750号',
  上海外高桥文化传播有限公司: '张杨北路3207号',
  '信德前滩（上海）文化置业有限公司': '浦东新区高青西路777号',
  上海乐来乐好剧院管理有限公司: '华池路10号1层140室',
  上海市奉贤区机关服务中心: '解放东路928号',
  上海邬桥牡丹影剧院: '大叶公路259号',
  奉贤区南桥影剧院: '南桥镇南桥路333号',
  上海胡桥影剧院: '柘林镇胡桥社区文化路45号',
  上海柘林影剧院: '柘林新街（钦林北路31号）',
  上海奉贤钱桥影剧院: '钱桥社区文化路8号',
  奉贤县青村文化站: '青村镇西街5号（人民路15号）',
  '上海九棵树文化传媒有限公司—大剧场': '树桓路99号',
  '上海九棵树文化传媒有限公司—小剧场': '树桓路99号',
  '上海九棵树文化传媒有限公司—实验剧场': '树桓路99号',
  '上海九棵树文化传媒有限公司—森林剧场': '树桓路99号',
  '上海九棵树文化传媒有限公司—水岸舞台': '树桓路99号',
  依弘剧场: '蕰川路6号30幢',
  上海星轶思达爱斯影院管理有限公司: '沪太路1933号[K]区2层202',
  上海保利大剧院: '白银路159号',
  嘉定影剧院有限责任公司: '城中路149号',
  开心麻花剧场: '陈翔公路2299号3层03-33、03-34',
  上海市崇明影剧院: '崇明城内八一路488号',
  崇明县沪剧团: '城桥镇川心街1号',
  上海风瀛洲文化传播有限公司: '城桥镇八一路488号2幢',
  海昌海洋公园-欢乐剧场: '临港新片区银飞路167号',
  海昌海洋公园-海豚表演场: '临港新片区银飞路166号',
  海昌海洋公园-大型动物表演场: '临港新片区银飞路168号',
  泥城影剧院: '泥城镇鸿音路3156弄8号',
  万祥影剧院: '万祥镇万祥路101号',
  '上海聆海美琪文化艺术发展有限公司（临港演艺中心）': '临港演艺中心',
  '上海展博置业有限公司（滴水湖剧院）': '临港新片区环湖西一路91号',
  上海保利云间剧院管理有限公司: '上海市松江区人民南路6弄69号-2',
  '武汉市群众艺术馆（武汉市非物质文化遗产保护中心）': '武汉市江岸区合作路15号',
  武汉中共中央机关旧址纪念馆: '武汉市江岸区胜利街163',
  武汉汉剧院: '湖北省武汉市江汉区北湖正街16号',
  '武汉博物馆（武汉市文物交流中心）': '湖北省武汉市江汉区青年路373号',
  八七会议会址纪念馆: '武汉市江岸区鄱阳街139号',
  '八路军武汉办事处旧址纪念馆（汉口新四军军部旧址纪念馆）': '武汉市江岸区长春街57号',
  '武汉京剧院有限责任公司(武汉京剧院)': '武汉市江汉区北湖正街16号',
  汉阳陵博物馆: '陕西省西安市咸阳市国际机场专用公路东段',
  西安半坡博物馆: '西安市半坡路155号',
  西安大唐西市博物馆: '陕西省西安市莲湖区劳动南路118号',
  西安事变纪念馆: '陕西省西安市碑林区建国路69号',
  八路军西安办事处纪念馆: '陕西省西安市新城区北新街七贤庄1号',
  西安唐皇城墙含光门遗址博物馆: '西安市甜水井大街含光门内广场',
  临潼区博物馆: '陕西省西安市临潼区环城东路1号',
  西安中国书法艺术博物馆: '西安市自强东路585号',
  '汉长安城遗址长乐宫四、五号遗址陈列馆': '西安市未央区罗高路罗家寨汉长安城遗址内',
  丰镐遗址车马坑陈列馆: '陕西省西安市长安区马王镇沣镐中路10号',
  华清池唐华清宫御汤遗址博物馆: '华清路3号',
  西安市长安区杜甫纪念馆: '韦曲街办双竹村',
  西安市长安民居博物馆: '王曲街办马厂村',
  西安市临潼区扁鹊纪念馆: '临潼区代王街办庞岩村',
  仙游寺博物馆: '马召镇金盆水库北梁',
  蓝田县蔡文姬纪念馆: '蓝田县工业园区文姬路中段',
  周至博物馆: '周至县县城中心街云塔十字南',
  葛牌镇区苏维埃政府纪念馆: '蓝田县葛牌镇葛牌街中段',
  陕西科学技术馆: '西安市新城区东新街252号',
  高陵区博物馆: '高陵区鹿苑街道昭慧广场',
  汉长安城遗址陈列馆: '陕西省西安市未央区邓六路与丰景路十字向南',
  西北大学博物馆: '太白北路229号',
  陕西师范大学博物馆: '西安市长安区西长安街620号',
  西安建筑科技大学校史馆: '陕西省西安市碑林区雁塔路中段13号',
  西安建筑科技大学贾平凹文学艺术馆: '陕西省西安市碑林区建设路附近',
  西安市长安博物馆: '文苑中路长安文化中心',
  长安大学地质博物馆: '雁塔路126号长安大学本部东院地学科技大厦负一层至二层',
  西安市秦阿房宫遗址博物馆: '陕西省西安市长安区西宝公路南50米',
  西安关中民俗艺术博物院: '西安市长安区五台古镇南五台山路1号',
  西安经文牛文化陶瓷博物馆: '西安市未央区朱宏路与北二环西北角汉城湖大风阁负一层',
  陕西元阳文化博物馆: '陕西省西安市碑林区顺城南路中段33号',
  西安大明宫陶瓷艺术博物馆: '西安市自强东路585号',
  陕西体育博物馆: '陕西省西安市雁塔区丈八东路303号',
  西安海棠职业学院中医美容博物馆: '陕西省西安市灞桥区弘知路西150米',
  西安工程大学纺织服装博物馆: '西安市临潼区陕鼓大道58号',
  秦二世陵遗址博物馆: '西安市曲江池南路252号',
  陕西汉唐石刻博物馆: '陕西省西安市未央区沣东新城沣东大道东段2196号 沣东自贸新天地西里',
  西安皇家艺术博物馆: '汉城街道办西查村北1号（石化大道）',
  陕西亮宝楼艺术博物馆: '西安市雁塔区雁引路35号',
  西安美都博物馆: '未央宫街办丰景路中段（汉长安城遗址保护区内）',
  西安秦砖汉瓦博物馆: '雁翔路南端',
  西安于右任书法艺术博物馆: '群贤路6号',
  陕西万达博物院: '西安市雁塔区林带路唐苑盆景园艺博览园之内',
  蓝田水陆庵壁塑博物馆: '蓝田县普化镇杨斜村',
  陕西唐三彩艺术博物馆: '西安市碑林区南二环东段559号8楼',
  西安户邑民间艺术博物馆: '芙蓉西路99号唐市街区A2',
  西安曲江艺术博物馆: '西安市曲江新区慈恩路66号A门',
  西安曲江富陶国际陶艺博物馆: '西安市雁塔区大唐芙蓉园南门唐市西曲馆23号',
  西安毛泽东敬览馆: '雁塔区长鸣路68号',
  西安于右任故居纪念馆: '书院门52号',
  西安雪花啤酒博物馆: '经开区凤城十二路99号',
  西安源浩华藏博物馆: '西安市曲江新区大唐不夜城唐城墙遗址公园内',
  西安健康博物馆: '陕西省西安市雁塔区西影路178号附近',
  西安唐都新碑林艺术博物馆: '大明宫国家遗址公园南宫墙西侧',
  西安大华博物馆: '西安市新城区太华南路251号',
  西安锦业美术博物馆: '高新区锦业路76号',
  西安曲江大玉坊博物馆: '西安市临潼区骊苑小区4号楼7层',
  西安柴窑文化博物馆: '西安市雁塔区曲江新区雁南二路开元广场西侧仿古城墙',
  大明宫国家遗址公园考古探索中心: '西安市自强东路585号',
  大明宫国家遗址公园丹凤门遗址博物馆: '陕西省西安市新城区自强东路585号',
  西安高陵钱币博物馆: '高陵区榆楚泾惠8路陕汽重卡发运中心五楼',
  西安高陵奇石博物馆: '高陵区桑军大道与310国道交汇处西安高陵奇石博物馆',
  高陵祥顺博物馆: '高陵区南新街226号',
  蓝田猿人遗址博物馆: '蓝田县九间房镇公王村公王岭',
  陕西钱币博物馆: '陕西省西安市雁塔区高新区高新路49号',
  临潼区鸿门宴博物馆: '新丰街道办事处鸿门宴堡2号',
  西安市青龙寺遗址博物馆: '陕西省西安市雁塔区西影路铁炉庙村北1号',
  空军军医大学口腔医学博物馆: '西安市新城区长乐西路145号',
  西安交通大学博物馆: '西安市咸宁西路28号(西安交通大学兴庆校区校园西南角)',
  高陵区防震减灾科普馆: '高陵区一中路362号',
  西安浐灞生态区城建博物馆: '浐灞大道1号浐灞商务中心',
  汪锋故居纪念馆: '蓝田县九间房镇街子村',
  西安市高家大院古典服饰博物馆: '西安市莲湖区北院门142号',
  西安市新美域和镜博物馆: '陕西省西安市碑林区南门里',
  西安市曲江红色记忆博物馆: '翠华南路808号科泰大厦',
  西安市大唐青铜镜博物馆: '西安市高新区丈八二路31号2栋7单元70117',
  西安市雅观陶瓷艺术博物馆: '西安市未央区北二环中段669号',
  西安市非物质文化遗产博物馆: '陕西省西安市碑林区文艺北路甲字1号',
  西安美术学院美术博物馆: '陕西省西安市雁塔区西安美术学院贰号教学楼',
  西安市贾平凹文学艺术博物馆: '曲江新区芷阳三路9号',
  起良蔡侯纸博物馆: '西安市高新区九峰镇起良村',
  西安市蓝田玉文化博物馆: '蓝田县焦岱镇焦岱街石艺园',
  西安市水墨长安艺术博物馆: '西安市灞桥区柳雪路996号',
  西安市荞麦园美术博物馆: '西安市含光南路100号',
  西安市曲江丝路遗珍博物馆: '西安市曲江新区大唐芙蓉园紫云楼四楼',
  西安市明清皮影艺术博物馆: '陕西省西安市雁塔区当代戏剧中心3层',
  长安大学公路交通博物馆: '西安市未央区长大南路356号',
  西安音乐学院艺术博物馆: '陕西省西安市雁塔区长安中路108号',
  西安汉风水务博物馆: '西安市未央区二环北路西段汉城湖景区内',
  西安市城市记忆博物馆: '幸福南路109号老钢厂设计创意产业园一号楼',
  西安市圣普美术博物馆: '西安市自强东路585号',
  陕西明善博物馆: '陕西省咸阳市秦都区水井路',
  秦咸阳宫遗址博物馆: '陕西省咸阳市渭城区窑店镇牛羊村北',
  唐华清宫梨园遗址博物馆: '陕西省西安市临潼区华清路38号华清池',
  秦都区沙河古桥遗址博物馆: '陕西省咸阳市秦都区西咸新区沣西新城钓台街',
  楼增良红木雕刻艺术博物馆: '陕西省西咸新区空港新城保税区十路以西',
  西安市曲江第二小学儿童博物馆: '西安市雁塔区曲江新区雁翔路4050号',
  西安建筑科技大学中国音乐史博物馆: '高新区草堂镇西安建筑科技大学草堂校区学府城16号楼',
  西安市中国古琴博物馆: '西安市沣东新城沣河东路818号',
  西安市新梦想影业博物馆: '西安市雁塔区朱雀大街南段12号城市立方5楼',
  西安市新源民俗艺术博物馆: '西安市高陵区通远街办史喻六组',
  西安市德江陶瓷模范标本博物馆: '灞桥区狄寨街狄寨 北路白鹿仓白家大院内',
  西安市团结民俗博物馆: '陕西省西安市未央区团结村三组甲字1号',
  西安市惟德玉文化博物馆: '陕西省西安市沣东新城三桥街办西安车辆厂生活区二期东2号',
  交大西迁博物馆: '西安市咸宁西路28号',
  西安红色体育博物馆: '经开区凤城八路鼎正大都城',
  陕西科技大学中国轻工业博物馆: '西安市未央区大学生陕西科技大学校内',
  西安交通大学附属中学博物馆: '陕西省西安市雁塔区雁翔路99号',
  西安市高陵区西北人民革命大学旧址博物馆: '通远街办环镇北路（高陵职校院内）',
  西安市吉兆春皮肤医药博物馆: '西安市高陵区中小企业聚集园C-4,5楼',
  西安市太乙面食文化博物馆: '长安区太乙宫新一村美满区',
  军用航空科技博物馆: '陕西省西安市灞桥区霸陵路1号',
  西安市城市影像博物馆: '西安市科技路西安大都荟',
  西安市石仟佛造像艺术博物馆: '慈恩西路69号',
  西安市古陶瓷博物馆: '灞桥区电厂南路8号',
  西安市羊文化博物馆: '西安市雁塔区雁翔路93号',
  西安市太和医室博物馆: '西安市碑林区兴庆宫公园花萼相辉楼',
  西安市瑛煌关中婚俗文化博物馆: '西安市鄠邑区甘亭街道草堂路438号',
  西安市云之翼航空博物馆: '高新集贤产业园',
  西安市和璞玉文化博物馆: '长安区神舟三路239号',
  西安市沣峪口老油坊博物馆: '长安区滦镇街办西留堡村',
  西影电影博物馆: '西影路508号',
  西安市黄土画派博物馆: '雁塔区朱雀大街132号阳阳国际',
  西安市民俗博物馆: '西安市新城区昌仁里3号',
  西安市鄠邑区非物质文化遗产博物馆: '西安市鄠邑区人民路',
  '临潼区文物管理委员会办公室（区文物稽查队）': '临潼区健康北路文化综合楼1楼',
  姜寨遗址文物管理所: '临潼区健康北路文化综合楼2楼',
  康家白家遗址文物管理所: '临潼区健康北路文化综合楼2楼',
  区博物馆: '临潼区环城东路1号',
  扁鹊纪念馆: '临潼区代王街办南陈村陈东组',
  鸿门宴博物馆: '临潼区新丰街办鸿门宴路1号',
  秦东陵文物管理所: '临潼区斜口街办韩峪村',
  西段遗址文物管理所: '临潼区人民南路37号映登大楼9楼',
  五星街天主教堂: '西安市莲湖区五星街17号',
  西安和平电影院: '西安市莲湖区北大街175号',
  北院门144号民居: '西安市莲湖区北院门144号',
  西安人民剧院: '西安市莲湖区北大街41号',
  大皮院清真寺: '西安市莲湖区大皮院108号',
  西安市广仁寺: '西安市莲湖区西北一路152号',
  小皮院清真寺: '西安市莲湖区小皮院28号',
  '雷神庙·万阁楼': '西安市莲湖区糖坊街83号',
  化觉巷232号: '西安市莲湖区化觉巷232号',
  小学习巷营里寺: '西安市莲湖区小学习巷86号',
  北广济街清真寺: '西安市莲湖区北广济街83号',
  原市长楼: '西安市莲湖区北院门159号',
  原市政府礼堂: '西安市莲湖区北院门159号',
  西五台: '西安市莲湖区洒金桥162号',
  大麦市街38号民居: '西安市莲湖区大麦市街38号',
  '西安高家大院古典 服饰博物馆': '西安市莲湖区北院门144号',
  '西安于右任书法 艺术博物馆': '西安市莲湖区群贤路6号',
  '陕建集团总公司 办公楼': '西安市莲湖区北大街199号',
  任家庄门楼: '西安市莲湖区劳动北路',
  '西安市鄠邑区文物管理所 （西安市鄠邑区钟楼博物馆）': '西安市鄠邑区东西南北四街交汇处',
  西安市华夏匾额博物馆: '西安市鄠邑区余下街办丝路国际雕塑文化艺术园内',
  西安市鄠邑区公输堂小木作艺术博物馆: '西安市鄠邑区渭丰镇祁村南堡中部',
  西安新梦想影业博物馆: '朱雀大街南段城市立方5层',
  临潼区文化馆: '临潼区健康北路文化综合楼',
  临潼区图书馆秦陵社区分馆: '临潼区万年路与秦陵北路交叉处（秦陵社区办公区一楼）',
  临潼区图书馆骊阅分馆: '临潼区西关正街骊阅城市书房四楼（铁一处对面）',
  红25军军部旧址: '蓝田县葛牌镇葛牌街村',
  '秦始皇陵（部分）': '临潼区秦陵街办',
  '华清宫遗址（部分）': '临潼区骊山街办华清路38号',
  西安事变旧址-华清池五间厅: '临潼区骊山街办华清路38号华清宫内',
  '秦东陵（部分）': '临潼区斜口街办韩峪村',
  五凤遗址: '鄠邑区蒋村街道五凤村',
  天池寺塔: '长安区太乙宫',
  清华山石窟: '长安区滦镇青华山',
  楼观台: '周至县楼观镇东楼村',
  老子墓: '周至县楼观镇西楼村',
  宗圣宫遗址: '周至县楼观镇东楼村',
  傥骆道遗址周至段: '周至县骆峪镇骆峪村—厚畛子镇',
  佛坪厅故城: '周至县厚畛子乡镇老县城村',
  泥峪石门遗址: '周至县竹峪镇泥峪河村',
  王氏宗祠: '周至县竹峪镇兰梅塬村',
  化羊庙: '高新区庞光镇化羊村',
  草堂寺: '高新区草堂镇',
  鼎湖延寿宫遗址: '蓝田县焦岱镇焦岱村三组西南、张家村北侧',
  汤峪栈道遗址: '蓝田县汤峪镇汤一村',
  锡水洞遗址: '蓝田县辋川镇锡水村',
  葛牌革命旧址: '蓝田县葛牌镇',
  汪锋故居及墓园: '蓝田县九间房镇街子村',
  香洲区图书馆: '香洲区健民路868号香山文化艺术中心（香洲区图书馆）',
  香洲区博物馆: '香洲区南屏镇东大街一巷2号',
  珠海市盛宝博物馆: '香洲区吉大路2号珠海德翰大酒店二楼',
  珠海汉东博物馆: '香洲区翠景路229号兴隆大厦旁',
  珠海钰海博物馆: '香洲区九洲大道1009号钰海环球金融中心37楼',
  珠海市普济艺术博物馆: '香洲区金凤路1888号珠海普陀寺内',
  罗西尼钟表博物馆: '高新区科技六路68号',
  珠海市原道文化博物馆: '横琴新区仁山路188号1栋',
  横琴粤澳深度合作区富华紫檀博物馆: '横琴新区横琴大道仁山路99号1号楼',
  珠海市古元美术馆: '香洲区梅华东路388号',
  斗门区体育馆: '斗门区井岸镇西堤路2017号',
  斗门体育馆: '斗门区井岸镇西堤路2017号',
  斗门全民健身中心: '斗门体育馆旁（格力广场）',
  金湾全民健身广场: '金湾区航空新城',
  横琴镇全民健身广场: '横琴新区永兴街旁',
  唐家湾镇全民健身广场: '高新区港湾大道唐家第二工业区旁（远大美域小区对面）',
  南水镇全民健身广场: '高栏港区南水镇文化中心广场',
  平沙镇全民健身广场: '高栏港区平沙镇美平广场',
  桂山镇全民健身广场: '万山区桂山镇文天祥广场',
  担杆镇全民健身广场: '万山区担杆镇外伶仃岛文化中心广场',
  '万山镇全民健身广场（大万山岛）': '万山区大万山岛',
  '万山镇全民健身广场（东澳岛）': '万山区东澳岛'
};

// 按城市分组区县（自动生成，按人口降序）
const districtsByCity = {
  shenzhen: ['全部区县', '宝安区', '龙岗区', '龙华区', '南山区', '福田区', '罗湖区', '光明区', '坪山区', '盐田区', '大鹏新区', '深汕特别合作区'],
  guangzhou: ['全部区县', '白云区', '番禺区', '天河区', '海珠区', '花都区', '增城区', '黄埔区', '荔湾区', '越秀区', '南沙区', '从化区'],
  shanghai: [
    '全部区县',
    '浦东新区',
    '闵行区',
    '宝山区',
    '松江区',
    '嘉定区',
    '杨浦区',
    '青浦区',
    '普陀区',
    '奉贤区',
    '徐汇区',
    '静安区',
    '金山区',
    '虹口区',
    '长宁区',
    '黄浦区',
    '虹口',
    '杨浦',
    '徐汇',
    '嘉定',
    '上海市',
    '长宁',
    '普陀',
    '临港',
    '静安',
    '崇明区',
    '青浦',
    '松江',
    '崇明',
    '闵行',
    '奉贤',
    '浦东',
    '黄浦',
    '宝山'
  ],
  beijing: [
    '全部区县',
    '朝阳区',
    '海淀区',
    '昌平区',
    '丰台区',
    '大兴区',
    '通州区',
    '顺义区',
    '房山区',
    '西城区',
    '东城区',
    '石景山区',
    '密云区',
    '平谷区',
    '怀柔区',
    '门头沟区',
    '延庆区',
    '北京经济技术开发区',
    '燕山地区',
    '怀柔区，东城区'
  ],
  hangzhou: ['全部区县', '萧山区', '上城区', '余杭区', '临平区', '拱墅区', '富阳区', '西湖区', '建德市', '桐庐县', '临安区', '滨江区', '淳安县', '下城区', '江干区'],
  chengdu: [
    '全部区县',
    '郫都区',
    '新都区',
    '双流区',
    '龙泉驿区',
    '高新区',
    '金牛区',
    '武侯区',
    '温江区',
    '成华区',
    '青羊区',
    '锦江区',
    '天府新区',
    '都江堰市',
    '邛崃市',
    '大邑县',
    '崇州市',
    '彭州市'
  ],
  chongqing: [
    '全部区县',
    '渝北区',
    '九龙坡区',
    '沙坪坝区',
    '南岸区',
    '巴南区',
    '江北区',
    '北碚区',
    '璧山区',
    '渝中区',
    '大渡口区',
    '綦江区',
    'A馆:重庆市',
    '垫江县',
    '两江新区',
    '万州区',
    '巫山县',
    '江津区',
    '石柱县',
    '酉阳自治县',
    '万盛经济技术开发区',
    '合川区',
    '荣昌区',
    '开州区',
    '奉节县',
    '大足区',
    '巫溪县',
    '鸿恩寺馆:重庆市',
    '北陪区',
    '永川区',
    '忠县',
    '武隆区',
    '涪陵区',
    '酉阳县',
    '市体育馆',
    '长寿区',
    '秀山县',
    '南川区',
    '梁平区',
    '大田湾体育场',
    '潼南区',
    '铜梁区',
    '万盛经开区',
    '奥体中心体育场',
    '城万旧址：城口县',
    '云阳县',
    '彭水县',
    '黔江区',
    '丰都县',
    '城口县'
  ],
  nanjing: ['全部区县', '江宁区', '浦口区', '栖霞区', '六合区', '鼓楼区', '秦淮区', '玄武区', '溧水区', '建邺区', '雨花台区', '高淳区'],
  wuhan: ['全部区县', '洪山区', '江夏区', '武昌区', '黄陂区', '蔡甸区', '东西湖区', '新洲区', '硚口区', '江汉区', '江岸区', '汉阳区', '青山区'],
  xian: [
    '全部区县',
    '雁塔区',
    '长安区',
    '未央区',
    '高新区',
    '碑林区',
    '莲湖区',
    '灞桥区',
    '临潼区',
    '新城区',
    '鄠邑区',
    '高陵区',
    '阎良区',
    '经开区',
    '秦都区',
    '蓝田县',
    '浐灞生态区',
    '曲江新区',
    '沣东新城',
    '西安市新城',
    '空港新城',
    '汉 西咸新区',
    '西安市莲湖',
    '周至县',
    '西安市鄠邑',
    '渭城区',
    '西安市碑林',
    '西安市临潼',
    '咸阳市渭城区'
  ],
  zhuhai: ['全部区县', '高新区', '香洲区', '斗门区', '金湾区', '高栏港区', '万山区', '横琴新区']
};

// 区县常住人口(2020 七普, 万人)，用于区县筛选按人口降序
const districtPopulation = {
  宝安区: 447,
  龙岗区: 397,
  龙华区: 253,
  南山区: 180,
  福田区: 156,
  罗湖区: 114,
  光明区: 110,
  坪山区: 55,
  盐田区: 21,
  大鹏新区: 15,
  白云区: 374,
  番禺区: 266,
  天河区: 224,
  海珠区: 182,
  花都区: 170,
  增城区: 146,
  黄埔区: 126,
  荔湾区: 123,
  越秀区: 116,
  南沙区: 84,
  从化区: 71,
  浦东新区: 568,
  闵行区: 265,
  宝山区: 223,
  松江区: 191,
  嘉定区: 184,
  杨浦区: 131,
  青浦区: 130,
  普陀区: 129,
  徐汇区: 111,
  奉贤区: 114,
  静安区: 98,
  金山区: 82,
  虹口区: 76,
  长宁区: 69,
  黄浦区: 66,
  朝阳区: 345,
  海淀区: 313,
  昌平区: 227,
  丰台区: 202,
  大兴区: 199,
  通州区: 184,
  顺义区: 132,
  房山区: 131,
  西城区: 110,
  东城区: 92,
  石景山区: 57,
  密云区: 46,
  平谷区: 46,
  怀柔区: 41,
  门头沟区: 39,
  延庆区: 23,
  萧山区: 205,
  上城区: 133,
  余杭区: 122,
  临平区: 117,
  富阳区: 83,
  西湖区: 81,
  钱塘区: 80,
  建德市: 78,
  桐庐县: 75,
  拱墅区: 109,
  临安区: 64,
  滨江区: 53,
  淳安县: 51,
  郫都区: 167,
  新都区: 156,
  双流区: 146,
  龙泉驿区: 135,
  温江区: 99,
  金牛区: 126,
  武侯区: 121,
  成华区: 96,
  青羊区: 96,
  锦江区: 90,
  高新区: 130,
  天府新区: 90,
  都江堰市: 71,
  江宁区: 156,
  浦口区: 117,
  鼓楼区: 94,
  栖霞区: 98,
  六合区: 94,
  玄武区: 61,
  秦淮区: 74,
  建邺区: 48,
  雨花台区: 46,
  溧水区: 50,
  高淳区: 43,
  洪山区: 172,
  江夏区: 147,
  武昌区: 128,
  黄陂区: 115,
  蔡甸区: 92,
  东西湖区: 88,
  硚口区: 83,
  江汉区: 73,
  汉阳区: 67,
  江岸区: 71,
  新洲区: 86,
  青山区: 49,
  雁塔区: 204,
  长安区: 164,
  未央区: 160,
  碑林区: 76,
  莲湖区: 71,
  新城区: 62,
  灞桥区: 70,
  临潼区: 68,
  高陵区: 30,
  阎良区: 28,
  鄠邑区: 39,
  渝北区: 219,
  九龙坡区: 153,
  沙坪坝区: 148,
  南岸区: 120,
  巴南区: 118,
  江北区: 91,
  北碚区: 84,
  璧山区: 76,
  渝中区: 58,
  大渡口区: 43,
  香洲区: 112,
  斗门区: 61,
  金湾区: 44
};

// 中文 source 名称 → 区名映射（自动生成，兜底用）
const sourceChineseToDistrict = {
  深圳图书馆: '福田区',
  深圳少年儿童图书馆: '福田区',
  深圳博物馆: '福田区',
  深圳科学技术馆: '光明区',
  深圳滨海艺术中心: '宝安区',
  深圳音乐厅: '福田区',
  深圳市当代艺术与城市规划馆: '福田区',
  深圳市体育中心: '福田区',
  深圳市文化馆: '福田区',
  深圳自然博物馆: '坪山区',
  南山图书馆: '南山区',
  南山博物馆: '南山区',
  南山区文化馆: '南山区',
  南山区青少年活动中心: '南山区',
  南山文体中心: '南山区',
  南山安全教育体验馆: '南山区',
  蛇口海洋科普馆: '南山区',
  深爱人才馆: '南山区',
  南头古城博物馆群: '南山区',
  招商局历史博物馆: '南山区',
  南山书房: '南山区',
  华侨城湿地: '南山区',
  深圳湾体育中心: '南山区',
  欢乐港湾: '宝安区',
  福田区图书馆: '福田区',
  福田区文化馆: '福田区',
  福田美术馆: '福田区',
  深圳古生物博物馆: '罗湖区',
  罗湖区图书馆: '罗湖区',
  罗湖区文化馆: '罗湖区',
  深圳戏院: '罗湖区',
  深圳大剧院: '罗湖区',
  宝安图书馆: '宝安区',
  宝安区博物馆: '宝安区',
  宝安1990文化馆: '宝安区',
  宝安科技馆: '宝安区',
  宝安体育中心: '宝安区',
  宝安区青少年宫: '宝安区',
  宝安城市规划展览馆: '宝安区',
  湾区之眼: '宝安区',
  龙岗区图书馆: '龙岗区',
  龙岗区博物馆: '龙岗区',
  龙岗区文化馆: '龙岗区',
  龙岗区青少年宫: '龙岗区',
  龙岗客家民俗博物馆: '龙岗区',
  龙岗体育中心: '龙岗区',
  深圳龙岗国际艺术中心: '龙岗区',
  龙岗区科技馆: '龙岗区',
  龙岗儿童公园: '龙岗区',
  龙华区图书馆: '龙华区',
  龙华区青少年宫: '龙华区',
  龙华区文化馆: '龙华区',
  中国版画博物馆: '龙华区',
  龙华生态文明展览馆: '龙华区',
  龙华区科技馆: '龙华区',
  龙华白石龙纪念馆: '龙华区',
  光明区图书馆: '光明区',
  光明区科技馆: '光明区',
  光明区文化馆: '光明区',
  光明文化艺术中心: '光明区',
  光明区青少年活动中心: '光明区',
  光明区群众体育中心: '光明区',
  光明虹桥公园: '光明区',
  玉塘文体中心: '光明区',
  坪山区图书馆: '坪山区',
  坪山美术馆: '坪山区',
  坪山大剧院: '坪山区',
  坪山区科技馆: '坪山区',
  坪山体育中心: '坪山区',
  坪山东江纵队纪念馆: '坪山区',
  坪山中心公园: '坪山区',
  马峦山郊野公园: '坪山区',
  聚龙山生态公园: '坪山区',
  燕子湖国际会展中心: '坪山区',
  盐田区图书馆: '盐田区',
  盐田区文化馆: '盐田区',
  中英街历史博物馆: '盐田区',
  盐田科技馆: '盐田区',
  盐田体育中心: '盐田区',
  盐田中央公园: '盐田区',
  大鹏地质公园博物馆: '大鹏新区',
  大亚湾核能科技馆: '大鹏新区',
  大鹏新区图书馆: '大鹏新区',
  大鹏古城博物馆: '大鹏新区',
  大鹏新区文化馆: '大鹏新区',
  深圳西涌天文台: '大鹏新区',
  东涌红树林湿地公园: '大鹏新区',
  坝光红树林湿地公园: '大鹏新区',
  玫瑰海岸: '大鹏新区',
  杨梅坑: '大鹏新区',
  七娘山: '大鹏新区',
  官湖村艺象艺术区: '大鹏新区',
  金沙湾国际乐园: '大鹏新区',
  大鹏新区科学馆: '大鹏新区',
  大鹏较场尾沙滩: '大鹏新区',
  葵涌生态公园: '大鹏新区',
  深圳市安全教育基地: '福田区',
  OPOWER文化艺术中心: '南山区',
  坪山区青少年宫: '坪山区',
  广东省博物馆: '天河区',
  广州博物馆: '越秀区',
  广州图书馆: '天河区',
  上海博物馆: '黄浦区',
  上海科技馆: '浦东新区',
  中国国家博物馆: '东城区',
  故宫博物院: '东城区',
  何香凝美术馆: '南山区',
  关山月美术馆: '福田区',
  深圳美术馆: '罗湖区',
  深圳保利剧院: '南山区',
  深圳会展中心: '福田区',
  深圳国际会展中心: '宝安区',
  锦绣中华民俗村: '南山区',
  深圳市少年宫: '福田区',
  深圳市青少年活动中心: '福田区',
  深圳书城: '福田区',
  深圳湾公园: '南山区',
  海上世界文化艺术中心: '南山区',
  深圳中医药博物馆: '福田区',
  深圳珠宝博物馆: '盐田区',
  深圳欢乐谷: '南山区',
  深圳欢乐海岸: '南山区',
  深圳世界之窗: '南山区',
  洪湖公园: '罗湖区',
  大沙河生态长廊: '南山区',
  淘金山绿道: '罗湖区',
  西湾红树林公园: '宝安区',
  茅洲河碧道: '光明区',
  石岩湖湿地公园: '宝安区',
  石岩文化艺术中心: '宝安区',
  红花山公园: '坪山区',
  深圳大运中心: '龙岗区',
  大运中心公园: '龙岗区',
  安托山公共文化中心: '福田区',
  北站中心公园: '龙华区',
  '深圳科学公园（南翼）': '光明区',
  人才公园: '南山区',
  吉华街道文化站: '龙岗区',
  南湾街道文化站: '龙岗区',
  坪地街道文化站: '龙岗区',
  园岭街道综合性文化服务中心: '福田区',
  桃源街道综合性文化服务中心: '南山区',
  凤凰街道综合性文化服务中心: '光明区',
  江岭社区公共文化服务中心: '坪山区',
  迳口社区综合性文化服务中心: '光明区',
  浙江省博物馆: '西湖区',
  中国科学技术馆: '朝阳区',
  北京天文馆: '西城区',
  国家自然博物馆: '东城区',
  国家动物博物馆: '朝阳区',
  中国消防博物馆: '西城区',
  北京汽车博物馆: '丰台区',
  北京动物园: '西城区',
  北京海洋馆: '西城区',
  北京欢乐谷: '朝阳区',
  水立方嬉水乐园: '朝阳区',
  欢乐水魔方水上乐园: '丰台区',
  朝阳公园: '朝阳区',
  世界公园: '丰台区',
  北京野生动物园: '大兴区',
  北京科学中心: '西城区',
  中国地质博物馆: '西城区',
  北京奥运博物馆: '朝阳区',
  中国航空博物馆: '昌平区',
  中国考古博物馆: '朝阳区',
  中国园林博物馆: '丰台区',
  中国军事博物馆: '海淀区',
  海淀公共安全馆: '海淀区',
  乐高探索中心: '普陀区',
  首都图书馆: '朝阳区',
  国家图书馆: '海淀区',
  中国妇女儿童博物馆: '东城区',
  中国古动物馆: '西城区',
  索尼探梦科技馆: '朝阳区',
  泡泡玛特城市乐园: '朝阳区',
  北京植物园: '海淀区',
  颐和园: '海淀区',
  天坛公园: '东城区',
  地坛公园: '东城区',
  北海公园: '西城区',
  景山公园: '西城区',
  中山公园: '西城区',
  劳动人民文化宫: '东城区',
  北京天文馆A馆: '西城区',
  北京天文馆B馆: '西城区',
  北京展览馆: '西城区',
  中国美术馆: '东城区',
  北京音乐厅: '西城区',
  国家大剧院: '西城区',
  梅兰芳大剧院: '西城区',
  长安大戏院: '东城区',
  北京儿艺剧场: '东城区',
  北京展览馆剧场: '西城区',
  北京工人体育馆: '朝阳区',
  北京工人体育场: '朝阳区',
  五棵松体育馆: '海淀区',
  奥林匹克森林公园: '朝阳区',
  元大都城垣遗址公园: '朝阳区',
  奥林匹克公园: '朝阳区',
  朝阳公园海洋沙滩狂欢节: '朝阳区',
  蟹岛度假村: '朝阳区',
  南宫旅游景区: '丰台区',
  北京莲花池公园: '丰台区',
  北京世界花卉大观园: '丰台区',
  北京园博园: '丰台区',
  北京石景山游乐园: '石景山区',
  八大处公园: '石景山区',
  法海寺: '石景山区',
  首钢园: '石景山区',
  北京国际雕塑公园: '石景山区',
  百望山森林公园: '海淀区',
  凤凰岭自然风景区: '海淀区',
  鹫峰国家森林公园: '海淀区',
  阳台山自然风景区: '海淀区',
  香山公园: '海淀区',
  北京植物园樱桃沟: '海淀区',
  北京植物园温室: '海淀区',
  北京天文馆天象厅: '西城区',
  中国科学技术馆儿童科学乐园: '朝阳区',
  北京城市图书馆: '通州区',
  北京环球度假区: '通州区',
  北京运河奥体公园: '通州区',
  北京西海子公园: '通州区',
  北京运河森林公园: '通州区',
  北京东郊湿地公园: '通州区',
  北京张家湾公园: '通州区',
  北京台湖公园: '通州区',
  北京月亮河公园: '通州区',
  北京路县故城遗址: '通州区',
  北京通州博物馆: '通州区',
  北京汉石桥湿地: '顺义区',
  北京奥林匹克水上公园: '顺义区',
  北京顺义公园: '顺义区',
  北京顺义新城滨河森林公园: '顺义区',
  北京国际鲜花港: '顺义区',
  北京张裕爱斐堡国际酒庄: '密云区',
  北京古北水镇: '密云区',
  北京司马台长城: '密云区',
  北京黑龙潭景区: '密云区',
  北京云蒙山景区: '密云区',
  北京雾灵山景区: '密云区',
  北京金海湖景区: '平谷区',
  北京京东大峡谷: '平谷区',
  北京石林峡景区: '平谷区',
  北京延庆奥林匹克园区: '延庆区',
  北京世园公园: '延庆区',
  北京八达岭国家森林公园: '延庆区',
  北京野鸭湖国家湿地公园: '延庆区',
  北京龙庆峡景区: '延庆区',
  北京云居寺: '房山区',
  北京十渡景区: '房山区',
  北京房山世界地质公园: '房山区',
  北京上方山国家森林公园: '房山区',
  北京石花洞景区: '房山区',
  北京银狐洞景区: '房山区',
  北京百花山景区: '房山区',
  北京圣莲山景区: '房山区',
  北京青龙湖公园: '房山区',
  北京蒲洼乡花台景区: '房山区',
  北京霞云岭国家森林公园: '房山区',
  北京大兴区动物园: '大兴区',
  北京密云区动物园: '密云区',
  蓝色港湾: '怀柔区',
  北京门头沟区剧院: '门头沟区',
  北京石景山区创意园: '石景山区',
  北京西城区海洋馆: '西城区',
  北京大兴区创意园: '大兴区',
  潭柘寺: '门头沟区',
  北京自然博物馆: '延庆区',
  北京大兴区剧院: '大兴区',
  北京丰台区艺术中心: '丰台区',
  日坛公园: '西城区',
  北京西城区创意园: '西城区',
  北京石景山区海洋馆: '石景山区',
  北京海淀区文化馆: '海淀区',
  北京大兴区美术馆: '大兴区',
  北京海淀区体育场: '海淀区',
  国家体育馆: '通州区',
  北京丰台区体育场: '丰台区',
  北京石景山区体育馆: '石景山区',
  北京昌平区体育场: '昌平区',
  北京房山区文化中心: '房山区',
  北京丰台区创意园: '丰台区',
  北京东城区博物馆: '东城区',
  北京大兴区公园: '大兴区',
  北京昌平区剧院: '昌平区',
  北京房山区公园: '房山区',
  松美术馆: '通州区',
  北京东城区体育场: '东城区',
  北京房山区美术馆: '房山区',
  北京门头沟区科技馆: '门头沟区',
  北京海淀区植物园: '海淀区',
  北京门头沟区文化馆: '门头沟区',
  北京门头沟区植物园: '门头沟区',
  北京通州区植物园: '通州区',
  北京房山区海洋馆: '房山区',
  北京顺义区创意园: '顺义区',
  北京门头沟区体育馆: '门头沟区',
  北京密云区会展中心: '密云区',
  北京通州区图书馆: '通州区',
  中国铁道博物馆正阳门馆: '东城区',
  龙潭湖公园: '密云区',
  国贸商城: '房山区',
  王府井: '石景山区',
  北京门头沟区体育场: '门头沟区',
  北京西城区植物园: '西城区',
  北京石景山区美术馆: '石景山区',
  前门大街: '丰台区',
  北京丰台区博物馆: '丰台区',
  北京西城区会展中心: '西城区',
  国家体育场: '东城区',
  北京昌平区文化馆: '昌平区',
  北京怀柔区文化中心: '怀柔区',
  大观园: '怀柔区',
  中国科技馆: '丰台区',
  北京房山区图书馆: '房山区',
  北京东城区青少年宫: '东城区',
  北京石景山区图书馆: '石景山区',
  北京丰台区剧院: '丰台区',
  北京朝阳区公园: '朝阳区',
  北京延庆区艺术中心: '延庆区',
  北京房山区文化馆: '房山区',
  北京石景山区青少年宫: '石景山区',
  恭王府博物馆: '西城区',
  玉渊潭公园: '朝阳区',
  北京延庆区会展中心: '延庆区',
  北京海淀区文化中心: '海淀区',
  北京延庆区体育场: '延庆区',
  孔庙和国子监博物馆: '东城区',
  首都博物馆: '朝阳区',
  北京房山区青少年宫: '房山区',
  红螺寺: '怀柔区',
  北京丰台区文化中心: '丰台区',
  北京西城区文化馆: '西城区',
  北京丰台区图书馆: '丰台区',
  北京西城区青少年宫: '西城区',
  什刹海: '房山区',
  北京石景山区植物园: '石景山区',
  北京顺义区体育馆: '顺义区',
  北京大兴区会展中心: '大兴区',
  北京密云区体育场: '密云区',
  今日美术馆: '丰台区',
  北京昌平区海洋馆: '昌平区',
  北京丰台区文化馆: '丰台区',
  北京通州区美术馆: '通州区',
  北京房山区植物园: '房山区',
  北京大兴区图书馆: '大兴区',
  北京西城区体育馆: '西城区',
  北京密云区图书馆: '密云区',
  北京怀柔区公园: '怀柔区',
  中国邮政邮票博物馆: '东城区',
  大钟寺古钟博物馆: '海淀区',
  北京故宫博物院: '门头沟区',
  北京怀柔区体育馆: '怀柔区',
  北京昌平区青少年宫: '昌平区',
  北京朝阳区图书馆: '朝阳区',
  郭沫若纪念馆: '西城区',
  红砖美术馆: '大兴区',
  北京门头沟区会展中心: '门头沟区',
  北京房山区剧院: '房山区',
  北京古观象台: '东城区',
  北京昌平区图书馆: '昌平区',
  北京朝阳区博物馆: '朝阳区',
  北京石景山区科技馆: '石景山区',
  北京通州区动物园: '通州区',
  北京门头沟区公园: '门头沟区',
  北京通州区剧院: '通州区',
  北京海淀区博物馆: '海淀区',
  北京大兴区植物园: '大兴区',
  八达岭长城: '房山区',
  北京顺义区图书馆: '顺义区',
  北京怀柔区青少年宫: '怀柔区',
  北京房山区动物园: '房山区',
  北京房山区体育馆: '房山区',
  北京门头沟区艺术中心: '门头沟区',
  云居寺: '房山区',
  北京丰台区科技馆: '丰台区',
  北京顺义区文化馆: '顺义区',
  北京密云区文化中心: '密云区',
  北京海淀区海洋馆: '海淀区',
  北京房山区体育场: '房山区',
  牛街礼拜寺: '西城区',
  北京昌平区文化中心: '昌平区',
  北京海淀区美术馆: '海淀区',
  北京怀柔区美术馆: '怀柔区',
  北京朝阳区艺术中心: '朝阳区',
  北京东城区剧院: '东城区',
  北京房山区博物馆: '房山区',
  北京通州区体育场: '通州区',
  北京顺义区海洋馆: '顺义区',
  北京石景山区博物馆: '石景山区',
  陶然亭公园: '门头沟区',
  北京大兴区科技馆: '大兴区',
  北京东城区体育馆: '东城区',
  北京延庆区动物园: '延庆区',
  北京东城区海洋馆: '东城区',
  北京海淀区图书馆: '海淀区',
  北京顺义区动物园: '顺义区',
  北京顺义区艺术中心: '顺义区',
  北京密云区艺术中心: '密云区',
  北京昌平区动物园: '昌平区',
  白云观: '西城区',
  北京石景山区公园: '石景山区',
  北京朝阳区剧院: '朝阳区',
  北京通州区文化中心: '通州区',
  北京朝阳区科技馆: '朝阳区',
  北京西城区剧院: '西城区',
  南锣鼓巷: '顺义区',
  三里屯: '门头沟区',
  北京西城区科技馆: '西城区',
  北京延庆区博物馆: '延庆区',
  北京东城区创意园: '东城区',
  北京延庆区剧院: '延庆区',
  北京门头沟区动物园: '门头沟区',
  北京海淀区会展中心: '海淀区',
  北京海淀区创意园: '海淀区',
  北京怀柔区植物园: '怀柔区',
  北京怀柔区体育场: '怀柔区',
  北京密云区体育馆: '密云区',
  雍和宫: '东城区',
  北京延庆区青少年宫: '延庆区',
  北京延庆区文化中心: '延庆区',
  北京顺义区美术馆: '顺义区',
  北京西城区博物馆: '西城区',
  北京西城区文化中心: '西城区',
  北京昌平区科技馆: '昌平区',
  智化寺: '东城区',
  北京顺义区公园: '顺义区',
  北京门头沟区海洋馆: '门头沟区',
  北京海淀区青少年宫: '海淀区',
  国家游泳中心: '西城区',
  北京延庆区体育馆: '延庆区',
  北京丰台区动物园: '丰台区',
  北京石刻艺术博物馆: '海淀区',
  北京怀柔区博物馆: '怀柔区',
  北京海淀区科技馆: '海淀区',
  北京通州区文化馆: '通州区',
  北京海淀区体育馆: '海淀区',
  北京西城区美术馆: '西城区',
  北京画院美术馆: '朝阳区',
  北京延庆区美术馆: '延庆区',
  戒台寺: '门头沟区',
  北京朝阳区文化中心: '朝阳区',
  北京石景山区文化馆: '石景山区',
  北京顺义区植物园: '顺义区',
  北京朝阳区美术馆: '朝阳区',
  北京密云区公园: '密云区',
  北京延庆区植物园: '延庆区',
  北京顺义区科技馆: '顺义区',
  北京密云区创意园: '密云区',
  北京西城区体育场: '西城区',
  北京鲁迅博物馆: '西城区',
  北京大兴区海洋馆: '大兴区',
  北京朝阳区青少年宫: '朝阳区',
  北京昌平区博物馆: '昌平区',
  北京门头沟区图书馆: '门头沟区',
  老舍纪念馆: '东城区',
  北京丰台区青少年宫: '丰台区',
  北京怀柔区文化馆: '怀柔区',
  北京顺义区会展中心: '顺义区',
  北京东城区科技馆: '东城区',
  北京朝阳区创意园: '朝阳区',
  北京东城区文化中心: '东城区',
  北京东城区动物园: '东城区',
  北京艺术博物馆: '海淀区',
  北京朝阳区体育馆: '朝阳区',
  北京昌平区美术馆: '昌平区',
  北京朝阳区体育场: '朝阳区',
  北京朝阳区动物园: '朝阳区',
  北京海淀区艺术中心: '海淀区',
  北京西城区艺术中心: '西城区',
  北京东城区艺术中心: '东城区',
  北京怀柔区剧院: '怀柔区',
  北京通州区创意园: '通州区',
  北京丰台区会展中心: '丰台区',
  茅盾故居: '东城区',
  妙应寺白塔: '西城区',
  北京昌平区植物园: '昌平区',
  北京延庆区海洋馆: '延庆区',
  北京通州区科技馆: '通州区',
  北京密云区剧院: '密云区',
  北京通州区博物馆: '通州区',
  北京东城区公园: '东城区',
  北京东城区图书馆: '东城区',
  北京怀柔区海洋馆: '怀柔区',
  北京石景山区会展中心: '石景山区',
  北京大兴区文化馆: '大兴区',
  北京密云区海洋馆: '密云区',
  北京大兴区艺术中心: '大兴区',
  北京丰台区公园: '丰台区',
  北京密云区植物园: '密云区',
  宋庆龄同志故居: '西城区',
  北京怀柔区会展中心: '怀柔区',
  北京大兴区体育馆: '大兴区',
  北京延庆区文化馆: '延庆区',
  北京昌平区公园: '昌平区',
  北京民俗博物馆: '朝阳区',
  北京石景山区艺术中心: '石景山区',
  北京通州区青少年宫: '通州区',
  北京怀柔区动物园: '怀柔区',
  北京朝阳区会展中心: '朝阳区',
  北京顺义区博物馆: '顺义区',
  北京门头沟区创意园: '门头沟区',
  北京通州区公园: '通州区',
  北京东城区会展中心: '东城区',
  北京丰台区美术馆: '丰台区',
  北京密云区科技馆: '密云区',
  三圣花乡: '锦江区',
  天府人文艺术图书馆: '金牛区',
  成都武侯祠博物馆: '武侯区',
  成都金沙遗址博物馆: '青羊区',
  锦城湖公园: '高新区',
  成都蹦床馆: '武侯区',
  街子古镇: '崇州市',
  成都IFS国际金融中心: '锦江区',
  成都环球中心: '高新区',
  成都大悦城: '武侯区',
  成都博物馆: '青羊区',
  四川科技馆: '青羊区',
  环球中心天堂岛海洋乐园: '高新区',
  青龙湖湿地公园: '龙泉驿区',
  成都植物园: '新都区',
  成都欢乐谷: '金牛区',
  成都融创水世界: '都江堰市',
  成都国色天乡乐园: '温江区',
  成都海昌极地海洋公园: '天府新区',
  国际非遗博览园: '青羊区',
  成都图书馆: '青羊区',
  成都杜甫草堂博物馆: '青羊区',
  四川省体育馆: '武侯区',
  成都跆拳道馆: '武侯区',
  黄龙溪古镇: '双流区',
  洛带古镇: '龙泉驿区',
  平乐古镇: '邛崃市',
  成都来福士广场: '武侯区',
  成都金牛区青少年宫: '金牛区',
  四川博物院: '武侯区',
  锦里: '武侯区',
  成都成华区文化馆: '成华区',
  白鹭湾湿地公园: '锦江区',
  宽窄巷子: '青羊区',
  四川省图书馆: '青羊区',
  安仁古镇: '大邑县',
  成都远洋太古里: '锦江区',
  成都万象城: '成华区',
  成都高新区创意园: '高新区',
  成都新都区美术馆: '新都区',
  成都新都区植物园: '新都区',
  成都动物园: '成华区',
  成都跑酷场: '成华区',
  成都武术馆: '青羊区',
  成都高新区公园: '高新区',
  成都龙泉驿区青少年宫: '龙泉驿区',
  成都成华区海洋馆: '成华区',
  成都双流区艺术中心: '双流区',
  成都天府新区体育馆: '天府新区',
  成都龙泉驿区美术馆: '龙泉驿区',
  兴隆湖湿地公园: '天府新区',
  成都龙泉驿区会展中心: '龙泉驿区',
  成都武侯区青少年宫: '武侯区',
  成都锦江区文化馆: '锦江区',
  成都川剧院: '锦江区',
  天府绿道: '高新区',
  成都亲子游泳馆: '高新区',
  成都银泰中心: '高新区',
  成都武侯区美术馆: '武侯区',
  成都青羊区图书馆: '青羊区',
  成都龙泉驿区植物园: '龙泉驿区',
  成都双流区美术馆: '双流区',
  成都轮滑场: '金牛区',
  成都瑜伽馆: '锦江区',
  成都锦江区博物馆: '锦江区',
  成都成华区图书馆: '成华区',
  成都锦江区公园: '锦江区',
  成都龙泉驿区体育场: '龙泉驿区',
  成都金牛区科技馆: '金牛区',
  成都温江区青少年宫: '温江区',
  人民公园: '青羊区',
  成都高尔夫球场: '双流区',
  成都滑板场: '成华区',
  成都新都区科技馆: '新都区',
  浣花溪公园: '青羊区',
  成都青羊区植物园: '青羊区',
  成都锦江区会展中心: '锦江区',
  锦江绿道: '锦江区',
  成都天府新区艺术中心: '天府新区',
  成都马术俱乐部: '双流区',
  成都新都区海洋馆: '新都区',
  成都天府新区动物园: '天府新区',
  成都武侯区文化中心: '武侯区',
  成都双流区剧院: '双流区',
  成都温江区公园: '温江区',
  成都武侯区文化馆: '武侯区',
  成都青羊区海洋馆: '青羊区',
  成都锦江区创意园: '锦江区',
  成都龙泉驿区博物馆: '龙泉驿区',
  成都郫都区公园: '郫都区',
  成都成华区体育场: '成华区',
  成都都江堰市海洋馆: '都江堰市',
  成都体育馆: '青羊区',
  成都都江堰市剧院: '都江堰市',
  成都郫都区剧院: '郫都区',
  成都温江区海洋馆: '温江区',
  成都青羊区体育场: '青羊区',
  成都高新区文化中心: '高新区',
  成都彭州市图书馆: '彭州市',
  成都温江区会展中心: '温江区',
  成都高新区植物园: '高新区',
  成都彭州市文化馆: '彭州市',
  成都高新区会展中心: '高新区',
  成都锦江区科技馆: '锦江区',
  成都新都区会展中心: '新都区',
  成都成华区青少年宫: '成华区',
  成都锦江区美术馆: '锦江区',
  成都都江堰市创意园: '都江堰市',
  成都金牛区公园: '金牛区',
  成都成华区艺术中心: '成华区',
  成都成华区美术馆: '成华区',
  成都高新区青少年宫: '高新区',
  成都双流区文化馆: '双流区',
  成都彭州市动物园: '彭州市',
  成都都江堰市博物馆: '都江堰市',
  成都高新区动物园: '高新区',
  成都都江堰市图书馆: '都江堰市',
  成都都江堰市艺术中心: '都江堰市',
  成都金牛区艺术中心: '金牛区',
  成都彭州市艺术中心: '彭州市',
  成都锦江区海洋馆: '锦江区',
  成都温江区文化中心: '温江区',
  成都成华区体育馆: '成华区',
  成都温江区剧院: '温江区',
  成都平衡车场: '武侯区',
  成都金牛区体育场: '金牛区',
  成都双流区动物园: '双流区',
  成都都江堰市动物园: '都江堰市',
  成都青羊区公园: '青羊区',
  成都金牛区会展中心: '金牛区',
  成都天府新区公园: '天府新区',
  成都天府新区植物园: '天府新区',
  成都武侯区博物馆: '武侯区',
  成都金牛区植物园: '金牛区',
  成都成华区会展中心: '成华区',
  成都天府新区博物馆: '天府新区',
  成都彭州市青少年宫: '彭州市',
  成都高新区文化馆: '高新区',
  成都彭州市剧院: '彭州市',
  成都天府新区创意园: '天府新区',
  成都武侯区图书馆: '武侯区',
  成都温江区植物园: '温江区',
  成都龙泉驿区剧院: '龙泉驿区',
  成都温江区文化馆: '温江区',
  成都武侯区艺术中心: '武侯区',
  成都高新区博物馆: '高新区',
  成都新都区文化中心: '新都区',
  成都青羊区创意园: '青羊区',
  成都天府新区文化中心: '天府新区',
  成都青羊区美术馆: '青羊区',
  成都郫都区动物园: '郫都区',
  成都武侯区体育馆: '武侯区',
  成都成华区创意园: '成华区',
  成都龙泉驿区公园: '龙泉驿区',
  成都郫都区海洋馆: '郫都区',
  成都彭州市文化中心: '彭州市',
  成都郫都区博物馆: '郫都区',
  成都金牛区创意园: '金牛区',
  成都锦江区艺术中心: '锦江区',
  成都武侯区创意园: '武侯区',
  成都成华区博物馆: '成华区',
  成都都江堰市植物园: '都江堰市',
  成都天府新区美术馆: '天府新区',
  成都锦江区体育馆: '锦江区',
  成都武侯区植物园: '武侯区',
  成都成华区科技馆: '成华区',
  成都击剑馆: '武侯区',
  成都武侯区剧院: '武侯区',
  成都锦江区体育场: '锦江区',
  成都都江堰市文化中心: '都江堰市',
  成都郫都区青少年宫: '郫都区',
  成都龙泉驿区动物园: '龙泉驿区',
  成都金牛区图书馆: '金牛区',
  成都新都区动物园: '新都区',
  成都新都区文化馆: '新都区',
  成都天府新区科技馆: '天府新区',
  成都都江堰市会展中心: '都江堰市',
  成都双流区博物馆: '双流区',
  成都郫都区植物园: '郫都区',
  成都都江堰市公园: '都江堰市',
  成都武侯区体育场: '武侯区',
  成都体育学院: '武侯区',
  成都郫都区文化馆: '郫都区',
  成都彭州市会展中心: '彭州市',
  成都新都区创意园: '新都区',
  成都青羊区青少年宫: '青羊区',
  成都金牛区剧院: '金牛区',
  成都双流区创意园: '双流区',
  成都青羊区剧院: '青羊区',
  成都龙泉驿区科技馆: '龙泉驿区',
  成都温江区科技馆: '温江区',
  成都金牛区美术馆: '金牛区',
  成都彭州市体育场: '彭州市',
  成都金牛区文化馆: '金牛区',
  成都成华区文化中心: '成华区',
  成都青羊区文化中心: '青羊区',
  成都彭州市博物馆: '彭州市',
  成都龙泉驿区海洋馆: '龙泉驿区',
  成都青羊区艺术中心: '青羊区',
  成都都江堰市体育馆: '都江堰市',
  成都成华区公园: '成华区',
  成都新都区剧院: '新都区',
  成都武侯区科技馆: '武侯区',
  成都冰场: '锦江区',
  成都青羊区会展中心: '青羊区',
  成都龙泉驿区图书馆: '龙泉驿区',
  成都锦江区动物园: '锦江区',
  成都彭州市体育馆: '彭州市',
  成都新都区公园: '新都区',
  成都武侯区会展中心: '武侯区',
  成都都江堰市美术馆: '都江堰市',
  成都高新区图书馆: '高新区',
  成都青羊区科技馆: '青羊区',
  成都龙泉驿区文化馆: '龙泉驿区',
  成都双流区图书馆: '双流区',
  成都彭州市科技馆: '彭州市',
  成都射箭馆: '武侯区',
  成都锦江区青少年宫: '锦江区',
  成都彭州市海洋馆: '彭州市',
  蜀锦织绣博物馆: '青羊区',
  成都温江区动物园: '温江区',
  成都锦江区文化中心: '锦江区',
  成都郫都区图书馆: '郫都区',
  成都彭州市植物园: '彭州市',
  成都新都区青少年宫: '新都区',
  成都温江区图书馆: '温江区',
  成都天府新区海洋馆: '天府新区',
  成都温江区体育馆: '温江区',
  成都锦江区剧院: '锦江区',
  成都青羊区体育馆: '青羊区',
  成都双流区海洋馆: '双流区',
  成都双流区文化中心: '双流区',
  成都攀岩馆: '武侯区',
  成都武侯区动物园: '武侯区',
  成都高新区体育馆: '高新区',
  成都双流区体育场: '双流区',
  成都金牛区海洋馆: '金牛区',
  成都高新区剧院: '高新区',
  成都郫都区体育场: '郫都区',
  成都郫都区科技馆: '郫都区',
  成都足球训练基地: '武侯区',
  成都新都区体育馆: '新都区',
  成都郫都区体育馆: '郫都区',
  成都新都区体育场: '新都区',
  成都金牛区博物馆: '金牛区',
  成都龙泉驿区艺术中心: '龙泉驿区',
  成都双流区植物园: '双流区',
  成都天府新区文化馆: '天府新区',
  成都天府新区图书馆: '天府新区',
  成都温江区创意园: '温江区',
  成都青羊区博物馆: '青羊区',
  成都高新区科技馆: '高新区',
  成都郫都区艺术中心: '郫都区',
  成都温江区美术馆: '温江区',
  成都天府新区体育场: '天府新区',
  成都郫都区会展中心: '郫都区',
  成都都江堰市体育场: '都江堰市',
  成都成华区动物园: '成华区',
  成都市游泳馆: '青羊区',
  成都高新区美术馆: '高新区',
  成都双流区公园: '双流区',
  成都双流区体育馆: '双流区',
  重庆中国三峡博物馆: '渝中区',
  重庆园博园: '渝北区',
  重庆少年儿童图书馆: '渝中区',
  重庆武隆区植物园: '武隆区',
  重庆北碚区动物园: '北碚区',
  重庆巴南区科技馆: '巴南区',
  重庆科技馆: '江北区',
  重庆动物园: '九龙坡区',
  洪崖洞: '渝中区',
  重庆图书馆: '沙坪坝区',
  重庆际华园: '渝北区',
  重庆融创乐园: '沙坪坝区',
  重庆大渡口区体育场: '大渡口区',
  重庆北碚区会展中心: '北碚区',
  重庆北碚区文化馆: '北碚区',
  重庆大足区体育馆: '大足区',
  重庆江北区剧院: '江北区',
  重庆工业博物馆: '大渡口区',
  彩云湖湿地公园: '九龙坡区',
  重庆融创海世界: '沙坪坝区',
  重庆汉海海洋公园: '巴南区',
  仙女山国家森林公园: '武隆区',
  南山植物园: '南岸区',
  重庆江北区美术馆: '江北区',
  重庆大足区植物园: '大足区',
  缙云山自然保护区: '北碚区',
  重庆欢乐海底世界: '渝中区',
  白公馆: '沙坪坝区',
  重庆南岸区公园: '南岸区',
  湖广会馆: '渝中区',
  鹅岭公园: '渝中区',
  重庆武隆区青少年宫: '武隆区',
  重庆沙坪坝区会展中心: '沙坪坝区',
  重庆融创雪世界: '沙坪坝区',
  重庆两江新区艺术中心: '两江新区',
  重庆大足区海洋馆: '大足区',
  重庆渝中区创意园: '渝中区',
  重庆自然博物馆: '北碚区',
  磁器口古镇: '沙坪坝区',
  重庆大渡口区文化中心: '大渡口区',
  重庆中央公园: '渝北区',
  武隆喀斯特: '武隆区',
  南山: '南岸区',
  重庆沙坪坝区文化中心: '沙坪坝区',
  重庆九龙坡区科技馆: '九龙坡区',
  重庆渝中区海洋馆: '渝中区',
  歌乐山国家森林公园: '沙坪坝区',
  重庆大足区体育场: '大足区',
  重庆大足区文化馆: '大足区',
  重庆江北区图书馆: '江北区',
  重庆两江新区海洋馆: '两江新区',
  重庆武隆区公园: '武隆区',
  渣滓洞: '沙坪坝区',
  重庆北碚区图书馆: '北碚区',
  重庆渝北区艺术中心: '渝北区',
  重庆渝中区文化中心: '渝中区',
  重庆大足区动物园: '大足区',
  重庆南岸区创意园: '南岸区',
  重庆北碚区创意园: '北碚区',
  重庆沙坪坝区植物园: '沙坪坝区',
  重庆渝北区科技馆: '渝北区',
  重庆大足区创意园: '大足区',
  重庆渝北区博物馆: '渝北区',
  重庆巴南区美术馆: '巴南区',
  南山一棵树观景台: '南岸区',
  江北嘴: '江北区',
  重庆大渡口区动物园: '大渡口区',
  重庆北碚区海洋馆: '北碚区',
  十八梯: '渝中区',
  重庆红岩革命历史博物馆: '渝中区',
  重庆奥体中心: '九龙坡区',
  重庆沙坪坝区图书馆: '沙坪坝区',
  金佛山: '南川区',
  南滨路: '南岸区',
  重庆南岸区图书馆: '南岸区',
  重庆两江新区青少年宫: '两江新区',
  重庆武隆区文化馆: '武隆区',
  重庆沙坪坝区剧院: '沙坪坝区',
  重庆武隆区体育场: '武隆区',
  重庆南川区公园: '南川区',
  重庆南川区科技馆: '南川区',
  重庆江北区文化中心: '江北区',
  歌乐山烈士陵园: '沙坪坝区',
  重庆武隆区会展中心: '武隆区',
  重庆南川区艺术中心: '南川区',
  重庆两江新区图书馆: '两江新区',
  重庆九龙坡区体育馆: '九龙坡区',
  重庆九龙坡区图书馆: '九龙坡区',
  重庆南岸区博物馆: '南岸区',
  重庆火锅博物馆: '九龙坡区',
  重庆江北区会展中心: '江北区',
  重庆九龙坡区文化馆: '九龙坡区',
  重庆渝中区艺术中心: '渝中区',
  重庆欢乐谷: '渝北区',
  大足石刻: '大足区',
  重庆武隆区动物园: '武隆区',
  重庆两江新区动物园: '两江新区',
  江北嘴中央公园: '江北区',
  重庆巴南区图书馆: '巴南区',
  重庆两江新区会展中心: '两江新区',
  重庆巴南区剧院: '巴南区',
  重庆美术馆: '渝中区',
  重庆大渡口区海洋馆: '大渡口区',
  重庆渝北区创意园: '渝北区',
  重庆两江新区科技馆: '两江新区',
  重庆两江新区美术馆: '两江新区',
  重庆南川区体育馆: '南川区',
  重庆北碚区博物馆: '北碚区',
  重庆九龙坡区体育场: '九龙坡区',
  铁山坪森林公园: '江北区',
  周公馆: '渝中区',
  重庆江北区动物园: '江北区',
  重庆九龙坡区文化中心: '九龙坡区',
  重庆南岸区文化馆: '南岸区',
  重庆江北区博物馆: '江北区',
  重庆大渡口区文化馆: '大渡口区',
  重庆沙坪坝区体育场: '沙坪坝区',
  重庆巴南区青少年宫: '巴南区',
  重庆大渡口区美术馆: '大渡口区',
  重庆南岸区体育馆: '南岸区',
  重庆北碚区植物园: '北碚区',
  重庆大足区图书馆: '大足区',
  重庆欢乐谷玛雅海滩水公园: '渝北区',
  重庆九龙坡区创意园: '九龙坡区',
  重庆江北区青少年宫: '江北区',
  重庆大渡口区会展中心: '大渡口区',
  重庆建川博物馆聚落: '九龙坡区',
  北滨路: '江北区',
  重庆渝中区公园: '渝中区',
  重庆渝中区图书馆: '渝中区',
  重庆大足区艺术中心: '大足区',
  朝天门广场: '渝中区',
  重庆南川区文化中心: '南川区',
  重庆两江新区体育场: '两江新区',
  重庆沙坪坝区动物园: '沙坪坝区',
  重庆江北区体育场: '江北区',
  重庆渝北区剧院: '渝北区',
  重庆南岸区剧院: '南岸区',
  重庆渝中区会展中心: '渝中区',
  重庆巴南区文化馆: '巴南区',
  重庆南川区文化馆: '南川区',
  桂园: '渝中区',
  重庆江北区植物园: '江北区',
  重庆渝北区会展中心: '渝北区',
  重庆巴南区艺术中心: '巴南区',
  重庆大足区剧院: '大足区',
  重庆渝中区动物园: '渝中区',
  重庆九龙坡区会展中心: '九龙坡区',
  重庆沙坪坝区科技馆: '沙坪坝区',
  重庆南川区体育场: '南川区',
  重庆大渡口区博物馆: '大渡口区',
  重庆国际马戏城: '江北区',
  重庆大渡口区科技馆: '大渡口区',
  重庆渝北区文化馆: '渝北区',
  重庆巴南区体育馆: '巴南区',
  重庆两江新区剧院: '两江新区',
  重庆大足区文化中心: '大足区',
  重庆九龙坡区公园: '九龙坡区',
  重庆南川区植物园: '南川区',
  重庆九龙坡区美术馆: '九龙坡区',
  重庆南岸区艺术中心: '南岸区',
  重庆江北区科技馆: '江北区',
  重庆北碚区青少年宫: '北碚区',
  重庆南川区剧院: '南川区',
  重庆武隆区文化中心: '武隆区',
  重庆北碚区艺术中心: '北碚区',
  重庆江北区艺术中心: '江北区',
  重庆南岸区文化中心: '南岸区',
  重庆巴南区海洋馆: '巴南区',
  重庆沙坪坝区创意园: '沙坪坝区',
  重庆大剧院: '江北区',
  重庆巴南区博物馆: '巴南区',
  重庆渝北区海洋馆: '渝北区',
  重庆沙坪坝区艺术中心: '沙坪坝区',
  重庆武隆区创意园: '武隆区',
  重庆江北区海洋馆: '江北区',
  重庆沙坪坝区公园: '沙坪坝区',
  重庆沙坪坝区体育馆: '沙坪坝区',
  重庆武隆区海洋馆: '武隆区',
  重庆大渡口区创意园: '大渡口区',
  重庆武隆区体育馆: '武隆区',
  重庆北碚区美术馆: '北碚区',
  重庆南川区海洋馆: '南川区',
  重庆渝中区科技馆: '渝中区',
  重庆大渡口区植物园: '大渡口区',
  重庆两江新区文化馆: '两江新区',
  重庆武隆区图书馆: '武隆区',
  重庆渝中区美术馆: '渝中区',
  鹅岭二厂: '渝中区',
  重庆南岸区美术馆: '南岸区',
  重庆渝北区图书馆: '渝北区',
  重庆北碚区体育场: '北碚区',
  重庆武隆区美术馆: '武隆区',
  重庆南岸区科技馆: '南岸区',
  重庆北碚区公园: '北碚区',
  重庆渝北区青少年宫: '渝北区',
  重庆南岸区青少年宫: '南岸区',
  重庆巴南区体育场: '巴南区',
  重庆南岸区海洋馆: '南岸区',
  重庆北碚区剧院: '北碚区',
  重庆沙坪坝区美术馆: '沙坪坝区',
  重庆武隆区剧院: '武隆区',
  重庆大渡口区艺术中心: '大渡口区',
  重庆北碚区科技馆: '北碚区',
  重庆南岸区动物园: '南岸区',
  重庆两江新区创意园: '两江新区',
  重庆大渡口区体育馆: '大渡口区',
  重庆大渡口区图书馆: '大渡口区',
  重庆九龙坡区青少年宫: '九龙坡区',
  重庆沙坪坝区文化馆: '沙坪坝区',
  重庆九龙坡区海洋馆: '九龙坡区',
  重庆两江新区公园: '两江新区',
  重庆渝中区植物园: '渝中区',
  重庆大足区公园: '大足区',
  重庆南川区动物园: '南川区',
  重庆武隆区博物馆: '武隆区',
  重庆大足区科技馆: '大足区',
  重庆巴南区动物园: '巴南区',
  重庆南川区美术馆: '南川区',
  重庆渝北区体育馆: '渝北区',
  重庆渝北区公园: '渝北区',
  重庆九龙坡区艺术中心: '九龙坡区',
  重庆大渡口区公园: '大渡口区',
  重庆渝北区动物园: '渝北区',
  重庆南川区博物馆: '南川区',
  重庆渝中区体育馆: '渝中区',
  重庆渝中区体育场: '渝中区',
  重庆南川区会展中心: '南川区',
  重庆渝中区剧院: '渝中区',
  重庆渝北区植物园: '渝北区',
  重庆渝中区青少年宫: '渝中区',
  重庆北碚区文化中心: '北碚区',
  重庆南川区青少年宫: '南川区',
  重庆大足区会展中心: '大足区',
  重庆九龙坡区博物馆: '九龙坡区',
  重庆两江新区植物园: '两江新区',
  重庆大渡口区青少年宫: '大渡口区',
  重庆巴南区植物园: '巴南区',
  国泰艺术中心: '渝中区',
  重庆九龙坡区植物园: '九龙坡区',
  重庆江北区体育馆: '江北区',
  重庆巴南区公园: '巴南区',
  重庆渝中区博物馆: '渝中区',
  重庆江北区创意园: '江北区',
  重庆巴南区文化中心: '巴南区',
  重庆九龙坡区剧院: '九龙坡区',
  重庆沙坪坝区青少年宫: '沙坪坝区',
  重庆渝北区美术馆: '渝北区',
  重庆沙坪坝区博物馆: '沙坪坝区',
  重庆两江新区体育馆: '两江新区',
  重庆大足区博物馆: '大足区',
  重庆江北区文化馆: '江北区',
  解放碑步行街: '渝中区',
  重庆南岸区体育场: '南岸区',
  重庆南岸区会展中心: '南岸区',
  重庆渝北区文化中心: '渝北区',
  广东科学中心: '番禺区',
  广州青少年科技馆: '越秀区',
  广州少年儿童图书馆: '越秀区',
  广州地铁博物馆: '海珠区',
  广州市儿童公园: '白云区',
  广州动物园: '越秀区',
  广州海洋馆: '越秀区',
  正佳极地海洋世界: '天河区',
  正佳雨林生态植物园: '天河区',
  正佳自然科学博物馆: '天河区',
  广州融创文旅城: '花都区',
  永庆坊: '荔湾区',
  陈家祠: '荔湾区',
  岭南印象园: '番禺区',
  海珠国家湿地公园: '海珠区',
  华南植物园: '天河区',
  白云山: '白云区',
  大夫山森林公园: '番禺区',
  海鸥岛: '番禺区',
  广州新儿童活动中心: '白云区',
  广州开发区科技馆: '黄埔区',
  广州艺术博物院: '越秀区',
  南越王博物院: '越秀区',
  广州市文化馆新馆: '海珠区',
  广州大剧院: '天河区',
  广州塔: '海珠区',
  广州国际金融城: '天河区',
  广州北京路步行街: '越秀区',
  广州上下九步行街: '荔湾区',
  广州天河城: '天河区',
  广州太古汇: '天河区',
  广州正佳广场: '天河区',
  广州万菱汇: '天河区',
  广州凯德广场: '白云区',
  广州白云万达广场: '白云区',
  广州越秀公园: '越秀区',
  广州流花湖公园: '越秀区',
  广州荔湾湖公园: '荔湾区',
  广州海珠湖公园: '海珠区',
  广州天河公园: '天河区',
  广州珠江公园: '天河区',
  广州麓湖公园: '越秀区',
  广州东山湖公园: '越秀区',
  广州二沙岛: '越秀区',
  广州沙面岛: '荔湾区',
  广州长隆野生动物世界: '番禺区',
  广州长隆欢乐世界: '番禺区',
  广州长隆水上乐园: '番禺区',
  广州长隆飞鸟乐园: '番禺区',
  广州融创雪世界: '花都区',
  广州融创水世界: '花都区',
  广州融创体育世界: '花都区',
  广州花都湖公园: '花都区',
  广州增城白水寨: '增城区',
  广州从化温泉: '从化区',
  广州从化溪头村: '从化区',
  广州南沙湿地公园: '南沙区',
  广州南沙天后宫: '南沙区',
  广州黄埔军校旧址: '黄埔区',
  广州南海神庙: '黄埔区',
  广州南越王宫博物馆: '越秀区',
  广州北京路千年古道遗址: '越秀区',
  广州粤剧艺术博物馆: '荔湾区',
  广州三二九起义指挥部旧址: '越秀区',
  广州起义烈士陵园: '越秀区',
  广州鲁迅纪念馆: '越秀区',
  广州近代史博物馆: '越秀区',
  广州农民运动讲习所旧址: '越秀区',
  广州南越王墓博物馆: '越秀区',
  广州北京路天河城: '越秀区',
  广州天河城百货: '天河区',
  广州太古汇商场: '天河区',
  广州维多利广场: '天河区',
  广州天河体育中心: '天河区',
  广州珠江新城: '天河区',
  广州花城广场: '天河区',
  广州海心沙: '天河区',
  广州琶洲会展中心: '海珠区',
  广州塔摩天轮: '海珠区',
  广州塔极速云霄: '海珠区',
  广州塔户外观景平台: '海珠区',
  广州海心桥: '天河区',
  广州滨江公园: '海珠区',
  广州二沙岛体育公园: '越秀区',
  广州二沙岛艺术公园: '越秀区',
  广州海印公园: '海珠区',
  广州晓港公园: '海珠区',
  广州黄埔公园: '黄埔区',
  广州萝岗香雪公园: '黄埔区',
  广州天鹿湖森林公园: '黄埔区',
  广州九龙湖度假区: '花都区',
  广州花都石头记矿物园: '花都区',
  广州芙蓉嶂风景区: '花都区',
  广州九龙潭森林公园: '花都区',
  广州花都融创乐园: '花都区',
  广州花都融创雪世界: '花都区',
  广州花都融创水世界: '花都区',
  广州花都融创体育世界: '花都区',
  广州从化流溪河国家森林公园: '从化区',
  广州从化碧水湾温泉: '从化区',
  广州增城正果老街: '增城区',
  广东美术馆: '从化区',
  荔湾湖公园: '越秀区',
  广州白云区剧院: '白云区',
  流花湖公园: '南沙区',
  广州花都区动物园: '花都区',
  广州番禺区剧院: '番禺区',
  广州花都区剧院: '花都区',
  长隆野生动物世界: '增城区',
  沙湾古镇: '海珠区',
  天河公园: '南沙区',
  广州黄埔区美术馆: '黄埔区',
  宝墨园: '黄埔区',
  广州荔湾区博物馆: '荔湾区',
  广州荔湾区文化馆: '荔湾区',
  余荫山房: '白云区',
  广州越秀区博物馆: '越秀区',
  广州天河区青少年宫: '天河区',
  广州越秀区创意园: '越秀区',
  广州海珠区图书馆: '海珠区',
  广州黄埔区创意园: '黄埔区',
  广州番禺区博物馆: '番禺区',
  广州海珠区美术馆: '海珠区',
  广州荔湾区体育馆: '荔湾区',
  广州南沙区文化馆: '南沙区',
  越秀公园: '黄埔区',
  长隆水上乐园: '荔湾区',
  上下九: '南沙区',
  长隆欢乐世界: '番禺区',
  广州从化区剧院: '从化区',
  广州黄埔区公园: '黄埔区',
  珠江公园: '增城区',
  广州南沙区海洋馆: '南沙区',
  广州从化区图书馆: '从化区',
  海珠湖公园: '增城区',
  广州黄埔区体育馆: '黄埔区',
  云台花园: '南沙区',
  广州从化区文化中心: '从化区',
  广州黄埔区动物园: '黄埔区',
  广州南沙区科技馆: '南沙区',
  广州黄埔区体育场: '黄埔区',
  广州增城区美术馆: '增城区',
  广州花都区会展中心: '花都区',
  广州海珠区科技馆: '海珠区',
  广州天河区剧院: '天河区',
  广州增城区公园: '增城区',
  广州黄埔区剧院: '黄埔区',
  广州从化区科技馆: '从化区',
  广州越秀区科技馆: '越秀区',
  北京路: '荔湾区',
  广州南沙区植物园: '南沙区',
  广州天河区文化中心: '天河区',
  广州天河区博物馆: '天河区',
  广州白云区文化中心: '白云区',
  广州黄埔区文化中心: '黄埔区',
  广州南沙区青少年宫: '南沙区',
  广州番禺区公园: '番禺区',
  广州番禺区海洋馆: '番禺区',
  广州从化区体育场: '从化区',
  广州番禺区体育馆: '番禺区',
  广州越秀区会展中心: '越秀区',
  广州海珠区创意园: '海珠区',
  广州天河区动物园: '天河区',
  广州花都区美术馆: '花都区',
  广州荔湾区文化中心: '荔湾区',
  广州天河区体育场: '天河区',
  广州白云区创意园: '白云区',
  广州越秀区剧院: '越秀区',
  广州越秀区图书馆: '越秀区',
  广州天河区会展中心: '天河区',
  麓湖公园: '天河区',
  广州增城区剧院: '增城区',
  广州南沙区文化中心: '南沙区',
  广州南沙区公园: '南沙区',
  广州花都区海洋馆: '花都区',
  广州农民运动讲习所: '越秀区',
  广州白云区艺术中心: '白云区',
  广州越秀区文化中心: '越秀区',
  广州海珠区剧院: '海珠区',
  广州花都区科技馆: '花都区',
  广州荔湾区动物园: '荔湾区',
  广州增城区海洋馆: '增城区',
  广州番禺区科技馆: '番禺区',
  广州白云区体育馆: '白云区',
  广州白云区文化馆: '白云区',
  广州荔湾区美术馆: '荔湾区',
  广州花都区创意园: '花都区',
  广州白云区动物园: '白云区',
  广州海珠区青少年宫: '海珠区',
  广州黄埔区博物馆: '黄埔区',
  白云山风景名胜区: '白云区',
  广州起义纪念馆: '越秀区',
  天河城: '花都区',
  广州荔湾区创意园: '荔湾区',
  广州海珠区会展中心: '海珠区',
  广州增城区体育场: '增城区',
  广州花都区艺术中心: '花都区',
  广州从化区公园: '从化区',
  广州越秀区体育馆: '越秀区',
  广州荔湾区剧院: '荔湾区',
  白水寨风景名胜区: '增城区',
  广州白云区美术馆: '白云区',
  广州南沙区体育场: '南沙区',
  广州荔湾区植物园: '荔湾区',
  广州增城区科技馆: '增城区',
  广州天河区科技馆: '天河区',
  广州越秀区动物园: '越秀区',
  广州番禺区植物园: '番禺区',
  南沙湿地公园: '南沙区',
  广州白云区青少年宫: '白云区',
  广州荔湾区图书馆: '荔湾区',
  广州增城区艺术中心: '增城区',
  广州天河区创意园: '天河区',
  广州花都区植物园: '花都区',
  广州白云区海洋馆: '白云区',
  广州越秀区公园: '越秀区',
  广州花都区体育馆: '花都区',
  广州增城区博物馆: '增城区',
  广州番禺区文化中心: '番禺区',
  广州增城区青少年宫: '增城区',
  广州天河区体育馆: '天河区',
  广州天河区文化馆: '天河区',
  广州黄埔区艺术中心: '黄埔区',
  广州从化区创意园: '从化区',
  广州从化区青少年宫: '从化区',
  广州荔湾区科技馆: '荔湾区',
  广州增城区文化中心: '增城区',
  广州越秀区艺术中心: '越秀区',
  广州白云区博物馆: '白云区',
  广州天河区艺术中心: '天河区',
  广州从化区会展中心: '从化区',
  莲花山旅游区: '番禺区',
  广州番禺区体育场: '番禺区',
  广州南沙区体育馆: '南沙区',
  广州荔湾区会展中心: '荔湾区',
  广州花都区公园: '花都区',
  广州增城区创意园: '增城区',
  广州越秀区植物园: '越秀区',
  广州黄埔区图书馆: '黄埔区',
  广州黄埔区海洋馆: '黄埔区',
  广州花都区文化馆: '花都区',
  广州花都区图书馆: '花都区',
  广州白云区会展中心: '白云区',
  广州白云区体育场: '白云区',
  广州增城区体育馆: '增城区',
  广州天河区植物园: '天河区',
  广州从化区体育馆: '从化区',
  广州荔湾区公园: '荔湾区',
  广州增城区文化馆: '增城区',
  广州南沙区美术馆: '南沙区',
  广州越秀区体育场: '越秀区',
  广州从化区艺术中心: '从化区',
  广州从化区美术馆: '从化区',
  广州黄埔区科技馆: '黄埔区',
  广州南沙区会展中心: '南沙区',
  广州从化区海洋馆: '从化区',
  广州天河区图书馆: '天河区',
  广州番禺区文化馆: '番禺区',
  广州从化区植物园: '从化区',
  广州番禺区艺术中心: '番禺区',
  广州黄埔区会展中心: '黄埔区',
  广州海珠区海洋馆: '海珠区',
  广州越秀区文化馆: '越秀区',
  广州从化区博物馆: '从化区',
  广州越秀区美术馆: '越秀区',
  广州南沙区艺术中心: '南沙区',
  流溪河国家森林公园: '从化区',
  广州南沙区动物园: '南沙区',
  广州海珠区文化中心: '海珠区',
  广州黄埔区文化馆: '黄埔区',
  广州海珠区动物园: '海珠区',
  广州越秀区海洋馆: '越秀区',
  广州荔湾区艺术中心: '荔湾区',
  广州荔湾区海洋馆: '荔湾区',
  广州白云区图书馆: '白云区',
  广州海珠区植物园: '海珠区',
  广州天河区海洋馆: '天河区',
  广州海珠区公园: '海珠区',
  广州番禺区会展中心: '番禺区',
  广州海珠区艺术中心: '海珠区',
  广州越秀区青少年宫: '越秀区',
  广州从化区动物园: '从化区',
  广州海珠区体育场: '海珠区',
  广州南沙区博物馆: '南沙区',
  广州增城区图书馆: '增城区',
  广州番禺区图书馆: '番禺区',
  广州花都区体育场: '花都区',
  广州增城区动物园: '增城区',
  广州花都区博物馆: '花都区',
  广州荔湾区体育场: '荔湾区',
  广州番禺区青少年宫: '番禺区',
  广州番禺区美术馆: '番禺区',
  广州南沙区剧院: '南沙区',
  广州黄埔区青少年宫: '黄埔区',
  广州南沙区创意园: '南沙区',
  广州白云区科技馆: '白云区',
  广州花都区青少年宫: '花都区',
  广州黄埔区植物园: '黄埔区',
  广州从化区文化馆: '从化区',
  广州增城区植物园: '增城区',
  广州海珠区体育馆: '海珠区',
  广州天河区公园: '天河区',
  广州增城区会展中心: '增城区',
  广州海珠区文化馆: '海珠区',
  广州花都区文化中心: '花都区',
  广州番禺区创意园: '番禺区',
  广州天河区美术馆: '天河区',
  广州白云区公园: '白云区',
  广州海珠区博物馆: '海珠区',
  广州荔湾区青少年宫: '荔湾区',
  广州番禺区动物园: '番禺区',
  广州南沙区图书馆: '南沙区',
  广州白云区植物园: '白云区',
  '浙江省博物馆（之江馆）': '西湖区',
  '浙江省博物馆（孤山馆）': '西湖区',
  '浙江自然博物院（杭州馆）': '拱墅区',
  浙江省科技馆: '拱墅区',
  浙江省地质博物馆: '西湖区',
  浙江省非物质文化遗产馆: '西湖区',
  浙江图书馆: '西湖区',
  中国杭州低碳科技馆: '滨江区',
  杭州亚运会博物馆: '滨江区',
  良渚博物院: '余杭区',
  中国丝绸博物馆: '西湖区',
  中国水利博物馆: '萧山区',
  中国茶叶博物馆: '西湖区',
  中国湿地博物馆: '西湖区',
  中国动漫博物馆: '滨江区',
  杭州博物馆: '上城区',
  良渚古城遗址公园: '余杭区',
  杭州野生动物世界: '富阳区',
  杭州植物园: '西湖区',
  西溪国家湿地公园: '西湖区',
  西湖风景名胜区: '西湖区',
  杭州乐园: '萧山区',
  杭州少年儿童图书馆: '西湖区',
  杭州科技馆: '拱墅区',
  杭州中国茶叶博物馆龙井馆: '西湖区',
  杭州西湖博物馆: '上城区',
  杭州京杭大运河博物馆: '拱墅区',
  杭州工艺美术博物馆: '拱墅区',
  杭州中国湿地博物馆: '西湖区',
  杭州青少年活动中心: '西湖区',
  杭州嘟嘟城: '江干区',
  杭州西湖: '西湖区',
  杭州灵隐寺: '西湖区',
  杭州雷峰塔: '西湖区',
  杭州岳庙: '西湖区',
  杭州六和塔: '西湖区',
  杭州虎跑公园: '西湖区',
  杭州九溪烟树: '西湖区',
  杭州云栖竹径: '西湖区',
  杭州龙井村: '西湖区',
  杭州满陇桂雨: '西湖区',
  杭州太子湾公园: '西湖区',
  杭州花港观鱼: '西湖区',
  杭州苏堤: '西湖区',
  杭州白堤: '西湖区',
  杭州曲院风荷: '西湖区',
  杭州平湖秋月: '西湖区',
  杭州柳浪闻莺: '西湖区',
  杭州南屏晚钟: '西湖区',
  杭州双峰插云: '西湖区',
  杭州吴山天风: '上城区',
  杭州涌金公园: '上城区',
  杭州钱王祠: '上城区',
  杭州鼓楼: '上城区',
  杭州河坊街: '上城区',
  杭州南宋御街: '上城区',
  杭州湖滨银泰: '上城区',
  杭州武林广场: '拱墅区',
  杭州运河广场: '拱墅区',
  杭州小河直街: '拱墅区',
  杭州桥西直街: '拱墅区',
  杭州拱宸桥: '拱墅区',
  杭州西溪湿地东区: '西湖区',
  杭州西溪湿地西区: '西湖区',
  杭州湘湖: '萧山区',
  杭州极地海洋世界: '萧山区',
  杭州跨湖桥遗址博物馆: '萧山区',
  杭州奥体中心: '滨江区',
  杭州滨江公园: '滨江区',
  杭州梦想小镇: '余杭区',
  杭州未来科技城: '余杭区',
  杭州临平新城: '临平区',
  杭州九堡大桥: '江干区',
  杭州钱江新城: '江干区',
  杭州城市阳台: '江干区',
  杭州大剧院: '江干区',
  杭州国际会议中心: '江干区',
  杭州奥体博览城: '滨江区',
  杭州白马湖国际会展中心: '滨江区',
  杭州之江文化中心: '西湖区',
  杭州文学馆: '西湖区',
  杭州西湖音乐喷泉: '西湖区',
  杭州西湖游船: '西湖区',
  杭州西湖三潭印月: '西湖区',
  杭州西湖湖心亭: '西湖区',
  杭州西湖阮公墩: '西湖区',
  杭州西湖杨公堤: '西湖区',
  杭州西湖苏堤春晓: '西湖区',
  杭州西湖断桥残雪: '西湖区',
  杭州西湖雷峰夕照: '西湖区',
  杭州西湖南屏晚钟: '西湖区',
  杭州西湖曲院风荷: '西湖区',
  杭州西湖花港观鱼: '西湖区',
  杭州西湖柳浪闻莺: '西湖区',
  杭州西湖双峰插云: '西湖区',
  杭州西湖平湖秋月: '西湖区',
  杭州西湖吴山天风: '上城区',
  杭州运河文化广场: '拱墅区',
  杭州运河夜游: '拱墅区',
  杭州运河游船: '拱墅区',
  杭州西溪湿地摇橹船: '西湖区',
  杭州西溪湿地龙舟赛: '西湖区',
  杭州西溪湿地植物园: '西湖区',
  杭州西溪湿地博物馆: '西湖区',
  杭州湘湖游船: '萧山区',
  杭州湘湖音乐喷泉: '萧山区',
  杭州极地海洋世界海豚表演: '萧山区',
  杭州极地海洋世界白鲸表演: '萧山区',
  杭州奥体中心体育场: '滨江区',
  杭州奥体中心游泳馆: '滨江区',
  杭州奥体中心网球中心: '滨江区',
  杭州梦想小镇创业大街: '余杭区',
  杭州未来科技城梦想小镇: '余杭区',
  杭州未来科技城学术交流中心: '余杭区',
  杭州未来科技城海创园: '余杭区',
  杭州未来科技城人才公园: '余杭区',
  杭州临平新城体育公园: '临平区',
  杭州临平新城文化艺术中心: '临平区',
  杭州临平新城市民广场: '临平区',
  杭州九堡大桥公园: '江干区',
  杭州钱江新城灯光秀: '江干区',
  杭州城市阳台灯光秀: '江干区',
  杭州大剧院歌剧厅: '江干区',
  杭州大剧院音乐厅: '江干区',
  杭州国际会议中心大剧场: '江干区',
  杭州奥体博览城网球中心: '滨江区',
  杭州奥体博览城游泳馆: '滨江区',
  杭州白马湖国际会展中心展览厅: '滨江区',
  杭州之江文化中心图书馆: '西湖区',
  杭州之江文化中心博物馆: '西湖区',
  杭州之江文化中心美术馆: '西湖区',
  杭州之江文化中心科技馆: '西湖区',
  杭州文学馆展览厅: '西湖区',
  杭州文学馆阅读室: '西湖区',
  杭州淳安县海洋馆: '淳安县',
  杭州临安区青少年宫: '临安区',
  杭州桐庐县公园: '桐庐县',
  宋城: '西湖区',
  杭州西湖区图书馆: '西湖区',
  杭州上城区体育馆: '上城区',
  杭州萧山区海洋馆: '萧山区',
  西湖博物馆: '下城区',
  杭州余杭区美术馆: '余杭区',
  西溪湿地: '江干区',
  六和塔: '滨江区',
  杭州滨江区体育馆: '滨江区',
  杭州临安区艺术中心: '临安区',
  杭州下城区美术馆: '下城区',
  烂苹果乐园: '萧山区',
  杭州下城区剧院: '下城区',
  白龙潭景区: '西湖区',
  小河直街: '拱墅区',
  雷峰塔: '富阳区',
  杭州建德市体育场: '建德市',
  杭州江干区博物馆: '江干区',
  杭州淳安县文化馆: '淳安县',
  杭州淳安县艺术中心: '淳安县',
  杭州西湖区公园: '西湖区',
  杭州富阳区动物园: '富阳区',
  杭州西湖区艺术中心: '西湖区',
  西湖景区: '西湖区',
  龙井: '淳安县',
  云栖竹径: '西湖区',
  杭州淳安县美术馆: '淳安县',
  杭州上城区海洋馆: '上城区',
  中国扇博物馆: '拱墅区',
  长乔极地海洋公园: '下城区',
  杭州余杭区艺术中心: '余杭区',
  南宋官窑博物馆: '滨江区',
  杭州上城区公园: '上城区',
  杭州上城区植物园: '上城区',
  杭州滨江区文化馆: '滨江区',
  中国美术学院美术馆: '西湖区',
  杭州滨江区科技馆: '滨江区',
  杭州临安区公园: '临安区',
  杭州拱墅区剧院: '拱墅区',
  杭州萧山区植物园: '萧山区',
  杭州萧山区动物园: '萧山区',
  杭州萧山区图书馆: '萧山区',
  杭州下城区文化馆: '下城区',
  杭州上城区创意园: '上城区',
  浙江自然博物院杭州馆: '下城区',
  中国刀剪剑博物馆: '江干区',
  杭州下城区创意园: '下城区',
  杭州桐庐县海洋馆: '桐庐县',
  杭州桐庐县剧院: '桐庐县',
  中国伞博物馆: '桐庐县',
  杭州滨江区公园: '滨江区',
  杭州建德市动物园: '建德市',
  杭州下城区青少年宫: '下城区',
  杭州滨江区体育场: '滨江区',
  杭州江干区青少年宫: '江干区',
  胡庆余堂中药博物馆: '下城区',
  京杭大运河杭州景区: '拱墅区',
  拱宸桥: '拱墅区',
  九溪: '临安区',
  杭州萧山区博物馆: '萧山区',
  杭州富阳区体育场: '富阳区',
  杭州野生动物园: '滨江区',
  杭州下城区体育馆: '下城区',
  杭州富阳区公园: '富阳区',
  杭州江干区美术馆: '江干区',
  杭州临安区会展中心: '临安区',
  杭州萧山区体育场: '萧山区',
  杭州富阳区文化中心: '富阳区',
  杭州萧山区创意园: '萧山区',
  灵山风景区: '西湖区',
  杭州淳安县博物馆: '淳安县',
  杭州淳安县剧院: '淳安县',
  杭州江干区体育馆: '江干区',
  中国杭帮菜博物馆: '西湖区',
  韩美林艺术馆: '西湖区',
  中国京杭大运河博物馆: '富阳区',
  杭州滨江区美术馆: '滨江区',
  杭州滨江区青少年宫: '滨江区',
  湘湖: '萧山区',
  杭州余杭区创意园: '余杭区',
  杭州滨江区海洋馆: '滨江区',
  杭州西湖区科技馆: '西湖区',
  杭州拱墅区体育馆: '拱墅区',
  杭州建德市植物园: '建德市',
  虎跑: '下城区',
  杭州下城区艺术中心: '下城区',
  杭州西湖区文化中心: '西湖区',
  杭州拱墅区艺术中心: '拱墅区',
  浙江省博物馆之江馆区: '西湖区',
  杭州拱墅区创意园: '拱墅区',
  杭州拱墅区海洋馆: '拱墅区',
  浙江美术馆: '江干区',
  杭州临安区剧院: '临安区',
  杭州淳安县科技馆: '淳安县',
  杭州建德市文化中心: '建德市',
  杭州桐庐县体育馆: '桐庐县',
  杭州富阳区艺术中心: '富阳区',
  杭州江干区体育场: '江干区',
  浙江省博物馆武林馆区: '下城区',
  西溪湿地洪园: '余杭区',
  杭州建德市海洋馆: '建德市',
  杭州临安区文化馆: '临安区',
  杭州桐庐县创意园: '桐庐县',
  杭州余杭区剧院: '余杭区',
  杭州下城区科技馆: '下城区',
  杭州江干区文化馆: '江干区',
  杭州江干区科技馆: '江干区',
  杭州下城区图书馆: '下城区',
  杭州富阳区博物馆: '富阳区',
  杭州桐庐县美术馆: '桐庐县',
  杭州富阳区剧院: '富阳区',
  西湖音乐喷泉: '西湖区',
  杭州上城区科技馆: '上城区',
  杭州西湖区会展中心: '西湖区',
  杭州淳安县体育馆: '淳安县',
  杭州拱墅区文化馆: '拱墅区',
  杭州拱墅区公园: '拱墅区',
  灵隐寺: '建德市',
  杭州拱墅区科技馆: '拱墅区',
  杭州富阳区植物园: '富阳区',
  杭州萧山区科技馆: '萧山区',
  岳庙: '滨江区',
  杭州临安区科技馆: '临安区',
  杭州淳安县公园: '淳安县',
  杭州余杭区文化中心: '余杭区',
  杭州桐庐县文化中心: '桐庐县',
  杭州余杭区图书馆: '余杭区',
  杭州余杭区海洋馆: '余杭区',
  杭州余杭区文化馆: '余杭区',
  杭州西湖区文化馆: '西湖区',
  跨湖桥遗址博物馆: '萧山区',
  杭州下城区体育场: '下城区',
  杭州拱墅区体育场: '拱墅区',
  杭州临安区体育场: '临安区',
  杭州建德市科技馆: '建德市',
  杭州上城区体育场: '上城区',
  杭州临安区图书馆: '临安区',
  杭州建德市博物馆: '建德市',
  杭州桐庐县青少年宫: '桐庐县',
  杭州富阳区图书馆: '富阳区',
  虎跑公园: '西湖区',
  杭州临安区美术馆: '临安区',
  杭州下城区动物园: '下城区',
  杭州滨江区图书馆: '滨江区',
  杭州萧山区美术馆: '萧山区',
  杭州西湖区体育场: '西湖区',
  杭州余杭区会展中心: '余杭区',
  杭州桐庐县文化馆: '桐庐县',
  杭州淳安县体育场: '淳安县',
  杭州桐庐县图书馆: '桐庐县',
  杭州西湖区体育馆: '西湖区',
  湘湖旅游度假区: '萧山区',
  杭州淳安县青少年宫: '淳安县',
  杭州上城区美术馆: '上城区',
  杭州临安区创意园: '临安区',
  杭州余杭区植物园: '余杭区',
  杭州临安区体育馆: '临安区',
  杭州临安区植物园: '临安区',
  杭州余杭区科技馆: '余杭区',
  杭州临安区海洋馆: '临安区',
  杭州上城区会展中心: '上城区',
  满觉陇: '西湖区',
  杭州拱墅区博物馆: '拱墅区',
  杭州西湖区博物馆: '西湖区',
  杭州江干区创意园: '江干区',
  东方文化园: '萧山区',
  杭州富阳区文化馆: '富阳区',
  杭州江干区文化中心: '江干区',
  杭州上城区动物园: '上城区',
  杭州滨江区艺术中心: '滨江区',
  杭州萧山区会展中心: '萧山区',
  杭州滨江区创意园: '滨江区',
  九溪十八涧: '西湖区',
  杭州江干区图书馆: '江干区',
  杭州建德市创意园: '建德市',
  杭州上城区艺术中心: '上城区',
  杭州西湖区创意园: '西湖区',
  杭州余杭区公园: '余杭区',
  杭州江干区动物园: '江干区',
  杭州建德市文化馆: '建德市',
  杭州萧山区公园: '萧山区',
  杭州建德市体育馆: '建德市',
  杭州建德市艺术中心: '建德市',
  杭州上城区文化中心: '上城区',
  杭州淳安县文化中心: '淳安县',
  杭州富阳区青少年宫: '富阳区',
  杭州桐庐县博物馆: '桐庐县',
  杭州上城区博物馆: '上城区',
  杭州江干区剧院: '江干区',
  杭州下城区海洋馆: '下城区',
  杭州余杭区体育馆: '余杭区',
  杭州建德市会展中心: '建德市',
  杭州上城区剧院: '上城区',
  杭州淳安县植物园: '淳安县',
  杭州拱墅区植物园: '拱墅区',
  杭州西湖区美术馆: '西湖区',
  杭州拱墅区青少年宫: '拱墅区',
  杭州江干区公园: '江干区',
  杭州拱墅区文化中心: '拱墅区',
  杭州上城区图书馆: '上城区',
  杭州下城区文化中心: '下城区',
  杭州西湖区动物园: '西湖区',
  杭州滨江区动物园: '滨江区',
  杭州萧山区剧院: '萧山区',
  杭州江干区植物园: '江干区',
  杭州拱墅区美术馆: '拱墅区',
  杭州淳安县动物园: '淳安县',
  杭州富阳区海洋馆: '富阳区',
  杭州萧山区文化中心: '萧山区',
  杭州滨江区植物园: '滨江区',
  杭州富阳区美术馆: '富阳区',
  杭州余杭区动物园: '余杭区',
  杭州余杭区博物馆: '余杭区',
  杭州下城区会展中心: '下城区',
  湖滨步行街: '上城区',
  杭州西湖区青少年宫: '西湖区',
  杭州富阳区科技馆: '富阳区',
  杭州建德市剧院: '建德市',
  杭州建德市图书馆: '建德市',
  杭州桐庐县体育场: '桐庐县',
  杭州桐庐县动物园: '桐庐县',
  杭州拱墅区会展中心: '拱墅区',
  杭州萧山区青少年宫: '萧山区',
  杭州下城区植物园: '下城区',
  杭州富阳区体育馆: '富阳区',
  杭州淳安县会展中心: '淳安县',
  杭州西湖区海洋馆: '西湖区',
  杭州上城区青少年宫: '上城区',
  杭州西湖区剧院: '西湖区',
  杭州江干区艺术中心: '江干区',
  杭州滨江区博物馆: '滨江区',
  清河坊街: '上城区',
  杭州桐庐县植物园: '桐庐县',
  杭州萧山区文化馆: '萧山区',
  杭州滨江区会展中心: '滨江区',
  杭州下城区博物馆: '下城区',
  杭州桐庐县会展中心: '桐庐县',
  杭州临安区动物园: '临安区',
  杭州拱墅区图书馆: '拱墅区',
  杭州建德市公园: '建德市',
  杭州江干区会展中心: '江干区',
  超山风景区: '临平区',
  太子湾公园: '西湖区',
  龙井村: '西湖区',
  西湖音乐节: '西湖区',
  江苏省科学技术馆: '鼓楼区',
  玄武湖公园: '玄武区',
  红山森林动物园: '玄武区',
  玛雅海滩水公园: '长安区',
  秦淮非遗馆: '秦淮区',
  夫子庙秦淮风光带: '秦淮区',
  南京图书馆: '玄武区',
  金陵图书馆: '建邺区',
  南京市少年儿童图书馆: '玄武区',
  南京奥林匹克体育中心: '建邺区',
  南京高淳区青少年宫: '高淳区',
  南京溧水区美术馆: '溧水区',
  南京浦口区动物园: '浦口区',
  南京科技馆: '雨花台区',
  老门东: '秦淮区',
  青奥公园: '建邺区',
  阳山碑材: '江宁区',
  游子山: '高淳区',
  南京江宁区公园: '江宁区',
  南京鼓楼区植物园: '鼓楼区',
  南京雨花台区科技馆: '雨花台区',
  南京市博物馆: '秦淮区',
  六朝博物馆: '玄武区',
  莫愁湖公园: '建邺区',
  银杏湖乐园: '江宁区',
  五台山体育中心: '鼓楼区',
  雨花台烈士陵园: '雨花台区',
  梅园新村纪念馆: '玄武区',
  大金山国防园: '溧水区',
  南京六合区科技馆: '六合区',
  南京建邺区动物园: '建邺区',
  南京六合区会展中心: '六合区',
  南京高淳区会展中心: '高淳区',
  南京溧水区体育馆: '溧水区',
  中山植物园: '玄武区',
  中山陵: '玄武区',
  南京江宁区体育场: '江宁区',
  南京江宁区剧院: '江宁区',
  南京浦口区剧院: '浦口区',
  南京雨花台区会展中心: '雨花台区',
  南京玄武区美术馆: '玄武区',
  江宁织造博物馆: '玄武区',
  南京国防园: '鼓楼区',
  南京溧水区艺术中心: '溧水区',
  南京溧水区创意园: '溧水区',
  南京海底世界: '玄武区',
  明孝陵: '玄武区',
  南京雨花台区剧院: '雨花台区',
  南京玄武区体育馆: '玄武区',
  南京鼓楼区创意园: '鼓楼区',
  总统府: '玄武区',
  中华门瓮城: '秦淮区',
  珍珠泉风景区: '浦口区',
  南京雨花台区图书馆: '雨花台区',
  南京云锦博物馆: '建邺区',
  南京浦口区会展中心: '浦口区',
  南京秦淮区图书馆: '秦淮区',
  南京雨花台区博物馆: '雨花台区',
  南京鼓楼区图书馆: '鼓楼区',
  南京江宁区会展中心: '江宁区',
  南京博物院: '玄武区',
  南京雨花台区文化中心: '雨花台区',
  南京建邺区植物园: '建邺区',
  南京浦口区文化馆: '浦口区',
  南京江宁区文化中心: '江宁区',
  南京鼓楼区海洋馆: '鼓楼区',
  南京浦口区文化中心: '浦口区',
  侵华日军南京大屠杀遇难同胞纪念馆: '建邺区',
  南京浦口区体育馆: '浦口区',
  南京江宁区植物园: '江宁区',
  南京欢乐谷: '栖霞区',
  南京雨花台区美术馆: '雨花台区',
  南京鼓楼区体育馆: '鼓楼区',
  南京高淳区博物馆: '高淳区',
  傅家边: '溧水区',
  桂子山石柱林: '六合区',
  南京建邺区科技馆: '建邺区',
  南京栖霞区公园: '栖霞区',
  南京秦淮区会展中心: '秦淮区',
  南京平山森林公园: '六合区',
  颐和路: '鼓楼区',
  阅江楼: '鼓楼区',
  南京中国科举博物馆: '秦淮区',
  南京绿博园: '建邺区',
  渡江胜利纪念馆: '鼓楼区',
  东庐山: '溧水区',
  南京溧水区图书馆: '溧水区',
  南京秦淮区博物馆: '秦淮区',
  南京雨花台区体育场: '雨花台区',
  南京鼓楼区青少年宫: '鼓楼区',
  南京玄武区博物馆: '玄武区',
  南京栖霞区文化馆: '栖霞区',
  南京江宁区文化馆: '江宁区',
  南京溧水区青少年宫: '溧水区',
  南京秦淮区科技馆: '秦淮区',
  牛首山文化旅游区: '江宁区',
  南京江宁区美术馆: '江宁区',
  南京江宁区博物馆: '江宁区',
  南京六合区美术馆: '六合区',
  南京江宁区图书馆: '江宁区',
  南京鼓楼区博物馆: '鼓楼区',
  南京六合区体育馆: '六合区',
  南京秦淮区植物园: '秦淮区',
  南京六合区图书馆: '六合区',
  老山国家森林公园: '浦口区',
  弘阳欢乐世界: '浦口区',
  南京六合区植物园: '六合区',
  南京玄武区文化中心: '玄武区',
  南京地质博物馆: '玄武区',
  高淳老街: '高淳区',
  栖霞山风景区: '栖霞区',
  南京浦口区植物园: '浦口区',
  南京江宁区艺术中心: '江宁区',
  南京古生物博物馆: '玄武区',
  南京玄武区图书馆: '玄武区',
  南京建邺区图书馆: '建邺区',
  南京建邺区美术馆: '建邺区',
  南京栖霞区文化中心: '栖霞区',
  南京秦淮区美术馆: '秦淮区',
  南京建邺区青少年宫: '建邺区',
  南京城墙博物馆: '玄武区',
  南京浦口区公园: '浦口区',
  南京六合区文化馆: '六合区',
  南京溧水区科技馆: '溧水区',
  南京栖霞区体育场: '栖霞区',
  南京玄武区剧院: '玄武区',
  大报恩寺遗址公园: '秦淮区',
  金牛湖: '六合区',
  南京鼓楼区体育场: '鼓楼区',
  南京高淳区科技馆: '高淳区',
  南京玄武区会展中心: '玄武区',
  南京六合区艺术中心: '六合区',
  南京玄武区体育场: '玄武区',
  南京栖霞区剧院: '栖霞区',
  南京建邺区公园: '建邺区',
  瞻园: '秦淮区',
  南京浦口区体育场: '浦口区',
  南京雨花台区体育馆: '雨花台区',
  汤山古猿人洞: '江宁区',
  天生桥: '溧水区',
  南京秦淮区文化馆: '秦淮区',
  南京栖霞区科技馆: '栖霞区',
  南京六合区海洋馆: '六合区',
  南京溧水区体育场: '溧水区',
  南京六合区剧院: '六合区',
  南京鼓楼区美术馆: '鼓楼区',
  南京玄武区海洋馆: '玄武区',
  南京鼓楼区剧院: '鼓楼区',
  南京建邺区文化馆: '建邺区',
  南京六合区青少年宫: '六合区',
  南京浦口区科技馆: '浦口区',
  南京秦淮区体育馆: '秦淮区',
  南京雨花台区创意园: '雨花台区',
  南京雨花台区文化馆: '雨花台区',
  南京高淳区体育馆: '高淳区',
  南京高淳区剧院: '高淳区',
  南京栖霞区艺术中心: '栖霞区',
  南京溧水区会展中心: '溧水区',
  南京高淳区文化中心: '高淳区',
  南京江宁区科技馆: '江宁区',
  南京秦淮区动物园: '秦淮区',
  南京高淳区创意园: '高淳区',
  南京高淳区植物园: '高淳区',
  南京建邺区体育馆: '建邺区',
  南京建邺区会展中心: '建邺区',
  南京建邺区创意园: '建邺区',
  南京浦口区海洋馆: '浦口区',
  高淳陶瓷小镇: '高淳区',
  南京江宁区青少年宫: '江宁区',
  南京六合区体育场: '六合区',
  南京玄武区创意园: '玄武区',
  南京秦淮区公园: '秦淮区',
  南京秦淮区创意园: '秦淮区',
  南京溧水区植物园: '溧水区',
  南京玄武区科技馆: '玄武区',
  南京浦口区美术馆: '浦口区',
  汤山温泉旅游度假区: '江宁区',
  南京溧水区剧院: '溧水区',
  南京秦淮区文化中心: '秦淮区',
  南京栖霞区创意园: '栖霞区',
  南京溧水区海洋馆: '溧水区',
  南京浦口区创意园: '浦口区',
  南京秦淮区青少年宫: '秦淮区',
  南京溧水区博物馆: '溧水区',
  南京栖霞区青少年宫: '栖霞区',
  南京金箔艺术馆: '江宁区',
  南京鼓楼区文化中心: '鼓楼区',
  南京雨花台区青少年宫: '雨花台区',
  南京玄武区公园: '玄武区',
  南京浦口区博物馆: '浦口区',
  南京鼓楼区艺术中心: '鼓楼区',
  南京六合区公园: '六合区',
  南京六合区动物园: '六合区',
  南京溧水区文化中心: '溧水区',
  南京浦口区艺术中心: '浦口区',
  美龄宫: '玄武区',
  桠溪国际慢城: '高淳区',
  南京栖霞区体育馆: '栖霞区',
  南京雨花台区海洋馆: '雨花台区',
  南京栖霞区图书馆: '栖霞区',
  南京高淳区海洋馆: '高淳区',
  南京建邺区体育场: '建邺区',
  南京高淳区图书馆: '高淳区',
  南京江宁区体育馆: '江宁区',
  南京直立人化石遗址博物馆: '江宁区',
  南京高淳区文化馆: '高淳区',
  南京鼓楼区动物园: '鼓楼区',
  南京雨花台区植物园: '雨花台区',
  南京秦淮区海洋馆: '秦淮区',
  周园: '溧水区',
  南京玄武区文化馆: '玄武区',
  南京玄武区艺术中心: '玄武区',
  南京栖霞区博物馆: '栖霞区',
  南京六合区博物馆: '六合区',
  南京秦淮区剧院: '秦淮区',
  南京六合区创意园: '六合区',
  南京栖霞区动物园: '栖霞区',
  南京浦口区图书馆: '浦口区',
  南京溧水区公园: '溧水区',
  南京高淳区公园: '高淳区',
  南京秦淮区艺术中心: '秦淮区',
  南京江宁区动物园: '江宁区',
  南京雨花台区公园: '雨花台区',
  南京雨花台区艺术中心: '雨花台区',
  南京栖霞区植物园: '栖霞区',
  南京秦淮区体育场: '秦淮区',
  南京溧水区动物园: '溧水区',
  南京建邺区剧院: '建邺区',
  南京鼓楼区科技馆: '鼓楼区',
  南京鼓楼区会展中心: '鼓楼区',
  南京建邺区博物馆: '建邺区',
  南京高淳区体育场: '高淳区',
  南京建邺区艺术中心: '建邺区',
  南京建邺区海洋馆: '建邺区',
  南京高淳区动物园: '高淳区',
  南京雨花台区动物园: '雨花台区',
  南京栖霞区海洋馆: '栖霞区',
  鸡鸣寺: '玄武区',
  无想山: '溧水区',
  南京江宁区创意园: '江宁区',
  南京江宁区海洋馆: '江宁区',
  南京玄武区植物园: '玄武区',
  固城湖: '高淳区',
  南京六合区文化中心: '六合区',
  南京建邺区文化中心: '建邺区',
  南京玄武区青少年宫: '玄武区',
  南京玄武区动物园: '玄武区',
  南京鼓楼区公园: '鼓楼区',
  南京鼓楼区文化馆: '鼓楼区',
  南京溧水区文化馆: '溧水区',
  南京浦口区青少年宫: '浦口区',
  南京栖霞区会展中心: '栖霞区',
  南京高淳区艺术中心: '高淳区',
  南京高淳区美术馆: '高淳区',
  南京栖霞区美术馆: '栖霞区',
  上海自然博物馆: '静安区',
  上海天文馆: '浦东新区',
  上海儿童博物馆: '长宁区',
  上海地铁博物馆: '闵行区',
  上海海洋水族馆: '浦东新区',
  上海海昌海洋公园: '浦东新区',
  上海野生动物园: '浦东新区',
  上海欢乐谷: '松江区',
  上海迪士尼乐园: '浦东新区',
  上海汽车博物馆: '嘉定区',
  东方明珠塔: '浦东新区',
  上海中心大厦: '浦东新区',
  徐家汇书院: '徐汇区',
  世纪公园: '浦东新区',
  共青森林公园: '杨浦区',
  辰山植物园: '松江区',
  徐汇滨江滑板公园: '徐汇区',
  长风海洋世界: '普陀区',
  上海植物园: '徐汇区',
  上海昆虫博物馆: '徐汇区',
  上海消防博物馆: '长宁区',
  上海科技馆分馆: '静安区',
  上海少年儿童图书馆: '长宁区',
  世界技能博物馆: '杨浦区',
  上海图书馆: '徐汇区',
  上海美术馆: '浦东新区',
  上海大剧院: '黄浦区',
  上海音乐厅: '黄浦区',
  上海马戏城: '静安区',
  上海儿童艺术剧场: '黄浦区',
  上海东方艺术中心: '浦东新区',
  上海梅赛德斯奔驰文化中心: '浦东新区',
  上海八万人体育场: '徐汇区',
  上海体育馆: '徐汇区',
  上海源深体育中心: '浦东新区',
  上海浦东游泳馆: '浦东新区',
  上海静安体育中心: '静安区',
  上海长风公园: '普陀区',
  上海中山公园: '长宁区',
  上海人民公园: '黄浦区',
  上海外滩: '黄浦区',
  上海陆家嘴: '浦东新区',
  上海南京东路步行街: '黄浦区',
  上海淮海中路: '黄浦区',
  上海徐家汇商圈: '徐汇区',
  上海静安寺: '静安区',
  上海城隍庙: '黄浦区',
  上海豫园: '黄浦区',
  上海古猗园: '嘉定区',
  上海大观园: '青浦区',
  上海朱家角古镇: '青浦区',
  上海枫泾古镇: '金山区',
  上海七宝古镇: '闵行区',
  上海田子坊: '黄浦区',
  上海新天地: '黄浦区',
  上海科技馆主馆: '浦东新区',
  上海东方明珠太空舱: '浦东新区',
  上海东方明珠悬空观光廊: '浦东新区',
  上海中心大厦观光厅: '浦东新区',
  上海金茂大厦观光厅: '浦东新区',
  上海环球金融中心观光厅: '浦东新区',
  上海长风海洋世界: '普陀区',
  上海野生动物园车行区: '浦东新区',
  上海野生动物园步行区: '浦东新区',
  上海海昌海洋公园虎鲸馆: '浦东新区',
  上海海昌海洋公园北极熊馆: '浦东新区',
  上海迪士尼乐园城堡: '浦东新区',
  上海迪士尼乐园明日世界: '浦东新区',
  上海迪士尼乐园梦幻世界: '浦东新区',
  上海迪士尼乐园宝藏湾: '浦东新区',
  上海迪士尼乐园奇想花园: '浦东新区',
  上海迪士尼乐园探险岛: '浦东新区',
  上海迪士尼乐园皮克斯玩具总动员: '浦东新区',
  上海乐高乐园: '金山区',
  上海欢乐谷谷木游龙: '松江区',
  上海欢乐谷玛雅海滩水公园: '松江区',
  上海辰山植物园温室: '松江区',
  上海辰山植物园矿坑花园: '松江区',
  上海松江大学城: '松江区',
  上海松江方塔园: '松江区',
  上海松江醉白池: '松江区',
  上海泰晤士小镇: '松江区',
  上海欢乐谷魔幻城堡: '松江区',
  上海世纪公园: '浦东新区',
  上海陆家嘴中心绿地: '浦东新区',
  上海滨江森林公园: '浦东新区',
  上海南汇嘴观海公园: '浦东新区',
  上海滴水湖: '浦东新区',
  上海临港新城: '浦东新区',
  上海海洋大学: '浦东新区',
  上海上海大学: '宝山区',
  上海同济大学: '杨浦区',
  上海复旦大学: '杨浦区',
  上海交通大学: '徐汇区',
  上海华东师范大学: '闵行区',
  上海华东理工大学: '徐汇区',
  上海上海师范大学: '徐汇区',
  上海上海理工大学: '杨浦区',
  上海东华大学: '松江区',
  上海上海工程技术大学: '松江区',
  上海玻璃博物馆: '宝山区',
  淮海路: '宝山区',
  金茂大厦: '浦东新区',
  东方明珠: '金山区',
  外滩: '杨浦区',
  上海长宁区博物馆: '长宁区',
  上海徐汇区体育馆: '徐汇区',
  上海奉贤区青少年宫: '奉贤区',
  上海金山区体育馆: '金山区',
  长风公园: '长宁区',
  上海青浦区艺术中心: '青浦区',
  上海徐汇区博物馆: '徐汇区',
  上海航海博物馆: '宝山区',
  上海嘉定区美术馆: '嘉定区',
  徐家汇: '嘉定区',
  上海闵行区会展中心: '闵行区',
  上海金山区海洋馆: '金山区',
  上海电影博物馆: '闵行区',
  上海奉贤区体育馆: '奉贤区',
  上海金山区图书馆: '金山区',
  上海杨浦区植物园: '杨浦区',
  上海虹口区科技馆: '虹口区',
  上海普陀区体育场: '普陀区',
  上海宝山区青少年宫: '宝山区',
  上海嘉定区植物园: '嘉定区',
  上海公安博物馆: '黄浦区',
  人民广场: '虹口区',
  上海普陀区动物园: '普陀区',
  上海黄浦区创意园: '黄浦区',
  静安雕塑公园: '普陀区',
  上海嘉定区公园: '嘉定区',
  上海浦东新区美术馆: '浦东新区',
  上海黄浦区科技馆: '黄浦区',
  上海宝山区科技馆: '宝山区',
  环球金融中心: '奉贤区',
  上海奉贤区剧院: '奉贤区',
  陆家嘴: '浦东新区',
  上海徐汇区创意园: '徐汇区',
  上海宝山区植物园: '宝山区',
  上海静安区创意园: '静安区',
  上海金山区公园: '金山区',
  上海宝山区文化中心: '宝山区',
  上海静安区文化中心: '静安区',
  南京路: '闵行区',
  上海宝山区博物馆: '宝山区',
  上海虹口区会展中心: '虹口区',
  上海奉贤区文化馆: '奉贤区',
  上海普陀区剧院: '普陀区',
  上海浦东新区文化中心: '浦东新区',
  上海浦东新区公园: '浦东新区',
  上海宝山区海洋馆: '宝山区',
  上海普陀区博物馆: '普陀区',
  上海青浦区动物园: '青浦区',
  上海城市规划展示馆: '浦东新区',
  上海虹口区博物馆: '虹口区',
  上海闵行区博物馆: '闵行区',
  上海黄浦区博物馆: '黄浦区',
  上海浦东新区青少年宫: '浦东新区',
  上海杨浦区动物园: '杨浦区',
  上海普陀区青少年宫: '普陀区',
  上海青浦区科技馆: '青浦区',
  上海松江区剧院: '松江区',
  上海黄浦区海洋馆: '黄浦区',
  上海松江区博物馆: '松江区',
  上海静安区文化馆: '静安区',
  上海闵行区海洋馆: '闵行区',
  上海闵行区图书馆: '闵行区',
  上海闵行区科技馆: '闵行区',
  上海静安区科技馆: '静安区',
  上海静安区海洋馆: '静安区',
  上海普陀区会展中心: '普陀区',
  上海长宁区青少年宫: '长宁区',
  上海松江区植物园: '松江区',
  上海杨浦区剧院: '杨浦区',
  上海杨浦区公园: '杨浦区',
  上海长宁区艺术中心: '长宁区',
  上海博物馆东馆: '浦东新区',
  上海松江区体育馆: '松江区',
  上海浦东新区文化馆: '浦东新区',
  上海黄浦区图书馆: '黄浦区',
  上海中医药博物馆: '浦东新区',
  上海工艺美术博物馆: '徐汇区',
  上海奉贤区海洋馆: '奉贤区',
  上海徐汇区体育场: '徐汇区',
  上海黄浦区青少年宫: '黄浦区',
  上海普陀区科技馆: '普陀区',
  上海杨浦区创意园: '杨浦区',
  上海奉贤区动物园: '奉贤区',
  上海虹口区海洋馆: '虹口区',
  上海嘉定区动物园: '嘉定区',
  上海浦东新区海洋馆: '浦东新区',
  上海普陀区图书馆: '普陀区',
  上海普陀区艺术中心: '普陀区',
  上海动物园: '徐汇区',
  中国航海博物馆: '嘉定区',
  上海奉贤区艺术中心: '奉贤区',
  上海嘉定区会展中心: '嘉定区',
  上海奉贤区会展中心: '奉贤区',
  上海静安区植物园: '静安区',
  上海长宁区文化中心: '长宁区',
  上海黄浦区艺术中心: '黄浦区',
  上海浦东新区图书馆: '浦东新区',
  上海静安区艺术中心: '静安区',
  上海金山区创意园: '金山区',
  上海松江区青少年宫: '松江区',
  上海长宁区创意园: '长宁区',
  上海闵行区文化馆: '闵行区',
  上海杜莎夫人蜡像馆: '金山区',
  上海松江区文化馆: '松江区',
  上海松江区会展中心: '松江区',
  上海金山区动物园: '金山区',
  上海杨浦区文化中心: '杨浦区',
  上海杨浦区科技馆: '杨浦区',
  上海闵行区美术馆: '闵行区',
  上海黄浦区体育馆: '黄浦区',
  上海静安区体育场: '静安区',
  上海奉贤区美术馆: '奉贤区',
  上海徐汇区剧院: '徐汇区',
  上海金山区会展中心: '金山区',
  上海静安区青少年宫: '静安区',
  上海青浦区剧院: '青浦区',
  上海青浦区图书馆: '青浦区',
  上海徐汇区文化馆: '徐汇区',
  上海宝山区图书馆: '宝山区',
  上海浦东新区体育馆: '浦东新区',
  上海宝山区美术馆: '宝山区',
  上海长宁区体育场: '长宁区',
  上海静安区图书馆: '静安区',
  上海普陀区文化馆: '普陀区',
  上海虹口区艺术中心: '虹口区',
  上海金山区植物园: '金山区',
  上海杨浦区文化馆: '杨浦区',
  上海金山区文化馆: '金山区',
  上海金山区体育场: '金山区',
  上海青浦区公园: '青浦区',
  上海杨浦区图书馆: '杨浦区',
  上海嘉定区文化馆: '嘉定区',
  上海徐汇区海洋馆: '徐汇区',
  上海长宁区剧院: '长宁区',
  上海宝山区动物园: '宝山区',
  上海奉贤区体育场: '奉贤区',
  上海青浦区植物园: '青浦区',
  上海虹口区体育馆: '虹口区',
  上海虹口区公园: '虹口区',
  上海宝山区文化馆: '宝山区',
  上海青浦区体育馆: '青浦区',
  上海环球金融中心: '浦东新区',
  上海长宁区美术馆: '长宁区',
  上海金山区剧院: '金山区',
  上海杨浦区美术馆: '杨浦区',
  上海嘉定区创意园: '嘉定区',
  上海虹口区青少年宫: '虹口区',
  上海宝山区公园: '宝山区',
  上海杨浦区青少年宫: '杨浦区',
  上海浦东新区博物馆: '浦东新区',
  上海徐汇区文化中心: '徐汇区',
  上海长宁区会展中心: '长宁区',
  上海奉贤区植物园: '奉贤区',
  上海静安区博物馆: '静安区',
  上海黄浦区会展中心: '黄浦区',
  上海博物馆人民广场馆: '黄浦区',
  上海地震科普馆: '松江区',
  上海惊魂密境: '黄浦区',
  上海徐汇区艺术中心: '徐汇区',
  上海普陀区美术馆: '普陀区',
  上海黄浦区剧院: '黄浦区',
  上海松江区体育场: '松江区',
  上海杨浦区体育场: '杨浦区',
  上海徐汇区美术馆: '徐汇区',
  上海嘉定区图书馆: '嘉定区',
  上海松江区动物园: '松江区',
  上海虹口区图书馆: '虹口区',
  上海松江区美术馆: '松江区',
  上海嘉定区艺术中心: '嘉定区',
  上海长宁区公园: '长宁区',
  上海嘉定区剧院: '嘉定区',
  上海黄浦区动物园: '黄浦区',
  上海奉贤区博物馆: '奉贤区',
  上海徐汇区会展中心: '徐汇区',
  上海奉贤区文化中心: '奉贤区',
  上海黄浦区体育场: '黄浦区',
  上海静安区会展中心: '静安区',
  上海闵行区创意园: '闵行区',
  上海黄浦区公园: '黄浦区',
  上海宝山区体育场: '宝山区',
  上海闵行区公园: '闵行区',
  上海青浦区海洋馆: '青浦区',
  上海松江区文化中心: '松江区',
  上海闵行区动物园: '闵行区',
  上海普陀区文化中心: '普陀区',
  上海静安区体育馆: '静安区',
  上海静安区美术馆: '静安区',
  上海闵行区植物园: '闵行区',
  上海长宁区体育馆: '长宁区',
  上海虹口区植物园: '虹口区',
  上海长宁区动物园: '长宁区',
  上海普陀区公园: '普陀区',
  上海浦东新区体育场: '浦东新区',
  上海普陀区创意园: '普陀区',
  上海青浦区体育场: '青浦区',
  上海嘉定区科技馆: '嘉定区',
  上海青浦区创意园: '青浦区',
  上海松江区公园: '松江区',
  上海嘉定区体育馆: '嘉定区',
  上海嘉定区海洋馆: '嘉定区',
  上海金山区艺术中心: '金山区',
  上海青浦区会展中心: '青浦区',
  上海杨浦区博物馆: '杨浦区',
  上海徐汇区植物园: '徐汇区',
  上海闵行区体育馆: '闵行区',
  上海浦东新区剧院: '浦东新区',
  上海闵行区艺术中心: '闵行区',
  上海长宁区图书馆: '长宁区',
  上海长宁区科技馆: '长宁区',
  上海徐汇区青少年宫: '徐汇区',
  上海青浦区文化中心: '青浦区',
  上海虹口区文化馆: '虹口区',
  上海宝山区剧院: '宝山区',
  上海松江区海洋馆: '松江区',
  上海徐汇区科技馆: '徐汇区',
  上海浦东新区植物园: '浦东新区',
  上海金山区科技馆: '金山区',
  上海虹口区美术馆: '虹口区',
  上海隧道科技馆: '黄浦区',
  上海黄浦区文化中心: '黄浦区',
  上海浦东新区动物园: '浦东新区',
  上海虹口区创意园: '虹口区',
  '宝安区图书馆（总馆）': '宝安区',
  宝安区城市规划展览馆: '宝安区',
  '宝安1990文化馆（区文化馆总馆）': '宝安区',
  宝安博物馆: '宝安区',
  宝安美术馆: '宝安区',
  '宝安区青少年宫（滨海）': '宝安区',
  '湾区书城（深圳书城湾区城）': '宝安区',
  茅洲河展示馆: '宝安区',
  西湾红树林科普馆: '宝安区',
  福海安全生产警示教育中心: '宝安区',
  福永街道安全警示教育基地: '宝安区',
  宝安图书馆西乡街道分馆: '宝安区',
  新安街道分馆: '宝安区',
  新安中洲分馆: '宝安区',
  翻身社区阅读中心: '宝安区',
  宝民社区阅读中心: '宝安区',
  大仟里未来书屋: '宝安区',
  '宝读书房·旭书店': '宝安区',
  沙井街道图书馆分馆: '宝安区',
  松岗街道图书馆分馆: '宝安区',
  石岩街道图书馆分馆: '宝安区',
  福永街道图书馆分馆: '宝安区',
  燕罗街道图书馆分馆: '宝安区',
  航城街道图书馆分馆: '宝安区',
  新桥街道图书馆分馆: '宝安区',
  '滨海文化公园（欢乐港湾）': '宝安区',
  '宝安公园（醒狮乐园）': '宝安区',
  新安公园: '宝安区',
  西湾公园: '宝安区',
  蚝乡湖公园: '宝安区',
  '立新湖公园（立新湖儿童乐园）': '宝安区',
  凤凰山人才林公园: '宝安区',
  五指耙体育主题公园: '宝安区',
  铁仔山公园: '宝安区',
  福海河公园: '宝安区',
  钓鱼嘴原木亲子乐园: '宝安区',
  沙井市民广场: '宝安区',
  新桥市民广场: '宝安区',
  燕罗湿地公园: '宝安区',
  航城公园: '宝安区',
  石岩湿地公园: '宝安区',
  松岗公园: '宝安区',
  桥头公园: '宝安区',
  清平古墟影视小镇: '宝安区',
  王大中丞祠: '宝安区',
  西乡北帝古庙: '宝安区',
  沙井蚝文化博物馆: '宝安区',
  福永凤凰古村: '宝安区',
  '松岗琥珀博物馆（公益展厅）': '宝安区',
  燕罗红色文化纪念馆: '宝安区',
  上合孝德园: '宝安区',
  湖北省科学技术馆: '洪山区',
  盘龙城遗址博物院: '黄陂区',
  武汉科技馆: '江岸区',
  中科院武汉植物园: '武昌区',
  后官湖湿地公园: '蔡甸区',
  武汉海昌极地海洋公园: '东西湖区',
  汉秀剧场: '武昌区',
  武汉市少年儿童图书馆: '江岸区',
  木兰清凉寨: '黄陂区',
  黎黄陂路: '江岸区',
  武汉黄陂区动物园: '黄陂区',
  武汉博物馆: '江汉区',
  武汉欢乐谷: '武昌区',
  湖北美术馆: '武昌区',
  湖北省图书馆: '武昌区',
  武汉图书馆: '江汉区',
  武汉体育中心: '蔡甸区',
  武汉全民健身中心: '江岸区',
  木兰草原: '黄陂区',
  武汉东西湖区美术馆: '东西湖区',
  武汉江夏区博物馆: '江夏区',
  湖北省博物馆: '武昌区',
  东湖风景区: '武昌区',
  武汉美术馆: '江岸区',
  黄鹤楼公园: '武昌区',
  中山舰博物馆: '江夏区',
  辛亥革命武昌起义纪念馆: '武昌区',
  武汉体育馆: '硚口区',
  武汉黄陂区体育馆: '黄陂区',
  武汉汉阳区艺术中心: '汉阳区',
  武汉洪山区文化馆: '洪山区',
  武汉动物园: '汉阳区',
  武汉玛雅海滩水公园: '武昌区',
  辛亥革命博物馆: '武昌区',
  木兰天池: '黄陂区',
  汉口江滩公园: '江岸区',
  武汉江夏区体育馆: '江夏区',
  江汉关博物馆: '江岸区',
  粮道街: '武昌区',
  武汉江岸区海洋馆: '江岸区',
  武汉洪山区体育场: '洪山区',
  武汉自然博物馆: '东西湖区',
  解放公园: '江岸区',
  武汉硚口区文化馆: '硚口区',
  武汉江夏区图书馆: '江夏区',
  武汉武昌区剧院: '武昌区',
  武汉江夏区体育场: '江夏区',
  武汉黄陂区创意园: '黄陂区',
  武汉新洲区植物园: '新洲区',
  武汉汉阳区创意园: '汉阳区',
  武汉新洲区剧院: '新洲区',
  武汉江汉区科技馆: '江汉区',
  武汉新洲区体育场: '新洲区',
  武汉硚口区艺术中心: '硚口区',
  武汉黄陂区科技馆: '黄陂区',
  武汉新洲区文化馆: '新洲区',
  武汉杂技厅: '江汉区',
  武昌江滩公园: '武昌区',
  武汉江夏区剧院: '江夏区',
  武汉东西湖区文化馆: '东西湖区',
  武汉武昌区博物馆: '武昌区',
  武汉蔡甸区创意园: '蔡甸区',
  武汉蔡甸区植物园: '蔡甸区',
  武汉东西湖区植物园: '东西湖区',
  武汉江岸区体育馆: '江岸区',
  武汉东西湖区会展中心: '东西湖区',
  武汉江岸区博物馆: '江岸区',
  武汉蔡甸区青少年宫: '蔡甸区',
  武汉蔡甸区公园: '蔡甸区',
  武汉江夏区科技馆: '江夏区',
  武汉江汉区动物园: '江汉区',
  武汉江汉区图书馆: '江汉区',
  武汉江汉区体育场: '江汉区',
  武汉东西湖区文化中心: '东西湖区',
  武汉武昌区美术馆: '武昌区',
  武汉武昌区体育场: '武昌区',
  武汉东西湖区艺术中心: '东西湖区',
  武汉汉阳区公园: '汉阳区',
  武汉江夏区公园: '江夏区',
  锦里沟: '黄陂区',
  武汉青山区剧院: '青山区',
  武汉硚口区美术馆: '硚口区',
  武汉江岸区体育场: '江岸区',
  楚河汉街: '武昌区',
  武汉青山区美术馆: '青山区',
  武汉硚口区植物园: '硚口区',
  武汉江夏区海洋馆: '江夏区',
  武汉青山区创意园: '青山区',
  武汉洪山区创意园: '洪山区',
  武汉江岸区图书馆: '江岸区',
  武汉东西湖区体育馆: '东西湖区',
  武汉武昌区体育馆: '武昌区',
  武汉江汉区海洋馆: '江汉区',
  武汉江岸区艺术中心: '江岸区',
  武汉江汉区博物馆: '江汉区',
  武汉青山区科技馆: '青山区',
  户部巷: '武昌区',
  武汉新洲区文化中心: '新洲区',
  武汉青山区体育场: '青山区',
  木兰山: '黄陂区',
  武汉新洲区美术馆: '新洲区',
  武汉江夏区创意园: '江夏区',
  武汉新洲区科技馆: '新洲区',
  武汉青山区动物园: '青山区',
  武汉武昌区图书馆: '武昌区',
  武汉蔡甸区图书馆: '蔡甸区',
  武汉蔡甸区会展中心: '蔡甸区',
  武汉东西湖区科技馆: '东西湖区',
  武汉江夏区动物园: '江夏区',
  武汉黄陂区博物馆: '黄陂区',
  武汉东西湖区剧院: '东西湖区',
  武汉江夏区植物园: '江夏区',
  武汉黄陂区美术馆: '黄陂区',
  武汉汉阳区剧院: '汉阳区',
  武汉青山区体育馆: '青山区',
  武汉汉阳区文化中心: '汉阳区',
  武汉长江大桥: '武昌区',
  武汉武昌区海洋馆: '武昌区',
  武汉东西湖区体育场: '东西湖区',
  武汉汉阳区海洋馆: '汉阳区',
  武汉青山区博物馆: '青山区',
  武汉新洲区图书馆: '新洲区',
  武汉硚口区科技馆: '硚口区',
  武汉江岸区剧院: '江岸区',
  武汉汉阳区会展中心: '汉阳区',
  武汉青山区艺术中心: '青山区',
  武汉洪山区艺术中心: '洪山区',
  武汉武昌区艺术中心: '武昌区',
  硚口江滩公园: '硚口区',
  武汉青山区图书馆: '青山区',
  武汉硚口区会展中心: '硚口区',
  武汉江夏区美术馆: '江夏区',
  武汉江岸区会展中心: '江岸区',
  武汉蔡甸区文化馆: '蔡甸区',
  武汉黄陂区会展中心: '黄陂区',
  武汉洪山区公园: '洪山区',
  武汉黄陂区体育场: '黄陂区',
  武汉江夏区会展中心: '江夏区',
  武汉洪山区文化中心: '洪山区',
  武汉硚口区体育场: '硚口区',
  武汉汉阳区美术馆: '汉阳区',
  武汉江夏区青少年宫: '江夏区',
  汉阳江滩公园: '汉阳区',
  武汉洪山区科技馆: '洪山区',
  武汉黄陂区公园: '黄陂区',
  武汉新洲区海洋馆: '新洲区',
  武汉洪山区体育馆: '洪山区',
  武汉青山区文化馆: '青山区',
  武汉黄陂区文化中心: '黄陂区',
  武汉汉阳区文化馆: '汉阳区',
  武汉青山区文化中心: '青山区',
  武汉蔡甸区海洋馆: '蔡甸区',
  武汉江夏区文化馆: '江夏区',
  武汉黄陂区文化馆: '黄陂区',
  武汉洪山区海洋馆: '洪山区',
  武汉东西湖区海洋馆: '东西湖区',
  武汉黄陂区海洋馆: '黄陂区',
  武汉蔡甸区艺术中心: '蔡甸区',
  武汉港码头: '江岸区',
  鹦鹉洲长江大桥: '汉阳区',
  万松园: '江汉区',
  武汉汉阳区图书馆: '汉阳区',
  武汉武昌区植物园: '武昌区',
  武汉洪山区青少年宫: '洪山区',
  武汉东西湖区青少年宫: '东西湖区',
  武汉武昌区文化中心: '武昌区',
  武汉洪山区博物馆: '洪山区',
  武汉江岸区公园: '江岸区',
  武汉武昌区文化馆: '武昌区',
  武汉新洲区博物馆: '新洲区',
  武汉蔡甸区体育场: '蔡甸区',
  武汉硚口区动物园: '硚口区',
  武汉洪山区图书馆: '洪山区',
  武汉青山区青少年宫: '青山区',
  武汉武昌区青少年宫: '武昌区',
  武汉新洲区艺术中心: '新洲区',
  武汉黄陂区图书馆: '黄陂区',
  武汉蔡甸区体育馆: '蔡甸区',
  武汉汉阳区动物园: '汉阳区',
  武汉江汉区美术馆: '江汉区',
  武汉东西湖区公园: '东西湖区',
  武汉蔡甸区科技馆: '蔡甸区',
  武汉新洲区青少年宫: '新洲区',
  武汉江岸区美术馆: '江岸区',
  武汉硚口区创意园: '硚口区',
  武汉江岸区植物园: '江岸区',
  武汉青山区植物园: '青山区',
  武汉汉阳区科技馆: '汉阳区',
  武汉东西湖区动物园: '东西湖区',
  武汉江汉区文化馆: '江汉区',
  武汉汉阳区体育馆: '汉阳区',
  武汉硚口区公园: '硚口区',
  武汉东西湖区博物馆: '东西湖区',
  武汉武昌区公园: '武昌区',
  武汉江岸区文化中心: '江岸区',
  武汉新洲区体育馆: '新洲区',
  武汉蔡甸区剧院: '蔡甸区',
  武汉江汉区文化中心: '江汉区',
  武汉硚口区文化中心: '硚口区',
  武汉青山区公园: '青山区',
  武汉洪山区植物园: '洪山区',
  武汉江岸区动物园: '江岸区',
  武汉汉阳区植物园: '汉阳区',
  武汉蔡甸区动物园: '蔡甸区',
  武汉江汉区剧院: '江汉区',
  江汉路步行街: '江汉区',
  武汉硚口区剧院: '硚口区',
  武汉江岸区创意园: '江岸区',
  武汉洪山区剧院: '洪山区',
  武汉硚口区图书馆: '硚口区',
  武汉武昌区动物园: '武昌区',
  武汉黄陂区剧院: '黄陂区',
  武汉江汉区创意园: '江汉区',
  武汉汉阳区青少年宫: '汉阳区',
  武汉武昌区创意园: '武昌区',
  武汉汉阳区博物馆: '汉阳区',
  武汉蔡甸区博物馆: '蔡甸区',
  武汉江岸区科技馆: '江岸区',
  武汉江汉区艺术中心: '江汉区',
  武汉江岸区文化馆: '江岸区',
  武汉武昌区科技馆: '武昌区',
  武汉新洲区动物园: '新洲区',
  武汉江汉区体育馆: '江汉区',
  武汉江汉区青少年宫: '江汉区',
  武汉黄陂区艺术中心: '黄陂区',
  武汉硚口区海洋馆: '硚口区',
  武汉硚口区青少年宫: '硚口区',
  武汉黄陂区植物园: '黄陂区',
  武汉硚口区体育馆: '硚口区',
  武汉武昌区会展中心: '武昌区',
  武汉东西湖区创意园: '东西湖区',
  武汉洪山区会展中心: '洪山区',
  武汉洪山区美术馆: '洪山区',
  武汉东西湖区图书馆: '东西湖区',
  武汉新洲区公园: '新洲区',
  武汉汉阳区体育场: '汉阳区',
  武汉江岸区青少年宫: '江岸区',
  武汉东湖海洋世界: '武昌区',
  武汉青山区会展中心: '青山区',
  武汉江汉区会展中心: '江汉区',
  武汉江汉区公园: '江汉区',
  武汉江夏区文化中心: '江夏区',
  武汉蔡甸区美术馆: '蔡甸区',
  武汉洪山区动物园: '洪山区',
  武汉青山区海洋馆: '青山区',
  武汉硚口区博物馆: '硚口区',
  武汉新洲区会展中心: '新洲区',
  武汉江汉区植物园: '江汉区',
  西安碑林博物馆: '碑林区',
  大唐西市博物馆: '莲湖区',
  陕西科技馆: '新城区',
  兴庆宫公园: '碑林区',
  华夏文旅海洋公园: '灞桥区',
  大唐不夜城: '雁塔区',
  曲江书城: '雁塔区',
  西安奥体中心: '未央区',
  黑河国家森林公园: '周至县',
  西安城墙: '碑林区',
  西安高陵区艺术中心: '高陵区',
  昆明池七夕公园: '长安区',
  乐华城: '未央区',
  永兴坊: '新城区',
  半坡遗址博物馆: '灞桥区',
  雁鸣湖: '灞桥区',
  西安灞桥区美术馆: '灞桥区',
  汉阳陵博物院: '未央区',
  大雁塔景区: '雁塔区',
  陕西省图书馆: '碑林区',
  环城公园: '碑林区',
  楼观台森林公园: '周至县',
  大唐芙蓉园: '雁塔区',
  西安新城区博物馆: '新城区',
  易俗社文化街区: '新城区',
  陕西历史博物馆: '雁塔区',
  汉城湖公园: '未央区',
  华清宫: '临潼区',
  西安莲湖区动物园: '莲湖区',
  西安碑林区图书馆: '碑林区',
  曲江池遗址公园: '雁塔区',
  书院门: '碑林区',
  西安图书馆: '未央区',
  王顺山国家森林公园: '蓝田县',
  西安未央区植物园: '未央区',
  西安高陵区创意园: '高陵区',
  西安博物院: '碑林区',
  西安新城区动物园: '新城区',
  西安雁塔区博物馆: '雁塔区',
  大明宫遗址博物馆: '未央区',
  浐灞国家湿地公园: '未央区',
  太平国家森林公园: '鄠邑区',
  翠华山国家地质公园: '长安区',
  西安临潼区美术馆: '临潼区',
  西安雁塔区图书馆: '雁塔区',
  朱雀国家森林公园: '鄠邑区',
  西安莲湖区科技馆: '莲湖区',
  西安新城区青少年宫: '新城区',
  西安鄠邑区科技馆: '鄠邑区',
  西安植物园: '雁塔区',
  西安市钟鼓楼博物馆: '莲湖区',
  西安莲湖区图书馆: '莲湖区',
  曲江海洋极地公园: '雁塔区',
  西安未央区图书馆: '未央区',
  西安灞桥区会展中心: '灞桥区',
  西安新城区体育馆: '新城区',
  西安碑林区公园: '碑林区',
  西安临潼区公园: '临潼区',
  西安未央区博物馆: '未央区',
  西安阎良区美术馆: '阎良区',
  秦始皇帝陵博物院: '临潼区',
  西安未央区美术馆: '未央区',
  西安未央区公园: '未央区',
  西安阎良区植物园: '阎良区',
  西安长安区海洋馆: '长安区',
  西安莲湖区博物馆: '莲湖区',
  西安灞桥区艺术中心: '灞桥区',
  西安高陵区会展中心: '高陵区',
  西安临潼区文化馆: '临潼区',
  西安未央区创意园: '未央区',
  西安碑林区科技馆: '碑林区',
  西安新城区剧院: '新城区',
  西安鄠邑区体育馆: '鄠邑区',
  西安灞桥区公园: '灞桥区',
  西安阎良区剧院: '阎良区',
  西安高陵区博物馆: '高陵区',
  西安高陵区体育场: '高陵区',
  西安莲湖区艺术中心: '莲湖区',
  西安雁塔区剧院: '雁塔区',
  西安欢乐谷: '长安区',
  西安阎良区体育馆: '阎良区',
  西安未央区动物园: '未央区',
  西安临潼区科技馆: '临潼区',
  西安长安区美术馆: '长安区',
  西安阎良区公园: '阎良区',
  西安长安区植物园: '长安区',
  西安高陵区科技馆: '高陵区',
  西安鄠邑区文化中心: '鄠邑区',
  陕西自然博物馆: '雁塔区',
  西安长安区公园: '长安区',
  西安未央区剧院: '未央区',
  西安高陵区海洋馆: '高陵区',
  西安新城区创意园: '新城区',
  西安阎良区动物园: '阎良区',
  西安灞桥区博物馆: '灞桥区',
  西安阎良区科技馆: '阎良区',
  西安鄠邑区青少年宫: '鄠邑区',
  西安雁塔区体育馆: '雁塔区',
  西安莲湖区文化馆: '莲湖区',
  西安阎良区海洋馆: '阎良区',
  西安未央区青少年宫: '未央区',
  西安灞桥区图书馆: '灞桥区',
  西安灞桥区植物园: '灞桥区',
  长安十二时辰主题街区: '雁塔区',
  西安临潼区艺术中心: '临潼区',
  西安高陵区剧院: '高陵区',
  西安碑林区会展中心: '碑林区',
  西安碑林区体育场: '碑林区',
  西安新城区科技馆: '新城区',
  西安临潼区图书馆: '临潼区',
  西安长安区艺术中心: '长安区',
  西安碑林区博物馆: '碑林区',
  西安灞桥区动物园: '灞桥区',
  西安新城区植物园: '新城区',
  西安未央区文化馆: '未央区',
  西安长安区体育场: '长安区',
  西安长安区体育馆: '长安区',
  西安雁塔区公园: '雁塔区',
  西安灞桥区体育场: '灞桥区',
  西安阎良区会展中心: '阎良区',
  西安长安区会展中心: '长安区',
  西安长安区青少年宫: '长安区',
  西安阎良区文化馆: '阎良区',
  西安阎良区创意园: '阎良区',
  西安雁塔区科技馆: '雁塔区',
  西安新城区艺术中心: '新城区',
  西安长安区动物园: '长安区',
  西安未央区体育馆: '未央区',
  西安新城区体育场: '新城区',
  西安莲湖区植物园: '莲湖区',
  西安碑林区美术馆: '碑林区',
  西安高陵区体育馆: '高陵区',
  西安高陵区文化馆: '高陵区',
  西安雁塔区动物园: '雁塔区',
  西安未央区科技馆: '未央区',
  西安临潼区植物园: '临潼区',
  西安高陵区公园: '高陵区',
  西安高陵区动物园: '高陵区',
  西安长安区文化中心: '长安区',
  西安长安区科技馆: '长安区',
  西安莲湖区体育场: '莲湖区',
  西安临潼区创意园: '临潼区',
  西安高陵区植物园: '高陵区',
  西安碑林区植物园: '碑林区',
  西安鄠邑区图书馆: '鄠邑区',
  西安灞桥区创意园: '灞桥区',
  西安雁塔区体育场: '雁塔区',
  西安莲湖区美术馆: '莲湖区',
  回民街: '莲湖区',
  西安雁塔区会展中心: '雁塔区',
  西安阎良区艺术中心: '阎良区',
  西安莲湖区文化中心: '莲湖区',
  西安临潼区会展中心: '临潼区',
  西安长安区博物馆: '长安区',
  西安未央区体育场: '未央区',
  西安碑林区文化中心: '碑林区',
  西安新城区公园: '新城区',
  西安临潼区青少年宫: '临潼区',
  西安碑林区海洋馆: '碑林区',
  西安雁塔区文化馆: '雁塔区',
  西安灞桥区体育馆: '灞桥区',
  西安碑林区青少年宫: '碑林区',
  西安鄠邑区博物馆: '鄠邑区',
  西安鄠邑区剧院: '鄠邑区',
  西安未央区海洋馆: '未央区',
  西安鄠邑区会展中心: '鄠邑区',
  西安雁塔区艺术中心: '雁塔区',
  西安雁塔区文化中心: '雁塔区',
  西安鄠邑区美术馆: '鄠邑区',
  西安临潼区体育馆: '临潼区',
  西安阎良区图书馆: '阎良区',
  西安灞桥区文化中心: '灞桥区',
  西安长安区创意园: '长安区',
  西安莲湖区体育馆: '莲湖区',
  西安碑林区艺术中心: '碑林区',
  西安新城区海洋馆: '新城区',
  西安碑林区体育馆: '碑林区',
  西安雁塔区创意园: '雁塔区',
  西安高陵区青少年宫: '高陵区',
  西安临潼区动物园: '临潼区',
  西安未央区艺术中心: '未央区',
  西安灞桥区文化馆: '灞桥区',
  西安碑林区文化馆: '碑林区',
  西安临潼区剧院: '临潼区',
  西安鄠邑区公园: '鄠邑区',
  西安莲湖区海洋馆: '莲湖区',
  西安长安区文化馆: '长安区',
  西安鄠邑区植物园: '鄠邑区',
  西安莲湖区剧院: '莲湖区',
  西安莲湖区青少年宫: '莲湖区',
  西安灞桥区海洋馆: '灞桥区',
  西安鄠邑区动物园: '鄠邑区',
  西安新城区美术馆: '新城区',
  西安新城区文化中心: '新城区',
  西安长安区图书馆: '长安区',
  西安雁塔区美术馆: '雁塔区',
  西安阎良区青少年宫: '阎良区',
  西安灞桥区科技馆: '灞桥区',
  西安临潼区文化中心: '临潼区',
  西安阎良区体育场: '阎良区',
  西安新城区文化馆: '新城区',
  西安鄠邑区艺术中心: '鄠邑区',
  西安临潼区海洋馆: '临潼区',
  西安临潼区博物馆: '临潼区',
  西安未央区文化中心: '未央区',
  西安碑林区动物园: '碑林区',
  西安雁塔区海洋馆: '雁塔区',
  西安高陵区美术馆: '高陵区',
  西安高陵区文化中心: '高陵区',
  西安鄠邑区体育场: '鄠邑区',
  西安雁塔区青少年宫: '雁塔区',
  西安灞桥区剧院: '灞桥区',
  西安莲湖区创意园: '莲湖区',
  西安阎良区博物馆: '阎良区',
  西安新城区会展中心: '新城区',
  西安高陵区图书馆: '高陵区',
  西安灞桥区青少年宫: '灞桥区',
  西安新城区图书馆: '新城区',
  西安雁塔区植物园: '雁塔区',
  西安碑林区剧院: '碑林区',
  西安阎良区文化中心: '阎良区',
  西安鄠邑区文化馆: '鄠邑区',
  西安莲湖区会展中心: '莲湖区',
  西安临潼区体育场: '临潼区',
  西安碑林区创意园: '碑林区',
  西安鄠邑区创意园: '鄠邑区',
  西安未央区会展中心: '未央区',
  西安鄠邑区海洋馆: '鄠邑区',
  西安莲湖区公园: '莲湖区',
  西安长安区剧院: '长安区',
  珠海博物馆: '香洲区',
  珠海市图书馆: '香洲区',
  珠海市文化馆: '香洲区',
  古元美术馆: '香洲区',
  珠海大剧院: '香洲区',
  香山文化艺术中心: '香洲区',
  珠海规划展览馆: '香洲区',
  国家方志馆粤港澳大湾区分馆: '香洲区',
  珠海市青少年妇女儿童活动中心: '香洲区',
  珠海市工人文化宫: '香洲区',
  圆明新园: '香洲区',
  梅溪牌坊: '香洲区',
  珠海国际会展中心: '香洲区',
  华发商都: '香洲区',
  珠海海滨公园: '香洲区',
  金湾区图书馆: '金湾区',
  金湾区文化馆: '金湾区',
  金湾区博物馆: '金湾区',
  金湾艺术中心: '金湾区',
  汤臣倍健透明工厂: '金湾区',
  珠海航展馆: '金湾区',
  珠海海泉湾度假区: '金湾区',
  金湾体育中心: '金湾区',
  三灶镇文化中心: '金湾区',
  金海岸文化艺术中心: '金湾区',
  斗门区图书馆: '斗门区',
  斗门区博物馆: '斗门区',
  斗门区文化馆: '斗门区',
  斗门旧街: '斗门区',
  金台寺: '斗门区',
  御温泉: '斗门区',
  斗门体育中心: '斗门区',
  井岸镇文化中心: '斗门区',
  黄杨山: '斗门区',
  斗门非遗展示馆: '斗门区',
  横琴文化艺术中心: '横琴新区',
  珠海长隆海洋王国: '横琴新区',
  珠海长隆飞船乐园: '横琴新区',
  珠海长隆横琴剧院: '横琴新区',
  横琴国际网球中心: '横琴新区',
  星乐度露营小镇: '横琴新区',
  横琴湿地公园: '横琴新区',
  横琴花海长廊: '横琴新区',
  横琴口岸: '横琴新区',
  横琴金融岛: '横琴新区',
  珠海渔女景区: '香洲区',
  野狸岛音乐广场: '香洲区',
  珠海市体育中心: '香洲区',
  香洲区文化馆: '香洲区',
  '龙岗国际艺术中心·D+数字艺术馆': '龙岗区',
  '龙岗国际艺术中心·国际演艺中心': '龙岗区',
  深圳市龙岗区怡利翡翠博物馆: '龙岗区',
  深圳市龙岗区龙岭邮票博物馆: '龙岗区',
  深圳市龙岗区万国珠宝汇矿物博物馆: '龙岗区',
  龙岗区图书馆少儿馆: '龙岗区',
  深圳市百师园非物质文化遗产博物馆: '龙岗区',
  深圳市丁全匠作博物馆: '龙岗区',
  深圳市梵亚艺术博物馆: '龙岗区',
  '深圳市龙岗区东江潮红色文化博物馆（新生主馆）': '龙岗区',
  深圳市隐秀高尔夫博物馆: '龙岗区',
  '深圳·红立方': '龙岗区',
  茅洲河体育艺术中心: '光明区',
  深圳市坪山区文化馆: '坪山区',
  深圳市工业展览馆: '福田区',
  南山区天后博物馆: '南山区',
  风华大剧院: '南山区',
  '福田文体中心·戏剧主题馆': '福田区',
  '福田文体中心·舞蹈主题馆': '福田区',
  '福田文体中心·音乐主题馆': '福田区',
  '福田文体中心·梦工场': '福田区',
  '福田文体中心·非遗主题馆': '福田区',
  大鹏新区博物馆: '大鹏新区',
  金龟自然书房分馆: '坪山区',
  坪山儿童公园分馆: '坪山区',
  '坪山图书馆·客家特藏馆': '坪山区',
  深圳红木家具博物馆: '龙华区',
  深圳望野博物馆: '龙华区',
  深圳市龙华区美联红木艺术博物馆: '龙华区',
  深圳市艺之卉百年时尚博物馆: '龙华区',
  中国文化名人大营救纪念馆: '龙华区',
  龙岗文化中心音乐厅: '龙岗区',
  龙岗文化中心大剧院: '龙岗区',
  深圳市龙岗区文化馆: '龙岗区',
  世纪琥珀博物馆: '宝安区',
  华润大厦艺术中心美术馆: '南山区',
  南头古城博物馆: '南山区',
  龙华图书馆: '龙华区',
  蛇口海上世界文化艺术中心: '南山区',
  深圳南山文体中心剧院聚橙剧院: '南山区',
  依波钟表文化博物馆: '光明区',
  惜物博物馆: '光明区',
  光明区少年儿童图书馆: '光明区',
  深汕西文体中心: '深汕特别合作区',
  '深圳（宝安）劳务工博物馆': '宝安区',
  至美术馆: '宝安区',
  深圳市坪山区美术馆: '坪山区',
  深圳市坪山区图书馆: '坪山区',
  深圳市坪山区东江纵队纪念馆: '坪山区',
  深圳市福田区图书馆: '福田区',
  光明国际马术中心: '光明区',
  罗湖体育馆: '罗湖区',
  罗湖体育休闲公园: '罗湖区',
  罗湖网球中心: '罗湖区',
  横岗文体中心: '龙岗区',
  宝龙文体中心: '龙岗区',
  深圳布吉文体中心: '龙岗区',
  深圳市青少年足球训练基地: '光明区',
  光明区红花山体育中心: '光明区',
  '北京大学附属中学深圳学校(集团)黄埔学校(小学部)': '福田区',
  民治体育公园: '龙华区',
  葵涌中学体育场: '大鹏新区',
  南澳中学体育场: '大鹏新区',
  南澳中心小学体育场: '大鹏新区',
  人大附中深圳学校高中部体育场: '大鹏新区',
  葵涌第二小学体育场: '大鹏新区',
  溪涌小学体育场: '大鹏新区',
  葵涌中心小学体育场: '大鹏新区',
  大鹏第二小学体育场: '大鹏新区',
  深圳市龙岗区体育中心: '龙岗区',
  沙头角体育馆: '盐田区',
  盐田区游泳馆: '盐田区',
  盐田区体育发展服务中心网球场: '盐田区',
  九龙山体育公园: '龙华区',
  冰纷万象滑雪场: '南山区',
  锡才体育公园: '南山区',
  大鹏新区葵涌中心小学: '大鹏新区',
  景鹏小学: '福田区',
  南海足球公园: '南山区',
  荔香公园网球场: '南山区',
  桃源群众篮球网球体育公园: '南山区',
  大沙河公园体育中心: '南山区',
  蛇口体育中心: '南山区',
  深圳湾体育训练基地: '南山区',
  深圳中山公园棒球场: '南山区',
  简上体育综合体: '龙华区',
  '综合训练馆（室内网球馆）': '宝安区',
  宝安游泳场馆: '宝安区',
  宝安体育场: '宝安区',
  宝安体育馆: '宝安区',
  深圳市坪山区坪山体育中心体育馆: '坪山区',
  香蜜体育中心: '福田区',
  黄木岗网球中心: '福田区',
  莲花体育中心: '福田区',
  福田体育公园: '福田区',
  福田区景田网球中心: '福田区',
  福田海滨生态体育公园: '福田区',
  北京老爷车博物馆: '怀柔区',
  北京李大钊故居: '西城区',
  北京励志堂科举匾额博物馆: '朝阳区',
  历代帝王庙: '西城区',
  中国法院博物馆: '东城区',
  北京韩美林艺术馆: '通州区',
  延庆博物馆: '延庆区',
  北京西瓜博物馆: '大兴区',
  中国人民大学博物馆: '海淀区',
  北京空竹博物馆: '西城区',
  北京市怀柔区博物馆: '怀柔区',
  北京怀柔喇叭沟门满族民俗博物馆: '怀柔区',
  民航博物馆: '朝阳区',
  中国传媒大学传媒博物馆: '朝阳区',
  西藏文化博物馆: '朝阳区',
  和苑博物馆: '朝阳区',
  中国海关博物馆: '东城区',
  北京御仙都皇家菜博物馆: '海淀区',
  北京市平谷区博物馆: '平谷区',
  北京英杰硬石艺术博物馆: '朝阳区',
  北京税务博物馆: '朝阳区',
  中国华侨历史博物馆: '东城区',
  中国人民大学家书博物馆: '海淀区',
  北京文旺阁木作博物馆: '通州区',
  延庆区地质博物馆: '延庆区',
  北京市姜杰钢琴手风琴博物馆: '海淀区',
  首都粮食博物馆: '东城区',
  香山革命纪念馆: '海淀区',
  北京荣唐连环画博物馆: '朝阳区',
  北京二锅头酒博物馆: '怀柔区，东城区',
  北京市大兴区月季博物馆: '大兴区',
  北京皇城御窑金砖博物馆: '通州区',
  北京燕京八绝博物馆: '石景山区',
  北京东璧堂中医药博物馆: '房山区',
  北京市和光书院博物馆: '朝阳区',
  北京大戚收音机电影机博物馆: '通州区',
  北京菜百黄金珠宝博物馆: '西城区',
  北京市石景山区博物馆: '石景山区',
  颐和园博物馆: '海淀区',
  中国共产党早期北京革命活动纪念馆: '东城区',
  北京京华茶叶博物馆: '西城区',
  北京文景珍本期刊博物馆: '房山区',
  国家典籍博物馆: '海淀区',
  北京航空航天模型博物馆: '延庆区',
  北京法和律师博物馆: '东城区',
  北京龙顺成京作非遗博物馆: '东城区',
  中国共产党历史展览馆: '朝阳区',
  北京市顺义区博物馆: '顺义区',
  北京金漆镶嵌艺术博物馆: '朝阳区',
  北京云汇网球木拍博物馆: '朝阳区',
  北京自来水博物馆: '东城区',
  中国佛教图书文物馆: '西城区',
  北京劲飞京作红木文化博物馆: '昌平区',
  西黄寺博物馆: '朝阳区',
  北京中药炮制技术博物馆: '大兴区',
  '何扬·吴茜现代绘画馆': '朝阳区',
  平西抗日战争纪念馆: '房山区',
  北京中梦足球博物馆: '朝阳区',
  北京九鼎灶文化博物馆: '顺义区',
  北京宣南文化博物馆管理处: '西城区',
  '北京文博交流馆（北京市智化寺管理处）': '东城区',
  北京莱恩堡葡萄酒文化博物馆: '房山区',
  北京市房山世界地质公园博物馆: '房山区',
  北京百年世界老电话博物馆: '通州区',
  中国电信博物馆: '海淀区',
  北京市海淀区中关村村史馆: '海淀区',
  中国化工博物馆: '海淀区',
  北京服装学院民族服饰博物馆: '朝阳区',
  北京工艺美术博物馆: '朝阳区',
  中央美术学院美术馆: '朝阳区',
  北京警察博物馆: '东城区',
  '北京考古遗址博物馆（金中都水关遗址）': '丰台区',
  十三陵水库展览馆: '昌平区',
  国家大剧院台湖舞美艺术博物馆: '通州区',
  北京天桥印象博物馆: '西城区',
  北京牛栏山二锅头酒文化博物馆: '顺义区',
  石景山区石刻博物馆: '石景山区',
  北京公交馆: '丰台区',
  北京天元中医药博物馆: '朝阳区',
  视障文化博物馆: '西城区',
  中国木偶艺术剧院博物馆: '朝阳区',
  景泰蓝艺术博物馆: '东城区',
  北京六必居博物馆: '西城区',
  北京福履布鞋文化博物馆: '西城区',
  慈善寺古香道文化陈列馆: '石景山区',
  科学家博物馆: '朝阳区',
  全聚德博物馆: '西城区',
  对外经贸博物馆: '朝阳区',
  瀛海文史馆: '大兴区',
  宋庆龄故居管理中心: '西城区',
  万寿寺博物馆: '海淀区',
  北京舞蹈学院舞蹈博物馆: '海淀区',
  北京市大兴区天宫院乡情文史馆: '大兴区',
  '北京外国语大学校史馆、世界语言艺术博物馆': '海淀区',
  北京宝翠宫翡翠博物馆: '西城区',
  京东方历史展览馆: '朝阳区',
  水峪村生态博物馆: '房山区',
  北京神州连环画博物馆: '西城区',
  北京果脯博物馆: '怀柔区',
  延庆石刻博物馆: '延庆区',
  北京市大兴区榆垡镇乡情文史馆: '大兴区',
  北京遇见艺术博物馆: '朝阳区',
  北京神农农耕文化博物馆: '门头沟区',
  清华大学科学博物馆: '海淀区',
  徐悲鸿纪念馆: '西城区',
  炎黄艺术馆: '朝阳区',
  明十三陵博物馆: '昌平区',
  梅兰芳纪念馆: '西城区',
  雍和宫藏传佛教艺术博物馆: '东城区',
  '北京考古遗址博物馆（北京大葆台遗址博物馆）': '丰台区',
  北京大学赛克勒考古与艺术博物馆: '海淀区',
  北京市白塔寺管理处: '西城区',
  李大钊烈士陵园: '海淀区',
  詹天佑纪念馆: '延庆区',
  北京焦庄户地道战遗址纪念馆: '顺义区',
  中央民族大学民族博物馆: '海淀区',
  北京航空航天博物馆: '海淀区',
  北京房山云居寺石经博物馆: '房山区',
  密云区博物馆: '密云区',
  昌平区博物馆: '昌平区',
  通州区博物馆: '通州区',
  山戎文化陈列馆: '延庆区',
  '长辛店二·七纪念馆': '丰台区',
  上宅文化陈列馆: '平谷区',
  郭守敬纪念馆: '西城区',
  中国第四纪冰川遗迹陈列馆: '石景山区',
  周口店北京人遗址博物馆: '房山区',
  中国印刷博物馆: '大兴区',
  '中国工艺美术馆（中国非物质文化遗产馆）': '朝阳区',
  北京红楼文化艺术博物馆: '西城区',
  '北京中轴线遗产保护中心（正阳门）': '东城区',
  '北京明城墙遗址公园（东南城角角楼）': '东城区',
  '北京大觉寺与团城管理处（团城演武厅）': '海淀区',
  文天祥祠: '东城区',
  永定河文化博物馆: '门头沟区',
  北京市钟鼓楼文物保管所: '东城区',
  北京法海寺博物馆: '石景山区',
  中国国家画院美术馆: '海淀区',
  圆明园展览馆: '海淀区',
  '北京大觉寺与团城管理处（大觉寺）': '海淀区',
  北京中华民族博物院: '朝阳区',
  观复博物馆: '朝阳区',
  古陶文明博物馆: '西城区',
  中国钱币博物馆: '西城区',
  文化和旅游部恭王府博物馆: '西城区',
  中国现代文学馆: '朝阳区',
  慈悲庵: '西城区',
  中国蜜蜂博物馆: '海淀区',
  平北抗日战争纪念馆: '延庆区',
  卢沟桥历史博物馆: '丰台区',
  曹雪芹纪念馆: '海淀区',
  冀热察挺进军司令部旧址陈列馆: '门头沟区',
  北京中医药大学中医药博物馆: '朝阳区',
  香山双清别墅: '海淀区',
  老甲艺术馆: '昌平区',
  北京戏曲博物馆: '西城区',
  保利艺术博物馆: '东城区',
  北京中国紫檀博物馆: '朝阳区',
  北京南海子麋鹿苑博物馆: '大兴区',
  中华世纪坛艺术馆: '海淀区',
  北京王府井古人类文化遗址博物馆: '东城区',
  北京金台艺术馆: '朝阳区',
  '中国铁道博物馆（东郊展馆）': '朝阳区',
  中国铁道博物馆正阳门展馆: '东城区',
  北京皇城艺术馆: '东城区',
  北京御生堂中医药博物馆: '昌平区',
  居庸关长城博物馆: '昌平区',
  北京人民艺术剧院戏剧博物馆: '东城区',
  '北京市海淀区三山五园文化艺术中心（北京市海淀区博物...': '海淀区',
  毛主席纪念堂: '东城区',
  民族文化宫博物馆: '西城区',
  中国农业博物馆: '朝阳区',
  中国航天博物馆: '丰台区',
  地坛体育中心: '东城区',
  天坛体育中心: '东城区',
  东单体育中心: '东城区',
  地坛体育馆: '东城区',
  广安体育中心: '西城区',
  广安游泳网球馆: '西城区',
  月坛体育馆: '西城区',
  月坛综合训练馆: '西城区',
  月坛体育场: '西城区',
  西城区武术和棋类运动管理中心: '西城区',
  朝阳体育馆: '朝阳区',
  郡王府体育中心: '朝阳区',
  海淀温泉体育中心: '海淀区',
  北京市网球运动管理中心: '丰台区',
  丰台体育中心: '丰台区',
  门头沟区体育馆: '门头沟区',
  良乡训练基地: '房山区',
  房山区体育场: '房山区',
  良乡体育中心: '房山区',
  潞城全民健身中心: '通州区',
  顺义体育中心: '顺义区',
  顺义城南体育中心: '顺义区',
  昌平体育馆: '昌平区',
  昌平区体育运动场: '昌平区',
  回龙观体育文化公园: '昌平区',
  天通苑体育馆: '昌平区',
  大兴区体育中心: '大兴区',
  平谷区体育中心: '平谷区',
  怀柔区体育中心: '怀柔区',
  密云区体育中心: '密云区',
  延庆区体育中心: '延庆区',
  北京经济技术开发区体育中心: '北京经济技术开发区',
  燕山体育馆: '燕山地区',
  '重庆中国三峡博物馆(重庆博物馆)': '渝中区',
  '红岩革命纪念馆（重庆红岩革命历史博物馆）': '渝中区',
  '重庆歌乐山革命纪念馆（重庆红岩革命历史博物馆）': '沙坪坝区',
  大足石刻博物馆: '大足区',
  重庆大韩民国临时政府旧址陈列馆: '渝中区',
  '重庆特园民主党派历史陈列馆（中国民主党派历史陈列馆）': '渝中区',
  重庆历史名人馆: '渝中区',
  重庆抗战戏剧博物馆: '渝中区',
  '重庆史迪威博物馆（史迪威研究中心）': '渝中区',
  重庆体育博物馆: '渝中区',
  重庆典籍博物馆: '渝中区',
  二厂记忆博物馆: '渝中区',
  重庆嘉陵江索道博物馆: '两江新区',
  重庆自然资源科普馆: '两江新区',
  重庆师范大学博物馆: '沙坪坝区',
  重庆警察博物馆: '九龙坡区',
  重庆市规划展览馆: '南岸区',
  西南大学历史博物馆: '北碚区',
  中国西部科学院旧址陈列馆: '北碚区',
  重庆电信博物馆: '两江新区',
  重庆川剧博物馆: '两江新区',
  重庆白鹤梁水下博物馆: '涪陵区',
  重庆三峡移民纪念馆: '万州区',
  重庆市万州区博物馆: '万州区',
  重庆市万州革命烈士陵园管理中心: '万州区',
  重庆市万州良公祠民俗博物馆: '万州区',
  '万县“九五”惨案纪念馆': '万州区',
  重庆市万州区三峡石博物馆: '万州区',
  重庆市民族博物馆: '黔江区',
  万涛故居: '黔江区',
  黔江区博物馆: '黔江区',
  重庆市涪陵区博物馆: '涪陵区',
  重庆市渝中区博物馆: '渝中区',
  '重庆“湖广填四川”移民博物馆（重庆湖广会馆）': '渝中区',
  王琦美术博物馆: '渝中区',
  重庆巴渝民间中医药博物馆: '渝中区',
  重庆市巴渝名匾文化艺术博物馆: '渝中区',
  重庆市渝中区友好飞虎队博物馆: '渝中区',
  重庆市渝中区巴渝民风博物馆: '渝中区',
  重庆大轰炸遗址陈列馆: '渝中区',
  重庆金融历史博物馆: '渝中区',
  渝中区古典戏法魔术博物馆: '渝中区',
  重庆市大渡口区博物馆: '大渡口区',
  明玉珍睿陵陈列馆: '两江新区',
  重庆金融博物馆: '两江新区',
  重庆旁观者设计博物馆: '两江新区',
  '重庆市沙坪坝博物馆（重庆市沙坪坝区巴蜀古代建筑博物馆）': '沙坪坝区',
  重庆郭沫若纪念馆: '沙坪坝区',
  重庆张治中纪念馆: '沙坪坝区',
  重庆冯玉祥纪念馆: '沙坪坝区',
  重庆抗战教育博物馆: '沙坪坝区',
  重庆沙坪坝地质博物馆: '沙坪坝区',
  重庆市九龙坡区重庆巴人博物馆: '九龙坡区',
  '刘伯承六店旧居纪念馆（刘伯承六店旧居管理中心）': '九龙坡区',
  重庆华岩佛教博物馆: '九龙坡区',
  重庆三耳火锅博物馆: '九龙坡区',
  重庆市九龙坡区黄桷坪钢琴博物馆: '九龙坡区',
  重庆市九龙坡区九龙沉香博物馆: '九龙坡区',
  重庆市九龙坡区建川博物馆: '九龙坡区',
  重庆市九龙坡区周君记火锅调料历史文化博物馆: '九龙坡区',
  重庆抗战遗址博物馆: '南岸区',
  南岸区博物馆: '南岸区',
  重庆市中医药博物馆: '南岸区',
  重庆市南岸区德庄火锅博物馆: '南岸区',
  重庆市北碚区博物馆: '北碚区',
  卢作孚纪念馆: '北碚区',
  四世同堂纪念馆: '北碚区',
  梁实秋纪念馆: '北碚区',
  '抗战时期荣誉军人自治实验区陈列馆（重庆市北碚区博物馆分馆）': '北碚区',
  '晏阳初纪念馆（重庆市北碚区博物馆分馆）': '北碚区',
  '国立复旦大学重庆旧址（抗战时期复旦大学校史纪念馆）': '北碚区',
  中共中央西南局缙云山办公地旧址陈列馆: '北碚区',
  王朴烈士陵园: '北碚区',
  北碚教育博物馆: '北碚区',
  重庆巴渝民俗博物馆: '两江新区',
  重庆宝林博物馆: '两江新区',
  重庆市渝北区渝都古典照相机缝纫机博物馆: '两江新区',
  重庆御临旅游纪念品博物馆: '两江新区',
  重庆市巴南区博物馆: '巴南区',
  重庆长江石文化艺术博物馆: '巴南区',
  重庆市巴南区江碧波艺术博物馆: '巴南区',
  重庆市长寿区博物馆: '长寿区',
  重庆市长寿区杨克明故居陈列馆: '长寿区',
  江津博物馆: '江津区',
  聂荣臻元帅陈列馆: '江津区',
  重庆市江津区陈独秀旧居陈列馆: '江津区',
  中等师范教育历史陈列馆: '江津区',
  陶行知先生纪念馆: '合川区',
  钓鱼城古战场遗址博物馆: '合川区',
  重庆友军辣椒博物馆: '合川区',
  重庆市合川区三江民俗博物馆: '合川区',
  合川区楠山坊金丝楠木博物馆: '合川区',
  '永川博物馆（陈子庄艺术陈列馆）': '永川区',
  重庆市永川堃航博物馆: '永川区',
  重庆市永川区蕴宝博物馆: '永川区',
  南川区博物馆: '南川区',
  重庆市南川区蝶语昆虫博物馆: '南川区',
  綦江博物馆: '綦江区',
  重庆市綦江区红军长征纪念馆: '綦江区',
  饶国梁纪念馆: '大足区',
  重庆市大足区红岩重型汽车博物馆: '大足区',
  重庆大圆祥博物馆: '璧山区',
  铜梁区博物馆: '铜梁区',
  铜梁木匾博物馆: '铜梁区',
  重庆市铜梁区邱少云烈士纪念馆: '铜梁区',
  潼南区博物馆: '潼南区',
  '杨闇公杨尚昆旧居陈列馆（重庆市潼南区杨尚昆故里管理处）': '潼南区',
  荣昌陶博物馆: '荣昌区',
  张培爵纪念馆: '荣昌区',
  重庆市荣昌区万灵提琴博物馆: '荣昌区',
  重庆市荣昌陶窑口博物馆: '荣昌区',
  刘伯承同志纪念馆: '开州区',
  重庆市开州博物馆: '开州区',
  重庆市开州区雨青博物馆: '开州区',
  重庆市梁平区博物馆: '梁平区',
  重庆市武隆博物馆: '武隆区',
  后坪坝苏维埃政府史迹展览馆: '武隆区',
  和平中学旧址陈列馆: '武隆区',
  川陕苏区城口纪念馆: '城口县',
  城口县红三十三军指挥部旧址群陈列馆: '城万旧址：城口县',
  丰都县博物馆: '丰都县',
  云阳县博物馆: '云阳县',
  张桓侯庙博物馆: '云阳县',
  云阳古建博物苑: '云阳县',
  云阳县彭咏梧纪念馆: '云阳县',
  云阳县非物质文化遗产博物馆: '云阳县',
  奉节县夔州博物馆: '奉节县',
  奉节县白帝城博物馆: '奉节县',
  奉节县瞿塘关遗址博物馆: '奉节县',
  奉节县诗城博物馆: '奉节县',
  巫山博物馆: '巫山县',
  巫山县李季达陈列馆: '巫山县',
  巫山县下庄人事迹陈列馆: '巫山县',
  巫山县长康博物馆: '巫山县',
  巫溪县博物馆: '巫溪县',
  石柱土家族自治县博物馆: '石柱县',
  酉阳土家族苗族自治县酉州博物馆: '酉阳县',
  酉阳土家族苗族自治县赵世炎烈士纪念馆: '酉阳自治县',
  南腰界红三军司令部旧址陈列馆: '酉阳县',
  九黎苗族历史文化博物馆: '彭水县',
  重庆市万盛经济技术开发区博物馆: '万盛经开区',
  重庆市少年儿童图书馆: '两江新区',
  重庆市万州区图书馆: '万州区',
  重庆市黔江区图书馆: '黔江区',
  重庆市涪陵区图书馆: '涪陵区',
  重庆市渝中区图书馆: '渝中区',
  重庆市大渡口区图书馆: '大渡口区',
  重庆市江北区图书馆: '鸿恩寺馆:重庆市',
  重庆市沙坪坝区图书馆: '沙坪坝区',
  重庆市九龙坡区图书馆: '九龙坡区',
  重庆市南岸区图书馆: '南岸区',
  重庆市北碚图书馆: '北碚区',
  重庆市渝北区图书馆: '两江新区',
  重庆市巴南区图书馆: '巴南区',
  重庆市长寿区图书馆: '长寿区',
  重庆市江津区图书馆: '江津区',
  重庆市合川区图书馆: '合川区',
  重庆市南川区图书馆: '南川区',
  重庆市大足区图书馆: '大足区',
  重庆市双桥经开区图书馆: '大足区',
  重庆市万盛经济技术开发区图书馆: '万盛经济技术开发区',
  重庆市綦江区图书馆: '綦江区',
  重庆市永川区图书馆: '永川区',
  '重庆市潼南区图书馆（新馆）': '潼南区',
  重庆市璧山区图书馆: '璧山区',
  重庆市铜梁区图书馆: '铜梁区',
  重庆市荣昌区图书馆: 'A馆:重庆市',
  重庆市梁平区图书馆: '梁平区',
  重庆市武隆区图书馆: '武隆区',
  重庆市开州区图书馆: '开州区',
  重庆市城口县图书馆: '城口县',
  重庆市丰都县图书馆: '丰都县',
  重庆市垫江县图书馆: '垫江县',
  重庆市云阳县图书馆: '云阳县',
  重庆市奉节县图书馆: '奉节县',
  重庆市巫山县图书馆: '巫山县',
  重庆市巫溪县图书馆: '巫溪县',
  重庆市石柱土家族自治县图书馆: '石柱县',
  重庆市酉阳土家族苗族自治县图书馆: '酉阳县',
  重庆市群众艺术馆: '两江新区',
  重庆市万州区文化馆: '万州区',
  重庆市涪陵区文化馆: '涪陵区',
  重庆市渝中区文化馆: '渝中区',
  重庆市大渡口区文化馆: '大渡口区',
  重庆市江北区文化馆: '江北区',
  重庆市沙坪坝区文化馆: '沙坪坝区',
  重庆市九龙坡区文化馆: '九龙坡区',
  重庆市南岸区文化馆: '南岸区',
  重庆市北碚区文化馆: '北碚区',
  重庆市綦江区文化馆: '綦江区',
  重庆市大足区文化馆: '大足区',
  重庆市双桥经开区文化馆: '大足区',
  重庆市渝北区文化馆: '渝北区',
  重庆市巴南区文化馆: '巴南区',
  重庆市黔江区民族文化艺术馆: '黔江区',
  重庆市长寿区文化馆: '长寿区',
  重庆市江津区文化馆: '江津区',
  重庆市合川区文化馆: '合川区',
  重庆市永川区文化艺术馆: '永川区',
  重庆市南川区文化馆: '南川区',
  重庆市璧山区文化馆: '璧山区',
  重庆市万盛经开区文化馆: '万盛经开区',
  重庆市铜梁区文化馆: '铜梁区',
  重庆市潼南区文化馆: '潼南区',
  重庆市荣昌区文化馆: '荣昌区',
  重庆市开州区文化馆: '开州区',
  重庆市武隆区文化馆: '武隆区',
  重庆市城口县文化馆: '城口县',
  重庆市丰都县文化馆: '丰都县',
  重庆市垫江县文化馆: '垫江县',
  重庆市云阳县文化馆: '云阳县',
  重庆市奉节县文化馆: '奉节县',
  重庆市巫山县文化馆: '巫山县',
  重庆市巫溪县文化馆: '巫溪县',
  重庆市石柱土家族自治县文化馆: '石柱县',
  重庆市秀山土家族苗族自治县文化馆: '秀山县',
  重庆市酉阳土家族苗族自治县文化馆: '酉阳县',
  重庆市体育馆: '市体育馆',
  重庆市大田湾体育场: '大田湾体育场',
  重庆市奥林匹克体育中心体育场: '奥体中心体育场',
  重庆市奥林匹克体育中心游泳跳水馆: '奥体中心体育场',
  '万州游泳（跳水）馆': '万州区',
  万州区三峡之星体育馆: '万州区',
  万州体育场: '万州区',
  涪陵区体育场: '涪陵区',
  涪陵区体育馆: '涪陵区',
  大渡口区体育馆: '大渡口区',
  江南体育中心体育训练场: '南岸区',
  江南体育中心综合馆: '南岸区',
  江南游泳馆: '南岸区',
  江南体育馆: '南岸区',
  北陪区缙云体育中心体育场: '北陪区',
  北陪区绪云体育中心体育馆: '北陪区',
  万盛文体中心体育馆: '綦江区',
  万盛文体中心体育场: '綦江区',
  万盛滨江路体育馆: '綦江区',
  万盛游泳馆: '綦江区',
  綦江体育中心体育场: '綦江区',
  綦江区体育馆: '綦江区',
  大足区体育中心游泳馆: '大足区',
  大足区体育中心体育馆: '大足区',
  大足区体育中心体育场: '大足区',
  黔江区游泳馆: '黔江区',
  黔江区体育场: '黔江区',
  黔江区体育馆: '黔江区',
  长寿区体育中心体育馆: '长寿区',
  长寿区体育场: '长寿区',
  江津区体育馆: '江津区',
  江津区体育场: '江津区',
  江津区游泳馆: '江津区',
  '江津区全民健身指导中心（区羽毛球馆）': '江津区',
  合川区体育馆: '合川区',
  永川区游泳馆: '永川区',
  永川区体育中心体育场: '永川区',
  永川区体育馆: '永川区',
  南川区体育场: '南川区',
  南川区体育馆: '南川区',
  璧山区体育馆: '璧山区',
  璧山区体育中心: '璧山区',
  铜梁区藕塘湾体育场: '铜梁区',
  铜梁区全民健身中心: '铜梁区',
  铜梁区金龙体育馆: '铜梁区',
  铜梁龙体育场: '铜梁区',
  潼南区体育场: '潼南区',
  潼南区体育馆: '潼南区',
  荣昌区体育场: '荣昌区',
  荣昌区体育中心游泳池: '荣昌区',
  荣昌区全民健身活动中心: '荣昌区',
  荣昌区体育馆: '荣昌区',
  武隆区体育馆: '武隆区',
  庙坝镇全民健身中心: '城口县',
  东安镇全民健身中心: '城口县',
  城口县岗天乡全民健身中心: '城口县',
  城口县体育馆: '城口县',
  丰都县体育馆: '丰都县',
  丰都县体育场: '丰都县',
  垫江县体育馆: '垫江县',
  垫江县体育场: '垫江县',
  垫江县全民健身中心: '垫江县',
  忠县体育馆: '忠县',
  云阳县全民健身活动中心: '云阳县',
  云阳县体育馆: '云阳县',
  云阳县体育场: '云阳县',
  云阳县游泳中心: '云阳县',
  巫山县章家湾训练中心: '巫山县',
  重庆市巫山县苟家体育场: '巫山县',
  巫山县体育馆: '巫山县',
  巫山县全民健身中心: '巫山县',
  石柱县体育场: '石柱县',
  石柱县体育馆: '石柱县',
  秀山体育场: '秀山县',
  秀山体育馆: '秀山县',
  彭水县体育场: '彭水县',
  彭水县体育馆: '彭水县',
  彭水县全民健身中心: '彭水县',
  开州区体育馆: '开州区',
  开州区游泳馆: '开州区',
  开州区体育场: '开州区',
  梁平区东门体育馆: '梁平区',
  梁平区东门游泳馆: '梁平区',
  酉阳县体育馆: '酉阳县',
  杭州市西湖区文化馆: '西湖区',
  杭州市西湖区图书馆: '西湖区',
  余杭区文化馆: '余杭区',
  余杭区图书馆: '余杭区',
  仓前街道图书分馆: '余杭区',
  良渚街道图书分馆: '余杭区',
  仁和街道图书分馆: '余杭区',
  五常街道图书分馆: '余杭区',
  闲林街道图书分馆: '余杭区',
  余杭街道图书分馆: '余杭区',
  中泰街道图书分馆: '余杭区',
  百丈镇图书分馆: '余杭区',
  黄湖镇图书分馆: '余杭区',
  径山镇图书分馆: '余杭区',
  鸬鸟镇图书分馆: '余杭区',
  瓶窑镇图书分馆: '余杭区',
  '余杭章太炎故居纪念馆（章太炎研究中心）': '余杭区',
  '余杭小百花越剧艺术中心（苕溪大剧院）': '余杭区',
  余杭区非遗馆: '余杭区',
  良渚街道综合文化站: '余杭区',
  鸬鸟镇乡镇综合文化站: '余杭区',
  黄湖镇综合文化站: '余杭区',
  瓶窑镇综合文化站: '余杭区',
  中泰街道综合文化站: '余杭区',
  径山镇乡镇综合文化站: '余杭区',
  仁和街道综合文化站: '余杭区',
  仓前街道综合文化站: '余杭区',
  闲林街道综合文化站: '余杭区',
  百丈镇综合文化站: '余杭区',
  五常街道综合文化站: '余杭区',
  余杭街道综合文化站: '余杭区',
  杭州市滨江区文化馆: '滨江区',
  杭州市滨江区图书馆: '滨江区',
  杭州市滨江区非物质文化遗产馆: '滨江区',
  区文化馆: '临平区',
  区图书馆: '临平区',
  临平博物馆: '临平区',
  '图书馆临平街道分馆（智慧分馆）': '临平区',
  图书馆运河街道分馆: '临平区',
  图书馆南苑街道分馆: '临平区',
  图书馆星桥街道分馆: '临平区',
  图书馆乔司街道分馆: '临平区',
  图书馆崇贤街道分馆: '临平区',
  '图书馆东湖街道分馆（北沙书房）': '临平区',
  图书馆塘栖镇分馆: '临平区',
  黄炎培故居: '浦东新区',
  张闻天故居: '浦东新区',
  浦东历史博物馆: '浦东新区',
  上海中国航海博物馆: '浦东新区',
  高桥历史文化陈列馆: '浦东新区',
  新场历史文化陈列馆: '浦东新区',
  上海吴昌硕纪念馆: '浦东新区',
  上海美特斯邦威服饰博物馆: '浦东新区',
  上海动漫博物馆: '浦东新区',
  上海震旦博物馆: '浦东新区',
  '上海（中医药大学）中医药博物馆': '浦东新区',
  上海东方地质博物馆: '浦东新区',
  上海观复博物馆: '浦东新区',
  上海金刚博物馆: '浦东新区',
  上海有恒博物馆: '浦东新区',
  上海海派红木艺术博物馆: '浦东新区',
  交通银行博物馆: '浦东新区',
  上海老相机摄影博物馆: '浦东新区',
  上海火炬众创孵化博物馆: '浦东新区',
  '上海天文馆（上海科技馆分馆）': '浦东新区',
  上海宝库匠心博物馆: '浦东新区',
  上海双拥工作展览馆: '浦东新区',
  '上海市历史博物馆（上海革命历史博物馆）': '黄浦区',
  '中共代表团驻沪办事处纪念馆（周公馆）': '黄浦区',
  中国社会主义青年团中央机关旧址纪念馆: '黄浦区',
  上海豫园管理处: '黄浦区',
  上海三山会馆管理处: '黄浦区',
  上海韬奋纪念馆: '黄浦区',
  上海孙中山故居纪念馆: '黄浦区',
  上海周虎臣曹素功笔墨博物馆: '黄浦区',
  上海琉璃艺术博物馆: '黄浦区',
  上海电信博物馆: '黄浦区',
  上海民政博物馆: '黄浦区',
  上海市外滩历史纪念馆: '黄浦区',
  童涵春堂中药博物馆: '黄浦区',
  上海市银行博物馆: '黄浦区',
  大韩民国临时政府旧址管理处: '黄浦区',
  '国际乒联博物馆（中国乒乓球博物馆）': '黄浦区',
  上海体育博物馆: '黄浦区',
  中国劳动组合书记部旧址陈列馆: '静安区',
  上海毛泽东旧居陈列馆: '静安区',
  上海蔡元培故居陈列馆: '静安区',
  中共上海地下组织斗争史陈列馆暨刘长胜故居: '静安区',
  中共二大会址纪念馆: '静安区',
  '上海自然博物馆（上海科技馆分馆）': '静安区',
  中共三大后中央局机关历史纪念馆: '静安区',
  中共淞浦特委机关旧址陈列馆: '静安区',
  元利当铺旧址博物馆: '静安区',
  上海眼镜博物馆: '静安区',
  上海四行仓库抗战纪念馆: '静安区',
  上海棋牌文化博物馆: '静安区',
  上海印刷字体展示馆: '静安区',
  上海寰宇铃铛博物馆: '静安区',
  中共中央秘书处机关旧址纪念馆: '静安区',
  中共中央军委机关旧址纪念馆: '静安区',
  中央特科机关旧址纪念馆: '静安区',
  黄道婆纪念馆: '徐汇区',
  徐光启纪念馆: '徐汇区',
  上海土山湾博物馆: '徐汇区',
  上海市龙华烈士纪念馆: '徐汇区',
  上海宋庆龄故居纪念馆: '徐汇区',
  中国科学院上海昆虫博物馆: '徐汇区',
  上海师范大学博物馆: '徐汇区',
  上海音乐学院东方乐器博物馆: '徐汇区',
  上海交通大学校史博物馆: '徐汇区',
  上海交通大学董浩云航运博物馆: '徐汇区',
  钱学森图书馆: '徐汇区',
  上海无线电博物馆: '徐汇区',
  衡复风貌博物馆群: '徐汇区',
  上海气象博物馆: '徐汇区',
  上海品牌博物馆: '徐汇区',
  '《义勇军进行曲》灌制地纪念馆 （百代小楼）': '徐汇区',
  上海市长宁区革命文物陈列馆: '长宁区',
  宋庆龄生平事迹陈列馆: '长宁区',
  '上海（东华大学）纺织服饰博物馆': '长宁区',
  上海凝聚力工程博物馆: '长宁区',
  上海艺术品博物馆: '长宁区',
  上海广播博物馆: '长宁区',
  上海对外经贸大学博物馆: '长宁区',
  上海元代水闸遗址博物馆: '普陀区',
  顾正红纪念馆: '普陀区',
  苏州河工业文明展示馆: '普陀区',
  上海纺织博物馆: '普陀区',
  华东师范大学博物馆: '普陀区',
  沪西工人半日学校史料陈列馆: '普陀区',
  上海泰迪之家泰迪熊博物馆: '普陀区',
  上海鲁迅纪念馆: '虹口区',
  中共四大纪念馆: '虹口区',
  左联会址纪念馆: '虹口区',
  李白烈士故居: '虹口区',
  沈尹默故居: '虹口区',
  上海邮政博物馆: '虹口区',
  上海犹太难民纪念馆: '虹口区',
  中国证券博物馆: '虹口区',
  国歌展示馆: '杨浦区',
  上海中国烟草博物馆: '杨浦区',
  上海院士风采馆: '杨浦区',
  复旦大学博物馆: '杨浦区',
  上海理工大学印刷博物馆: '杨浦区',
  上海海洋大学博物馆: '杨浦区',
  上海体育大学武术博物馆: '杨浦区',
  上海财经大学商学博物馆: '杨浦区',
  同济大学博物馆: '杨浦区',
  中国近现代新闻出版博物馆: '杨浦区',
  上海世界技能博物馆: '杨浦区',
  上海淞沪抗战纪念馆: '宝山区',
  上海陈化成纪念馆: '宝山区',
  上海市陶行知纪念馆: '宝山区',
  上海解放纪念馆: '宝山区',
  南京路上好八连事迹陈列馆: '宝山区',
  '上海大学博物馆（海派文化博物馆）': '宝山区',
  上海中国工业设计博物馆: '宝山区',
  上海尊木汇木文化博物馆: '宝山区',
  上海智慧湾增材制造文化博物馆: '宝山区',
  上海百诺巧克力博物馆: '宝山区',
  上海杨明洁工业设计博物馆: '宝山区',
  闵行区博物馆: '闵行区',
  张充仁纪念馆: '闵行区',
  上海民族乐器博物馆: '闵行区',
  上海航宇科普中心: '闵行区',
  上海观止矿晶博物馆: '闵行区',
  上海翰林匾额博物馆: '闵行区',
  上海交通大学博物馆: '闵行区',
  上海乳业博物馆: '闵行区',
  嘉定竹刻博物馆: '嘉定区',
  顾维钧生平陈列馆: '嘉定区',
  四海壶具博物馆: '嘉定区',
  上海翥云艺术博物馆: '嘉定区',
  上海大来时间博物馆: '嘉定区',
  上海海纳吴觉农茶文化博物馆: '嘉定区',
  金山区博物馆: '金山区',
  上海南社纪念馆: '金山区',
  上海市沧海盐田盐文化博物馆: '金山区',
  上海市松江区博物馆: '松江区',
  上海中国留学生博物馆: '松江区',
  上海天文博物馆: '松江区',
  上海立信会计学院中国会计博物馆: '松江区',
  上海国际酒文化博物馆: '松江区',
  董其昌书画艺术博物馆: '松江区',
  上海外国语大学语言博物馆: '松江区',
  上海来伊份零食博物馆: '松江区',
  青浦区博物馆: '青浦区',
  陈云纪念馆: '青浦区',
  上海福寿园人文纪念馆: '青浦区',
  上海市青浦区任屯血防陈列馆: '青浦区',
  上海崧泽遗址博物馆: '青浦区',
  上海中华印刷博物馆: '青浦区',
  上海红十字历史文化陈列馆: '青浦区',
  奉贤区博物馆: '奉贤区',
  上海知青博物馆: '奉贤区',
  上海农垦博物馆: '奉贤区',
  上海真静传统木作博物馆: '奉贤区',
  上海电线电缆博物馆: '奉贤区',
  崇明区博物馆: '崇明区',
  上海崇明向化灶文化博物馆: '崇明区',
  上海崇明竖新抗日战争博物馆: '崇明区',
  江南造船展示馆: '崇明区',
  '上海图书馆（淮海馆）': '上海市',
  '上海图书馆（东馆）': '上海市',
  '上海少年儿童图书馆（长风馆）': '上海市',
  '上海少年儿童图书馆（南西馆）': '上海市',
  上海浦东图书馆: '浦东新区',
  上海浦东图书馆南汇分馆: '浦东新区',
  '上海浦东图书馆陆家嘴分馆（东方路）': '浦东新区',
  '上海浦东图书馆陆家嘴分馆（浦城路）': '浦东新区',
  上海浦东图书馆少儿分馆: '浦东新区',
  南码头路街道图书馆: '浦东新区',
  三林镇图书馆: '浦东新区',
  三林镇图书馆懿德分馆: '浦东新区',
  三林镇图书馆世博分馆: '浦东新区',
  塘桥街道图书馆: '浦东新区',
  北蔡镇图书馆: '浦东新区',
  张江图书馆: '浦东新区',
  张江图书馆孙桥分馆: '浦东新区',
  潍坊街道图书馆: '浦东新区',
  金杨新村街道图书馆: '浦东新区',
  周家渡街道图书馆: '浦东新区',
  上钢图书馆: '浦东新区',
  上钢图书馆综合体分馆: '浦东新区',
  花木街道图书馆: '浦东新区',
  东明路街道图书馆: '浦东新区',
  高东镇图书馆: '浦东新区',
  高桥镇图书馆: '浦东新区',
  高行镇图书馆: '浦东新区',
  '南汇新城镇图书馆（芦潮港馆）': '浦东新区',
  '南汇新城镇图书馆（申港馆）': '浦东新区',
  宣桥镇图书馆: '浦东新区',
  新场镇图书馆: '浦东新区',
  万祥镇图书馆: '浦东新区',
  合庆镇图书馆: '浦东新区',
  惠南镇图书馆: '浦东新区',
  惠南镇图书馆东城分馆: '浦东新区',
  '新川沙图书馆（成人馆）': '浦东新区',
  '新川沙图书馆（少儿馆）': '浦东新区',
  曹路镇图书馆: '浦东新区',
  康桥镇图书馆: '浦东新区',
  祝桥镇图书馆: '浦东新区',
  老港镇图书馆: '浦东新区',
  浦兴路街道图书馆: '浦东新区',
  浦兴路街道图书馆金桥湾分馆: '浦东新区',
  周浦镇图书馆: '浦东新区',
  傅雷图书馆: '浦东新区',
  泥城镇图书馆: '浦东新区',
  唐镇图书馆: '浦东新区',
  '唐镇图书馆（王港分中心）': '浦东新区',
  航头镇图书馆: '浦东新区',
  航头镇图书馆鹤沙分馆: '浦东新区',
  沪东社区图书馆: '浦东新区',
  陆家嘴街道图书馆: '浦东新区',
  书院镇图书馆: '浦东新区',
  洋泾社区图书馆: '浦东新区',
  金桥镇图书馆: '浦东新区',
  大团镇图书馆: '浦东新区',
  黄浦区图书馆: '黄浦区',
  '黄浦区明复图书馆(原卢湾区图书馆)': '黄浦区',
  半淞园路街道图书馆: '黄浦区',
  打浦桥街道图书馆: '黄浦区',
  淮海中路街道图书馆: '黄浦区',
  南京东路街道图书馆: '黄浦区',
  瑞金二路街道图书馆: '黄浦区',
  外滩街道图书馆: '黄浦区',
  五里桥街道图书馆: '黄浦区',
  小东门街道图书馆: '黄浦区',
  豫园街道图书馆: '黄浦区',
  老西门街道图书馆: '黄浦区',
  '静安区图书馆（新闸路）': '静安区',
  '静安区图书馆（天目中路）': '静安区',
  '静安区图书馆（闻喜路）': '静安区',
  静安区少年儿童图书馆: '静安区',
  静安区闸北少年儿童图书馆: '静安区',
  曹家渡街道图书馆: '静安区',
  曹家渡街道达安星之会所图书室: '静安区',
  '曹家渡街道图书馆（少儿）': '静安区',
  静安区图书馆北站街道分馆: '静安区',
  江宁路街道图书馆: '静安区',
  静安寺街道图书馆: '静安区',
  南京西路街道图书馆: '静安区',
  南京西路街道少儿图书馆: '静安区',
  石门二路街道图书馆: '静安区',
  宝山路街道图书馆: '静安区',
  '北站街道图书馆（艺术图书馆）': '静安区',
  大宁路街道图书馆: '静安区',
  宁的书房: '静安区',
  '大宁路街道分馆（社区文化中心）': '静安区',
  共和新路街道图书馆: '静安区',
  临汾路街道图书馆: '静安区',
  彭浦新村街道图书馆: '静安区',
  彭浦镇图书馆: '静安区',
  天目西路街道图书馆: '静安区',
  芷江西路街道图书馆: '静安区',
  '徐汇区图书馆（徐家汇书院）': '徐汇区',
  徐家汇街道图书馆: '徐汇区',
  天平路街道图书馆: '徐汇区',
  湖南路街道图书馆: '徐汇区',
  枫林路街道图书馆: '徐汇区',
  斜土路街道图书馆: '徐汇区',
  田林街道图书馆: '徐汇区',
  长桥街道图书馆: '徐汇区',
  虹梅路街道图书馆: '徐汇区',
  康健新村街道图书馆: '徐汇区',
  龙华街道图书馆: '徐汇区',
  凌云路街道图书馆: '徐汇区',
  漕河泾街道图书馆: '徐汇区',
  '漕河泾街道图书馆 石龙分馆': '徐汇区',
  华泾镇图书馆: '徐汇区',
  '长宁区图书馆（天山馆）': '长宁区',
  '长宁区图书馆（愚园馆）': '长宁区',
  '长宁区图书馆（仙霞馆）': '长宁区',
  北新泾街道图书馆: '长宁区',
  程家桥街道图书馆: '长宁区',
  虹桥街道图书馆: '长宁区',
  '虹桥街道图书馆分馆（古北天空书苑）': '长宁区',
  华阳路街道图书馆: '长宁区',
  江苏路街道图书馆: '长宁区',
  天山路街道图书馆: '长宁区',
  仙霞新村街道图书馆: '长宁区',
  新华路街道图书馆: '长宁区',
  新泾镇图书馆: '长宁区',
  周家桥街道图书馆: '长宁区',
  曹杨新村街道图书馆: '普陀区',
  长风新村街道图书馆: '普陀区',
  长寿路街道图书馆: '普陀区',
  万里街道图书馆: '普陀区',
  长征镇图书馆: '普陀区',
  甘泉街道图书馆: '普陀区',
  石泉路街道图书馆: '普陀区',
  桃浦镇图书馆: '普陀区',
  宜川路街道图书馆: '普陀区',
  真如镇街道图书馆: '普陀区',
  虹口区图书馆: '虹口区',
  虹口区图书馆曲阳分馆: '虹口区',
  虹口区图书馆和平分馆: '虹口区',
  广中路街道图书馆: '虹口区',
  嘉兴路街道图书馆: '虹口区',
  江湾镇街道图书馆: '虹口区',
  '江湾镇街道图书馆分馆（逸仙会客厅）': '虹口区',
  凉城新村街道图书馆: '虹口区',
  欧阳路街道图书馆: '虹口区',
  曲阳路街道图书馆: '虹口区',
  北外滩街道图书馆: '虹口区',
  四川北路街道图书馆: '虹口区',
  '杨浦区图书馆（平凉分馆）': '杨浦区',
  '杨浦区图书馆（少儿分馆）': '杨浦区',
  长白新村街道图书馆: '杨浦区',
  大桥街道图书馆: '杨浦区',
  定海路街道图书馆: '杨浦区',
  江浦路街道图书馆: '杨浦区',
  江浦路街道图书馆少儿分馆: '杨浦区',
  控江路街道图书馆: '杨浦区',
  平凉路街道图书馆: '杨浦区',
  四平路街道图书馆: '杨浦区',
  五角场街道图书馆: '杨浦区',
  '五角场街道图书馆（国定支路分馆）': '杨浦区',
  '长海路街道图书馆（政府路馆）': '杨浦区',
  '长海路街道图书馆（翔殷路馆）': '杨浦区',
  '长海路街道图书馆（市光路馆）': '杨浦区',
  延吉新村街道图书馆: '杨浦区',
  殷行街道图书馆: '杨浦区',
  新江湾城街道图书馆: '杨浦区',
  大场镇图书馆: '宝山区',
  高境镇图书馆: '宝山区',
  顾村镇图书馆: '宝山区',
  '顾村镇图书馆（诗乡广场分馆）': '宝山区',
  '顾村镇图书馆（馨佳园分馆）': '宝山区',
  '顾村镇图书馆（菊泉分馆）': '宝山区',
  罗店镇图书馆: '宝山区',
  '罗店镇图书馆（塘西街分馆）': '宝山区',
  '罗店镇图书馆（美兰西湖分馆）': '宝山区',
  罗泾镇图书馆: '宝山区',
  罗泾镇图书馆分馆: '宝山区',
  庙行镇图书馆: '宝山区',
  淞南镇图书馆: '宝山区',
  吴淞街道图书馆: '宝山区',
  杨行镇图书馆: '宝山区',
  友谊路街道图书馆: '宝山区',
  '月浦镇图书馆（盛桥馆）': '宝山区',
  '月浦镇图书馆（庆安路馆）': '宝山区',
  '月浦镇图书馆（龙镇路馆）': '宝山区',
  '月浦镇图书馆（马泾桥馆）': '宝山区',
  张庙街道图书馆: '宝山区',
  '古美路街道图书馆（东馆）': '闵行区',
  '古美路街道图书馆（西馆）': '闵行区',
  虹桥镇图书馆: '闵行区',
  华漕镇图书馆: '闵行区',
  大零号湾图书馆: '闵行区',
  马桥镇图书馆: '闵行区',
  梅陇镇图书馆: '闵行区',
  梅陇镇图书馆晶城分馆: '闵行区',
  浦江图书馆: '闵行区',
  浦江镇图书馆永康分馆: '闵行区',
  七宝镇图书馆: '闵行区',
  吴泾镇图书馆: '闵行区',
  新虹街道图书馆: '闵行区',
  莘庄工业区图书馆: '闵行区',
  莘庄镇图书馆: '闵行区',
  颛桥镇图书馆: '闵行区',
  浦锦街道图书馆: '闵行区',
  嘉定区图书馆: '嘉定区',
  嘉定区图书馆清河路分馆: '嘉定区',
  安亭镇图书馆: '嘉定区',
  '安亭镇图书馆（黄渡分馆）': '嘉定区',
  '安亭镇图书馆（方泰分馆）': '嘉定区',
  华亭镇图书馆: '嘉定区',
  嘉定工业区图书馆: '嘉定区',
  嘉定镇街道图书馆: '嘉定区',
  江桥镇图书馆: '嘉定区',
  江桥镇龙湖图书馆: '嘉定区',
  菊园新区图书馆: '嘉定区',
  马陆镇图书馆: '嘉定区',
  南翔镇图书馆: '嘉定区',
  南翔镇图书馆东社区分馆: '嘉定区',
  外冈镇图书馆: '嘉定区',
  新成路街道图书馆: '嘉定区',
  徐行镇图书馆: '嘉定区',
  真新街道图书馆: '嘉定区',
  '真新街道图书馆（新丰分馆）': '嘉定区',
  金山区图书馆: '金山区',
  漕泾镇图书馆: '金山区',
  枫泾镇图书馆: '金山区',
  高新区图书馆: '金山区',
  金山卫镇图书馆: '金山区',
  金山卫镇图书馆钱圩分馆: '金山区',
  廊下镇图书馆: '金山区',
  吕巷镇图书馆: '金山区',
  吕巷镇图书馆干巷分馆: '金山区',
  山阳镇图书馆: '金山区',
  山阳镇海璟图书馆: '金山区',
  石化街道图书馆: '金山区',
  亭林镇图书馆: '金山区',
  张堰镇图书馆: '金山区',
  朱泾镇图书馆: '金山区',
  朱泾镇图书馆新农分馆: '金山区',
  '人文松江活动中心（松江区图书馆）': '松江区',
  车墩镇图书馆: '松江区',
  洞泾镇图书馆: '松江区',
  方松街道图书馆: '松江区',
  九亭镇图书馆: '松江区',
  泖港镇图书馆: '松江区',
  佘山镇图书馆: '松江区',
  佘山镇佘北图书馆: '松江区',
  石湖荡镇图书馆: '松江区',
  泗泾镇图书馆: '松江区',
  泗泾新凯图书馆: '松江区',
  泗泾新凯大居图书馆: '松江区',
  小昆山镇图书馆: '松江区',
  新浜镇图书馆: '松江区',
  新桥镇图书馆: '松江区',
  叶榭镇图书馆: '松江区',
  永丰街道图书馆: '松江区',
  岳阳街道图书馆: '松江区',
  中山街道图书馆: '松江区',
  九里亭街道图书馆: '松江区',
  广富林街道图书馆: '松江区',
  青浦区图书馆: '青浦区',
  白鹤镇图书馆: '青浦区',
  '白鹤镇图书馆（赵屯分中心）': '青浦区',
  华新镇图书馆: '青浦区',
  '华新镇图书馆（凤溪分馆）': '青浦区',
  金泽镇图书馆: '青浦区',
  练塘镇图书馆: '青浦区',
  夏阳街道图书馆: '青浦区',
  徐泾镇图书馆: '青浦区',
  '徐泾镇图书馆（北大居分馆）': '青浦区',
  赵巷镇图书馆: '青浦区',
  '赵巷镇图书馆（新城一站分馆）': '青浦区',
  '青溪书房·赵巷公园': '青浦区',
  重固镇图书馆: '青浦区',
  朱家角镇图书馆: '青浦区',
  香花桥街道图书馆: '青浦区',
  '香花桥街道图书馆 （玉兰花园分馆）': '青浦区',
  盈浦街道图书馆: '青浦区',
  奉贤区图书馆: '奉贤区',
  奉城镇图书馆: '奉贤区',
  海湾镇图书馆: '奉贤区',
  金汇镇图书馆: '奉贤区',
  南桥镇图书馆: '奉贤区',
  青村镇图书馆: '奉贤区',
  四团镇图书馆: '奉贤区',
  柘林镇图书馆: '奉贤区',
  庄行镇图书馆: '奉贤区',
  奉浦街道图书馆: '奉贤区',
  西渡街道图书馆: '奉贤区',
  金海街道图书馆: '奉贤区',
  海湾旅游区图书馆: '奉贤区',
  头桥街道图书馆: '奉贤区',
  崇明区图书馆: '崇明区',
  堡镇图书馆: '崇明区',
  长兴镇图书馆: '崇明区',
  陈家镇图书馆: '崇明区',
  城桥镇图书馆: '崇明区',
  东平镇图书馆: '崇明区',
  港西镇图书馆: '崇明区',
  港沿镇图书馆: '崇明区',
  横沙乡图书馆: '崇明区',
  建设镇图书馆: '崇明区',
  绿华镇图书馆: '崇明区',
  庙镇图书馆: '崇明区',
  三星镇图书馆: '崇明区',
  竖新镇图书馆: '崇明区',
  向化镇图书馆: '崇明区',
  新村乡图书馆: '崇明区',
  新海镇图书馆: '崇明区',
  新河镇图书馆: '崇明区',
  中兴镇图书馆: '崇明区',
  上海浦东碧云美术馆: '浦东新区',
  海派连环画艺术馆: '浦东新区',
  上海王狮美术馆: '浦东新区',
  浦东云间美术馆: '浦东新区',
  周浦美术馆: '浦东新区',
  上海浦东林隐美术馆: '浦东新区',
  上海浦东新区库伯美术馆: '浦东新区',
  上海艺仓美术馆: '浦东新区',
  上海昊美术馆: '浦东新区',
  上海浦东新区联明美术馆: '浦东新区',
  上海浦东新区叁柒贰叁美术馆: '浦东新区',
  上海浦东新区越婷惠美术馆: '浦东新区',
  震旦美术馆: '浦东新区',
  上海久事美术馆: '黄浦区',
  春美术馆: '黄浦区',
  胡问遂艺术馆: '黄浦区',
  上海驰翰美术馆: '黄浦区',
  上海民生现代美术馆: '黄浦区',
  'chi K11美术馆': '黄浦区',
  上海外滩美术馆: '黄浦区',
  上海复星艺术中心: '黄浦区',
  华山艺术馆: '静安区',
  明当代美术馆: '静安区',
  心象艺术馆: '静安区',
  上海静安毕加索艺术馆: '静安区',
  上海静安大风堂美术馆: '静安区',
  上海大学美术馆: '静安区',
  'Fotografiska 影像艺术中心': '静安区',
  上海中国画院美术馆: '徐汇区',
  上海市徐汇区艺术馆: '徐汇区',
  西岸美术馆: '徐汇区',
  '龙美术馆（西岸馆）': '徐汇区',
  上海油罐艺术中心: '徐汇区',
  START星美术馆: '徐汇区',
  上海明圆美术馆: '徐汇区',
  上海徐汇区九点水美术馆: '徐汇区',
  刘海粟美术馆: '长宁区',
  上海油画雕塑院美术馆: '长宁区',
  '上海中国画院 程十发美术馆': '长宁区',
  上海虹桥当代美术馆: '长宁区',
  上海正好美术馆: '长宁区',
  上海杨培明宣传画收藏艺术馆: '长宁区',
  上海长宁华萃当代美术馆: '长宁区',
  上海长宁王小慧艺术馆: '长宁区',
  '刘海粟美术馆(分馆)': '普陀区',
  上海苏宁艺术馆: '普陀区',
  朱屺瞻艺术馆: '虹口区',
  上海多伦现代美术馆: '虹口区',
  上海虹口青藤美术馆: '虹口区',
  趣看美术馆: '虹口区',
  敦煌当代美术馆: '杨浦区',
  鸿一美术馆: '杨浦区',
  刘小晴艺术馆: '杨浦区',
  上海美术学院美术馆: '宝山区',
  上海湫光美术馆: '宝山区',
  上海宝山区龙现代美术馆: '宝山区',
  '上海交通大学 程及美术馆': '闵行区',
  上海海派艺术馆: '闵行区',
  蔡兵美术馆: '闵行区',
  上海宝龙美术馆: '闵行区',
  上海明珠美术馆: '闵行区',
  上海闵行区美博美术馆: '闵行区',
  上海半岛美术馆: '闵行区',
  中闵虹桥美术馆: '闵行区',
  上海金臣亦飞鸣美术馆: '闵行区',
  陆俨少艺术院: '嘉定区',
  上海韩天衡美术馆: '嘉定区',
  上海秦古美术馆: '嘉定区',
  泰美术馆: '嘉定区',
  上海嘉定区北虹桥美术馆: '嘉定区',
  嘉源海美术馆: '嘉定区',
  上海嘉定十方画院: '嘉定区',
  丁聪美术馆: '金山区',
  上海金山区海鸥美术馆: '金山区',
  云间会堂美术馆: '松江区',
  程十发艺术馆: '松江区',
  松江美术馆: '松江区',
  上海松江云间美术馆: '松江区',
  上海艺术百代美术馆: '松江区',
  上海YOUNG美术馆: '松江区',
  上海松江清控人居美术馆: '松江区',
  上海松江区新桥美术馆: '松江区',
  上海松江区贤禾美术馆: '松江区',
  上海松江云间少儿美术馆: '松江区',
  上海国稷美术馆: '松江区',
  洙桥美术馆: '松江区',
  余德耀美术馆: '青浦区',
  上海市鹤龙美术馆: '青浦区',
  上海青浦青渚美术馆: '青浦区',
  上海青浦区金夜美术馆: '青浦区',
  上海青浦区练塘可的美术馆: '青浦区',
  上海吴宜恩美术馆: '奉贤区',
  崇明美术馆: '崇明区',
  浦东新区文化艺术指导中心: '浦东新区',
  浦东新区文化艺术指导中心惠南分中心: '浦东新区',
  浦东新区文化艺术指导中心外高桥分中心: '浦东新区',
  浦东新区金海文化艺术中心: '浦东新区',
  浦东新区浦东文化馆: '浦东新区',
  浦东新区浦南文化馆: '浦东新区',
  黄浦区文化馆: '黄浦区',
  徐汇区文化馆: '徐汇区',
  长宁文化艺术中心: '长宁区',
  静安区文化馆: '静安区',
  静安区文化馆分馆: '静安区',
  虹口区文化馆: '虹口区',
  杨浦文化艺术中心: '杨浦区',
  普陀区文化馆: '普陀区',
  '上海市闵行区文化和旅游管理事务中心 （上海市闵行区群众艺术馆）': '闵行区',
  金山区文化馆: '金山区',
  '人文松江活动中心（松江区文化馆）': '松江区',
  青浦区文化馆: '青浦区',
  奉贤区文化馆: '奉贤区',
  崇明区文化馆: '崇明区',
  周浦镇文化服务中心: '浦东新区',
  三林镇文化服务中心: '浦东新区',
  三林镇懿德文化分中心: '浦东新区',
  三林镇前滩社区文化分中心: '浦东新区',
  泥城镇文化服务中心: '浦东新区',
  金杨社区文化活动中心: '浦东新区',
  金杨社区文化活动中心云山路分中心: '浦东新区',
  唐镇文化体育中心: '浦东新区',
  大团镇文化服务中心: '浦东新区',
  金桥镇文化服务中心: '浦东新区',
  书院镇文化服务中心: '浦东新区',
  曹路镇文化服务中心: '浦东新区',
  曹路社区文化活动中心: '浦东新区',
  曹路社区文化活动中心顾路分中心: '浦东新区',
  花木街道社区文化活动中心: '浦东新区',
  川沙新镇文化服务中心: '浦东新区',
  祝桥镇文化服务中心: '浦东新区',
  惠南镇文化服务中心: '浦东新区',
  新场镇文化服务中心: '浦东新区',
  浦兴社区文化活动中心: '浦东新区',
  浦兴社区文化活动中心金桥湾分中心: '浦东新区',
  高东镇文化服务中心: '浦东新区',
  塘桥社区文化活动中心: '浦东新区',
  老港镇文化服务中心: '浦东新区',
  康桥镇文化服务中心: '浦东新区',
  航头镇文化服务中心: '浦东新区',
  航头镇文化服务中心鹤沙分中心: '浦东新区',
  '南汇新城镇社区党群服务中心（文化服务中心）': '浦东新区',
  陆家嘴金融城文化中心: '浦东新区',
  陆家嘴金融城文化分中心: '浦东新区',
  高行镇文化服务中心: '浦东新区',
  万祥镇文化服务中心: '浦东新区',
  宣桥镇社区文化活动中心: '浦东新区',
  周家渡街道文化中心: '浦东新区',
  潍坊社区文化活动中心: '浦东新区',
  上钢社区文化活动中心: '浦东新区',
  南码头社区文化活动中心: '浦东新区',
  洋泾社区文化活动中心: '浦东新区',
  北蔡镇文化服务中心: '浦东新区',
  合庆镇文化服务中心: '浦东新区',
  张江镇文化服务中心: '浦东新区',
  张江镇文化服务中心-孙桥分中心: '浦东新区',
  沪东社区文化活动中心: '浦东新区',
  沪东社区文化分中心: '浦东新区',
  高桥镇文化服务中心: '浦东新区',
  东明社区文化活动中心: '浦东新区',
  东明社区文化活动分中心: '浦东新区',
  五里桥社区文化活动中心: '黄浦区',
  南京东路社区文化活动中心: '黄浦区',
  打浦桥社区文化活动中心: '黄浦区',
  瑞金二路社区文化活动中心: '黄浦区',
  淮海中路社区文化活动中心: '黄浦区',
  外滩社区文化活动中心: '黄浦区',
  小东门街道社区文化活动中心: '黄浦区',
  半淞园路社区文化活动中心: '黄浦区',
  豫园社区文化活动中心: '黄浦区',
  老西门社区文化活动中心: '黄浦区',
  石门二路社区文化活动中心: '静安区',
  北站街道社区文化活动中心: '静安区',
  临汾社区文化活动中心: '静安区',
  江宁路街道社区文化活动中心: '静安区',
  江宁路街道社区文化活动中心分中心: '静安区',
  '南京西路街道社区文化活动中心（福民会馆）': '静安区',
  曹家渡街道社区文化活动中心: '静安区',
  静安寺街道社区文化活动中心: '静安区',
  大宁路街道社区文化活动中心: '静安区',
  彭浦镇社区文化活动中心: '静安区',
  宝山路街道党群服务中心: '静安区',
  共和新路街道社区党群服务中心: '静安区',
  彭浦新村街道社区文化活动中心: '静安区',
  芷江西路街道社区文化活动中心: '静安区',
  天目西路街道社区文化活动中心: '静安区',
  徐家汇社区文化活动中心: '徐汇区',
  天平街道社区文化活动中心: '徐汇区',
  '天平街道66梧桐院(文化活动分中心)': '徐汇区',
  湖南街道社区文化活动中心: '徐汇区',
  '枫林街道社区党群服务中心(文化活动分中心)': '徐汇区',
  '枫林街道天龙党群服务中心(文化活动分中心)': '徐汇区',
  斜土社区文化活动中心: '徐汇区',
  田林街道党群服务中心: '徐汇区',
  长桥社区文化活动中心: '徐汇区',
  虹梅街道党群服务中心: '徐汇区',
  康健街道社区党群服务中心: '徐汇区',
  龙华社区党群中心: '徐汇区',
  凌云街道社区文化活动中心: '徐汇区',
  漕河泾街道社区文化活动中心: '徐汇区',
  华泾社区文化活动中心: '徐汇区',
  华阳社区文化活动中心: '长宁区',
  新泾镇社区文化事务中心: '长宁区',
  北新泾社区文化活动中心: '长宁区',
  天山社区文化活动中心: '长宁区',
  新华社区文化活动中心: '长宁区',
  '仙霞社区文化活动中心（西部）': '长宁区',
  '仙霞社区文化活动中心（东部）': '长宁区',
  程家桥街道社区文化活动中心: '长宁区',
  虹桥街道社区文化活动中心: '长宁区',
  '虹桥街道社区文化活动中心（分中心）': '长宁区',
  周家桥社区文化活动中心: '长宁区',
  江苏路街道社区文化活动中心: '长宁区',
  长征社区文化活动中心: '普陀区',
  曹杨社区文化活动中心: '普陀区',
  甘泉社区文化活动中心: '普陀区',
  长风社区文化活动中心: '普陀区',
  桃浦社区文化活动中心: '普陀区',
  真如社区文化活动中心: '普陀区',
  长寿社区文化活动中心: '普陀区',
  石泉社区文化活动中心: '普陀区',
  宜川社区文化活动中心: '普陀区',
  万里社区文化活动中心: '普陀区',
  嘉兴路街道社区文化活动中心: '虹口区',
  嘉兴路街道社区文化活动分中心: '虹口区',
  曲阳路街道社区文化活动中心: '虹口区',
  江湾镇街道社区文化活动中心: '虹口区',
  欧阳路街道社区文化活动中心: '虹口区',
  四川北路街道社区文化活动中心: '虹口区',
  凉城新村街道社区文化活动中心: '虹口区',
  北外滩街道社区文化活动中心: '虹口区',
  广中路街道社区文化活动中心: '虹口区',
  五角场社区文化活动中心: '杨浦区',
  五角场社区文化活动分中心: '杨浦区',
  大桥街道社区文化活动中心: '杨浦区',
  四平路街道社区文化活动中心: '杨浦区',
  定海路街道社区文化活动中心: '杨浦区',
  定海路街道社区文化活动分中心: '杨浦区',
  平凉社区文化活动中心: '杨浦区',
  长白新村街道社区文化活动中心: '杨浦区',
  '228街坊文化活动中心': '杨浦区',
  长海路街道社区文化活动中心: '杨浦区',
  长海路街道社区文化活动分中心: '杨浦区',
  延吉社区文化活动中心: '杨浦区',
  江浦社区文化活动中心: '杨浦区',
  江浦路街道社区文化活动分中心: '杨浦区',
  控江路街道社区文化活动中心: '杨浦区',
  控江路街道社区文化活动分中心: '杨浦区',
  殷行社区文化活动中心: '杨浦区',
  新江湾城社区文化活动中心: '杨浦区',
  政青路文化活动分中心: '杨浦区',
  罗店镇社区文化活动中心: '宝山区',
  罗店镇社区文化活动分中心: '宝山区',
  友谊路街道社区事务受理服务中心: '宝山区',
  友谊路街道社区文化活动分中心: '宝山区',
  顾村镇社区文化活动中心: '宝山区',
  顾村镇菊泉文体中心: '宝山区',
  顾村镇馨佳园社区文化活动中心: '宝山区',
  罗泾镇社区文化活动中心: '宝山区',
  罗泾镇社区文化活动分中心: '宝山区',
  吴淞街道社区文化活动中心: '宝山区',
  高境镇社区文化活动中心: '宝山区',
  高境镇社区文化活动分中心: '宝山区',
  杨行镇社会事业发展服务中心: '宝山区',
  庙行镇社区文化活动中心: '宝山区',
  庙行镇社区文化活动分中心: '宝山区',
  淞南镇社区文化活动中心: '宝山区',
  月浦镇社区文化活动中心: '宝山区',
  '月浦镇社区文化中心（友间公寓分中心）': '宝山区',
  张庙街道社区文化活动中心: '宝山区',
  大场镇社会事业发展服务中心: '宝山区',
  虹桥镇文化体育事业发展中心: '闵行区',
  颛桥镇文体中心: '闵行区',
  江川文化馆: '闵行区',
  新虹街道社区党群服务中心: '闵行区',
  古美路街道社区党群服务中心: '闵行区',
  马桥景城文化中心: '闵行区',
  华漕镇文化体育事业发展中心: '闵行区',
  莘庄工业区文化体育事业发展中心: '闵行区',
  浦江镇社区文化活动中心: '闵行区',
  浦江镇青少年社区文化活动中心: '闵行区',
  浦江镇瑞和社区文化活动中心: '闵行区',
  吴泾镇社区文化活动中心: '闵行区',
  莘庄镇文化体育事业发展中心: '闵行区',
  七宝镇文化体育事业发展中心: '闵行区',
  '七宝体育活动中心（航华分中心）': '闵行区',
  闵行区梅陇镇文化体育事业发展中心: '闵行区',
  '浦锦街道社区党群服务中心（文化体育）': '闵行区',
  嘉定镇社区党群服务中心: '嘉定区',
  外冈镇文化体育服务中心: '嘉定区',
  菊园新区社区文化活动中心: '嘉定区',
  新成路街道社区党群服务中心: '嘉定区',
  南翔镇文化体育服务中心: '嘉定区',
  华亭镇社区文化活动中心: '嘉定区',
  真新街道社区党群服务中心: '嘉定区',
  徐行镇文化体育服务中心: '嘉定区',
  江桥镇社区文化活动中心: '嘉定区',
  嘉定工业区文化体育服务中心: '嘉定区',
  马陆镇文化体育服务中心: '嘉定区',
  安亭镇文化体育服务中心: '嘉定区',
  安亭镇文化体育服务中心黄渡分中心: '嘉定区',
  安亭镇文化体育服务中心方泰分中心: '嘉定区',
  朱泾镇社区文化活动中心: '金山区',
  朱泾镇社区文化活动中心新农分中心: '金山区',
  山阳镇社区党群服务中心: '金山区',
  漕泾镇社区党群服务中心: '金山区',
  枫泾镇社区党群服务中心: '金山区',
  枫泾镇社区文化活动中心兴塔分中心: '金山区',
  吕巷镇社区党群服务中心: '金山区',
  亭林镇社区文化活动中心: '金山区',
  亭林镇社区文化活动中心松隐分中心: '金山区',
  高新区社区文化活动中心: '金山区',
  金山卫镇社区党群服务中心: '金山区',
  金山卫镇社区文化活动中心钱圩分中心: '金山区',
  廊下镇社区党群服务中心: '金山区',
  张堰镇社区党群服务中心: '金山区',
  石化街道社区党群服务中心: '金山区',
  方松社区文化活动中心: '松江区',
  '中山街道社区党群服务中心（中山幸福里）': '松江区',
  永丰街道社区党群服务中心: '松江区',
  佘山镇社区文化活动中心: '松江区',
  佘山镇社区文化活动中心佘北分中心: '松江区',
  泗泾镇社区文化活动中心: '松江区',
  泗泾镇新凯社区文化活动中心: '松江区',
  九亭镇社区文化活动中心: '松江区',
  新浜镇社区文化活动中心: '松江区',
  车墩镇社区文化活动中心: '松江区',
  岳阳街道社区党群服务中心: '松江区',
  叶榭镇社区文化活动中心: '松江区',
  广富林街道社区文化活动中心: '松江区',
  洞泾镇社区文化活动中心: '松江区',
  新桥镇社区党群服务中心: '松江区',
  九里亭街道社区党群服务中心: '松江区',
  石湖荡镇社区文化活动中心: '松江区',
  泖港镇社区文化活动中心: '松江区',
  小昆山镇社区党群服务中心: '松江区',
  徐泾社区文化活动中心: '青浦区',
  徐泾北大居社区文化活动分中心: '青浦区',
  练塘镇社区文化活动中心: '青浦区',
  '练塘镇社区文化活动中心（小蒸分中心）': '青浦区',
  '练塘镇社区文化活动中心（蒸淀分中心）': '青浦区',
  白鹤镇社区文化活动中心: '青浦区',
  '白鹤镇社区文化活动中心（赵屯分中心）': '青浦区',
  朱家角镇社区文化活动中心: '青浦区',
  朱家角镇沈巷社区文化活动中心: '青浦区',
  重固镇社区文化活动中心: '青浦区',
  华新镇文化体育服务中心: '青浦区',
  '凤溪社区文化体育服务中心（凤溪分中心）': '青浦区',
  赵巷镇社区文化活动中心: '青浦区',
  赵巷镇新城一站大居社区文化体育服务中心: '青浦区',
  金泽镇社区文化活动中心: '青浦区',
  金泽镇社区文化活动服务中心商榻分中心: '青浦区',
  盈浦街道社区文化活动中心: '青浦区',
  夏阳街道社区文化活动中心: '青浦区',
  香花桥街道社区文化活动中心: '青浦区',
  '香花桥街道清河湾U365党群服务中心（社区文化活动分中心）': '奉贤区',
  金汇镇社区文化活动中心: '奉贤区',
  金汇镇社区文化活动中心泰日分中心: '奉贤区',
  徐里桥社区文化活动中心: '奉贤区',
  青村镇社区文化活动中心: '奉贤区',
  青村镇社区文化活动中心钱桥分中心: '奉贤区',
  柘林镇社区文化活动中心: '奉贤区',
  庄行镇社区文化活动中心: '奉贤区',
  '庄行镇社区文化活动中心（邬桥分中心）': '奉贤区',
  四团镇社区文化活动中心: '奉贤区',
  海湾镇社区文化活动中心: '奉贤区',
  奉城镇社区文化活动中心: '奉贤区',
  金海街道社区文化活动中心: '奉贤区',
  海湾旅游区社区文化活动中心: '奉贤区',
  奉浦街道社区文化活动中心: '奉贤区',
  西渡街道社区文化活动中心: '奉贤区',
  头桥街道社区文化活动中心: '奉贤区',
  竖新镇社区文化活动中心: '崇明区',
  横沙乡社区党群服务中心: '崇明区',
  建设镇社区党群服务中心: '崇明区',
  堡镇社区文化活动中心: '崇明区',
  港西镇社区党群服务中心: '崇明区',
  港沿镇社区党群服务中心: '崇明区',
  东平镇社区文化活动中心: '崇明区',
  绿华镇社区文化活动中心: '崇明区',
  新海镇社区文化活动中心: '崇明区',
  新村乡社区党群服务中心: '崇明区',
  新河镇社区党群服务中心: '崇明区',
  中兴镇社区文化活动中心: '崇明区',
  三星镇社区文化活动中心: '崇明区',
  '城桥镇社区党群服务中心 （城桥镇文体服务中心）': '崇明区',
  庙镇社区文化活动中心: '崇明区',
  陈家镇社区文化活动中心: '崇明区',
  长兴镇社区党群服务中心: '崇明区',
  向化镇社区文化活动中心: '崇明区',
  上海黄浦剧场有限公司: '黄浦',
  '上海黄浦剧场有限公司（小剧场）': '黄浦',
  上海木偶剧团有限公司: '黄浦',
  '上海木偶剧团有限公司（小剧场）': '黄浦',
  上海新光影艺苑有限公司: '黄浦',
  上海共舞台有限公司: '黄浦',
  上海中国大戏院有限公司: '黄浦',
  上海市卢湾体育中心: '黄浦',
  '上海儿童国际文化发展有限公司（上海儿童艺术剧场-黑匣子剧场）': '黄浦',
  '上海儿童国际文化发展有限公司（上海儿童艺术剧场-中心剧场）': '黄浦',
  '上海儿童国际文化发展有限公司（上海儿童艺术剧场-小剧场）': '黄浦',
  上海大剧院-大剧场: '黄浦',
  上海大剧院-中剧场: '黄浦',
  上海大剧院-小剧场: '黄浦',
  上海音乐厅小剧场: '黄浦',
  上海天蟾逸夫舞台: '黄浦',
  上海兰心大戏院: '黄浦',
  上海人民大舞台: '黄浦',
  上海文化广场剧院管理有限公司: '黄浦',
  '上海市黄浦区文化馆（上海市雅庐书场）-白玉兰剧场': '黄浦',
  '上海市黄浦区文化馆（上海市雅庐书场）-雅庐书场': '黄浦',
  '上海长江剧场（红匣子）': '黄浦',
  '上海长江剧场（黑匣子）': '黄浦',
  上海豫尚文化传播有限公司: '黄浦',
  '上海话剧艺术中心有限公司黄浦分公司（茉莉花剧场）': '黄浦',
  上海八佰秀企业管理有限公司: '静安',
  上展中心剧院: '静安',
  上海小伙伴剧场: '静安',
  上海尚演文化投资管理有限公司: '静安',
  上海戏剧学院: '静安',
  文艺会堂: '静安',
  '兰馨影业有限公司-光影车间.静剧场': '静安',
  '中国福利会儿童艺术剧院(马兰花剧场)': '静安',
  静安体育中心: '静安',
  上戏实验剧院: '静安',
  云峰剧院: '静安',
  上海美琪大戏院: '静安',
  上海马戏城有限公司: '静安',
  上海商城有限公司: '静安',
  '上海市闸北区宋园茶艺馆（书场）': '静安',
  海上文化管理中心-大宁剧院: '静安',
  上海铁路工人文化宫: '静安',
  上海市沪北电影院有限责任公司: '静安',
  上海艺海剧场: '静安',
  上海话剧艺术中心-艺术剧院: '徐汇',
  上海话剧艺术中心-戏剧沙龙: '徐汇',
  上海话剧艺术中心-D6空间: '徐汇',
  上海大戏院: '徐汇',
  上海交响乐团音乐厅: '徐汇',
  徐汇区田林街道社区文化活动中心: '徐汇',
  上音歌剧院: '徐汇',
  上海东亚体育文化中心有限公司: '徐汇',
  上海大舞台: '徐汇',
  上海表坊文化发展有限公司-上剧场: '徐汇',
  上海市宛平艺苑: '徐汇',
  虹口足球场: '虹口',
  上海摩登嘉旋文化发展有限公司: '虹口',
  虹口区曲阳文化馆: '虹口',
  '1933微剧场': '虹口',
  虹口区工人文化宫: '虹口',
  上海丝芭文化传媒有限公司-星梦剧场: '虹口',
  精武体育馆: '虹口',
  上海泛景文化传播有限公司-珍珠剧场: '虹口',
  上海盈寰文化传媒有限公司-BlueNote: '虹口',
  上海虹口保利大剧院管理有限公司-北外滩友邦大剧院: '虹口',
  上海市长宁民俗文化中心: '长宁',
  上海市长宁文化艺术中心: '长宁',
  上海国际舞蹈中心剧场经营管理有限公司: '长宁',
  上海东虹桥剧院管理有限公司: '长宁',
  江川剧场: '闵行',
  上海新东苑实业有限公司: '闵行',
  新浦江影剧院: '闵行',
  旗忠森林体育城: '闵行',
  吴泾文化馆: '闵行',
  上海城市剧院管理有限公司: '闵行',
  上海零聚演出经纪有限公司: '闵行',
  '索石文化传播（上海）有限公司': '闵行',
  上海零湾美琪剧院管理有限公司: '闵行',
  上海市青浦区文化馆: '青浦',
  青浦区赵巷镇文化中心站: '青浦',
  青浦重固影剧院: '青浦',
  青浦朱家角影剧院: '青浦',
  练塘影剧院: '青浦',
  上海虹馆文化发展有限公司: '青浦',
  上海释乐文化传播有限公司: '青浦',
  上海市优演剧场管理有限公司: '青浦',
  '青隐（上海）文化艺术发展有限公司': '青浦',
  上海乐演优你科技有限公司: '青浦',
  YOUNG剧场-大剧院: '杨浦',
  YOUNG剧场-小剧院: '杨浦',
  东宫剧院: '杨浦',
  上海国际时尚中心园区管理有限公司: '杨浦',
  梅赛德斯-奔驰文化中心: '浦东',
  梅赛德斯-奔驰文化中心-音乐俱乐部: '浦东',
  南汇海东影剧院: '浦东',
  上海南汇周浦影剧场: '浦东',
  南汇宣桥镇影剧院: '浦东',
  上海艺晟文化传播有限公司: '浦东',
  上海浦东新区三墩影剧院: '浦东',
  上海浦东新区川沙影剧院: '浦东',
  南汇盐仓影剧院: '浦东',
  上海浦东新区东方电影院有限公司: '浦东',
  上海市浦东新区航头镇书场茶馆: '浦东',
  南汇三灶影剧院: '浦东',
  上海市南汇大团镇永春演艺厅: '浦东',
  上海市南汇航头镇陶园春演艺厅: '浦东',
  上海尚银东艺数字影城管理有限公司: '浦东',
  上海兰馨影业有限公司: '浦东',
  上海市澧溪文化艺术有限公司: '浦东',
  上海野生动物园发展有限公司: '浦东',
  上海证大喜马拉雅演艺有限公司: '浦东',
  '保利尚悦湾（上海）剧院管理有限公司1862时尚艺术中心': '浦东',
  上海东方艺术中心管理有限公司-音乐厅: '浦东',
  上海东方艺术中心管理有限公司-歌剧厅: '浦东',
  上海东方艺术中心管理有限公司-演奏厅: '浦东',
  上海笋馨文化传媒有限公司: '浦东',
  上海冉旭文化娱乐中心: '浦东',
  上海张江文化控股有限公司-张江戏剧谷: '浦东',
  '上海世博中心有限公司(红厅）': '浦东',
  迪士尼-大剧院: '浦东',
  '迪士尼-凡迭戈剧院、林间剧场、故事舞台': '浦东',
  上海浦东新区三林影剧院: '浦东',
  上海宋城世博演艺发展有限公司-千古情: '浦东',
  上海宋城世博演艺发展有限公司-百乐门: '浦东',
  上海外高桥文化传播有限公司: '浦东',
  '信德前滩（上海）文化置业有限公司': '浦东',
  上海乐来乐好剧院管理有限公司: '普陀',
  上海市奉贤区机关服务中心: '奉贤',
  上海邬桥牡丹影剧院: '奉贤',
  奉贤区南桥影剧院: '奉贤',
  上海胡桥影剧院: '奉贤',
  上海柘林影剧院: '奉贤',
  上海奉贤钱桥影剧院: '奉贤',
  奉贤县青村文化站: '奉贤',
  '上海九棵树文化传媒有限公司—大剧场': '奉贤',
  '上海九棵树文化传媒有限公司—小剧场': '奉贤',
  '上海九棵树文化传媒有限公司—实验剧场': '奉贤',
  '上海九棵树文化传媒有限公司—森林剧场': '奉贤',
  '上海九棵树文化传媒有限公司—水岸舞台': '奉贤',
  依弘剧场: '宝山',
  上海星轶思达爱斯影院管理有限公司: '宝山',
  上海保利大剧院: '嘉定',
  嘉定影剧院有限责任公司: '嘉定',
  开心麻花剧场: '嘉定',
  上海市崇明影剧院: '崇明',
  崇明县沪剧团: '崇明',
  上海风瀛洲文化传播有限公司: '崇明',
  海昌海洋公园-欢乐剧场: '临港',
  海昌海洋公园-海豚表演场: '临港',
  海昌海洋公园-大型动物表演场: '临港',
  泥城影剧院: '临港',
  万祥影剧院: '临港',
  '上海聆海美琪文化艺术发展有限公司（临港演艺中心）': '临港',
  '上海展博置业有限公司（滴水湖剧院）': '临港',
  上海保利云间剧院管理有限公司: '松江',
  '武汉市群众艺术馆（武汉市非物质文化遗产保护中心）': '江岸区',
  武汉中共中央机关旧址纪念馆: '江岸区',
  武汉汉剧院: '江汉区',
  '武汉博物馆（武汉市文物交流中心）': '江汉区',
  八七会议会址纪念馆: '江岸区',
  '八路军武汉办事处旧址纪念馆（汉口新四军军部旧址纪念馆）': '江岸区',
  '武汉京剧院有限责任公司(武汉京剧院)': '江汉区',
  汉阳陵博物馆: '咸阳市渭城区',
  西安半坡博物馆: '灞桥区',
  西安大唐西市博物馆: '莲湖区',
  西安事变纪念馆: '碑林区',
  八路军西安办事处纪念馆: '新城区',
  西安唐皇城墙含光门遗址博物馆: '曲江新区',
  临潼区博物馆: '临潼区',
  西安中国书法艺术博物馆: '曲江新区',
  '汉长安城遗址长乐宫四、五号遗址陈列馆': '未央区',
  丰镐遗址车马坑陈列馆: '长安区',
  华清池唐华清宫御汤遗址博物馆: '临潼区',
  西安市长安区杜甫纪念馆: '长安区',
  西安市长安民居博物馆: '长安区',
  西安市临潼区扁鹊纪念馆: '临潼区',
  仙游寺博物馆: '周至县',
  蓝田县蔡文姬纪念馆: '蓝田县',
  周至博物馆: '周至县',
  葛牌镇区苏维埃政府纪念馆: '蓝田县',
  陕西科学技术馆: '新城区',
  高陵区博物馆: '高陵区',
  汉长安城遗址陈列馆: '未央区',
  西北大学博物馆: '碑林区',
  陕西师范大学博物馆: '长安区',
  西安建筑科技大学校史馆: '碑林区',
  西安建筑科技大学贾平凹文学艺术馆: '碑林区',
  西安市长安博物馆: '长安区',
  长安大学地质博物馆: '雁塔区',
  西安市秦阿房宫遗址博物馆: '长安区',
  西安关中民俗艺术博物院: '长安区',
  西安经文牛文化陶瓷博物馆: '未央区',
  陕西元阳文化博物馆: '碑林区',
  西安大明宫陶瓷艺术博物馆: '曲江新区',
  陕西体育博物馆: '雁塔区',
  西安海棠职业学院中医美容博物馆: '灞桥区',
  西安工程大学纺织服装博物馆: '临潼区',
  秦二世陵遗址博物馆: '曲江新区',
  陕西汉唐石刻博物馆: '沣东新城',
  西安皇家艺术博物馆: '未央区',
  陕西亮宝楼艺术博物馆: '雁塔区',
  西安美都博物馆: '未央区',
  西安秦砖汉瓦博物馆: '曲江新区',
  西安于右任书法艺术博物馆: '莲湖区',
  陕西万达博物院: '雁塔区',
  蓝田水陆庵壁塑博物馆: '蓝田县',
  陕西唐三彩艺术博物馆: '碑林区',
  西安户邑民间艺术博物馆: '曲江新区',
  西安曲江艺术博物馆: '曲江新区',
  西安曲江富陶国际陶艺博物馆: '曲江新区',
  西安毛泽东敬览馆: '雁塔区',
  西安于右任故居纪念馆: '碑林区',
  西安雪花啤酒博物馆: '经开区',
  西安源浩华藏博物馆: '曲江新区',
  西安健康博物馆: '雁塔区',
  西安唐都新碑林艺术博物馆: '曲江新区',
  西安大华博物馆: '曲江新区',
  西安锦业美术博物馆: '高新区',
  西安曲江大玉坊博物馆: '临潼区',
  西安柴窑文化博物馆: '曲江新区',
  大明宫国家遗址公园考古探索中心: '新城区',
  大明宫国家遗址公园丹凤门遗址博物馆: '新城区',
  西安高陵钱币博物馆: '高陵区',
  西安高陵奇石博物馆: '高陵区',
  高陵祥顺博物馆: '高陵区',
  蓝田猿人遗址博物馆: '蓝田县',
  陕西钱币博物馆: '雁塔区',
  临潼区鸿门宴博物馆: '临潼区',
  西安市青龙寺遗址博物馆: '雁塔区',
  空军军医大学口腔医学博物馆: '新城区',
  西安交通大学博物馆: '碑林区',
  高陵区防震减灾科普馆: '高陵区',
  西安浐灞生态区城建博物馆: '浐灞生态区',
  汪锋故居纪念馆: '蓝田县',
  西安市高家大院古典服饰博物馆: '莲湖区',
  西安市新美域和镜博物馆: '碑林区',
  西安市曲江红色记忆博物馆: '雁塔区',
  西安市大唐青铜镜博物馆: '高新区',
  西安市雅观陶瓷艺术博物馆: '未央区',
  西安市非物质文化遗产博物馆: '碑林区',
  西安美术学院美术博物馆: '雁塔区',
  西安市贾平凹文学艺术博物馆: '曲江新区',
  起良蔡侯纸博物馆: '高新区',
  西安市蓝田玉文化博物馆: '蓝田县',
  西安市水墨长安艺术博物馆: '灞桥区',
  西安市荞麦园美术博物馆: '雁塔区',
  西安市曲江丝路遗珍博物馆: '曲江新区',
  西安市明清皮影艺术博物馆: '雁塔区',
  长安大学公路交通博物馆: '未央区',
  西安音乐学院艺术博物馆: '雁塔区',
  西安汉风水务博物馆: '未央区',
  西安市城市记忆博物馆: '新城区',
  西安市圣普美术博物馆: '曲江新区',
  陕西明善博物馆: '秦都区',
  秦咸阳宫遗址博物馆: '渭城区',
  唐华清宫梨园遗址博物馆: '临潼区',
  秦都区沙河古桥遗址博物馆: '秦都区',
  楼增良红木雕刻艺术博物馆: '空港新城',
  西安市曲江第二小学儿童博物馆: '雁塔区',
  西安建筑科技大学中国音乐史博物馆: '碑林区',
  西安市中国古琴博物馆: '沣东新城',
  西安市新梦想影业博物馆: '雁塔区',
  西安市新源民俗艺术博物馆: '高陵区',
  西安市德江陶瓷模范标本博物馆: '灞桥区',
  西安市团结民俗博物馆: '未央区',
  西安市惟德玉文化博物馆: '沣东新城',
  交大西迁博物馆: '碑林区',
  西安红色体育博物馆: '经开区',
  陕西科技大学中国轻工业博物馆: '未央区',
  西安交通大学附属中学博物馆: '雁塔区',
  西安市高陵区西北人民革命大学旧址博物馆: '高陵区',
  西安市吉兆春皮肤医药博物馆: '高陵区',
  西安市太乙面食文化博物馆: '长安区',
  军用航空科技博物馆: '灞桥区',
  西安市城市影像博物馆: '雁塔区',
  西安市石仟佛造像艺术博物馆: '曲江新区',
  西安市古陶瓷博物馆: '灞桥区',
  西安市羊文化博物馆: '雁塔区',
  西安市太和医室博物馆: '碑林区',
  西安市瑛煌关中婚俗文化博物馆: '鄠邑区',
  西安市云之翼航空博物馆: '高新区',
  西安市和璞玉文化博物馆: '长安区',
  西安市沣峪口老油坊博物馆: '长安区',
  西影电影博物馆: '雁塔区',
  西安市黄土画派博物馆: '碑林区',
  西安市民俗博物馆: '新城区',
  西安市鄠邑区非物质文化遗产博物馆: '鄠邑区',
  '临潼区文物管理委员会办公室（区文物稽查队）': '临潼区',
  姜寨遗址文物管理所: '临潼区',
  康家白家遗址文物管理所: '临潼区',
  区博物馆: '临潼区',
  扁鹊纪念馆: '临潼区',
  鸿门宴博物馆: '临潼区',
  秦东陵文物管理所: '临潼区',
  西段遗址文物管理所: '临潼区',
  古遗址: '汉 西咸新区',
  '（张学良将军公馆': '西安市碑林',
  西安事变指挥部: '西安市新城',
  新城黄楼: '西安市新城',
  西京招待所: '西安市新城',
  杨虎城将军纪念馆: '西安市莲湖',
  高桂滋公馆: '西安市碑林',
  '华清池五间厅）': '西安市临潼',
  五星街天主教堂: '西安市莲湖',
  西安和平电影院: '西安市莲湖',
  北院门144号民居: '西安市莲湖',
  西安人民剧院: '西安市莲湖',
  大皮院清真寺: '西安市莲湖',
  西安市广仁寺: '西安市莲湖',
  小皮院清真寺: '西安市莲湖',
  '雷神庙·万阁楼': '西安市莲湖',
  化觉巷232号: '西安市莲湖',
  小学习巷营里寺: '西安市莲湖',
  北广济街清真寺: '西安市莲湖',
  原市长楼: '西安市莲湖',
  原市政府礼堂: '西安市莲湖',
  西五台: '西安市莲湖',
  大麦市街38号民居: '西安市莲湖',
  '西安高家大院古典 服饰博物馆': '西安市莲湖',
  '西安于右任书法 艺术博物馆': '西安市莲湖',
  '陕建集团总公司 办公楼': '西安市莲湖',
  任家庄门楼: '西安市莲湖',
  '西安市鄠邑区文物管理所 （西安市鄠邑区钟楼博物馆）': '西安市鄠邑',
  西安市华夏匾额博物馆: '西安市鄠邑',
  西安市鄠邑区公输堂小木作艺术博物馆: '西安市鄠邑',
  临潼区文化馆: '临潼区',
  临潼区图书馆秦陵社区分馆: '临潼区',
  临潼区图书馆骊阅分馆: '临潼区',
  红25军军部旧址: '蓝田县',
  '秦始皇陵（部分）': '临潼区',
  '华清宫遗址（部分）': '临潼区',
  西安事变旧址-华清池五间厅: '临潼区',
  '秦东陵（部分）': '临潼区',
  五凤遗址: '鄠邑区',
  天池寺塔: '长安区',
  清华山石窟: '长安区',
  楼观台: '周至县',
  老子墓: '周至县',
  宗圣宫遗址: '周至县',
  傥骆道遗址周至段: '周至县',
  佛坪厅故城: '周至县',
  泥峪石门遗址: '周至县',
  王氏宗祠: '周至县',
  化羊庙: '高新区',
  草堂寺: '高新区',
  鼎湖延寿宫遗址: '蓝田县',
  汤峪栈道遗址: '蓝田县',
  锡水洞遗址: '蓝田县',
  葛牌革命旧址: '蓝田县',
  汪锋故居及墓园: '蓝田县',
  香洲区图书馆: '香洲区',
  香洲区博物馆: '香洲区',
  珠海市盛宝博物馆: '香洲区',
  珠海汉东博物馆: '香洲区',
  珠海钰海博物馆: '香洲区',
  珠海市普济艺术博物馆: '香洲区',
  罗西尼钟表博物馆: '高新区',
  珠海市原道文化博物馆: '横琴新区',
  横琴粤澳深度合作区富华紫檀博物馆: '横琴新区',
  珠海市古元美术馆: '香洲区',
  斗门区体育馆: '斗门区',
  斗门体育馆: '斗门区',
  斗门全民健身中心: '斗门区',
  金湾全民健身广场: '金湾区',
  横琴镇全民健身广场: '横琴新区',
  唐家湾镇全民健身广场: '高新区',
  南水镇全民健身广场: '高栏港区',
  平沙镇全民健身广场: '高栏港区',
  桂山镇全民健身广场: '万山区',
  担杆镇全民健身广场: '万山区',
  '万山镇全民健身广场（大万山岛）': '万山区',
  '万山镇全民健身广场（东澳岛）': '万山区'
};

// 区县关键字兜底（自动生成，按长度降序）
const districtKeywords = [
  ['北京经济技术开发区', '北京经济技术开发区'],
  ['万盛经济技术开发区', '万盛经济技术开发区'],
  ['鸿恩寺馆:重庆市', '鸿恩寺馆:重庆市'],
  ['城万旧址：城口县', '城万旧址：城口县'],
  ['怀柔区，东城区', '怀柔区，东城区'],
  ['奥体中心体育场', '奥体中心体育场'],
  ['深汕特别合作区', '深汕特别合作区'],
  ['咸阳市渭城区', '咸阳市渭城区'],
  ['汉 西咸新区', '汉 西咸新区'],
  ['A馆:重庆市', 'A馆:重庆市'],
  ['大田湾体育场', '大田湾体育场'],
  ['浐灞生态区', '浐灞生态区'],
  ['西安市临潼', '西安市临潼'],
  ['西安市莲湖', '西安市莲湖'],
  ['西安市鄠邑', '西安市鄠邑'],
  ['酉阳自治县', '酉阳自治县'],
  ['西安市新城', '西安市新城'],
  ['西安市碑林', '西安市碑林'],
  ['万盛经开区', '万盛经开区'],
  ['两江新区', '两江新区'],
  ['空港新城', '空港新城'],
  ['市体育馆', '市体育馆'],
  ['横琴新区', '横琴新区'],
  ['门头沟区', '门头沟区'],
  ['东西湖区', '东西湖区'],
  ['龙泉驿区', '龙泉驿区'],
  ['高栏港区', '高栏港区'],
  ['沙坪坝区', '沙坪坝区'],
  ['大鹏新区', '大鹏新区'],
  ['雨花台区', '雨花台区'],
  ['曲江新区', '曲江新区'],
  ['大渡口区', '大渡口区'],
  ['天府新区', '天府新区'],
  ['都江堰市', '都江堰市'],
  ['燕山地区', '燕山地区'],
  ['浦东新区', '浦东新区'],
  ['沣东新城', '沣东新城'],
  ['石景山区', '石景山区'],
  ['九龙坡区', '九龙坡区'],
  ['新都区', '新都区'],
  ['六合区', '六合区'],
  ['滨江区', '滨江区'],
  ['高新区', '高新区'],
  ['秦都区', '秦都区'],
  ['青浦区', '青浦区'],
  ['巫山县', '巫山县'],
  ['新洲区', '新洲区'],
  ['延庆区', '延庆区'],
  ['虹口区', '虹口区'],
  ['雁塔区', '雁塔区'],
  ['荣昌区', '荣昌区'],
  ['开州区', '开州区'],
  ['南沙区', '南沙区'],
  ['江宁区', '江宁区'],
  ['长安区', '长安区'],
  ['普陀区', '普陀区'],
  ['临潼区', '临潼区'],
  ['罗湖区', '罗湖区'],
  ['青山区', '青山区'],
  ['东城区', '东城区'],
  ['长寿区', '长寿区'],
  ['龙岗区', '龙岗区'],
  ['铜梁区', '铜梁区'],
  ['金牛区', '金牛区'],
  ['宝山区', '宝山区'],
  ['黄陂区', '黄陂区'],
  ['大邑县', '大邑县'],
  ['南岸区', '南岸区'],
  ['坪山区', '坪山区'],
  ['白云区', '白云区'],
  ['云阳县', '云阳县'],
  ['通州区', '通州区'],
  ['余杭区', '余杭区'],
  ['荔湾区', '荔湾区'],
  ['丰都县', '丰都县'],
  ['渝中区', '渝中区'],
  ['垫江县', '垫江县'],
  ['江岸区', '江岸区'],
  ['蔡甸区', '蔡甸区'],
  ['崇州市', '崇州市'],
  ['上海市', '上海市'],
  ['江津区', '江津区'],
  ['上城区', '上城区'],
  ['徐汇区', '徐汇区'],
  ['越秀区', '越秀区'],
  ['青羊区', '青羊区'],
  ['浦口区', '浦口区'],
  ['长宁区', '长宁区'],
  ['新城区', '新城区'],
  ['大足区', '大足区'],
  ['丰台区', '丰台区'],
  ['永川区', '永川区'],
  ['成华区', '成华区'],
  ['未央区', '未央区'],
  ['金湾区', '金湾区'],
  ['涪陵区', '涪陵区'],
  ['海淀区', '海淀区'],
  ['周至县', '周至县'],
  ['秀山县', '秀山县'],
  ['南川区', '南川区'],
  ['顺义区', '顺义区'],
  ['彭州市', '彭州市'],
  ['萧山区', '萧山区'],
  ['龙华区', '龙华区'],
  ['阎良区', '阎良区'],
  ['潼南区', '潼南区'],
  ['灞桥区', '灞桥区'],
  ['番禺区', '番禺区'],
  ['莲湖区', '莲湖区'],
  ['杨浦区', '杨浦区'],
  ['江北区', '江北区'],
  ['栖霞区', '栖霞区'],
  ['温江区', '温江区'],
  ['金山区', '金山区'],
  ['经开区', '经开区'],
  ['怀柔区', '怀柔区'],
  ['渝北区', '渝北区'],
  ['万山区', '万山区'],
  ['西城区', '西城区'],
  ['万州区', '万州区'],
  ['天河区', '天河区'],
  ['高淳区', '高淳区'],
  ['盐田区', '盐田区'],
  ['建德市', '建德市'],
  ['临平区', '临平区'],
  ['蓝田县', '蓝田县'],
  ['江汉区', '江汉区'],
  ['斗门区', '斗门区'],
  ['桐庐县', '桐庐县'],
  ['奉节县', '奉节县'],
  ['闵行区', '闵行区'],
  ['江夏区', '江夏区'],
  ['北陪区', '北陪区'],
  ['临安区', '临安区'],
  ['鼓楼区', '鼓楼区'],
  ['北碚区', '北碚区'],
  ['武隆区', '武隆区'],
  ['昌平区', '昌平区'],
  ['宝安区', '宝安区'],
  ['锦江区', '锦江区'],
  ['武昌区', '武昌区'],
  ['梁平区', '梁平区'],
  ['下城区', '下城区'],
  ['建邺区', '建邺区'],
  ['富阳区', '富阳区'],
  ['黄浦区', '黄浦区'],
  ['汉阳区', '汉阳区'],
  ['平谷区', '平谷区'],
  ['从化区', '从化区'],
  ['奉贤区', '奉贤区'],
  ['彭水县', '彭水县'],
  ['松江区', '松江区'],
  ['光明区', '光明区'],
  ['香洲区', '香洲区'],
  ['城口县', '城口县'],
  ['璧山区', '璧山区'],
  ['双流区', '双流区'],
  ['黄埔区', '黄埔区'],
  ['南山区', '南山区'],
  ['密云区', '密云区'],
  ['邛崃市', '邛崃市'],
  ['花都区', '花都区'],
  ['拱墅区', '拱墅区'],
  ['綦江区', '綦江区'],
  ['海珠区', '海珠区'],
  ['洪山区', '洪山区'],
  ['巴南区', '巴南区'],
  ['郫都区', '郫都区'],
  ['江干区', '江干区'],
  ['石柱县', '石柱县'],
  ['合川区', '合川区'],
  ['崇明区', '崇明区'],
  ['朝阳区', '朝阳区'],
  ['玄武区', '玄武区'],
  ['高陵区', '高陵区'],
  ['静安区', '静安区'],
  ['房山区', '房山区'],
  ['淳安县', '淳安县'],
  ['碑林区', '碑林区'],
  ['鄠邑区', '鄠邑区'],
  ['巫溪县', '巫溪县'],
  ['福田区', '福田区'],
  ['酉阳县', '酉阳县'],
  ['硚口区', '硚口区'],
  ['西湖区', '西湖区'],
  ['武侯区', '武侯区'],
  ['溧水区', '溧水区'],
  ['增城区', '增城区'],
  ['渭城区', '渭城区'],
  ['秦淮区', '秦淮区'],
  ['嘉定区', '嘉定区'],
  ['黔江区', '黔江区'],
  ['大兴区', '大兴区'],
  ['虹口', '虹口'],
  ['嘉定', '嘉定'],
  ['徐汇', '徐汇'],
  ['静安', '静安'],
  ['黄浦', '黄浦'],
  ['宝山', '宝山'],
  ['杨浦', '杨浦'],
  ['临港', '临港'],
  ['青浦', '青浦'],
  ['松江', '松江'],
  ['浦东', '浦东'],
  ['长宁', '长宁'],
  ['闵行', '闵行'],
  ['奉贤', '奉贤'],
  ['普陀', '普陀'],
  ['崇明', '崇明'],
  ['忠县', '忠县']
];

// 按城市分组场馆（自动生成）
const venuesByCity = {
  shenzhen: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: 'opower',
      name: 'OPOWER文化艺术中心'
    },
    {
      key: 'qns',
      name: '七娘山'
    },
    {
      key: 'baoan',
      name: '上合孝德园'
    },
    {
      key: 'szwt_11153449',
      name: '世纪琥珀博物馆'
    },
    {
      key: 'dchss',
      name: '东涌红树林湿地公园'
    },
    {
      key: 'szwt_11166901',
      name: '中国文化名人大营救纪念馆'
    },
    {
      key: 'lh_printmaking',
      name: '中国版画博物馆'
    },
    {
      key: 'yt_history',
      name: '中英街历史博物馆'
    },
    {
      key: '中轴云廊·顶上空间',
      name: '中轴云廊·顶上空间'
    },
    {
      key: 'szwt_11145432',
      name: '九龙山体育公园'
    },
    {
      key: 'baoan',
      name: '五指耙体育主题公园'
    },
    {
      key: 'szwt_11169233',
      name: '人大附中深圳学校高中部体育场'
    },
    {
      key: 'rcgy',
      name: '人才公园'
    },
    {
      key: 'hxngallery',
      name: '何香凝美术馆'
    },
    {
      key: 'szwt_11128382',
      name: '依波钟表文化博物馆'
    },
    {
      key: '光明区光明街道综合性文化服务中心',
      name: '光明区光明街道综合性文化服务中心'
    },
    {
      key: '光明区公明街道综合性文化服务中心',
      name: '光明区公明街道综合性文化服务中心'
    },
    {
      key: 'gmlib',
      name: '光明区图书馆'
    },
    {
      key: 'szwt_11128370',
      name: '光明区少年儿童图书馆'
    },
    {
      key: 'gmwhg',
      name: '光明区文化馆'
    },
    {
      key: 'gm_kjg',
      name: '光明区科技馆'
    },
    {
      key: 'szwt_12364975',
      name: '光明区红花山体育中心'
    },
    {
      key: 'gmtyzx',
      name: '光明区群众体育中心'
    },
    {
      key: 'gmqsng',
      name: '光明区青少年活动中心'
    },
    {
      key: '光明区马田街道综合性文化服务中心',
      name: '光明区马田街道综合性文化服务中心'
    },
    {
      key: 'szwt_12766454',
      name: '光明国际马术中心'
    },
    {
      key: 'gmarts',
      name: '光明文化艺术中心'
    },
    {
      key: '光明文化艺术中心',
      name: '光明文化艺术中心·演艺中心·大剧院'
    },
    {
      key: '光明文化艺术中心',
      name: '光明文化艺术中心美术馆'
    },
    {
      key: 'gmhbgy',
      name: '光明虹桥公园'
    },
    {
      key: 'gsyart',
      name: '关山月美术馆'
    },
    {
      key: 'szwt_11136104',
      name: '冰纷万象滑雪场'
    },
    {
      key: 'baoan',
      name: '凤凰山人才林公园'
    },
    {
      key: 'fhwh',
      name: '凤凰街道综合性文化服务中心'
    },
    {
      key: 'szwt_11999373',
      name: '北京大学附属中学深圳学校(集团)黄埔学校(小学部)'
    },
    {
      key: 'bzgx',
      name: '北站中心公园'
    },
    {
      key: 'oct_wetland',
      name: '华侨城湿地'
    },
    {
      key: 'szwt_11132724',
      name: '华润大厦艺术中心美术馆'
    },
    {
      key: 'szwt_11132704',
      name: '南头古城博物馆'
    },
    {
      key: 'ntgc',
      name: '南头古城博物馆群'
    },
    {
      key: 'nssxf',
      name: '南山书房'
    },
    {
      key: 'szwt_11644501',
      name: '南山区天后博物馆'
    },
    {
      key: 'nswhg',
      name: '南山区文化馆'
    },
    {
      key: 'nsqsng',
      name: '南山区青少年活动中心'
    },
    {
      key: 'nsmuseum',
      name: '南山博物馆'
    },
    {
      key: '南山博物馆',
      name: '南山博物馆一层一号专题展厅'
    },
    {
      key: '南山博物馆',
      name: '南山博物馆一层一号展厅'
    },
    {
      key: '南山博物馆',
      name: '南山博物馆二层三号展厅'
    },
    {
      key: '南山博物馆',
      name: '南山博物馆二层二号展厅'
    },
    {
      key: 'nslib',
      name: '南山图书馆'
    },
    {
      key: 'nsaqjy',
      name: '南山安全教育体验馆'
    },
    {
      key: 'nswtzx',
      name: '南山文体中心'
    },
    {
      key: 'szwt_11131701',
      name: '南海足球公园'
    },
    {
      key: 'nwwtz',
      name: '南湾街道文化站'
    },
    {
      key: 'szwt_11169235',
      name: '南澳中学体育场'
    },
    {
      key: 'szwt_11169234',
      name: '南澳中心小学体育场'
    },
    {
      key: 'jhwtz',
      name: '吉华街道文化站'
    },
    {
      key: '园山街道文化站',
      name: '园山街道文化站'
    },
    {
      key: 'ylwh',
      name: '园岭街道综合性文化服务中心'
    },
    {
      key: '坂田街道文化站',
      name: '坂田街道文化站'
    },
    {
      key: 'bghsl',
      name: '坝光红树林湿地公园'
    },
    {
      key: 'pdwtz',
      name: '坪地街道文化站'
    },
    {
      key: 'psdjng',
      name: '坪山东江纵队纪念馆'
    },
    {
      key: 'pszxgy',
      name: '坪山中心公园'
    },
    {
      key: 'pstyzx',
      name: '坪山体育中心'
    },
    {
      key: 'szwt_11170203',
      name: '坪山儿童公园分馆'
    },
    {
      key: 'pslib',
      name: '坪山区图书馆'
    },
    {
      key: 'pskjg',
      name: '坪山区科技馆'
    },
    {
      key: 'psqsng',
      name: '坪山区青少年宫'
    },
    {
      key: 'szwt_11170204',
      name: '坪山图书馆·客家特藏馆'
    },
    {
      key: 'psthtr',
      name: '坪山大剧院'
    },
    {
      key: 'psart',
      name: '坪山美术馆'
    },
    {
      key: 'dp_nuclear',
      name: '大亚湾核能科技馆'
    },
    {
      key: 'baoan',
      name: '大仟里未来书屋'
    },
    {
      key: 'szwt_11129790',
      name: '大沙河公园体育中心'
    },
    {
      key: 'dshslc',
      name: '大沙河生态长廊'
    },
    {
      key: '大浪街道综合文化服务中心',
      name: '大浪街道综合文化服务中心'
    },
    {
      key: 'dzxgy',
      name: '大运中心公园'
    },
    {
      key: '大鹏办事处公共事业服务中心',
      name: '大鹏办事处公共事业服务中心'
    },
    {
      key: 'dpgcbwg',
      name: '大鹏古城博物馆'
    },
    {
      key: 'dpgeopark',
      name: '大鹏地质公园博物馆'
    },
    {
      key: 'szwt_11171158',
      name: '大鹏新区博物馆'
    },
    {
      key: 'dplib',
      name: '大鹏新区图书馆'
    },
    {
      key: 'dpwhg',
      name: '大鹏新区文化馆'
    },
    {
      key: 'dpkjg',
      name: '大鹏新区科学馆'
    },
    {
      key: 'szwt_11133787',
      name: '大鹏新区葵涌中心小学'
    },
    {
      key: 'szwt_11168742',
      name: '大鹏第二小学体育场'
    },
    {
      key: 'jcw',
      name: '大鹏较场尾沙滩'
    },
    {
      key: 'atszx',
      name: '安托山公共文化中心'
    },
    {
      key: 'ghysq',
      name: '官湖村艺象艺术区'
    },
    {
      key: 'baoan_1990',
      name: '宝安1990文化馆'
    },
    {
      key: 'baoan',
      name: '宝安1990文化馆（区文化馆总馆）'
    },
    {
      key: 'baoan_ty',
      name: '宝安体育中心'
    },
    {
      key: 'szwt_11117343',
      name: '宝安体育场'
    },
    {
      key: 'szwt_11117344',
      name: '宝安体育馆'
    },
    {
      key: 'baoan',
      name: '宝安公园（醒狮乐园）'
    },
    {
      key: 'bamuseum',
      name: '宝安区博物馆'
    },
    {
      key: 'baoan',
      name: '宝安区图书馆（总馆）'
    },
    {
      key: 'baoan',
      name: '宝安区城市规划展览馆'
    },
    {
      key: '宝安区文化馆',
      name: '宝安区文化馆'
    },
    {
      key: '宝安区文化馆新桥街道分馆',
      name: '宝安区文化馆新桥街道分馆'
    },
    {
      key: '宝安区文化馆燕罗分馆',
      name: '宝安区文化馆燕罗街道分馆'
    },
    {
      key: 'baoan_qsng',
      name: '宝安区青少年宫'
    },
    {
      key: 'baoan',
      name: '宝安区青少年宫（滨海）'
    },
    {
      key: 'baoan',
      name: '宝安博物馆'
    },
    {
      key: 'balib',
      name: '宝安图书馆'
    },
    {
      key: 'baoan',
      name: '宝安图书馆西乡街道分馆'
    },
    {
      key: 'baoan_guihua',
      name: '宝安城市规划展览馆'
    },
    {
      key: 'szwt_11117342',
      name: '宝安游泳场馆'
    },
    {
      key: 'baoan_kjg',
      name: '宝安科技馆'
    },
    {
      key: 'baoan',
      name: '宝安美术馆'
    },
    {
      key: 'baoan',
      name: '宝民社区阅读中心'
    },
    {
      key: 'baoan',
      name: '宝读书房·旭书店'
    },
    {
      key: 'szwt_12490550',
      name: '宝龙文体中心'
    },
    {
      key: 'szwt_11128585',
      name: '惜物博物馆'
    },
    {
      key: 'zsjbwg',
      name: '招商局历史博物馆'
    },
    {
      key: 'baoan',
      name: '新安中洲分馆'
    },
    {
      key: 'baoan',
      name: '新安公园'
    },
    {
      key: 'baoan',
      name: '新安街道分馆'
    },
    {
      key: 'baoan',
      name: '新桥市民广场'
    },
    {
      key: 'baoan',
      name: '新桥街道图书馆分馆'
    },
    {
      key: 'szwt_11133687',
      name: '景鹏小学'
    },
    {
      key: 'ymk',
      name: '杨梅坑'
    },
    {
      key: 'baoan',
      name: '松岗公园'
    },
    {
      key: 'baoan',
      name: '松岗琥珀博物馆（公益展厅）'
    },
    {
      key: 'baoan',
      name: '松岗街道图书馆分馆'
    },
    {
      key: 'szwt_11129883',
      name: '桃源群众篮球网球体育公园'
    },
    {
      key: 'tywh',
      name: '桃源街道综合性文化服务中心'
    },
    {
      key: 'baoan',
      name: '桥头公园'
    },
    {
      key: 'szwt_12502724',
      name: '横岗文体中心'
    },
    {
      key: '横岗街道文化站',
      name: '横岗街道文化站'
    },
    {
      key: 'hlgw',
      name: '欢乐港湾'
    },
    {
      key: 'szwt_11197294',
      name: '民治体育公园'
    },
    {
      key: 'jlwh',
      name: '江岭社区公共文化服务中心'
    },
    {
      key: 'baoan',
      name: '沙井市民广场'
    },
    {
      key: 'baoan',
      name: '沙井蚝文化博物馆'
    },
    {
      key: 'baoan',
      name: '沙井街道图书馆分馆'
    },
    {
      key: 'szwt_11151909',
      name: '沙头角体育馆'
    },
    {
      key: 'hhgy',
      name: '洪湖公园'
    },
    {
      key: 'hssjwh',
      name: '海上世界文化艺术中心'
    },
    {
      key: 'tjsgd',
      name: '淘金山绿道'
    },
    {
      key: 'szwt_12374186',
      name: '深圳·红立方'
    },
    {
      key: 'szworld',
      name: '深圳世界之窗'
    },
    {
      key: 'szzybwg',
      name: '深圳中医药博物馆'
    },
    {
      key: 'szwt_11128645',
      name: '深圳中山公园棒球场'
    },
    {
      key: 'szbook',
      name: '深圳书城'
    },
    {
      key: 'szcec',
      name: '深圳会展中心'
    },
    {
      key: 'polytheatre',
      name: '深圳保利剧院'
    },
    {
      key: 'szwt_11129404',
      name: '深圳南山文体中心剧院聚橙剧院'
    },
    {
      key: 'szmuseum',
      name: '深圳博物馆'
    },
    {
      key: '深圳博物馆官网',
      name: '深圳博物馆（历史民俗馆）'
    },
    {
      key: '深圳博物馆官网',
      name: '深圳博物馆（古代艺术馆）'
    },
    {
      key: '深圳博物馆官网',
      name: '深圳博物馆（改革开放展览馆）'
    },
    {
      key: 'lh_paleo',
      name: '深圳古生物博物馆'
    },
    {
      key: 'shenzhen_world',
      name: '深圳国际会展中心'
    },
    {
      key: 'szlib',
      name: '深圳图书馆'
    },
    {
      key: '深圳图书馆',
      name: '深圳图书馆 (深圳图书馆中心馆)'
    },
    {
      key: '深圳图书馆',
      name: '深圳图书馆 (深圳图书馆北馆)'
    },
    {
      key: 'szdjy',
      name: '深圳大剧院'
    },
    {
      key: 'dyzx',
      name: '深圳大运中心'
    },
    {
      key: 'sz_children_lib',
      name: '深圳少年儿童图书馆'
    },
    {
      key: 'szwt_12861228',
      name: '深圳市丁全匠作博物馆'
    },
    {
      key: 'szsports',
      name: '深圳市体育中心'
    },
    {
      key: '深圳市体育中心',
      name: '深圳市体育中心体育场'
    },
    {
      key: 'szwt_11114635',
      name: '深圳市坪山区东江纵队纪念馆'
    },
    {
      key: 'szwt_11114636',
      name: '深圳市坪山区图书馆'
    },
    {
      key: 'szwt_11114606',
      name: '深圳市坪山区坪山体育中心体育馆'
    },
    {
      key: 'szwt_12095611',
      name: '深圳市坪山区文化馆'
    },
    {
      key: '深圳市坪山区石井街道公共文化服务中心',
      name: '深圳市坪山区石井街道公共文化服务中心'
    },
    {
      key: 'szwt_11114637',
      name: '深圳市坪山区美术馆'
    },
    {
      key: 'sz_safety',
      name: '深圳市安全教育基地'
    },
    {
      key: 'szcp',
      name: '深圳市少年宫'
    },
    {
      key: 'szwt_11671562',
      name: '深圳市工业展览馆'
    },
    {
      key: 'szmocap',
      name: '深圳市当代艺术与城市规划馆'
    },
    {
      key: 'szmassart',
      name: '深圳市文化馆'
    },
    {
      key: 'szwt_12861227',
      name: '深圳市梵亚艺术博物馆'
    },
    {
      key: 'szwt_12861229',
      name: '深圳市百师园非物质文化遗产博物馆'
    },
    {
      key: 'szwt_11111303',
      name: '深圳市福田区图书馆'
    },
    {
      key: 'szwt_11166908',
      name: '深圳市艺之卉百年时尚博物馆'
    },
    {
      key: 'szwt_12861225',
      name: '深圳市隐秀高尔夫博物馆'
    },
    {
      key: 'szaac',
      name: '深圳市青少年活动中心'
    },
    {
      key: 'szwt_12364970',
      name: '深圳市青少年足球训练基地'
    },
    {
      key: 'szwt_11166909',
      name: '深圳市龙华区美联红木艺术博物馆'
    },
    {
      key: 'szwt_12864963',
      name: '深圳市龙岗区万国珠宝汇矿物博物馆'
    },
    {
      key: 'szwt_12861226',
      name: '深圳市龙岗区东江潮红色文化博物馆（新生主馆）'
    },
    {
      key: 'szwt_11167839',
      name: '深圳市龙岗区体育中心'
    },
    {
      key: 'szwt_12864965',
      name: '深圳市龙岗区怡利翡翠博物馆'
    },
    {
      key: 'szwt_11167080',
      name: '深圳市龙岗区文化馆'
    },
    {
      key: 'szwt_12864964',
      name: '深圳市龙岗区龙岭邮票博物馆'
    },
    {
      key: 'szwt_12490551',
      name: '深圳布吉文体中心'
    },
    {
      key: 'lhtheatre',
      name: '深圳戏院'
    },
    {
      key: 'szwt_11168444',
      name: '深圳望野博物馆'
    },
    {
      key: 'hoha',
      name: '深圳欢乐海岸'
    },
    {
      key: 'hlgj',
      name: '深圳欢乐谷'
    },
    {
      key: 'szwty',
      name: '深圳湾体育中心'
    },
    {
      key: 'szwt_11129527',
      name: '深圳湾体育训练基地'
    },
    {
      key: 'szhbgy',
      name: '深圳湾公园'
    },
    {
      key: 'szbo',
      name: '深圳滨海艺术中心'
    },
    {
      key: 'szjewg',
      name: '深圳珠宝博物馆'
    },
    {
      key: 'kxgny',
      name: '深圳科学公园（南翼）'
    },
    {
      key: 'szstm',
      name: '深圳科学技术馆'
    },
    {
      key: '深圳科学技术馆官网',
      name: '深圳科学技术馆（光明新馆）'
    },
    {
      key: 'szwt_11168520',
      name: '深圳红木家具博物馆'
    },
    {
      key: 'szartm',
      name: '深圳美术馆'
    },
    {
      key: 'sznm',
      name: '深圳自然博物馆'
    },
    {
      key: 'xcart',
      name: '深圳西涌天文台'
    },
    {
      key: 'szconcert',
      name: '深圳音乐厅'
    },
    {
      key: '深圳音乐厅官网',
      name: '深圳音乐厅五楼小剧场'
    },
    {
      key: 'lg_arts',
      name: '深圳龙岗国际艺术中心'
    },
    {
      key: 'szwt_11116977',
      name: '深圳（宝安）劳务工博物馆'
    },
    {
      key: 'szwt_11127123',
      name: '深汕西文体中心'
    },
    {
      key: 'sarc',
      name: '深爱人才馆'
    },
    {
      key: 'baoan',
      name: '清平古墟影视小镇'
    },
    {
      key: 'bayarea_eye',
      name: '湾区之眼'
    },
    {
      key: 'baoan',
      name: '湾区书城（深圳书城湾区城）'
    },
    {
      key: 'szwt_11168745',
      name: '溪涌小学体育场'
    },
    {
      key: 'baoan',
      name: '滨海文化公园（欢乐港湾）'
    },
    {
      key: 'yhzgz',
      name: '燕子湖国际会展中心'
    },
    {
      key: 'baoan',
      name: '燕罗湿地公园'
    },
    {
      key: 'baoan',
      name: '燕罗红色文化纪念馆'
    },
    {
      key: 'baoan',
      name: '燕罗街道图书馆分馆'
    },
    {
      key: 'gmtysq',
      name: '玉塘文体中心'
    },
    {
      key: 'baoan',
      name: '王大中丞祠'
    },
    {
      key: 'mgha',
      name: '玫瑰海岸'
    },
    {
      key: '白花社区综合性文化服务中心',
      name: '白花社区综合性文化服务中心'
    },
    {
      key: 'ytzgy',
      name: '盐田中央公园'
    },
    {
      key: 'yttyzx',
      name: '盐田体育中心'
    },
    {
      key: 'szwt_11151907',
      name: '盐田区体育发展服务中心网球场'
    },
    {
      key: 'ytlib',
      name: '盐田区图书馆'
    },
    {
      key: 'ytwhg',
      name: '盐田区文化馆'
    },
    {
      key: 'szwt_11151908',
      name: '盐田区游泳馆'
    },
    {
      key: 'ytkjg',
      name: '盐田科技馆'
    },
    {
      key: 'sywhzx',
      name: '石岩文化艺术中心'
    },
    {
      key: 'sysgy',
      name: '石岩湖湿地公园'
    },
    {
      key: 'baoan',
      name: '石岩湿地公园'
    },
    {
      key: 'baoan',
      name: '石岩街道图书馆分馆'
    },
    {
      key: 'baoan',
      name: '福永凤凰古村'
    },
    {
      key: 'baoan',
      name: '福永街道图书馆分馆'
    },
    {
      key: 'baoan',
      name: '福永街道安全警示教育基地'
    },
    {
      key: 'baoan',
      name: '福海安全生产警示教育中心'
    },
    {
      key: 'baoan',
      name: '福海河公园'
    },
    {
      key: 'szwt_11111769',
      name: '福田体育公园'
    },
    {
      key: 'ftlib',
      name: '福田区图书馆'
    },
    {
      key: 'ftwhg',
      name: '福田区文化馆'
    },
    {
      key: 'szwt_11111305',
      name: '福田区景田网球中心'
    },
    {
      key: '福田戏剧馆',
      name: '福田戏剧馆'
    },
    {
      key: 'szwt_11485498',
      name: '福田文体中心·戏剧主题馆'
    },
    {
      key: 'szwt_11485494',
      name: '福田文体中心·梦工场'
    },
    {
      key: 'szwt_11485497',
      name: '福田文体中心·舞蹈主题馆'
    },
    {
      key: 'szwt_11485500',
      name: '福田文体中心·非遗主题馆'
    },
    {
      key: 'szwt_11485496',
      name: '福田文体中心·音乐主题馆'
    },
    {
      key: 'szwt_11111306',
      name: '福田海滨生态体育公园'
    },
    {
      key: 'ftart',
      name: '福田美术馆'
    },
    {
      key: '福田音乐馆',
      name: '福田音乐馆'
    },
    {
      key: 'baoan',
      name: '立新湖公园（立新湖儿童乐园）'
    },
    {
      key: 'szwt_11126064',
      name: '简上体育综合体'
    },
    {
      key: 'hhsgy',
      name: '红花山公园'
    },
    {
      key: 'szwt_11117341',
      name: '综合训练馆（室内网球馆）'
    },
    {
      key: 'szwt_12699821',
      name: '罗湖体育休闲公园'
    },
    {
      key: 'szwt_12699929',
      name: '罗湖体育馆'
    },
    {
      key: 'lhlib',
      name: '罗湖区图书馆'
    },
    {
      key: 'lhwhg2',
      name: '罗湖区文化馆'
    },
    {
      key: 'szwt_12699826',
      name: '罗湖网球中心'
    },
    {
      key: 'baoan',
      name: '翻身社区阅读中心'
    },
    {
      key: 'jlsgy',
      name: '聚龙山生态公园'
    },
    {
      key: 'szwt_11116976',
      name: '至美术馆'
    },
    {
      key: 'baoan',
      name: '航城公园'
    },
    {
      key: 'baoan',
      name: '航城街道图书馆分馆'
    },
    {
      key: 'szwt_12364958',
      name: '茅洲河体育艺术中心'
    },
    {
      key: 'baoan',
      name: '茅洲河展示馆'
    },
    {
      key: 'mzohbd',
      name: '茅洲河碧道'
    },
    {
      key: 'szwt_11129884',
      name: '荔香公园网球场'
    },
    {
      key: 'szwt_11111768',
      name: '莲花体育中心'
    },
    {
      key: 'szwt_11169238',
      name: '葵涌中学体育场'
    },
    {
      key: 'szwt_11168743',
      name: '葵涌中心小学体育场'
    },
    {
      key: 'kcsigy',
      name: '葵涌生态公园'
    },
    {
      key: 'szwt_11168746',
      name: '葵涌第二小学体育场'
    },
    {
      key: 'baoan',
      name: '蚝乡湖公园'
    },
    {
      key: 'szwt_11129541',
      name: '蛇口体育中心'
    },
    {
      key: 'szwt_11131232',
      name: '蛇口海上世界文化艺术中心'
    },
    {
      key: 'skhykpg',
      name: '蛇口海洋科普馆'
    },
    {
      key: 'baoan',
      name: '西乡北帝古庙'
    },
    {
      key: 'baoan',
      name: '西湾公园'
    },
    {
      key: 'xwhsl',
      name: '西湾红树林公园'
    },
    {
      key: 'baoan',
      name: '西湾红树林科普馆'
    },
    {
      key: 'jkwh',
      name: '迳口社区综合性文化服务中心'
    },
    {
      key: 'jsgjly',
      name: '金沙湾国际乐园'
    },
    {
      key: 'szwt_11170215',
      name: '金龟自然书房分馆'
    },
    {
      key: 'baoan',
      name: '钓鱼嘴原木亲子乐园'
    },
    {
      key: 'baoan',
      name: '铁仔山公园'
    },
    {
      key: 'szwt_11135809',
      name: '锡才体育公园'
    },
    {
      key: 'theme_park',
      name: '锦绣中华民俗村'
    },
    {
      key: 'szwt_11668510',
      name: '风华大剧院'
    },
    {
      key: 'szwt_11111766',
      name: '香蜜体育中心'
    },
    {
      key: 'mlsgy',
      name: '马峦山郊野公园'
    },
    {
      key: 'szwt_11111767',
      name: '黄木岗网球中心'
    },
    {
      key: 'lhxqlib',
      name: '龙华区图书馆'
    },
    {
      key: 'lhwhg',
      name: '龙华区文化馆'
    },
    {
      key: 'lhkjg',
      name: '龙华区科技馆'
    },
    {
      key: 'lhqsng',
      name: '龙华区青少年宫'
    },
    {
      key: 'szwt_11145352',
      name: '龙华图书馆'
    },
    {
      key: 'lh_ecology',
      name: '龙华生态文明展览馆'
    },
    {
      key: 'lhbljng',
      name: '龙华白石龙纪念馆'
    },
    {
      key: '龙城街道文化站',
      name: '龙城街道文化站'
    },
    {
      key: 'lgtyzx',
      name: '龙岗体育中心'
    },
    {
      key: 'lgpark',
      name: '龙岗儿童公园'
    },
    {
      key: 'lgmuseum',
      name: '龙岗区博物馆'
    },
    {
      key: 'lglib',
      name: '龙岗区图书馆'
    },
    {
      key: 'szwt_12863189',
      name: '龙岗区图书馆少儿馆'
    },
    {
      key: 'lgwhg',
      name: '龙岗区文化馆'
    },
    {
      key: 'lgkjg',
      name: '龙岗区科技馆'
    },
    {
      key: 'lgqsng',
      name: '龙岗区青少年宫'
    },
    {
      key: 'szwt_12865898',
      name: '龙岗国际艺术中心·D+数字艺术馆'
    },
    {
      key: 'szwt_12865897',
      name: '龙岗国际艺术中心·国际演艺中心'
    },
    {
      key: 'lg_hakka',
      name: '龙岗客家民俗博物馆'
    },
    {
      key: 'szwt_11167822',
      name: '龙岗文化中心大剧院'
    },
    {
      key: 'szwt_11167831',
      name: '龙岗文化中心音乐厅'
    },
    {
      key: '龙岗街道文化站',
      name: '龙岗街道文化站'
    }
  ],
  guangzhou: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: '广州本地宝',
      name: '上下九'
    },
    {
      key: '百度百家号（广州科普Citywalk）',
      name: '中国科学院华南植物园'
    },
    {
      key: '广州本地宝',
      name: '云台花园'
    },
    {
      key: '从化区图书馆',
      name: '从化区图书馆'
    },
    {
      key: 'gu_gov_6533838',
      name: '从化博物馆'
    },
    {
      key: '从化温泉旅游度假区',
      name: '从化温泉旅游度假区'
    },
    {
      key: '广州本地宝',
      name: '余荫山房'
    },
    {
      key: '广州本地宝',
      name: '北京路'
    },
    {
      key: '广州本地宝',
      name: '华南植物园'
    },
    {
      key: '南汉二陵博物馆',
      name: '南汉二陵博物馆'
    },
    {
      key: '南沙区图书馆',
      name: '南沙区图书馆'
    },
    {
      key: '南沙天后宫',
      name: '南沙天后宫'
    },
    {
      key: '广州本地宝',
      name: '南沙湿地公园'
    },
    {
      key: '南沙湿地景区',
      name: '南沙湿地景区'
    },
    {
      key: '广州本地宝',
      name: '南越王博物院'
    },
    {
      key: 'nanyuewang',
      name: '南越王博物院（王墓展区）'
    },
    {
      key: 'gu_gov_9589229',
      name: '南越王博物馆'
    },
    {
      key: '增城1978文化创意园',
      name: '增城1978文化创意园'
    },
    {
      key: '增城区图书馆',
      name: '增城区图书馆'
    },
    {
      key: '广州本地宝',
      name: '大夫山森林公园'
    },
    {
      key: '广州本地宝',
      name: '天河公园'
    },
    {
      key: '广州本地宝',
      name: '天河城'
    },
    {
      key: '孙中山大元帅府纪念馆',
      name: '孙中山大元帅府纪念馆'
    },
    {
      key: '广州本地宝',
      name: '宝墨园'
    },
    {
      key: '广州本地宝',
      name: '岭南印象园'
    },
    {
      key: 'gu_gov_9588085',
      name: '岭南金融博物馆'
    },
    {
      key: 'gu_gov_6533841',
      name: '广东中医药博物馆'
    },
    {
      key: 'gu_gov_9589224',
      name: '广东华侨博物馆'
    },
    {
      key: 'gu_gov_9587900',
      name: '广东民间工艺博物馆'
    },
    {
      key: '广东省文化和旅游厅',
      name: '广东民间工艺博物馆（陈家祠）'
    },
    {
      key: 'gu_gov_9497366',
      name: '广东省人民体育场'
    },
    {
      key: 'gdmuseum',
      name: '广东省博物馆'
    },
    {
      key: 'gu_gov_9512996',
      name: '广东省奥林匹克体育中心'
    },
    {
      key: 'gu_gov_9589386',
      name: '广东省科技图书馆'
    },
    {
      key: '羊城晚报',
      name: '广东省立中山图书馆'
    },
    {
      key: '广州本地宝',
      name: '广东科学中心'
    },
    {
      key: '广州本地宝',
      name: '广东美术馆'
    },
    {
      key: 'gdartmuseum',
      name: '广东美术馆（二沙岛本馆）'
    },
    {
      key: '广州本地宝',
      name: '广州万菱汇'
    },
    {
      key: '广州本地宝',
      name: '广州三二九起义指挥部旧址'
    },
    {
      key: '广州本地宝',
      name: '广州上下九步行街'
    },
    {
      key: '广州本地宝',
      name: '广州东山湖公园'
    },
    {
      key: '广州本地宝',
      name: '广州九龙湖度假区'
    },
    {
      key: '广州本地宝',
      name: '广州九龙潭森林公园'
    },
    {
      key: '广州本地宝',
      name: '广州二沙岛'
    },
    {
      key: '广州本地宝',
      name: '广州二沙岛体育公园'
    },
    {
      key: '广州本地宝',
      name: '广州二沙岛艺术公园'
    },
    {
      key: 'gu_gov_9513170',
      name: '广州亚运城综合体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州从化区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州从化区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州从化区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州从化区公园'
    },
    {
      key: '广州本地宝',
      name: '广州从化区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州从化区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州从化区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州从化区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州从化区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州从化区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州从化区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州从化区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州从化区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州从化区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州从化区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州从化区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州从化区青少年宫'
    },
    {
      key: '广州本地宝',
      name: '广州从化流溪河国家森林公园'
    },
    {
      key: '广州本地宝',
      name: '广州从化温泉'
    },
    {
      key: '广州本地宝',
      name: '广州从化溪头村'
    },
    {
      key: '广州本地宝',
      name: '广州从化碧水湾温泉'
    },
    {
      key: '广州本地宝',
      name: '广州农民运动讲习所'
    },
    {
      key: '广州本地宝',
      name: '广州农民运动讲习所旧址'
    },
    {
      key: '广州本地宝',
      name: '广州凯德广场'
    },
    {
      key: '广州本地宝',
      name: '广州动物园'
    },
    {
      key: '广州本地宝',
      name: '广州北京路千年古道遗址'
    },
    {
      key: '广州本地宝',
      name: '广州北京路天河城'
    },
    {
      key: '广州本地宝',
      name: '广州北京路步行街'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区公园'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州南沙区青少年宫'
    },
    {
      key: '广州本地宝',
      name: '广州南沙天后宫'
    },
    {
      key: '广州本地宝',
      name: '广州南沙湿地公园'
    },
    {
      key: '广州本地宝',
      name: '广州南海神庙'
    },
    {
      key: '广州本地宝',
      name: '广州南越王墓博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州南越王宫博物馆'
    },
    {
      key: 'gzmuseum',
      name: '广州博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州国际金融城'
    },
    {
      key: 'gzlib',
      name: '广州图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州地铁博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州塔'
    },
    {
      key: '广州本地宝',
      name: '广州塔户外观景平台'
    },
    {
      key: '广州本地宝',
      name: '广州塔摩天轮'
    },
    {
      key: '广州本地宝',
      name: '广州塔极速云霄'
    },
    {
      key: 'manual',
      name: '广州塔珠江滨水步道'
    },
    {
      key: '广州本地宝',
      name: '广州增城区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州增城区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州增城区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州增城区公园'
    },
    {
      key: '广州本地宝',
      name: '广州增城区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州增城区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州增城区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州增城区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州增城区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州增城区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州增城区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州增城区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州增城区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州增城区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州增城区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州增城区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州增城区青少年宫'
    },
    {
      key: '广州本地宝',
      name: '广州增城正果老街'
    },
    {
      key: '广州本地宝',
      name: '广州增城白水寨'
    },
    {
      key: '广州本地宝',
      name: '广州大剧院'
    },
    {
      key: 'gu_gov_9511671',
      name: '广州大学城体育中心'
    },
    {
      key: '广州本地宝',
      name: '广州天河体育中心'
    },
    {
      key: '广州本地宝',
      name: '广州天河公园'
    },
    {
      key: '广州本地宝',
      name: '广州天河区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州天河区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州天河区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州天河区公园'
    },
    {
      key: '广州本地宝',
      name: '广州天河区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州天河区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州天河区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州天河区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州天河区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州天河区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州天河区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州天河区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州天河区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州天河区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州天河区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州天河区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州天河区青少年宫'
    },
    {
      key: '广州本地宝',
      name: '广州天河城'
    },
    {
      key: '广州本地宝',
      name: '广州天河城百货'
    },
    {
      key: '广州本地宝',
      name: '广州天鹿湖森林公园'
    },
    {
      key: '广州本地宝',
      name: '广州太古汇'
    },
    {
      key: '广州本地宝',
      name: '广州太古汇商场'
    },
    {
      key: '广州本地宝',
      name: '广州少年儿童图书馆'
    },
    {
      key: 'gu_gov_6533842',
      name: '广州市东平典当博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州市儿童公园'
    },
    {
      key: '广州市文化广电旅游局',
      name: '广州市文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州市文化馆新馆'
    },
    {
      key: 'manual',
      name: '广州市文化馆（新馆）'
    },
    {
      key: '广州本地宝',
      name: '广州开发区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州新儿童活动中心'
    },
    {
      key: '广州本地宝',
      name: '广州晓港公园'
    },
    {
      key: 'gu_gov_9512915',
      name: '广州棋院'
    },
    {
      key: '广州本地宝',
      name: '广州正佳广场'
    },
    {
      key: '广州民俗博物馆（花都）',
      name: '广州民俗博物馆（花都）'
    },
    {
      key: '广州本地宝',
      name: '广州沙面岛'
    },
    {
      key: '广州本地宝',
      name: '广州流花湖公园'
    },
    {
      key: '广州本地宝',
      name: '广州海印公园'
    },
    {
      key: '广州本地宝',
      name: '广州海心桥'
    },
    {
      key: '广州本地宝',
      name: '广州海心沙'
    },
    {
      key: '广州本地宝',
      name: '广州海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区公园'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州海珠区青少年宫'
    },
    {
      key: '广州本地宝',
      name: '广州海珠湖公园'
    },
    {
      key: 'gu_gov_9513134',
      name: '广州海角红楼游泳场'
    },
    {
      key: '广州本地宝',
      name: '广州滨江公园'
    },
    {
      key: '广州本地宝',
      name: '广州珠江公园'
    },
    {
      key: '广州本地宝',
      name: '广州珠江新城'
    },
    {
      key: '广州本地宝',
      name: '广州琶洲会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区公园'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州番禺区青少年宫'
    },
    {
      key: '广州本地宝',
      name: '广州白云万达广场'
    },
    {
      key: '广州本地宝',
      name: '广州白云区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州白云区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州白云区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州白云区公园'
    },
    {
      key: '广州本地宝',
      name: '广州白云区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州白云区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州白云区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州白云区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州白云区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州白云区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州白云区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州白云区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州白云区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州白云区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州白云区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州白云区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州白云区青少年宫'
    },
    {
      key: '广州本地宝',
      name: '广州粤剧艺术博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州维多利广场'
    },
    {
      key: '广州本地宝',
      name: '广州艺术博物院'
    },
    {
      key: 'gu_gov_9375725',
      name: '广州艺术博物院（广州美术馆）新馆'
    },
    {
      key: '广州本地宝',
      name: '广州芙蓉嶂风景区'
    },
    {
      key: '广州本地宝',
      name: '广州花城广场'
    },
    {
      key: '广州本地宝',
      name: '广州花都区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州花都区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州花都区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州花都区公园'
    },
    {
      key: '广州本地宝',
      name: '广州花都区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州花都区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州花都区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州花都区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州花都区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州花都区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州花都区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州花都区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州花都区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州花都区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州花都区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州花都区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州花都区青少年宫'
    },
    {
      key: '广州本地宝',
      name: '广州花都湖公园'
    },
    {
      key: '广州本地宝',
      name: '广州花都石头记矿物园'
    },
    {
      key: '广州本地宝',
      name: '广州花都融创乐园'
    },
    {
      key: '广州本地宝',
      name: '广州花都融创体育世界'
    },
    {
      key: '广州本地宝',
      name: '广州花都融创水世界'
    },
    {
      key: '广州本地宝',
      name: '广州花都融创雪世界'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区公园'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾区青少年宫'
    },
    {
      key: '广州本地宝',
      name: '广州荔湾湖公园'
    },
    {
      key: '广州本地宝',
      name: '广州萝岗香雪公园'
    },
    {
      key: '广州本地宝',
      name: '广州融创体育世界'
    },
    {
      key: '广州本地宝',
      name: '广州融创文旅城'
    },
    {
      key: '广州本地宝',
      name: '广州融创水世界'
    },
    {
      key: '广州本地宝',
      name: '广州融创雪世界'
    },
    {
      key: 'gu_gov_9589240',
      name: '广州货币金融博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州起义烈士陵园'
    },
    {
      key: '广州本地宝',
      name: '广州起义纪念馆'
    },
    {
      key: '广州本地宝',
      name: '广州越秀公园'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区公园'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州越秀区青少年宫'
    },
    {
      key: '广州本地宝',
      name: '广州近代史博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州长隆欢乐世界'
    },
    {
      key: '广州本地宝',
      name: '广州长隆水上乐园'
    },
    {
      key: '广州本地宝',
      name: '广州长隆野生动物世界'
    },
    {
      key: '广州本地宝',
      name: '广州长隆飞鸟乐园'
    },
    {
      key: '广州本地宝',
      name: '广州青少年科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州鲁迅纪念馆'
    },
    {
      key: '广州本地宝',
      name: '广州麓湖公园'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔公园'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔军校旧址'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区会展中心'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区体育场'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区体育馆'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区公园'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区创意园'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区剧院'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区动物园'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区博物馆'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区图书馆'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区文化中心'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区文化馆'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区植物园'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区海洋馆'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区科技馆'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区美术馆'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区艺术中心'
    },
    {
      key: '广州本地宝',
      name: '广州黄埔区青少年宫'
    },
    {
      key: '腾讯新闻',
      name: '星海音乐厅'
    },
    {
      key: '新瑞金票',
      name: '正佳大剧院'
    },
    {
      key: '广州本地宝',
      name: '正佳极地海洋世界'
    },
    {
      key: '广州本地宝',
      name: '正佳自然科学博物馆'
    },
    {
      key: '广州本地宝',
      name: '正佳雨林生态植物园'
    },
    {
      key: '农讲所纪念馆',
      name: '毛泽东同志主办农民运动讲习所旧址纪念馆'
    },
    {
      key: '广州本地宝',
      name: '永庆坊'
    },
    {
      key: 'manual',
      name: '永庆坊（西关非遗街区）'
    },
    {
      key: '广州本地宝',
      name: '沙湾古镇'
    },
    {
      key: 'gu_gov_9513274',
      name: '沙面体育俱乐部'
    },
    {
      key: '广州本地宝',
      name: '流溪河国家森林公园'
    },
    {
      key: '广州本地宝',
      name: '流花湖公园'
    },
    {
      key: '广州本地宝',
      name: '海珠国家湿地公园'
    },
    {
      key: '广州本地宝',
      name: '海珠湖公园'
    },
    {
      key: '广州本地宝',
      name: '海鸥岛'
    },
    {
      key: '广州本地宝',
      name: '珠江公园'
    },
    {
      key: 'gu_gov_6533839',
      name: '番禺博物馆'
    },
    {
      key: '广州本地宝',
      name: '白云山'
    },
    {
      key: '广州本地宝',
      name: '白云山风景名胜区'
    },
    {
      key: '广州本地宝',
      name: '白水寨风景名胜区'
    },
    {
      key: 'gu_gov_9589231',
      name: '粤剧艺术博物馆'
    },
    {
      key: '花都区图书馆',
      name: '花都区图书馆'
    },
    {
      key: '花都湖公园',
      name: '花都湖公园'
    },
    {
      key: 'gu_gov_6533840',
      name: '荔湾博物馆'
    },
    {
      key: '广州本地宝',
      name: '荔湾湖公园'
    },
    {
      key: '广州本地宝',
      name: '莲花山旅游区'
    },
    {
      key: '广州本地宝',
      name: '越秀公园'
    },
    {
      key: '长隆官方',
      name: '长隆旅游度假区'
    },
    {
      key: '广州本地宝',
      name: '长隆欢乐世界'
    },
    {
      key: '广州本地宝',
      name: '长隆水上乐园'
    },
    {
      key: '广州本地宝',
      name: '长隆野生动物世界'
    },
    {
      key: '广州本地宝',
      name: '陈家祠'
    },
    {
      key: 'gu_gov_6533843',
      name: '陈李济中药博物馆'
    },
    {
      key: '广州本地宝',
      name: '麓湖公园'
    },
    {
      key: '黄埔军校旧址纪念馆',
      name: '黄埔军校旧址纪念馆'
    }
  ],
  shanghai: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: 'shanghai_gov_theatre_61',
      name: '1933微剧场'
    },
    {
      key: 'shanghai_gov_community_129',
      name: '228街坊文化活动中心'
    },
    {
      key: 'shanghai_gov_art_32',
      name: 'Fotografiska 影像艺术中心'
    },
    {
      key: 'shanghai_gov_art_38',
      name: 'START星美术馆'
    },
    {
      key: 'shanghai_gov_theatre_91',
      name: 'YOUNG剧场-大剧院'
    },
    {
      key: 'shanghai_gov_theatre_92',
      name: 'YOUNG剧场-小剧院'
    },
    {
      key: 'shanghai_gov_art_23',
      name: 'chi K11美术馆'
    },
    {
      key: 'shanghai_gov_museum_83',
      name: '《义勇军进行曲》灌制地纪念馆 （百代小楼）'
    },
    {
      key: 'shanghai_gov_art_77',
      name: '丁聪美术馆'
    },
    {
      key: 'shanghai_gov_community_177',
      name: '七宝体育活动中心（航华分中心）'
    },
    {
      key: 'shanghai_gov_library_198',
      name: '七宝镇图书馆'
    },
    {
      key: 'shanghai_gov_community_176',
      name: '七宝镇文化体育事业发展中心'
    },
    {
      key: 'shanghai_gov_theatre_157',
      name: '万祥影剧院'
    },
    {
      key: 'shanghai_gov_library_32',
      name: '万祥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_33',
      name: '万祥镇文化服务中心'
    },
    {
      key: 'shanghai_gov_community_110',
      name: '万里社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_127',
      name: '万里街道图书馆'
    },
    {
      key: 'shanghai_gov_library_305',
      name: '三星镇图书馆'
    },
    {
      key: 'shanghai_gov_community_276',
      name: '三星镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_4',
      name: '三林镇前滩社区文化分中心'
    },
    {
      key: 'shanghai_gov_library_11',
      name: '三林镇图书馆'
    },
    {
      key: 'shanghai_gov_library_13',
      name: '三林镇图书馆世博分馆'
    },
    {
      key: 'shanghai_gov_library_12',
      name: '三林镇图书馆懿德分馆'
    },
    {
      key: 'shanghai_gov_community_3',
      name: '三林镇懿德文化分中心'
    },
    {
      key: 'shanghai_gov_community_2',
      name: '三林镇文化服务中心'
    },
    {
      key: 'shanghai_gov_theatre_28',
      name: '上展中心剧院'
    },
    {
      key: 'shanghai_gov_theatre_36',
      name: '上戏实验剧院'
    },
    {
      key: 'shanghai_gov_art_84',
      name: '上海YOUNG美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海七宝古镇'
    },
    {
      key: 'shanghai_gov_museum_32',
      name: '上海三山会馆管理处'
    },
    {
      key: '上海本地宝',
      name: '上海上海大学'
    },
    {
      key: '上海本地宝',
      name: '上海上海工程技术大学'
    },
    {
      key: '上海本地宝',
      name: '上海上海师范大学'
    },
    {
      key: '上海本地宝',
      name: '上海上海理工大学'
    },
    {
      key: 'shanghai_gov_theatre_122',
      name: '上海世博中心有限公司(红厅）'
    },
    {
      key: '上海世博会博物馆',
      name: '上海世博会博物馆'
    },
    {
      key: 'shanghai_gov_museum_118',
      name: '上海世界技能博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海世纪公园'
    },
    {
      key: 'shanghai_gov_theatre_54',
      name: '上海东亚体育文化中心有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海东华大学'
    },
    {
      key: 'shanghai_gov_museum_13',
      name: '上海东方地质博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海东方明珠太空舱'
    },
    {
      key: '上海本地宝',
      name: '上海东方明珠悬空观光廊'
    },
    {
      key: '上海本地宝',
      name: '上海东方艺术中心'
    },
    {
      key: 'shanghai_gov_theatre_117',
      name: '上海东方艺术中心管理有限公司-歌剧厅'
    },
    {
      key: 'shanghai_gov_theatre_118',
      name: '上海东方艺术中心管理有限公司-演奏厅'
    },
    {
      key: 'shanghai_gov_theatre_116',
      name: '上海东方艺术中心管理有限公司-音乐厅'
    },
    {
      key: 'shanghai_gov_theatre_71',
      name: '上海东虹桥剧院管理有限公司'
    },
    {
      key: 'shanghai_gov_theatre_63',
      name: '上海丝芭文化传媒有限公司-星梦剧场'
    },
    {
      key: '上海本地宝',
      name: '上海中医药博物馆'
    },
    {
      key: 'shanghai_gov_museum_164',
      name: '上海中华印刷博物馆'
    },
    {
      key: 'shanghai_gov_theatre_7',
      name: '上海中国大戏院有限公司'
    },
    {
      key: 'shanghai_gov_museum_126',
      name: '上海中国工业设计博物馆'
    },
    {
      key: 'shanghai_gov_museum_109',
      name: '上海中国烟草博物馆'
    },
    {
      key: 'shanghai_gov_art_43',
      name: '上海中国画院 程十发美术馆'
    },
    {
      key: 'shanghai_gov_art_33',
      name: '上海中国画院美术馆'
    },
    {
      key: 'shanghai_gov_museum_152',
      name: '上海中国留学生博物馆'
    },
    {
      key: 'shanghai_gov_museum_5',
      name: '上海中国航海博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海中山公园'
    },
    {
      key: '上海本地宝',
      name: '上海中心大厦'
    },
    {
      key: '上海本地宝',
      name: '上海中心大厦观光厅'
    },
    {
      key: '上海本地宝',
      name: '上海临港新城'
    },
    {
      key: 'shanghai_gov_art_18',
      name: '上海久事美术馆'
    },
    {
      key: 'shanghai_gov_theatre_131',
      name: '上海乐来乐好剧院管理有限公司'
    },
    {
      key: 'shanghai_gov_theatre_90',
      name: '上海乐演优你科技有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海乐高乐园'
    },
    {
      key: 'shanghai_gov_theatre_139',
      name: '上海九棵树文化传媒有限公司—大剧场'
    },
    {
      key: 'shanghai_gov_theatre_141',
      name: '上海九棵树文化传媒有限公司—实验剧场'
    },
    {
      key: 'shanghai_gov_theatre_140',
      name: '上海九棵树文化传媒有限公司—小剧场'
    },
    {
      key: 'shanghai_gov_theatre_142',
      name: '上海九棵树文化传媒有限公司—森林剧场'
    },
    {
      key: 'shanghai_gov_theatre_143',
      name: '上海九棵树文化传媒有限公司—水岸舞台'
    },
    {
      key: 'shanghai_gov_museum_139',
      name: '上海乳业博物馆'
    },
    {
      key: 'shanghai_gov_theatre_51',
      name: '上海交响乐团音乐厅'
    },
    {
      key: '上海本地宝',
      name: '上海交通大学'
    },
    {
      key: 'shanghai_gov_art_61',
      name: '上海交通大学 程及美术馆'
    },
    {
      key: 'shanghai_gov_museum_138',
      name: '上海交通大学博物馆'
    },
    {
      key: 'shanghai_gov_museum_75',
      name: '上海交通大学校史博物馆'
    },
    {
      key: 'shanghai_gov_museum_76',
      name: '上海交通大学董浩云航运博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海人民公园'
    },
    {
      key: 'shanghai_gov_theatre_19',
      name: '上海人民大舞台'
    },
    {
      key: 'shanghai_gov_museum_46',
      name: '上海体育博物馆'
    },
    {
      key: 'shanghai_gov_museum_114',
      name: '上海体育大学武术博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海体育馆'
    },
    {
      key: 'shanghai_gov_theatre_160',
      name: '上海保利云间剧院管理有限公司'
    },
    {
      key: 'shanghai_gov_theatre_147',
      name: '上海保利大剧院'
    },
    {
      key: '上海本地宝',
      name: '上海儿童博物馆'
    },
    {
      key: 'shanghai_gov_theatre_10',
      name: '上海儿童国际文化发展有限公司（上海儿童艺术剧场-中心剧场）'
    },
    {
      key: 'shanghai_gov_theatre_11',
      name: '上海儿童国际文化发展有限公司（上海儿童艺术剧场-小剧场）'
    },
    {
      key: 'shanghai_gov_theatre_9',
      name: '上海儿童国际文化发展有限公司（上海儿童艺术剧场-黑匣子剧场）'
    },
    {
      key: '上海本地宝',
      name: '上海儿童艺术剧场'
    },
    {
      key: 'shanghai_gov_museum_93',
      name: '上海元代水闸遗址博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海八万人体育场'
    },
    {
      key: 'shanghai_gov_theatre_27',
      name: '上海八佰秀企业管理有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海公安博物馆'
    },
    {
      key: 'shanghai_gov_theatre_18',
      name: '上海兰心大戏院'
    },
    {
      key: 'shanghai_gov_theatre_110',
      name: '上海兰馨影业有限公司'
    },
    {
      key: 'shanghai_gov_theatre_6',
      name: '上海共舞台有限公司'
    },
    {
      key: 'shanghai_gov_theatre_120',
      name: '上海冉旭文化娱乐中心'
    },
    {
      key: 'shanghai_gov_museum_168',
      name: '上海农垦博物馆'
    },
    {
      key: 'shanghai_gov_museum_89',
      name: '上海凝聚力工程博物馆'
    },
    {
      key: 'shanghai_gov_museum_10',
      name: '上海动漫博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海动物园'
    },
    {
      key: 'shanghai_gov_art_67',
      name: '上海半岛美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海华东师范大学'
    },
    {
      key: '上海本地宝',
      name: '上海华东理工大学'
    },
    {
      key: '上海本地宝',
      name: '上海南京东路步行街'
    },
    {
      key: 'shanghai_gov_theatre_98',
      name: '上海南汇周浦影剧场'
    },
    {
      key: '上海本地宝',
      name: '上海南汇嘴观海公园'
    },
    {
      key: 'shanghai_gov_museum_149',
      name: '上海南社纪念馆'
    },
    {
      key: 'shanghaimuseum',
      name: '上海博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海博物馆东馆'
    },
    {
      key: '上海本地宝',
      name: '上海博物馆人民广场馆'
    },
    {
      key: 'shanghai_gov_museum_60',
      name: '上海印刷字体展示馆'
    },
    {
      key: 'shanghai_gov_museum_24',
      name: '上海双拥工作展览馆'
    },
    {
      key: '上海本地宝',
      name: '上海古猗园'
    },
    {
      key: '上海本地宝',
      name: '上海同济大学'
    },
    {
      key: 'shanghai_gov_art_96',
      name: '上海吴宜恩美术馆'
    },
    {
      key: 'shanghai_gov_museum_8',
      name: '上海吴昌硕纪念馆'
    },
    {
      key: 'shanghai_gov_museum_35',
      name: '上海周虎臣曹素功笔墨博物馆'
    },
    {
      key: 'shanghai_gov_museum_82',
      name: '上海品牌博物馆'
    },
    {
      key: 'shanghai_gov_theatre_40',
      name: '上海商城有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区公园'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区动物园'
    },
    {
      key: 'shanghai_gov_art_74',
      name: '上海嘉定区北虹桥美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海嘉定区艺术中心'
    },
    {
      key: 'shanghai_gov_art_76',
      name: '上海嘉定十方画院'
    },
    {
      key: 'shanghai_gov_museum_58',
      name: '上海四行仓库抗战纪念馆'
    },
    {
      key: 'shanghai_gov_art_89',
      name: '上海国稷美术馆'
    },
    {
      key: 'shanghai_gov_theatre_94',
      name: '上海国际时尚中心园区管理有限公司'
    },
    {
      key: 'shanghai_gov_theatre_70',
      name: '上海国际舞蹈中心剧场经营管理有限公司'
    },
    {
      key: 'shanghai_gov_museum_155',
      name: '上海国际酒文化博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海图书馆'
    },
    {
      key: 'manual',
      name: '上海图书馆总馆'
    },
    {
      key: 'shanghai_gov_library_2',
      name: '上海图书馆（东馆）'
    },
    {
      key: 'shanghai_gov_library_1',
      name: '上海图书馆（淮海馆）'
    },
    {
      key: 'shanghai_gov_museum_67',
      name: '上海土山湾博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海地铁博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海地震科普馆'
    },
    {
      key: 'shanghai_gov_theatre_77',
      name: '上海城市剧院管理有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海城市规划展示馆'
    },
    {
      key: '上海本地宝',
      name: '上海城隍庙'
    },
    {
      key: '上海本地宝',
      name: '上海复旦大学'
    },
    {
      key: 'shanghai_gov_art_25',
      name: '上海复星艺术中心'
    },
    {
      key: 'shanghai_gov_museum_157',
      name: '上海外国语大学语言博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海外滩'
    },
    {
      key: 'shanghai_gov_art_24',
      name: '上海外滩美术馆'
    },
    {
      key: 'shanghai_gov_theatre_129',
      name: '上海外高桥文化传播有限公司'
    },
    {
      key: 'shanghai_gov_art_52',
      name: '上海多伦现代美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海大剧院'
    },
    {
      key: 'shanghai_gov_theatre_13',
      name: '上海大剧院-中剧场'
    },
    {
      key: 'shanghai_gov_theatre_12',
      name: '上海大剧院-大剧场'
    },
    {
      key: 'shanghai_gov_theatre_14',
      name: '上海大剧院-小剧场'
    },
    {
      key: 'shanghai_gov_museum_125',
      name: '上海大学博物馆（海派文化博物馆）'
    },
    {
      key: 'shanghai_gov_art_31',
      name: '上海大学美术馆'
    },
    {
      key: 'shanghai_gov_theatre_49',
      name: '上海大戏院'
    },
    {
      key: 'shanghai_gov_museum_146',
      name: '上海大来时间博物馆'
    },
    {
      key: 'shanghai_gov_theatre_55',
      name: '上海大舞台'
    },
    {
      key: '上海本地宝',
      name: '上海大观园'
    },
    {
      key: 'shanghai_gov_museum_153',
      name: '上海天文博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海天文馆'
    },
    {
      key: 'shanghai_gov_museum_21',
      name: '上海天文馆（上海科技馆分馆）'
    },
    {
      key: 'shanghai_gov_theatre_17',
      name: '上海天蟾逸夫舞台'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区艺术中心'
    },
    {
      key: '上海本地宝',
      name: '上海奉贤区青少年宫'
    },
    {
      key: 'shanghai_gov_theatre_137',
      name: '上海奉贤钱桥影剧院'
    },
    {
      key: 'shanghai_gov_museum_34',
      name: '上海孙中山故居纪念馆'
    },
    {
      key: 'shanghai_gov_theatre_127',
      name: '上海宋城世博演艺发展有限公司-千古情'
    },
    {
      key: 'shanghai_gov_theatre_128',
      name: '上海宋城世博演艺发展有限公司-百乐门'
    },
    {
      key: 'shanghai_gov_museum_69',
      name: '上海宋庆龄故居纪念馆'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区公园'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海宝山区青少年宫'
    },
    {
      key: 'shanghai_gov_art_60',
      name: '上海宝山区龙现代美术馆'
    },
    {
      key: 'shanghai_gov_museum_22',
      name: '上海宝库匠心博物馆'
    },
    {
      key: 'shanghai_gov_art_64',
      name: '上海宝龙美术馆'
    },
    {
      key: 'shanghai_gov_museum_61',
      name: '上海寰宇铃铛博物馆'
    },
    {
      key: 'shanghai_gov_museum_92',
      name: '上海对外经贸大学博物馆'
    },
    {
      key: 'shanghai_gov_museum_127',
      name: '上海尊木汇木文化博物馆'
    },
    {
      key: 'shanghai_gov_theatre_29',
      name: '上海小伙伴剧场'
    },
    {
      key: '上海本地宝',
      name: '上海少年儿童图书馆'
    },
    {
      key: 'manual',
      name: '上海少年儿童图书馆新馆'
    },
    {
      key: 'shanghai_gov_library_4',
      name: '上海少年儿童图书馆（南西馆）'
    },
    {
      key: 'shanghai_gov_library_3',
      name: '上海少年儿童图书馆（长风馆）'
    },
    {
      key: 'shanghai_gov_theatre_30',
      name: '上海尚演文化投资管理有限公司'
    },
    {
      key: 'shanghai_gov_theatre_109',
      name: '上海尚银东艺数字影城管理有限公司'
    },
    {
      key: 'shanghai_gov_theatre_159',
      name: '上海展博置业有限公司（滴水湖剧院）'
    },
    {
      key: '上海展览中心',
      name: '上海展览中心'
    },
    {
      key: 'shanghai_gov_museum_172',
      name: '上海崇明向化灶文化博物馆'
    },
    {
      key: 'shanghai_gov_museum_173',
      name: '上海崇明竖新抗日战争博物馆'
    },
    {
      key: 'shanghai_gov_museum_163',
      name: '上海崧泽遗址博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海工艺美术博物馆'
    },
    {
      key: 'shanghai_gov_theatre_88',
      name: '上海市优演剧场管理有限公司'
    },
    {
      key: 'shanghai_gov_theatre_107',
      name: '上海市南汇大团镇永春演艺厅'
    },
    {
      key: 'shanghai_gov_theatre_108',
      name: '上海市南汇航头镇陶园春演艺厅'
    },
    {
      key: 'shanghai_gov_theatre_8',
      name: '上海市卢湾体育中心'
    },
    {
      key: 'shhistorymuseum',
      name: '上海市历史博物馆'
    },
    {
      key: 'shanghai_gov_museum_27',
      name: '上海市历史博物馆（上海革命历史博物馆）'
    },
    {
      key: 'shanghai_gov_museum_39',
      name: '上海市外滩历史纪念馆'
    },
    {
      key: 'shanghai_gov_theatre_132',
      name: '上海市奉贤区机关服务中心'
    },
    {
      key: 'shanghai_gov_theatre_57',
      name: '上海市宛平艺苑'
    },
    {
      key: 'manual',
      name: '上海市少年宫'
    },
    {
      key: 'shanghai_gov_theatre_150',
      name: '上海市崇明影剧院'
    },
    {
      key: 'shanghai_gov_art_34',
      name: '上海市徐汇区艺术馆'
    },
    {
      key: 'shanghai_gov_museum_151',
      name: '上海市松江区博物馆'
    },
    {
      key: 'shanghai_gov_museum_150',
      name: '上海市沧海盐田盐文化博物馆'
    },
    {
      key: 'shanghai_gov_theatre_44',
      name: '上海市沪北电影院有限责任公司'
    },
    {
      key: 'shanghai_gov_theatre_105',
      name: '上海市浦东新区航头镇书场茶馆'
    },
    {
      key: 'shanghai_gov_theatre_111',
      name: '上海市澧溪文化艺术有限公司'
    },
    {
      key: 'manual',
      name: '上海市群众艺术馆'
    },
    {
      key: 'shanghai_gov_museum_42',
      name: '上海市银行博物馆'
    },
    {
      key: 'shanghai_gov_museum_84',
      name: '上海市长宁区革命文物陈列馆'
    },
    {
      key: 'shanghai_gov_theatre_69',
      name: '上海市长宁文化艺术中心'
    },
    {
      key: 'shanghai_gov_theatre_68',
      name: '上海市长宁民俗文化中心'
    },
    {
      key: 'shanghai_gov_culture_18',
      name: '上海市闵行区文化和旅游管理事务中心 （上海市闵行区群众艺术馆）'
    },
    {
      key: 'shanghai_gov_theatre_41',
      name: '上海市闸北区宋园茶艺馆（书场）'
    },
    {
      key: 'shanghai_gov_museum_122',
      name: '上海市陶行知纪念馆'
    },
    {
      key: 'shanghai_gov_museum_162',
      name: '上海市青浦区任屯血防陈列馆'
    },
    {
      key: 'shanghai_gov_theatre_81',
      name: '上海市青浦区文化馆'
    },
    {
      key: 'shanghai_gov_art_92',
      name: '上海市鹤龙美术馆'
    },
    {
      key: 'shanghai_gov_theatre_21',
      name: '上海市黄浦区文化馆（上海市雅庐书场）-白玉兰剧场'
    },
    {
      key: 'shanghai_gov_theatre_22',
      name: '上海市黄浦区文化馆（上海市雅庐书场）-雅庐书场'
    },
    {
      key: 'shanghai_gov_museum_68',
      name: '上海市龙华烈士纪念馆'
    },
    {
      key: 'shanghai_gov_museum_73',
      name: '上海师范大学博物馆'
    },
    {
      key: 'shanghai_gov_museum_91',
      name: '上海广播博物馆'
    },
    {
      key: 'shanghai_gov_theatre_121',
      name: '上海张江文化控股有限公司-张江戏剧谷'
    },
    {
      key: '上海当代艺术博物馆',
      name: '上海当代艺术博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海徐家汇商圈'
    },
    {
      key: 'shanghai_gov_art_40',
      name: '上海徐汇区九点水美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区艺术中心'
    },
    {
      key: '上海本地宝',
      name: '上海徐汇区青少年宫'
    },
    {
      key: '上海本地宝',
      name: '上海惊魂密境'
    },
    {
      key: 'shanghai_gov_theatre_31',
      name: '上海戏剧学院'
    },
    {
      key: 'shanghai_gov_theatre_59',
      name: '上海摩登嘉旋文化发展有限公司'
    },
    {
      key: 'shcstheatre',
      name: '上海文化广场'
    },
    {
      key: 'shanghai_gov_theatre_20',
      name: '上海文化广场剧院管理有限公司'
    },
    {
      key: 'shanghai_gov_theatre_73',
      name: '上海新东苑实业有限公司'
    },
    {
      key: 'shanghai_gov_theatre_5',
      name: '上海新光影艺苑有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海新天地'
    },
    {
      key: 'shanghai_gov_museum_79',
      name: '上海无线电博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海昆虫博物馆'
    },
    {
      key: 'shanghai_gov_art_12',
      name: '上海昊美术馆'
    },
    {
      key: 'shanghai_gov_art_39',
      name: '上海明圆美术馆'
    },
    {
      key: 'shanghai_gov_art_65',
      name: '上海明珠美术馆'
    },
    {
      key: 'shanghai_gov_theatre_146',
      name: '上海星轶思达爱斯影院管理有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区公园'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区艺术中心'
    },
    {
      key: '上海本地宝',
      name: '上海普陀区青少年宫'
    },
    {
      key: 'shanghai_gov_museum_128',
      name: '上海智慧湾增材制造文化博物馆'
    },
    {
      key: 'shanghai_gov_museum_16',
      name: '上海有恒博物馆'
    },
    {
      key: 'shanghai_gov_theatre_3',
      name: '上海木偶剧团有限公司'
    },
    {
      key: 'shanghai_gov_theatre_4',
      name: '上海木偶剧团有限公司（小剧场）'
    },
    {
      key: '上海本地宝',
      name: '上海朱家角古镇'
    },
    {
      key: '上海本地宝',
      name: '上海杜莎夫人蜡像馆'
    },
    {
      key: 'shanghai_gov_museum_158',
      name: '上海来伊份零食博物馆'
    },
    {
      key: 'shanghai_gov_art_46',
      name: '上海杨培明宣传画收藏艺术馆'
    },
    {
      key: 'shanghai_gov_museum_130',
      name: '上海杨明洁工业设计博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区公园'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海杨浦区青少年宫'
    },
    {
      key: 'shanghai_gov_art_88',
      name: '上海松江云间少儿美术馆'
    },
    {
      key: 'shanghai_gov_art_82',
      name: '上海松江云间美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海松江区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海松江区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海松江区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海松江区公园'
    },
    {
      key: '上海本地宝',
      name: '上海松江区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海松江区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海松江区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海松江区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海松江区文化馆'
    },
    {
      key: 'shanghai_gov_art_86',
      name: '上海松江区新桥美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海松江区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海松江区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海松江区美术馆'
    },
    {
      key: 'shanghai_gov_art_87',
      name: '上海松江区贤禾美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海松江区青少年宫'
    },
    {
      key: '上海本地宝',
      name: '上海松江大学城'
    },
    {
      key: '上海本地宝',
      name: '上海松江方塔园'
    },
    {
      key: 'shanghai_gov_art_85',
      name: '上海松江清控人居美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海松江醉白池'
    },
    {
      key: '上海本地宝',
      name: '上海枫泾古镇'
    },
    {
      key: 'shanghai_gov_theatre_136',
      name: '上海柘林影剧院'
    },
    {
      key: '上海本地宝',
      name: '上海梅赛德斯奔驰文化中心'
    },
    {
      key: 'shanghai_gov_museum_59',
      name: '上海棋牌文化博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海植物园'
    },
    {
      key: '上海本地宝',
      name: '上海欢乐谷'
    },
    {
      key: '上海本地宝',
      name: '上海欢乐谷玛雅海滩水公园'
    },
    {
      key: '上海本地宝',
      name: '上海欢乐谷谷木游龙'
    },
    {
      key: '上海本地宝',
      name: '上海欢乐谷魔幻城堡'
    },
    {
      key: 'shanghai_gov_art_45',
      name: '上海正好美术馆'
    },
    {
      key: 'shanghai_gov_museum_48',
      name: '上海毛泽东旧居陈列馆'
    },
    {
      key: 'shanghai_gov_museum_38',
      name: '上海民政博物馆'
    },
    {
      key: 'shanghai_gov_museum_133',
      name: '上海民族乐器博物馆'
    },
    {
      key: 'shanghai_gov_art_22',
      name: '上海民生现代美术馆'
    },
    {
      key: 'shanghai_gov_museum_81',
      name: '上海气象博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海汽车博物馆'
    },
    {
      key: 'shanghai_gov_art_42',
      name: '上海油画雕塑院美术馆'
    },
    {
      key: 'shanghai_gov_art_37',
      name: '上海油罐艺术中心'
    },
    {
      key: 'shanghai_gov_theatre_65',
      name: '上海泛景文化传播有限公司-珍珠剧场'
    },
    {
      key: '上海本地宝',
      name: '上海泰晤士小镇'
    },
    {
      key: 'shanghai_gov_museum_99',
      name: '上海泰迪之家泰迪熊博物馆'
    },
    {
      key: 'shanghai_gov_library_5',
      name: '上海浦东图书馆'
    },
    {
      key: 'shanghai_gov_library_6',
      name: '上海浦东图书馆南汇分馆'
    },
    {
      key: 'shanghai_gov_library_9',
      name: '上海浦东图书馆少儿分馆'
    },
    {
      key: 'shanghai_gov_library_7',
      name: '上海浦东图书馆陆家嘴分馆（东方路）'
    },
    {
      key: 'shanghai_gov_library_8',
      name: '上海浦东图书馆陆家嘴分馆（浦城路）'
    },
    {
      key: 'shanghai_gov_theatre_101',
      name: '上海浦东新区三墩影剧院'
    },
    {
      key: 'shanghai_gov_theatre_126',
      name: '上海浦东新区三林影剧院'
    },
    {
      key: 'shanghai_gov_theatre_104',
      name: '上海浦东新区东方电影院有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区公园'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区博物馆'
    },
    {
      key: 'shanghai_gov_art_14',
      name: '上海浦东新区叁柒贰叁美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区图书馆'
    },
    {
      key: 'shanghai_gov_theatre_102',
      name: '上海浦东新区川沙影剧院'
    },
    {
      key: 'shanghai_gov_art_10',
      name: '上海浦东新区库伯美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区美术馆'
    },
    {
      key: 'shanghai_gov_art_13',
      name: '上海浦东新区联明美术馆'
    },
    {
      key: 'shanghai_gov_art_15',
      name: '上海浦东新区越婷惠美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海浦东新区青少年宫'
    },
    {
      key: 'shanghai_gov_art_9',
      name: '上海浦东林隐美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海浦东游泳馆'
    },
    {
      key: 'shanghai_gov_art_3',
      name: '上海浦东碧云美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海海昌海洋公园'
    },
    {
      key: '上海本地宝',
      name: '上海海昌海洋公园北极熊馆'
    },
    {
      key: '上海本地宝',
      name: '上海海昌海洋公园虎鲸馆'
    },
    {
      key: '上海本地宝',
      name: '上海海洋大学'
    },
    {
      key: 'shanghai_gov_museum_113',
      name: '上海海洋大学博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海海洋水族馆'
    },
    {
      key: 'shanghai_gov_museum_17',
      name: '上海海派红木艺术博物馆'
    },
    {
      key: 'shanghai_gov_art_62',
      name: '上海海派艺术馆'
    },
    {
      key: 'shanghai_gov_museum_147',
      name: '上海海纳吴觉农茶文化博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海消防博物馆'
    },
    {
      key: 'shanghai_gov_museum_119',
      name: '上海淞沪抗战纪念馆'
    },
    {
      key: '上海本地宝',
      name: '上海淮海中路'
    },
    {
      key: 'shanghai_gov_art_59',
      name: '上海湫光美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海源深体育中心'
    },
    {
      key: '上海本地宝',
      name: '上海滨江森林公园'
    },
    {
      key: '上海本地宝',
      name: '上海滴水湖'
    },
    {
      key: 'shanghai_gov_museum_20',
      name: '上海火炬众创孵化博物馆'
    },
    {
      key: 'shanghai_gov_museum_106',
      name: '上海犹太难民纪念馆'
    },
    {
      key: 'shanghai_gov_art_6',
      name: '上海王狮美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海环球金融中心'
    },
    {
      key: '上海本地宝',
      name: '上海环球金融中心观光厅'
    },
    {
      key: '上海本地宝',
      name: '上海玻璃博物馆'
    },
    {
      key: 'shanghai_gov_museum_112',
      name: '上海理工大学印刷博物馆'
    },
    {
      key: 'shanghai_gov_museum_36',
      name: '上海琉璃艺术博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海田子坊'
    },
    {
      key: 'shanghai_gov_museum_37',
      name: '上海电信博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海电影博物馆'
    },
    {
      key: 'shanghai_gov_museum_170',
      name: '上海电线电缆博物馆'
    },
    {
      key: 'shanghai_gov_museum_129',
      name: '上海百诺巧克力博物馆'
    },
    {
      key: 'shanghai_gov_theatre_66',
      name: '上海盈寰文化传媒有限公司-BlueNote'
    },
    {
      key: 'shanghai_gov_museum_169',
      name: '上海真静传统木作博物馆'
    },
    {
      key: 'shanghai_gov_museum_57',
      name: '上海眼镜博物馆'
    },
    {
      key: 'shanghai_gov_museum_167',
      name: '上海知青博物馆'
    },
    {
      key: 'shanghai_gov_museum_161',
      name: '上海福寿园人文纪念馆'
    },
    {
      key: 'shstm',
      name: '上海科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海科技馆主馆'
    },
    {
      key: '上海本地宝',
      name: '上海科技馆分馆'
    },
    {
      key: 'shanghai_gov_art_72',
      name: '上海秦古美术馆'
    },
    {
      key: 'shanghai_gov_museum_154',
      name: '上海立信会计学院中国会计博物馆'
    },
    {
      key: 'shanghai_gov_theatre_119',
      name: '上海笋馨文化传媒有限公司'
    },
    {
      key: 'shanghai_gov_museum_165',
      name: '上海红十字历史文化陈列馆'
    },
    {
      key: 'shanghai_gov_museum_96',
      name: '上海纺织博物馆'
    },
    {
      key: 'shanghai_gov_art_58',
      name: '上海美术学院美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海美术馆'
    },
    {
      key: 'chinaartmuseum',
      name: '上海美术馆（中华艺术宫）'
    },
    {
      key: 'shanghai_gov_museum_9',
      name: '上海美特斯邦威服饰博物馆'
    },
    {
      key: 'shanghai_gov_theatre_38',
      name: '上海美琪大戏院'
    },
    {
      key: 'shanghai_gov_museum_145',
      name: '上海翥云艺术博物馆'
    },
    {
      key: 'shanghai_gov_museum_137',
      name: '上海翰林匾额博物馆'
    },
    {
      key: 'shanghai_gov_museum_19',
      name: '上海老相机摄影博物馆'
    },
    {
      key: 'shanghai_gov_theatre_158',
      name: '上海聆海美琪文化艺术发展有限公司（临港演艺中心）'
    },
    {
      key: 'shanghai_gov_theatre_135',
      name: '上海胡桥影剧院'
    },
    {
      key: '上海本地宝',
      name: '上海自然博物馆'
    },
    {
      key: 'shanghai_gov_museum_52',
      name: '上海自然博物馆（上海科技馆分馆）'
    },
    {
      key: 'shanghai_gov_museum_135',
      name: '上海航宇科普中心'
    },
    {
      key: '上海本地宝',
      name: '上海航海博物馆'
    },
    {
      key: 'shanghai_gov_art_11',
      name: '上海艺仓美术馆'
    },
    {
      key: 'shanghai_gov_theatre_100',
      name: '上海艺晟文化传播有限公司'
    },
    {
      key: 'shanghai_gov_museum_90',
      name: '上海艺术品博物馆'
    },
    {
      key: 'shanghai_gov_art_83',
      name: '上海艺术百代美术馆'
    },
    {
      key: 'shanghai_gov_theatre_45',
      name: '上海艺海剧场'
    },
    {
      key: 'shanghai_gov_art_50',
      name: '上海苏宁艺术馆'
    },
    {
      key: 'shanghai_gov_museum_49',
      name: '上海蔡元培故居陈列馆'
    },
    {
      key: 'shanghai_gov_theatre_67',
      name: '上海虹口保利大剧院管理有限公司-北外滩友邦大剧院'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区公园'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区艺术中心'
    },
    {
      key: '上海本地宝',
      name: '上海虹口区青少年宫'
    },
    {
      key: 'shanghai_gov_art_53',
      name: '上海虹口青藤美术馆'
    },
    {
      key: 'shanghai_gov_art_44',
      name: '上海虹桥当代美术馆'
    },
    {
      key: 'shanghai_gov_theatre_86',
      name: '上海虹馆文化发展有限公司'
    },
    {
      key: 'shanghai_gov_theatre_56',
      name: '上海表坊文化发展有限公司-上剧场'
    },
    {
      key: 'shanghai_gov_museum_14',
      name: '上海观复博物馆'
    },
    {
      key: 'shanghai_gov_museum_136',
      name: '上海观止矿晶博物馆'
    },
    {
      key: 'shanghai_gov_museum_123',
      name: '上海解放纪念馆'
    },
    {
      key: 'shanghai_gov_theatre_114',
      name: '上海证大喜马拉雅演艺有限公司'
    },
    {
      key: 'shanghai_gov_theatre_48',
      name: '上海话剧艺术中心-D6空间'
    },
    {
      key: 'shanghai_gov_theatre_47',
      name: '上海话剧艺术中心-戏剧沙龙'
    },
    {
      key: 'shanghai_gov_theatre_46',
      name: '上海话剧艺术中心-艺术剧院'
    },
    {
      key: 'shanghai_gov_theatre_26',
      name: '上海话剧艺术中心有限公司黄浦分公司（茉莉花剧场）'
    },
    {
      key: '上海本地宝',
      name: '上海豫园'
    },
    {
      key: 'shanghai_gov_museum_31',
      name: '上海豫园管理处'
    },
    {
      key: 'shanghai_gov_theatre_25',
      name: '上海豫尚文化传播有限公司'
    },
    {
      key: 'shanghai_gov_museum_115',
      name: '上海财经大学商学博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海辰山植物园温室'
    },
    {
      key: '上海本地宝',
      name: '上海辰山植物园矿坑花园'
    },
    {
      key: '上海本地宝',
      name: '上海迪士尼乐园'
    },
    {
      key: '上海本地宝',
      name: '上海迪士尼乐园城堡'
    },
    {
      key: '上海本地宝',
      name: '上海迪士尼乐园奇想花园'
    },
    {
      key: '上海本地宝',
      name: '上海迪士尼乐园宝藏湾'
    },
    {
      key: '上海本地宝',
      name: '上海迪士尼乐园探险岛'
    },
    {
      key: '上海本地宝',
      name: '上海迪士尼乐园明日世界'
    },
    {
      key: '上海本地宝',
      name: '上海迪士尼乐园梦幻世界'
    },
    {
      key: '上海本地宝',
      name: '上海迪士尼乐园皮克斯玩具总动员'
    },
    {
      key: '上海迪士尼度假区',
      name: '上海迪士尼度假区'
    },
    {
      key: 'shanghai_gov_theatre_133',
      name: '上海邬桥牡丹影剧院'
    },
    {
      key: 'shanghai_gov_museum_105',
      name: '上海邮政博物馆'
    },
    {
      key: 'shanghai_gov_theatre_87',
      name: '上海释乐文化传播有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海野生动物园'
    },
    {
      key: 'shanghai_gov_theatre_112',
      name: '上海野生动物园发展有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海野生动物园步行区'
    },
    {
      key: '上海本地宝',
      name: '上海野生动物园车行区'
    },
    {
      key: 'shanghai_gov_museum_15',
      name: '上海金刚博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海金山区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海金山区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海金山区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海金山区公园'
    },
    {
      key: '上海本地宝',
      name: '上海金山区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海金山区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海金山区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海金山区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海金山区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海金山区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海金山区海洋馆'
    },
    {
      key: 'shanghai_gov_art_78',
      name: '上海金山区海鸥美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海金山区科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海金山区艺术中心'
    },
    {
      key: 'shanghai_gov_art_69',
      name: '上海金臣亦飞鸣美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海金茂大厦观光厅'
    },
    {
      key: 'manual',
      name: '上海铁路博物馆'
    },
    {
      key: 'shanghai_gov_theatre_43',
      name: '上海铁路工人文化宫'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区公园'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区艺术中心'
    },
    {
      key: '上海本地宝',
      name: '上海长宁区青少年宫'
    },
    {
      key: 'shanghai_gov_art_47',
      name: '上海长宁华萃当代美术馆'
    },
    {
      key: 'shanghai_gov_art_48',
      name: '上海长宁王小慧艺术馆'
    },
    {
      key: 'shanghai_gov_theatre_23',
      name: '上海长江剧场（红匣子）'
    },
    {
      key: 'shanghai_gov_theatre_24',
      name: '上海长江剧场（黑匣子）'
    },
    {
      key: '上海本地宝',
      name: '上海长风公园'
    },
    {
      key: '上海本地宝',
      name: '上海长风海洋世界'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区公园'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区科技馆'
    },
    {
      key: 'shanghai_gov_art_66',
      name: '上海闵行区美博美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海闵行区艺术中心'
    },
    {
      key: '上海本地宝',
      name: '上海陆家嘴'
    },
    {
      key: '上海本地宝',
      name: '上海陆家嘴中心绿地'
    },
    {
      key: 'shanghai_gov_museum_120',
      name: '上海陈化成纪念馆'
    },
    {
      key: 'shanghai_gov_museum_110',
      name: '上海院士风采馆'
    },
    {
      key: '上海本地宝',
      name: '上海隧道科技馆'
    },
    {
      key: 'shanghai_gov_theatre_80',
      name: '上海零湾美琪剧院管理有限公司'
    },
    {
      key: 'shanghai_gov_theatre_78',
      name: '上海零聚演出经纪有限公司'
    },
    {
      key: 'shanghai_gov_museum_11',
      name: '上海震旦博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区公园'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区科技馆'
    },
    {
      key: 'shanghai_gov_art_95',
      name: '上海青浦区练塘可的美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海青浦区艺术中心'
    },
    {
      key: 'shanghai_gov_art_94',
      name: '上海青浦区金夜美术馆'
    },
    {
      key: 'shanghai_gov_art_93',
      name: '上海青浦青渚美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海静安体育中心'
    },
    {
      key: '上海本地宝',
      name: '上海静安区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海静安区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海静安区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海静安区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海静安区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海静安区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海静安区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海静安区文化馆'
    },
    {
      key: '上海本地宝',
      name: '上海静安区植物园'
    },
    {
      key: '上海本地宝',
      name: '上海静安区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海静安区科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海静安区美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海静安区艺术中心'
    },
    {
      key: '上海本地宝',
      name: '上海静安区青少年宫'
    },
    {
      key: 'shanghai_gov_art_30',
      name: '上海静安大风堂美术馆'
    },
    {
      key: '上海本地宝',
      name: '上海静安寺'
    },
    {
      key: 'shanghai_gov_art_29',
      name: '上海静安毕加索艺术馆'
    },
    {
      key: 'shanghai_gov_art_71',
      name: '上海韩天衡美术馆'
    },
    {
      key: 'shanghai_gov_museum_33',
      name: '上海韬奋纪念馆'
    },
    {
      key: '上海本地宝',
      name: '上海音乐厅'
    },
    {
      key: 'shanghai_gov_theatre_16',
      name: '上海音乐厅小剧场'
    },
    {
      key: 'shanghai_gov_museum_74',
      name: '上海音乐学院东方乐器博物馆'
    },
    {
      key: 'shanghai_gov_theatre_152',
      name: '上海风瀛洲文化传播有限公司'
    },
    {
      key: '上海本地宝',
      name: '上海马戏城'
    },
    {
      key: 'shanghai_gov_theatre_39',
      name: '上海马戏城有限公司'
    },
    {
      key: 'shanghai_gov_art_21',
      name: '上海驰翰美术馆'
    },
    {
      key: 'shanghai_gov_museum_100',
      name: '上海鲁迅纪念馆'
    },
    {
      key: 'shanghai_gov_theatre_1',
      name: '上海黄浦剧场有限公司'
    },
    {
      key: 'shanghai_gov_theatre_2',
      name: '上海黄浦剧场有限公司（小剧场）'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区会展中心'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区体育场'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区体育馆'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区公园'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区创意园'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区剧院'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区动物园'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区博物馆'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区图书馆'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区文化中心'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区海洋馆'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区科技馆'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区艺术中心'
    },
    {
      key: '上海本地宝',
      name: '上海黄浦区青少年宫'
    },
    {
      key: 'shanghai_gov_museum_88',
      name: '上海（东华大学）纺织服饰博物馆'
    },
    {
      key: 'shanghai_gov_museum_12',
      name: '上海（中医药大学）中医药博物馆'
    },
    {
      key: 'shanghai_gov_library_21',
      name: '上钢图书馆'
    },
    {
      key: 'shanghai_gov_library_22',
      name: '上钢图书馆综合体分馆'
    },
    {
      key: 'shanghai_gov_community_37',
      name: '上钢社区文化活动中心'
    },
    {
      key: 'shanghai_gov_theatre_53',
      name: '上音歌剧院'
    },
    {
      key: '上海本地宝',
      name: '世界技能博物馆'
    },
    {
      key: '上海本地宝',
      name: '世纪公园'
    },
    {
      key: 'shanghai_gov_theatre_93',
      name: '东宫剧院'
    },
    {
      key: 'shanghai_gov_library_298',
      name: '东平镇图书馆'
    },
    {
      key: 'shanghai_gov_community_270',
      name: '东平镇社区文化活动中心'
    },
    {
      key: '上海本地宝',
      name: '东方明珠'
    },
    {
      key: '上海本地宝',
      name: '东方明珠塔'
    },
    {
      key: 'shanghai_gov_community_47',
      name: '东明社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_48',
      name: '东明社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_library_24',
      name: '东明路街道图书馆'
    },
    {
      key: '中共一大纪念馆',
      name: '中共一大纪念馆'
    },
    {
      key: 'shanghai_gov_museum_53',
      name: '中共三大后中央局机关历史纪念馆'
    },
    {
      key: 'shanghai_gov_museum_50',
      name: '中共上海地下组织斗争史陈列馆暨刘长胜故居'
    },
    {
      key: 'shanghai_gov_museum_63',
      name: '中共中央军委机关旧址纪念馆'
    },
    {
      key: 'shanghai_gov_museum_62',
      name: '中共中央秘书处机关旧址纪念馆'
    },
    {
      key: 'shanghai_gov_museum_51',
      name: '中共二大会址纪念馆'
    },
    {
      key: 'shanghai_gov_museum_29',
      name: '中共代表团驻沪办事处纪念馆（周公馆）'
    },
    {
      key: 'shanghai_gov_museum_101',
      name: '中共四大纪念馆'
    },
    {
      key: 'shanghai_gov_museum_54',
      name: '中共淞浦特委机关旧址陈列馆'
    },
    {
      key: 'shanghai_gov_library_311',
      name: '中兴镇图书馆'
    },
    {
      key: 'shanghai_gov_community_275',
      name: '中兴镇社区文化活动中心'
    },
    {
      key: '上观新闻',
      name: '中华艺术宫'
    },
    {
      key: '中华艺术宫（上海美术馆）',
      name: '中华艺术宫（上海美术馆）'
    },
    {
      key: 'shanghai_gov_museum_47',
      name: '中国劳动组合书记部旧址陈列馆'
    },
    {
      key: 'shanghai_gov_museum_30',
      name: '中国社会主义青年团中央机关旧址纪念馆'
    },
    {
      key: 'shanghai_gov_theatre_34',
      name: '中国福利会儿童艺术剧院(马兰花剧场)'
    },
    {
      key: 'shanghai_gov_museum_72',
      name: '中国科学院上海昆虫博物馆'
    },
    {
      key: '上海本地宝',
      name: '中国航海博物馆'
    },
    {
      key: 'shanghai_gov_museum_107',
      name: '中国证券博物馆'
    },
    {
      key: 'shanghai_gov_museum_117',
      name: '中国近现代新闻出版博物馆'
    },
    {
      key: 'shanghai_gov_museum_64',
      name: '中央特科机关旧址纪念馆'
    },
    {
      key: 'shanghai_gov_library_258',
      name: '中山街道图书馆'
    },
    {
      key: 'shanghai_gov_community_210',
      name: '中山街道社区党群服务中心（中山幸福里）'
    },
    {
      key: 'shanghai_gov_art_68',
      name: '中闵虹桥美术馆'
    },
    {
      key: 'shanghai_gov_community_61',
      name: '临汾社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_89',
      name: '临汾路街道图书馆'
    },
    {
      key: '上海本地宝',
      name: '乐高探索中心'
    },
    {
      key: 'shanghai_gov_library_244',
      name: '九亭镇图书馆'
    },
    {
      key: 'shanghai_gov_community_216',
      name: '九亭镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_259',
      name: '九里亭街道图书馆'
    },
    {
      key: 'shanghai_gov_community_224',
      name: '九里亭街道社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_53',
      name: '书院镇图书馆'
    },
    {
      key: 'shanghai_gov_community_11',
      name: '书院镇文化服务中心'
    },
    {
      key: 'shanghai_gov_theatre_37',
      name: '云峰剧院'
    },
    {
      key: 'shanghai_gov_art_79',
      name: '云间会堂美术馆'
    },
    {
      key: 'shanghai_gov_community_120',
      name: '五角场社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_121',
      name: '五角场社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_library_157',
      name: '五角场街道图书馆'
    },
    {
      key: 'shanghai_gov_library_158',
      name: '五角场街道图书馆（国定支路分馆）'
    },
    {
      key: 'shanghai_gov_community_49',
      name: '五里桥社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_65',
      name: '五里桥街道图书馆'
    },
    {
      key: 'shanghai_gov_museum_18',
      name: '交通银行博物馆'
    },
    {
      key: 'shanghai_gov_library_236',
      name: '亭林镇图书馆'
    },
    {
      key: 'shanghai_gov_community_201',
      name: '亭林镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_202',
      name: '亭林镇社区文化活动中心松隐分中心'
    },
    {
      key: 'shanghai_gov_library_240',
      name: '人文松江活动中心（松江区图书馆）'
    },
    {
      key: 'shanghai_gov_culture_21',
      name: '人文松江活动中心（松江区文化馆）'
    },
    {
      key: '上海本地宝',
      name: '人民广场'
    },
    {
      key: 'shanghai_gov_library_119',
      name: '仙霞新村街道图书馆'
    },
    {
      key: 'shanghai_gov_community_95',
      name: '仙霞社区文化活动中心（东部）'
    },
    {
      key: 'shanghai_gov_community_94',
      name: '仙霞社区文化活动中心（西部）'
    },
    {
      key: 'shanghai_gov_library_247',
      name: '佘山镇佘北图书馆'
    },
    {
      key: 'shanghai_gov_library_246',
      name: '佘山镇图书馆'
    },
    {
      key: 'shanghai_gov_community_212',
      name: '佘山镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_213',
      name: '佘山镇社区文化活动中心佘北分中心'
    },
    {
      key: 'shanghai_gov_art_91',
      name: '余德耀美术馆'
    },
    {
      key: 'shanghai_gov_theatre_145',
      name: '依弘剧场'
    },
    {
      key: 'shanghai_gov_theatre_115',
      name: '保利尚悦湾（上海）剧院管理有限公司1862时尚艺术中心'
    },
    {
      key: 'shanghai_gov_theatre_130',
      name: '信德前滩（上海）文化置业有限公司'
    },
    {
      key: 'shanghai_gov_library_45',
      name: '傅雷图书馆'
    },
    {
      key: 'shanghai_gov_museum_55',
      name: '元利当铺旧址博物馆'
    },
    {
      key: 'shanghai_gov_theatre_33',
      name: '兰馨影业有限公司-光影车间.静剧场'
    },
    {
      key: 'shanghai_gov_library_88',
      name: '共和新路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_70',
      name: '共和新路街道社区党群服务中心'
    },
    {
      key: '上海本地宝',
      name: '共青森林公园'
    },
    {
      key: 'shanghai_gov_library_141',
      name: '凉城新村街道图书馆'
    },
    {
      key: 'shanghai_gov_community_117',
      name: '凉城新村街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_86',
      name: '凌云街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_105',
      name: '凌云路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_239',
      name: '凤溪社区文化体育服务中心（凤溪分中心）'
    },
    {
      key: 'shanghai_gov_art_57',
      name: '刘小晴艺术馆'
    },
    {
      key: 'shanghai_gov_art_41',
      name: '刘海粟美术馆'
    },
    {
      key: 'shanghai_gov_art_49',
      name: '刘海粟美术馆(分馆)'
    },
    {
      key: 'manual',
      name: '前滩太古里'
    },
    {
      key: 'manual',
      name: '北外滩来福士广场'
    },
    {
      key: 'shanghai_gov_library_144',
      name: '北外滩街道图书馆'
    },
    {
      key: 'shanghai_gov_community_118',
      name: '北外滩街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_91',
      name: '北新泾社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_112',
      name: '北新泾街道图书馆'
    },
    {
      key: 'shanghai_gov_library_84',
      name: '北站街道图书馆（艺术图书馆）'
    },
    {
      key: 'shanghai_gov_community_60',
      name: '北站街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_15',
      name: '北蔡镇图书馆'
    },
    {
      key: 'shanghai_gov_community_40',
      name: '北蔡镇文化服务中心'
    },
    {
      key: 'shanghai_gov_community_56',
      name: '半淞园路社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_59',
      name: '半淞园路街道图书馆'
    },
    {
      key: 'shanghai_gov_museum_97',
      name: '华东师范大学博物馆'
    },
    {
      key: 'shanghai_gov_library_210',
      name: '华亭镇图书馆'
    },
    {
      key: 'shanghai_gov_community_185',
      name: '华亭镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_art_26',
      name: '华山艺术馆'
    },
    {
      key: 'shanghai_gov_library_264',
      name: '华新镇图书馆'
    },
    {
      key: 'shanghai_gov_library_265',
      name: '华新镇图书馆（凤溪分馆）'
    },
    {
      key: 'shanghai_gov_community_238',
      name: '华新镇文化体育服务中心'
    },
    {
      key: 'shanghai_gov_community_88',
      name: '华泾社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_108',
      name: '华泾镇图书馆'
    },
    {
      key: 'shanghai_gov_library_191',
      name: '华漕镇图书馆'
    },
    {
      key: 'shanghai_gov_community_169',
      name: '华漕镇文化体育事业发展中心'
    },
    {
      key: 'shanghai_gov_community_89',
      name: '华阳社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_116',
      name: '华阳路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_50',
      name: '南京东路社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_62',
      name: '南京东路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_80',
      name: '南京西路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_81',
      name: '南京西路街道少儿图书馆'
    },
    {
      key: 'shanghai_gov_community_64',
      name: '南京西路街道社区文化活动中心（福民会馆）'
    },
    {
      key: '上海本地宝',
      name: '南京路'
    },
    {
      key: 'shanghai_gov_museum_124',
      name: '南京路上好八连事迹陈列馆'
    },
    {
      key: 'shanghai_gov_library_283',
      name: '南桥镇图书馆'
    },
    {
      key: 'shanghai_gov_theatre_106',
      name: '南汇三灶影剧院'
    },
    {
      key: 'shanghai_gov_theatre_99',
      name: '南汇宣桥镇影剧院'
    },
    {
      key: 'shanghai_gov_library_29',
      name: '南汇新城镇图书馆（申港馆）'
    },
    {
      key: 'shanghai_gov_library_28',
      name: '南汇新城镇图书馆（芦潮港馆）'
    },
    {
      key: 'shanghai_gov_community_29',
      name: '南汇新城镇社区党群服务中心（文化服务中心）'
    },
    {
      key: 'shanghai_gov_theatre_97',
      name: '南汇海东影剧院'
    },
    {
      key: 'shanghai_gov_theatre_103',
      name: '南汇盐仓影剧院'
    },
    {
      key: 'shanghai_gov_community_38',
      name: '南码头社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_10',
      name: '南码头路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_217',
      name: '南翔镇图书馆'
    },
    {
      key: 'shanghai_gov_library_218',
      name: '南翔镇图书馆东社区分馆'
    },
    {
      key: 'shanghai_gov_community_184',
      name: '南翔镇文化体育服务中心'
    },
    {
      key: 'shanghai_gov_library_181',
      name: '友谊路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_145',
      name: '友谊路街道社区事务受理服务中心'
    },
    {
      key: 'shanghai_gov_community_146',
      name: '友谊路街道社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_library_188',
      name: '古美路街道图书馆（东馆）'
    },
    {
      key: 'shanghai_gov_library_189',
      name: '古美路街道图书馆（西馆）'
    },
    {
      key: 'shanghai_gov_community_167',
      name: '古美路街道社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_255',
      name: '叶榭镇图书馆'
    },
    {
      key: 'shanghai_gov_community_220',
      name: '叶榭镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_33',
      name: '合庆镇图书馆'
    },
    {
      key: 'shanghai_gov_community_41',
      name: '合庆镇文化服务中心'
    },
    {
      key: 'shanghai_gov_museum_116',
      name: '同济大学博物馆'
    },
    {
      key: 'shanghai_gov_library_307',
      name: '向化镇图书馆'
    },
    {
      key: 'shanghai_gov_community_281',
      name: '向化镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_231',
      name: '吕巷镇图书馆'
    },
    {
      key: 'shanghai_gov_library_232',
      name: '吕巷镇图书馆干巷分馆'
    },
    {
      key: 'shanghai_gov_community_200',
      name: '吕巷镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_theatre_76',
      name: '吴泾文化馆'
    },
    {
      key: 'shanghai_gov_library_199',
      name: '吴泾镇图书馆'
    },
    {
      key: 'shanghai_gov_community_174',
      name: '吴泾镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_179',
      name: '吴淞街道图书馆'
    },
    {
      key: 'shanghai_gov_community_152',
      name: '吴淞街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_99',
      name: '周家桥社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_122',
      name: '周家桥街道图书馆'
    },
    {
      key: 'shanghai_gov_library_20',
      name: '周家渡街道图书馆'
    },
    {
      key: 'shanghai_gov_community_35',
      name: '周家渡街道文化中心'
    },
    {
      key: 'shanghai_gov_art_8',
      name: '周浦美术馆'
    },
    {
      key: 'shanghai_gov_library_44',
      name: '周浦镇图书馆'
    },
    {
      key: 'shanghai_gov_community_1',
      name: '周浦镇文化服务中心'
    },
    {
      key: 'shanghai_gov_library_47',
      name: '唐镇图书馆'
    },
    {
      key: 'shanghai_gov_library_48',
      name: '唐镇图书馆（王港分中心）'
    },
    {
      key: 'shanghai_gov_community_8',
      name: '唐镇文化体育中心'
    },
    {
      key: 'shanghai_gov_library_138',
      name: '嘉兴路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_111',
      name: '嘉兴路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_112',
      name: '嘉兴路街道社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_library_205',
      name: '嘉定区图书馆'
    },
    {
      key: 'shanghai_gov_library_206',
      name: '嘉定区图书馆清河路分馆'
    },
    {
      key: 'manual',
      name: '嘉定区文化馆'
    },
    {
      key: 'manual',
      name: '嘉定博物馆'
    },
    {
      key: 'shanghai_gov_library_211',
      name: '嘉定工业区图书馆'
    },
    {
      key: 'shanghai_gov_community_189',
      name: '嘉定工业区文化体育服务中心'
    },
    {
      key: 'shanghai_gov_theatre_148',
      name: '嘉定影剧院有限责任公司'
    },
    {
      key: 'shanghai_gov_museum_141',
      name: '嘉定竹刻博物馆'
    },
    {
      key: 'shanghai_gov_community_180',
      name: '嘉定镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_212',
      name: '嘉定镇街道图书馆'
    },
    {
      key: 'shanghai_gov_art_75',
      name: '嘉源海美术馆'
    },
    {
      key: 'shanghai_gov_library_285',
      name: '四团镇图书馆'
    },
    {
      key: 'shanghai_gov_community_256',
      name: '四团镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_145',
      name: '四川北路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_116',
      name: '四川北路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_156',
      name: '四平路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_123',
      name: '四平路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_museum_144',
      name: '四海壶具博物馆'
    },
    {
      key: 'shanghai_gov_museum_108',
      name: '国歌展示馆'
    },
    {
      key: 'shanghai_gov_museum_44',
      name: '国际乒联博物馆（中国乒乓球博物馆）'
    },
    {
      key: 'shanghai_gov_library_297',
      name: '城桥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_277',
      name: '城桥镇社区党群服务中心 （城桥镇文体服务中心）'
    },
    {
      key: 'shanghai_gov_library_294',
      name: '堡镇图书馆'
    },
    {
      key: 'shanghai_gov_community_267',
      name: '堡镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_24',
      name: '塘桥社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_14',
      name: '塘桥街道图书馆'
    },
    {
      key: 'shanghai_gov_museum_111',
      name: '复旦大学博物馆'
    },
    {
      key: 'shanghai_gov_library_268',
      name: '夏阳街道图书馆'
    },
    {
      key: 'shanghai_gov_community_245',
      name: '夏阳街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_219',
      name: '外冈镇图书馆'
    },
    {
      key: 'shanghai_gov_community_181',
      name: '外冈镇文化体育服务中心'
    },
    {
      key: '上海本地宝',
      name: '外滩'
    },
    {
      key: 'shanghai_gov_community_54',
      name: '外滩社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_64',
      name: '外滩街道图书馆'
    },
    {
      key: 'shanghai_gov_library_56',
      name: '大团镇图书馆'
    },
    {
      key: 'shanghai_gov_community_9',
      name: '大团镇文化服务中心'
    },
    {
      key: 'shanghai_gov_library_166',
      name: '大场镇图书馆'
    },
    {
      key: 'shanghai_gov_community_162',
      name: '大场镇社会事业发展服务中心'
    },
    {
      key: 'shanghai_gov_library_87',
      name: '大宁路街道分馆（社区文化中心）'
    },
    {
      key: 'shanghai_gov_library_85',
      name: '大宁路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_67',
      name: '大宁路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_150',
      name: '大桥街道图书馆'
    },
    {
      key: 'shanghai_gov_community_122',
      name: '大桥街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_192',
      name: '大零号湾图书馆'
    },
    {
      key: 'shanghai_gov_museum_43',
      name: '大韩民国临时政府旧址管理处'
    },
    {
      key: 'shanghai_gov_community_92',
      name: '天山社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_118',
      name: '天山路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_76',
      name: '天平街道66梧桐院(文化活动分中心)'
    },
    {
      key: 'shanghai_gov_community_75',
      name: '天平街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_96',
      name: '天平路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_92',
      name: '天目西路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_73',
      name: '天目西路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_292',
      name: '头桥街道图书馆'
    },
    {
      key: 'shanghai_gov_community_263',
      name: '头桥街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_280',
      name: '奉城镇图书馆'
    },
    {
      key: 'shanghai_gov_community_258',
      name: '奉城镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_288',
      name: '奉浦街道图书馆'
    },
    {
      key: 'shanghai_gov_community_261',
      name: '奉浦街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_theatre_134',
      name: '奉贤区南桥影剧院'
    },
    {
      key: 'shanghai_gov_museum_166',
      name: '奉贤区博物馆'
    },
    {
      key: 'shanghai_gov_library_279',
      name: '奉贤区图书馆'
    },
    {
      key: 'shanghai_gov_culture_23',
      name: '奉贤区文化馆'
    },
    {
      key: 'shanghai_gov_theatre_138',
      name: '奉贤县青村文化站'
    },
    {
      key: 'shanghai_gov_library_86',
      name: '宁的书房'
    },
    {
      key: 'shanghai_gov_library_207',
      name: '安亭镇图书馆'
    },
    {
      key: 'shanghai_gov_library_209',
      name: '安亭镇图书馆（方泰分馆）'
    },
    {
      key: 'shanghai_gov_library_208',
      name: '安亭镇图书馆（黄渡分馆）'
    },
    {
      key: 'shanghai_gov_community_191',
      name: '安亭镇文化体育服务中心'
    },
    {
      key: 'shanghai_gov_community_193',
      name: '安亭镇文化体育服务中心方泰分中心'
    },
    {
      key: 'shanghai_gov_community_192',
      name: '安亭镇文化体育服务中心黄渡分中心'
    },
    {
      key: 'shanghai_gov_museum_86',
      name: '宋庆龄生平事迹陈列馆'
    },
    {
      key: 'shanghai_gov_library_151',
      name: '定海路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_125',
      name: '定海路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_126',
      name: '定海路街道社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_community_109',
      name: '宜川社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_132',
      name: '宜川路街道图书馆'
    },
    {
      key: 'manual',
      name: '宝山体育中心'
    },
    {
      key: 'manual',
      name: '宝山区图书馆'
    },
    {
      key: 'manual',
      name: '宝山区文化馆'
    },
    {
      key: 'manual',
      name: '宝山博物馆'
    },
    {
      key: 'shanghai_gov_community_69',
      name: '宝山路街道党群服务中心'
    },
    {
      key: 'shanghai_gov_library_83',
      name: '宝山路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_30',
      name: '宣桥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_34',
      name: '宣桥镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_66',
      name: '小东门街道图书馆'
    },
    {
      key: 'shanghai_gov_community_55',
      name: '小东门街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_252',
      name: '小昆山镇图书馆'
    },
    {
      key: 'shanghai_gov_community_227',
      name: '小昆山镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_233',
      name: '山阳镇图书馆'
    },
    {
      key: 'shanghai_gov_library_234',
      name: '山阳镇海璟图书馆'
    },
    {
      key: 'shanghai_gov_community_196',
      name: '山阳镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_257',
      name: '岳阳街道图书馆'
    },
    {
      key: 'shanghai_gov_community_219',
      name: '岳阳街道社区党群服务中心'
    },
    {
      key: 'shanghai_gov_museum_171',
      name: '崇明区博物馆'
    },
    {
      key: 'shanghai_gov_library_293',
      name: '崇明区图书馆'
    },
    {
      key: 'shanghai_gov_culture_24',
      name: '崇明区文化馆'
    },
    {
      key: 'shanghai_gov_theatre_151',
      name: '崇明县沪剧团'
    },
    {
      key: 'shanghai_gov_art_97',
      name: '崇明美术馆'
    },
    {
      key: 'shanghai_gov_community_16',
      name: '川沙新镇文化服务中心'
    },
    {
      key: 'shanghai_gov_museum_102',
      name: '左联会址纪念馆'
    },
    {
      key: 'shanghai_gov_community_127',
      name: '平凉社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_155',
      name: '平凉路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_137',
      name: '广中路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_119',
      name: '广中路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_260',
      name: '广富林街道图书馆'
    },
    {
      key: 'shanghai_gov_community_221',
      name: '广富林街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_287',
      name: '庄行镇图书馆'
    },
    {
      key: 'shanghai_gov_community_254',
      name: '庄行镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_255',
      name: '庄行镇社区文化活动中心（邬桥分中心）'
    },
    {
      key: 'shanghai_gov_library_177',
      name: '庙行镇图书馆'
    },
    {
      key: 'shanghai_gov_community_156',
      name: '庙行镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_157',
      name: '庙行镇社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_library_304',
      name: '庙镇图书馆'
    },
    {
      key: 'shanghai_gov_community_278',
      name: '庙镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_103',
      name: '康健新村街道图书馆'
    },
    {
      key: 'shanghai_gov_community_84',
      name: '康健街道社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_39',
      name: '康桥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_26',
      name: '康桥镇文化服务中心'
    },
    {
      key: 'shanghai_gov_library_230',
      name: '廊下镇图书馆'
    },
    {
      key: 'shanghai_gov_community_206',
      name: '廊下镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_162',
      name: '延吉新村街道图书馆'
    },
    {
      key: 'shanghai_gov_community_133',
      name: '延吉社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_302',
      name: '建设镇图书馆'
    },
    {
      key: 'shanghai_gov_community_266',
      name: '建设镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_theatre_149',
      name: '开心麻花剧场'
    },
    {
      key: 'shanghai_gov_museum_132',
      name: '张充仁纪念馆'
    },
    {
      key: 'shanghai_gov_library_237',
      name: '张堰镇图书馆'
    },
    {
      key: 'shanghai_gov_community_207',
      name: '张堰镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_186',
      name: '张庙街道图书馆'
    },
    {
      key: 'shanghai_gov_community_161',
      name: '张庙街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_16',
      name: '张江图书馆'
    },
    {
      key: 'shanghai_gov_library_17',
      name: '张江图书馆孙桥分馆'
    },
    {
      key: 'shanghai_gov_community_42',
      name: '张江镇文化服务中心'
    },
    {
      key: 'shanghai_gov_community_43',
      name: '张江镇文化服务中心-孙桥分中心'
    },
    {
      key: 'shanghai_gov_museum_2',
      name: '张闻天故居'
    },
    {
      key: 'shanghai_gov_library_90',
      name: '彭浦新村街道图书馆'
    },
    {
      key: 'shanghai_gov_community_71',
      name: '彭浦新村街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_91',
      name: '彭浦镇图书馆'
    },
    {
      key: 'shanghai_gov_community_68',
      name: '彭浦镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_museum_66',
      name: '徐光启纪念馆'
    },
    {
      key: '上海本地宝',
      name: '徐家汇'
    },
    {
      key: '上海本地宝',
      name: '徐家汇书院'
    },
    {
      key: 'shanghai_gov_community_74',
      name: '徐家汇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_95',
      name: '徐家汇街道图书馆'
    },
    {
      key: 'manual',
      name: '徐汇区图书馆'
    },
    {
      key: 'shanghai_gov_library_94',
      name: '徐汇区图书馆（徐家汇书院）'
    },
    {
      key: 'shanghai_gov_culture_9',
      name: '徐汇区文化馆'
    },
    {
      key: 'shanghai_gov_theatre_52',
      name: '徐汇区田林街道社区文化活动中心'
    },
    {
      key: '上海本地宝',
      name: '徐汇滨江滑板公园'
    },
    {
      key: 'manual',
      name: '徐汇西岸滨江'
    },
    {
      key: 'shanghai_gov_community_229',
      name: '徐泾北大居社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_community_228',
      name: '徐泾社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_269',
      name: '徐泾镇图书馆'
    },
    {
      key: 'shanghai_gov_library_270',
      name: '徐泾镇图书馆（北大居分馆）'
    },
    {
      key: 'shanghai_gov_library_221',
      name: '徐行镇图书馆'
    },
    {
      key: 'shanghai_gov_community_187',
      name: '徐行镇文化体育服务中心'
    },
    {
      key: 'shanghai_gov_community_250',
      name: '徐里桥社区文化活动中心'
    },
    {
      key: 'shanghai_gov_art_28',
      name: '心象艺术馆'
    },
    {
      key: 'shanghai_gov_library_34',
      name: '惠南镇图书馆'
    },
    {
      key: 'shanghai_gov_library_35',
      name: '惠南镇图书馆东城分馆'
    },
    {
      key: 'shanghai_gov_community_18',
      name: '惠南镇文化服务中心'
    },
    {
      key: 'shanghai_gov_community_51',
      name: '打浦桥社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_60',
      name: '打浦桥街道图书馆'
    },
    {
      key: 'misa',
      name: '捷豹上海交响音乐厅'
    },
    {
      key: 'shanghai_gov_library_154',
      name: '控江路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_136',
      name: '控江路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_137',
      name: '控江路街道社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_community_140',
      name: '政青路文化活动分中心'
    },
    {
      key: 'shanghai_gov_art_55',
      name: '敦煌当代美术馆'
    },
    {
      key: 'shanghai_gov_theatre_32',
      name: '文艺会堂'
    },
    {
      key: 'shanghai_gov_community_80',
      name: '斜土社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_99',
      name: '斜土路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_93',
      name: '新华社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_120',
      name: '新华路街道图书馆'
    },
    {
      key: 'shanghai_gov_museum_7',
      name: '新场历史文化陈列馆'
    },
    {
      key: 'shanghai_gov_library_31',
      name: '新场镇图书馆'
    },
    {
      key: 'shanghai_gov_community_20',
      name: '新场镇文化服务中心'
    },
    {
      key: 'shanghai_gov_library_37',
      name: '新川沙图书馆（少儿馆）'
    },
    {
      key: 'shanghai_gov_library_36',
      name: '新川沙图书馆（成人馆）'
    },
    {
      key: 'shanghai_gov_library_220',
      name: '新成路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_183',
      name: '新成路街道社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_308',
      name: '新村乡图书馆'
    },
    {
      key: 'shanghai_gov_community_273',
      name: '新村乡社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_254',
      name: '新桥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_223',
      name: '新桥镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_community_139',
      name: '新江湾城社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_164',
      name: '新江湾城街道图书馆'
    },
    {
      key: 'shanghai_gov_library_310',
      name: '新河镇图书馆'
    },
    {
      key: 'shanghai_gov_community_274',
      name: '新河镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_121',
      name: '新泾镇图书馆'
    },
    {
      key: 'shanghai_gov_community_90',
      name: '新泾镇社区文化事务中心'
    },
    {
      key: 'shanghai_gov_library_253',
      name: '新浜镇图书馆'
    },
    {
      key: 'shanghai_gov_community_217',
      name: '新浜镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_theatre_74',
      name: '新浦江影剧院'
    },
    {
      key: 'shanghai_gov_library_309',
      name: '新海镇图书馆'
    },
    {
      key: 'shanghai_gov_community_272',
      name: '新海镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_200',
      name: '新虹街道图书馆'
    },
    {
      key: 'shanghai_gov_community_166',
      name: '新虹街道社区党群服务中心'
    },
    {
      key: 'shanghai_gov_community_209',
      name: '方松社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_243',
      name: '方松街道图书馆'
    },
    {
      key: 'shanghai_gov_theatre_75',
      name: '旗忠森林体育城'
    },
    {
      key: 'shanghai_gov_art_27',
      name: '明当代美术馆'
    },
    {
      key: 'shanghai_gov_art_19',
      name: '春美术馆'
    },
    {
      key: 'manual',
      name: '普陀区图书馆'
    },
    {
      key: 'shanghai_gov_culture_16',
      name: '普陀区文化馆'
    },
    {
      key: 'manual',
      name: '普陀区青少年宫'
    },
    {
      key: 'manual',
      name: '普陀青少年水主题科普基地'
    },
    {
      key: 'shanghai_gov_library_143',
      name: '曲阳路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_113',
      name: '曲阳路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_74',
      name: '曹家渡街道图书馆'
    },
    {
      key: 'shanghai_gov_library_76',
      name: '曹家渡街道图书馆（少儿）'
    },
    {
      key: 'shanghai_gov_community_65',
      name: '曹家渡街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_75',
      name: '曹家渡街道达安星之会所图书室'
    },
    {
      key: 'shanghai_gov_library_124',
      name: '曹杨新村街道图书馆'
    },
    {
      key: 'shanghai_gov_community_102',
      name: '曹杨社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_13',
      name: '曹路社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_14',
      name: '曹路社区文化活动中心顾路分中心'
    },
    {
      key: 'shanghai_gov_library_38',
      name: '曹路镇图书馆'
    },
    {
      key: 'shanghai_gov_community_12',
      name: '曹路镇文化服务中心'
    },
    {
      key: 'shanghai_gov_library_183',
      name: '月浦镇图书馆（庆安路馆）'
    },
    {
      key: 'shanghai_gov_library_182',
      name: '月浦镇图书馆（盛桥馆）'
    },
    {
      key: 'shanghai_gov_library_185',
      name: '月浦镇图书馆（马泾桥馆）'
    },
    {
      key: 'shanghai_gov_library_184',
      name: '月浦镇图书馆（龙镇路馆）'
    },
    {
      key: 'shanghai_gov_community_160',
      name: '月浦镇社区文化中心（友间公寓分中心）'
    },
    {
      key: 'shanghai_gov_community_159',
      name: '月浦镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_275',
      name: '朱家角镇图书馆'
    },
    {
      key: 'shanghai_gov_community_236',
      name: '朱家角镇沈巷社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_235',
      name: '朱家角镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_art_51',
      name: '朱屺瞻艺术馆'
    },
    {
      key: 'shanghai_gov_library_238',
      name: '朱泾镇图书馆'
    },
    {
      key: 'shanghai_gov_library_239',
      name: '朱泾镇图书馆新农分馆'
    },
    {
      key: 'shanghai_gov_community_194',
      name: '朱泾镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_195',
      name: '朱泾镇社区文化活动中心新农分中心'
    },
    {
      key: 'shanghai_gov_museum_103',
      name: '李白烈士故居'
    },
    {
      key: 'manual',
      name: '杨浦体育活动中心'
    },
    {
      key: 'manual',
      name: '杨浦区图书馆'
    },
    {
      key: 'shanghai_gov_library_148',
      name: '杨浦区图书馆（少儿分馆）'
    },
    {
      key: 'shanghai_gov_library_147',
      name: '杨浦区图书馆（平凉分馆）'
    },
    {
      key: 'manual',
      name: '杨浦区青少年活动中心'
    },
    {
      key: 'shanghai_gov_culture_15',
      name: '杨浦文化艺术中心'
    },
    {
      key: 'shanghai_gov_library_180',
      name: '杨行镇图书馆'
    },
    {
      key: 'shanghai_gov_community_155',
      name: '杨行镇社会事业发展服务中心'
    },
    {
      key: 'manual',
      name: '松江博物馆'
    },
    {
      key: 'manual',
      name: '松江文化馆'
    },
    {
      key: 'shanghai_gov_art_81',
      name: '松江美术馆'
    },
    {
      key: 'shanghai_gov_community_79',
      name: '枫林街道天龙党群服务中心(文化活动分中心)'
    },
    {
      key: 'shanghai_gov_community_78',
      name: '枫林街道社区党群服务中心(文化活动分中心)'
    },
    {
      key: 'shanghai_gov_library_98',
      name: '枫林路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_226',
      name: '枫泾镇图书馆'
    },
    {
      key: 'shanghai_gov_community_198',
      name: '枫泾镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_community_199',
      name: '枫泾镇社区文化活动中心兴塔分中心'
    },
    {
      key: 'shanghai_gov_library_286',
      name: '柘林镇图书馆'
    },
    {
      key: 'shanghai_gov_community_253',
      name: '柘林镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_105',
      name: '桃浦社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_131',
      name: '桃浦镇图书馆'
    },
    {
      key: 'shanghai_gov_theatre_95',
      name: '梅赛德斯-奔驰文化中心'
    },
    {
      key: 'shanghai_gov_theatre_96',
      name: '梅赛德斯-奔驰文化中心-音乐俱乐部'
    },
    {
      key: 'shanghai_gov_library_194',
      name: '梅陇镇图书馆'
    },
    {
      key: 'shanghai_gov_library_195',
      name: '梅陇镇图书馆晶城分馆'
    },
    {
      key: 'shanghai_gov_library_301',
      name: '横沙乡图书馆'
    },
    {
      key: 'shanghai_gov_community_265',
      name: '横沙乡社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_142',
      name: '欧阳路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_115',
      name: '欧阳路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_138',
      name: '殷行社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_163',
      name: '殷行街道图书馆'
    },
    {
      key: 'shanghai_gov_library_256',
      name: '永丰街道图书馆'
    },
    {
      key: 'shanghai_gov_community_211',
      name: '永丰街道社区党群服务中心'
    },
    {
      key: 'shanghai_gov_museum_174',
      name: '江南造船展示馆'
    },
    {
      key: 'shanghai_gov_library_78',
      name: '江宁路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_62',
      name: '江宁路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_63',
      name: '江宁路街道社区文化活动中心分中心'
    },
    {
      key: 'shanghai_gov_theatre_72',
      name: '江川剧场'
    },
    {
      key: 'shanghai_gov_community_165',
      name: '江川文化馆'
    },
    {
      key: 'shanghai_gov_library_213',
      name: '江桥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_188',
      name: '江桥镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_214',
      name: '江桥镇龙湖图书馆'
    },
    {
      key: 'shanghai_gov_community_134',
      name: '江浦社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_152',
      name: '江浦路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_153',
      name: '江浦路街道图书馆少儿分馆'
    },
    {
      key: 'shanghai_gov_community_135',
      name: '江浦路街道社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_library_139',
      name: '江湾镇街道图书馆'
    },
    {
      key: 'shanghai_gov_library_140',
      name: '江湾镇街道图书馆分馆（逸仙会客厅）'
    },
    {
      key: 'shanghai_gov_community_114',
      name: '江湾镇街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_117',
      name: '江苏路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_100',
      name: '江苏路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_museum_104',
      name: '沈尹默故居'
    },
    {
      key: 'shanghai_gov_library_51',
      name: '沪东社区图书馆'
    },
    {
      key: 'shanghai_gov_community_45',
      name: '沪东社区文化分中心'
    },
    {
      key: 'shanghai_gov_community_44',
      name: '沪东社区文化活动中心'
    },
    {
      key: 'shanghai_gov_museum_98',
      name: '沪西工人半日学校史料陈列馆'
    },
    {
      key: 'shanghai_gov_library_245',
      name: '泖港镇图书馆'
    },
    {
      key: 'shanghai_gov_community_226',
      name: '泖港镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_250',
      name: '泗泾新凯图书馆'
    },
    {
      key: 'shanghai_gov_library_251',
      name: '泗泾新凯大居图书馆'
    },
    {
      key: 'shanghai_gov_library_249',
      name: '泗泾镇图书馆'
    },
    {
      key: 'shanghai_gov_community_215',
      name: '泗泾镇新凯社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_214',
      name: '泗泾镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_theatre_156',
      name: '泥城影剧院'
    },
    {
      key: 'shanghai_gov_library_46',
      name: '泥城镇图书馆'
    },
    {
      key: 'shanghai_gov_community_5',
      name: '泥城镇文化服务中心'
    },
    {
      key: 'shanghai_gov_art_73',
      name: '泰美术馆'
    },
    {
      key: 'shanghai_gov_library_54',
      name: '洋泾社区图书馆'
    },
    {
      key: 'shanghai_gov_community_39',
      name: '洋泾社区文化活动中心'
    },
    {
      key: 'shanghai_gov_art_90',
      name: '洙桥美术馆'
    },
    {
      key: 'shanghai_gov_library_242',
      name: '洞泾镇图书馆'
    },
    {
      key: 'shanghai_gov_community_222',
      name: '洞泾镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_art_7',
      name: '浦东云间美术馆'
    },
    {
      key: 'manual',
      name: '浦东体育公园'
    },
    {
      key: 'manual',
      name: '浦东博物馆'
    },
    {
      key: 'shanghai_gov_museum_3',
      name: '浦东历史博物馆'
    },
    {
      key: 'manual',
      name: '浦东新区图书馆'
    },
    {
      key: 'shanghai_gov_culture_2',
      name: '浦东新区文化艺术指导中心'
    },
    {
      key: 'shanghai_gov_culture_4',
      name: '浦东新区文化艺术指导中心外高桥分中心'
    },
    {
      key: 'shanghai_gov_culture_3',
      name: '浦东新区文化艺术指导中心惠南分中心'
    },
    {
      key: 'shanghai_gov_culture_6',
      name: '浦东新区浦东文化馆'
    },
    {
      key: 'shanghai_gov_culture_7',
      name: '浦东新区浦南文化馆'
    },
    {
      key: 'shanghai_gov_culture_5',
      name: '浦东新区金海文化艺术中心'
    },
    {
      key: 'manual',
      name: '浦东新区青少年活动中心'
    },
    {
      key: '浦东美术馆',
      name: '浦东美术馆'
    },
    {
      key: 'shanghai_gov_community_21',
      name: '浦兴社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_22',
      name: '浦兴社区文化活动中心金桥湾分中心'
    },
    {
      key: 'shanghai_gov_library_42',
      name: '浦兴路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_43',
      name: '浦兴路街道图书馆金桥湾分馆'
    },
    {
      key: 'shanghai_gov_library_196',
      name: '浦江图书馆'
    },
    {
      key: 'shanghai_gov_library_197',
      name: '浦江镇图书馆永康分馆'
    },
    {
      key: 'shanghai_gov_community_173',
      name: '浦江镇瑞和社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_171',
      name: '浦江镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_172',
      name: '浦江镇青少年社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_204',
      name: '浦锦街道图书馆'
    },
    {
      key: 'shanghai_gov_community_179',
      name: '浦锦街道社区党群服务中心（文化体育）'
    },
    {
      key: 'shanghai_gov_theatre_42',
      name: '海上文化管理中心-大宁剧院'
    },
    {
      key: 'shanghai_gov_theatre_155',
      name: '海昌海洋公园-大型动物表演场'
    },
    {
      key: 'shanghai_gov_theatre_153',
      name: '海昌海洋公园-欢乐剧场'
    },
    {
      key: 'shanghai_gov_theatre_154',
      name: '海昌海洋公园-海豚表演场'
    },
    {
      key: 'shanghai_gov_art_5',
      name: '海派连环画艺术馆'
    },
    {
      key: 'shanghai_gov_library_291',
      name: '海湾旅游区图书馆'
    },
    {
      key: 'shanghai_gov_community_260',
      name: '海湾旅游区社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_281',
      name: '海湾镇图书馆'
    },
    {
      key: 'shanghai_gov_community_257',
      name: '海湾镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_178',
      name: '淞南镇图书馆'
    },
    {
      key: 'shanghai_gov_community_158',
      name: '淞南镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_53',
      name: '淮海中路社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_61',
      name: '淮海中路街道图书馆'
    },
    {
      key: '上海本地宝',
      name: '淮海路'
    },
    {
      key: 'shanghai_gov_library_300',
      name: '港沿镇图书馆'
    },
    {
      key: 'shanghai_gov_community_269',
      name: '港沿镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_299',
      name: '港西镇图书馆'
    },
    {
      key: 'shanghai_gov_community_268',
      name: '港西镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_community_77',
      name: '湖南街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_97',
      name: '湖南路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_106',
      name: '漕河泾街道图书馆'
    },
    {
      key: 'shanghai_gov_library_107',
      name: '漕河泾街道图书馆 石龙分馆'
    },
    {
      key: 'shanghai_gov_community_87',
      name: '漕河泾街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_225',
      name: '漕泾镇图书馆'
    },
    {
      key: 'shanghai_gov_community_197',
      name: '漕泾镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_community_36',
      name: '潍坊社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_18',
      name: '潍坊街道图书馆'
    },
    {
      key: '上海本地宝',
      name: '环球金融中心'
    },
    {
      key: 'shanghai_gov_community_52',
      name: '瑞金二路社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_63',
      name: '瑞金二路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_103',
      name: '甘泉社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_129',
      name: '甘泉街道图书馆'
    },
    {
      key: 'shanghai_gov_community_81',
      name: '田林街道党群服务中心'
    },
    {
      key: 'shanghai_gov_library_100',
      name: '田林街道图书馆'
    },
    {
      key: 'shanghai_gov_library_262',
      name: '白鹤镇图书馆'
    },
    {
      key: 'shanghai_gov_library_263',
      name: '白鹤镇图书馆（赵屯分中心）'
    },
    {
      key: 'shanghai_gov_community_233',
      name: '白鹤镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_234',
      name: '白鹤镇社区文化活动中心（赵屯分中心）'
    },
    {
      key: 'shanghai_gov_library_278',
      name: '盈浦街道图书馆'
    },
    {
      key: 'shanghai_gov_community_244',
      name: '盈浦街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_106',
      name: '真如社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_133',
      name: '真如镇街道图书馆'
    },
    {
      key: 'shanghai_gov_library_222',
      name: '真新街道图书馆'
    },
    {
      key: 'shanghai_gov_library_223',
      name: '真新街道图书馆（新丰分馆）'
    },
    {
      key: 'shanghai_gov_community_186',
      name: '真新街道社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_235',
      name: '石化街道图书馆'
    },
    {
      key: 'shanghai_gov_community_208',
      name: '石化街道社区党群服务中心'
    },
    {
      key: 'shanghai_gov_community_108',
      name: '石泉社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_130',
      name: '石泉路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_248',
      name: '石湖荡镇图书馆'
    },
    {
      key: 'shanghai_gov_community_225',
      name: '石湖荡镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_59',
      name: '石门二路社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_82',
      name: '石门二路街道图书馆'
    },
    {
      key: 'shanghai_gov_library_40',
      name: '祝桥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_17',
      name: '祝桥镇文化服务中心'
    },
    {
      key: 'shanghai_gov_art_80',
      name: '程十发艺术馆'
    },
    {
      key: 'shanghai_gov_library_113',
      name: '程家桥街道图书馆'
    },
    {
      key: 'shanghai_gov_community_96',
      name: '程家桥街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_306',
      name: '竖新镇图书馆'
    },
    {
      key: 'shanghai_gov_community_264',
      name: '竖新镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_museum_41',
      name: '童涵春堂中药博物馆'
    },
    {
      key: 'shanghai_gov_theatre_64',
      name: '精武体育馆'
    },
    {
      key: 'shanghai_gov_theatre_79',
      name: '索石文化传播（上海）有限公司'
    },
    {
      key: 'shanghai_gov_theatre_85',
      name: '练塘影剧院'
    },
    {
      key: 'shanghai_gov_library_267',
      name: '练塘镇图书馆'
    },
    {
      key: 'shanghai_gov_community_230',
      name: '练塘镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_231',
      name: '练塘镇社区文化活动中心（小蒸分中心）'
    },
    {
      key: 'shanghai_gov_community_232',
      name: '练塘镇社区文化活动中心（蒸淀分中心）'
    },
    {
      key: 'shanghai_gov_library_303',
      name: '绿华镇图书馆'
    },
    {
      key: 'shanghai_gov_community_271',
      name: '绿华镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_172',
      name: '罗店镇图书馆'
    },
    {
      key: 'shanghai_gov_library_173',
      name: '罗店镇图书馆（塘西街分馆）'
    },
    {
      key: 'shanghai_gov_library_174',
      name: '罗店镇图书馆（美兰西湖分馆）'
    },
    {
      key: 'shanghai_gov_community_141',
      name: '罗店镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_142',
      name: '罗店镇社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_library_175',
      name: '罗泾镇图书馆'
    },
    {
      key: 'shanghai_gov_library_176',
      name: '罗泾镇图书馆分馆'
    },
    {
      key: 'shanghai_gov_community_150',
      name: '罗泾镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_151',
      name: '罗泾镇社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_library_41',
      name: '老港镇图书馆'
    },
    {
      key: 'shanghai_gov_community_25',
      name: '老港镇文化服务中心'
    },
    {
      key: 'shanghai_gov_community_58',
      name: '老西门社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_68',
      name: '老西门街道图书馆'
    },
    {
      key: 'shanghai_gov_art_20',
      name: '胡问遂艺术馆'
    },
    {
      key: 'shanghai_gov_library_49',
      name: '航头镇图书馆'
    },
    {
      key: 'shanghai_gov_library_50',
      name: '航头镇图书馆鹤沙分馆'
    },
    {
      key: 'shanghai_gov_community_27',
      name: '航头镇文化服务中心'
    },
    {
      key: 'shanghai_gov_community_28',
      name: '航头镇文化服务中心鹤沙分中心'
    },
    {
      key: 'shanghai_gov_library_23',
      name: '花木街道图书馆'
    },
    {
      key: 'shanghai_gov_community_15',
      name: '花木街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_93',
      name: '芷江西路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_72',
      name: '芷江西路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_museum_95',
      name: '苏州河工业文明展示馆'
    },
    {
      key: 'shanghai_gov_library_201',
      name: '莘庄工业区图书馆'
    },
    {
      key: 'shanghai_gov_community_170',
      name: '莘庄工业区文化体育事业发展中心'
    },
    {
      key: 'shanghai_gov_library_202',
      name: '莘庄镇图书馆'
    },
    {
      key: 'shanghai_gov_community_175',
      name: '莘庄镇文化体育事业发展中心'
    },
    {
      key: 'shanghai_gov_library_215',
      name: '菊园新区图书馆'
    },
    {
      key: 'shanghai_gov_community_182',
      name: '菊园新区社区文化活动中心'
    },
    {
      key: 'shanghai_gov_museum_156',
      name: '董其昌书画艺术博物馆'
    },
    {
      key: 'shanghai_gov_art_63',
      name: '蔡兵美术馆'
    },
    {
      key: 'shanghai_gov_library_134',
      name: '虹口区图书馆'
    },
    {
      key: 'shanghai_gov_library_136',
      name: '虹口区图书馆和平分馆'
    },
    {
      key: 'shanghai_gov_library_135',
      name: '虹口区图书馆曲阳分馆'
    },
    {
      key: 'shanghai_gov_theatre_62',
      name: '虹口区工人文化宫'
    },
    {
      key: 'shanghai_gov_culture_14',
      name: '虹口区文化馆'
    },
    {
      key: 'shanghai_gov_theatre_60',
      name: '虹口区曲阳文化馆'
    },
    {
      key: 'shanghai_gov_theatre_58',
      name: '虹口足球场'
    },
    {
      key: 'shanghai_gov_library_114',
      name: '虹桥街道图书馆'
    },
    {
      key: 'shanghai_gov_library_115',
      name: '虹桥街道图书馆分馆（古北天空书苑）'
    },
    {
      key: 'shanghai_gov_community_97',
      name: '虹桥街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_98',
      name: '虹桥街道社区文化活动中心（分中心）'
    },
    {
      key: 'shanghai_gov_library_190',
      name: '虹桥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_163',
      name: '虹桥镇文化体育事业发展中心'
    },
    {
      key: 'shanghai_gov_community_83',
      name: '虹梅街道党群服务中心'
    },
    {
      key: 'shanghai_gov_library_102',
      name: '虹梅路街道图书馆'
    },
    {
      key: 'shanghai_gov_museum_80',
      name: '衡复风貌博物馆群'
    },
    {
      key: 'shanghai_gov_art_35',
      name: '西岸美术馆'
    },
    {
      key: 'shanghai_gov_library_289',
      name: '西渡街道图书馆'
    },
    {
      key: 'shanghai_gov_community_262',
      name: '西渡街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_57',
      name: '豫园社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_67',
      name: '豫园街道图书馆'
    },
    {
      key: 'shanghai_gov_library_271',
      name: '赵巷镇图书馆'
    },
    {
      key: 'shanghai_gov_library_272',
      name: '赵巷镇图书馆（新城一站分馆）'
    },
    {
      key: 'shanghai_gov_community_241',
      name: '赵巷镇新城一站大居社区文化体育服务中心'
    },
    {
      key: 'shanghai_gov_community_240',
      name: '赵巷镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_art_54',
      name: '趣看美术馆'
    },
    {
      key: 'shanghai_gov_library_241',
      name: '车墩镇图书馆'
    },
    {
      key: 'shanghai_gov_community_218',
      name: '车墩镇社区文化活动中心'
    },
    {
      key: '上海本地宝',
      name: '辰山植物园'
    },
    {
      key: 'shanghai_gov_theatre_124',
      name: '迪士尼-凡迭戈剧院、林间剧场、故事舞台'
    },
    {
      key: 'shanghai_gov_theatre_123',
      name: '迪士尼-大剧院'
    },
    {
      key: 'shanghai_gov_library_274',
      name: '重固镇图书馆'
    },
    {
      key: 'shanghai_gov_community_237',
      name: '重固镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_museum_148',
      name: '金山区博物馆'
    },
    {
      key: 'shanghai_gov_library_224',
      name: '金山区图书馆'
    },
    {
      key: 'shanghai_gov_culture_20',
      name: '金山区文化馆'
    },
    {
      key: 'shanghai_gov_library_228',
      name: '金山卫镇图书馆'
    },
    {
      key: 'shanghai_gov_library_229',
      name: '金山卫镇图书馆钱圩分馆'
    },
    {
      key: 'shanghai_gov_community_204',
      name: '金山卫镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_community_205',
      name: '金山卫镇社区文化活动中心钱圩分中心'
    },
    {
      key: 'shanghai_gov_library_19',
      name: '金杨新村街道图书馆'
    },
    {
      key: 'shanghai_gov_community_6',
      name: '金杨社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_7',
      name: '金杨社区文化活动中心云山路分中心'
    },
    {
      key: 'shanghai_gov_library_55',
      name: '金桥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_10',
      name: '金桥镇文化服务中心'
    },
    {
      key: 'shanghai_gov_library_282',
      name: '金汇镇图书馆'
    },
    {
      key: 'shanghai_gov_community_248',
      name: '金汇镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_249',
      name: '金汇镇社区文化活动中心泰日分中心'
    },
    {
      key: 'shanghai_gov_library_266',
      name: '金泽镇图书馆'
    },
    {
      key: 'shanghai_gov_community_242',
      name: '金泽镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_243',
      name: '金泽镇社区文化活动服务中心商榻分中心'
    },
    {
      key: 'shanghai_gov_library_290',
      name: '金海街道图书馆'
    },
    {
      key: 'shanghai_gov_community_259',
      name: '金海街道社区文化活动中心'
    },
    {
      key: '上海本地宝',
      name: '金茂大厦'
    },
    {
      key: 'shanghai_gov_museum_77',
      name: '钱学森图书馆'
    },
    {
      key: 'shanghai_gov_library_295',
      name: '长兴镇图书馆'
    },
    {
      key: 'shanghai_gov_community_280',
      name: '长兴镇社区党群服务中心'
    },
    {
      key: 'shanghai_gov_library_111',
      name: '长宁区图书馆（仙霞馆）'
    },
    {
      key: 'shanghai_gov_library_109',
      name: '长宁区图书馆（天山馆）'
    },
    {
      key: 'shanghai_gov_library_110',
      name: '长宁区图书馆（愚园馆）'
    },
    {
      key: 'shanghai_gov_culture_10',
      name: '长宁文化艺术中心'
    },
    {
      key: 'shanghai_gov_community_107',
      name: '长寿社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_126',
      name: '长寿路街道图书馆'
    },
    {
      key: 'shanghai_gov_community_101',
      name: '长征社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_128',
      name: '长征镇图书馆'
    },
    {
      key: 'shanghai_gov_community_82',
      name: '长桥社区文化活动中心'
    },
    {
      key: 'shanghai_gov_library_101',
      name: '长桥街道图书馆'
    },
    {
      key: 'shanghai_gov_library_161',
      name: '长海路街道图书馆（市光路馆）'
    },
    {
      key: 'shanghai_gov_library_159',
      name: '长海路街道图书馆（政府路馆）'
    },
    {
      key: 'shanghai_gov_library_160',
      name: '长海路街道图书馆（翔殷路馆）'
    },
    {
      key: 'shanghai_gov_community_130',
      name: '长海路街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_131',
      name: '长海路街道社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_library_149',
      name: '长白新村街道图书馆'
    },
    {
      key: 'shanghai_gov_community_128',
      name: '长白新村街道社区文化活动中心'
    },
    {
      key: '上海本地宝',
      name: '长风公园'
    },
    {
      key: 'shanghai_gov_library_125',
      name: '长风新村街道图书馆'
    },
    {
      key: '上海本地宝',
      name: '长风海洋世界'
    },
    {
      key: 'shanghai_gov_community_104',
      name: '长风社区文化活动中心'
    },
    {
      key: 'manual',
      name: '闵行体育公园文体中心'
    },
    {
      key: 'shanghai_gov_museum_131',
      name: '闵行区博物馆'
    },
    {
      key: 'manual',
      name: '闵行区图书馆'
    },
    {
      key: 'shanghai_gov_community_178',
      name: '闵行区梅陇镇文化体育事业发展中心'
    },
    {
      key: 'manual',
      name: '闵行区青少年活动中心'
    },
    {
      key: 'manual',
      name: '闵行博物馆'
    },
    {
      key: 'shanghai_gov_art_70',
      name: '陆俨少艺术院'
    },
    {
      key: '上海本地宝',
      name: '陆家嘴'
    },
    {
      key: 'shanghai_gov_library_52',
      name: '陆家嘴街道图书馆'
    },
    {
      key: 'shanghai_gov_community_30',
      name: '陆家嘴金融城文化中心'
    },
    {
      key: 'shanghai_gov_community_31',
      name: '陆家嘴金融城文化分中心'
    },
    {
      key: 'shanghai_gov_museum_160',
      name: '陈云纪念馆'
    },
    {
      key: 'shanghai_gov_library_296',
      name: '陈家镇图书馆'
    },
    {
      key: 'shanghai_gov_community_279',
      name: '陈家镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_art_16',
      name: '震旦美术馆'
    },
    {
      key: 'shanghai_gov_library_284',
      name: '青村镇图书馆'
    },
    {
      key: 'shanghai_gov_community_251',
      name: '青村镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_252',
      name: '青村镇社区文化活动中心钱桥分中心'
    },
    {
      key: 'shanghai_gov_museum_159',
      name: '青浦区博物馆'
    },
    {
      key: 'shanghai_gov_library_261',
      name: '青浦区图书馆'
    },
    {
      key: 'shanghai_gov_culture_22',
      name: '青浦区文化馆'
    },
    {
      key: 'shanghai_gov_theatre_82',
      name: '青浦区赵巷镇文化中心站'
    },
    {
      key: 'shanghai_gov_theatre_84',
      name: '青浦朱家角影剧院'
    },
    {
      key: 'shanghai_gov_theatre_83',
      name: '青浦重固影剧院'
    },
    {
      key: 'shanghai_gov_library_273',
      name: '青溪书房·赵巷公园'
    },
    {
      key: 'shanghai_gov_theatre_89',
      name: '青隐（上海）文化艺术发展有限公司'
    },
    {
      key: 'shanghai_gov_theatre_35',
      name: '静安体育中心'
    },
    {
      key: 'shanghai_gov_library_77',
      name: '静安区图书馆北站街道分馆'
    },
    {
      key: 'shanghai_gov_library_70',
      name: '静安区图书馆（天目中路）'
    },
    {
      key: 'shanghai_gov_library_69',
      name: '静安区图书馆（新闸路）'
    },
    {
      key: 'shanghai_gov_library_71',
      name: '静安区图书馆（闻喜路）'
    },
    {
      key: 'shanghai_gov_library_72',
      name: '静安区少年儿童图书馆'
    },
    {
      key: 'shanghai_gov_culture_12',
      name: '静安区文化馆'
    },
    {
      key: 'shanghai_gov_culture_13',
      name: '静安区文化馆分馆'
    },
    {
      key: 'shanghai_gov_library_73',
      name: '静安区闸北少年儿童图书馆'
    },
    {
      key: 'shanghai_gov_library_79',
      name: '静安寺街道图书馆'
    },
    {
      key: 'shanghai_gov_community_66',
      name: '静安寺街道社区文化活动中心'
    },
    {
      key: '上海本地宝',
      name: '静安雕塑公园'
    },
    {
      key: 'shanghai_gov_library_168',
      name: '顾村镇图书馆'
    },
    {
      key: 'shanghai_gov_library_171',
      name: '顾村镇图书馆（菊泉分馆）'
    },
    {
      key: 'shanghai_gov_library_169',
      name: '顾村镇图书馆（诗乡广场分馆）'
    },
    {
      key: 'shanghai_gov_library_170',
      name: '顾村镇图书馆（馨佳园分馆）'
    },
    {
      key: 'shanghai_gov_community_147',
      name: '顾村镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_148',
      name: '顾村镇菊泉文体中心'
    },
    {
      key: 'shanghai_gov_community_149',
      name: '顾村镇馨佳园社区文化活动中心'
    },
    {
      key: 'shanghai_gov_museum_94',
      name: '顾正红纪念馆'
    },
    {
      key: 'shanghai_gov_museum_142',
      name: '顾维钧生平陈列馆'
    },
    {
      key: 'shanghai_gov_library_203',
      name: '颛桥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_164',
      name: '颛桥镇文体中心'
    },
    {
      key: 'shanghai_gov_library_276',
      name: '香花桥街道图书馆'
    },
    {
      key: 'shanghai_gov_library_277',
      name: '香花桥街道图书馆 （玉兰花园分馆）'
    },
    {
      key: 'shanghai_gov_community_247',
      name: '香花桥街道清河湾U365党群服务中心（社区文化活动分中心）'
    },
    {
      key: 'shanghai_gov_community_246',
      name: '香花桥街道社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_168',
      name: '马桥景城文化中心'
    },
    {
      key: 'shanghai_gov_library_193',
      name: '马桥镇图书馆'
    },
    {
      key: 'shanghai_gov_library_216',
      name: '马陆镇图书馆'
    },
    {
      key: 'shanghai_gov_community_190',
      name: '马陆镇文化体育服务中心'
    },
    {
      key: 'shanghai_gov_library_25',
      name: '高东镇图书馆'
    },
    {
      key: 'shanghai_gov_community_23',
      name: '高东镇文化服务中心'
    },
    {
      key: 'shanghai_gov_library_167',
      name: '高境镇图书馆'
    },
    {
      key: 'shanghai_gov_community_153',
      name: '高境镇社区文化活动中心'
    },
    {
      key: 'shanghai_gov_community_154',
      name: '高境镇社区文化活动分中心'
    },
    {
      key: 'shanghai_gov_library_227',
      name: '高新区图书馆'
    },
    {
      key: 'shanghai_gov_community_203',
      name: '高新区社区文化活动中心'
    },
    {
      key: 'shanghai_gov_museum_6',
      name: '高桥历史文化陈列馆'
    },
    {
      key: 'shanghai_gov_library_26',
      name: '高桥镇图书馆'
    },
    {
      key: 'shanghai_gov_community_46',
      name: '高桥镇文化服务中心'
    },
    {
      key: 'shanghai_gov_library_27',
      name: '高行镇图书馆'
    },
    {
      key: 'shanghai_gov_community_32',
      name: '高行镇文化服务中心'
    },
    {
      key: 'shanghai_gov_art_56',
      name: '鸿一美术馆'
    },
    {
      key: 'shanghai_gov_library_57',
      name: '黄浦区图书馆'
    },
    {
      key: 'shanghai_gov_culture_8',
      name: '黄浦区文化馆'
    },
    {
      key: 'shanghai_gov_library_58',
      name: '黄浦区明复图书馆(原卢湾区图书馆)'
    },
    {
      key: 'shanghai_gov_museum_1',
      name: '黄炎培故居'
    },
    {
      key: 'shanghai_gov_museum_65',
      name: '黄道婆纪念馆'
    },
    {
      key: 'shanghai_gov_community_85',
      name: '龙华社区党群中心'
    },
    {
      key: 'shanghai_gov_library_104',
      name: '龙华街道图书馆'
    },
    {
      key: 'shanghai_gov_art_36',
      name: '龙美术馆（西岸馆）'
    }
  ],
  beijing: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: 'beijing_gov_whlyj_street_116',
      name: 'nan'
    },
    {
      key: 'beijing_gov_wwj_545784',
      name: '万寿寺博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_81',
      name: '万寿路街道文化活动中心'
    },
    {
      key: '三山五园文化艺术中心',
      name: '三山五园文化艺术中心'
    },
    {
      key: '北京本地宝',
      name: '三里屯'
    },
    {
      key: 'manual',
      name: '三里屯太古里北区下沉广场'
    },
    {
      key: 'beijing_gov_whlyj_street_42',
      name: '三里屯街道'
    },
    {
      key: 'beijing_gov_whlyj_street_69',
      name: '三间房地区'
    },
    {
      key: 'beijing_gov_whlyj_street_106',
      name: '上地街道图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_105',
      name: '上地街道文化活动中心'
    },
    {
      key: 'beijing_gov_wwj_545874',
      name: '上宅文化陈列馆'
    },
    {
      key: 'beijing_gov_whlyj_street_121',
      name: '上庄镇市民活动中心（北京市海淀区上庄镇党群活动中心）'
    },
    {
      key: '北京本地宝',
      name: '世界公园'
    },
    {
      key: 'beijing_gov_whlyj_street_113',
      name: '东升镇东部文化活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_114',
      name: '东升镇北部活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_112',
      name: '东升镇南部文化活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_6',
      name: '东华门街道图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_5',
      name: '东华门街道综合文化中心'
    },
    {
      key: 'beijing_gov_tyj_3',
      name: '东单体育中心'
    },
    {
      key: 'beijing_gov_whlyj_street_9',
      name: '东四街道市民活动中心'
    },
    {
      key: 'beijing_gov_whlyj_perf_29',
      name: '东图会议中心剧场'
    },
    {
      key: 'beijing_gov_whlyj_street_70',
      name: '东坝地区'
    },
    {
      key: 'manual',
      name: '东城区图书馆'
    },
    {
      key: 'manual',
      name: '东城区文化馆'
    },
    {
      key: 'manual',
      name: '东小口森林公园'
    },
    {
      key: 'beijing_gov_whlyj_street_282',
      name: '东小口镇'
    },
    {
      key: 'beijing_gov_whlyj_street_49',
      name: '东湖街道'
    },
    {
      key: 'beijing_gov_whlyj_street_11',
      name: '东直门街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_18',
      name: '东花市街道图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_17',
      name: '东花市街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_158',
      name: '东辛房街道'
    },
    {
      key: 'beijing_gov_whlyj_street_145',
      name: '东铁匠营街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_78',
      name: '东风地区'
    },
    {
      key: 'beijing_gov_whlyj_street_195',
      name: '东风街道'
    },
    {
      key: 'beijing_gov_whlyj_street_126',
      name: '东高地街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_303',
      name: '东高村镇'
    },
    {
      key: 'beijing_gov_whlyj_street_210',
      name: '中仓街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_94',
      name: '中关村街道图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_93',
      name: '中关村街道综合文化活动中心'
    },
    {
      key: 'centuryaltar',
      name: '中华世纪坛'
    },
    {
      key: 'beijing_gov_wwj_546018',
      name: '中华世纪坛艺术馆'
    },
    {
      key: 'beijing_gov_wwj_546129',
      name: '中国人民大学博物馆'
    },
    {
      key: 'beijing_gov_wwj_546210',
      name: '中国人民大学家书博物馆'
    },
    {
      key: '中国人民革命军事博物馆',
      name: '中国人民革命军事博物馆'
    },
    {
      key: 'beijing_gov_wwj_546174',
      name: '中国传媒大学传媒博物馆'
    },
    {
      key: 'beijing_gov_wwj_545811',
      name: '中国佛教图书文物馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_44',
      name: '中国儿童中心剧场'
    },
    {
      key: 'beijing_gov_whlyj_perf_8',
      name: '中国儿童剧场'
    },
    {
      key: 'beijing_gov_wwj_325880511',
      name: '中国共产党历史展览馆'
    },
    {
      key: 'beijing_gov_wwj_11077342',
      name: '中国共产党早期北京革命活动纪念馆'
    },
    {
      key: '北京本地宝',
      name: '中国军事博物馆'
    },
    {
      key: 'beijing_gov_wwj_545748',
      name: '中国农业博物馆'
    },
    {
      key: 'beijing_gov_wwj_546147',
      name: '中国化工博物馆'
    },
    {
      key: 'beijing_gov_wwj_546213',
      name: '中国华侨历史博物馆'
    },
    {
      key: 'beijing_gov_wwj_545886',
      name: '中国印刷博物馆'
    },
    {
      key: '北京本地宝',
      name: '中国古动物馆'
    },
    {
      key: '北京本地宝',
      name: '中国园林博物馆'
    },
    {
      key: 'chnmuseum',
      name: '中国国家博物馆'
    },
    {
      key: 'beijing_gov_wwj_545919',
      name: '中国国家画院美术馆'
    },
    {
      key: '北京本地宝',
      name: '中国地质博物馆'
    },
    {
      key: '北京本地宝',
      name: '中国妇女儿童博物馆'
    },
    {
      key: 'beijing_gov_wwj_545889',
      name: '中国工艺美术馆（中国非物质文化遗产馆）'
    },
    {
      key: 'beijing_gov_wwj_743627813',
      name: '中国木偶艺术剧院博物馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_24',
      name: '中国木偶艺术剧院大厅'
    },
    {
      key: 'beijing_gov_whlyj_perf_25',
      name: '中国木偶艺术剧院小铃铛剧场'
    },
    {
      key: 'beijing_gov_wwj_546114',
      name: '中国法院博物馆'
    },
    {
      key: 'beijing_gov_wwj_546186',
      name: '中国海关博物馆'
    },
    {
      key: '北京本地宝',
      name: '中国消防博物馆'
    },
    {
      key: 'beijing_gov_wwj_545952',
      name: '中国现代文学馆'
    },
    {
      key: 'beijing_gov_wwj_545982',
      name: '中国电信博物馆'
    },
    {
      key: '中国电影博物馆',
      name: '中国电影博物馆'
    },
    {
      key: '北京本地宝',
      name: '中国科学技术馆'
    },
    {
      key: '北京本地宝',
      name: '中国科学技术馆儿童科学乐园'
    },
    {
      key: '北京本地宝',
      name: '中国科技馆'
    },
    {
      key: 'beijing_gov_wwj_545880',
      name: '中国第四纪冰川遗迹陈列馆'
    },
    {
      key: '北京本地宝',
      name: '中国美术馆'
    },
    {
      key: '北京本地宝',
      name: '中国考古博物馆'
    },
    {
      key: 'beijing_gov_wwj_545754',
      name: '中国航天博物馆'
    },
    {
      key: '北京本地宝',
      name: '中国航空博物馆'
    },
    {
      key: 'beijing_gov_wwj_545955',
      name: '中国蜜蜂博物馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_26',
      name: '中国评剧大剧院大剧场'
    },
    {
      key: 'beijing_gov_whlyj_perf_27',
      name: '中国评剧大剧院小剧场'
    },
    {
      key: '北京本地宝',
      name: '中国邮政邮票博物馆'
    },
    {
      key: 'beijing_gov_wwj_545943',
      name: '中国钱币博物馆'
    },
    {
      key: 'beijing_gov_wwj_546048',
      name: '中国铁道博物馆正阳门展馆'
    },
    {
      key: '北京本地宝',
      name: '中国铁道博物馆正阳门馆'
    },
    {
      key: 'beijing_gov_wwj_546045',
      name: '中国铁道博物馆（东郊展馆）'
    },
    {
      key: 'beijing_gov_wwj_545847',
      name: '中央民族大学民族博物馆'
    },
    {
      key: 'beijing_gov_wwj_545853',
      name: '中央美术学院美术馆'
    },
    {
      key: '北京本地宝',
      name: '中山公园'
    },
    {
      key: '中山公园音乐堂',
      name: '中山公园音乐堂'
    },
    {
      key: 'beijing_gov_tyj_16',
      name: '丰台体育中心'
    },
    {
      key: 'manual',
      name: '丰台区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_14',
      name: '丰台区图书馆
（北大地馆）'
    },
    {
      key: 'beijing_gov_whlyj_lib_15',
      name: '丰台区图书馆
（大红门馆）'
    },
    {
      key: 'beijing_gov_whlyj_street_128',
      name: '丰台区太平桥街道市民活动中心'
    },
    {
      key: 'beijing_gov_whlyj_cc_6',
      name: '丰台区文化馆'
    },
    {
      key: 'beijing_gov_whlyj_street_129',
      name: '丰台区新村街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_137',
      name: '丰台区王佐镇文化服务中心'
    },
    {
      key: 'beijing_gov_whlyj_street_123',
      name: '丰台区青塔街道综合文化中心'
    },
    {
      key: 'manual',
      name: '丰台区青少年宫'
    },
    {
      key: 'beijing_gov_whlyj_street_131',
      name: '丰台街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_202',
      name: '临河里街道综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '乐高探索中心'
    },
    {
      key: 'beijing_gov_whlyj_street_200',
      name: '九棵树街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_323',
      name: '九渡河综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_206',
      name: '于家务回族乡综合文化中心'
    },
    {
      key: 'manual',
      name: '云居城市休闲公园'
    },
    {
      key: '北京本地宝',
      name: '云居寺'
    },
    {
      key: 'beijing_gov_whlyj_street_138',
      name: '云岗街道综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '五棵松体育馆'
    },
    {
      key: 'beijing_gov_whlyj_street_155',
      name: '五里坨街道'
    },
    {
      key: 'beijing_gov_whlyj_street_359',
      name: '井庄镇'
    },
    {
      key: 'beijing_gov_whlyj_street_40',
      name: '亚运村街道'
    },
    {
      key: 'beijing_gov_whlyj_street_3',
      name: '交道口街道综合文化中心'
    },
    {
      key: 'manual',
      name: '亦庄滨河森林公园'
    },
    {
      key: 'beijing_gov_whlyj_street_275',
      name: '亦庄镇'
    },
    {
      key: 'beijing_gov_wwj_743627969',
      name: '京东方历史展览馆'
    },
    {
      key: 'manual',
      name: '亮马河滨水步道'
    },
    {
      key: 'beijing_gov_whlyj_perf_6',
      name: '人艺实验剧场'
    },
    {
      key: '北京本地宝',
      name: '什刹海'
    },
    {
      key: 'beijing_gov_whlyj_street_23',
      name: '什刹海街道'
    },
    {
      key: 'beijing_gov_whlyj_street_228',
      name: '仁和镇'
    },
    {
      key: '北京本地宝',
      name: '今日美术馆'
    },
    {
      key: 'beijing_gov_whlyj_street_16',
      name: '体育馆路街道综合文化中心'
    },
    {
      key: 'beijing_gov_wwj_545940',
      name: '何扬·吴茜现代绘画馆'
    },
    {
      key: 'beijing_gov_whlyj_street_186',
      name: '佛子庄乡'
    },
    {
      key: 'beijing_gov_whlyj_perf_17',
      name: '保利剧院'
    },
    {
      key: 'beijing_gov_wwj_546003',
      name: '保利艺术博物馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_9',
      name: '假日经典小剧场'
    },
    {
      key: 'beijing_gov_whlyj_street_364',
      name: '儒林街道'
    },
    {
      key: '北京本地宝',
      name: '元大都城垣遗址公园'
    },
    {
      key: 'beijing_gov_whlyj_street_242',
      name: '光明街道'
    },
    {
      key: 'beijing_gov_wwj_743627928',
      name: '全聚德博物馆'
    },
    {
      key: '北京本地宝',
      name: '八大处公园'
    },
    {
      key: 'beijing_gov_whlyj_street_150',
      name: '八宝山街道'
    },
    {
      key: 'beijing_gov_whlyj_street_151',
      name: '八角街道'
    },
    {
      key: 'beijing_gov_whlyj_street_357',
      name: '八达岭镇'
    },
    {
      key: '北京本地宝',
      name: '八达岭长城'
    },
    {
      key: 'beijing_gov_whlyj_street_57',
      name: '八里庄街道'
    },
    {
      key: 'beijing_gov_whlyj_street_85',
      name: '八里庄街道党群文化中心（慧美党群服务中心）'
    },
    {
      key: 'beijing_gov_whlyj_street_86',
      name: '八里庄街道图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_48',
      name: '六里屯街道'
    },
    {
      key: 'beijing_gov_whlyj_street_250',
      name: '兴丰街道'
    },
    {
      key: 'beijing_gov_whlyj_street_298',
      name: '兴寿镇'
    },
    {
      key: 'beijing_gov_whlyj_street_317',
      name: '兴谷街道'
    },
    {
      key: 'beijing_gov_wwj_545970',
      name: '冀热察挺进军司令部旧址陈列馆'
    },
    {
      key: 'beijing_gov_whlyj_street_163',
      name: '军庄镇'
    },
    {
      key: '北京本地宝',
      name: '凤凰岭自然风景区'
    },
    {
      key: 'beijing_gov_whlyj_street_309',
      name: '刘家店镇'
    },
    {
      key: 'beijing_gov_whlyj_street_362',
      name: '刘斌堡乡'
    },
    {
      key: 'beijing_gov_whlyj_perf_31',
      name: '刘老根大舞台'
    },
    {
      key: '北京本地宝',
      name: '前门大街'
    },
    {
      key: 'beijing_gov_whlyj_perf_34',
      name: '前门梨园剧场'
    },
    {
      key: 'beijing_gov_whlyj_street_12',
      name: '前门街道市民活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_56',
      name: '劲松街道'
    },
    {
      key: '北京本地宝',
      name: '劳动人民文化宫'
    },
    {
      key: 'beijing_gov_whlyj_street_283',
      name: '北七家镇'
    },
    {
      key: 'beijing_gov_whlyj_street_89',
      name: '北下关街道综合文化活动中心（农科院站）'
    },
    {
      key: 'beijing_gov_whlyj_street_88',
      name: '北下关街道综合文化活动中心（评剧团站）'
    },
    {
      key: '北京本地宝',
      name: '北京上方山国家森林公园'
    },
    {
      key: '北京本地宝',
      name: '北京世园公园'
    },
    {
      key: '北京本地宝',
      name: '北京世界花卉大观园'
    },
    {
      key: 'beijing_gov_whlyj_perf_11',
      name: '北京世纪剧院'
    },
    {
      key: '北京本地宝',
      name: '北京东城区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京东城区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京东城区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京东城区公园'
    },
    {
      key: '北京本地宝',
      name: '北京东城区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京东城区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京东城区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京东城区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京东城区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京东城区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京东城区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京东城区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京东城区艺术中心'
    },
    {
      key: '北京本地宝',
      name: '北京东城区青少年宫'
    },
    {
      key: 'beijing_gov_wwj_10877430',
      name: '北京东璧堂中医药博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京东郊湿地公园'
    },
    {
      key: 'beijing_gov_wwj_545973',
      name: '北京中医药大学中医药博物馆'
    },
    {
      key: 'beijing_gov_wwj_545931',
      name: '北京中华民族博物院'
    },
    {
      key: 'beijing_gov_wwj_546006',
      name: '北京中国紫檀博物馆'
    },
    {
      key: 'beijing_gov_wwj_326114740',
      name: '北京中梦足球博物馆'
    },
    {
      key: 'beijing_gov_wwj_10877410',
      name: '北京中药炮制技术博物馆'
    },
    {
      key: 'beijing_gov_wwj_545898',
      name: '北京中轴线遗产保护中心（正阳门）'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区公园'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区艺术中心'
    },
    {
      key: '北京本地宝',
      name: '北京丰台区青少年宫'
    },
    {
      key: 'beijing_gov_wwj_21228156',
      name: '北京九鼎灶文化博物馆'
    },
    {
      key: 'beijing_gov_wwj_10877405',
      name: '北京二锅头酒博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京云居寺'
    },
    {
      key: 'beijing_gov_wwj_325968712',
      name: '北京云汇网球木拍博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京云蒙山景区'
    },
    {
      key: '北京本地宝',
      name: '北京京东大峡谷'
    },
    {
      key: 'beijing_gov_wwj_11186650',
      name: '北京京华茶叶博物馆'
    },
    {
      key: 'beijing_gov_wwj_546063',
      name: '北京人民艺术剧院戏剧博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京儿艺剧场'
    },
    {
      key: '北京本地宝',
      name: '北京八达岭国家森林公园'
    },
    {
      key: 'beijing_gov_wwj_743627785',
      name: '北京公交馆'
    },
    {
      key: 'beijing_gov_wwj_743627844',
      name: '北京六必居博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京动物园'
    },
    {
      key: 'beijing_gov_wwj_546099',
      name: '北京励志堂科举匾额博物馆'
    },
    {
      key: 'beijing_gov_wwj_10877390',
      name: '北京劲飞京作红木文化博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京十渡景区'
    },
    {
      key: 'beijing_gov_wwj_546009',
      name: '北京南海子麋鹿苑博物馆'
    },
    {
      key: 'manual',
      name: '北京古代建筑博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京古北水镇'
    },
    {
      key: '北京本地宝',
      name: '北京古观象台'
    },
    {
      key: '北京本地宝',
      name: '北京台湖公园'
    },
    {
      key: '北京本地宝',
      name: '北京司马台长城'
    },
    {
      key: '北京本地宝',
      name: '北京园博园'
    },
    {
      key: 'bjry',
      name: '北京国际戏剧中心·人艺小剧场'
    },
    {
      key: '北京本地宝',
      name: '北京国际雕塑公园'
    },
    {
      key: '北京本地宝',
      name: '北京国际鲜花港'
    },
    {
      key: '北京本地宝',
      name: '北京圣莲山景区'
    },
    {
      key: 'beijing_gov_whlyj_perf_38',
      name: '北京地质礼堂'
    },
    {
      key: '北京本地宝',
      name: '北京城市图书馆'
    },
    {
      key: 'beijing_gov_wwj_743627956',
      name: '北京外国语大学校史馆、世界语言艺术博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区公园'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京大兴区艺术中心'
    },
    {
      key: 'beijing_gov_wwj_545832',
      name: '北京大学赛克勒考古与艺术博物馆'
    },
    {
      key: 'beijing_gov_wwj_11077317',
      name: '北京大戚收音机电影机博物馆'
    },
    {
      key: 'beijing_gov_wwj_545904',
      name: '北京大觉寺与团城管理处（团城演武厅）'
    },
    {
      key: 'beijing_gov_wwj_545925',
      name: '北京大觉寺与团城管理处（大觉寺）'
    },
    {
      key: '首都博物馆',
      name: '北京大运河博物馆'
    },
    {
      key: 'bjmuseum',
      name: '北京大运河博物馆（首都博物馆东馆）'
    },
    {
      key: 'beijing_gov_wwj_743627797',
      name: '北京天元中医药博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京天文馆'
    },
    {
      key: '北京本地宝',
      name: '北京天文馆A馆'
    },
    {
      key: '北京本地宝',
      name: '北京天文馆B馆'
    },
    {
      key: '北京本地宝',
      name: '北京天文馆天象厅'
    },
    {
      key: 'beijing_gov_whlyj_perf_12',
      name: '北京天桥剧场'
    },
    {
      key: 'beijing_gov_wwj_743627673',
      name: '北京天桥印象博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京奥林匹克水上公园'
    },
    {
      key: '北京本地宝',
      name: '北京奥运博物馆'
    },
    {
      key: 'beijing_gov_wwj_743627961',
      name: '北京宝翠宫翡翠博物馆'
    },
    {
      key: 'beijing_gov_wwj_546072',
      name: '北京宣南文化博物馆管理处'
    },
    {
      key: '北京本地宝',
      name: '北京密云区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京密云区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京密云区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京密云区公园'
    },
    {
      key: '北京本地宝',
      name: '北京密云区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京密云区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京密云区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京密云区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京密云区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京密云区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京密云区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京密云区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京密云区艺术中心'
    },
    {
      key: '北京本地宝',
      name: '北京展览馆'
    },
    {
      key: '北京本地宝',
      name: '北京展览馆剧场'
    },
    {
      key: '北京本地宝',
      name: '北京工人体育场'
    },
    {
      key: '北京本地宝',
      name: '北京工人体育馆'
    },
    {
      key: 'beijing_gov_wwj_546015',
      name: '北京工艺美术博物馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_1',
      name: '北京市东城区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_2',
      name: '北京市东城区图书馆东总布分馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_7',
      name: '北京市东城区图书馆北京银行陶然支行分馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_4',
      name: '北京市东城区图书馆王府井书店分馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_3',
      name: '北京市东城区图书馆角楼分馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_6',
      name: '北京市东城区图书馆语文书店分馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_5',
      name: '北京市东城区图书馆阅想书店分馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_1',
      name: '北京市东城区文化馆'
    },
    {
      key: 'beijing_gov_wwj_11077312',
      name: '北京市和光书院博物馆'
    },
    {
      key: 'beijing_gov_wwj_743627951',
      name: '北京市大兴区天宫院乡情文史馆'
    },
    {
      key: 'beijing_gov_wwj_10877415',
      name: '北京市大兴区月季博物馆'
    },
    {
      key: 'beijing_gov_wwj_743628001',
      name: '北京市大兴区榆垡镇乡情文史馆'
    },
    {
      key: 'beijing_gov_wwj_662465',
      name: '北京市姜杰钢琴手风琴博物馆'
    },
    {
      key: 'manual',
      name: '北京市少年宫'
    },
    {
      key: 'beijing_gov_wwj_546198',
      name: '北京市平谷区博物馆'
    },
    {
      key: 'beijing_gov_wwj_546135',
      name: '北京市怀柔区博物馆'
    },
    {
      key: 'beijing_gov_wwj_546156',
      name: '北京市房山世界地质公园博物馆'
    },
    {
      key: 'manual',
      name: '北京市文化馆'
    },
    {
      key: 'beijing_gov_wwj_546066',
      name: '北京市海淀区三山五园文化艺术中心（北京市海淀区博物...'
    },
    {
      key: 'beijing_gov_wwj_325729837',
      name: '北京市海淀区中关村村史馆'
    },
    {
      key: 'beijing_gov_wwj_545835',
      name: '北京市白塔寺管理处'
    },
    {
      key: 'beijing_gov_wwj_11077332',
      name: '北京市石景山区博物馆'
    },
    {
      key: 'beijing_gov_tyj_15',
      name: '北京市网球运动管理中心'
    },
    {
      key: 'beijing_gov_whlyj_lib_8',
      name: '北京市西城区图书馆（北址）'
    },
    {
      key: 'beijing_gov_whlyj_lib_9',
      name: '北京市西城区图书馆（南址）'
    },
    {
      key: 'beijing_gov_whlyj_cc_2',
      name: '北京市西城区文化馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_21',
      name: '北京市通州区图书馆'
    },
    {
      key: 'beijing_gov_wwj_545913',
      name: '北京市钟鼓楼文物保管所'
    },
    {
      key: 'manual',
      name: '北京市青少年活动中心'
    },
    {
      key: 'beijing_gov_wwj_325880521',
      name: '北京市顺义区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区艺术中心'
    },
    {
      key: '北京本地宝',
      name: '北京延庆区青少年宫'
    },
    {
      key: '北京本地宝',
      name: '北京延庆奥林匹克园区'
    },
    {
      key: '北京本地宝',
      name: '北京张家湾公园'
    },
    {
      key: '北京本地宝',
      name: '北京张裕爱斐堡国际酒庄'
    },
    {
      key: 'beijing_gov_wwj_546195',
      name: '北京御仙都皇家菜博物馆'
    },
    {
      key: 'beijing_gov_wwj_546057',
      name: '北京御生堂中医药博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区公园'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京怀柔区青少年宫'
    },
    {
      key: 'beijing_gov_wwj_546150',
      name: '北京怀柔喇叭沟门满族民俗博物馆'
    },
    {
      key: 'beijing_gov_wwj_545994',
      name: '北京戏曲博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京房山世界地质公园'
    },
    {
      key: 'beijing_gov_wwj_545856',
      name: '北京房山云居寺石经博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京房山区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京房山区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京房山区公园'
    },
    {
      key: '北京本地宝',
      name: '北京房山区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京房山区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京房山区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京房山区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京房山区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京房山区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京房山区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京房山区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京房山区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京房山区青少年宫'
    },
    {
      key: '北京本地宝',
      name: '北京故宫博物院'
    },
    {
      key: 'manual',
      name: '北京数字文化馆'
    },
    {
      key: 'beijing_gov_wwj_545895',
      name: '北京文博交流馆（北京市智化寺管理处）'
    },
    {
      key: 'beijing_gov_wwj_546219',
      name: '北京文旺阁木作博物馆'
    },
    {
      key: 'beijing_gov_wwj_21228162',
      name: '北京文景珍本期刊博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区公园'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京昌平区青少年宫'
    },
    {
      key: 'beijing_gov_wwj_545901',
      name: '北京明城墙遗址公园（东南城角角楼）'
    },
    {
      key: '北京本地宝',
      name: '北京月亮河公园'
    },
    {
      key: 'beijing_gov_wwj_546021',
      name: '北京服装学院民族服饰博物馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_30',
      name: '北京朝阳剧场'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区公园'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区艺术中心'
    },
    {
      key: '北京本地宝',
      name: '北京朝阳区青少年宫'
    },
    {
      key: 'beijing_gov_wwj_546090',
      name: '北京李大钊故居'
    },
    {
      key: 'beijing_gov_wwj_743627987',
      name: '北京果脯博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京植物园'
    },
    {
      key: '北京本地宝',
      name: '北京植物园樱桃沟'
    },
    {
      key: '北京本地宝',
      name: '北京植物园温室'
    },
    {
      key: '北京本地宝',
      name: '北京欢乐谷'
    },
    {
      key: '北京本地宝',
      name: '北京民俗博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京汉石桥湿地'
    },
    {
      key: '北京本地宝',
      name: '北京汽车博物馆'
    },
    {
      key: 'beijing_gov_wwj_325822216',
      name: '北京法和律师博物馆'
    },
    {
      key: 'beijing_gov_wwj_545916',
      name: '北京法海寺博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区艺术中心'
    },
    {
      key: '北京本地宝',
      name: '北京海淀区青少年宫'
    },
    {
      key: 'manual',
      name: '北京消防科普教育基地'
    },
    {
      key: 'beijing_gov_wwj_545844',
      name: '北京焦庄户地道战遗址纪念馆'
    },
    {
      key: 'beijing_gov_wwj_10877425',
      name: '北京燕京八绝博物馆'
    },
    {
      key: 'beijing_gov_wwj_743627719',
      name: '北京牛栏山二锅头酒文化博物馆'
    },
    {
      key: 'beijing_gov_wwj_546030',
      name: '北京王府井古人类文化遗址博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京环球度假区'
    },
    {
      key: '北京本地宝',
      name: '北京画院美术馆'
    },
    {
      key: 'beijing_gov_wwj_546084',
      name: '北京百年世界老电话博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京百花山景区'
    },
    {
      key: 'beijing_gov_wwj_10877420',
      name: '北京皇城御窑金砖博物馆'
    },
    {
      key: 'beijing_gov_wwj_546054',
      name: '北京皇城艺术馆'
    },
    {
      key: '北京本地宝',
      name: '北京石刻艺术博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区公园'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区艺术中心'
    },
    {
      key: '北京本地宝',
      name: '北京石景山区青少年宫'
    },
    {
      key: '北京本地宝',
      name: '北京石景山游乐园'
    },
    {
      key: '北京本地宝',
      name: '北京石林峡景区'
    },
    {
      key: '北京本地宝',
      name: '北京石花洞景区'
    },
    {
      key: 'beijing_gov_wwj_743628012',
      name: '北京神农农耕文化博物馆'
    },
    {
      key: 'beijing_gov_wwj_743627979',
      name: '北京神州连环画博物馆'
    },
    {
      key: 'beijing_gov_wwj_743627862',
      name: '北京福履布鞋文化博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京科学中心'
    },
    {
      key: 'beijing_gov_wwj_546204',
      name: '北京税务博物馆'
    },
    {
      key: 'beijing_gov_wwj_546132',
      name: '北京空竹博物馆'
    },
    {
      key: 'beijing_gov_wwj_545892',
      name: '北京红楼文化艺术博物馆'
    },
    {
      key: 'beijing_gov_tyj_33',
      name: '北京经济技术开发区体育中心'
    },
    {
      key: 'beijing_gov_wwj_546081',
      name: '北京老爷车博物馆'
    },
    {
      key: 'beijing_gov_wwj_545829',
      name: '北京考古遗址博物馆（北京大葆台遗址博物馆）'
    },
    {
      key: 'beijing_gov_wwj_326128383',
      name: '北京考古遗址博物馆（金中都水关遗址）'
    },
    {
      key: 'beijing_gov_wwj_546027',
      name: '北京自来水博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京自然博物馆'
    },
    {
      key: 'beijing_gov_wwj_743627946',
      name: '北京舞蹈学院舞蹈博物馆'
    },
    {
      key: 'beijing_gov_wwj_545850',
      name: '北京航空航天博物馆'
    },
    {
      key: 'beijing_gov_wwj_325729805',
      name: '北京航空航天模型博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京艺术博物馆'
    },
    {
      key: '北京艺术博物馆（万寿寺）',
      name: '北京艺术博物馆（万寿寺）'
    },
    {
      key: 'beijing_gov_wwj_546192',
      name: '北京英杰硬石艺术博物馆'
    },
    {
      key: 'beijing_gov_wwj_10877395',
      name: '北京荣唐连环画博物馆'
    },
    {
      key: 'beijing_gov_wwj_325729820',
      name: '北京莱恩堡葡萄酒文化博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京莲花池公园'
    },
    {
      key: 'beijing_gov_wwj_11077327',
      name: '北京菜百黄金珠宝博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京蒲洼乡花台景区'
    },
    {
      key: 'beijing_gov_whlyj_perf_40',
      name: '北京蓬蒿人剧场'
    },
    {
      key: 'beijing_gov_whlyj_perf_39',
      name: '北京蜂巢剧场'
    },
    {
      key: 'beijing_gov_whlyj_perf_45',
      name: '北京西区剧场'
    },
    {
      key: '北京本地宝',
      name: '北京西城区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京西城区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京西城区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京西城区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京西城区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京西城区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京西城区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京西城区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京西城区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京西城区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京西城区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京西城区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京西城区艺术中心'
    },
    {
      key: '北京本地宝',
      name: '北京西城区青少年宫'
    },
    {
      key: '北京本地宝',
      name: '北京西海子公园'
    },
    {
      key: 'beijing_gov_wwj_546120',
      name: '北京西瓜博物馆'
    },
    {
      key: 'manual',
      name: '北京规划展览馆'
    },
    {
      key: 'beijing_gov_wwj_546024',
      name: '北京警察博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京路县故城遗址'
    },
    {
      key: '北京本地宝',
      name: '北京运河奥体公园'
    },
    {
      key: '北京本地宝',
      name: '北京运河森林公园'
    },
    {
      key: '北京本地宝',
      name: '北京通州区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京通州区公园'
    },
    {
      key: '北京本地宝',
      name: '北京通州区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京通州区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京通州区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京通州区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京通州区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京通州区文化中心'
    },
    {
      key: '北京本地宝',
      name: '北京通州区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京通州区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京通州区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京通州区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京通州区青少年宫'
    },
    {
      key: '北京本地宝',
      name: '北京通州博物馆'
    },
    {
      key: 'beijing_gov_wwj_743628006',
      name: '北京遇见艺术博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京野生动物园'
    },
    {
      key: '北京本地宝',
      name: '北京野鸭湖国家湿地公园'
    },
    {
      key: 'beijing_gov_wwj_546033',
      name: '北京金台艺术馆'
    },
    {
      key: '北京本地宝',
      name: '北京金海湖景区'
    },
    {
      key: 'beijing_gov_wwj_325880527',
      name: '北京金漆镶嵌艺术博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京银狐洞景区'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区体育场'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区公园'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区剧院'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京门头沟区艺术中心'
    },
    {
      key: '北京本地宝',
      name: '北京雾灵山景区'
    },
    {
      key: '北京本地宝',
      name: '北京霞云岭国家森林公园'
    },
    {
      key: '北京本地宝',
      name: '北京青龙湖公园'
    },
    {
      key: 'beijing_gov_wwj_546117',
      name: '北京韩美林艺术馆'
    },
    {
      key: '北京本地宝',
      name: '北京音乐厅'
    },
    {
      key: '北京本地宝',
      name: '北京顺义公园'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区会展中心'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区体育馆'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区公园'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区创意园'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区动物园'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区博物馆'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区图书馆'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区文化馆'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区植物园'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区海洋馆'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区科技馆'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区美术馆'
    },
    {
      key: '北京本地宝',
      name: '北京顺义区艺术中心'
    },
    {
      key: '北京本地宝',
      name: '北京顺义新城滨河森林公园'
    },
    {
      key: '北京本地宝',
      name: '北京鲁迅博物馆'
    },
    {
      key: '北京鲁迅博物馆（北京新文化运动纪念馆）',
      name: '北京鲁迅博物馆（北京新文化运动纪念馆）'
    },
    {
      key: '北京本地宝',
      name: '北京黑龙潭景区'
    },
    {
      key: '北京本地宝',
      name: '北京龙庆峡景区'
    },
    {
      key: 'beijing_gov_wwj_325822223',
      name: '北京龙顺成京作非遗博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_223',
      name: '北务镇'
    },
    {
      key: 'beijing_gov_whlyj_street_90',
      name: '北太平庄街道综合文化活动中心（蓟门书院）'
    },
    {
      key: 'beijing_gov_whlyj_street_125',
      name: '北宫镇综合文化活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_234',
      name: '北小营镇'
    },
    {
      key: 'beijing_gov_whlyj_street_330',
      name: '北房镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_10',
      name: '北新桥街道综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '北海公园'
    },
    {
      key: 'beijing_gov_whlyj_street_231',
      name: '北石槽镇'
    },
    {
      key: 'beijing_gov_whlyj_street_272',
      name: '北臧村镇'
    },
    {
      key: 'beijing_gov_whlyj_street_204',
      name: '北苑街道文体活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_205',
      name: '北苑街道文化活动中心'
    },
    {
      key: 'beijing_gov_wwj_743627558',
      name: '十三陵水库展览馆'
    },
    {
      key: 'beijing_gov_whlyj_street_287',
      name: '十三陵镇'
    },
    {
      key: 'beijing_gov_whlyj_street_63',
      name: '十八里店地区'
    },
    {
      key: 'beijing_gov_whlyj_street_187',
      name: '十渡镇'
    },
    {
      key: 'beijing_gov_whlyj_street_363',
      name: '千家店镇'
    },
    {
      key: 'beijing_gov_whlyj_street_295',
      name: '南口镇'
    },
    {
      key: '北京本地宝',
      name: '南宫旅游景区'
    },
    {
      key: 'beijing_gov_whlyj_street_232',
      name: '南彩镇'
    },
    {
      key: 'beijing_gov_whlyj_street_238',
      name: '南法信镇'
    },
    {
      key: 'manual',
      name: '南海子公园'
    },
    {
      key: 'beijing_gov_whlyj_street_312',
      name: '南独乐河镇'
    },
    {
      key: 'beijing_gov_whlyj_street_79',
      name: '南磨房地区'
    },
    {
      key: 'beijing_gov_whlyj_street_191',
      name: '南窖乡'
    },
    {
      key: 'beijing_gov_whlyj_street_122',
      name: '南苑街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_280',
      name: '南邵镇'
    },
    {
      key: '北京本地宝',
      name: '南锣鼓巷'
    },
    {
      key: 'beijing_gov_whlyj_street_258',
      name: '博兴街道'
    },
    {
      key: 'beijing_gov_wwj_545961',
      name: '卢沟桥历史博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_142',
      name: '卢沟桥街道市民活动中心'
    },
    {
      key: 'beijing_gov_wwj_546102',
      name: '历代帝王庙'
    },
    {
      key: 'beijing_gov_whlyj_street_244',
      name: '双丰街道'
    },
    {
      key: 'beijing_gov_whlyj_street_53',
      name: '双井街道'
    },
    {
      key: 'beijing_gov_whlyj_street_152',
      name: '古城街道'
    },
    {
      key: 'beijing_gov_wwj_545937',
      name: '古陶文明博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_203',
      name: '台湖镇文体活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_302',
      name: '史各庄街道'
    },
    {
      key: 'beijing_gov_whlyj_street_190',
      name: '史家营乡'
    },
    {
      key: 'beijing_gov_whlyj_street_136',
      name: '右安门街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_222',
      name: '后沙峪镇'
    },
    {
      key: 'beijing_gov_whlyj_street_197',
      name: '向阳街道'
    },
    {
      key: 'beijing_gov_wwj_545883',
      name: '周口店北京人遗址博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_180',
      name: '周口店镇'
    },
    {
      key: 'beijing_gov_whlyj_street_80',
      name: '呼家楼街道'
    },
    {
      key: 'beijing_gov_whlyj_street_127',
      name: '和义街道文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_41',
      name: '和平街街道'
    },
    {
      key: 'beijing_gov_whlyj_street_1',
      name: '和平里街道综合文化中心'
    },
    {
      key: 'beijing_gov_wwj_546183',
      name: '和苑博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_327',
      name: '喇叭沟门满族乡综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_perf_47',
      name: '嘻哈包袱铺交道口店'
    },
    {
      key: 'beijing_gov_whlyj_street_117',
      name: '四季青镇综合文化活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_366',
      name: '四海镇'
    },
    {
      key: 'beijing_gov_tyj_26',
      name: '回龙观体育文化公园'
    },
    {
      key: 'beijing_gov_whlyj_street_296',
      name: '回龙观街道'
    },
    {
      key: 'beijing_gov_whlyj_street_50',
      name: '团结湖街道'
    },
    {
      key: 'beijing_gov_whlyj_perf_46',
      name: '国图艺术中心（原国图音乐厅）'
    },
    {
      key: '北京本地宝',
      name: '国家体育场'
    },
    {
      key: '北京本地宝',
      name: '国家体育馆'
    },
    {
      key: 'beijing_gov_wwj_21228167',
      name: '国家典籍博物馆'
    },
    {
      key: '北京本地宝',
      name: '国家动物博物馆'
    },
    {
      key: '北京本地宝',
      name: '国家图书馆'
    },
    {
      key: '国家图书馆',
      name: '国家图书馆少年儿童馆'
    },
    {
      key: '北京本地宝',
      name: '国家大剧院'
    },
    {
      key: 'beijing_gov_wwj_743627668',
      name: '国家大剧院台湖舞美艺术博物馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_4',
      name: '国家大剧院小剧场'
    },
    {
      key: 'beijing_gov_whlyj_perf_2',
      name: '国家大剧院戏剧场'
    },
    {
      key: 'beijing_gov_whlyj_perf_3',
      name: '国家大剧院歌剧院'
    },
    {
      key: 'beijing_gov_whlyj_perf_1',
      name: '国家大剧院音乐厅'
    },
    {
      key: '北京本地宝',
      name: '国家游泳中心'
    },
    {
      key: '北京本地宝',
      name: '国家自然博物馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_36',
      name: '国话先锋剧场'
    },
    {
      key: '北京本地宝',
      name: '国贸商城'
    },
    {
      key: '圆明园',
      name: '圆明园'
    },
    {
      key: 'beijing_gov_wwj_545922',
      name: '圆明园展览馆'
    },
    {
      key: 'beijing_gov_tyj_1',
      name: '地坛体育中心'
    },
    {
      key: 'beijing_gov_tyj_4',
      name: '地坛体育馆'
    },
    {
      key: '北京本地宝',
      name: '地坛公园'
    },
    {
      key: 'beijing_gov_whlyj_street_47',
      name: '垡头街道'
    },
    {
      key: 'beijing_gov_whlyj_street_169',
      name: '城关街道'
    },
    {
      key: 'beijing_gov_whlyj_street_277',
      name: '城北街道'
    },
    {
      key: 'beijing_gov_whlyj_street_300',
      name: '城南街道'
    },
    {
      key: 'beijing_gov_whlyj_street_157',
      name: '城子街道'
    },
    {
      key: 'manual',
      name: '城市绿心森林公园'
    },
    {
      key: 'beijing_gov_whlyj_street_316',
      name: '夏各庄镇'
    },
    {
      key: 'beijing_gov_tyj_28',
      name: '大兴区体育中心'
    },
    {
      key: 'beijing_gov_whlyj_lib_23',
      name: '大兴区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_14',
      name: '大兴区文化馆'
    },
    {
      key: 'beijing_gov_whlyj_street_306',
      name: '大兴庄镇'
    },
    {
      key: 'beijing_gov_whlyj_street_305',
      name: '大华山镇'
    },
    {
      key: 'beijing_gov_whlyj_street_159',
      name: '大台街道'
    },
    {
      key: 'beijing_gov_whlyj_street_235',
      name: '大孙各庄镇'
    },
    {
      key: 'beijing_gov_whlyj_street_192',
      name: '大安山乡'
    },
    {
      key: 'beijing_gov_whlyj_street_45',
      name: '大屯街道'
    },
    {
      key: 'beijing_gov_whlyj_street_156',
      name: '大峪街道'
    },
    {
      key: 'beijing_gov_whlyj_street_371',
      name: '大庄科乡'
    },
    {
      key: 'manual',
      name: '大望京公园'
    },
    {
      key: 'beijing_gov_whlyj_street_35',
      name: '大栅栏街道'
    },
    {
      key: 'beijing_gov_whlyj_street_374',
      name: '大榆树镇'
    },
    {
      key: 'beijing_gov_whlyj_street_183',
      name: '大石窝镇'
    },
    {
      key: 'beijing_gov_whlyj_street_124',
      name: '大红门街道综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '大观园'
    },
    {
      key: '北京本地宝',
      name: '大钟寺古钟博物馆'
    },
    {
      key: 'beijing_gov_tyj_2',
      name: '天坛体育中心'
    },
    {
      key: '北京本地宝',
      name: '天坛公园'
    },
    {
      key: 'beijing_gov_whlyj_street_19',
      name: '天坛街道市民活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_253',
      name: '天宫院街道'
    },
    {
      key: 'beijing_gov_whlyj_perf_14',
      name: '天桥艺术中心中剧场'
    },
    {
      key: 'beijing_gov_whlyj_perf_16',
      name: '天桥艺术中心多功能剧场'
    },
    {
      key: 'beijing_gov_whlyj_perf_13',
      name: '天桥艺术中心大剧场'
    },
    {
      key: 'beijing_gov_whlyj_perf_15',
      name: '天桥艺术中心小剧场'
    },
    {
      key: 'beijing_gov_whlyj_street_21',
      name: '天桥街道'
    },
    {
      key: 'beijing_gov_whlyj_street_229',
      name: '天竺镇'
    },
    {
      key: 'beijing_gov_tyj_27',
      name: '天通苑体育馆'
    },
    {
      key: 'beijing_gov_whlyj_street_288',
      name: '天通苑北街道'
    },
    {
      key: 'beijing_gov_whlyj_street_281',
      name: '天通苑南街道'
    },
    {
      key: 'beijing_gov_whlyj_street_61',
      name: '太阳宫地区'
    },
    {
      key: 'manual',
      name: '太阳宫市民活动中心'
    },
    {
      key: '北京本地宝',
      name: '奥林匹克公园'
    },
    {
      key: '北京本地宝',
      name: '奥林匹克森林公园'
    },
    {
      key: 'beijing_gov_whlyj_street_37',
      name: '奥运村街道'
    },
    {
      key: 'beijing_gov_whlyj_street_167',
      name: '妙峰山镇'
    },
    {
      key: '北京本地宝',
      name: '妙应寺白塔'
    },
    {
      key: '北京本地宝',
      name: '孔庙和国子监博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_75',
      name: '孙河地区'
    },
    {
      key: 'beijing_gov_whlyj_street_95',
      name: '学院路街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_271',
      name: '安定镇'
    },
    {
      key: 'beijing_gov_whlyj_street_2',
      name: '安定门街道文体中心'
    },
    {
      key: 'beijing_gov_whlyj_street_51',
      name: '安贞街道'
    },
    {
      key: 'beijing_gov_whlyj_street_209',
      name: '宋庄镇综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '宋庆龄同志故居'
    },
    {
      key: 'beijing_gov_wwj_545763',
      name: '宋庆龄故居管理中心'
    },
    {
      key: 'beijing_gov_whlyj_street_139',
      name: '宛平街道文体活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_325',
      name: '宝山镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_344',
      name: '密云区不老屯镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_348',
      name: '密云区东邵渠镇综合文化中心'
    },
    {
      key: 'beijing_gov_tyj_31',
      name: '密云区体育中心'
    },
    {
      key: 'beijing_gov_whlyj_street_339',
      name: '密云区冯家峪镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_338',
      name: '密云区北庄镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_352',
      name: '密云区十里堡镇综合文化中心'
    },
    {
      key: 'beijing_gov_wwj_545859',
      name: '密云区博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_343',
      name: '密云区古北口镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_lib_27',
      name: '密云区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_342',
      name: '密云区大城子镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_347',
      name: '密云区太师屯镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_353',
      name: '密云区密云镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_340',
      name: '密云区巨各庄镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_cc_18',
      name: '密云区文化馆'
    },
    {
      key: 'beijing_gov_whlyj_street_350',
      name: '密云区新城子镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_355',
      name: '密云区果园街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_346',
      name: '密云区河南寨镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_337',
      name: '密云区溪翁庄镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_349',
      name: '密云区石城镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_341',
      name: '密云区穆家峪镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_351',
      name: '密云区西田各庄镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_345',
      name: '密云区高岭镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_356',
      name: '密云区鼓楼街道综合文化中心'
    },
    {
      key: 'beijing_gov_wwj_743627936',
      name: '对外经贸博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_64',
      name: '将台地区'
    },
    {
      key: 'beijing_gov_whlyj_street_54',
      name: '小关街道'
    },
    {
      key: 'beijing_gov_whlyj_street_293',
      name: '小汤山镇'
    },
    {
      key: 'beijing_gov_whlyj_street_76',
      name: '小红门地区'
    },
    {
      key: 'beijing_gov_wwj_546069',
      name: '居庸关长城博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_29',
      name: '展览路街道'
    },
    {
      key: 'beijing_gov_whlyj_street_314',
      name: '山东庄镇'
    },
    {
      key: 'beijing_gov_wwj_545868',
      name: '山戎文化陈列馆'
    },
    {
      key: 'beijing_gov_whlyj_street_319',
      name: '峪口镇'
    },
    {
      key: 'beijing_gov_whlyj_perf_35',
      name: '崇文工人文化宫'
    },
    {
      key: 'beijing_gov_whlyj_street_13',
      name: '崇文门外街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_72',
      name: '崔各庄地区'
    },
    {
      key: 'beijing_gov_whlyj_street_289',
      name: '崔村镇'
    },
    {
      key: 'beijing_gov_whlyj_street_59',
      name: '左家庄街道'
    },
    {
      key: 'beijing_gov_whlyj_street_67',
      name: '常营地区'
    },
    {
      key: 'beijing_gov_wwj_545967',
      name: '平北抗日战争纪念馆'
    },
    {
      key: 'beijing_gov_whlyj_street_77',
      name: '平房地区'
    },
    {
      key: 'beijing_gov_wwj_545964',
      name: '平西抗日战争纪念馆'
    },
    {
      key: 'beijing_gov_tyj_29',
      name: '平谷区体育中心'
    },
    {
      key: 'beijing_gov_whlyj_lib_25',
      name: '平谷区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_16',
      name: '平谷区文化馆'
    },
    {
      key: 'beijing_gov_whlyj_street_313',
      name: '平谷镇'
    },
    {
      key: 'beijing_gov_whlyj_street_30',
      name: '广内街道'
    },
    {
      key: 'beijing_gov_whlyj_street_28',
      name: '广外街道'
    },
    {
      key: 'beijing_gov_whlyj_street_154',
      name: '广宁街道'
    },
    {
      key: 'beijing_gov_tyj_5',
      name: '广安体育中心'
    },
    {
      key: 'beijing_gov_tyj_6',
      name: '广安游泳网球馆'
    },
    {
      key: 'beijing_gov_whlyj_street_321',
      name: '庙城镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_273',
      name: '庞各庄镇'
    },
    {
      key: 'beijing_gov_whlyj_street_361',
      name: '康庄镇'
    },
    {
      key: 'beijing_gov_whlyj_street_292',
      name: '延寿镇'
    },
    {
      key: 'beijing_gov_tyj_32',
      name: '延庆区体育中心'
    },
    {
      key: 'beijing_gov_whlyj_lib_28',
      name: '延庆区图书馆'
    },
    {
      key: 'beijing_gov_wwj_662437',
      name: '延庆区地质博物馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_19',
      name: '延庆区文化馆'
    },
    {
      key: 'beijing_gov_wwj_546123',
      name: '延庆博物馆'
    },
    {
      key: 'beijing_gov_wwj_743627996',
      name: '延庆石刻博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_372',
      name: '延庆镇文体中心'
    },
    {
      key: 'beijing_gov_whlyj_street_7',
      name: '建国门街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_39',
      name: '建外街道'
    },
    {
      key: 'beijing_gov_whlyj_street_184',
      name: '张坊镇'
    },
    {
      key: 'beijing_gov_whlyj_street_215',
      name: '张家湾镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_369',
      name: '张山营镇'
    },
    {
      key: 'beijing_gov_whlyj_street_225',
      name: '张镇'
    },
    {
      key: 'beijing_gov_wwj_545793',
      name: '徐悲鸿纪念馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_28',
      name: '德云社天桥剧场'
    },
    {
      key: 'beijing_gov_whlyj_street_27',
      name: '德胜街道'
    },
    {
      key: 'manual',
      name: '念坛公园'
    },
    {
      key: 'beijing_gov_whlyj_street_332',
      name: '怀北镇综合文化中心'
    },
    {
      key: 'beijing_gov_tyj_30',
      name: '怀柔区体育中心'
    },
    {
      key: 'beijing_gov_whlyj_lib_26',
      name: '怀柔区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_17',
      name: '怀柔区文化馆'
    },
    {
      key: 'beijing_gov_whlyj_street_328',
      name: '怀柔镇综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '恭王府博物馆'
    },
    {
      key: 'beijing_gov_wwj_743627885',
      name: '慈善寺古香道文化陈列馆'
    },
    {
      key: 'beijing_gov_wwj_545958',
      name: '慈悲庵'
    },
    {
      key: 'beijing_gov_whlyj_street_146',
      name: '成寿寺街道综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '戒台寺'
    },
    {
      key: 'beijing_gov_tyj_19',
      name: '房山区体育场'
    },
    {
      key: 'beijing_gov_whlyj_lib_19',
      name: '房山区图书馆城关分馆（老馆）'
    },
    {
      key: 'beijing_gov_whlyj_lib_18',
      name: '房山区图书馆（新）'
    },
    {
      key: 'beijing_gov_whlyj_cc_10',
      name: '房山区文化馆城关分馆（老馆）'
    },
    {
      key: 'beijing_gov_whlyj_cc_9',
      name: '房山区文化馆（新）'
    },
    {
      key: 'beijing_gov_whlyj_street_170',
      name: '拱辰街道'
    },
    {
      key: 'gugong',
      name: '故宫博物院'
    },
    {
      key: 'beijing_gov_wwj_545949',
      name: '文化和旅游部恭王府博物馆'
    },
    {
      key: 'beijing_gov_wwj_545907',
      name: '文天祥祠'
    },
    {
      key: 'beijing_gov_whlyj_street_220',
      name: '文景街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_165',
      name: '斋堂镇'
    },
    {
      key: 'beijing_gov_whlyj_street_217',
      name: '新华街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_24',
      name: '新街口街道'
    },
    {
      key: 'beijing_gov_whlyj_street_193',
      name: '新镇街道'
    },
    {
      key: 'beijing_gov_whlyj_street_143',
      name: '方庄街道综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '日坛公园'
    },
    {
      key: 'beijing_gov_whlyj_street_360',
      name: '旧县镇文体中心'
    },
    {
      key: 'beijing_gov_whlyj_street_266',
      name: '旧宫镇'
    },
    {
      key: 'beijing_gov_whlyj_street_243',
      name: '旺泉街道'
    },
    {
      key: 'beijing_gov_tyj_24',
      name: '昌平体育馆'
    },
    {
      key: 'beijing_gov_tyj_25',
      name: '昌平区体育运动场'
    },
    {
      key: 'beijing_gov_wwj_545862',
      name: '昌平区博物馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_24',
      name: '昌平区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_15',
      name: '昌平区文化馆'
    },
    {
      key: 'beijing_gov_wwj_545799',
      name: '明十三陵博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_198',
      name: '星城街道'
    },
    {
      key: '北京本地宝',
      name: '景山公园'
    },
    {
      key: 'beijing_gov_whlyj_street_4',
      name: '景山街道综合文化中心'
    },
    {
      key: 'beijing_gov_wwj_743627828',
      name: '景泰蓝艺术博物馆'
    },
    {
      key: '北京本地宝',
      name: '智化寺'
    },
    {
      key: 'beijing_gov_whlyj_street_108',
      name: '曙光街道图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_107',
      name: '曙光街道市民活动中心'
    },
    {
      key: 'beijing_gov_wwj_545976',
      name: '曹雪芹纪念馆'
    },
    {
      key: 'beijing_gov_tyj_9',
      name: '月坛体育场'
    },
    {
      key: 'beijing_gov_tyj_7',
      name: '月坛体育馆'
    },
    {
      key: 'beijing_gov_tyj_8',
      name: '月坛综合训练馆'
    },
    {
      key: 'beijing_gov_whlyj_street_25',
      name: '月坛街道'
    },
    {
      key: 'beijing_gov_whlyj_street_43',
      name: '望京街道'
    },
    {
      key: 'manual',
      name: '望和公园'
    },
    {
      key: 'beijing_gov_whlyj_street_44',
      name: '朝外街道'
    },
    {
      key: 'manual',
      name: '朝阳体育中心'
    },
    {
      key: 'beijing_gov_tyj_12',
      name: '朝阳体育馆'
    },
    {
      key: '北京本地宝',
      name: '朝阳公园'
    },
    {
      key: '北京本地宝',
      name: '朝阳公园海洋沙滩狂欢节'
    },
    {
      key: 'manual',
      name: '朝阳区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_10',
      name: '朝阳区图书馆（劲松馆）'
    },
    {
      key: 'beijing_gov_whlyj_lib_11',
      name: '朝阳区图书馆（小庄馆）'
    },
    {
      key: 'manual',
      name: '朝阳区文化馆'
    },
    {
      key: 'manual',
      name: '朝阳区青少年活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_8',
      name: '朝阳门街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_233',
      name: '木林镇'
    },
    {
      key: 'beijing_gov_wwj_545838',
      name: '李大钊烈士陵园'
    },
    {
      key: 'beijing_gov_whlyj_street_239',
      name: '李桥镇'
    },
    {
      key: 'beijing_gov_whlyj_street_237',
      name: '李遂镇'
    },
    {
      key: 'beijing_gov_whlyj_street_71',
      name: '来广营地区'
    },
    {
      key: 'beijing_gov_whlyj_street_331',
      name: '杨宋镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_214',
      name: '杨庄街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_240',
      name: '杨镇'
    },
    {
      key: '北京本地宝',
      name: '松美术馆'
    },
    {
      key: 'beijing_gov_whlyj_street_248',
      name: '林校路街道'
    },
    {
      key: 'beijing_gov_whlyj_street_329',
      name: '桥梓镇综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '梅兰芳大剧院'
    },
    {
      key: 'beijing_gov_wwj_545808',
      name: '梅兰芳纪念馆'
    },
    {
      key: 'beijing_gov_whlyj_street_221',
      name: '梨园镇文化活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_31',
      name: '椿树街道'
    },
    {
      key: 'beijing_gov_whlyj_street_274',
      name: '榆垡镇'
    },
    {
      key: 'beijing_gov_whlyj_street_354',
      name: '檀营地区综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '欢乐水魔方水上乐园'
    },
    {
      key: 'beijing_gov_wwj_545736',
      name: '毛主席纪念堂'
    },
    {
      key: 'beijing_gov_whlyj_perf_18',
      name: '民族宫大剧院'
    },
    {
      key: 'beijing_gov_wwj_545742',
      name: '民族文化宫博物馆'
    },
    {
      key: 'beijing_gov_wwj_546162',
      name: '民航博物馆'
    },
    {
      key: 'beijing_gov_wwj_743627974',
      name: '水峪村生态博物馆'
    },
    {
      key: '北京本地宝',
      name: '水立方嬉水乐园'
    },
    {
      key: 'beijing_gov_whlyj_street_219',
      name: '永乐店镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_20',
      name: '永外街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_368',
      name: '永宁镇'
    },
    {
      key: 'manual',
      name: '永定河休闲森林公园'
    },
    {
      key: 'beijing_gov_wwj_545910',
      name: '永定河文化博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_111',
      name: '永定路街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_168',
      name: '永定镇'
    },
    {
      key: 'beijing_gov_whlyj_street_216',
      name: '永顺镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_365',
      name: '沈家营镇'
    },
    {
      key: 'manual',
      name: '沙河滨河公园'
    },
    {
      key: 'beijing_gov_whlyj_street_285',
      name: '沙河镇'
    },
    {
      key: 'beijing_gov_whlyj_street_185',
      name: '河北镇'
    },
    {
      key: 'beijing_gov_whlyj_street_334',
      name: '河口镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_336',
      name: '泉河街道综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '法海寺'
    },
    {
      key: '北京本地宝',
      name: '泡泡玛特城市乐园'
    },
    {
      key: 'beijing_gov_whlyj_street_284',
      name: '流村镇'
    },
    {
      key: 'manual',
      name: '海淀体育中心'
    },
    {
      key: '北京本地宝',
      name: '海淀公共安全馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_19',
      name: '海淀剧院'
    },
    {
      key: 'manual',
      name: '海淀区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_13',
      name: '海淀区图书馆（北馆）'
    },
    {
      key: 'beijing_gov_whlyj_cc_4',
      name: '海淀区文化馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_5',
      name: '海淀区文化馆（北馆）'
    },
    {
      key: 'beijing_gov_whlyj_street_92',
      name: '海淀区海淀街道图书分馆'
    },
    {
      key: 'manual',
      name: '海淀区青少年活动中心'
    },
    {
      key: 'beijing_gov_whlyj_perf_41',
      name: '海淀工人文化宫'
    },
    {
      key: 'beijing_gov_tyj_14',
      name: '海淀温泉体育中心'
    },
    {
      key: 'beijing_gov_whlyj_street_91',
      name: '海淀街道市民活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_115',
      name: '海淀镇综合文化活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_110',
      name: '清华园街道综合文化活动中心'
    },
    {
      key: 'beijing_gov_wwj_743628017',
      name: '清华大学科学博物馆'
    },
    {
      key: '清华大学艺术博物馆',
      name: '清华大学艺术博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_166',
      name: '清水镇'
    },
    {
      key: 'beijing_gov_whlyj_street_96',
      name: '清河街道综合文化服务中心'
    },
    {
      key: 'beijing_gov_whlyj_street_247',
      name: '清源街道'
    },
    {
      key: 'beijing_gov_whlyj_street_333',
      name: '渤海镇综合文化中心'
    },
    {
      key: 'manual',
      name: '温榆河公园'
    },
    {
      key: 'beijing_gov_whlyj_street_119',
      name: '温泉镇市民活动中心'
    },
    {
      key: 'beijing_gov_whlyj_perf_33',
      name: '湖广会馆大戏楼'
    },
    {
      key: 'beijing_gov_whlyj_street_304',
      name: '滨河街道'
    },
    {
      key: 'beijing_gov_whlyj_street_218',
      name: '漷县书院'
    },
    {
      key: 'beijing_gov_whlyj_street_52',
      name: '潘家园街道'
    },
    {
      key: 'beijing_gov_tyj_21',
      name: '潞城全民健身中心'
    },
    {
      key: 'beijing_gov_whlyj_street_199',
      name: '潞城镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_208',
      name: '潞源街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_207',
      name: '潞邑街道综合文化中心'
    },
    {
      key: '北京本地宝',
      name: '潭柘寺'
    },
    {
      key: 'beijing_gov_whlyj_street_162',
      name: '潭柘寺镇'
    },
    {
      key: 'manual',
      name: '潮白河森林公园'
    },
    {
      key: 'beijing_gov_wwj_743627941',
      name: '瀛海文史馆'
    },
    {
      key: 'beijing_gov_whlyj_street_264',
      name: '瀛海镇'
    },
    {
      key: 'beijing_gov_wwj_545796',
      name: '炎黄艺术馆'
    },
    {
      key: 'beijing_gov_whlyj_street_318',
      name: '熊儿寨乡'
    },
    {
      key: 'beijing_gov_whlyj_street_109',
      name: '燕园街道文化服务中心'
    },
    {
      key: 'beijing_gov_tyj_34',
      name: '燕山体育馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_20',
      name: '燕山图书馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_11',
      name: '燕山文化馆'
    },
    {
      key: 'beijing_gov_whlyj_street_230',
      name: '牛栏山镇'
    },
    {
      key: '北京本地宝',
      name: '牛街礼拜寺'
    },
    {
      key: 'beijing_gov_whlyj_street_22',
      name: '牛街街道'
    },
    {
      key: 'beijing_gov_whlyj_street_213',
      name: '玉桥街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_144',
      name: '玉泉营街道市民活动中心'
    },
    {
      key: '北京本地宝',
      name: '玉渊潭公园'
    },
    {
      key: 'beijing_gov_whlyj_street_66',
      name: '王四营地区'
    },
    {
      key: 'beijing_gov_whlyj_street_160',
      name: '王平镇'
    },
    {
      key: '北京本地宝',
      name: '王府井'
    },
    {
      key: 'beijing_gov_whlyj_street_315',
      name: '王辛庄镇'
    },
    {
      key: 'beijing_gov_whlyj_street_370',
      name: '珍珠泉乡'
    },
    {
      key: 'beijing_gov_whlyj_street_324',
      name: '琉璃庙镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_173',
      name: '琉璃河镇'
    },
    {
      key: 'beijing_gov_whlyj_street_84',
      name: '甘家口街道市民活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_104',
      name: '田村路街道文化活动中心'
    },
    {
      key: '北京本地宝',
      name: '白云观'
    },
    {
      key: 'beijing_gov_whlyj_street_26',
      name: '白纸坊街道'
    },
    {
      key: 'beijing_gov_whlyj_street_294',
      name: '百善镇'
    },
    {
      key: '北京本地宝',
      name: '百望山森林公园'
    },
    {
      key: 'beijing_gov_whlyj_street_358',
      name: '百泉街道'
    },
    {
      key: 'beijing_gov_whlyj_street_140',
      name: '看丹街道综合文化中心（党群服务中心）'
    },
    {
      key: 'beijing_gov_whlyj_street_245',
      name: '石园街道'
    },
    {
      key: 'manual',
      name: '石景山区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_lib_16',
      name: '石景山区图书馆少儿馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_7',
      name: '石景山区文化馆'
    },
    {
      key: 'beijing_gov_wwj_743627734',
      name: '石景山区石刻博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_181',
      name: '石楼镇'
    },
    {
      key: 'beijing_gov_whlyj_street_134',
      name: '石榴庄街道综合文化中心（原东铁匠营街道综合文化活动中心）'
    },
    {
      key: 'beijing_gov_whlyj_street_133',
      name: '石榴庄街道综合文化中心（原大红门街道综合文化中心）'
    },
    {
      key: 'beijing_gov_whlyj_street_269',
      name: '礼贤镇'
    },
    {
      key: 'beijing_gov_wwj_743627911',
      name: '科学家博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_241',
      name: '空港街道'
    },
    {
      key: 'beijing_gov_whlyj_street_174',
      name: '窦店镇1'
    },
    {
      key: 'beijing_gov_whlyj_street_175',
      name: '窦店镇2'
    },
    {
      key: 'beijing_gov_whlyj_street_74',
      name: '管庄地区'
    },
    {
      key: '北京本地宝',
      name: '索尼探梦科技馆'
    },
    {
      key: 'manual',
      name: '紫竹院公园'
    },
    {
      key: 'beijing_gov_whlyj_street_87',
      name: '紫竹院街道综合文化服务中心'
    },
    {
      key: 'beijing_gov_whlyj_perf_37',
      name: '繁星戏剧村（2个厅）'
    },
    {
      key: '北京本地宝',
      name: '红砖美术馆'
    },
    {
      key: '北京本地宝',
      name: '红螺寺'
    },
    {
      key: 'beijing_gov_whlyj_street_82',
      name: '羊坊店地区文体活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_83',
      name: '羊坊店街道文化中心'
    },
    {
      key: 'manual',
      name: '老君堂公园'
    },
    {
      key: 'beijing_gov_whlyj_street_148',
      name: '老山街道'
    },
    {
      key: 'beijing_gov_wwj_545991',
      name: '老甲艺术馆'
    },
    {
      key: '北京本地宝',
      name: '老舍纪念馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_32',
      name: '老舍茶馆(含新京调)'
    },
    {
      key: 'beijing_gov_whlyj_street_246',
      name: '胜利街道'
    },
    {
      key: 'beijing_gov_tyj_20',
      name: '良乡体育中心'
    },
    {
      key: 'beijing_gov_tyj_18',
      name: '良乡训练基地'
    },
    {
      key: 'beijing_gov_whlyj_street_178',
      name: '良乡镇'
    },
    {
      key: 'beijing_gov_whlyj_street_132',
      name: '花乡街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_103',
      name: '花园路街道市民活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_120',
      name: '苏家坨镇综合文化活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_147',
      name: '苹果园街道'
    },
    {
      key: '北京本地宝',
      name: '茅盾故居'
    },
    {
      key: 'beijing_gov_whlyj_street_257',
      name: '荣华街道'
    },
    {
      key: 'manual',
      name: '莲石湖公园'
    },
    {
      key: 'beijing_gov_whlyj_perf_7',
      name: '菊隐剧场'
    },
    {
      key: 'beijing_gov_whlyj_street_188',
      name: '蒲洼乡'
    },
    {
      key: '北京本地宝',
      name: '蓝色港湾'
    },
    {
      key: '北京本地宝',
      name: '蟹岛度假村'
    },
    {
      key: 'beijing_gov_whlyj_street_100',
      name: '西三旗街道文化活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_118',
      name: '西北旺镇市民活动中心'
    },
    {
      key: 'manual',
      name: '西城区图书馆'
    },
    {
      key: 'manual',
      name: '西城区文化馆'
    },
    {
      key: 'beijing_gov_tyj_10',
      name: '西城区武术和棋类运动管理中心'
    },
    {
      key: 'manual',
      name: '西海子公园'
    },
    {
      key: 'beijing_gov_whlyj_street_171',
      name: '西潞街道'
    },
    {
      key: 'beijing_gov_whlyj_street_261',
      name: '西红门镇'
    },
    {
      key: 'beijing_gov_whlyj_street_135',
      name: '西罗园街道综合文化中心'
    },
    {
      key: 'beijing_gov_wwj_546171',
      name: '西藏文化博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_34',
      name: '西长安街街道'
    },
    {
      key: 'beijing_gov_whlyj_street_201',
      name: '西集镇文体活动中心'
    },
    {
      key: 'beijing_gov_wwj_662468',
      name: '西黄寺博物馆'
    },
    {
      key: 'beijing_gov_wwj_545934',
      name: '观复博物馆'
    },
    {
      key: 'beijing_gov_whlyj_street_252',
      name: '观音寺街道'
    },
    {
      key: 'beijing_gov_wwj_743627807',
      name: '视障文化博物馆'
    },
    {
      key: 'beijing_gov_wwj_545841',
      name: '詹天佑纪念馆'
    },
    {
      key: 'beijing_gov_whlyj_street_65',
      name: '豆各庄地区'
    },
    {
      key: 'beijing_gov_whlyj_street_224',
      name: '赵全营镇'
    },
    {
      key: 'beijing_gov_whlyj_street_196',
      name: '迎风街道'
    },
    {
      key: 'manual',
      name: '通州体育中心'
    },
    {
      key: 'beijing_gov_wwj_545865',
      name: '通州区博物馆'
    },
    {
      key: 'manual',
      name: '通州区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_12',
      name: '通州区文化馆'
    },
    {
      key: 'manual',
      name: '通州区青少年活动中心'
    },
    {
      key: 'manual',
      name: '通州运河文化广场'
    },
    {
      key: 'beijing_gov_whlyj_street_212',
      name: '通运街道综合文化中心'
    },
    {
      key: 'beijing_gov_tyj_13',
      name: '郡王府体育中心'
    },
    {
      key: 'beijing_gov_wwj_545877',
      name: '郭守敬纪念馆'
    },
    {
      key: '北京本地宝',
      name: '郭沫若纪念馆'
    },
    {
      key: 'beijing_gov_whlyj_street_55',
      name: '酒仙桥街道'
    },
    {
      key: 'beijing_gov_whlyj_street_262',
      name: '采育镇'
    },
    {
      key: 'beijing_gov_whlyj_street_308',
      name: '金海湖镇'
    },
    {
      key: 'beijing_gov_whlyj_street_68',
      name: '金盏地区'
    },
    {
      key: 'beijing_gov_whlyj_street_33',
      name: '金融街街道'
    },
    {
      key: 'beijing_gov_whlyj_street_153',
      name: '金顶街街道'
    },
    {
      key: 'beijing_gov_whlyj_street_320',
      name: '镇罗营镇'
    },
    {
      key: 'beijing_gov_whlyj_street_326',
      name: '长哨营满族乡综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_265',
      name: '长子营镇'
    },
    {
      key: '北京本地宝',
      name: '长安大戏院'
    },
    {
      key: 'manual',
      name: '长沟湿地公园'
    },
    {
      key: 'beijing_gov_whlyj_street_182',
      name: '长沟镇'
    },
    {
      key: 'beijing_gov_wwj_545871',
      name: '长辛店二·七纪念馆'
    },
    {
      key: 'beijing_gov_whlyj_street_130',
      name: '长辛店街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_172',
      name: '长阳镇'
    },
    {
      key: 'beijing_gov_tyj_17',
      name: '门头沟区体育馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_8',
      name: '门头沟区文化馆'
    },
    {
      key: 'beijing_gov_whlyj_street_177',
      name: '阎村镇'
    },
    {
      key: '北京本地宝',
      name: '阳台山自然风景区'
    },
    {
      key: 'beijing_gov_whlyj_street_290',
      name: '阳坊镇'
    },
    {
      key: '北京本地宝',
      name: '陶然亭公园'
    },
    {
      key: 'beijing_gov_whlyj_street_32',
      name: '陶然亭街道'
    },
    {
      key: 'beijing_gov_whlyj_street_322',
      name: '雁栖镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_164',
      name: '雁翅镇'
    },
    {
      key: '北京本地宝',
      name: '雍和宫'
    },
    {
      key: 'beijing_gov_wwj_545817',
      name: '雍和宫藏传佛教艺术博物馆'
    },
    {
      key: 'beijing_gov_whlyj_perf_42',
      name: '雷剧场'
    },
    {
      key: 'beijing_gov_whlyj_street_286',
      name: '霍营街道'
    },
    {
      key: 'beijing_gov_whlyj_street_189',
      name: '霞云岭乡'
    },
    {
      key: 'beijing_gov_whlyj_street_263',
      name: '青云店镇'
    },
    {
      key: 'beijing_gov_whlyj_street_97',
      name: '青龙桥街道综合文化活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_179',
      name: '青龙湖镇'
    },
    {
      key: 'beijing_gov_whlyj_street_176',
      name: '韩村河镇'
    },
    {
      key: 'beijing_gov_tyj_22',
      name: '顺义体育中心'
    },
    {
      key: 'beijing_gov_whlyj_lib_22',
      name: '顺义区图书馆'
    },
    {
      key: 'beijing_gov_whlyj_cc_13',
      name: '顺义区文化馆'
    },
    {
      key: 'beijing_gov_tyj_23',
      name: '顺义城南体育中心'
    },
    {
      key: 'manual',
      name: '顺义新城滨河森林公园'
    },
    {
      key: '北京本地宝',
      name: '颐和园'
    },
    {
      key: 'beijing_gov_wwj_11077337',
      name: '颐和园博物馆'
    },
    {
      key: 'bjry',
      name: '首都剧场'
    },
    {
      key: '北京本地宝',
      name: '首都博物馆'
    },
    {
      key: '北京本地宝',
      name: '首都图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_46',
      name: '首都机场街道'
    },
    {
      key: 'beijing_gov_wwj_10877380',
      name: '首都粮食博物馆'
    },
    {
      key: '北京本地宝',
      name: '首钢园'
    },
    {
      key: 'manual',
      name: '首钢园·六工汇'
    },
    {
      key: '北京本地宝',
      name: '香山公园'
    },
    {
      key: 'beijing_gov_wwj_545979',
      name: '香山双清别墅'
    },
    {
      key: 'beijing_gov_whlyj_street_99',
      name: '香山街道图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_98',
      name: '香山街道综合文化中心'
    },
    {
      key: 'beijing_gov_wwj_10877385',
      name: '香山革命纪念馆'
    },
    {
      key: 'beijing_gov_whlyj_street_367',
      name: '香水园街道'
    },
    {
      key: 'beijing_gov_whlyj_street_36',
      name: '香河园街道'
    },
    {
      key: 'beijing_gov_whlyj_street_373',
      name: '香营乡文体中心'
    },
    {
      key: 'beijing_gov_whlyj_street_311',
      name: '马坊镇'
    },
    {
      key: 'beijing_gov_whlyj_street_227',
      name: '马坡镇'
    },
    {
      key: 'beijing_gov_whlyj_street_141',
      name: '马家堡街道文化活动中心'
    },
    {
      key: 'manual',
      name: '马家湾湿地公园'
    },
    {
      key: 'beijing_gov_whlyj_street_310',
      name: '马昌营镇'
    },
    {
      key: 'beijing_gov_whlyj_street_279',
      name: '马池口镇'
    },
    {
      key: 'beijing_gov_whlyj_street_102',
      name: '马连洼街道图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_101',
      name: '马连洼街道综合文化活动中心'
    },
    {
      key: 'beijing_gov_whlyj_street_211',
      name: '马驹桥镇综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_226',
      name: '高丽营镇'
    },
    {
      key: 'beijing_gov_whlyj_street_73',
      name: '高碑店地区'
    },
    {
      key: 'beijing_gov_whlyj_street_255',
      name: '高米店街道'
    },
    {
      key: 'beijing_gov_whlyj_street_268',
      name: '魏善庄镇'
    },
    {
      key: 'beijing_gov_whlyj_street_149',
      name: '鲁谷街道'
    },
    {
      key: 'manual',
      name: '鸿博公园'
    },
    {
      key: '北京本地宝',
      name: '鹫峰国家森林公园'
    },
    {
      key: 'beijing_gov_whlyj_street_60',
      name: '麦子店街道'
    },
    {
      key: 'beijing_gov_whlyj_street_259',
      name: '黄村镇'
    },
    {
      key: 'beijing_gov_whlyj_street_307',
      name: '黄松峪乡'
    },
    {
      key: 'beijing_gov_whlyj_street_62',
      name: '黑庄户地区'
    },
    {
      key: 'beijing_gov_whlyj_perf_43',
      name: '鼓楼西剧场'
    },
    {
      key: 'beijing_gov_whlyj_street_335',
      name: '龙山街道综合文化中心'
    },
    {
      key: 'beijing_gov_whlyj_street_161',
      name: '龙泉镇'
    },
    {
      key: 'beijing_gov_whlyj_street_301',
      name: '龙泽园街道'
    },
    {
      key: 'beijing_gov_whlyj_street_236',
      name: '龙湾屯镇'
    },
    {
      key: '北京本地宝',
      name: '龙潭湖公园'
    },
    {
      key: 'beijing_gov_whlyj_street_15',
      name: '龙潭街道图书馆'
    },
    {
      key: 'beijing_gov_whlyj_street_14',
      name: '龙潭街道综合文化中心'
    }
  ],
  hangzhou: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: 'hangzhou_gov_丁兰文体中心',
      name: '丁兰文体中心'
    },
    {
      key: 'manual',
      name: '上城区图书馆（青少年分馆）'
    },
    {
      key: 'hangzhou_gov_上城区定安路体育中心',
      name: '上城区定安路体育中心'
    },
    {
      key: 'hangzhou_gov_下城区体育中心',
      name: '下城区体育中心'
    },
    {
      key: '杭州本地宝',
      name: '东方文化园'
    },
    {
      key: '杭州本地宝',
      name: '中国丝绸博物馆'
    },
    {
      key: '杭州本地宝',
      name: '中国京杭大运河博物馆'
    },
    {
      key: '杭州本地宝',
      name: '中国伞博物馆'
    },
    {
      key: '杭州本地宝',
      name: '中国刀剪剑博物馆'
    },
    {
      key: '杭州本地宝',
      name: '中国动漫博物馆'
    },
    {
      key: '西泠印社',
      name: '中国印学博物馆'
    },
    {
      key: '杭州本地宝',
      name: '中国扇博物馆'
    },
    {
      key: '杭州本地宝',
      name: '中国杭州低碳科技馆'
    },
    {
      key: '杭州本地宝',
      name: '中国杭帮菜博物馆'
    },
    {
      key: '杭州本地宝',
      name: '中国水利博物馆'
    },
    {
      key: '杭州本地宝',
      name: '中国湿地博物馆'
    },
    {
      key: '杭州本地宝',
      name: '中国美术学院美术馆'
    },
    {
      key: '杭州本地宝',
      name: '中国茶叶博物馆'
    },
    {
      key: 'hangzhou_gov_中泰街道图书分馆',
      name: '中泰街道图书分馆'
    },
    {
      key: 'hangzhou_gov_中泰街道综合文化站',
      name: '中泰街道综合文化站'
    },
    {
      key: 'hangzhou_gov_临安文体会展中心_改建中',
      name: '临安文体会展中心(改建中)'
    },
    {
      key: 'hangzhou_gov_临平博物馆',
      name: '临平博物馆'
    },
    {
      key: 'hangzhou_gov_九堡体育中心',
      name: '九堡体育中心'
    },
    {
      key: '杭州本地宝',
      name: '九溪'
    },
    {
      key: '杭州本地宝',
      name: '九溪十八涧'
    },
    {
      key: '杭州本地宝',
      name: '云栖竹径'
    },
    {
      key: 'hangzhou_gov_五常街道图书分馆',
      name: '五常街道图书分馆'
    },
    {
      key: 'hangzhou_gov_五常街道综合文化站',
      name: '五常街道综合文化站'
    },
    {
      key: '杭州本地宝',
      name: '京杭大运河杭州景区'
    },
    {
      key: 'hangzhou_gov_仁和街道图书分馆',
      name: '仁和街道图书分馆'
    },
    {
      key: 'hangzhou_gov_仁和街道综合文化站',
      name: '仁和街道综合文化站'
    },
    {
      key: 'hangzhou_gov_仓前街道图书分馆',
      name: '仓前街道图书分馆'
    },
    {
      key: 'hangzhou_gov_仓前街道综合文化站',
      name: '仓前街道综合文化站'
    },
    {
      key: 'hangzhou_gov_余杭区体育中心_改建中',
      name: '余杭区体育中心（改建中）'
    },
    {
      key: 'hangzhou_gov_余杭区图书馆',
      name: '余杭区图书馆'
    },
    {
      key: 'hangzhou_gov_余杭区文化馆',
      name: '余杭区文化馆'
    },
    {
      key: 'hangzhou_gov_余杭区闲林体艺馆',
      name: '余杭区闲林体艺馆'
    },
    {
      key: 'manual',
      name: '余杭区青少年宫'
    },
    {
      key: 'hangzhou_gov_余杭区非遗馆',
      name: '余杭区非遗馆'
    },
    {
      key: 'hangzhou_gov_余杭小百花越剧艺术中心_苕溪大剧院',
      name: '余杭小百花越剧艺术中心（苕溪大剧院）'
    },
    {
      key: 'hangzhou_gov_余杭章太炎故居纪念馆_章太炎研究中心',
      name: '余杭章太炎故居纪念馆（章太炎研究中心）'
    },
    {
      key: 'hangzhou_gov_余杭街道图书分馆',
      name: '余杭街道图书分馆'
    },
    {
      key: 'hangzhou_gov_余杭街道综合文化站',
      name: '余杭街道综合文化站'
    },
    {
      key: '杭州本地宝',
      name: '六和塔'
    },
    {
      key: 'hangzhou_gov_区图书馆',
      name: '区图书馆'
    },
    {
      key: 'hangzhou_gov_区文化馆',
      name: '区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '南宋官窑博物馆'
    },
    {
      key: 'hangzhou_gov_图书馆东湖街道分馆_北沙书房',
      name: '图书馆东湖街道分馆（北沙书房）'
    },
    {
      key: 'hangzhou_gov_图书馆临平街道分馆_智慧分馆',
      name: '图书馆临平街道分馆（智慧分馆）'
    },
    {
      key: 'hangzhou_gov_图书馆乔司街道分馆',
      name: '图书馆乔司街道分馆'
    },
    {
      key: 'hangzhou_gov_图书馆南苑街道分馆',
      name: '图书馆南苑街道分馆'
    },
    {
      key: 'hangzhou_gov_图书馆塘栖镇分馆',
      name: '图书馆塘栖镇分馆'
    },
    {
      key: 'hangzhou_gov_图书馆崇贤街道分馆',
      name: '图书馆崇贤街道分馆'
    },
    {
      key: 'hangzhou_gov_图书馆星桥街道分馆',
      name: '图书馆星桥街道分馆'
    },
    {
      key: 'hangzhou_gov_图书馆运河街道分馆',
      name: '图书馆运河街道分馆'
    },
    {
      key: '杭州市文化广电旅游局',
      name: '天目里'
    },
    {
      key: '杭州本地宝',
      name: '太子湾公园'
    },
    {
      key: '杭州本地宝',
      name: '宋城'
    },
    {
      key: 'hangzhou_gov_富阳区体育中心',
      name: '富阳区体育中心'
    },
    {
      key: '杭州本地宝',
      name: '小河直街'
    },
    {
      key: '杭州本地宝',
      name: '岳庙'
    },
    {
      key: 'hangzhou_gov_建德市新安江体育馆',
      name: '建德市新安江体育馆'
    },
    {
      key: 'hangzhou_gov_径山镇乡镇综合文化站',
      name: '径山镇乡镇综合文化站'
    },
    {
      key: 'hangzhou_gov_径山镇图书分馆',
      name: '径山镇图书分馆'
    },
    {
      key: 'hangzhou_gov_拱墅区体育馆',
      name: '拱墅区体育馆'
    },
    {
      key: 'hangzhou_gov_拱墅区文体中心',
      name: '拱墅区文体中心'
    },
    {
      key: '杭州本地宝',
      name: '拱宸桥'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州上城区青少年宫'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州下城区青少年宫'
    },
    {
      key: '杭州本地宝',
      name: '杭州中国湿地博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州中国茶叶博物馆龙井馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州临安区青少年宫'
    },
    {
      key: '杭州本地宝',
      name: '杭州临平新城'
    },
    {
      key: '杭州本地宝',
      name: '杭州临平新城体育公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州临平新城市民广场'
    },
    {
      key: '杭州本地宝',
      name: '杭州临平新城文化艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州之江文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州之江文化中心博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州之江文化中心图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州之江文化中心科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州之江文化中心美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州乐园'
    },
    {
      key: '杭州本地宝',
      name: '杭州九堡大桥'
    },
    {
      key: '杭州本地宝',
      name: '杭州九堡大桥公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州九溪烟树'
    },
    {
      key: '杭州本地宝',
      name: '杭州云栖竹径'
    },
    {
      key: '杭州本地宝',
      name: '杭州亚运会博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州京杭大运河博物馆'
    },
    {
      key: 'hangzhou_gov_杭州体育场',
      name: '杭州体育场'
    },
    {
      key: 'hangzhou_gov_杭州体育馆',
      name: '杭州体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州余杭区艺术中心'
    },
    {
      key: 'hangzhou_gov_杭州全民健身中心',
      name: '杭州全民健身中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州六和塔'
    },
    {
      key: 'manual',
      name: '杭州动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州南宋御街'
    },
    {
      key: '杭州本地宝',
      name: '杭州南屏晚钟'
    },
    {
      key: '杭州本地宝',
      name: '杭州博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州双峰插云'
    },
    {
      key: '杭州本地宝',
      name: '杭州吴山天风'
    },
    {
      key: '杭州本地宝',
      name: '杭州嘟嘟城'
    },
    {
      key: '杭州本地宝',
      name: '杭州国际会议中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州国际会议中心大剧场'
    },
    {
      key: '杭州市文化广电旅游局',
      name: '杭州国际博览中心'
    },
    {
      key: 'manual',
      name: '杭州图书馆'
    },
    {
      key: '杭州图书馆官网',
      name: '杭州图书馆少儿分馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州城市阳台'
    },
    {
      key: '杭州本地宝',
      name: '杭州城市阳台灯光秀'
    },
    {
      key: 'hangzhou_gov_杭州大关游泳健身馆',
      name: '杭州大关游泳健身馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州大剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州大剧院歌剧厅'
    },
    {
      key: '杭州本地宝',
      name: '杭州大剧院音乐厅'
    },
    {
      key: '杭州本地宝',
      name: '杭州太子湾公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州奥体中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州奥体中心体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州奥体中心游泳馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州奥体中心网球中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州奥体博览城'
    },
    {
      key: '杭州本地宝',
      name: '杭州奥体博览城游泳馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州奥体博览城网球中心'
    },
    {
      key: '宋城演艺',
      name: '杭州宋城'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州富阳区青少年宫'
    },
    {
      key: '杭州本地宝',
      name: '杭州小河直街'
    },
    {
      key: '杭州本地宝',
      name: '杭州少年儿童图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州岳庙'
    },
    {
      key: '杭州本地宝',
      name: '杭州工艺美术博物馆'
    },
    {
      key: 'hangzhou_gov_杭州市体育事业发展中心杭州体育场',
      name: '杭州市体育事业发展中心杭州体育场'
    },
    {
      key: 'hangzhou_gov_杭州市体育事业发展中心杭州体育馆_改建中',
      name: '杭州市体育事业发展中心杭州体育馆（改建中）'
    },
    {
      key: 'hangzhou_gov_杭州市体育事业发展中心杭州全民健身中心_在建',
      name: '杭州市体育事业发展中心杭州全民健身中心（在建）'
    },
    {
      key: 'hangzhou_gov_杭州市体育事业发展中心杭州大关游泳健身馆',
      name: '杭州市体育事业发展中心杭州大关游泳健身馆'
    },
    {
      key: 'hangzhou_gov_杭州市体育事业发展中心杭州游泳健身馆',
      name: '杭州市体育事业发展中心杭州游泳健身馆'
    },
    {
      key: 'hangzhou_gov_杭州市奥体中心',
      name: '杭州市奥体中心'
    },
    {
      key: 'hangzhou_gov_杭州市滨江区图书馆',
      name: '杭州市滨江区图书馆'
    },
    {
      key: 'hangzhou_gov_杭州市滨江区文化馆',
      name: '杭州市滨江区文化馆'
    },
    {
      key: 'hangzhou_gov_杭州市滨江区非物质文化遗产馆',
      name: '杭州市滨江区非物质文化遗产馆'
    },
    {
      key: 'hangzhou_gov_杭州市职工文化中心',
      name: '杭州市职工文化中心'
    },
    {
      key: 'hangzhou_gov_杭州市西湖区图书馆',
      name: '杭州市西湖区图书馆'
    },
    {
      key: 'hangzhou_gov_杭州市西湖区文化馆',
      name: '杭州市西湖区文化馆'
    },
    {
      key: 'hangzhou_gov_杭州市陈经纶体育学校',
      name: '杭州市陈经纶体育学校'
    },
    {
      key: '杭州本地宝',
      name: '杭州平湖秋月'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州建德市艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱墅区青少年宫'
    },
    {
      key: '杭州本地宝',
      name: '杭州拱宸桥'
    },
    {
      key: '杭州本地宝',
      name: '杭州文学馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州文学馆展览厅'
    },
    {
      key: '杭州本地宝',
      name: '杭州文学馆阅读室'
    },
    {
      key: '杭州本地宝',
      name: '杭州曲院风荷'
    },
    {
      key: '杭州本地宝',
      name: '杭州未来科技城'
    },
    {
      key: '杭州本地宝',
      name: '杭州未来科技城人才公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州未来科技城学术交流中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州未来科技城梦想小镇'
    },
    {
      key: '杭州本地宝',
      name: '杭州未来科技城海创园'
    },
    {
      key: '杭州本地宝',
      name: '杭州极地海洋世界'
    },
    {
      key: '杭州本地宝',
      name: '杭州极地海洋世界海豚表演'
    },
    {
      key: '杭州本地宝',
      name: '杭州极地海洋世界白鲸表演'
    },
    {
      key: '杭州本地宝',
      name: '杭州柳浪闻莺'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州桐庐县青少年宫'
    },
    {
      key: '杭州本地宝',
      name: '杭州桥西直街'
    },
    {
      key: '杭州本地宝',
      name: '杭州梦想小镇'
    },
    {
      key: '杭州本地宝',
      name: '杭州梦想小镇创业大街'
    },
    {
      key: '杭州本地宝',
      name: '杭州植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州武林广场'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州江干区青少年宫'
    },
    {
      key: '杭州本地宝',
      name: '杭州河坊街'
    },
    {
      key: '杭州本地宝',
      name: '杭州涌金公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州淳安县青少年宫'
    },
    {
      key: 'hangzhou_gov_杭州游泳健身馆',
      name: '杭州游泳健身馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州湖滨银泰'
    },
    {
      key: '杭州本地宝',
      name: '杭州湘湖'
    },
    {
      key: '杭州本地宝',
      name: '杭州湘湖游船'
    },
    {
      key: '杭州本地宝',
      name: '杭州湘湖音乐喷泉'
    },
    {
      key: '杭州本地宝',
      name: '杭州满陇桂雨'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州滨江区青少年宫'
    },
    {
      key: '杭州本地宝',
      name: '杭州灵隐寺'
    },
    {
      key: '杭州本地宝',
      name: '杭州白堤'
    },
    {
      key: '杭州本地宝',
      name: '杭州白马湖国际会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州白马湖国际会展中心展览厅'
    },
    {
      key: '杭州本地宝',
      name: '杭州科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州花港观鱼'
    },
    {
      key: '杭州本地宝',
      name: '杭州苏堤'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州萧山区青少年宫'
    },
    {
      key: '杭州本地宝',
      name: '杭州虎跑公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖三潭印月'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区会展中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区体育场'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区体育馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区公园'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区创意园'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区图书馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区文化中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区海洋馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区科技馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区美术馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区艺术中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖区青少年宫'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖南屏晚钟'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖双峰插云'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖吴山天风'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖平湖秋月'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖断桥残雪'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖曲院风荷'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖杨公堤'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖柳浪闻莺'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖游船'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖湖心亭'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖花港观鱼'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖苏堤春晓'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖阮公墩'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖雷峰夕照'
    },
    {
      key: '杭州本地宝',
      name: '杭州西湖音乐喷泉'
    },
    {
      key: '杭州本地宝',
      name: '杭州西溪湿地东区'
    },
    {
      key: '杭州本地宝',
      name: '杭州西溪湿地博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州西溪湿地摇橹船'
    },
    {
      key: '杭州本地宝',
      name: '杭州西溪湿地植物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州西溪湿地西区'
    },
    {
      key: '杭州本地宝',
      name: '杭州西溪湿地龙舟赛'
    },
    {
      key: '杭州本地宝',
      name: '杭州跨湖桥遗址博物馆'
    },
    {
      key: '杭州本地宝',
      name: '杭州运河夜游'
    },
    {
      key: '浙江交响乐团',
      name: '杭州运河大剧院'
    },
    {
      key: '杭州本地宝',
      name: '杭州运河广场'
    },
    {
      key: '杭州本地宝',
      name: '杭州运河文化广场'
    },
    {
      key: '杭州本地宝',
      name: '杭州运河游船'
    },
    {
      key: '杭州本地宝',
      name: '杭州野生动物世界'
    },
    {
      key: '杭州本地宝',
      name: '杭州野生动物园'
    },
    {
      key: '杭州本地宝',
      name: '杭州钱江新城'
    },
    {
      key: '杭州本地宝',
      name: '杭州钱江新城灯光秀'
    },
    {
      key: '杭州本地宝',
      name: '杭州钱王祠'
    },
    {
      key: '杭州本地宝',
      name: '杭州雷峰塔'
    },
    {
      key: '杭州本地宝',
      name: '杭州青少年活动中心'
    },
    {
      key: '杭州本地宝',
      name: '杭州鼓楼'
    },
    {
      key: '杭州本地宝',
      name: '杭州龙井村'
    },
    {
      key: 'hangzhou_gov_桐庐县体育馆',
      name: '桐庐县体育馆'
    },
    {
      key: 'hangzhou_gov_桐庐县分水镇文体中心',
      name: '桐庐县分水镇文体中心'
    },
    {
      key: 'hangzhou_gov_桐庐县城北体育健身中心',
      name: '桐庐县城北体育健身中心'
    },
    {
      key: 'hangzhou_gov_桐庐县横村镇文体中心',
      name: '桐庐县横村镇文体中心'
    },
    {
      key: 'hangzhou_gov_江南体育中心',
      name: '江南体育中心'
    },
    {
      key: 'hangzhou_gov_江干区体育中心',
      name: '江干区体育中心'
    },
    {
      key: '杭州本地宝',
      name: '浙江图书馆'
    },
    {
      key: 'zjam',
      name: '浙江省博物馆'
    },
    {
      key: '杭州市文化广电旅游局',
      name: '浙江省博物馆之江馆'
    },
    {
      key: '浙江省博物馆',
      name: '浙江省博物馆之江馆区'
    },
    {
      key: '浙江省博物馆',
      name: '浙江省博物馆武林馆区'
    },
    {
      key: '杭州本地宝',
      name: '浙江省博物馆（之江馆）'
    },
    {
      key: '杭州本地宝',
      name: '浙江省博物馆（孤山馆）'
    },
    {
      key: '杭州本地宝',
      name: '浙江省地质博物馆'
    },
    {
      key: '浙江省文化馆',
      name: '浙江省文化馆'
    },
    {
      key: '杭州本地宝',
      name: '浙江省科技馆'
    },
    {
      key: '杭州本地宝',
      name: '浙江省非物质文化遗产馆'
    },
    {
      key: '杭州本地宝',
      name: '浙江美术馆'
    },
    {
      key: '浙江自然博物院',
      name: '浙江自然博物院'
    },
    {
      key: '浙江自然博物院',
      name: '浙江自然博物院杭州馆'
    },
    {
      key: '杭州本地宝',
      name: '浙江自然博物院（杭州馆）'
    },
    {
      key: 'hangzhou_gov_淳安县体育馆',
      name: '淳安县体育馆'
    },
    {
      key: '杭州本地宝',
      name: '清河坊街'
    },
    {
      key: '杭州本地宝',
      name: '湖滨步行街'
    },
    {
      key: '杭州本地宝',
      name: '湘湖'
    },
    {
      key: '杭州本地宝',
      name: '湘湖旅游度假区'
    },
    {
      key: '杭州本地宝',
      name: '满觉陇'
    },
    {
      key: 'hangzhou_gov_滨江区体育馆',
      name: '滨江区体育馆'
    },
    {
      key: '杭州本地宝',
      name: '灵山风景区'
    },
    {
      key: '杭州本地宝',
      name: '灵隐寺'
    },
    {
      key: '杭州本地宝',
      name: '烂苹果乐园'
    },
    {
      key: 'hangzhou_gov_瓶窑镇图书分馆',
      name: '瓶窑镇图书分馆'
    },
    {
      key: 'hangzhou_gov_瓶窑镇综合文化站',
      name: '瓶窑镇综合文化站'
    },
    {
      key: '杭州本地宝',
      name: '白龙潭景区'
    },
    {
      key: 'hangzhou_gov_百丈镇图书分馆',
      name: '百丈镇图书分馆'
    },
    {
      key: 'hangzhou_gov_百丈镇综合文化站',
      name: '百丈镇综合文化站'
    },
    {
      key: '杭州本地宝',
      name: '胡庆余堂中药博物馆'
    },
    {
      key: '杭州本地宝',
      name: '良渚博物院'
    },
    {
      key: '杭州本地宝',
      name: '良渚古城遗址公园'
    },
    {
      key: 'hangzhou_gov_良渚街道图书分馆',
      name: '良渚街道图书分馆'
    },
    {
      key: 'hangzhou_gov_良渚街道综合文化站',
      name: '良渚街道综合文化站'
    },
    {
      key: 'hangzhou_gov_萧山区临浦镇文体中心_改建中',
      name: '萧山区临浦镇文体中心（改建中）'
    },
    {
      key: 'hangzhou_gov_萧山区体育中心',
      name: '萧山区体育中心'
    },
    {
      key: 'hangzhou_gov_萧山区瓜沥镇文体中心',
      name: '萧山区瓜沥镇文体中心'
    },
    {
      key: 'hangzhou_gov_萧山区衙前镇文体中心',
      name: '萧山区衙前镇文体中心'
    },
    {
      key: '杭州本地宝',
      name: '虎跑'
    },
    {
      key: '杭州本地宝',
      name: '虎跑公园'
    },
    {
      key: 'hangzhou_gov_西湖区文体中心',
      name: '西湖区文体中心'
    },
    {
      key: 'manual',
      name: '西湖区文化馆'
    },
    {
      key: '杭州本地宝',
      name: '西湖博物馆'
    },
    {
      key: '杭州本地宝',
      name: '西湖景区'
    },
    {
      key: '杭州本地宝',
      name: '西湖音乐喷泉'
    },
    {
      key: '杭州本地宝',
      name: '西湖音乐节'
    },
    {
      key: '杭州本地宝',
      name: '西湖风景名胜区'
    },
    {
      key: '杭州本地宝',
      name: '西溪国家湿地公园'
    },
    {
      key: '杭州本地宝',
      name: '西溪湿地'
    },
    {
      key: 'manual',
      name: '西溪湿地公园'
    },
    {
      key: '杭州本地宝',
      name: '西溪湿地洪园'
    },
    {
      key: '杭州本地宝',
      name: '超山风景区'
    },
    {
      key: '杭州本地宝',
      name: '跨湖桥遗址博物馆'
    },
    {
      key: '杭州本地宝',
      name: '长乔极地海洋公园'
    },
    {
      key: 'hangzhou_gov_闲林街道图书分馆',
      name: '闲林街道图书分馆'
    },
    {
      key: 'hangzhou_gov_闲林街道综合文化站',
      name: '闲林街道综合文化站'
    },
    {
      key: '杭州本地宝',
      name: '雷峰塔'
    },
    {
      key: '杭州本地宝',
      name: '韩美林艺术馆'
    },
    {
      key: 'hangzhou_gov_鸬鸟镇乡镇综合文化站',
      name: '鸬鸟镇乡镇综合文化站'
    },
    {
      key: 'hangzhou_gov_鸬鸟镇图书分馆',
      name: '鸬鸟镇图书分馆'
    },
    {
      key: 'hangzhou_gov_黄湖镇图书分馆',
      name: '黄湖镇图书分馆'
    },
    {
      key: 'hangzhou_gov_黄湖镇综合文化站',
      name: '黄湖镇综合文化站'
    },
    {
      key: '杭州本地宝',
      name: '龙井'
    },
    {
      key: '杭州本地宝',
      name: '龙井村'
    }
  ],
  chengdu: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: '成都本地宝',
      name: '三圣花乡'
    },
    {
      key: '成都本地宝',
      name: '人民公园'
    },
    {
      key: '成都本地宝',
      name: '兴隆湖湿地公园'
    },
    {
      key: '成都本地宝',
      name: '四川博物院'
    },
    {
      key: '成都本地宝',
      name: '四川省体育馆'
    },
    {
      key: '成都本地宝',
      name: '四川省图书馆'
    },
    {
      key: '成都本地宝',
      name: '四川科技馆'
    },
    {
      key: '成都本地宝',
      name: '国际非遗博览园'
    },
    {
      key: '成都本地宝',
      name: '天府人文艺术图书馆'
    },
    {
      key: '成都本地宝',
      name: '天府绿道'
    },
    {
      key: '成都本地宝',
      name: '安仁古镇'
    },
    {
      key: '成都本地宝',
      name: '宽窄巷子'
    },
    {
      key: '成都本地宝',
      name: '平乐古镇'
    },
    {
      key: '成都本地宝',
      name: '成都IFS国际金融中心'
    },
    {
      key: '成都本地宝',
      name: '成都万象城'
    },
    {
      key: '成都本地宝',
      name: '成都亲子游泳馆'
    },
    {
      key: '成都本地宝',
      name: '成都体育学院'
    },
    {
      key: '成都本地宝',
      name: '成都体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都冰场'
    },
    {
      key: '成都本地宝',
      name: '成都击剑馆'
    },
    {
      key: '成都本地宝',
      name: '成都动物园'
    },
    {
      key: '成都本地宝',
      name: '成都博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都双流区体育场'
    },
    {
      key: '成都本地宝',
      name: '成都双流区体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都双流区公园'
    },
    {
      key: '成都本地宝',
      name: '成都双流区创意园'
    },
    {
      key: '成都本地宝',
      name: '成都双流区剧院'
    },
    {
      key: '成都本地宝',
      name: '成都双流区动物园'
    },
    {
      key: '成都本地宝',
      name: '成都双流区博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都双流区图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都双流区文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都双流区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都双流区植物园'
    },
    {
      key: '成都本地宝',
      name: '成都双流区海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都双流区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都双流区艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都国色天乡乐园'
    },
    {
      key: '成都本地宝',
      name: '成都图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都大悦城'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区体育场'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区公园'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区创意园'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区动物园'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区植物园'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都天府新区艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都射箭馆'
    },
    {
      key: '成都本地宝',
      name: '成都川剧院'
    },
    {
      key: '成都本地宝',
      name: '成都市游泳馆'
    },
    {
      key: '成都本地宝',
      name: '成都平衡车场'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市体育场'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市剧院'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市动物园'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市植物园'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都彭州市青少年宫'
    },
    {
      key: '成都本地宝',
      name: '成都成华区会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都成华区体育场'
    },
    {
      key: '成都本地宝',
      name: '成都成华区体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都成华区公园'
    },
    {
      key: '成都本地宝',
      name: '成都成华区创意园'
    },
    {
      key: '成都本地宝',
      name: '成都成华区动物园'
    },
    {
      key: '成都本地宝',
      name: '成都成华区博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都成华区图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都成华区文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都成华区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都成华区海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都成华区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都成华区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都成华区艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都成华区青少年宫'
    },
    {
      key: '成都本地宝',
      name: '成都攀岩馆'
    },
    {
      key: '成都本地宝',
      name: '成都新都区会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都新都区体育场'
    },
    {
      key: '成都本地宝',
      name: '成都新都区体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都新都区公园'
    },
    {
      key: '成都本地宝',
      name: '成都新都区创意园'
    },
    {
      key: '成都本地宝',
      name: '成都新都区剧院'
    },
    {
      key: '成都本地宝',
      name: '成都新都区动物园'
    },
    {
      key: '成都本地宝',
      name: '成都新都区文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都新都区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都新都区植物园'
    },
    {
      key: '成都本地宝',
      name: '成都新都区海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都新都区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都新都区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都新都区青少年宫'
    },
    {
      key: '成都本地宝',
      name: '成都杜甫草堂博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都来福士广场'
    },
    {
      key: '成都本地宝',
      name: '成都植物园'
    },
    {
      key: '成都本地宝',
      name: '成都欢乐谷'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区体育场'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区创意园'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区剧院'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区动物园'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区植物园'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都武侯区青少年宫'
    },
    {
      key: '成都本地宝',
      name: '成都武侯祠博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都武术馆'
    },
    {
      key: '成都本地宝',
      name: '成都海昌极地海洋公园'
    },
    {
      key: '成都本地宝',
      name: '成都温江区会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都温江区体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都温江区公园'
    },
    {
      key: '成都本地宝',
      name: '成都温江区创意园'
    },
    {
      key: '成都本地宝',
      name: '成都温江区剧院'
    },
    {
      key: '成都本地宝',
      name: '成都温江区动物园'
    },
    {
      key: '成都本地宝',
      name: '成都温江区图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都温江区文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都温江区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都温江区植物园'
    },
    {
      key: '成都本地宝',
      name: '成都温江区海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都温江区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都温江区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都温江区青少年宫'
    },
    {
      key: '成都本地宝',
      name: '成都滑板场'
    },
    {
      key: '成都本地宝',
      name: '成都环球中心'
    },
    {
      key: '成都本地宝',
      name: '成都瑜伽馆'
    },
    {
      key: '成都本地宝',
      name: '成都融创水世界'
    },
    {
      key: '成都本地宝',
      name: '成都足球训练基地'
    },
    {
      key: '成都本地宝',
      name: '成都跆拳道馆'
    },
    {
      key: '成都本地宝',
      name: '成都跑酷场'
    },
    {
      key: '成都本地宝',
      name: '成都蹦床馆'
    },
    {
      key: '成都本地宝',
      name: '成都轮滑场'
    },
    {
      key: '成都本地宝',
      name: '成都远洋太古里'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区体育场'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区公园'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区剧院'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区动物园'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区植物园'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都郫都区青少年宫'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市体育场'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市公园'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市创意园'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市剧院'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市动物园'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市植物园'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都都江堰市艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都金沙遗址博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区体育场'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区公园'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区创意园'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区剧院'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区植物园'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都金牛区青少年宫'
    },
    {
      key: '成都本地宝',
      name: '成都银泰中心'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区体育场'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区公园'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区创意园'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区剧院'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区动物园'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都锦江区青少年宫'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区体育场'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区公园'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区创意园'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区剧院'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区植物园'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都青羊区青少年宫'
    },
    {
      key: '成都本地宝',
      name: '成都马术俱乐部'
    },
    {
      key: '成都本地宝',
      name: '成都高尔夫球场'
    },
    {
      key: '成都本地宝',
      name: '成都高新区会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都高新区体育馆'
    },
    {
      key: '成都本地宝',
      name: '成都高新区公园'
    },
    {
      key: '成都本地宝',
      name: '成都高新区创意园'
    },
    {
      key: '成都本地宝',
      name: '成都高新区剧院'
    },
    {
      key: '成都本地宝',
      name: '成都高新区动物园'
    },
    {
      key: '成都本地宝',
      name: '成都高新区博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都高新区图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都高新区文化中心'
    },
    {
      key: '成都本地宝',
      name: '成都高新区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都高新区植物园'
    },
    {
      key: '成都本地宝',
      name: '成都高新区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都高新区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都高新区青少年宫'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区会展中心'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区体育场'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区公园'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区剧院'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区动物园'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区博物馆'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区图书馆'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区文化馆'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区植物园'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区海洋馆'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区科技馆'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区美术馆'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区艺术中心'
    },
    {
      key: '成都本地宝',
      name: '成都龙泉驿区青少年宫'
    },
    {
      key: '成都本地宝',
      name: '洛带古镇'
    },
    {
      key: '成都本地宝',
      name: '浣花溪公园'
    },
    {
      key: '成都本地宝',
      name: '环球中心天堂岛海洋乐园'
    },
    {
      key: '成都本地宝',
      name: '白鹭湾湿地公园'
    },
    {
      key: '成都本地宝',
      name: '蜀锦织绣博物馆'
    },
    {
      key: '成都本地宝',
      name: '街子古镇'
    },
    {
      key: '成都本地宝',
      name: '锦城湖公园'
    },
    {
      key: '成都本地宝',
      name: '锦江绿道'
    },
    {
      key: '成都本地宝',
      name: '锦里'
    },
    {
      key: '成都本地宝',
      name: '青龙湖湿地公园'
    },
    {
      key: '成都本地宝',
      name: '黄龙溪古镇'
    }
  ],
  chongqing: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: 'chongqing_gov_bowuguan_31',
      name: '万县“九五”惨案纪念馆'
    },
    {
      key: 'chongqing_gov_tiyu_8',
      name: '万州体育场'
    },
    {
      key: 'chongqing_gov_tiyu_7',
      name: '万州区三峡之星体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_6',
      name: '万州游泳（跳水）馆'
    },
    {
      key: 'chongqing_gov_bowuguan_34',
      name: '万涛故居'
    },
    {
      key: 'chongqing_gov_tiyu_19',
      name: '万盛文体中心体育场'
    },
    {
      key: 'chongqing_gov_tiyu_18',
      name: '万盛文体中心体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_21',
      name: '万盛游泳馆'
    },
    {
      key: 'chongqing_gov_tiyu_20',
      name: '万盛滨江路体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_57',
      name: '东安镇全民健身中心'
    },
    {
      key: 'chongqing_gov_bowuguan_76',
      name: '中共中央西南局缙云山办公地旧址陈列馆'
    },
    {
      key: 'chongqing_gov_bowuguan_23',
      name: '中国西部科学院旧址陈列馆'
    },
    {
      key: 'chongqing_gov_bowuguan_92',
      name: '中等师范教育历史陈列馆'
    },
    {
      key: 'chongqing_gov_tiyu_62',
      name: '丰都县体育场'
    },
    {
      key: 'chongqing_gov_tiyu_61',
      name: '丰都县体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_126',
      name: '丰都县博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_151',
      name: '九黎苗族历史文化博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_14',
      name: '二厂记忆博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_70',
      name: '云阳县体育场'
    },
    {
      key: 'chongqing_gov_tiyu_69',
      name: '云阳县体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_68',
      name: '云阳县全民健身活动中心'
    },
    {
      key: 'chongqing_gov_bowuguan_130',
      name: '云阳县博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_133',
      name: '云阳县彭咏梧纪念馆'
    },
    {
      key: 'chongqing_gov_tiyu_71',
      name: '云阳县游泳中心'
    },
    {
      key: 'chongqing_gov_bowuguan_134',
      name: '云阳县非物质文化遗产博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_132',
      name: '云阳古建博物苑'
    },
    {
      key: '重庆本地宝',
      name: '仙女山国家森林公园'
    },
    {
      key: 'chongqing_gov_bowuguan_58',
      name: '刘伯承六店旧居纪念馆（刘伯承六店旧居管理中心）'
    },
    {
      key: 'chongqing_gov_bowuguan_117',
      name: '刘伯承同志纪念馆'
    },
    {
      key: 'chongqing_gov_bowuguan_146',
      name: '刘邓大军挺进大西南司令部旧址陈列馆'
    },
    {
      key: '重庆本地宝',
      name: '北滨路'
    },
    {
      key: 'chongqing_gov_bowuguan_79',
      name: '北碚教育博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_17',
      name: '北陪区绪云体育中心体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_16',
      name: '北陪区缙云体育中心体育场'
    },
    {
      key: '重庆本地宝',
      name: '十八梯'
    },
    {
      key: '重庆本地宝',
      name: '南山'
    },
    {
      key: '重庆本地宝',
      name: '南山一棵树观景台'
    },
    {
      key: '重庆本地宝',
      name: '南山植物园'
    },
    {
      key: 'chongqing_gov_bowuguan_66',
      name: '南岸区博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_40',
      name: '南川区体育场'
    },
    {
      key: 'chongqing_gov_tiyu_41',
      name: '南川区体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_101',
      name: '南川区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '南滨路'
    },
    {
      key: 'chongqing_gov_bowuguan_149',
      name: '南腰界红三军司令部旧址陈列馆'
    },
    {
      key: 'chongqing_gov_bowuguan_70',
      name: '卢作孚纪念馆'
    },
    {
      key: 'chongqing_gov_tiyu_36',
      name: '合川区体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_97',
      name: '合川区楠山坊金丝楠木博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_122',
      name: '后坪坝苏维埃政府史迹展览馆'
    },
    {
      key: '重庆本地宝',
      name: '周公馆'
    },
    {
      key: 'chongqing_gov_bowuguan_123',
      name: '和平中学旧址陈列馆'
    },
    {
      key: 'chongqing_gov_bowuguan_71',
      name: '四世同堂纪念馆'
    },
    {
      key: '重庆本地宝',
      name: '国泰艺术中心'
    },
    {
      key: 'chongqing_gov_bowuguan_75',
      name: '国立复旦大学重庆旧址（抗战时期复旦大学校史纪念馆）'
    },
    {
      key: 'chongqing_gov_tiyu_65',
      name: '垫江县体育场'
    },
    {
      key: 'chongqing_gov_tiyu_64',
      name: '垫江县体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_66',
      name: '垫江县全民健身中心'
    },
    {
      key: 'chongqing_gov_bowuguan_127',
      name: '垫江县博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_59',
      name: '城口县体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_58',
      name: '城口县岗天乡全民健身中心'
    },
    {
      key: 'chongqing_gov_bowuguan_125',
      name: '城口县红三十三军指挥部旧址群陈列馆'
    },
    {
      key: 'chongqing_gov_tiyu_11',
      name: '大渡口区体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_26',
      name: '大足区体育中心体育场'
    },
    {
      key: 'chongqing_gov_tiyu_25',
      name: '大足区体育中心体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_24',
      name: '大足区体育中心游泳馆'
    },
    {
      key: '重庆本地宝',
      name: '大足石刻'
    },
    {
      key: 'chongqing_gov_bowuguan_4',
      name: '大足石刻博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_135',
      name: '奉节县夔州博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_136',
      name: '奉节县白帝城博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_137',
      name: '奉节县瞿塘关遗址博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_138',
      name: '奉节县诗城博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_124',
      name: '川陕苏区城口纪念馆'
    },
    {
      key: 'chongqing_gov_bowuguan_139',
      name: '巫山博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_141',
      name: '巫山县下庄人事迹陈列馆'
    },
    {
      key: 'chongqing_gov_tiyu_74',
      name: '巫山县体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_75',
      name: '巫山县全民健身中心'
    },
    {
      key: 'chongqing_gov_bowuguan_140',
      name: '巫山县李季达陈列馆'
    },
    {
      key: 'chongqing_gov_tiyu_72',
      name: '巫山县章家湾训练中心'
    },
    {
      key: 'chongqing_gov_bowuguan_142',
      name: '巫山县长康博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_143',
      name: '巫溪县博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_56',
      name: '庙坝镇全民健身中心'
    },
    {
      key: 'chongqing_gov_tiyu_85',
      name: '开州区体育场'
    },
    {
      key: 'chongqing_gov_tiyu_83',
      name: '开州区体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_84',
      name: '开州区游泳馆'
    },
    {
      key: 'chongqing_gov_bowuguan_114',
      name: '张培爵纪念馆'
    },
    {
      key: 'chongqing_gov_bowuguan_131',
      name: '张桓侯庙博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_77',
      name: '张自忠烈士陵园'
    },
    {
      key: '重庆本地宝',
      name: '彩云湖湿地公园'
    },
    {
      key: 'chongqing_gov_tiyu_80',
      name: '彭水县体育场'
    },
    {
      key: 'chongqing_gov_tiyu_81',
      name: '彭水县体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_82',
      name: '彭水县全民健身中心'
    },
    {
      key: 'chongqing_gov_bowuguan_150',
      name: '彭水苗族土家族自治县博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_67',
      name: '忠县体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_129',
      name: '忠县石宝寨'
    },
    {
      key: 'chongqing_gov_bowuguan_128',
      name: '忠州博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_73',
      name: '抗战时期荣誉军人自治实验区陈列馆（重庆市北碚区博物馆分馆）'
    },
    {
      key: 'chongqing_gov_bowuguan_48',
      name: '明玉珍睿陵陈列馆'
    },
    {
      key: 'chongqing_gov_bowuguan_74',
      name: '晏阳初纪念馆（重庆市北碚区博物馆分馆）'
    },
    {
      key: '重庆本地宝',
      name: '朝天门广场'
    },
    {
      key: 'chongqing_gov_bowuguan_112',
      name: '杨闇公杨尚昆旧居陈列馆（重庆市潼南区杨尚昆故里管理处）'
    },
    {
      key: '重庆本地宝',
      name: '桂园'
    },
    {
      key: 'chongqing_gov_bowuguan_72',
      name: '梁实秋纪念馆'
    },
    {
      key: 'chongqing_gov_tiyu_86',
      name: '梁平区东门体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_87',
      name: '梁平区东门游泳馆'
    },
    {
      key: '重庆本地宝',
      name: '歌乐山国家森林公园'
    },
    {
      key: '重庆本地宝',
      name: '歌乐山烈士陵园'
    },
    {
      key: 'chongqing_gov_tiyu_55',
      name: '武隆区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '武隆喀斯特'
    },
    {
      key: 'chongqing_gov_tiyu_38',
      name: '永川区体育中心体育场'
    },
    {
      key: 'chongqing_gov_tiyu_39',
      name: '永川区体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_37',
      name: '永川区游泳馆'
    },
    {
      key: 'chongqing_gov_bowuguan_98',
      name: '永川博物馆（陈子庄艺术陈列馆）'
    },
    {
      key: '重庆本地宝',
      name: '江北嘴'
    },
    {
      key: '重庆本地宝',
      name: '江北嘴中央公园'
    },
    {
      key: 'chongqing_gov_tiyu_12',
      name: '江南体育中心体育训练场'
    },
    {
      key: 'chongqing_gov_tiyu_13',
      name: '江南体育中心综合馆'
    },
    {
      key: 'chongqing_gov_tiyu_15',
      name: '江南体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_14',
      name: '江南游泳馆'
    },
    {
      key: 'chongqing_gov_tiyu_33',
      name: '江津区体育场'
    },
    {
      key: 'chongqing_gov_tiyu_32',
      name: '江津区体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_35',
      name: '江津区全民健身指导中心（区羽毛球馆）'
    },
    {
      key: 'chongqing_gov_tiyu_34',
      name: '江津区游泳馆'
    },
    {
      key: 'chongqing_gov_bowuguan_89',
      name: '江津博物馆'
    },
    {
      key: '重庆本地宝',
      name: '洪崖洞'
    },
    {
      key: 'chongqing_gov_tiyu_9',
      name: '涪陵区体育场'
    },
    {
      key: 'chongqing_gov_tiyu_10',
      name: '涪陵区体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_46',
      name: '渝中区古典戏法魔术博物馆'
    },
    {
      key: '重庆本地宝',
      name: '渣滓洞'
    },
    {
      key: '重庆本地宝',
      name: '湖广会馆'
    },
    {
      key: 'chongqing_gov_tiyu_49',
      name: '潼南区体育场'
    },
    {
      key: 'chongqing_gov_tiyu_50',
      name: '潼南区体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_111',
      name: '潼南区博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_78',
      name: '王朴烈士陵园'
    },
    {
      key: 'chongqing_gov_bowuguan_39',
      name: '王琦美术博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_44',
      name: '璧山区体育中心'
    },
    {
      key: 'chongqing_gov_tiyu_43',
      name: '璧山区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '白公馆'
    },
    {
      key: 'chongqing_gov_tiyu_76',
      name: '石柱县体育场'
    },
    {
      key: 'chongqing_gov_tiyu_77',
      name: '石柱县体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_144',
      name: '石柱土家族自治县博物馆'
    },
    {
      key: '重庆本地宝',
      name: '磁器口古镇'
    },
    {
      key: 'chongqing_gov_tiyu_78',
      name: '秀山体育场'
    },
    {
      key: 'chongqing_gov_tiyu_79',
      name: '秀山体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_145',
      name: '秀山土家族苗族自治县民族博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_22',
      name: '綦江体育中心体育场'
    },
    {
      key: 'chongqing_gov_tiyu_23',
      name: '綦江区体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_103',
      name: '綦江博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_2',
      name: '红岩革命纪念馆（重庆红岩革命历史博物馆）'
    },
    {
      key: '重庆本地宝',
      name: '缙云山自然保护区'
    },
    {
      key: 'chongqing_gov_bowuguan_90',
      name: '聂荣臻元帅陈列馆'
    },
    {
      key: 'chongqing_gov_tiyu_52',
      name: '荣昌区体育中心游泳池'
    },
    {
      key: 'chongqing_gov_tiyu_51',
      name: '荣昌区体育场'
    },
    {
      key: 'chongqing_gov_tiyu_54',
      name: '荣昌区体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_53',
      name: '荣昌区全民健身活动中心'
    },
    {
      key: 'chongqing_gov_bowuguan_113',
      name: '荣昌陶博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_22',
      name: '西南大学历史博物馆'
    },
    {
      key: '重庆本地宝',
      name: '解放碑步行街'
    },
    {
      key: 'chongqing_gov_tiyu_88',
      name: '酉阳县体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_148',
      name: '酉阳土家族苗族自治县赵世炎烈士纪念馆'
    },
    {
      key: 'chongqing_gov_bowuguan_147',
      name: '酉阳土家族苗族自治县酉州博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_38',
      name: '重庆“湖广填四川”移民博物馆（重庆湖广会馆）'
    },
    {
      key: 'chongqing_gov_bowuguan_27',
      name: '重庆三峡移民纪念馆'
    },
    {
      key: 'chongqing_gov_bowuguan_60',
      name: '重庆三耳火锅博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆两江新区青少年宫'
    },
    {
      key: '重庆本地宝',
      name: '重庆中国三峡博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_1',
      name: '重庆中国三峡博物馆(重庆博物馆)'
    },
    {
      key: '重庆本地宝',
      name: '重庆中央公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆九龙坡区青少年宫'
    },
    {
      key: 'chongqing_gov_bowuguan_12',
      name: '重庆体育博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_13',
      name: '重庆典籍博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_54',
      name: '重庆冯玉祥纪念馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆北碚区青少年宫'
    },
    {
      key: 'chongqing_gov_bowuguan_59',
      name: '重庆华岩佛教博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆南岸区青少年宫'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆南川区青少年宫'
    },
    {
      key: 'chongqing_gov_bowuguan_9',
      name: '重庆历史名人馆'
    },
    {
      key: 'chongqing_gov_bowuguan_95',
      name: '重庆友军辣椒博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_11',
      name: '重庆史迪威博物馆（史迪威研究中心）'
    },
    {
      key: 'chongqing_gov_bowuguan_16',
      name: '重庆嘉陵江索道博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆园博园'
    },
    {
      key: '重庆本地宝',
      name: '重庆国际马戏城'
    },
    {
      key: '重庆本地宝',
      name: '重庆图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大剧院'
    },
    {
      key: 'chongqing_gov_bowuguan_107',
      name: '重庆大圆祥博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆大渡口区青少年宫'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆大足区艺术中心'
    },
    {
      key: 'chongqing_gov_bowuguan_44',
      name: '重庆大轰炸遗址陈列馆'
    },
    {
      key: 'chongqing_gov_bowuguan_6',
      name: '重庆大韩民国临时政府旧址陈列馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆奥体中心'
    },
    {
      key: 'chongqing_gov_bowuguan_81',
      name: '重庆宝林博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆少年儿童图书馆'
    },
    {
      key: 'chongqing_gov_bowuguan_25',
      name: '重庆川剧博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆工业博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆巴南区青少年宫'
    },
    {
      key: 'chongqing_gov_bowuguan_80',
      name: '重庆巴渝民俗博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_40',
      name: '重庆巴渝民间中医药博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_32',
      name: '重庆市万州区三峡石博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_28',
      name: '重庆市万州区博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_3',
      name: '重庆市万州区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_2',
      name: '重庆市万州区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_30',
      name: '重庆市万州良公祠民俗博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_29',
      name: '重庆市万州革命烈士陵园管理中心'
    },
    {
      key: 'chongqing_gov_wenhuaguan_23',
      name: '重庆市万盛经开区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_152',
      name: '重庆市万盛经济技术开发区博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_21',
      name: '重庆市万盛经济技术开发区图书馆'
    },
    {
      key: 'chongqing_gov_bowuguan_67',
      name: '重庆市中医药博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_32',
      name: '重庆市丰都县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_31',
      name: '重庆市丰都县文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_62',
      name: '重庆市九龙坡区九龙沉香博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_64',
      name: '重庆市九龙坡区周君记火锅调料历史文化博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_10',
      name: '重庆市九龙坡区图书馆'
    },
    {
      key: 'chongqing_gov_bowuguan_63',
      name: '重庆市九龙坡区建川博物馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_8',
      name: '重庆市九龙坡区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_57',
      name: '重庆市九龙坡区重庆巴人博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_61',
      name: '重庆市九龙坡区黄桷坪钢琴博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_35',
      name: '重庆市云阳县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_34',
      name: '重庆市云阳县文化馆'
    },
    {
      key: 'chongqing_gov_tiyu_1',
      name: '重庆市体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_69',
      name: '重庆市北碚区博物馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_10',
      name: '重庆市北碚区文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_12',
      name: '重庆市北碚图书馆'
    },
    {
      key: 'chongqing_gov_tushuguan_11',
      name: '重庆市南岸区图书馆'
    },
    {
      key: 'chongqing_gov_bowuguan_68',
      name: '重庆市南岸区德庄火锅博物馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_9',
      name: '重庆市南岸区文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_18',
      name: '重庆市南川区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_21',
      name: '重庆市南川区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_102',
      name: '重庆市南川区蝶语昆虫博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_20',
      name: '重庆市双桥经开区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_13',
      name: '重庆市双桥经开区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_96',
      name: '重庆市合川区三江民俗博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_17',
      name: '重庆市合川区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_19',
      name: '重庆市合川区文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_33',
      name: '重庆市垫江县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_32',
      name: '重庆市垫江县文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_31',
      name: '重庆市城口县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_30',
      name: '重庆市城口县文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_47',
      name: '重庆市大渡口区博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_7',
      name: '重庆市大渡口区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_5',
      name: '重庆市大渡口区文化馆'
    },
    {
      key: 'chongqing_gov_tiyu_2',
      name: '重庆市大田湾体育场'
    },
    {
      key: 'chongqing_gov_tushuguan_19',
      name: '重庆市大足区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_12',
      name: '重庆市大足区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_106',
      name: '重庆市大足区红岩重型汽车博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_36',
      name: '重庆市奉节县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_35',
      name: '重庆市奉节县文化馆'
    },
    {
      key: 'chongqing_gov_tiyu_3',
      name: '重庆市奥林匹克体育中心体育场'
    },
    {
      key: 'chongqing_gov_tiyu_4',
      name: '重庆市奥林匹克体育中心游泳跳水馆'
    },
    {
      key: 'chongqing_gov_tushuguan_2',
      name: '重庆市少年儿童图书馆'
    },
    {
      key: 'chongqing_gov_tushuguan_37',
      name: '重庆市巫山县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_36',
      name: '重庆市巫山县文化馆'
    },
    {
      key: 'chongqing_gov_tiyu_73',
      name: '重庆市巫山县苟家体育场'
    },
    {
      key: 'chongqing_gov_tushuguan_38',
      name: '重庆市巫溪县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_37',
      name: '重庆市巫溪县文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_84',
      name: '重庆市巴南区博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_14',
      name: '重庆市巴南区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_15',
      name: '重庆市巴南区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_86',
      name: '重庆市巴南区江碧波艺术博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_41',
      name: '重庆市巴渝名匾文化艺术博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_30',
      name: '重庆市开州区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_27',
      name: '重庆市开州区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_119',
      name: '重庆市开州区雨青博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_118',
      name: '重庆市开州博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_42',
      name: '重庆市彭水苗族土家族自治县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_41',
      name: '重庆市彭水苗族土家族自治县文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_34',
      name: '重庆市忠县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_33',
      name: '重庆市忠县文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_120',
      name: '重庆市梁平区博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_28',
      name: '重庆市梁平区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_28',
      name: '重庆市梁平区文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_29',
      name: '重庆市武隆区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_29',
      name: '重庆市武隆区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_121',
      name: '重庆市武隆博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_33',
      name: '重庆市民族博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_23',
      name: '重庆市永川区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_20',
      name: '重庆市永川区文化艺术馆'
    },
    {
      key: 'chongqing_gov_bowuguan_100',
      name: '重庆市永川区蕴宝博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_99',
      name: '重庆市永川堃航博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_8',
      name: '重庆市江北区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_6',
      name: '重庆市江北区文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_16',
      name: '重庆市江津区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_18',
      name: '重庆市江津区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_91',
      name: '重庆市江津区陈独秀旧居陈列馆'
    },
    {
      key: 'chongqing_gov_tushuguan_9',
      name: '重庆市沙坪坝区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_7',
      name: '重庆市沙坪坝区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_51',
      name: '重庆市沙坪坝博物馆（重庆市沙坪坝区巴蜀古代建筑博物馆）'
    },
    {
      key: 'chongqing_gov_bowuguan_36',
      name: '重庆市涪陵区博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_5',
      name: '重庆市涪陵区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_3',
      name: '重庆市涪陵区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_37',
      name: '重庆市渝中区博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_42',
      name: '重庆市渝中区友好飞虎队博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_6',
      name: '重庆市渝中区图书馆'
    },
    {
      key: 'chongqing_gov_bowuguan_43',
      name: '重庆市渝中区巴渝民风博物馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_4',
      name: '重庆市渝中区文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_13',
      name: '重庆市渝北区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_14',
      name: '重庆市渝北区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_82',
      name: '重庆市渝北区渝都古典照相机缝纫机博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_24',
      name: '重庆市潼南区图书馆（新馆）'
    },
    {
      key: 'chongqing_gov_wenhuaguan_25',
      name: '重庆市潼南区文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_25',
      name: '重庆市璧山区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_22',
      name: '重庆市璧山区文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_39',
      name: '重庆市石柱土家族自治县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_38',
      name: '重庆市石柱土家族自治县文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_40',
      name: '重庆市秀山土家族苗族自治县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_39',
      name: '重庆市秀山土家族苗族自治县文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_22',
      name: '重庆市綦江区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_11',
      name: '重庆市綦江区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_104',
      name: '重庆市綦江区红军长征纪念馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_1',
      name: '重庆市群众艺术馆'
    },
    {
      key: 'chongqing_gov_bowuguan_115',
      name: '重庆市荣昌区万灵提琴博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_27',
      name: '重庆市荣昌区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_26',
      name: '重庆市荣昌区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_116',
      name: '重庆市荣昌陶窑口博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_21',
      name: '重庆市规划展览馆'
    },
    {
      key: 'chongqing_gov_tushuguan_41',
      name: '重庆市酉阳土家族苗族自治县图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_40',
      name: '重庆市酉阳土家族苗族自治县文化馆'
    },
    {
      key: 'chongqing_gov_tushuguan_26',
      name: '重庆市铜梁区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_24',
      name: '重庆市铜梁区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_110',
      name: '重庆市铜梁区邱少云烈士纪念馆'
    },
    {
      key: 'chongqing_gov_bowuguan_87',
      name: '重庆市长寿区博物馆'
    },
    {
      key: 'chongqing_gov_tushuguan_15',
      name: '重庆市长寿区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_17',
      name: '重庆市长寿区文化馆'
    },
    {
      key: 'chongqing_gov_bowuguan_88',
      name: '重庆市长寿区杨克明故居陈列馆'
    },
    {
      key: 'chongqing_gov_tushuguan_4',
      name: '重庆市黔江区图书馆'
    },
    {
      key: 'chongqing_gov_wenhuaguan_16',
      name: '重庆市黔江区民族文化艺术馆'
    },
    {
      key: 'chongqing_gov_bowuguan_19',
      name: '重庆师范大学博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆建川博物馆聚落'
    },
    {
      key: 'chongqing_gov_bowuguan_53',
      name: '重庆张治中纪念馆'
    },
    {
      key: 'chongqing_gov_bowuguan_83',
      name: '重庆御临旅游纪念品博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_10',
      name: '重庆抗战戏剧博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_55',
      name: '重庆抗战教育博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_65',
      name: '重庆抗战遗址博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_50',
      name: '重庆旁观者设计博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆欢乐海底世界'
    },
    {
      key: '重庆本地宝',
      name: '重庆欢乐谷'
    },
    {
      key: '重庆本地宝',
      name: '重庆欢乐谷玛雅海滩水公园'
    },
    {
      key: 'chongqing_gov_bowuguan_3',
      name: '重庆歌乐山革命纪念馆（重庆红岩革命历史博物馆）'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆武隆区青少年宫'
    },
    {
      key: '重庆本地宝',
      name: '重庆汉海海洋公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆江北区青少年宫'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆沙坪坝区青少年宫'
    },
    {
      key: 'chongqing_gov_bowuguan_56',
      name: '重庆沙坪坝地质博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区体育场'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝中区青少年宫'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区会展中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区体育馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区公园'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区创意园'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区剧院'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区动物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区图书馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区文化中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区文化馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区植物园'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区海洋馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区艺术中心'
    },
    {
      key: '重庆本地宝',
      name: '重庆渝北区青少年宫'
    },
    {
      key: '重庆本地宝',
      name: '重庆火锅博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_8',
      name: '重庆特园民主党派历史陈列馆（中国民主党派历史陈列馆）'
    },
    {
      key: 'chongqing_gov_bowuguan_24',
      name: '重庆电信博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_26',
      name: '重庆白鹤梁水下博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆科技馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆红岩革命历史博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆美术馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆自然博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_17',
      name: '重庆自然资源科普馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆融创乐园'
    },
    {
      key: '重庆本地宝',
      name: '重庆融创海世界'
    },
    {
      key: '重庆本地宝',
      name: '重庆融创雪世界'
    },
    {
      key: 'chongqing_gov_bowuguan_20',
      name: '重庆警察博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_52',
      name: '重庆郭沫若纪念馆'
    },
    {
      key: 'chongqing_gov_bowuguan_49',
      name: '重庆金融博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_45',
      name: '重庆金融历史博物馆'
    },
    {
      key: 'chongqing_gov_bowuguan_85',
      name: '重庆长江石文化艺术博物馆'
    },
    {
      key: '重庆本地宝',
      name: '重庆际华园'
    },
    {
      key: '重庆本地宝',
      name: '金佛山'
    },
    {
      key: 'chongqing_gov_bowuguan_94',
      name: '钓鱼城古战场遗址博物馆'
    },
    {
      key: '重庆本地宝',
      name: '铁山坪森林公园'
    },
    {
      key: 'chongqing_gov_tiyu_46',
      name: '铜梁区全民健身中心'
    },
    {
      key: 'chongqing_gov_bowuguan_108',
      name: '铜梁区博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_45',
      name: '铜梁区藕塘湾体育场'
    },
    {
      key: 'chongqing_gov_tiyu_47',
      name: '铜梁区金龙体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_109',
      name: '铜梁木匾博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_48',
      name: '铜梁龙体育场'
    },
    {
      key: 'chongqing_gov_tiyu_30',
      name: '长寿区体育中心体育馆'
    },
    {
      key: 'chongqing_gov_tiyu_31',
      name: '长寿区体育场'
    },
    {
      key: 'chongqing_gov_bowuguan_93',
      name: '陶行知先生纪念馆'
    },
    {
      key: 'chongqing_gov_bowuguan_105',
      name: '饶国梁纪念馆'
    },
    {
      key: '重庆本地宝',
      name: '鹅岭二厂'
    },
    {
      key: '重庆本地宝',
      name: '鹅岭公园'
    },
    {
      key: 'chongqing_gov_tiyu_28',
      name: '黔江区体育场'
    },
    {
      key: 'chongqing_gov_tiyu_29',
      name: '黔江区体育馆'
    },
    {
      key: 'chongqing_gov_bowuguan_35',
      name: '黔江区博物馆'
    },
    {
      key: 'chongqing_gov_tiyu_27',
      name: '黔江区游泳馆'
    }
  ],
  nanjing: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: '南京本地宝',
      name: '东庐山'
    },
    {
      key: 'nanjing_gov_zgdbtmyxcjng',
      name: '中共代表团梅园新村纪念馆'
    },
    {
      key: '南京本地宝',
      name: '中华门瓮城'
    },
    {
      key: '南京本地宝',
      name: '中山植物园'
    },
    {
      key: '南京本地宝',
      name: '中山陵'
    },
    {
      key: '南京本地宝',
      name: '五台山体育中心'
    },
    {
      key: '南京本地宝',
      name: '侵华日军南京大屠杀遇难同胞纪念馆'
    },
    {
      key: '南京本地宝',
      name: '傅家边'
    },
    {
      key: 'nanjing_gov_lhqtsg',
      name: '六合区图书馆'
    },
    {
      key: 'nanjing_gov_lhqdewhg',
      name: '六合区文化馆'
    },
    {
      key: 'nanjing_gov_lhqdetsg',
      name: '六合区第二图书馆'
    },
    {
      key: '南京本地宝',
      name: '六朝博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京中国科举博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京云锦博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京六合区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京六合区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京六合区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京六合区公园'
    },
    {
      key: '南京本地宝',
      name: '南京六合区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京六合区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京六合区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京六合区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京六合区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京六合区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京六合区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京六合区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京六合区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京六合区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京六合区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京六合区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京六合区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '南京博物院'
    },
    {
      key: '南京本地宝',
      name: '南京古生物博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京国防园'
    },
    {
      key: '南京本地宝',
      name: '南京图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京地质博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京城墙博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京奥林匹克体育中心'
    },
    {
      key: '南京本地宝',
      name: '南京市博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京市少年儿童图书馆'
    },
    {
      key: 'nanjing_gov_njswhg',
      name: '南京市文化馆'
    },
    {
      key: 'nanjing_gov_njmsbwg',
      name: '南京市民俗博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京平山森林公园'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区公园'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京建邺区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区公园'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京栖霞区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '南京欢乐谷'
    },
    {
      key: 'nanjing_gov_njjbtsg',
      name: '南京江北图书馆（新馆）'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区公园'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京江宁区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区公园'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京浦口区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '南京海底世界'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区公园'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京溧水区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区公园'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京玄武区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '南京直立人化石遗址博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区公园'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京秦淮区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '南京绿博园'
    },
    {
      key: '南京本地宝',
      name: '南京金箔艺术馆'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区公园'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京雨花台区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区公园'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京高淳区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区会展中心'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区体育场'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区体育馆'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区公园'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区创意园'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区剧院'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区动物园'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区博物馆'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区图书馆'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区文化中心'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区文化馆'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区植物园'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区海洋馆'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区科技馆'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区美术馆'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区艺术中心'
    },
    {
      key: '南京本地宝',
      name: '南京鼓楼区青少年宫'
    },
    {
      key: '南京本地宝',
      name: '周园'
    },
    {
      key: '南京本地宝',
      name: '固城湖'
    },
    {
      key: 'nanjing_gov_cqbwg',
      name: '城墙博物馆'
    },
    {
      key: '南京本地宝',
      name: '大报恩寺遗址公园'
    },
    {
      key: '南京本地宝',
      name: '大金山国防园'
    },
    {
      key: '南京本地宝',
      name: '天生桥'
    },
    {
      key: 'nanjing_gov_njstptglsbwg',
      name: '太平天国历史博物馆'
    },
    {
      key: '南京本地宝',
      name: '夫子庙秦淮风光带'
    },
    {
      key: 'nanjing_gov_jqtsg',
      name: '建邺区图书馆'
    },
    {
      key: 'nanjing_gov_jqwhg',
      name: '建邺区文化馆'
    },
    {
      key: '南京本地宝',
      name: '弘阳欢乐世界'
    },
    {
      key: '南京本地宝',
      name: '总统府'
    },
    {
      key: '南京本地宝',
      name: '无想山'
    },
    {
      key: '南京本地宝',
      name: '明孝陵'
    },
    {
      key: 'nanjing_gov_qxqtsg',
      name: '栖霞区图书馆'
    },
    {
      key: 'nanjing_gov_qxqwhg',
      name: '栖霞区文化馆'
    },
    {
      key: '南京本地宝',
      name: '栖霞山风景区'
    },
    {
      key: '南京本地宝',
      name: '桂子山石柱林'
    },
    {
      key: '南京本地宝',
      name: '桠溪国际慢城'
    },
    {
      key: '南京本地宝',
      name: '梅园新村纪念馆'
    },
    {
      key: 'nanjing_gov_jbxqwhg',
      name: '江北新区文化馆'
    },
    {
      key: 'nanjing_gov_jnqtsg',
      name: '江宁区图书馆'
    },
    {
      key: 'nanjing_gov_jnqwhg',
      name: '江宁区文化馆'
    },
    {
      key: '南京本地宝',
      name: '江宁织造博物馆'
    },
    {
      key: '南京本地宝',
      name: '江苏省科学技术馆'
    },
    {
      key: 'nanjing_gov_jssmsg',
      name: '江苏省美术馆'
    },
    {
      key: '南京本地宝',
      name: '汤山古猿人洞'
    },
    {
      key: '南京本地宝',
      name: '汤山温泉旅游度假区'
    },
    {
      key: 'nanjing_gov_pkqtsg',
      name: '浦口区图书馆'
    },
    {
      key: 'nanjing_gov_pkqwhg',
      name: '浦口区文化馆'
    },
    {
      key: '南京本地宝',
      name: '渡江胜利纪念馆'
    },
    {
      key: '南京本地宝',
      name: '游子山'
    },
    {
      key: 'nanjing_gov_lsqsnettsg',
      name: '溧水区儿童图书馆'
    },
    {
      key: 'nanjing_gov_sqtsg',
      name: '溧水区图书馆'
    },
    {
      key: 'nanjing_gov_sqwhg',
      name: '溧水区文化馆'
    },
    {
      key: '南京本地宝',
      name: '牛首山文化旅游区'
    },
    {
      key: 'nanjing_gov_xwqsnettsg',
      name: '玄武区少年儿童图书馆'
    },
    {
      key: 'nanjing_gov_xwqwhg',
      name: '玄武区文化馆'
    },
    {
      key: '南京本地宝',
      name: '玄武湖公园'
    },
    {
      key: '南京本地宝',
      name: '玛雅海滩水公园'
    },
    {
      key: '南京本地宝',
      name: '珍珠泉风景区'
    },
    {
      key: 'nanjing_gov_bjhwhzx',
      name: '百家湖文化中心'
    },
    {
      key: '南京本地宝',
      name: '瞻园'
    },
    {
      key: 'nanjing_gov_qhqtsg',
      name: '秦淮区图书馆'
    },
    {
      key: 'nanjing_gov_qhqwhg',
      name: '秦淮区文化馆'
    },
    {
      key: '南京本地宝',
      name: '秦淮非遗馆'
    },
    {
      key: '南京本地宝',
      name: '红山森林动物园'
    },
    {
      key: '南京本地宝',
      name: '美龄宫'
    },
    {
      key: '南京本地宝',
      name: '老山国家森林公园'
    },
    {
      key: '南京本地宝',
      name: '老门东'
    },
    {
      key: '南京本地宝',
      name: '莫愁湖公园'
    },
    {
      key: '南京本地宝',
      name: '金牛湖'
    },
    {
      key: '南京本地宝',
      name: '金陵图书馆'
    },
    {
      key: 'nanjing_gov_jlmsg',
      name: '金陵美术馆'
    },
    {
      key: '南京本地宝',
      name: '银杏湖乐园'
    },
    {
      key: '南京本地宝',
      name: '阅江楼'
    },
    {
      key: '南京本地宝',
      name: '阳山碑材'
    },
    {
      key: 'nanjing_gov_yhtqtsg',
      name: '雨花台区图书馆'
    },
    {
      key: 'nanjing_gov_yhtqwhg',
      name: '雨花台区文化馆'
    },
    {
      key: '南京本地宝',
      name: '雨花台烈士陵园'
    },
    {
      key: '南京本地宝',
      name: '青奥公园'
    },
    {
      key: '南京本地宝',
      name: '颐和路'
    },
    {
      key: 'nanjing_gov_gcqtsg',
      name: '高淳区图书馆'
    },
    {
      key: 'nanjing_gov_gcqwhg',
      name: '高淳区文化馆'
    },
    {
      key: '南京本地宝',
      name: '高淳老街'
    },
    {
      key: '南京本地宝',
      name: '高淳陶瓷小镇'
    },
    {
      key: '南京本地宝',
      name: '鸡鸣寺'
    },
    {
      key: 'nanjing_gov_glqtsg',
      name: '鼓楼区图书馆'
    },
    {
      key: 'nanjing_gov_glqwhg',
      name: '鼓楼区文化馆'
    }
  ],
  wuhan: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: '武汉本地宝',
      name: '万松园'
    },
    {
      key: '武汉本地宝',
      name: '东湖风景区'
    },
    {
      key: '武汉本地宝',
      name: '中山舰博物馆'
    },
    {
      key: '武汉本地宝',
      name: '中科院武汉植物园'
    },
    {
      key: 'wuhan_gov_1437249',
      name: '八七会议会址纪念馆'
    },
    {
      key: 'wuhan_gov_1437250',
      name: '八路军武汉办事处旧址纪念馆（汉口新四军军部旧址纪念馆）'
    },
    {
      key: '武汉本地宝',
      name: '后官湖湿地公园'
    },
    {
      key: '武汉本地宝',
      name: '户部巷'
    },
    {
      key: '武汉本地宝',
      name: '木兰天池'
    },
    {
      key: '武汉本地宝',
      name: '木兰山'
    },
    {
      key: '武汉本地宝',
      name: '木兰清凉寨'
    },
    {
      key: '武汉本地宝',
      name: '木兰草原'
    },
    {
      key: '武汉本地宝',
      name: '楚河汉街'
    },
    {
      key: '武汉本地宝',
      name: '武昌江滩公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉东湖海洋世界'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉东西湖区青少年宫'
    },
    {
      key: 'wuhan_gov_1437239',
      name: '武汉中共中央机关旧址纪念馆'
    },
    {
      key: 'wuhan_gov_1437254',
      name: '武汉京剧院有限责任公司(武汉京剧院)'
    },
    {
      key: '武汉本地宝',
      name: '武汉体育中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉全民健身中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉博物馆'
    },
    {
      key: 'wuhan_gov_1437246',
      name: '武汉博物馆（武汉市文物交流中心）'
    },
    {
      key: '武汉本地宝',
      name: '武汉图书馆'
    },
    {
      key: 'wuhan_gov_1437237',
      name: '武汉市中山舰博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉市少年儿童图书馆'
    },
    {
      key: 'wuhan_gov_1437251',
      name: '武汉市晴川阁管理处（武汉大禹文化博物馆）'
    },
    {
      key: 'wuhan_gov_1437233',
      name: '武汉市群众艺术馆（武汉市非物质文化遗产保护中心）'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉新洲区青少年宫'
    },
    {
      key: '武汉本地宝',
      name: '武汉杂技厅'
    },
    {
      key: 'wuhan_gov_1437253',
      name: '武汉楚剧院有限责任公司(武汉楚剧院)'
    },
    {
      key: '武汉本地宝',
      name: '武汉欢乐谷'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉武昌区青少年宫'
    },
    {
      key: 'wuhan_gov_1437243',
      name: '武汉汉剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉汉阳区青少年宫'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江夏区青少年宫'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉江岸区青少年宫'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉江汉区青少年宫'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉洪山区青少年宫'
    },
    {
      key: '武汉本地宝',
      name: '武汉海昌极地海洋公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉港码头'
    },
    {
      key: '武汉本地宝',
      name: '武汉玛雅海滩水公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉硚口区青少年宫'
    },
    {
      key: '武汉本地宝',
      name: '武汉科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉自然博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉蔡甸区青少年宫'
    },
    {
      key: '武汉本地宝',
      name: '武汉长江大桥'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉青山区青少年宫'
    },
    {
      key: 'wuhan_gov_1437235',
      name: '武汉革命博物馆（武昌农民运动讲习所旧址纪念馆，中共五大会址纪念馆）'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区会展中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区体育场'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区体育馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区公园'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区创意园'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区剧院'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区动物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区博物馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区图书馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区文化中心'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区文化馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区植物园'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区海洋馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区科技馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区美术馆'
    },
    {
      key: '武汉本地宝',
      name: '武汉黄陂区艺术中心'
    },
    {
      key: '武汉本地宝',
      name: '汉口江滩公园'
    },
    {
      key: '武汉本地宝',
      name: '汉秀剧场'
    },
    {
      key: '武汉本地宝',
      name: '汉阳江滩公园'
    },
    {
      key: '武汉本地宝',
      name: '江汉关博物馆'
    },
    {
      key: 'wuhan_gov_1437247',
      name: '江汉关博物馆（武汉国民政府旧址纪念馆、詹天佑故居博物馆）'
    },
    {
      key: '武汉本地宝',
      name: '江汉路步行街'
    },
    {
      key: '武汉本地宝',
      name: '湖北省博物馆'
    },
    {
      key: '武汉本地宝',
      name: '湖北省图书馆'
    },
    {
      key: '武汉本地宝',
      name: '湖北省科学技术馆'
    },
    {
      key: '武汉本地宝',
      name: '湖北美术馆'
    },
    {
      key: '武汉本地宝',
      name: '盘龙城遗址博物院'
    },
    {
      key: '武汉本地宝',
      name: '硚口江滩公园'
    },
    {
      key: '武汉本地宝',
      name: '粮道街'
    },
    {
      key: '武汉本地宝',
      name: '解放公园'
    },
    {
      key: '武汉本地宝',
      name: '辛亥革命博物馆'
    },
    {
      key: '武汉本地宝',
      name: '辛亥革命武昌起义纪念馆'
    },
    {
      key: '武汉本地宝',
      name: '锦里沟'
    },
    {
      key: '武汉本地宝',
      name: '鹦鹉洲长江大桥'
    },
    {
      key: '武汉本地宝',
      name: '黄鹤楼公园'
    },
    {
      key: '武汉本地宝',
      name: '黎黄陂路'
    }
  ],
  xian: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: 'xian_gov_4',
      name: '4、国家规定的其他免费服务项目'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '东岳庙'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '东渭桥遗址'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '东马坊遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '中山图书馆旧址'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '中渭桥遗址'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '丰镐遗址'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '丰镐遗址车马坑陈列馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '临潼区博物馆'
    },
    {
      key: 'xian_gov_1716743219733606401',
      name: '临潼区图书馆秦陵社区分馆'
    },
    {
      key: 'xian_gov_1716743219733606401',
      name: '临潼区图书馆骊阅分馆'
    },
    {
      key: 'xian_gov_1716743219733606401',
      name: '临潼区文化馆'
    },
    {
      key: 'xian_gov_1716741181564076033',
      name: '临潼区文物管理委员会办公室（区文物稽查队）'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '临潼区鸿门宴博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '义和遗址'
    },
    {
      key: '西安本地宝',
      name: '乐华城'
    },
    {
      key: '西安本地宝',
      name: '书院门'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '二圣宫'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '二龙塔'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '五凤遗址'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '五星街天主教堂'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '井勿幕墓'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '交大西迁博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '人民剧院'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '仙游寺'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '仙游寺博物馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '仙游寺法王塔'
    },
    {
      key: 'xian_gov_618490b1f8fd1c0bdc62ed8e',
      name: '代知识分子奋勇前进的磅礴伟力'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '任家庄门楼'
    },
    {
      key: 'xian_gov_09',
      name: '传统医药（09）'
    },
    {
      key: 'xian_gov_08',
      name: '传统技艺 （08）'
    },
    {
      key: 'xian_gov_08',
      name: '传统技艺（08）'
    },
    {
      key: 'xian_gov_07',
      name: '传统美术（07）'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '佛坪厅故城'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '傥骆道遗址周至段'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '八云塔'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '八仙庵'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '八路军西安办事处旧址'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '八路军西安办事处纪念馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '公输堂'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '关中书院'
    },
    {
      key: '西安本地宝',
      name: '兴庆宫公园'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '兴庆宫遗址'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '兴教寺塔（包括兴教寺其他建筑物）'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '军用航空科技博物馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '凤栖原西汉家族墓地'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '刘进夫妇墓'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '化羊庙'
    },
    {
      key: 'xian_gov_232',
      name: '化觉巷232号'
    },
    {
      key: 'xian_gov_232',
      name: '化觉巷232号民居'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '北丈八寺村遗址'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '北广济街清真寺'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '北广济街清真寺邦克楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '北庞天佛寺（天王庙）'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '北留遗址'
    },
    {
      key: 'xian_gov_144',
      name: '北院门144号民居'
    },
    {
      key: 'xian_gov_1716741181564076033',
      name: '区博物馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '半坡遗址'
    },
    {
      key: '西安本地宝',
      name: '半坡遗址博物馆'
    },
    {
      key: '西安本地宝',
      name: '华夏文旅海洋公园'
    },
    {
      key: '西安本地宝',
      name: '华清宫'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '华清宫遗址'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '华清宫遗址（部分）'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '华清池五间厅）'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '华清池唐华清宫御汤遗址博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '华胥陵'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '南城清真寺'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '南淇水药王楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '南豆角村南、北门楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '卧龙寺石刻造像和铁钟'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '原市委礼堂'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '原市政府市长楼'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '原市政府礼堂'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '原市长楼'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '古遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '吕家堡吕氏宗祠'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '吕柟墓'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '周穆王陵'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '周至博物馆'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '周至县中国道文化展示区（楼观台正对面）'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '周至县泓菏温泉游泳馆'
    },
    {
      key: 'xian_gov_10113',
      name: '周至县燕云府邸商铺一楼10113室'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '周至王氏宗祠'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '唐华清宫梨园遗址博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '唐旗寨八仙庙'
    },
    {
      key: '西安本地宝',
      name: '回民街'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '圜丘遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '城关遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '大仁遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '大兴善寺'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '大华纱厂旧址'
    },
    {
      key: '西安本地宝',
      name: '大唐不夜城'
    },
    {
      key: '西安本地宝',
      name: '大唐芙蓉园'
    },
    {
      key: '西安本地宝',
      name: '大唐西市博物馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '大学习巷清真寺'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '大明宫国家遗址公园丹凤门遗址博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '大明宫国家遗址公园考古探索中心'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '大明宫遗址'
    },
    {
      key: '西安本地宝',
      name: '大明宫遗址博物馆'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '大皮院清真寺'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '大秦寺塔'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '大雁塔'
    },
    {
      key: '西安本地宝',
      name: '大雁塔景区'
    },
    {
      key: 'xian_gov_38',
      name: '大麦市街38号民居'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '天池寺塔'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '太史桥'
    },
    {
      key: '西安本地宝',
      name: '太平国家森林公园'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '太液池遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '奎星阁'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '姜寨遗址'
    },
    {
      key: 'xian_gov_1716741181564076033',
      name: '姜寨遗址文物管理所'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '孙蔚如旧居'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '宋村遗址'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '宗圣宫遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '定六村无量庙'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '宝庆寺塔'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '小学习巷营里寺'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '小寨汉墓'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '小皮院清真寺'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '小雁塔'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '崔家堡遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '广仁寺古建筑群'
    },
    {
      key: 'xian_gov_1716741181564076033',
      name: '康家白家遗址文物管理所'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '康家遗址'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '建章宫遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '张云山墓'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '怀珍坊遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '感业寺遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '成道宫村成道宫'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '户县化羊庙'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '户县化羊庙东岳献殿'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '户县文庙'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '户县王氏宗祠'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '户县钟楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '扁鹊墓'
    },
    {
      key: 'xian_gov_1716741181564076033',
      name: '扁鹊纪念馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '敬德塔'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '斡尔垛遗址'
    },
    {
      key: 'xian_gov_10',
      name: '新城区东站路10号新兴骏景园二期东门'
    },
    {
      key: 'xian_gov_8',
      name: '新城区幸福北路8号'
    },
    {
      key: 'xian_gov_61',
      name: '新城区新科路61号'
    },
    {
      key: 'xian_gov_26',
      name: '新城区西五路26号'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '新城黄楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '新寺遗址'
    },
    {
      key: '西安本地宝',
      name: '昆明池七夕公园'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '明秦王墓'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '明秦王府城墙遗址'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '易俗社剧场'
    },
    {
      key: '西安本地宝',
      name: '易俗社文化街区'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '昭慧塔（高陵塔）'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '晏平寨晏氏祠堂'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '景联关帝庙'
    },
    {
      key: '西安本地宝',
      name: '曲江书城'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '曲江新区鸿基紫韵会所负一层'
    },
    {
      key: '西安本地宝',
      name: '曲江池遗址公园'
    },
    {
      key: '西安本地宝',
      name: '曲江海洋极地公园'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '未央区北二环君临大酒店五路'
    },
    {
      key: 'xian_gov_158',
      name: '未央区渭滨路158号谭家街办文化站隔壁'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '朱子桥墓'
    },
    {
      key: '西安本地宝',
      name: '朱雀国家森林公园'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '李华太平寺'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '李晟碑'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '李颙墓'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '杜公祠'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '杜陵'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '杨官寨遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '杨家堡城隍庙'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '杨武庄公墓及祠'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '杨砺墓'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '杨虎城将军纪念馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '杨虎城陵园'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '柳青墓'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '栎阳城遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '栎阳桥'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '楼增良红木雕刻艺术博物馆'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '楼观台'
    },
    {
      key: '西安本地宝',
      name: '楼观台森林公园'
    },
    {
      key: 'xian_gov_11',
      name: '民俗（11）'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '民盟省委会工作站办公楼'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '水陆庵'
    },
    {
      key: '西安本地宝',
      name: '永兴坊'
    },
    {
      key: '西安本地宝',
      name: '汉城湖公园'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '汉长安城遗址'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '汉长安城遗址长乐宫四、五号遗址陈列馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '汉长安城遗址陈列馆'
    },
    {
      key: '西安本地宝',
      name: '汉阳陵博物院'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '汉阳陵博物馆'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '汤峪栈道遗址'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '汪锋故居及墓园'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '汪锋故居纪念馆'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '泥峪石门遗址'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '泳往直前游泳馆'
    },
    {
      key: 'xian_gov_1901554530815434753',
      name: '泾渭国际中心城市书屋'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '洩湖遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '洪庆古墓'
    },
    {
      key: '西安本地宝',
      name: '浐灞国家湿地公园'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '清华山石窟'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '滹沱村遗址'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '灞桥遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '灞源革命纪念馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '灰堆坡遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '燉煌寺塔'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '牛郎织女石刻'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '玄帝祠玉皇楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '王九思墓'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '王季陵'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '王曲张学良故居'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '王氏宗祠'
    },
    {
      key: '西安本地宝',
      name: '王顺山国家森林公园'
    },
    {
      key: '西安本地宝',
      name: '玛雅海滩水公园'
    },
    {
      key: '西安本地宝',
      name: '环城公园'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '白家遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '白马寺滩聚落遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '真守村遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '祖庵城隍庙'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '秦一秦镇南城门楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '秦三极乐寺大殿'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '秦东陵'
    },
    {
      key: 'xian_gov_1716741181564076033',
      name: '秦东陵文物管理所'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '秦东陵（部分）'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '秦二世胡亥墓'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '秦二世陵遗址博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '秦咸阳宫遗址博物馆'
    },
    {
      key: '西安本地宝',
      name: '秦始皇帝陵博物院'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '秦始皇陵'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '秦始皇陵（部分）'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '秦庄襄王墓'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '秦都区沙河古桥遗址博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '秦镇商铺群'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '穆家堰戏楼'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '空军军医大学口腔医学博物馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '窦皇后陵'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '立园村城门楼'
    },
    {
      key: 'xian_gov_25',
      name: '红25军军部旧址'
    },
    {
      key: 'xian_gov_1901554530815434753',
      name: '经开区文化艺术中心'
    },
    {
      key: 'xian_gov_1901554530815434753',
      name: '经开区草滩金牛城市书房'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '罔极寺'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '罗军武民居'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '罗汉寺'
    },
    {
      key: '西安本地宝',
      name: '翠华山国家地质公园'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '老凹庄关帝庙'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '老子墓'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '老牛坡遗址'
    },
    {
      key: 'xian_gov_4039',
      name: '芦苇荡40号、39号姚家民居'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '英里遗址'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '草堂寺'
    },
    {
      key: 'xian_gov_41',
      name: '莲湖区丰禾路41号'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '莲湖区劳动南路中段'
    },
    {
      key: 'xian_gov_6',
      name: '莲湖区群贤路6号（唐延路北段锦都小区内）'
    },
    {
      key: 'xian_gov_1351001',
      name: '莲湖区西大街135号西京饭店1001号'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '葛牌镇区苏维埃政府纪念馆'
    },
    {
      key: 'xian_gov_25',
      name: '葛牌镇红25军军部旧址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '葛牌镇革命旧址（中共鄂豫陕省委扩大会议旧址、葛牌镇区苏维埃政府旧址）'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '葛牌革命旧址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '董仲舒墓'
    },
    {
      key: 'xian_gov_1763123354408628225',
      name: '蓝田县体育中心'
    },
    {
      key: 'xian_gov_1763123354408628225',
      name: '蓝田县图书馆'
    },
    {
      key: 'xian_gov_1763123354408628225',
      name: '蓝田县文化馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '蓝田县蔡文姬纪念馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '蓝田吕氏家族墓地'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '蓝田水陆庵壁塑博物馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '蓝田猿人遗址'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '蓝田猿人遗址博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '蔡文姬墓'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '薄太后陵'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '薛家寨汉墓群'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '袁氏家族墓地'
    },
    {
      key: 'xian_gov_85',
      name: '西七路85号民居'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '西五台'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '西京招待所'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西北一印旧址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西北人民革命大学旧址'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西北大学博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西北大学礼堂'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西北饭店有限责任公司'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安万寿寺塔'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安三鑫实业有限公司三鑫大酒店'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安东新巷礼拜堂'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安中国书法艺术博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区公园'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区文化馆'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安临潼区青少年宫'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '西安事变指挥部'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '西安事变旧址'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '西安事变旧址-华清池五间厅'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安事变纪念馆'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '西安于右任书法 艺术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安于右任书法艺术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安于右任故居纪念馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安交大汉壁画墓'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安交通大学主楼群'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安交通大学博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安交通大学附属中学博物馆'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '西安人民剧院'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安人民大厦'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安健康博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安关中民俗艺术博物院'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安半坡博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安博物院'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '西安和平电影院'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安唐皇城墙含光门遗址博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安唐都新碑林艺术博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安城墙'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '西安城隍庙'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安大华博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安大唐西市博物馆'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安大唐西市酒店'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安大明宫陶瓷艺术博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安奥体中心'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安工程大学纺织服装博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市中国古琴博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市临潼区扁鹊纪念馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市云之翼航空博物馆'
    },
    {
      key: 'xian_gov_1998584920184258561',
      name: '西安市华夏匾额博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市古陶瓷博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市吉兆春皮肤医药博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市和璞玉文化博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市团结民俗博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市圣普美术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市城市影像博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市城市记忆博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安市基督教南新街礼拜堂'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市大唐青铜镜博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市太乙面食文化博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市太和医室博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安市实验小学办公楼'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '西安市广仁寺'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市德江陶瓷模范标本博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市惟德玉文化博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市新梦想影业博物馆'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安市新概念运动康体有限公司'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市新源民俗艺术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市新美域和镜博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市明清皮影艺术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市曲江丝路遗珍博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市曲江第二小学儿童博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市曲江红色记忆博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市民俗博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市水墨长安艺术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市沣峪口老油坊博物馆'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安市游泳中心（室内池）'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安市灞桥区灞瑞一路高科绿水东城二期售楼部'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安市灞桥区鸿铭世纪游泳健身俱乐部'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市瑛煌关中婚俗文化博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市石仟佛造像艺术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市秦阿房宫遗址博物馆'
    },
    {
      key: 'xian_gov_13613110401',
      name: '西安市经开区未央路136-1号中讯大厦3幢1单元10401室'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市羊文化博物馆'
    },
    {
      key: 'xian_gov_wlj',
      name: '西安市群众艺术馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市荞麦园美术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市蓝田玉文化博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市贾平凹文学艺术博物馆'
    },
    {
      key: 'xian_gov_1998584920184258561',
      name: '西安市鄠邑区公输堂小木作艺术博物馆'
    },
    {
      key: 'xian_gov_1998569549761884162',
      name: '西安市鄠邑区农民画展览馆'
    },
    {
      key: 'xian_gov_1998569549761884162',
      name: '西安市鄠邑区图书馆'
    },
    {
      key: 'xian_gov_1998584920184258561',
      name: '西安市鄠邑区文物管理所 （西安市鄠邑区钟楼博物馆）'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市鄠邑区非物质文化遗产博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安市钟鼓楼博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市长安区杜甫纪念馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市长安博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市长安民居博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市雅观陶瓷艺术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市青龙寺遗址博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市非物质文化遗产博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市高家大院古典服饰博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市高陵区西北人民革命大学旧址博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安市黄土画派博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安建筑科技大学中国音乐史博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安建筑科技大学校史馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安建筑科技大学贾平凹文学艺术馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安户邑民间艺术博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安报话大楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安新华书店钟楼店旧址'
    },
    {
      key: '西安本地宝',
      name: '西安新城区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安新城区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安新城区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安新城区公园'
    },
    {
      key: '西安本地宝',
      name: '西安新城区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安新城区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安新城区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安新城区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安新城区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安新城区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安新城区文化馆'
    },
    {
      key: '西安本地宝',
      name: '西安新城区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安新城区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安新城区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安新城区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安新城区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安新城区青少年宫'
    },
    {
      key: 'xian_gov_1818857916155949058',
      name: '西安新梦想影业博物馆'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安明泰祥瑞体育有限公司'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安曲江大玉坊博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安曲江富陶国际陶艺博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安曲江艺术博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安未央区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安未央区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安未央区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安未央区公园'
    },
    {
      key: '西安本地宝',
      name: '西安未央区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安未央区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安未央区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安未央区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安未央区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安未央区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安未央区文化馆'
    },
    {
      key: '西安本地宝',
      name: '西安未央区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安未央区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安未央区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安未央区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安未央区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安未央区青少年宫'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安柴窑文化博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安植物园'
    },
    {
      key: '西安本地宝',
      name: '西安欢乐谷'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安毛泽东敬览馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安汉风水务博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安浐灞生态区城建博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安海棠职业学院中医美容博物馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '西安清真寺'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安源浩华藏博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区公园'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区文化馆'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安灞桥区青少年宫'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安理工大学西汉壁画墓'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安皇家艺术博物馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '西安碑林'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区公园'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区文化馆'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安碑林区青少年宫'
    },
    {
      key: '西安本地宝',
      name: '西安碑林博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安秦砖汉瓦博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安红色体育博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安经文牛文化陶瓷博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安美术学院美术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安美都博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区公园'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区文化馆'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安莲湖区青少年宫'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西安邮政局大楼'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区公园'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区文化馆'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安鄠邑区青少年宫'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '西安钟楼、鼓楼'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安锦业美术博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安长安区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安长安区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安长安区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安长安区公园'
    },
    {
      key: '西安本地宝',
      name: '西安长安区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安长安区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安长安区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安长安区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安长安区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安长安区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安长安区文化馆'
    },
    {
      key: '西安本地宝',
      name: '西安长安区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安长安区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安长安区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安长安区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安长安区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安长安区青少年宫'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区公园'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区文化馆'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安阎良区栎阳湖农业示范园有限责任公司（阎良区栎阳湖农业示范园游泳池）'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安阎良区青少年宫'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区公园'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区文化馆'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安雁塔区青少年宫'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安雅致东方酒店游泳池'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安雪花啤酒博物馆'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安零距离健身有限公司万年路分公司'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安音乐学院艺术博物馆'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '西安高家大院古典 服饰博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区会展中心'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区体育场'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区体育馆'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区公园'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区创意园'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区剧院'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区动物园'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区博物馆'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区图书馆'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区文化中心'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区文化馆'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区植物园'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区海洋馆'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区科技馆'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区美术馆'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区艺术中心'
    },
    {
      key: '西安本地宝',
      name: '西安高陵区青少年宫'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安高陵奇石博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西安高陵钱币博物馆'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安麟凤休闲娱乐有限公司'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '西安龙腾体育文化传播有限公司（白鹿溪谷游泳馆）'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '西峪遗址'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '西影电影博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '西段遗址'
    },
    {
      key: 'xian_gov_1716741181564076033',
      name: '西段遗址文物管理所'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '西汉帝陵（霸陵）'
    },
    {
      key: 'xian_gov_608a5b0df8fd1c20730c5c09',
      name: '读等服务'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '赵公明庙'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '赵瞻墓'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '赵西城隍庙'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '起良蔡侯纸博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '路翰林故居'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '通远坊天主教堂'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '遇仙桥及石造像'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '郭北遗址'
    },
    {
      key: 'xian_gov_1998569549761884162',
      name: '鄠邑区文化馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '重阳宫祖庵碑林'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '锡水洞遗址'
    },
    {
      key: 'xian_gov_6f',
      name: '长安北路草场坡荣城小区商铺6F'
    },
    {
      key: 'xian_gov_1712397055545675777',
      name: '长安区文化馆'
    },
    {
      key: 'xian_gov_1',
      name: '长安区王曲街道鱼鲍头村甲子1号'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '长安区韦曲街办何家营新村神禾二路东口'
    },
    {
      key: '西安本地宝',
      name: '长安十二时辰主题街区'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '长安华严寺塔'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '长安圣寿寺塔'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '长安大学公路交通博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '长安大学地质博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '长安郭氏民宅'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '阿房宫遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '陈富新民居'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '陈平墓'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '陕建集团办公楼'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '陕建集团总公司 办公楼'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西万达博物院'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西亮宝楼艺术博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西体育博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西元阳文化博物馆'
    },
    {
      key: '西安本地宝',
      name: '陕西历史博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西唐三彩艺术博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '陕西宾馆别墅群'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西师范大学博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '陕西师范大学图书馆'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '陕西德奥文化体育运动有限公司'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西明善博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西汉唐石刻博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '陕西省供销总社办公楼'
    },
    {
      key: '西安本地宝',
      name: '陕西省图书馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '陕西省检察院办公楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '陕西省民政厅办公楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '陕西省纺织供销公司办公楼'
    },
    {
      key: 'xian_gov_5da6c0c865cbd86d495781e8',
      name: '陕西省西安市国家航空高技术产业基地航空二路华宇理想国接待中心'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西科学技术馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西科技大学中国轻工业博物馆'
    },
    {
      key: '西安本地宝',
      name: '陕西科技馆'
    },
    {
      key: '西安本地宝',
      name: '陕西自然博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '陕西钱币博物馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '隋大兴、唐长安城遗址（包括青龙寺遗址）'
    },
    {
      key: 'xian_gov_3',
      name: '雁塔区长安南路华城泊郡3号楼'
    },
    {
      key: 'xian_gov_3916',
      name: '雁塔区长安西路39号铭城16号一层商铺'
    },
    {
      key: '西安本地宝',
      name: '雁鸣湖'
    },
    {
      key: 'xian_gov_1767090210230796290',
      name: '雷神庙·万阁楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '雷神庙万阁楼'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '革命公园'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '香积寺'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '香积寺善导塔'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '马王村城楼'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '马营遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '高培支旧居'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '高桂滋公馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '高铁寨汉墓'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '高陵区博物馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '高陵区防震减灾科普馆'
    },
    {
      key: 'xian_gov_62d8ba0ef8fd1c4c210ae016',
      name: '高陵祥顺博物馆'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '鱼化寨遗址'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '鸠摩罗什舍利塔'
    },
    {
      key: 'xian_gov_1716741181564076033',
      name: '鸿门宴博物馆'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '黄堆村遗址'
    },
    {
      key: '西安本地宝',
      name: '黑河国家森林公园'
    },
    {
      key: 'xian_gov_61a43e9bf8fd1c0bdc700bfa',
      name: '鼎湖延寿宫遗址'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '齐王庙'
    },
    {
      key: 'xian_gov_60b5fe19f8fd1c0bdc2dead1',
      name: '龙窝酒作坊'
    },
    {
      key: 'xian_gov_5fbb551ff8fd1c59664b3711',
      name: '（张学良将军公馆'
    }
  ],
  zhuhai: [
    {
      key: 'all',
      name: '全部地点'
    },
    {
      key: 'zhuhai_gov_tycg_wanshan_dongao',
      name: '万山镇全民健身广场（东澳岛）'
    },
    {
      key: 'zhuhai_gov_tycg_wanshan_dawan',
      name: '万山镇全民健身广场（大万山岛）'
    },
    {
      key: 'szwhzx',
      name: '三灶镇文化中心'
    },
    {
      key: 'jawhzx',
      name: '井岸镇文化中心'
    },
    {
      key: 'hfsd',
      name: '华发商都'
    },
    {
      key: 'zhuhai_gov_tycg_nanshui_square',
      name: '南水镇全民健身广场'
    },
    {
      key: 'gymuseum',
      name: '古元美术馆'
    },
    {
      key: 'zhuhai_gov_tycg_tangjiawan_square',
      name: '唐家湾镇全民健身广场'
    },
    {
      key: 'fzg',
      name: '国家方志馆粤港澳大湾区分馆'
    },
    {
      key: 'ymxy',
      name: '圆明新园'
    },
    {
      key: 'zhuhai_gov_tycg_pingsha_square',
      name: '平沙镇全民健身广场'
    },
    {
      key: 'ywq',
      name: '御温泉'
    },
    {
      key: 'zhuhai_gov_tycg_dangan_square',
      name: '担杆镇全民健身广场'
    },
    {
      key: 'dmtyzx',
      name: '斗门体育中心'
    },
    {
      key: 'zhuhai_gov_tycg_doumen_gym2',
      name: '斗门体育馆'
    },
    {
      key: 'zhuhai_gov_tycg_doumen_fitness',
      name: '斗门全民健身中心'
    },
    {
      key: 'zhuhai_gov_tycg_doumen_gym',
      name: '斗门区体育馆'
    },
    {
      key: 'dmmuseum',
      name: '斗门区博物馆'
    },
    {
      key: 'dmlib',
      name: '斗门区图书馆'
    },
    {
      key: 'dmwhg',
      name: '斗门区文化馆'
    },
    {
      key: 'dmjj',
      name: '斗门旧街'
    },
    {
      key: 'dmfy',
      name: '斗门非遗展示馆'
    },
    {
      key: 'xld',
      name: '星乐度露营小镇'
    },
    {
      key: 'zhuhai_gov_tycg_guishan_square',
      name: '桂山镇全民健身广场'
    },
    {
      key: 'mxpf',
      name: '梅溪牌坊'
    },
    {
      key: 'hqka',
      name: '横琴口岸'
    },
    {
      key: 'hqwlqzx',
      name: '横琴国际网球中心'
    },
    {
      key: 'hqwhys',
      name: '横琴文化艺术中心'
    },
    {
      key: 'hqsdgy',
      name: '横琴湿地公园'
    },
    {
      key: 'zhuhai_gov_bwg_fuhua',
      name: '横琴粤澳深度合作区富华紫檀博物馆'
    },
    {
      key: 'hqhchl',
      name: '横琴花海长廊'
    },
    {
      key: 'hqjrd',
      name: '横琴金融岛'
    },
    {
      key: 'zhuhai_gov_tycg_hengqin_square',
      name: '横琴镇全民健身广场'
    },
    {
      key: 'tcbj',
      name: '汤臣倍健透明工厂'
    },
    {
      key: 'zhmuseum',
      name: '珠海博物馆'
    },
    {
      key: 'zhcec',
      name: '珠海国际会展中心'
    },
    {
      key: 'zhtheatre',
      name: '珠海大剧院'
    },
    {
      key: 'zhtyzx',
      name: '珠海市体育中心'
    },
    {
      key: 'zhuhai_gov_bwg_yuandao',
      name: '珠海市原道文化博物馆'
    },
    {
      key: 'zhuhai_gov_msg_guyuan',
      name: '珠海市古元美术馆'
    },
    {
      key: 'zhlib',
      name: '珠海市图书馆'
    },
    {
      key: 'zhgrwhg',
      name: '珠海市工人文化宫'
    },
    {
      key: 'zhwhg',
      name: '珠海市文化馆'
    },
    {
      key: 'zhuhai_gov_bwg_puji',
      name: '珠海市普济艺术博物馆'
    },
    {
      key: 'zhuhai_gov_bwg_shengbao',
      name: '珠海市盛宝博物馆'
    },
    {
      key: 'zhqsng',
      name: '珠海市青少年妇女儿童活动中心'
    },
    {
      key: 'zhuhai_gov_bwg_handong',
      name: '珠海汉东博物馆'
    },
    {
      key: 'hqw',
      name: '珠海海泉湾度假区'
    },
    {
      key: 'hbgy',
      name: '珠海海滨公园'
    },
    {
      key: 'zhyn',
      name: '珠海渔女景区'
    },
    {
      key: 'zhairshow',
      name: '珠海航展馆'
    },
    {
      key: 'zhplan',
      name: '珠海规划展览馆'
    },
    {
      key: 'zhuhai_gov_bwg_yuhai',
      name: '珠海钰海博物馆'
    },
    {
      key: 'zhhqtj',
      name: '珠海长隆横琴剧院'
    },
    {
      key: 'zhlh',
      name: '珠海长隆海洋王国'
    },
    {
      key: 'zhfclc',
      name: '珠海长隆飞船乐园'
    },
    {
      key: 'zhuhai_gov_bwg_luoxini',
      name: '罗西尼钟表博物馆'
    },
    {
      key: 'yld',
      name: '野狸岛音乐广场'
    },
    {
      key: 'jts',
      name: '金台寺'
    },
    {
      key: 'jhawhys',
      name: '金海岸文化艺术中心'
    },
    {
      key: 'jwtyzx',
      name: '金湾体育中心'
    },
    {
      key: 'zhuhai_gov_tycg_jinwan_square',
      name: '金湾全民健身广场'
    },
    {
      key: 'jwmuseum',
      name: '金湾区博物馆'
    },
    {
      key: 'jwlib',
      name: '金湾区图书馆'
    },
    {
      key: 'jwwhg',
      name: '金湾区文化馆'
    },
    {
      key: 'jwart',
      name: '金湾艺术中心'
    },
    {
      key: 'xsart',
      name: '香山文化艺术中心'
    },
    {
      key: 'zhuhai_gov_bwg_xiangzhou',
      name: '香洲区博物馆'
    },
    {
      key: 'zhuhai_gov_tsg_xiangzhou',
      name: '香洲区图书馆'
    },
    {
      key: 'xzwhg',
      name: '香洲区文化馆'
    },
    {
      key: 'hys',
      name: '黄杨山'
    }
  ]
};

module.exports = {
  cities,
  timeFilters,
  familyFilters,
  typeFilters,
  feeFilters,
  durationFilters,
  districtMapping,
  sourceToVenue,
  venueAddressMap,
  districtsByCity,
  districtPopulation,
  venuesByCity,
  sourceChineseToDistrict,
  districtKeywords
};
