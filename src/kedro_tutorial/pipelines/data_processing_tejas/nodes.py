"""
This is a boilerplate pipeline 'data_processing_tejas'
generated using Kedro 0.18.3
"""
import pandas as pd

def _is_true(x: pd.Series)->pd.Series:
    return x=="t"

def _parse_percentage(x:pd.Series)->pd.Series:
    x = x.str.replace("%","")
    x = x.astype(float) / 100
    return x

def _parse_money(x:pd.Series)->pd.Series:
    x = x.str.replace("$","").str.replace(",","")
    x = x.astype(float)
    return x

def preprocess_companies(companies: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the data for the companies
    Args:
        Companies: raw data.
    Returns:
        Preprocessed data, with `company rating` converted to a float and `iata_approved`
        converted to boolean
    """
    companies['iata_approved'] = _is_true(companies['iata_approved'])
    companies['company_rating'] = _parse_percentage(companies['company_rating'])
    return companies

def preprocess_shuttles(shuttles:pd.DataFrame)->pd.DataFrame:
    """

    :param companies: raw data frame
    :return: companies dataframe where the cost of shuttle in converted into float and `d_check_complete`,
        `moon_clearance_complete` converted to boolean.
    """
    shuttles['d_check_complete'] = _is_true(shuttles['d_check_complete'])
    shuttles['moon_clearance_complete'] = _is_true(shuttles['moon_clearance_complete'])
    shuttles['price'] = _parse_money(shuttles['price'])
    return shuttles

def create_model_input_table(shuttles:pd.DataFrame, companies:pd.DataFrame, reviews:pd.DataFrame)->pd.DataFrame:
    """

    :param shuttles: Processed data for shuttles
    :param companies: Processed data for companies
    :param reviews: Processed data for reviews
    :return:
    model input table
    """

    rated_shuttles = shuttles.merge(reviews,left_on="id",right_on="shuttle_id")
    model_input_table = rated_shuttles.merge(companies,left_on="company_id",right_on="id")
    model_input_table = model_input_table.dropna()
    return model_input_table