import os, requests, codecs


def biomodels_download(model_id, fname=None):
    """
    Download a sbml model from biomodels
    Args:
        model_id: A biomodels identifier
        sbml_filename: An optional filename to save sbml model to

    Returns:

    """
    if fname is None:
        fname = os.path.join(os.path.dirname(__file__), '{}.sbml'.find(model_id))
    base_url = "https://www.ebi.ac.uk/biomodels-main/download?mid"
    model_url = f'{base_url}={model_id}'
    # get the model directly from url
    sbml = requests.get(model_url).content.decode('utf-8')
    with codecs.open(fname, 'w', 'utf-8') as f:
        f.write(sbml)
    return sbml
