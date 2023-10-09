# generated by datamodel-codegen:
#   filename:  jsonschemaLeo.json
#   timestamp: 2023-10-04T18:33:32+00:00

from __future__ import annotations

from typing import Any, Dict, Optional, Set, Union

from pydantic import BaseModel, Extra, Field
from typing_extensions import Annotated


class QuestionWindowItem(BaseModel):
    class Config:
        extra = Extra.forbid

    Past_Week: Annotated[
        Optional[Dict[str, Any]], Field(alias='Past Week', title='Past Week')
    ] = None


class QuestionWindowItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Past_Month: Annotated[
        Optional[Dict[str, Any]], Field(alias='Past Month', title='Past Month')
    ] = None


class QuestionWindowItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    Now: Annotated[Optional[Dict[str, Any]], Field(title='Now')] = None


class QuestionWindowItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    Past_Three_Days: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Past Three Days', title='Past Three Days'),
    ] = None


class DeviceItem(BaseModel):
    class Config:
        extra = Extra.forbid

    iPhone: Annotated[Optional[Dict[str, Any]], Field(title='iPhone')] = None


class DeviceItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Android: Annotated[Optional[Dict[str, Any]], Field(title='Android')] = None


class CategoryItem(BaseModel):
    class Config:
        extra = Extra.forbid

    Sleep: Annotated[Optional[Dict[str, Any]], Field(title='Sleep')] = None


class CategoryItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Activity: Annotated[Optional[Dict[str, Any]], Field(title='Activity')] = None


class CategoryItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    Suicide: Annotated[Optional[Dict[str, Any]], Field(title='Suicide')] = None


class CategoryItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    Emotion: Annotated[Optional[Dict[str, Any]], Field(title='Emotion')] = None


class CategoryItem4(BaseModel):
    class Config:
        extra = Extra.forbid

    Anhedonia: Annotated[Optional[Dict[str, Any]], Field(title='Anhedonia')] = None


class CategoryItem5(BaseModel):
    class Config:
        extra = Extra.forbid

    Social: Annotated[Optional[Dict[str, Any]], Field(title='Social')] = None


class EMA(BaseModel):
    class Config:
        extra = Extra.forbid

    Configuration_File: Annotated[
        Optional[bool], Field(alias='Configuration File', title='Configuration File')
    ] = True
    Question_Window: Annotated[
        Optional[
            Union[
                QuestionWindowItem,
                QuestionWindowItem1,
                QuestionWindowItem2,
                QuestionWindowItem3,
            ]
        ],
        Field(alias='Question Window', title='Question Window'),
    ] = None
    Device: Annotated[
        Optional[Union[DeviceItem, DeviceItem1]], Field(title='Device')
    ] = None
    Category: Annotated[
        Optional[
            Set[
                Union[
                    CategoryItem,
                    CategoryItem1,
                    CategoryItem2,
                    CategoryItem3,
                    CategoryItem4,
                    CategoryItem5,
                ]
            ]
        ],
        # Field(title='Category', unique_items=True),
        Field(title='Category'),
    ] = None


class EcologicalMomentaryAssessment(BaseModel):
    EMA: Annotated[Optional[EMA], Field(title='EMA')] = None


class StudySiteItem(BaseModel):
    class Config:
        extra = Extra.forbid

    Helsinki_Alto: Annotated[
        Optional[Dict[str, Any]], Field(alias='Helsinki-Alto', title='Helsinki-Alto')
    ] = None


class StudySiteItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Vanderbilt: Annotated[Optional[Dict[str, Any]], Field(title='Vanderbilt')] = None


class StudySiteItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    VUMC: Annotated[Optional[Dict[str, Any]], Field(title='VUMC')] = None


class StudySiteItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    UCLA: Annotated[Optional[Dict[str, Any]], Field(title='UCLA')] = None


