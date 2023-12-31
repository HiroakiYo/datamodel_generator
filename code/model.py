# generated by datamodel-codegen:
#   filename:  schema_mod.json
#   timestamp: 2023-10-09T17:35:33+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Extra, Field
from typing_extensions import Annotated


class PastWeek(BaseModel):
    class Config:
        extra = Extra.forbid

    Past_Week: Annotated[
        Optional[Dict[str, Any]], Field(alias='Past Week', title='Past Week')
    ] = None


class PastMonth(BaseModel):
    class Config:
        extra = Extra.forbid

    Past_Month: Annotated[
        Optional[Dict[str, Any]], Field(alias='Past Month', title='Past Month')
    ] = None


class Now(BaseModel):
    class Config:
        extra = Extra.forbid

    Now_Schema: Annotated[Optional[Dict[str, Any]], Field(alias="Now", title='Now')] = None


class PastThreeDays(BaseModel):
    class Config:
        extra = Extra.forbid

    Past_Three_Days: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Past Three Days', title='Past Three Days'),
    ] = None


class IPhone(BaseModel):
    class Config:
        extra = Extra.forbid

    iPhone_Schema: Annotated[Optional[Dict[str, Any]], Field(alias="iPhone", title='iPhone')] = None


class Android(BaseModel):
    class Config:
        extra = Extra.forbid

    Android_Schema: Annotated[Optional[Dict[str, Any]], Field(alias="Android", title='Android')] = None


class Sleep(BaseModel):
    class Config:
        extra = Extra.forbid

    Sleep_Schema: Annotated[Optional[Dict[str, Any]], Field(alias="Sleep", title='Sleep')] = None


class Activity(BaseModel):
    class Config:
        extra = Extra.forbid

    Activity_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Activity',title='Activity')] = None


class Suicide(BaseModel):
    class Config:
        extra = Extra.forbid

    Suicide_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Suicide', title='Suicide')] = None


class Emotion(BaseModel):
    class Config:
        extra = Extra.forbid

    Emotion_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='emotion', title='Emotion')] = None


class Anhedonia(BaseModel):
    class Config:
        extra = Extra.forbid

    Anhedonia_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Anhedonia',title='Anhedonia')
    ] = None


class Social(BaseModel):
    class Config:
        extra = Extra.forbid

    Social_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Social',title='Social')] = None


class EMA(BaseModel):
    class Config:
        extra = Extra.forbid

    Configuration_File: Annotated[
        Optional[bool], Field(alias='Configuration File', title='Configuration File')
    ] = True
    Question_Window: Annotated[
        Optional[Union[PastWeek, PastMonth, Now, PastThreeDays]],
        Field(alias='Question Window', title='Question Window'),
    ] = None
    Device_Schema: Annotated[
        Optional[Union[IPhone, Android]], Field(alias='Device', title='Device')
    ] = None
    Category_Schema: Annotated[
        Optional[List[Union[Sleep, Activity, Suicide, Emotion, Anhedonia, Social]]],
        Field(alias='Category', title='Category'),
    ] = None


class EcologicalMomentaryAssessment(BaseModel):
    EMA_Schema: Annotated[Optional[EMA], Field(alias='EMA',title='EMA')] = None


class HelsinkiAlto(BaseModel):
    class Config:
        extra = Extra.forbid

    Helsinki_Alto_Schema: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Helsinki-Alto', title='Helsinki-Alto'),
    ] = None


class Vanderbilt(BaseModel):
    class Config:
        extra = Extra.forbid

    Vanderbilt_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Vanderbilt',title='Vanderbilt')
    ] = None


class VUMC(BaseModel):
    class Config:
        extra = Extra.forbid

    VUMC_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='VUMC',title='VUMC')] = None


class UCLA(BaseModel):
    class Config:
        extra = Extra.forbid

    UCLA_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='UCLA', title='UCLA')] = None


class McLean(BaseModel):
    class Config:
        extra = Extra.forbid

    McLean_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='McLean', title='McLean')] = None


