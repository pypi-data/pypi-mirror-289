from dataclasses import dataclass as __dataclass, InitVar


@__dataclass
class ResponseObject:
    pass


@__dataclass
class Course(ResponseObject):
    id: int
    shortname: str
    categoryid: int
    categorysortorder: InitVar[str]
    fullname: str
    displayname: str
    idnumber: InitVar[int]
    summary: str
    summaryformat: InitVar[int]
    format: InitVar[str]
    showgrades: InitVar[int]
    newsitems: InitVar[int]
    startdate: InitVar[int]
    enddate: InitVar[int]
    numsections: int
    maxbytes: InitVar[int]
    showreports: InitVar[int]
    visible: int
    hiddensections: InitVar[int]
    groupmode: InitVar[int]
    groupmodeforce: InitVar[int]
    defaultgroupingid: InitVar[int]
    timecreated: InitVar[int]
    timemodified: InitVar[int]
    enablecompletion: InitVar[int]
    completionnotify: InitVar[int]
    lang: InitVar[int]
    forcetheme: InitVar[int]
    courseformatoptions: InitVar[list[dict[str, int]]]