class StudySiteItem4(BaseModel):
    class Config:
        extra = Extra.forbid

    McLean: Annotated[Optional[Dict[str, Any]], Field(title='McLean')] = None


class StudySiteItem5(BaseModel):
    class Config:
        extra = Extra.forbid

    Cornell: Annotated[Optional[Dict[str, Any]], Field(title='Cornell')] = None


class StudySiteItem6(BaseModel):
    class Config:
        extra = Extra.forbid

    UCSD: Annotated[Optional[Dict[str, Any]], Field(title='UCSD')] = None


class StudySiteItem7(BaseModel):
    class Config:
        extra = Extra.forbid

    Stanford: Annotated[Optional[Dict[str, Any]], Field(title='Stanford')] = None


class StudySiteItem8(BaseModel):
    class Config:
        extra = Extra.forbid

    MSSM_Mayberg: Annotated[
        Optional[Dict[str, Any]], Field(alias='MSSM-Mayberg', title='MSSM-Mayberg')
    ] = None


class StudySiteItem9(BaseModel):
    class Config:
        extra = Extra.forbid

    MSSM_Murrough: Annotated[
        Optional[Dict[str, Any]], Field(alias='MSSM-Murrough', title='MSSM-Murrough')
    ] = None


class StudySiteItem10(BaseModel):
    class Config:
        extra = Extra.forbid

    Princeton: Annotated[Optional[Dict[str, Any]], Field(title='Princeton')] = None


class StudySiteItem11(BaseModel):
    class Config:
        extra = Extra.forbid

    Pittsburgh: Annotated[Optional[Dict[str, Any]], Field(title='Pittsburgh')] = None


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
                StudySiteItem,
                StudySiteItem1,
                StudySiteItem2,
                StudySiteItem3,
                StudySiteItem4,
                StudySiteItem5,
                StudySiteItem6,
                StudySiteItem7,
                StudySiteItem8,
                StudySiteItem9,
                StudySiteItem10,
                StudySiteItem11,
            ]
        ],
        Field(alias='Study Site', title='Study Site'),
    ] = None


class ModalityItem(BaseModel):
    class Config:
        extra = Extra.forbid

    Digital_: Annotated[
        Optional[Dict[str, Any]], Field(alias='Digital ', title='Digital ')
    ] = None


class ModalityItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Psychometrics: Annotated[
        Optional[Dict[str, Any]], Field(title='Psychometrics')
    ] = None


class ModalityItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    Synthetic_EEG: Annotated[
        Optional[Dict[str, Any]], Field(alias='Synthetic EEG', title='Synthetic EEG')
    ] = None


class ModalityItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    Neuropsychological_Assessments: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='Neuropsychological Assessments',
            title='Neuropsychological Assessments',
        ),
    ] = None


class ModalityItem4(BaseModel):
    class Config:
        extra = Extra.forbid

    Genetics: Annotated[Optional[Dict[str, Any]], Field(title='Genetics')] = None


class ModalityItem5(BaseModel):
    class Config:
        extra = Extra.forbid

    EMR_Clinical_Data: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='EMR Clinical Data', title='EMR Clinical Data'),
    ] = None


class ModalityItem6(BaseModel):
    class Config:
        extra = Extra.forbid

    Behavioral__Assessments: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Behavioral  Assessments', title='Behavioral  Assessments'),
    ] = None


class ModalityItem7(BaseModel):
    class Config:
        extra = Extra.forbid

    Ecological_Momentary_Assessments: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='Ecological Momentary Assessments',
            title='Ecological Momentary Assessments',
        ),
    ] = None


class ModalityItem8(BaseModel):
    class Config:
        extra = Extra.forbid

    Neurocognitive_Task_Performance: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='Neurocognitive Task Performance',
            title='Neurocognitive Task Performance',
        ),
    ] = None


class ModalityItem9(BaseModel):
    class Config:
        extra = Extra.forbid

    Affect_Interview: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Affect Interview', title='Affect Interview'),
    ] = None