class Cornell(BaseModel):
    class Config:
        extra = Extra.forbid

    Cornell_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Cornell', title='Cornell')] = None


class UCSD(BaseModel):
    class Config:
        extra = Extra.forbid

    UCSD_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='UCSD', title='UCSD')] = None


class Stanford(BaseModel):
    class Config:
        extra = Extra.forbid

    Stanford_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Stanford', title='Stanford')] = None


class MSSMMayberg(BaseModel):
    class Config:
        extra = Extra.forbid

    MSSM_Mayberg_Schema: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='MSSM-Mayberg', title='MSSM-Mayberg'),
    ] = None


class MSSMMurrough(BaseModel):
    class Config:
        extra = Extra.forbid

    MSSM_Murrough_Schema: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='MSSM-Murrough', title='MSSM-Murrough'),
    ] = None


class Princeton(BaseModel):
    class Config:
        extra = Extra.forbid

    Princeton_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Princeton', title='Princeton')
    ] = None


class Pittsburgh(BaseModel):
    class Config:
        extra = Extra.forbid

    Pittsburgh_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Pittsburgh',title='Pittsburgh')
    ] = None


class Collection(BaseModel):
    class Config:
        extra = Extra.forbid

    Study_Name: Annotated[
        Optional[str], Field(alias='Study Name', title='Study Name')
    ] = None
    Collection_Site: Annotated[
        Optional[str], Field(alias='Collection Site', title='Collection Site')
    ] = None
    Study_Site: Annotated[
        Optional[
            Union[
                HelsinkiAlto,
                Vanderbilt,
                VUMC,
                UCLA,
                McLean,
                Cornell,
                UCSD,
                Stanford,
                MSSMMayberg,
                MSSMMurrough,
                Princeton,
                Pittsburgh,
            ]
        ],
        Field(alias='Study Site', title='Study Site'),
    ] = None


class Digital(BaseModel):
    class Config:
        extra = Extra.forbid

    Digital_: Annotated[
        Optional[Dict[str, Any]], Field(alias='Digital', title='Digital ')
    ] = None


class Psychometrics(BaseModel):
    class Config:
        extra = Extra.forbid

    Psychometrics_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Psychometrics', title='Psychometrics')
    ] = None


class SyntheticEEG(BaseModel):
    class Config:
        extra = Extra.forbid

    Synthetic_EEG: Annotated[
        Optional[Dict[str, Any]], Field(alias='Synthetic EEG', title='Synthetic EEG')
    ] = None


class NeuropsychologicalAssessments(BaseModel):
    class Config:
        extra = Extra.forbid

    Neuropsychological_Assessments: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='Neuropsychological Assessments',
            title='Neuropsychological Assessments',
        ),
    ] = None


class Genetics(BaseModel):
    class Config:
        extra = Extra.forbid

    Genetics_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Genetics',title='Genetics')] = None


class EMRClinicalData(BaseModel):
    class Config:
        extra = Extra.forbid

    EMR_Clinical_Data: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='EMR Clinical Data', title='EMR Clinical Data'),
    ] = None


class BehavioralAssessments(BaseModel):
    class Config:
        extra = Extra.forbid

    Behavioral__Assessments: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Behavioral  Assessments', title='Behavioral  Assessments'),
    ] = None


class EcologicalMomentaryAssessments(BaseModel):
    class Config:
        extra = Extra.forbid

    Ecological_Momentary_Assessments: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='Ecological Momentary Assessments',
            title='Ecological Momentary Assessments',
        ),
    ] = None


class NeurocognitiveTaskPerformance(BaseModel):
    class Config:
        extra = Extra.forbid

    Neurocognitive_Task_Performance: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='Neurocognitive Task Performance',
            title='Neurocognitive Task Performance',
        ),
    ] = None


class AffectInterview(BaseModel):
    class Config:
        extra = Extra.forbid

    Affect_Interview: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Affect Interview', title='Affect Interview'),
    ] = None


class MRI(BaseModel):
    class Config:
        extra = Extra.forbid

    MRI_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='MRI',title='MRI')] = None


