#!/usr/bin/env python

import click
import os

@click.group('')
@click.pass_context
def github(ctx):
    """
    \b
    Control Station - Managing GITHUB Account
    """
    pass


@github.command('repo_sync', short_help='Syncing repositories with upstream')
@click.argument('repo_filename', metavar="<repo_filename>", default='/opt/PW/github_repo.yaml', type=click.Path(exists=True))
# @click.option('-s', '--sync', is_flag=True, show_default=False, help='Syncing repositories with upstream')
@click.pass_context
def repo_sync(ctx, repo_filename):
    """
        Syncing repositories with upstream
        
        \b
        <repo_filename> : File containing list of repositories to sync
        Default File : /opt/PW/github_repo.yaml
        \b   
    """
    # Open the file in read mode
    with open(repo_filename, 'r') as file:
        lines = file.readlines()

    # # Print the lines
    for line in lines:
        print(f'gh repo sync {line.strip()}')
        os.system(f'gh repo sync {line.strip()}')

    # Need to prepare directory for sending the files to Remote Host
    # click.echo (f'Deploy Streamlit Core Modules to -> {host} using Port {ssh_port}')
    # os.system(f'rsync -avzhe "ssh -p{ssh_port}"  --delete --exclude  ".*" --exclude "node_modules"  /opt/LLM/streamlit/* root@{host}.synercatalyst.com:/var/lib/streamlit
    # Need to prepare directory for sending the files to Remote Host
    # click.echo (f'Deploy Streamlit Core Modules to -> {host} using Port {ssh_port}')
    # os.system(f'rsync -avzhe "ssh -p{ssh_port}"  --delete --exclude  ".*" --exclude "node_modules"  /opt/LLM/streamlit/* root@{host}.synercatalyst.com:/var/lib/streamlit')
