from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.db import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.Prompt import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.FB.FormBuilder import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.FB.FBMTXT import *
import pandas as pd
import csv
from datetime import datetime,date,time,timedelta
from pathlib import Path
from colored import Fore,Style,Back
from barcode import Code39,UPCA,EAN8,EAN13
import barcode,qrcode,os,sys,argparse
from datetime import datetime,timedelta
import zipfile,tarfile
import base64,json
from ast import literal_eval
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base as dbase
from sqlalchemy.ext.automap import automap_base
from pathlib import Path
import upcean

class Exercise(BASE,Template):
    __tablename__="Exercise"
    exid=Column(Integer,primary_key=True)
    Name=Column(String)
    Note=Column(String)
    Reps=Column(Integer) # 8 reps of 30 repcounts NAME
    RepCount=Column(Integer) #30 times rep
    CurrentRep=Column(Integer)
    cdt=Column(DateTime) #CurrentDateTime
    ldt=Column(DateTime) #LastDateTime

    def __init__(self,**kwargs):
        kwargs['__tablename__']=self.__tablename__
        self.init(**kwargs,)

class Routine(BASE,Template):
    __tablename__="Routine"
    roid=Column(Integer,primary_key=True)
    Name=Column(String)
    Note=Column(String)
    exid=Column(Integer)
    precedence=Column(Integer)
    doe=Column(Date)
    toe=Column(Time)
    dtoe=Column(DateTime)

    sdt=Column(DateTime) #StartDateTime
    edt=Column(DateTime) #EndDateTime

Exercise.metadata.create_all(ENGINE)
Routine.metadata.create_all(ENGINE)

'''
            #for use with header
            fieldname='ALL_INFO'
            mode='LU'
            h=f'{Prompt.header.format(Fore=Fore,mode=mode,fieldname=fieldname,Style=Style)}'
'''
#header='{Fore.grey_70}[{Fore.light_steel_blue}{mode}{Fore.medium_violet_red}@{Fore.light_green}{fieldname}{Fore.grey_70}]{Style.reset}{Fore.light_yellow} '
e_data={'Name':{
            'type':'str',
            'default':'',
            },
        'Note':{
            'type':'str',
            'default':'',
            },
        'Reps':{
           'type':'int',
           'default':8,
            },
        'RepCount':{
            'type':'int',
            'default':30,
            },
        'CurrentRep':{
            'type':'int',
            'default':'0',
            },
      }    