class EEG(BaseModel):
    class Config:
        extra = Extra.forbid

    EEG_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='EEG',title='EEG')] = None


class LiquidMarkers(BaseModel):
    class Config:
        extra = Extra.forbid

    Liquid_Markers: Annotated[
        Optional[Dict[str, Any]], Field(alias='Liquid Markers', title='Liquid Markers')
    ] = None


class CategoryOfData(BaseModel):
    class Config:
        extra = Extra.forbid

    Modality_Schema: Annotated[
        Optional[
            Union[
                Digital,
                Psychometrics,
                SyntheticEEG,
                NeuropsychologicalAssessments,
                Genetics,
                EMRClinicalData,
                BehavioralAssessments,
                EcologicalMomentaryAssessments,
                NeurocognitiveTaskPerformance,
                AffectInterview,
                MRI,
                EEG,
                LiquidMarkers,
            ]
        ],
        Field(alias='Modality',title='Modality'),
    ] = None


class InputDataCollection(BaseModel):
    Collection_: Annotated[
        Optional[Collection], Field(alias='Collection', title='Collection ')
    ] = None
    Category_of_Data: Annotated[
        Optional[CategoryOfData],
        Field(alias='Category of Data', title='Category of Data'),
    ] = None


class UniversityOfTennesseeKnoxville(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_Tennessee_Knoxville: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='University of Tennessee Knoxville',
            title='University of Tennessee Knoxville',
        ),
    ] = None


class StanfordUniversity(BaseModel):
    class Config:
        extra = Extra.forbid

    Stanford_University: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Stanford University', title='Stanford University'),
    ] = None


class UniversityOfPittsburgh(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_Pittsburgh: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='University of Pittsburgh', title='University of Pittsburgh'),
    ] = None


class HarvardMedicalSchool(BaseModel):
    class Config:
        extra = Extra.forbid

    Harvard_Medical_School: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Harvard Medical School', title='Harvard Medical School'),
    ] = None


class BrighamAndWomenSHospital(BaseModel):
    class Config:
        extra = Extra.forbid

    Brigham_and_Women_s_Hospital: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias="Brigham and Women's Hospital", title="Brigham and Women's Hospital"
        ),
    ] = None


class WeillCornellMedicine(BaseModel):
    class Config:
        extra = Extra.forbid

    Weill_Cornell_Medicine: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Weill Cornell Medicine', title='Weill Cornell Medicine'),
    ] = None


class UniversityOfOxford(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_Oxford: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='University of Oxford', title='University of Oxford'),
    ] = None


class VanderbiltUniversity(BaseModel):
    class Config:
        extra = Extra.forbid

    Vanderbilt_University: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Vanderbilt University', title='Vanderbilt University'),
    ] = None


class VanderbiltUniversityMedicalCenter(BaseModel):
    class Config:
        extra = Extra.forbid

    Vanderbilt_University_Medical_Center: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='Vanderbilt University Medical Center',
            title='Vanderbilt University Medical Center',
        ),
    ] = None


class McleanHospital(BaseModel):
    class Config:
        extra = Extra.forbid

    Mclean_Hospital: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Mclean Hospital', title='Mclean Hospital'),
    ] = None


class UniversityOfCaliforniaLosAngeles(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_California_Los_Angeles: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='University of California Los Angeles',
            title='University of California Los Angeles',
        ),
    ] = None


class PrincetonUniversity(BaseModel):
    class Config:
        extra = Extra.forbid

    Princeton_University: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Princeton University', title='Princeton University'),
    ] = None


class AltoUniversity(BaseModel):
    class Config:
        extra = Extra.forbid

    Alto_University: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Alto University', title='Alto University'),
    ] = None


class UniversityOfCaliforniaSanDiego(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_California_San_Diego: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='University of California San Diego',
            title='University of California San Diego',
        ),
    ] = None


class IcahnSchoolOfMedicineAtMountSenai(BaseModel):
    class Config:
        extra = Extra.forbid

    Icahn_School_of_Medicine_at_Mount_Senai: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='Icahn School of Medicine at Mount Senai',
            title='Icahn School of Medicine at Mount Senai',
        ),
    ] = None


