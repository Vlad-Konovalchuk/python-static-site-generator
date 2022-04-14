from typer import Typer
from ssg.site import Site


def main(source='content', dest='dist'):
    config = {'source': source, 'dest': dest}
    site = Site(**config).build()


Typer.run(main)
