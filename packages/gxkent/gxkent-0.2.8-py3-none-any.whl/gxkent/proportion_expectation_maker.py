"""
            This takes a simple object of objects that setup an expectations about what the percentage proportions of a column with limited numbers of values.. 
            
            It is not clear to me that this is generalizable.. or that this belongs in Kent.. but I do not know where else to put it.

usage: 

ProportionExpectationMaker.addToKent(
                    MyKentObj,
                    proportion_expectations_object, 
                    col_to_aggregate, 
                    col_to_count, 
                    db, table, catalog
                        )




    @staticmethod
    def addToKent(Kent: GXKent, proportion_expectations_object, col_to_aggregate, col_to_count, db, table, catalog = '' ):


"""
from gxkent import GXKent
from sqlalchemy import text

class ProportionExpectationMaker:

    @staticmethod
    def flat_print_dict(d, indent=0):
        # TODO someday.. convert this to something that returns text instead of just printing it..
        # Calculate the maximum length of the main dictionary keys
        max_key_length = max(len(repr(key)) for key in d.keys())
        
        # Find the maximum length of the sub-dictionary keys
        all_sub_keys = {sub_key for value in d.values() if isinstance(value, dict) for sub_key in value.keys()}
        max_sub_key_length = max(len(repr(sub_key)) for sub_key in all_sub_keys)
        
        # Iterate over the main dictionary items
        for i, (key, value) in enumerate(d.items()):
            # Calculate the padding needed for alignment
            padding = ' ' * (max_key_length - len(repr(key)))
            # Print the key and the start of the sub-dictionary
            print('  ' * indent + repr(key) + ':' + padding, end='\t{ ')
            if isinstance(value, dict):
                # Prepare the sub-dictionary items with proper alignment
                sub_items = []
                for sub_key, sub_value in value.items():
                    sub_padding = ' ' * (max_sub_key_length - len(repr(sub_key)))
                    sub_items.append(f"'{sub_key}':{sub_padding} {sub_value}")
                # Join and print the sub-items, followed by closing brace and a comma
                print(",\t\t ".join(sub_items), end=' }')
            else:
                # For non-dictionary values, print them directly
                print(repr(value), end='')
            # Add a comma at the end of each main dictionary item, except the last one
            if i < len(d) - 1:
                print(',')
            else:
                print()


    @staticmethod
    def generatePropObj(connection,percent_threshold,col_to_aggregate, col_to_count, db, table, catalog = ''):

        this_sql = ProportionExpectationMaker.generateSQL(col_to_aggregate, col_to_count, db, table, catalog)
        return_me_obj = {}

        result = connection.execute(text(this_sql))

        round_to = 3

        for row in result.mappings():

            percent_of_total = round(float(row['percent_of_total']),round_to)

            if(percent_of_total > percent_threshold):
                #Use the original percentage as the starting point for all of the values..
                this_row_obj = {
                    'min': percent_of_total,
                    'max': percent_of_total,
                    'original_value': percent_of_total,
                }

                return_me_obj[row['agg_on_this']] = this_row_obj

        return(return_me_obj)

    @staticmethod
    def generateSQL(col_to_aggregate, col_to_count, db, table, catalog = ''):
        """
        This helper function will return the SQL you need to show the relative proportions of common categories/groups/values
        In a dataset..so that you can know how to generate the right code
        """
        if len(catalog) == 0:
            #then thhere is no catalog
            this_db_table = f"{db}.{table}"
        else:
            this_db_table = f"{catalog}.{db}.{table}"

        analysis_sql = f"""
SELECT
    `{col_to_aggregate}` AS agg_on_this,
    `{col_to_aggregate}`, 
    ROUND((COUNT(DISTINCT({col_to_count})) / {col_to_count}_total) * 100,4) AS percent_of_total
FROM {this_db_table}
JOIN (
        SELECT COUNT(DISTINCT({col_to_count})) AS {col_to_count}_total
        FROM {this_db_table}
    ) AS {col_to_count}_total_table  
GROUP BY `{col_to_aggregate}`
ORDER BY percent_of_total DESC
        """

        return(analysis_sql)

    @staticmethod
    def addToKent(Kent: GXKent, proportion_expectations_object, col_to_aggregate, col_to_count, db, table, catalog = '' ):
        """   
            This takes a simple object of objects that setup an expectations about what the percentage proportions of a column with limited numbers of values.. 
            So you pass in something that looks like this: 

            proportion_expectations_object = {
                'This common value': {
                            'min': 4,
                            'max': 5.5,
                            'original_value': 4.7
                },
                'This other value': {
                            'min': 32,
                            'max': 36.5.5,
                            'original_value': 35.1
                },              
                etc..
            }

            and this will add new expectations to Kent that will say.. 
            "We are expecting this 'This common value' to be between 4 percent and 5.5 percent"

            Because this returns distinct expectations there is no need for the total to add up to 100% or even nearly to 100%

        """


        for this_row_value, this_expected_obj in proportion_expectations_object.items():

            expected_min = this_expected_obj['min']
            expected_max = this_expected_obj['max']
            this_expected_percent = this_expected_obj['original_value']

            if len(catalog) == 0:
                #then thhere is no catalog
                this_db_table = f"{db}.{table}"
            else:
                this_db_table = f"{catalog}.{db}.{table}"

            analysis_sql = f"""
SELECT `{col_to_aggregate}`, ROUND((COUNT(DISTINCT({col_to_count})) / {col_to_count}_total) * 100,4) AS percent_of_total
FROM {this_db_table}
JOIN (
        SELECT COUNT(DISTINCT({col_to_count})) AS {col_to_count}_total
        FROM {this_db_table}
    ) AS {col_to_count}_total_table 
WHERE {col_to_aggregate} = '{this_row_value}'  
GROUP BY `{col_to_aggregate}`
        """

            this_gxDF = Kent.gx_df_from_sql(analysis_sql)


            Kent.capture_expectation(
                expectation_name=f"{col_to_aggregate} {this_row_value} is roughly {this_expected_percent} above {expected_min} and below {expected_max}",
                expectation_result=this_gxDF.expect_column_values_to_be_between(
                        column='percent_of_total', 
                        min_value=expected_min,
                        max_value=expected_max
                        )
            )