class UniversityOfHelsinki(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_Helsinki: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='University of Helsinki', title='University of Helsinki'),
    ] = None


class Institution(BaseModel):
    class Config:
        extra = Extra.forbid

    PI_Schema: Annotated[Optional[str], Field(alias='PI',title='PI')] = None
    siteId_Schema: Annotated[Optional[str], Field(alias='siteId',title='siteId')] = None
    name_Schema: Annotated[
        Optional[
            Union[
                UniversityOfTennesseeKnoxville,
                StanfordUniversity,
                UniversityOfPittsburgh,
                HarvardMedicalSchool,
                BrighamAndWomenSHospital,
                WeillCornellMedicine,
                UniversityOfOxford,
                VanderbiltUniversity,
                VanderbiltUniversityMedicalCenter,
                McleanHospital,
                UniversityOfCaliforniaLosAngeles,
                PrincetonUniversity,
                AltoUniversity,
                UniversityOfCaliforniaSanDiego,
                IcahnSchoolOfMedicineAtMountSenai,
                UniversityOfHelsinki,
            ]
        ],
        Field(alias='name',title='name'),
    ] = None


class Site(BaseModel):
    institution_Schema: Annotated[
        Optional[Institution], Field(alias='institution',title='institution')
    ] = None


class Other(BaseModel):
    class Config:
        extra = Extra.forbid

    Other_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Other',title='Other')] = None


class Mid(BaseModel):
    class Config:
        extra = Extra.forbid

    Mid_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Mid', title='Mid')] = None


class Post(BaseModel):
    class Config:
        extra = Extra.forbid

    Post_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Post',title='Post')] = None


class Baseline(BaseModel):
    class Config:
        extra = Extra.forbid

    Baseline_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Baseline',title='Baseline')] = None


class PreScan(BaseModel):
    class Config:
        extra = Extra.forbid

    Pre_Scan_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Pre-Scan', title='Pre-Scan')
    ] = None


class Admission(BaseModel):
    class Config:
        extra = Extra.forbid

    Admission_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Admission',title='Admission')
    ] = None


class BaselineSelfReport(BaseModel):
    class Config:
        extra = Extra.forbid

    Baseline_self_report: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Baseline self-report', title='Baseline self-report'),
    ] = None


class AlternativeBaseline(BaseModel):
    class Config:
        extra = Extra.forbid

    Alternative_baseline: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Alternative baseline', title='Alternative baseline'),
    ] = None


class Discharge(BaseModel):
    class Config:
        extra = Extra.forbid

    Discharge_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Discharge',title='Discharge')
    ] = None


class FollowUp(BaseModel):
    class Config:
        extra = Extra.forbid

    Follow_up_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Follow-up', title='Follow-up')
    ] = None


class Enrollment(BaseModel):
    class Config:
        extra = Extra.forbid

    Enrollment_Schema: Annotated[
        Optional[Dict[str, Any]], Field(title='Enrollment')
    ] = None


class MRIScreening(BaseModel):
    class Config:
        extra = Extra.forbid

    MRI_screening: Annotated[
        Optional[Dict[str, Any]], Field(alias='MRI screening', title='MRI screening')
    ] = None


class Scan(BaseModel):
    class Config:
        extra = Extra.forbid

    Scan_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Scan',title='Scan')] = None


class Screening(BaseModel):
    class Config:
        extra = Extra.forbid

    Screening_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Screening',title='Screening')
    ] = None


class Field1180Day(BaseModel):
    class Config:
        extra = Extra.forbid

    field_1_180_day: Annotated[
        Optional[Dict[str, Any]], Field(alias='1-180 day', title='1-180 day')
    ] = None


class LessThan1Day(BaseModel):
    class Config:
        extra = Extra.forbid

    less_than_1_day: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='less than 1 day', title='less than 1 day'),
    ] = None


class Other2(BaseModel):
    class Config:
        extra = Extra.forbid

    value_Schema: Annotated[Optional[str], Field(alias='value',title='value')] = None


