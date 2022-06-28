# type: ignore
# this file can't use mypy annonations, because "invoke" doesn't support them :(
# https://github.com/pyinvoke/invoke/issues/357


from invoke import task


@task
def deploy(c):
    """
    Deploy API server to elasticbeanstalk environment
    """
    c.run("echo 'Starting deploy...'", pty=True)
    c.run("date", pty=True)
    c.run("eb deploy", pty=True)
    c.run("echo 'Finished deploy...'", pty=True)
    c.run("date", pty=True)

@task
def build(c):
    """
    Build the API container
    """
    c.run(
        f"docker-compose build",
        pty=True,
    )

@task
def start(c):
    """
    Start the API container
    """
    c.run(f"docker-compose up", pty=True)


