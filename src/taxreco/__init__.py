import pandas as pd
from name_matching.name_matcher import NameMatcher

adjusted_names = pd.read_csv('test/adjusted_test_names.csv')
test_names = pd.read_csv('test/test_names.csv')

matcher = NameMatcher(  ngrams=(2, 5),
                        top_n=10,
                        number_of_rows=500,
                        number_of_matches=3,
                        lowercase=True,
                        punctuations=True,
                        remove_ascii=True,
                        legal_suffixes=False,
                        common_words=False,
                        preprocess_split=False,
                        verbose=True)


matcher.set_distance_metrics(['iterative_sub_string', 'pearson_ii', 'bag', 'fuzzy_wuzzy_partial_string', 'editex'])

matcher.load_and_process_master_data('company_name', test_names, transform=True)

matches = matcher.match_names(to_be_matched=adjusted_names, column_matching='company_name')

complete_matched_data = pd.merge(pd.merge(test_names, matches, how='left', right_index=True, left_index=True), adjusted_names, how='left', left_on='match_index_0', right_index=True, suffixes=['', '_matched'])

m = matches.loc[:, ['original_name', 'match_name_0', 'score_0', 'match_index_0']]

print(m.to_string())