class Other1(BaseModel):
    class Config:
        extra = Extra.forbid

    Other_Schema: Annotated[Optional[Other2], Field(alias='Other',title='Other')] = None


class CollectionTime(BaseModel):
    class Config:
        extra = Extra.forbid

    Collection_Phase: Annotated[
        Optional[Union[Other, Mid, Post, Baseline]],
        Field(alias='Collection Phase', title='Collection Phase'),
    ] = None
    Collection_Event: Annotated[
        Optional[
            Union[
                PreScan,
                Admission,
                BaselineSelfReport,
                AlternativeBaseline,
                Discharge,
                FollowUp,
                Enrollment,
                MRIScreening,
                Scan,
                Screening,
                Baseline,
            ]
        ],
        Field(alias='Collection Event', title='Collection Event'),
    ] = None
    Start_Time: Annotated[
        Optional[str], Field(alias='Start Time', title='Start Time')
    ] = None
    End_Time: Annotated[Optional[str], Field(alias='End Time', title='End Time')] = None
    Collection_Duration: Annotated[
        Optional[Union[Field1180Day, LessThan1Day, Other1]],
        Field(alias='Collection Duration', title='Collection Duration'),
    ] = None


class CollectionTiming(BaseModel):
    CollectionTime_Schema: Annotated[
        Optional[CollectionTime], Field(alias='CollectionTime', title='CollectionTime')
    ] = None


class RiskFactors(BaseModel):
    class Config:
        extra = Extra.forbid

    Stressful_life_events: Annotated[
        Optional[str],
        Field(alias='Stressful life events', title='Stressful life events'),
    ] = None
    Parental_bonding: Annotated[
        Optional[str], Field(alias='Parental bonding', title='Parental bonding')
    ] = None
    Social_life: Annotated[
        Optional[str], Field(alias='Social life', title='Social life')
    ] = None
    Childhood_sexual_abuse: Annotated[
        Optional[str],
        Field(alias='Childhood sexual abuse', title='Childhood sexual abuse'),
    ] = None
    Childhood_physical_abuse: Annotated[
        Optional[str],
        Field(alias='Childhood physical abuse', title='Childhood physical abuse'),
    ] = None
    Childhood_trauma: Annotated[
        Optional[str], Field(alias='Childhood trauma', title='Childhood trauma')
    ] = None
    Positive_Family_History: Annotated[
        Optional[str],
        Field(alias='Positive Family History', title='Positive Family History'),
    ] = None
    Personality_Schema: Annotated[Optional[str], Field(alias='Personality',title='Personality')] = None


class UNKNOWN(BaseModel):
    class Config:
        extra = Extra.forbid

    UNKNOWN_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='UNKNOWN',title='UNKNOWN')] = None


class YES(BaseModel):
    class Config:
        extra = Extra.forbid

    YES_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='YES',title='YES')] = None


class NO(BaseModel):
    class Config:
        extra = Extra.forbid

    NO_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='NO',title='NO')] = None


class TreatmentHistory(BaseModel):
    class Config:
        extra = Extra.forbid

    Previous_Treatment: Annotated[
        Optional[Union[UNKNOWN, YES, NO]],
        Field(alias='Previous Treatment', title='Previous Treatment'),
    ] = None
    Outcome_Schema: Annotated[Optional[str], Field(alias='Outcome',title='Outcome')] = None


class DBS(BaseModel):
    class Config:
        extra = Extra.forbid

    DBS_: Annotated[Optional[Dict[str, Any]], Field(alias='DBS', title='DBS ')] = None


class KetaminInfusion(BaseModel):
    class Config:
        extra = Extra.forbid

    Ketamin_Infusion: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Ketamin Infusion', title='Ketamin Infusion'),
    ] = None


class SAINT(BaseModel):
    class Config:
        extra = Extra.forbid

    SAINT_: Annotated[
        Optional[Dict[str, Any]], Field(alias='SAINT', title='SAINT')
    ] = None


class CBT(BaseModel):
    class Config:
        extra = Extra.forbid

    CBT_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='CBT',title='CBT')] = None


