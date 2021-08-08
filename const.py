START = False
PAUSE = False
SAVE_PERCENT = True
LIMIT_VOL: 103
LIMIT_PERCENT: 100
LIMIT_ODD: 349
LIMIT_TIME: 45

CATEGORY = {'all': 'Все матчи', 'live': 'Онлайн матчи', 'prematch': 'Предстоящие матчи'}
FIRST_HALF = {'goal0_5': 0.5, 'goal1_5': 1.5, 'goal2_5': 2.5, 'none': 'нет'}

MONEY = {'min': 0, 'max': 10000000}
PERCENT = {'min': 0, 'max': 100}
COEFF = {'min': 1.01, 'max': 1000}
TIME1 = {'min': 0, 'max': 45}
TIME2 = {'min': 45, 'max': 90}

import numpy


def VOL_RANGE(value):
    return numpy.concatenate(
        (numpy.arange(0, 10, 1),
         [10],
         numpy.arange(10, 100, 5),
         numpy.arange(100, 1000, 50),
         numpy.arange(1000, 10000, 500),
         numpy.arange(10000, 100000, 5000),
         numpy.arange(100000, 1000000, 50000),
         [1000000, '∞', '∞']
         ))[value]


def ODD_RANGE(value):
    return round(numpy.concatenate((
        numpy.arange(1.01, 2, 0.01),
        numpy.arange(2, 3, 0.02),
        numpy.arange(3, 4, 0.05),
        numpy.arange(4, 6, 0.1),
        numpy.arange(6, 10, 0.2),
        numpy.arange(10, 20, 0.5),
        numpy.arange(20, 30, 1),
        numpy.arange(30, 50, 2),
        numpy.arange(50, 100, 5),
        numpy.arange(100, 1010, 10)
    ))[value], 2)


