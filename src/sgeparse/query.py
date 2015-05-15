from .parser import JobsParser
import subprocess as sp


def get_jobs():
    xml_text = fetch_xml()
    parser = JobsParser(xml_text)
    return parser.jobs


def fetch_xml():
    cmd = ['qstat', '-xml']
    return sp.check_output(cmd)