class ModalityItem10(BaseModel):
    class Config:
        extra = Extra.forbid

    MRI: Annotated[Optional[Dict[str, Any]], Field(title='MRI')] = None


class ModalityItem11(BaseModel):
    class Config:
        extra = Extra.forbid

    EEG: Annotated[Optional[Dict[str, Any]], Field(title='EEG')] = None


class ModalityItem12(BaseModel):
    class Config:
        extra = Extra.forbid

    Liquid_Markers: Annotated[
        Optional[Dict[str, Any]], Field(alias='Liquid Markers', title='Liquid Markers')
    ] = None


class CategoryOfData(BaseModel):
    class Config:
        extra = Extra.forbid

    Modality: Annotated[
        Optional[
            Union[
                ModalityItem,
                ModalityItem1,
                ModalityItem2,
                ModalityItem3,
                ModalityItem4,
                ModalityItem5,
                ModalityItem6,
                ModalityItem7,
                ModalityItem8,
                ModalityItem9,
                ModalityItem10,
                ModalityItem11,
                ModalityItem12,
            ]
        ],
        Field(title='Modality'),
    ] = None


class InputDataCollection(BaseModel):
    Collection_: Annotated[
        Optional[Collection], Field(alias='Collection ', title='Collection ')
    ] = None
    Category_of_Data: Annotated[
        Optional[CategoryOfData],
        Field(alias='Category of Data', title='Category of Data'),
    ] = None


class NameItem(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_Tennessee_Knoxville: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='University of Tennessee Knoxville',
            title='University of Tennessee Knoxville',
        ),
    ] = None


class NameItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Stanford_University: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Stanford University', title='Stanford University'),
    ] = None


class NameItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_Pittsburgh: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='University of Pittsburgh', title='University of Pittsburgh'),
    ] = None


class NameItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    Harvard_Medical_School: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Harvard Medical School', title='Harvard Medical School'),
    ] = None


class NameItem4(BaseModel):
    class Config:
        extra = Extra.forbid

    Brigham_and_Women_s_Hospital: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias="Brigham and Women's Hospital", title="Brigham and Women's Hospital"
        ),
    ] = None


class NameItem5(BaseModel):
    class Config:
        extra = Extra.forbid

    Weill_Cornell_Medicine: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Weill Cornell Medicine', title='Weill Cornell Medicine'),
    ] = None


class NameItem6(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_Oxford: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='University of Oxford', title='University of Oxford'),
    ] = None


class NameItem7(BaseModel):
    class Config:
        extra = Extra.forbid

    Vanderbilt_University: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Vanderbilt University', title='Vanderbilt University'),
    ] = None


class NameItem8(BaseModel):
    class Config:
        extra = Extra.forbid

    Vanderbilt_University_Medical_Center: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='Vanderbilt University Medical Center',
            title='Vanderbilt University Medical Center',
        ),
    ] = None


class NameItem9(BaseModel):
    class Config:
        extra = Extra.forbid

    Mclean_Hospital: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Mclean Hospital', title='Mclean Hospital'),
    ] = None


class NameItem10(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_California_Los_Angeles: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='University of California Los Angeles',
            title='University of California Los Angeles',
        ),
    ] = None


class NameItem11(BaseModel):
    class Config:
        extra = Extra.forbid

    Princeton_University: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Princeton University', title='Princeton University'),
    ] = None


class NameItem12(BaseModel):
    class Config:
        extra = Extra.forbid

    Alto_University: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Alto University', title='Alto University'),
    ] = None


class NameItem13(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_California_San_Diego: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='University of California San Diego',
            title='University of California San Diego',
        ),
    ] = None


class NameItem14(BaseModel):
    class Config:
        extra = Extra.forbid

    Icahn_School_of_Medicine_at_Mount_Senai: Annotated[
        Optional[Dict[str, Any]],
        Field(
            alias='Icahn School of Medicine at Mount Senai',
            title='Icahn School of Medicine at Mount Senai',
        ),
    ] = None


