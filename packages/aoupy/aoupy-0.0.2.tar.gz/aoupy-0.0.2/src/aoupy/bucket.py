import os
import polars as pl
from polars import DataFrame

def copy_from_bucket(file_path: str, bucket_id: str = None) -> None:
    """
    Copies a file from specified bucket and path into the enviroment workspace.
    
    Parameters:
    -----------
    file_path: str
        Path to the file to copy from bucket
    bucket_id:[Optional]
        The bucket id to copy the file from. Defaults to the environment variable 'WORKSPACE_BUCKET'.
    
    Returns:
    -------
    None returned. File from bucket is copied to the work environment.

    Example:
    --------
    copy_from_bucket('datasets/fitbit.csv')
    """
    
    if bucket_id == None:
        bucket_id = os.getenv('WORKSPACE_BUCKET')

    os.system(f"gsutil cp '{bucket_id}/{file_path}' .")
    print(f'[INFO] {file_path} is successfully downloaded into your working space')
        
def read_from_bucket(file_path: str, bucket_id: str = None, lazy: bool = True) -> DataFrame:
    """Copies and reads a csv file from bucket
    
    Parameters:
    -----------
    file_path: str
        Path to the csv file to read from bucket
    bucket_id: [Optional] str
        The bucket id to read the file from. Defaults to environment variable WORKSPACE_BUCKET.
    lazy: [Optional] bool
        Either to read or scan csv file. Check polars documentation for this behaviour. Defaults to True.
    
    Returns:
    -------
    Polars Dataframe is returned. Read might be set to lazy to scan the csv instead of reading. Check polars documentation for this behaviour.

    Example:
    --------
    df = read_from_bucket('datasets/fitbit.csv')
    """
    
    if file_path.split(".")[-1] != "csv":
            raise ValueError("The specified file is not csv format hence cannot be loaded")
    
    if bucket_id == None:
        bucket_id = os.getenv('WORKSPACE_BUCKET')

    os.system(f"gsutil cp '{bucket_id}/{file_path}' 'bucket_io/{file_path}'")
    print(f'[INFO] {file_path} is successfully downloaded into bucket_io folder')
    
    if lazy:
        return pl.scan_csv(f'bucket_io/{file_path}')
    else:
        return pl.read_csv(f'bucket_io/{file_path}')

def copy_to_bucket(file_name: str, target: str, bucket_id: str = None) -> None:
    """Copies a file from enviroment workspace to designated bucket folder
    
    Parameters:
    -----------
    file_name: str
        Path to file in the environment to copy to bucket
    target: str
        Path to copy the file
    bucket_id:[Optional]
        The bucket id to copy the file to. Defaults to environment variable WORKSPACE_BUCKET.
    
    Returns:
    -------
    None returned. File from the environment is copied to the given location.

    Example:
    --------
    copy_from_bucket('fitbit.csv', 'datasets/fitbit.csv')
    """
    
    if bucket_id == None:
       bucket_id = os.getenv('WORKSPACE_BUCKET')
        
    os.system(f"gsutil cp {file_name} {bucket_id}/{target}")

def ls_bucket(target: str = None, bucket_id: str = None) -> None:
    """List the files in the given directory in the given bucket
    
    Parameters:
    -----------
    target: str [Optional]
        Path to folder in the bucket to list the files. Defaults to workspace folder.
    bucket_id:[Optional]
        The bucket id to list the files from. Defaults to environment variable WORKSPACE_BUCKET.
    
    Returns:
    -------
    None returned. Files from the given directory is listed.

    Example:
    --------
    ls_bucket('datasets')
    """
    
    if bucket_id == None:
       bucket_id = os.getenv('WORKSPACE_BUCKET')
    
    if target == None:
        os.system(f"gsutil ls {bucket_id}")
    else:
        os.system(f"gsutil ls {bucket_id}/{target}")

def remove_from_bucket(file_path: str, bucket_id:str = None) -> None:
    """Removes the file from the bucket

    Parameters:
    -----------
    file_path: str
        Path to file to remove.
    bucket_id:[Optional]
        The bucket id to remove the file from. Defaults to environment variable WORKSPACE_BUCKET.
    
    Returns:
    -------
    None returned. File from bucket is removed.

    Example:
    --------
    remove_from_bucket('datasets/fitbit.csv')
    """
    
    if bucket_id == None:
       bucket_id = os.getenv('WORKSPACE_BUCKET')
    os.system(f"gsutil rm {bucket_id}/{file_path}")

def write_to_bucket(file: DataFrame, target: str, bucket_id: str =  None) -> None:
    """Writes the given file to the given bucket location
    
    Parameters:
    -----------
    file: DataFrama
        Polars DataFrame to write to the bucket
    target: str
        Path to write the file
    bucket_id:[Optional]
        The bucket id to write the file. Defaults to environment variable WORKSPACE_BUCKET.
    
    Returns:
    -------
    None returned. DataFrame is written to the given bucket.

    Example:
    --------
    write_from_bucket(fitbit_dat, 'datasets/fitbit.csv')
    """
    
    file.write_csv(f'bucket_io/temp.csv')
    copy_to_bucket(file_name = 'bucket_io/temp.csv', target=target, bucket_id=bucket_id)