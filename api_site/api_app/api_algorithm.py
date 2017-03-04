"""
API Algorithm
1. if meme_cahce Not None And data_set is True 
    1.1. return JSON Ready
    1.2. Meme Cache Populate
2. else if db_cahce Not None And data_set is True
    2.1. return JSON Ready
    2.2. API Populate
    2.3. Meme Cache Populate
3. else API Populate
    3.1. Meme Cache Populate
    3.2. return JSON Ready
"""

"""
API Populate Algorithm
1. if google_doc_link is True read csv_data_set
    1.1. split csv_data_set into title, description, image_url
    1.2. if int( title[1]  ) is True then data_id = join( title[0], title[1] )
    1.3. else data_id = join( title[0], title[1] … title[n]  ), where 2 < n < number_of_ words_in_title/2  < 15
    1.4. if Mobile Image is True, image_mobile_ready = True
    1.5. else image_mobile_ready = False
    1.6. data_set_in = { data_id, title, description, image_url , image_mobile_ready }
2. if db_cahce None, save db_cahce[ “default”, data_set_in[ data_id, title, description, image_url, image_mobile_ready ], ‘version1’ ] 
3. else set db_cahce[ ‘version1’ ] to db_cahce[ ‘version2’ ]
    3.1. save db_cahce[ “default”, data_set_in[ data_id, title, description, image_url ], ‘version1’ ] 
"""