from .parser import JobsParser


def get_jobs():
    xml_text = fetch_xml()
    parser = JobsParser(xml_text)
    return parser.jobs


def fetch_xml():
    pass