class TMS(BaseModel):
    class Config:
        extra = Extra.forbid

    TMS_: Annotated[Optional[Dict[str, Any]], Field(alias='TMS', title='TMS ')] = None


class RTMS(BaseModel):
    class Config:
        extra = Extra.forbid

    rTMS_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='rTMS',title='rTMS')] = None


class TBS(BaseModel):
    class Config:
        extra = Extra.forbid

    TBS_: Annotated[Optional[Dict[str, Any]], Field(alias='TBS', title='TBS ')] = None


class ITBS(BaseModel):
    class Config:
        extra = Extra.forbid

    iTBS_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='iTBS',title='iTBS')] = None


class UltrasoundPulsation(BaseModel):
    class Config:
        extra = Extra.forbid

    Ultrasound_Pulsation: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Ultrasound Pulsation', title='Ultrasound Pulsation'),
    ] = None


class Pharmacological(BaseModel):
    class Config:
        extra = Extra.forbid

    Pharmacological_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Pharmacological',title='Pharmacological')
    ] = None


class CurrentTreatment(BaseModel):
    class Config:
        extra = Extra.forbid

    Treatment_Type: Annotated[
        Optional[
            List[
                Union[
                    DBS,
                    KetaminInfusion,
                    SAINT,
                    CBT,
                    TMS,
                    RTMS,
                    TBS,
                    ITBS,
                    UltrasoundPulsation,
                    Pharmacological,
                ]
            ]
        ],
        Field(alias='Treatment Type', title='Treatment Type'),
    ] = None


class Dropout(BaseModel):
    class Config:
        extra = Extra.forbid

    Dropout_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Dropout',title='Dropout')] = None


class Completer(BaseModel):
    class Config:
        extra = Extra.forbid

    Completer_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Completer',title='Completer')
    ] = None


class Active(BaseModel):
    class Config:
        extra = Extra.forbid

    Active_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Active',title='Active')] = None


class Participant1(BaseModel):
    class Config:
        extra = Extra.forbid

    ParticipantID_Schema: Annotated[Optional[str], Field(alias='ParticipantID',title='ParticipantID')] = None
    ParticipantStatus_Schema: Annotated[
        Optional[Union[Dropout, Completer, Active]], Field(alias='ParticipantStatus',title='ParticipantStatus')
    ] = None


class Clinical(BaseModel):
    class Config:
        extra = Extra.forbid

    Length_of_current_MDE: Annotated[
        Optional[float],
        Field(alias='Length of current MDE', title='Length of current MDE'),
    ] = None
    No__of_prior_MDEs: Annotated[
        Optional[int], Field(alias='No. of prior MDEs', title='No. of prior MDEs')
    ] = None
    Baseline_QIDS_score: Annotated[
        Optional[int], Field(alias='Baseline QIDS score', title='Baseline QIDS score')
    ] = None
    Age_at_MDD_onset: Annotated[
        Optional[int], Field(alias='Age at MDD onset', title='Age at MDD onset')
    ] = None


class Social1(BaseModel):
    class Config:
        extra = Extra.forbid

    Adversity_Index: Annotated[
        Optional[str], Field(alias='Adversity Index', title='Adversity Index')
    ] = None
    Years_of_education: Annotated[
        Optional[int], Field(alias='Years of education', title='Years of education')
    ] = None
    ZIP_Schema: Annotated[Optional[str], Field(alias='ZIP',title='ZIP')] = None
    Occupation_Schema: Annotated[Optional[str], Field(alias='Occupation',title='Occupation')] = None
    Children_Schema: Annotated[Optional[int], Field(alias='Children',title='Children')] = None
    Country_Schema: Annotated[Optional[str], Field(alias='Country',title='Country')] = None
    State_Schema: Annotated[Optional[str], Field(alias='State',title='State')] = None


class SomethingElse(BaseModel):
    class Config:
        extra = Extra.forbid

    Something_else: Annotated[
        Optional[Dict[str, Any]], Field(alias='Something else', title='Something else')
    ] = None


