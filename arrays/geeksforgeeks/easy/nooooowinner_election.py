'''Given an array of n names arr of candidates in an election, 
where each name is a string of lowercase characters. A candidate
 name in the array represents a vote casted to the candidate. 
 Print the name of the candidate that received the maximum count
   of votes. If there is a draw between two candidates, then print lexicographically smaller name.'''

def winner(arr, n):
    dict1 = {}
    for name in arr:
        if name in dict1:
            dict1[name] += 1
        else:
            dict1[name] = 1
    print(dict1['rbwsb'])
    maxi = 0
    nmax = 'zzzzzzzzzzzzzzzz'
    res = []
    for k, v in dict1.items():
        if v == 2 :
            res.append((k,v))
    return res

arr = [
    'rlixc', 'bfztu', 'qsyil', 'vuszo', 'onosn', 'wetzt', 'enmmt', 'wsfno', 
    'btuqc', 'otaqu', 'knrjf', 'zhtdc', 'kdvoz', 'lxzbl', 'fhvuw', 'woreo', 
    'ajfep', 'smypy', 'cfdly', 'iqhjw', 'egkya', 'kppfz', 'ubxmp', 'pjnqb', 
    'ryzmx', 'djwag', 'chhax', 'saggq', 'fpjdy', 'izhnt', 'hdhiv', 'prwsu', 
    'fltqf', 'yqeii', 'pzyhl', 'dxnsu', 'orzuh', 'ukyde', 'taxhm', 'svwvg', 
    'ezlkn', 'bbsmi', 'rilmi', 'blxsa', 'buumt', 'yqzvz', 'uxqpc', 'nsvqo', 
    'fepwn', 'axuxi', 'ervbt', 'nxbkk', 'mkjbb', 'mjbip', 'rfocn', 'yxxks', 
    'hvdaf', 'bvugi', 'qgbyw', 'iasoo', 'zkmkd', 'oerpp', 'onstp', 'uiqtp', 
    'cesqq', 'uuahy', 'sugyb', 'jnbej', 'rlrta', 'dffkb', 'vruet', 'mklwx', 
    'anera', 'vrzdx', 'osidj', 'nfzsp', 'rnhry', 'giumk', 'nyrhe', 'gaftn', 
    'qoonf', 'zlods', 'dhglk', 'ghndy', 'aflzz', 'wxuda', 'wzizc', 'whqxc', 
    'tyzux', 'ahroe', 'qfsyj', 'ulsyo', 'cqkza', 'auitf', 'aoqhf', 'ecljd', 
    'azsmo', 'uxtag', 'uqoyd', 'iuoeh', 'wenkd', 'ftpul', 'xuiml', 'atsmy', 
    'zgfwe', 'zracr', 'vxbdu', 'ogvup', 'otuth', 'sbwcz', 'gzpjy', 'qfuyr', 
    'rtizy', 'zdqkt', 'znpym', 'fdzad', 'mnfsz', 'gfpvk', 'icvbc', 'wgqfu', 
    'blrea', 'qgycm', 'thejt', 'qvirb', 'uuwcv', 'ucthl', 'ragfd', 'wjvpg', 
    'jjxux', 'sgjix', 'xsiiy', 'kauna', 'dnfep', 'lmads', 'tcnul', 'gsski', 
    'wkhxy', 'kprts', 'mrfqo', 'gdlme', 'nhmju', 'odxxx', 'udcrh', 'kbzwt', 
    'msbwy', 'hnklh', 'uhezj', 'xfydy', 'fmnad', 'ulovf', 'agpif', 'skbfm', 
    'zdpwx', 'thcgd', 'sdvbh', 'hslpw', 'ucoet', 'ylewc', 'izbqp', 'fpidr', 
    'vwxoh', 'pyxqh', 'cuxhg', 'qukph', 'nyjkg', 'bhfgv', 'hkcwl', 'terko', 
    'wuvqb', 'kgpzi', 'ddqky', 'ekklk', 'hsyvx', 'rhiij', 'pstbe', 'hpdac', 
    'byaga', 'zhikn', 'zfppz', 'rglkr', 'itxsr', 'acqqz', 'wkeem', 'ouqtk', 
    'vzeiv', 'ruvvb', 'cblzs', 'mbgvz', 'iqlpo', 'caurc', 'ihxni', 'upijz', 
    'jsilb', 'pcusq', 'zoqpe', 'lvzno', 'cvqew', 'hkkob', 'pyfik', 'dvzpp', 
    'ncozi', 'lnbel', 'kecef', 'buitv', 'wsqiz', 'fwqtc', 'gqdmm', 'lvvlg', 
    'ullnq', 'ltqmm', 'qvrtn', 'skxgc', 'ocnpw', 'wsjhx', 'rhmig', 'rrrtk', 
    'vxhvt', 'nysrg', 'mxrrk', 'qxqcb', 'jofvq', 'xnlca', 'hnziz', 'tbwte', 
    'udexe', 'xsypr', 'fzwxn', 'hmqhd', 'ueuha', 'hlklh', 'eomyh', 'oagri', 
    'xglny', 'somlm', 'drobt', 'miydb', 'ohskl', 'rmgrh', 'gfguc', 'ocucn', 
    'xeqmb', 'cjzwq', 'twjpk', 'nbhlk', 'pcthe', 'wgrgw', 'owzmv', 'hjenb', 
    'wzglg', 'nfuol', 'jitnj', 'prmst', 'uwxcy', 'rbwsb', 'ffzsd', 'fcvlw', 
    'nyjwj', 'ykeva', 'qfviu', 'lcsac', 'fjuwz', 'slssh', 'ouhdy', 'piigt', 
    'quhmo', 'duxmv', 'qxnss', 'snukk', 'tuuqc', 'qweyj', 'dvoco', 'zkwmm', 
    'asfie', 'vkgjv', 'ulhjo', 'ksbaq', 'kcrbs', 'nnyae', 'dkcsw', 'oxyab', 
    'xwwmq', 'mepny', 'bpxoc', 'ziqby', 'zrfcs', 'fmlgz', 'vescw', 'uucsw', 
    'kolzs', 'qipqz', 'jowyl', 'qqrmm', 'badgp', 'hzjth', 'hifte', 'ubzkw', 
    'bvvtj', 'prksn', 'wuhxd', 'pfvkd', 'dlqhu', 'htjqn', 'mnlka', 'icwvi', 
    'yziqp', 'ifszc', 'tqldo', 'sufrk', 'pttaf', 'jlovh', 'ispmu', 'ctxkd', 
    'ojinw', 'ejhcp', 'tifmc', 'hwipk', 'laygc', 'fullv', 'gqvst', 'wmybi', 
    'jlknw', 'dzcsf', 'luidw', 'qnmtm', 'mkvyx', 'gnoij', 'ljclr', 'onalo', 
    'oblnv', 'bolvo', 'rdkza', 'knfxw', 'lgrlj', 'xptyi', 'ywglq', 'pcllt', 
    'lqlmp', 'hxvqb', 'vhxyd', 'kxzto', 'lsvsq', 'oifco', 'iiufs', 'wjtgb', 
    'pajdg', 'arslm', 'uuggt', 'rhqvi', 'tcnjc', 'hzcpv', 'dlvgh', 'bugum', 
    'kjwdc', 'pcanm', 'tnjwd', 'lzzin', 'cbrhj', 'gzhsx', 'hvoow', 'igult', 
    'mzmni', 'phliv', 'hvifs', 'kxdqp', 'rbwsb', 'jsbmt', 'hldkd', 'zntaz', 
    'keneg', 'kcxxs', 'fqfxk', 'hovaj', 'fhude', 'ykrsg', 'bnnzw', 'sdgqa', 
    'fmveg', 'qalaz', 'ligfb', 'xcsdx', 'qpblz', 'jmfym', 'teblh', 'dhdaq', 
    'xvabd', 'kpafm', 'nvuqe', 'glfad', 'psmmr', 'zewpw', 'luyfy', 'frzkd', 
    'jngrg', 'zuhfa', 'tpson', 'ramwj', 'fzelw', 'bsqot', 'hrfao', 'kfpsy', 
    'aszuu', 'ibqat', 'ujvtf', 'qzizr', 'mvaxx', 'debkt', 'czqfd', 'itlfs', 
    'uecfo', 'vavqc', 'vpnpb', 'vmugt', 'icwnn', 'mwrpb', 'fkbff', 'tzjgp', 
    'iflgm', 'tzkve', 'ecadi', 'xxbng', 'imrdm', 'ipfkv', 'pcmsl', 'sjudo', 
    'gegsb', 'pgovg', 'gnfaw', 'wnfty', 'jfujr', 'lrbwz', 'jxveg', 'eayuv', 
    'fpvjs', 'vtfki', 'eblxy', 'ponbj', 'afhwg', 'qpldk', 'zdirn', 'ujpve', 
    'shytz', 'yxhyw', 'obchy', 'uvvch', 'fzorh', 'iotei', 'flsbz', 'girld', 
    'bocdf', 'uhrup', 'ylsos', 'qvrvt', 'gsmff', 'ouafg', 'hacix', 'lnzei', 
    'ogcww', 'rsdog', 'dmwix', 'pndei', 'bcbld', 'cbete', 'cxvpp', 'gvcez', 
    'lbvzl', 'bdtub', 'ceszx', 'scgxu', 'tqssz', 'yflcn', 'vjsbp', 'sxfmv', 
    'nxxkn', 'kozcp', 'uwkts', 'yhdiv', 'hxzni', 'ozppo', 'rtawq', 'dnxil', 
    'mkuym', 'iwxot', 'wnajp', 'imqsy', 'movfx', 'cjdkq', 'dcpsj', 'saalo', 
    'zlwxs', 'ompmd', 'elflh', 'kosgu', 'ibrzp', 'xqlma', 'jgvwy', 'oojee', 
    'mwqqg', 'khztw', 'ojash', 'nfbdu', 'shcqv', 'kpxtl', 'xiisx', 'hqhgs', 
    'awnfn', 'fcgqw', 'lgjml', 'pswcz', 'wqzkj', 'fvrzc', 'dmltq', 'vvryg', 
    'epibh', 'mpsza', 'mrmsn', 'lhjsl', 'ohkkz', 'cqdmm', 'rlraf', 'yhijb', 
    'eywai', 'dvkqp', 'hwwsc', 'schxh', 'bfecn', 'lvjrp', 'ttwdv', 'vmlvn', 
    'rcoah', 'borul', 'bgykr', 'jrakx', 'mhqgc', 'mqpas', 'inmfe', 'gyvmp', 
    'jqdps', 'qxdsd', 'vstzp', 'banqo', 'lcbjh', 'eewcd', 'gylvd', 'ealdd', 
    'dzyyq', 'qikgl', 'sukqp', 'ckpwi', 'yuehn', 'ocpxu', 'fxpga', 'jnvwf', 
    'gejit', 'obfon', 'scexh', 'ghzje', 'tqvaz', 'wfpoe', 'adqzj', 'chwkt', 
    'ojciv', 'dznwp', 'anuha', 'wpalz', 'kyjut', 'grfkz', 'vkcfk', 'ujcbq', 
    'pataj', 'ypoey', 'hiypz', 'huage', 'vraeg', 'yoyjs', 'zutje', 'mnkkk', 
    'rrspq', 'wotfv', 'ehnrn', 'sxmkt', 'lesgk', 'xqgwj', 'qeexf', 'cupck', 
    'viktj', 'dsgov', 'wwyyl', 'szqss', 'hqxaq', 'gsgmp', 'rprng', 'zkeoj', 
    'rsrnl', 'dihbx', 'ezmlv', 'kygcd', 'xlvuw', 'iorzy', 'oslxg', 'dbofi', 
    'iubtx', 'tbdys', 'qzktk', 'uzmgy', 'zdkun', 'mgarz', 'hjfpx', 'gkioq', 
    'ifftw', 'mxxyj', 'joogm', 'uxrlq', 'puzzo', 'sghri', 'oupoy', 'xrrho', 
    'dazny', 'zzfvi', 'jumyx', 'mgswl', 'ultlj', 'tzdfr', 'gjuqv', 'mjvie', 
    'drqox', 'tsgrw', 'kcxzf', 'qfkpr', 'mqfwe', 'kxrwe', 'ajxdf', 'bjkky', 
    'nomer', 'zqcwq', 'mtcjh', 'voagb', 'gpvfc', 'ivueu', 'xplbe', 'yiufm', 
    'jitbe', 'tsgvz', 'cyplw', 'pywzp', 'ywolr', 'duwzq', 'il aas', 'rdkja', 
    'azoif', 'zowim', 'rwkoy', 'ezuhp', 'krest', 'pwedo', 'mafax', 'rcwfw', 
    'anhuw', 'prxrd', 'spzcr', 'hvxdp', 'phnae', 'ovmea', 'ouqbz', 'jctac', 
    'rjyws', 'wdbdp', 'unlla', 'pcrdz', 'lgnmd', 'pmmgp', 'udfap', 'qppex', 
    'poeqe', 'mdkev', 'iapwl', 'jfrfa', 'bkwpt', 'ppgcr', 'mtpzr', 'lakwm', 
    'ahimc', 'hsbuv', 'celnh', 'ozrxw', 'rigeq', 'byoch', 'ndrti', 'qxtrw', 
    'esrnf', 'shuuz', 'baozu', 'usbca', 'nnqpx', 'fqqhr', 'wfhcw', 'gabtp', 
    'dxsmg', 'anpyo', 'zdlnl', 'efved', 'jvghk', 'czaal', 'hhcgn', 'xtwmn', 
    'qiwhq', 'pgcjg', 'uncnt', 'grato', 'efdqp', 'pztel', 'kkubm', 'yywbo', 
    'caddl', 'pieby', 'rnbek', 'ennxa', 'hsgny', 'zzxwf', 'zjgfl', 'wihsg', 
    'fleze', 'eckhn', 'nrdig', 'gkoui', 'dalfe', 'snroc', 'ajfai', 'gkuda', 
    'zdonm', 'dyqgj', 'ltzly', 'xxmtk', 'yfuxw', 'rygmk', 'tdlcv', 'ezhvi', 
    'dtuny', 'otitd', 'oxelr', 'fuabq', 'fsqhe', 'itaxd', 'ggllk', 'ccfap', 
    'ciqjn', 'esobs', 'gjkct', 'jzueq', 'iecse', 'unvbw', 'yjobm', 'anwsv', 
    'owbxy', 'bcepn', 'agdxs', 'hglxy', 'zomte', 'pjhlg', 'pkswe', 'oruek', 
    'puhta', 'ijbny', 'zjgbe', 'ktbpk', 'dmtdu', 'ifovd', 'fiatc', 'fzcyf', 
    'zxbhs', 'hfefj', 'jjtoe', 'omqbp', 'aoqfd', 'hpurd', 'zbyjq', 'dysyq', 
    'gfndy', 'bewye', 'qlnyf', 'gsemz', 'zjinx', 'weidm', 'sayhc', 'smpzd', 
    'smjxw', 'vjgyi', 'tzqid', 'hqjoi', 'qmvjn', 'zspoo', 'saass', 'frjds', 
    'nlmtr', 'fvsjp', 'ezdzo', 'gsdvq', 'bakcb', 'rucpx', 'wzemp', 'elhpb', 
    'xtalr', 'zgzma', 'zkxpo', 'ditfg', 'snoan', 'mqbjc', 'eacpx', 'kpckh', 
    'pzghm', 'qofwn', 'rtata', 'szuwn', 'snhjt', 'llmlg', 'uisje', 'jikns', 
    'cvjoj', 'hxekf', 'sncdt', 'ltaub', 'coknb', 'lvhhx'
]

n = len(arr)

res = winner(arr, n)
print(res)