league = {
    11633637: "Argentinian Primera B Metropolitana",
    7511144: "Argentinian Primera C",
    67387: "Argentinian Primera Division",
    12103652: "Argentinian Torneo A",
    803237: "Argentinian Primera B Nacional",
    2888729: "Armenian Premier League",
    9: "Austrian Erste Liga",
    10479956: "Austrian Bundesliga",
    11770149: "Austrian Amateurs",
    12224787: "Belarusian 1st Division",
    12216449: "Belarusian Cup",
    89979: "Belgian First Division A",
    12007003: "Bolivian Liga de Futbol Profesional",
    3127357: "Bosnian Premier League",
    13: "Brazilian Serie A",
    7980087: "Brazilian Serie D",
    12148223: "Brazilian U20",
    321319: "Brazilian Serie B",
    3172302: "Brazilian Serie C",
    12235831: "Brazilian Campeonato Carioca B",
    15: "Bulgarian A League",
    12231751: "Canadian Premier League",
    12366021: "ATP Toronto 2021",
    744098: "Chilean Primera Division",
    857992: "Chilean Primera B",
    879931: "Chinese Super League",
    856134: "Colombian Primera B",
    844197: "Colombian Primera A",
    2079376: "Costa Rican Primera Division",
    17: "Croatian 1 HNL",
    12363255: "Liberec Challenger 2021",
    12204204: "Czech 1 Liga",
    892425: "Czech 3 Liga",
    862638: "Czech 2 Liga",
    12016693: "Danish Women's Matches",
    23: "Danish Superliga",
    25: "Danish 1st Division",
    803690: "Ecuadorian Serie A",
    801976: "Egyptian Premier",
    12009363: "Salvadoran Primera Division",
    12216175: "Estonian Premier League",
    873203: "Estonian Esiliiga",
    47: "Finnish Ykkonen",
    12012945: "Finnish Women's Matches",
    11887991: "Finnish Kakkonen",
    45: "Finnish Veikkausliiga",
    57: "French Ligue 2",
    12206060: "French National 2",
    55: "French Ligue 1",
    2273834: "Georgian Umaglesi Liga",
    11591693: "German 3 Liga",
    853948: "German Regionalliga Bavaria",
    59: "German Bundesliga",
    318343: "German Regionalliga Northeast",
    61: "German Bundesliga 2",
    11458113: "German Cup",
    6566654: "Guatemalan Liga Nacional",
    12202271: "Honduras Liga Nacional",
    1842928: "Hungarian NB I",
    4556576: "Hungarian NB II",
    12209556: "Icelandic Urvalsdeild",
    12005119: "Icelandic Women's Matches",
    12006352: "Icelandic 4 Deild",
    12363303: "WTA Cluj-Napoca 2021",
    11638775: "CS:GO",
    11426307: "DOTA 2",
    12291729: "LOL 2021",
    10546040: "Swedish SHL",
    10546104: "Russian KHL",
    12247754: "Elite Friendlies",
    11432305: "NFL Preseason Matches",
    12222436: "Dominican Republic Matches",
    12242357: "UEFA Champions League Qualifiers",
    12005859: "Friendly Matches",
    9617433: "ITF Germany Futures",
    12365799: "National Bank Open 2021",
    11799196: "Irish Women's Matches",
    12203971: "Irish Premier Division",
    12005855: "Irish Division 1",
    12007809: "Israeli Toto Cup Leumit",
    12363227: "Cordenons Challenger 2021",
    12214429: "Italian Cup",
    81: "Italian Serie A",
    1062024: "Japanese J League 2",
    89: "Japanese J League",
    12213822: "South Korean K League Challenge",
    12209550: "South Korean K League Classic",
    1587980: "Lithuanian 1 Lyga",
    879221: "Lithuanian A Lyga",
    4515700: "Luxembourg Division Nationale",
    1476085: "Malaysian Premier League",
    840886: "Malaysian Super League",
    5627174: "Mexican Liga MX",
    12007718: "Mexican Women's Matches",
    12009467: "Moldovan Divizia Nationala",
    12208242: "Montenegrin 1st League",
    9404054: "Dutch Eredivisie",
    11: "Dutch Eerste Divisie",
    11424392: "Dutch Super Cup",
    12200621: "Nicaraguan Primera Division",
    1517121: "Macedonian 1st League",
    11068551: "Norwegian Eliteserien",
    12007716: "Norwegian Women's Matches",
    3972877: "Panamanian Premier League",
    839575: "Paraguayan Primera Division",
    12013277: "Paraguayan Segunda Divsion",
    8594603: "Peruvian Primera Division",
    7710075: "Polish III Liga",
    97: "Polish Ekstraklasa",
    11838780: "Polish 2 Liga",
    403085: "Polish I Liga",
    99: "Portuguese Primeira Liga",
    9513: "Portuguese Segunda Liga",
    11802732: "Portuguese U19 Championship",
    4905: "Romanian Liga I",
    862579: "Romanian Liga II",
    8070418: "Russian Football National League",
    101: "Russian Premier League",
    7426251: "Russian Women's Matches",
    12218903: "Russian Professional Football League",
    12212459: "Serbian First League",
    103: "Serbian Super League",
    848322: "Singapore S-League",
    12013300: "Slovakian Super League",
    12215677: "Slovakian 2 Liga",
    115: "Slovenian Premier League",
    8995647: "Slovenian 2 SNL",
    117: "Spanish La Liga",
    12363525: "UTR Barcelona Men’s 6 2021",
    920223: "Swedish Division 2",
    12202373: "Swedish Superettan",
    129: "Swedish Allsvenskan",
    135: "Swiss Challenge League",
    8964557: "Swiss 1 Liga Promotion",
    133: "Swiss Super League",
    139: "Ukrainian Premier League",
    12290898: "LOL - LEC Split",
    35: "English League 1",
    107: "Scottish Championship",
    12335763: "Women's Olympics 2020",
    10932509: "English Premier League",
    12282733: "NFL",
    12290952: "LOL - LPL Split",
    12344448: "Women's Olympics 2020",
    7129730: "English Championship",
    12335751: "Women's Olympics 2020",
    105: "Scottish Premiership",
    109: "Scottish League One",
    340643: "English Community Shield",
    12290864: "LOL - TCL Season",
    37: "English League 2",
    111: "Scottish League Two",
    12290868: "LOL - CBLOL Split Season",
    2134: "English Football League Cup",
    12364547: "ITF Pescara",
    12216637: "US United Soccer League",
    12362985: "WTA San Jose 2021",
    12331715: "US National Women Soccer League",
    12363621: "WTA Concord 2021",
    12324198: "US USL League One",
    12362677: "ATP Washington 2021",
    141: "US Major League Soccer",
    843454: "Uruguayan Primera Division",
    1065530: "Venezuelan Primera Division"
}