class NameItem15(BaseModel):
    class Config:
        extra = Extra.forbid

    University_of_Helsinki: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='University of Helsinki', title='University of Helsinki'),
    ] = None


class Institution(BaseModel):
    class Config:
        extra = Extra.forbid

    PI: Annotated[Optional[str], Field(title='PI')] = None
    siteId: Annotated[Optional[str], Field(title='siteId')] = None
    name: Annotated[
        Optional[
            Union[
                NameItem,
                NameItem1,
                NameItem2,
                NameItem3,
                NameItem4,
                NameItem5,
                NameItem6,
                NameItem7,
                NameItem8,
                NameItem9,
                NameItem10,
                NameItem11,
                NameItem12,
                NameItem13,
                NameItem14,
                NameItem15,
            ]
        ],
        Field(title='name'),
    ] = None


class Site(BaseModel):
    institution: Annotated[Optional[Institution], Field(title='institution')] = None


class CollectionPhaseItem(BaseModel):
    class Config:
        extra = Extra.forbid

    Other: Annotated[Optional[Dict[str, Any]], Field(title='Other')] = None


class CollectionPhaseItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Mid: Annotated[Optional[Dict[str, Any]], Field(title='Mid')] = None


class CollectionPhaseItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    Post: Annotated[Optional[Dict[str, Any]], Field(title='Post')] = None


class CollectionPhaseItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    Baseline: Annotated[Optional[Dict[str, Any]], Field(title='Baseline')] = None


class CollectionEventItem(BaseModel):
    class Config:
        extra = Extra.forbid

    Pre_Scan: Annotated[
        Optional[Dict[str, Any]], Field(alias='Pre-Scan', title='Pre-Scan')
    ] = None


class CollectionEventItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Admission: Annotated[Optional[Dict[str, Any]], Field(title='Admission')] = None


class CollectionEventItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    Baseline_self_report: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Baseline self-report', title='Baseline self-report'),
    ] = None


class CollectionEventItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    Alternative_baseline: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Alternative baseline', title='Alternative baseline'),
    ] = None


class CollectionEventItem4(BaseModel):
    class Config:
        extra = Extra.forbid

    Discharge: Annotated[Optional[Dict[str, Any]], Field(title='Discharge')] = None


class CollectionEventItem5(BaseModel):
    class Config:
        extra = Extra.forbid

    Follow_up: Annotated[
        Optional[Dict[str, Any]], Field(alias='Follow-up', title='Follow-up')
    ] = None


class CollectionEventItem6(BaseModel):
    class Config:
        extra = Extra.forbid

    Enrollment: Annotated[Optional[Dict[str, Any]], Field(title='Enrollment')] = None


class CollectionEventItem7(BaseModel):
    class Config:
        extra = Extra.forbid

    MRI_screening: Annotated[
        Optional[Dict[str, Any]], Field(alias='MRI screening', title='MRI screening')
    ] = None


class CollectionEventItem8(BaseModel):
    class Config:
        extra = Extra.forbid

    Scan: Annotated[Optional[Dict[str, Any]], Field(title='Scan')] = None


class CollectionEventItem9(BaseModel):
    class Config:
        extra = Extra.forbid

    Screening: Annotated[Optional[Dict[str, Any]], Field(title='Screening')] = None


class CollectionEventItem10(BaseModel):
    class Config:
        extra = Extra.forbid

    Baseline: Annotated[Optional[Dict[str, Any]], Field(title='Baseline')] = None


class CollectionDurationItem(BaseModel):
    class Config:
        extra = Extra.forbid

    field_1_180_day: Annotated[
        Optional[Dict[str, Any]], Field(alias='1-180 day', title='1-180 day')
    ] = None


class CollectionDurationItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    less_than_1_day: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='less than 1 day', title='less than 1 day'),
    ] = None


