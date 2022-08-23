# entity_matching
A Fuzzy Name Matching utility to match different company names and link them from "sales" to "taxbook".

## sales
A Sales Source data is typically a txt file with tab delimited values.
An example looks like this:
| sales_name                 | gstin           |
|----------------------------|-----------------|
| 10 muffins                 | 33AAOFT0781F1Z4 |
| 2k engineering corporation | 06AAAFZ9208K1ZU |
| 3 an telecom               | 23ANYPT9196P1ZF |

## taxbook
A Taxbook Source data is typically a txt file with tab delimited values.
An example looks like this:

| index | sales_name                | tan        |
|-------|---------------------------|------------|
| 0     | gujarat paraffins pvt ltd | AHMG00111G |
| 1     | sk exports                | KNPS01212B |
| 2     | wilshire health care      | BPLW00334F |

`Sample data can be found under the data folder`

## Running the utility

* Install Python (Latest).
* Run `pip3 install -r requirements.txt`
* After the dependencies are installed, run `python3 src/taxreco/match.py`
* You'll be prompted for the sales and taxbook file locations.
* Finally the output will be exported into a tab delimited text file called matched_output.txt


