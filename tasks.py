from invoke import task 

@task
def start(ctx):
    ctx.run("python src/index.py")

@task
def test(ctx):
    ctx.run("poetry run pytest src")

@task
def coverage_report(ctx):
    ctx.run("poetry run coverage run --branch -m pytest")
    ctx.run("poetry run coverage report -m")
    ctx.run("poetry run coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")