class Other(BaseModel):
    class Config:
        extra = Extra.forbid

    value: Annotated[Optional[str], Field(title='value')] = None


class CollectionDurationItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    Other: Annotated[Optional[Other], Field(title='Other')] = None


class CollectionTime(BaseModel):
    class Config:
        extra = Extra.forbid

    Collection_Phase: Annotated[
        Optional[
            Union[
                CollectionPhaseItem,
                CollectionPhaseItem1,
                CollectionPhaseItem2,
                CollectionPhaseItem3,
            ]
        ],
        Field(alias='Collection Phase', title='Collection Phase'),
    ] = None
    Collection_Event: Annotated[
        Optional[
            Union[
                CollectionEventItem,
                CollectionEventItem1,
                CollectionEventItem2,
                CollectionEventItem3,
                CollectionEventItem4,
                CollectionEventItem5,
                CollectionEventItem6,
                CollectionEventItem7,
                CollectionEventItem8,
                CollectionEventItem9,
                CollectionEventItem10,
            ]
        ],
        Field(alias='Collection Event', title='Collection Event'),
    ] = None
    Start_Time: Annotated[
        Optional[str], Field(alias='Start Time', title='Start Time')
    ] = None
    End_Time: Annotated[Optional[str], Field(alias='End Time', title='End Time')] = None
    Collection_Duration: Annotated[
        Optional[
            Union[
                CollectionDurationItem, CollectionDurationItem1, CollectionDurationItem2
            ]
        ],
        Field(alias='Collection Duration', title='Collection Duration'),
    ] = None


class CollectionTiming(BaseModel):
    CollectionTime: Annotated[
        Optional[CollectionTime], Field(title='CollectionTime')
    ] = None


class ParticipantStatu(BaseModel):
    class Config:
        extra = Extra.forbid

    Dropout: Annotated[Optional[Dict[str, Any]], Field(title='Dropout')] = None


class ParticipantStatu1(BaseModel):
    class Config:
        extra = Extra.forbid

    Completer: Annotated[Optional[Dict[str, Any]], Field(title='Completer')] = None


class ParticipantStatu2(BaseModel):
    class Config:
        extra = Extra.forbid

    Active: Annotated[Optional[Dict[str, Any]], Field(title='Active')] = None


class Participant1(BaseModel):
    class Config:
        extra = Extra.forbid

    ParticipantID: Annotated[Optional[str], Field(title='ParticipantID')] = None
    ParticipantStatus: Annotated[
        Optional[Union[ParticipantStatu, ParticipantStatu1, ParticipantStatu2]],
        Field(title='ParticipantStatus'),
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
    Personality: Annotated[Optional[str], Field(title='Personality')] = None
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


class PreviousTreatmentItem(BaseModel):
    class Config:
        extra = Extra.forbid

    UNKNOWN: Annotated[Optional[Dict[str, Any]], Field(title='UNKNOWN')] = None


class PreviousTreatmentItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    YES: Annotated[Optional[Dict[str, Any]], Field(title='YES')] = None


class PreviousTreatmentItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    NO: Annotated[Optional[Dict[str, Any]], Field(title='NO')] = None


class TreatmentHistory(BaseModel):
    class Config:
        extra = Extra.forbid

    Previous_Treatment: Annotated[
        Optional[
            Union[PreviousTreatmentItem, PreviousTreatmentItem1, PreviousTreatmentItem2]
        ],
        Field(alias='Previous Treatment', title='Previous Treatment'),
    ] = None
    Outcome: Annotated[Optional[str], Field(title='Outcome')] = None


class TreatmentTypeItem(BaseModel):
    class Config:
        extra = Extra.forbid

    DBS_: Annotated[Optional[Dict[str, Any]], Field(alias='DBS ', title='DBS ')] = None


class TreatmentTypeItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Ketamin_Infusion: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Ketamin Infusion', title='Ketamin Infusion'),
    ] = None


class TreatmentTypeItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    SAINT_: Annotated[
        Optional[Dict[str, Any]], Field(alias='SAINT ', title='SAINT ')
    ] = None


class TreatmentTypeItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    CBT: Annotated[Optional[Dict[str, Any]], Field(title='CBT')] = None


class TreatmentTypeItem4(BaseModel):
    class Config:
        extra = Extra.forbid

    TMS_: Annotated[Optional[Dict[str, Any]], Field(alias='TMS ', title='TMS ')] = None


class TreatmentTypeItem5(BaseModel):
    class Config:
        extra = Extra.forbid

    rTMS: Annotated[Optional[Dict[str, Any]], Field(title='rTMS')] = None


class TreatmentTypeItem6(BaseModel):
    class Config:
        extra = Extra.forbid

    TBS_: Annotated[Optional[Dict[str, Any]], Field(alias='TBS ', title='TBS ')] = None


class TreatmentTypeItem7(BaseModel):
    class Config:
        extra = Extra.forbid

    iTBS: Annotated[Optional[Dict[str, Any]], Field(title='iTBS')] = None


class TreatmentTypeItem8(BaseModel):
    class Config:
        extra = Extra.forbid

    Ultrasound_Pulsation: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Ultrasound Pulsation', title='Ultrasound Pulsation'),
    ] = None


class TreatmentTypeItem9(BaseModel):
    class Config:
        extra = Extra.forbid

    Pharmacological: Annotated[
        Optional[Dict[str, Any]], Field(title='Pharmacological')
    ] = None


class CurrentTreatment(BaseModel):
    class Config:
        extra = Extra.forbid

    Treatment_Type: Annotated[
        Optional[
            Set[
                Union[
                    TreatmentTypeItem,
                    TreatmentTypeItem1,
                    TreatmentTypeItem2,
                    TreatmentTypeItem3,
                    TreatmentTypeItem4,
                    TreatmentTypeItem5,
                    TreatmentTypeItem6,
                    TreatmentTypeItem7,
                    TreatmentTypeItem8,
                    TreatmentTypeItem9,
                ]
            ]
        ],
        # Field(alias='Treatment Type', title='Treatment Type', unique_items=True),
        Field(alias='Treatment Type', title='Treatment Type'),

    ] = None


class Social(BaseModel):
    class Config:
        extra = Extra.forbid

    ZIP: Annotated[Optional[str], Field(title='ZIP')] = None
    Adversity_Index: Annotated[
        Optional[str], Field(alias='Adversity Index', title='Adversity Index')
    ] = None
    Years_of_education: Annotated[
        Optional[int], Field(alias='Years of education', title='Years of education')
    ] = None
    Occupation: Annotated[Optional[str], Field(title='Occupation')] = None
    Children: Annotated[Optional[int], Field(title='Children')] = None
    Country: Annotated[Optional[str], Field(title='Country')] = None
    State: Annotated[Optional[str], Field(title='State')] = None


class RaceItem(BaseModel):
    class Config:
        extra = Extra.forbid

    Other: Annotated[Optional[Dict[str, Any]], Field(title='Other')] = None


class RaceItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Did_not_Answer_Unknown: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Did not Answer/Unknown', title='Did not Answer/Unknown'),
    ] = None


class RaceItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    Non_Hispanic_White: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Non-Hispanic White', title='Non-Hispanic White'),
    ] = None


class RaceItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    Non_Hispanic_Black: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Non-Hispanic Black', title='Non-Hispanic Black'),
    ] = None


class RaceItem4(BaseModel):
    class Config:
        extra = Extra.forbid

    Asian_Pacific_Islander: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Asian/Pacific-Islander', title='Asian/Pacific-Islander'),
    ] = None


class RaceItem5(BaseModel):
    class Config:
        extra = Extra.forbid

    Hispanic: Annotated[Optional[Dict[str, Any]], Field(title='Hispanic')] = None


