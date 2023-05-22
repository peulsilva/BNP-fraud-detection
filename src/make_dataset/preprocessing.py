import pandas  as pd

class Preprocessing:
    def __init__(self) -> None:
        pass

    @staticmethod
    def remove_outliers(
        series: pd.Series,
        low_quantile : float = 0.1,
        high_quantile : float = 0.9 
    ) -> pd.Series:
        """Remove values out of (low_quantile, high_quantile)

        Args:
            series (pd.Series): _description_
            low_quantile (float, optional): _description_. Defaults to 0.1.
            high_quantile (float, optional): _description_. Defaults to 0.9.

        Returns:
            _type_: _description_
        """        
        low_quantile_value = series\
            .quantile(low_quantile)
        high_quantile_value = series\
            .quantile(high_quantile)
        
        return series[(series > low_quantile_value) & (series < high_quantile_value) ]
    
    @staticmethod 
    def get_columns_with(
        df: pd.DataFrame,
        key : str,
        method : str = "contains"
    ) -> pd.DataFrame:
        """Returns columns of a dataframe containing a certain key

        Args:
            df (pd.DataFrame): _description_
            key (str): _description_

        Returns:
            _type_: _description_
        """        
        possible_methods = [
            "contains",
            "endswith",
            "startswith"
        ]

        if (method not in possible_methods):
            raise ValueError(f"method must be one of {possible_methods}")
        
        if (method == "contains"):
            mask = df\
                .columns\
                .str\
                .contains(key)
        elif method == "endswith":
            mask = df\
                .columns\
                .str\
                .endswith(key)
            
        else:
            mask = df\
                .columns\
                .str\
                .startswith(key)

        return df[df.columns[mask]]