class DidNotAnswerUnknown(BaseModel):
    class Config:
        extra = Extra.forbid

    Did_not_Answer_Unknown: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Did not Answer/Unknown', title='Did not Answer/Unknown'),
    ] = None


class Homosexual(BaseModel):
    class Config:
        extra = Extra.forbid

    Homosexual_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Homosexual',title='Homosexual')
    ] = None


class Heterosexual(BaseModel):
    class Config:
        extra = Extra.forbid

    Heterosexual_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Heterosexual',title='Heterosexual')
    ] = None


class Bisexual(BaseModel):
    class Config:
        extra = Extra.forbid

    Bisexual_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Bisexual',title='Bisexual')] = None


class ChooseNotToDisclose(BaseModel):
    class Config:
        extra = Extra.forbid

    Choose_not_to_disclose: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Choose not to disclose', title='Choose not to disclose'),
    ] = None


class DoNotKnow(BaseModel):
    class Config:
        extra = Extra.forbid

    Do_not_know: Annotated[
        Optional[Dict[str, Any]], Field(alias='Do not know', title='Do not know')
    ] = None


class Married(BaseModel):
    class Config:
        extra = Extra.forbid

    Married_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Married',title='Married')] = None


class Single(BaseModel):
    class Config:
        extra = Extra.forbid

    Single_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Single',title='Single')] = None


class Female(BaseModel):
    class Config:
        extra = Extra.forbid

    Female_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Female', title='Female')] = None


class Unkown(BaseModel):
    class Config:
        extra = Extra.forbid

    Unkown_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Unknown',title='Unkown')] = None


class Male(BaseModel):
    class Config:
        extra = Extra.forbid

    Male_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Male',title='Male')] = None


class Other3(BaseModel):
    class Config:
        extra = Extra.forbid

    Other_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Other',title='Other')] = None


class NonHispanicWhite(BaseModel):
    class Config:
        extra = Extra.forbid

    Non_Hispanic_White: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Non-Hispanic White', title='Non-Hispanic White'),
    ] = None


class NonHispanicBlack(BaseModel):
    class Config:
        extra = Extra.forbid

    Non_Hispanic_Black: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Non-Hispanic Black', title='Non-Hispanic Black'),
    ] = None


class AsianPacificIslander(BaseModel):
    class Config:
        extra = Extra.forbid

    Asian_Pacific_Islander_Schema: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Asian/Pacific-Islander', title='Asian/Pacific-Islander'),
    ] = None


class Hispanic(BaseModel):
    class Config:
        extra = Extra.forbid

    Hispanic_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Hispanic',title='Hispanic')] = None


class FemaleToMale(BaseModel):
    class Config:
        extra = Extra.forbid

    Female_to_Male_Schema: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Female-to-Male', title='Female-to-Male'),
    ] = None


class AdditionalCategory1(BaseModel):
    class Config:
        extra = Extra.forbid

    category_Schema: Annotated[Optional[str], Field(alias='category',title='category')] = None


class AdditionalCategory(BaseModel):
    class Config:
        extra = Extra.forbid

    Additional_category: Annotated[
        Optional[AdditionalCategory1],
        Field(alias='Additional category', title='Additional category'),
    ] = None


class MaleToFemale(BaseModel):
    class Config:
        extra = Extra.forbid

    Male_to_Female_Schema: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Male-to-Female', title='Male-to-Female'),
    ] = None


class NonConforming(BaseModel):
    class Config:
        extra = Extra.forbid

    Non_conforming_Schema: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Non-conforming', title='Non-conforming'),
    ] = None