class SexualOrientationItem(BaseModel):
    class Config:
        extra = Extra.forbid

    Something_else: Annotated[
        Optional[Dict[str, Any]], Field(alias='Something else', title='Something else')
    ] = None


class SexualOrientationItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Did_not_Answer_Unknown: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Did not Answer/Unknown', title='Did not Answer/Unknown'),
    ] = None


class SexualOrientationItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    Homosexual: Annotated[Optional[Dict[str, Any]], Field(title='Homosexual')] = None


class SexualOrientationItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    Heterosexual: Annotated[
        Optional[Dict[str, Any]], Field(title='Heterosexual')
    ] = None


class SexualOrientationItem4(BaseModel):
    class Config:
        extra = Extra.forbid

    Bisexual: Annotated[Optional[Dict[str, Any]], Field(title='Bisexual')] = None


class SexualOrientationItem5(BaseModel):
    class Config:
        extra = Extra.forbid

    Choose_not_to_disclose: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Choose not to disclose', title='Choose not to disclose'),
    ] = None


class SexualOrientationItem6(BaseModel):
    class Config:
        extra = Extra.forbid

    Do_not_know: Annotated[
        Optional[Dict[str, Any]], Field(alias='Do not know', title='Do not know')
    ] = None


class MaritalStatu(BaseModel):
    class Config:
        extra = Extra.forbid

    Did_not_Answer_Unknown: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Did not Answer/Unknown', title='Did not Answer/Unknown'),
    ] = None


class MaritalStatu1(BaseModel):
    class Config:
        extra = Extra.forbid

    Married: Annotated[Optional[Dict[str, Any]], Field(title='Married')] = None


class MaritalStatu2(BaseModel):
    class Config:
        extra = Extra.forbid

    Single: Annotated[Optional[Dict[str, Any]], Field(title='Single')] = None


class SexAtBirthItem(BaseModel):
    class Config:
        extra = Extra.forbid

    Female: Annotated[Optional[Dict[str, Any]], Field(title='Female')] = None


class SexAtBirthItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Unkown: Annotated[Optional[Dict[str, Any]], Field(title='Unkown')] = None


class SexAtBirthItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    Male: Annotated[Optional[Dict[str, Any]], Field(title='Male')] = None


class GenderItem(BaseModel):
    class Config:
        extra = Extra.forbid

    Female_to_Male: Annotated[
        Optional[Dict[str, Any]], Field(alias='Female-to-Male', title='Female-to-Male')
    ] = None


class AdditionalCategory(BaseModel):
    class Config:
        extra = Extra.forbid

    category: Annotated[Optional[str], Field(title='category')] = None


class GenderItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    Additional_category: Annotated[
        Optional[AdditionalCategory],
        Field(alias='Additional category', title='Additional category'),
    ] = None


class GenderItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    Choose_not_to_disclose: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Choose not to disclose', title='Choose not to disclose'),
    ] = None


class GenderItem3(BaseModel):
    class Config:
        extra = Extra.forbid

    Did_not_Answer_Unknown: Annotated[
        Optional[Dict[str, Any]],
        Field(alias='Did not Answer/Unknown', title='Did not Answer/Unknown'),
    ] = None


class GenderItem4(BaseModel):
    class Config:
        extra = Extra.forbid

    Male: Annotated[Optional[Dict[str, Any]], Field(title='Male')] = None


class GenderItem5(BaseModel):
    class Config:
        extra = Extra.forbid

    Female: Annotated[Optional[Dict[str, Any]], Field(title='Female')] = None


class GenderItem6(BaseModel):
    class Config:
        extra = Extra.forbid

    Male_to_Female: Annotated[
        Optional[Dict[str, Any]], Field(alias='Male-to-Female', title='Male-to-Female')
    ] = None