class ExerciseTracker:
    def newExercise(self):
        while True:
            try:
                newE=FormBuilder(data=e_data)
                if newE in [None,]:
                    return
                newEx=Exercise(**newE)

                with Session(ENGINE) as session:
                    check=session.query(Exercise)
                    for f in newE.keys():
                        check=check.filter(getattr(Exercise,f)==getattr(newEx,f))
                    results=check.all()
                    ct=len(results)
                    if ct > 0:
                        print(f"There is already an exercise with that data! {check}")
                    else:
                        session.add(newEx)
                        session.commit()
                        session.flush()
                        session.refresh(newEx)
                        print(newEx)

            except Exception as e:
                print(e)

    def searchExercise(self,returnable=False,oneShot=False):
        while True:
            try:
                search=Prompt.__init2__(None,func=FormBuilderMkText,ptext="Search? ",helpText="What are you looking for in Name/Note/exid?",data="string")
                if search in [None,]:
                    return
                exid=None
                try:
                    exid=int(search)
                except Exception as e:
                    print(e,"exid will be None")
                    exid=None
                with Session(ENGINE) as session:
                    if search == 'd':
                        query=session.query(Exercise)
                    else:
                        query=session.query(Exercise).filter(or_(Exercise.Name.icontains(search),Exercise.Note.icontains(search),Exercise.exid==exid))
                    results=query.all()
                    ct=len(results)
                    if ct == 0:
                        print("no results")
                    if returnable:
                        return results
                    for num,i in enumerate(results):
                        msg=f'''{Fore.light_green}{num+1}/{Fore.light_yellow}{ct} -> {i}'''
                        print(msg)
                if oneShot:
                    break
            except Exception as e:
                print(e)

    def rmExercise(self):
        results=self.searchExercise(returnable=True,oneShot=True)
        ct=len(results)
        if ct == 0:
            print("nothing to delete")
        for num,i in enumerate(results):
            msg=f'''{Fore.light_magenta}{num}/{Fore.light_yellow}{ct} -> {i}'''
            print(msg)
        which=Prompt.__init2__(self,func=FormBuilderMkText,ptext="Which result[s(,) do you wish to delete?",helpText="comma separated list of indexes",data="list")
        if which in [None,'d']:
            print("nothing was selected!")
            return
        else:
            deleted=0
            with Session(ENGINE) as session:
                for i in which:
                    try:
                        exindex=int(i)
                        if exindex >= 0 and exindex <= ct:
                            session.query(Exercise).filter(Exercise.exid==results[exindex].exid).delete()
                            session.commit()
                            deleted+=1
                    except Exception as e:
                        print(e)
            print(f"deleted {deleted} exercises!")
             
    def editExercise(self):
        results=self.searchExercise(returnable=True,oneShot=True)
        ct=len(results)
        if ct == 0:
            print("nothing to edit")
        for num,i in enumerate(results):
            msg=f'''{Fore.light_magenta}{num}/{Fore.light_yellow}{ct} -> {i}'''
            print(msg)
        which=Prompt.__init2__(self,func=FormBuilderMkText,ptext="Which result[s(,) do you wish to edit?",helpText="comma separated list of indexes",data="list")
        if which in [None,'d']:
            print("nothing was selected!")
            return
        else:
            edited=0
            with Session(ENGINE) as session:
                for i in which:
                    try:
                        exindex=int(i)
                        if exindex >= 0 and exindex <= ct:
                            exercise=session.query(Exercise).filter(Exercise.exid==results[exindex].exid)
                            print(f"{Fore.light_green}OLD{Style.reset} -> {exercise}")
                            data_l={}
                            for k in exercise.__table__.columns:
                                if k.name not in ['exid',]:
                                    data_l[k.name]={
                                    'default':getattr(exercise,k.name),
                                    'type':str(k.type)
                                    }
                            edited=FormBuilder(data=data_l)
                            if edited in [None,]:
                                continue
                            for k in edited:
                                setattr(exercise,k,edited[k])
                            session.commit()
                            session.flush()
                            session.refresh(exercise)
                            print(f"{Fore.light_magenta}EDITED{Style.reset} -> {exercise}")
                            edited+=1
                    except Exception as e:
                        print(e)
            print(f"edited {edited} exercises!")
    def newRoutine(self):
        with Session(ENGINE) as session:
            data_r={
            'Name':{
                'default':'',
                'type':'string',
                },
            'Note':{
                'default':'',
                'type':'string',
                },
            }
            routine=FormBuilder(data=data_r)
            while True:
                exercises=self.searchExercise(returnable=True,oneShot=True)
                if exercises in [None,]:
                    break
                precedence=None
                def gethpv():
                    with Session(ENGINE) as session:
                        hpv=session.query(Routine).filter(Routine.Name==routine.get("Name")).order_by(Routine.precedence.desc()).first()
                        if hpv:
                            return hpv.precedence
                precedence=gethpv()
                for num,i in enumerate(exercises):
                    print(i)
                    use=Prompt.__init2__(None,func=FormBuilderMkText,ptext="Use?",helpText="yes or no?",data="boolean")
                    if use in [None,]:
                        break
                    elif use in [True,]:
                        dtoe=datetime.now()
                        doe=date(dtoe.year,dtoe.month,dtoe.day)
                        toe=time(dtoe.hour,dtoe.minute,dtoe.second)
                        nt=None
                        if precedence:
                            nt=precedence+1
                        else:
                            nt=0
                        rts=Routine(Name=routine.get("Name"),Note=routine.get("Note"),exid=i.exid,precedence=nt,doe=doe,dtoe=dtoe,toe=toe)
                        session.add(rts)
                        session.commit()
                        precedence=gethpv()
                    else:
                        pass
                #set the order



    def __init__(self):
        fieldname='Menu'
        mode='ExerciseTracker'
        h=f'{Prompt.header.format(Fore=Fore,mode=mode,fieldname=fieldname,Style=Style)}'
        header='{Fore.grey_70}[{Fore.light_steel_blue}{mode}{Fore.medium_violet_red}@{Fore.light_green}{fieldname}{Fore.grey_70}]{Style.reset}{Fore.light_yellow} '

        helpText=f'''
        ne,NewExercise - create a new exercise
        re,RemoveExercise - delete an exercise
        se,SearchExercise - search for an exercise from it's Note,Name, or ID
        ee,EditExercise - edit an exercise
        '''
        while True:
            doWhat=Prompt.__init2__(None,func=FormBuilderMkText,ptext=f"{h} Do what?",helpText=helpText,data="string")
            if doWhat in [None,]:
                return
            elif doWhat in ['d',]:
                print(helpText)
                continue
            elif doWhat.lower() in ['NewExercise','ne']:
                self.newExercise()
            elif doWhat.lower() in ['RemoveExercise','re']:
                self.rmExercise()
            elif doWhat.lower() in ['se','SearchExercise']:
                self.searchExercise()
            elif doWhat.lower() in ['ee','EditExercise']:
                self.editExercise()
            elif doWhat.lower() in ['nr','newRoutine']:
                self.newRoutine()