class Demographics(BaseModel):
    class Config:
        extra = Extra.forbid

    Sexual_Orientation: Annotated[
        Optional[
            Union[
                SomethingElse,
                DidNotAnswerUnknown,
                Homosexual,
                Heterosexual,
                Bisexual,
                ChooseNotToDisclose,
                DoNotKnow,
            ]
        ],
        Field(alias='Sexual Orientation', title='Sexual Orientation'),
    ] = None
    Marital_Status: Annotated[
        Optional[Union[DidNotAnswerUnknown, Married, Single]],
        Field(alias='Marital Status', title='Marital Status'),
    ] = None
    Family_Income: Annotated[
        Optional[str], Field(alias='Family Income', title='Family Income')
    ] = None
    Sex_at_Birth: Annotated[
        Optional[Union[Female, Unkown, Male]],
        Field(alias='Sex at Birth', title='Sex at Birth'),
    ] = None
    Race_Schema: Annotated[
        Optional[
            Union[
                Other3,
                DidNotAnswerUnknown,
                NonHispanicWhite,
                NonHispanicBlack,
                AsianPacificIslander,
                Hispanic,
            ]
        ],
        Field(alias='Race',title='Race'),
    ] = None
    Age_Schema: Annotated[Optional[int], Field(alias='Age',title='Age')] = None
    Gender_Schema: Annotated[
        Optional[
            Union[
                FemaleToMale,
                AdditionalCategory,
                ChooseNotToDisclose,
                DidNotAnswerUnknown,
                Male,
                Female,
                MaleToFemale,
                NonConforming,
            ]
        ],
        Field(alias='Gender',title='Gender'),
    ] = None


class Left(BaseModel):
    class Config:
        extra = Extra.forbid

    Left_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Left',title='Left')] = None


class Right(BaseModel):
    class Config:
        extra = Extra.forbid

    Right_Schema: Annotated[Optional[Dict[str, Any]], Field(alias='Right',title='Right')] = None


class Ambidextrous(BaseModel):
    class Config:
        extra = Extra.forbid

    Ambidextrous_Schema: Annotated[
        Optional[Dict[str, Any]], Field(alias='Ambidextrous',title='Ambidextrous')
    ] = None


class Physical(BaseModel):
    class Config:
        extra = Extra.forbid

    Height_in_Inches: Annotated[
        Optional[float], Field(alias='Height in Inches', title='Height in Inches')
    ] = None
    Weight_in_Pounds: Annotated[
        Optional[float], Field(alias='Weight in Pounds', title='Weight in Pounds')
    ] = None
    Handidness_Schema: Annotated[
        Optional[Union[Left, Right, Ambidextrous]], Field(alias='Handidness',title='Handidness')
    ] = None


class Participant(BaseModel):
    Risk_factors_: Annotated[
        Optional[RiskFactors], Field(alias='Risk factors?', title='Risk factors?')
    ] = None
    Treatment_History: Annotated[
        Optional[TreatmentHistory],
        Field(alias='Treatment History', title='Treatment History'),
    ] = None
    Current_Treatment: Annotated[
        Optional[CurrentTreatment],
        Field(alias='Current Treatment', title='Current Treatment'),
    ] = None
    Participant_Schema: Annotated[
        Optional[Participant1], Field(alias='Participant',title='Participant')
    ] = None
    Clinical_Schema: Annotated[Optional[Clinical], Field(alias='Clinical',title='Clinical')] = None
    Social_Schema: Annotated[Optional[Social1], Field(alias='Social',title='Social')] = None
    Demographics_Schema: Annotated[
        Optional[Demographics], Field(alias='Demographics',title='Demographics')
    ] = None
    Physical_Schema: Annotated[Optional[Physical], Field(alias='Physical',title='Physical')] = None


class MetadataForEMAContentSandboxV1(BaseModel):
    class Config:
        extra = Extra.forbid

    Ecological_Momentary_Assessment: Annotated[
        Optional[EcologicalMomentaryAssessment],
        Field(
            alias='Ecological Momentary Assessment',
            title='Ecological Momentary Assessment',
        ),
    ] = None
    Input_Data_Collection: Annotated[
        Optional[InputDataCollection],
        Field(alias='Input Data Collection', title='Input Data Collection'),
    ] = None
    Site_: Annotated[Optional[Site], Field(alias='Site', title='Site ')] = None
    Collection_Timing: Annotated[
        Optional[CollectionTiming],
        Field(alias='Collection Timing', title='Collection Timing'),
    ] = None
    Participant_: Annotated[
        Optional[Participant], Field(alias='Participant ', title='Participant ')
    ] = None
