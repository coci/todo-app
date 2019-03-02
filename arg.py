import click

@click.command()
@click.option('--edit')
@click.option('--id')
def iran(id):
	print(id)
if __name__ = '__main__':
	iran()	