class GenderItem7(BaseModel):
    class Config:
        extra = Extra.forbid

    Non_conforming: Annotated[
        Optional[Dict[str, Any]], Field(alias='Non-conforming', title='Non-conforming')
    ] = None


class Demographics(BaseModel):
    class Config:
        extra = Extra.forbid

    Race: Annotated[
        Optional[
            Union[RaceItem, RaceItem1, RaceItem2, RaceItem3, RaceItem4, RaceItem5]
        ],
        Field(title='Race'),
    ] = None
    Age: Annotated[Optional[int], Field(title='Age')] = None
    Sexual_Orientation: Annotated[
        Optional[
            Union[
                SexualOrientationItem,
                SexualOrientationItem1,
                SexualOrientationItem2,
                SexualOrientationItem3,
                SexualOrientationItem4,
                SexualOrientationItem5,
                SexualOrientationItem6,
            ]
        ],
        Field(alias='Sexual Orientation', title='Sexual Orientation'),
    ] = None
    Marital_Status: Annotated[
        Optional[Union[MaritalStatu, MaritalStatu1, MaritalStatu2]],
        Field(alias='Marital Status', title='Marital Status'),
    ] = None
    Family_Income: Annotated[
        Optional[str], Field(alias='Family Income', title='Family Income')
    ] = None
    Sex_at_Birth: Annotated[
        Optional[Union[SexAtBirthItem, SexAtBirthItem1, SexAtBirthItem2]],
        Field(alias='Sex at Birth', title='Sex at Birth'),
    ] = None
    Gender: Annotated[
        Optional[
            Union[
                GenderItem,
                GenderItem1,
                GenderItem2,
                GenderItem3,
                GenderItem4,
                GenderItem5,
                GenderItem6,
                GenderItem7,
            ]
        ],
        Field(title='Gender'),
    ] = None


class Handidnes(BaseModel):
    class Config:
        extra = Extra.forbid

    Left: Annotated[Optional[Dict[str, Any]], Field(title='Left')] = None


class Handidnes1(BaseModel):
    class Config:
        extra = Extra.forbid

    Right: Annotated[Optional[Dict[str, Any]], Field(title='Right')] = None


class Handidnes2(BaseModel):
    class Config:
        extra = Extra.forbid

    Ambidextrous: Annotated[
        Optional[Dict[str, Any]], Field(title='Ambidextrous')
    ] = None


class Physical(BaseModel):
    class Config:
        extra = Extra.forbid

    Handidness: Annotated[
        Optional[Union[Handidnes, Handidnes1, Handidnes2]], Field(title='Handidness')
    ] = None
    Height_in_Inches: Annotated[
        Optional[float], Field(alias='Height in Inches', title='Height in Inches')
    ] = None
    Weight_in_Pounds: Annotated[
        Optional[float], Field(alias='Weight in Pounds', title='Weight in Pounds')
    ] = None


class Participant(BaseModel):
    Participant: Annotated[Optional[Participant1], Field(title='Participant')] = None
    Clinical: Annotated[Optional[Clinical], Field(title='Clinical')] = None
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
    Social: Annotated[Optional[Social], Field(title='Social')] = None
    Demographics: Annotated[Optional[Demographics], Field(title='Demographics')] = None
    Physical: Annotated[Optional[Physical], Field(title='Physical')] = None


class MetadataForEmaContentSandboxV1(BaseModel):
    class Config:
        extra = Extra.forbid

    Ecological_Momentary_Assessment: Annotated[
        Optional[EcologicalMomentaryAssessment],
        Field(alias='Ecological Momentary Assessment'),
    ] = None
    Input_Data_Collection: Annotated[
        Optional[InputDataCollection], Field(alias='Input Data Collection')
    ] = None
    Site: Optional[Site] = None
    Collection_Timing: Annotated[
        Optional[CollectionTiming], Field(alias='Collection Timing')
    ] = None
    Participant: Optional[Participant] = None
