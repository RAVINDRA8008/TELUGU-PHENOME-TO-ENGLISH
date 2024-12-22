phoneme_map = {
    # Vowels
    'అ': 'a', 'ఆ': 'aa', 'ఇ': 'i', 'ఈ': 'ee', 'ఉ': 'u', 'ఊ': 'oo',
    'ఋ': 'ru', 'ౠ': 'ruu', 'ఎ': 'e', 'ఏ': 'ee', 'ఐ': 'ai', 'ఒ': 'o', 'ఓ': 'oo', 'ఔ': 'au',

    # Consonants
    'క': 'ka', 'ఖ': 'kha', 'గ': 'ga', 'ఘ': 'gha', 'ఙ': 'nga',
    'చ': 'cha', 'ఛ': 'chha', 'జ': 'ja', 'ఝ': 'jha', 'ఞ': 'nya',
    'ట': 'ṭa', 'ఠ': 'ṭha', 'డ': 'ḍa', 'ఢ': 'ḍha', 'ణ': 'ṇa',
    'త': 'ta', 'థ': 'tha', 'ద': 'dha', 'ధ': 'dhha', 'న': 'na',
    'ప': 'pa', 'ఫ': 'pha', 'బ': 'ba', 'భ': 'bha', 'మ': 'ma',
    'య': 'ya', 'ర': 'ra', 'ల': 'la', 'వ': 'va', 'శ': 'sha',
    'ష': 'ssa', 'స': 'sa', 'హ': 'ha', 'ళ': 'lla', 'ం': 'm', 'ః': 'h',

    # Vowel diacritics
    'ా': 'aa', 'ి': 'i', 'ీ': 'ee', 'ు': 'u', 'ూ': 'oo', 'ృ': 'ru', 'ౄ': 'ruu',
    'ె': 'e', 'ే': 'ee', 'ై': 'ai', 'ొ': 'o', 'ో': 'oo', 'ౌ': 'au',

    # Virama (indicates the absence of a vowel)
    '్': '',

    # 'క' - Ka
    'క': 'ka', 'కా': 'kaa', 'కి': 'ki', 'కీ': 'kee', 'కు': 'ku',
    'కూ': 'koo', 'కృ': 'kru', 'కౄ': 'kroo', 'కె': 'ke', 'కే': 'kay',
    'కై': 'kai', 'కొ': 'ko', 'కో': 'kow', 'కౌ': 'kau', 'కం': 'kam', 'కః': 'kaha',

    # 'ఖ' - Kha
    'ఖ': 'kha', 'ఖా': 'khaa', 'ఖి': 'khi', 'ఖీ': 'khee', 'ఖు': 'khu',
    'ఖూ': 'khoo', 'ఖృ': 'khru', 'ఖౄ': 'khroo', 'ఖె': 'khe', 'ఖే': 'khay',
    'ఖై': 'khai', 'ఖొ': 'kho', 'ఖో': 'khow', 'ఖౌ': 'khau', 'ఖం': 'kham', 'ఖః': 'khaha',

    # 'గ' - Ga
    'గ': 'ga', 'గా': 'gaa', 'గి': 'gi', 'గీ': 'gee', 'గు': 'gu',
    'గూ': 'goo', 'గృ': 'gru', 'గౄ': 'groo', 'గె': 'ge', 'గే': 'gay',
    'గై': 'gai', 'గొ': 'go', 'గో': 'gow', 'గౌ': 'gau', 'గం': 'gam', 'గః': 'gaha',

    # 'ఘ' - Gha
    'ఘ': 'gha', 'ఘా': 'ghaa', 'ఘి': 'ghi', 'ఘీ': 'ghee', 'ఘు': 'ghu',
    'ఘూ': 'ghow', 'ఘృ': 'ghru', 'ఘౄ': 'ghroo', 'ఘె': 'ghe', 'ఘే': 'ghay',
    'ఘై': 'ghai', 'ఘొ': 'gho', 'ఘౌ': 'ghau', 'ఘం': 'gham', 'ఘః': 'ghaha',

    # 'చ' - Cha
    'చ': 'cha', 'చా': 'chaa', 'చి': 'chi', 'చీ': 'chee', 'చు': 'chu',
    'చూ': 'choo', 'చృ': 'chru', 'చౄ': 'chroo', 'చె': 'che', 'చే': 'chey',
    'చై': 'chai', 'చొ': 'cho', 'చో': 'chow', 'చౌ': 'chai', 'చం': 'cham', 'చః': 'chaha',

    # 'ఛ' - cHa
    'ఛ': 'cHa', 'ఛా': 'cHaa', 'ఛి': 'cHi', 'ఛీ': 'cHee', 'ఛు': 'cHu',
    'ఛూ': 'cHoo', 'ఛృ': 'cHru', 'ఛౄ': 'cHroo', 'ఛె': 'cHe', 'ఛే': 'cHey',
    'ఛై': 'cHai', 'ఛొ': 'cHo', 'ఛో': 'cHow', 'ఛౌ': 'cHau', 'ఛం': 'cHam', 'ఛః': 'cHaha',

    # 'జ' - Ja
    'జ': 'ja', 'జా': 'jaa', 'జి': 'ji', 'జీ': 'jee', 'జు': 'ju',
    'జూ': 'joo', 'జృ': 'jru', 'జౄ': 'jroo', 'జె': 'j', 'జే': 'jae',
    'జై': 'jai', 'జొ': 'jo', 'జో': 'jow', 'జౌ': 'jau', 'జం': 'jam', 'జః': 'jaha',

    # 'ఝ' - Jha
    'ఝ': 'jha', 'ఝా': 'jhaa', 'ఝి': 'jhi', 'ఝీ': 'jhee', 'ఝు': 'jhu',
    'ఝూ': 'jhoo', 'ఝృ': 'jhru', 'ఝౄ': 'jhroo', 'ఝె': 'jhe', 'ఝే': 'jhew',
    'ఝై': 'jhai', 'ఝొ': 'jho', 'ఝో': 'jhoo', 'ఝౌ': 'jhau', 'ఝం': 'jham', 'ఝః': 'jhaha',

    # 'ట' - Ta
    'ట': 'ta', 'టా': 'taa', 'టి': 'ti', 'టీ': 'tee', 'టు': 'tu',
    'టూ': 'too', 'టృ': 'tru', 'టౄ': 'true', 'టె': 'te', 'టే': 'teh',
    'టై': 'tai', 'టొ': 'tow', 'టో': 'toe', 'టౌ': 'tau', 'టం': 'tam', 'టః': 'taha',

    # 'ఠ' - Tta
    'ఠ': 'Tta', 'ఠా': 'Ttaa', 'ఠి': 'Tti', 'ఠీ': 'Ttee', 'ఠు': 'Ttu',
    'ఠూ': 'Ttoo', 'ఠృ': 'Ttru', 'ఠౄ': 'Ttoo', 'ఠె': 'Tte', 'ఠే': 'Ttey',
    'ఠై': 'Ttai', 'ఠొ': 'Tto', 'ఠో': 'Ttow', 'ఠౌ': 'Ttou', 'ఠం': 'Ttam', 'ఠః': 'Ttaha',

    # 'డ' - Da
    'డ': 'da', 'డా': 'daa', 'డి': 'di', 'డీ': 'dee', 'డు': 'do',
    'డూ': 'doo', 'డృ': 'dru', 'డౄ': 'droo', 'డె': 'de', 'డే': 'day',
    'డై': 'dai', 'డొ': 'do', 'డో': 'dow', 'డౌ': 'dau', 'డం': 'dam', 'డః': 'daha',

    # 'ఢ' - Dha
    'ఢ': 'dha', 'ఢా': 'dhaa', 'ఢి': 'dhi', 'ఢీ': 'dhee', 'ఢు': 'dhu',
    'ఢూ': 'dhoo', 'ఢృ': 'dhru', 'ఢౄ': 'dhroo', 'ఢె': 'dhe', 'ఢే': 'dhay',
    'ఢై': 'dhai', 'ఢొ': 'dho', 'ఢో': 'dhow', 'ఢౌ': 'dhau', 'ఢం': 'dham', 'ఢః': 'dhaha',

    # 'న' - Na
    'న': 'na', 'నా': 'naa', 'ని': 'ni', 'నీ': 'nee', 'ను': 'nu',
    'నూ': 'noo', 'నృ': 'nru', 'నౄ': 'nroo', 'నె': 'ne', 'నే': 'ney',
    'నై': 'nai', 'నొ': 'no', 'నో': 'nOO', 'నౌ': 'nau', 'నం': 'nam', 'నః': 'naha',

    # 'త' - Tha
    'త': 'tha', 'తా': 'thaa', 'తి': 'thi', 'తీ': 'thee', 'తు': 'thu',
    'తూ': 'thoo', 'తృ': 'thru', 'తౄ': 'throo', 'తె': 'the', 'తే': 'they',
    'తై': 'thai', 'తొ': 'tho', 'తో': 'thow', 'తౌ': 'thau', 'తం': 'tham', 'తః': 'thaha',

    # 'థ' - Tha
    'థ': 'tha', 'థా': 'thaa', 'థి': 'thi', 'థీ': 'thee', 'థు': 'thu',
    'థూ': 'thoo', 'థృ': 'thru', 'థౄ': 'throo', 'థె': 'the', 'థే': 'they',
    'థై': 'thai', 'థొ': 'tho', 'థో': 'thoo', 'థౌ': 'thau', 'థం': 'tham', 'థః': 'thaha',

    # 'ద' - Dha
    'ద': 'dha', 'దా': 'dhaa', 'ది': 'dhi', 'దీ': 'dhee', 'దు': 'dru',
    'దూ': 'dhoo', 'దృ': 'dhru', 'దౄ': 'dhroo', 'దె': 'dhe', 'దే': 'dhay',
    'దై': 'dhai', 'దొ': 'dho', 'దో': 'dhow', 'దౌ': 'dhau', 'దం': 'dham', 'దః': 'dhaha',

    # 'ధ' - dHa
    'ధ': 'dHa', 'ధా': 'dHaa', 'ధి': 'dHi', 'ధీ': 'dHee', 'ధు': 'dHu',
    'ధూ': 'dHoo', 'ధృ': 'dHru', 'ధౄ': 'dHroo', 'ధె': 'dHe', 'ధే': 'dHey',
    'ధై': 'dHai', 'ధొ': 'dHo', 'ధో': 'dHow', 'ధౌ': 'dHau', 'ధం': 'dHam', 'ధః': 'dHaha',

    # 'ణ' - Nha
    'ణ': 'nha','ణా': 'naa','ణి': 'ni','ణీ': 'nii','ణు': 'nu',
    'ణూ': 'nuu','ణృ': 'nr','ణౄ': 'nru','ణె': 'ne','ణే': 'ney',
    'ణై': 'nai','ణొ': 'no','ణో': 'noo','ణౌ': 'nau','ణం': 'nam','ణః': 'naha',

    # 'ప' - Pa
    'ప': 'pa', 'పా': 'paa', 'పీ': 'pee', 'పి': 'pi', 'పు': 'pu',
    'పూ': 'poo', 'పృ': 'pru', 'పౄ': 'proo', 'పె': 'pe', 'పే': 'pey',
    'పై': 'pai', 'పొ': 'po', 'పో': 'po', 'పౌ': 'pau', 'పం': 'pam', 'పః': 'paha',

    # 'ఫ' - Pha
    'ఫ': 'pha', 'ఫా': 'phaa', 'ఫి': 'phi', 'ఫీ': 'phii', 'ఫు': 'phu',
    'ఫూ': 'phoo', 'ఫృ': 'phru', 'ఫౄ': 'phroo', 'ఫె': 'phe', 'ఫే': 'phey',
    'ఫై': 'phai', 'ఫొ': 'pho', 'ఫో': 'phow', 'ఫౌ': 'phau', 'ఫం': 'pham', 'ఫః': 'phaha',

    # 'బ' - Ba
    'బ': 'ba', 'బా': 'baa', 'బి': 'bi', 'బీ': 'bee', 'బు': 'bu',
    'బూ': 'boo', 'బృ': 'bru', 'బౄ': 'broo', 'బె': 'be', 'బే': 'bey',
    'బై': 'bai', 'బొ': 'bo', 'బో': 'bo', 'బౌ': 'bau', 'బం': 'bam', 'బః': 'baha',

    # 'భ' - Bha
    'భ': 'bha', 'భా': 'bhaa', 'భి': 'bhi', 'భీ': 'bhee', 'భు': 'bhu',
    'భూ': 'bhoo', 'భృ': 'bhru', 'భౄ': 'bhroo', 'భె': 'bhe', 'భే': 'bhey',
    'భై': 'bhai', 'భొ': 'bho', 'భో': 'bhow', 'భౌ': 'bhau', 'భం': 'bham', 'భః': 'bhaha',

    # 'మ' - Ma
    'మ': 'ma', 'మా': 'maa', 'మి': 'mi', 'మీ': 'mee', 'ము': 'mu',
    'మూ': 'moo', 'మృ': 'mru', 'మౄ': 'mroo', 'మె': 'me', 'మే': 'mey',
    'మై': 'mai', 'మొ': 'mo', 'మో': 'mo', 'మౌ': 'mau', 'మం': 'mam', 'మః': 'maha',

    # 'య' - Ya
    'య': 'ya', 'యా': 'yaa', 'యి': 'yi', 'యీ': 'yee', 'యు': 'yu',
    'యూ': 'yoo', 'యృ': 'yru', 'యౄ': 'yroo', 'యె': 'ye', 'యే': 'yeh',
    'యై': 'yai', 'యొ': 'yo', 'యో': 'yo', 'యౌ': 'yau', 'యం': 'yam', 'యః': 'yaha',

    # 'ర' - Ra
    'ర': 'ra', 'రా': 'raa', 'రి': 'ri', 'రీ': 'ree', 'రు': 'ru',
    'రూ': 'roo', 'రృ': 'ru', 'రౄ': 'roo', 'రె': 're', 'రే': 'rey',
    'రై': 'rai', 'రొ': 'ro', 'రో': 'row', 'రౌ': 'rau', 'రం': 'ram', 'రః': 'raha',

    # 'ల' - La
    'ల': 'la', 'లా': 'laa', 'లి': 'li', 'లీ': 'lee', 'లు': 'lu',
    'లూ': 'loo', 'లృ': 'lru', 'లౄ': 'lroo', 'లె': 'le', 'లే': 'ley',
    'లై': 'lai', 'లో': 'lo', 'లో': 'low', 'లౌ': 'lau', 'లం': 'lam', 'లః': 'laha',

    # 'వ' - Va
    'వ': 'va', 'వా': 'vaa', 'వి': 'vi', 'వీ': 'vee', 'వు': 'vu',
    'వూ': 'voo', 'వృ': 'vru', 'వౄ': 'vroo', 'వె': 've', 'వే': 'vey',
    'వై': 'vai', 'వొ': 'vo', 'వో': 'vow', 'వౌ': 'vau', 'వం': 'vam', 'వః': 'vaha',

    # 'శ' - Sha
    'శ': 'sha', 'శా': 'shaa', 'శి': 'shi', 'శీ': 'shee', 'శు': 'shu',
    'శూ': 'shoo', 'శృ': 'shru', 'శౄ': 'shroo', 'శె': 'she', 'శే': 'shay',
    'శై': 'shai', 'శొ': 'sho', 'శో': 'show', 'శౌ': 'shau', 'శం': 'sham', 'శః': 'shaha',

    # 'ష' - Ssa
    'ష': 'ssa', 'షా': 'ssaa', 'షి': 'ssi', 'షీ': 'ssii', 'షు': 'ssu',
    'షూ': 'ssuu', 'షృ': 'ssru', 'షౄ': 'ssroo', 'షె': 'sse', 'షే': 'ssay',
    'షై': 'ssai', 'షొ': 'sso', 'షో': 'ssow', 'షౌ': 'ssau', 'షం': 'ssam', 'షః': 'ssaha',

    # 'స' - Sa
    'స': 'sa', 'సా': 'saa', 'సి': 'si', 'సీ': 'see', 'సు': 'su',
    'సూ': 'soo', 'సృ': 'sru', 'సౄ': 'sroo', 'సె': 'se', 'సే': 'sey',
    'సై': 'sai', 'సొ': 'so', 'సో': 'so', 'సౌ': 'sau', 'సం': 'sam', 'సః': 'saha',

    # 'హ' - Ha
    'హ': 'ha', 'హా': 'haa', 'హి': 'hi', 'హీ': 'hee', 'హు': 'hu',
    'హూ': 'hoo', 'హృ': 'hru', 'హౄ': 'hroo', 'హె': 'he', 'హే': 'hey',
    'హై': 'hai', 'హొ': 'ho', 'హో': 'how', 'హౌ': 'hau', 'హం': 'ham', 'హః': 'haha',

    # 'ళ' - la
    'ళ': 'ḷa', 'ళా': 'ḷaa', 'ళి': 'ḷi', 'ళీ': 'ḷee', 'ళు': 'ḷu',

    'ళూ': 'ḷoo', 'ళృ': 'ḷru', 'ళౄ': 'ḷroo', 'ళె': 'ḷe', 'ళే': 'ḷay',

    'ళై': 'ḷai', 'ళొ': 'ḷo', 'ళో': 'ḷow', 'ళౌ': 'ḷau', 'ళం': 'ḷam', 'ళః': 'ḷaha',

    # 'క్ష' - Ksha
    'క్ష': 'ksha', 'క్షా': 'kshaa', 'క్షి': 'kshi', 'క్షీ': 'kshii', 'క్షు': 'kshu',
    'క్షూ': 'kshoo', 'క్షృ': 'kshru', 'క్షౄ': 'kshroo', 'క్షె': 'kshe', 'క్షే': 'kshay',
    'క్షై': 'kshai', 'క్షొ': 'ksho', 'క్షో': 'kshow', 'క్షౌ': 'kshau', 'క్షం': 'ksham', 'క్షః': 'kshaha',

    # 'ఱ' - Rra (rare)
    'ఱ': 'rra', 'ఱా': 'rraa', 'ఱి': 'rri', 'ఱీ': 'rree', 'ఱు': 'rru',
    'ఱూ': 'rroo', 'ఱృ': 'rrru', 'ఱౄ': 'rrroo', 'ఱె': 'rre', 'ఱే': 'rrey',
    'ఱై': 'rrhai', 'ఱొ': 'rro', 'ఱో': 'rrow', 'ఱౌ': 'rrau', 'ఱం': 'rram', 'ఱః': 'rrhaha'

}

