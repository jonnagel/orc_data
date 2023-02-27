# Warning: ensure you do not cause any issues while collecting data.
# The following code is a demonstration only. DO NOT collect data without permission. 

orc_col_map = { 'schname': 'school_name',
    'schoolid': 'school_id1',
    'schid': 'school_id2',
    'surveyyearkey': 'survey_year_key',
    'surveyyear': 'survey_year',
    'districtid': 'district_id',
    'leaname': 'lea_name',
    'leaid': 'lea_id',
    'schaddress': 'school_address',
    'schcity': 'school_city',
    'schstate': 'school_state',
    'schzip': 'school_zip',
    'maleenrollment': 'male_enrollment',
    'femaleenrollment': 'female_enrollment',
    'totalenrollment': 'total_enrollment',
    'mpercent': 'male_pct',
    'fpercent': 'female_pct',
    'amepercent': 'ame_pct',
    'asipercent': 'asian_pct',
    'hispercent': 'hispanic_pct',
    'blapercent': 'black_pct',
    'whipercent': 'white_pct',
    'hipacpercent': 'hipac_pct',
    'morepercent': 'more_pct',
    'dispercent': 'dis_pct',
    'leppercent': 'lpp_pct',
    'lepenrolledpercent': 'lep_enrolled_pct',
    'fivehundredfourpercent': 'five_hundred_four_pct',
    'focusondisabilities': 'focus_on_disabilities',
    'studentstoteachers': 'students_to_teachers'}

"""
# I had to revert to collecting school IDs by zip
by_zip = 'removed'.format
data_l = []
error_log = []
school_data = []
school_data_df = pd.DataFrame()
# need KS zip codes
KS_zips = pd.read_html('https://www.kansas-demographics.com/zip_codes_by_population')
zips = KS_zips[0]['Zip Code']
zips = zips[zips.str.len().eq(5)]
for x in zips:
    try:
        url = by_zip(x)
        data = requests.get(url).json()
        data_l.append(data)
    except:
        print(x)
for d in data_l:
    school_data_df = pd.concat([school_data_df, json_normalize(d)], ignore_index=True)
school_data_df.to_pickle('data/orc/school_data_by_zip.p')
# get data from website
for s in tqdm(school_data_df.school_id.unique()):
    try:
        data_d = requests.get(f"removed").json()
        school_data.append(json_normalize(data_d))
    except:
        error_log.append(s)
        print(f"{s} failed")
school_data3_df = pd.concat(school_data, ignore_index=True)
school_data3_df.to_pickle('data/orc/kansas_enrollment.p')
"""
