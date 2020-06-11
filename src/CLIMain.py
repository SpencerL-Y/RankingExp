import sys
import os
import datetime 
import random
import click

from BoogieParser import *
from SVMLearn import *

#from SVMLearnMulti import *

@click.group()
def cli():
    pass


@click.command()
@click.argument("source")
def parseBoogie(source, parseoutfile):
    parseBoogieProgram(source, parseoutfile)

@click.command()
@click.argument("source")
@click.argument('log', default=("./Log_temp"))

def learnMultiRanking(source, log):
    os.system("mkdir " + log)
    sourceFilePath, sourceFileName, templatePath, templateFileName, Info, parse_oldtime, parse_newtime = parseBoogieProgram(source, "OneLoop.py")
    from OneLoop import L
    result, rf_list = SVMLearnMulti(sourceFilePath, sourceFileName, log, parse_oldtime, parse_newtime)
    printSummary(len(rf_list), result, rf_list)
    
@click.command()
@click.argument("source")
@click.argument('log', default=("./Log_temp"))

def learnNestedRanking(source, log):
    os.system("mkdir " + log)
    sourceFilePath, sourceFileName, templatePath, templateFileName, Info, parse_oldtime, parse_newtime = parseBoogieProgram(source, "OneLoop.py")
    from OneLoop import L
    result, rf_list = SVMLearnNested(sourceFilePath, sourceFileName, templatePath, templateFileName, Info, log, parse_oldtime, parse_newtime)
    printSummary(len(rf_list), result, rf_list)

cli.add_command(learnNestedRanking)
cli.add_command(learnMultiRanking)
cli.add_command(parseBoogie)


if __name__ == '__main__':
    print("SVMRanker -- Version 1.0")
    cli()