def text_to_phonemes(text):
    """
    Convert Telugu text to phonemes based on the phoneme_map.

    Parameters:
    text (str): The input text in Telugu.

    Returns:
    list: A list containing phonetic representations of each word.
    """
    result = []
    word = []
    i = 0
    while i < len(text):
        # Check if two characters together form a valid phoneme combination
        if i + 1 < len(text) and text[i:i+2] in phoneme_map:
            phoneme = phoneme_map[text[i:i+2]]
            word.append(phoneme)
            i += 2
        else:
            char = text[i]
            # Map individual characters, skipping characters not in the map
            if char in phoneme_map:
                phoneme = phoneme_map[char]
                word.append(phoneme)
            i += 1
        # Check for word boundary or end of text
        if i == len(text) or text[i] == ' ':
            if word:
                result.append(''.join(word))
                word = []
            if i < len(text) and text[i] == ' ':
                result.append(' ')
                i += 1

    return result

def process_text(text):
    """
    Process input text (single line or paragraph) and convert to phonemes.

    Parameters:
    text (str): The input text in Telugu.

    Returns:
    str: Phonetic representation of the entire text.
    """
    words = text.split(' ')
    phonetic_words = []

    for word in words:
        phonetic_word = text_to_phonemes(word)
        phonetic_words.append(''.join(phonetic_word))

    return ' '.join(phonetic_words)

