import logging

import azure.functions as func


def main(req: func.HttpRequest,outputblob:func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info(req.route_params)

    outputtext = "追加コメントですaa"
    outputblob.set(outputtext)

    return func.HttpResponse(f"{outputtext}")
