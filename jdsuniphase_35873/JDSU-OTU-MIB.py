# SNMP MIB module (JDSU-OTU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/jdsuniphase_35873/JDSU-OTU-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:53:13 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(jdsuOtu,) = mibBuilder.importSymbols(
    "JDSU-SMI-MIB",
    "jdsuOtu")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jdsuOtuMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jdsuOtuMib.setRevisions(
        ("2020-10-02 16:13",
         "2021-07-27 17:49",
         "2021-07-22 16:48",
         "2019-12-12 07:25",
         "2019-09-11 15:49",
         "2019-08-27 16:00",
         "2019-01-25 09:00",
         "2017-12-15 13:46",
         "2017-08-12 14:07",
         "2017-03-23 10:44",
         "2015-11-10 14:27",
         "2014-01-22 08:51")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JdsuOnmsiUtf8String(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )



class JdsuOtuAlarmSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5),
          ("indeterminate", 6))
    )



class JdsuOtuAlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optic", 1),
          ("system", 2))
    )



class JdsuOtuMonitoringStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notmonitored", 0),
          ("monitored", 1))
    )



class JdsuOtuOpticalAlarmSubProblem(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fiberCut", 1),
          ("injection", 2),
          ("attenuation", 3),
          ("shortEventLevel", 4),
          ("notUsed2", 5),
          ("notUsed3", 6),
          ("notUsed4", 7),
          ("notUsed5", 8))
    )



class JdsuOtuAlarmSpecificProblem(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("attenuation", 1),
          ("missingOrCorruptedFile", 2),
          ("localMode", 3),
          ("innerApplicationCommunicationProblem", 4),
          ("harddiskSpace", 5),
          ("temperature", 6),
          ("switchProblem", 7),
          ("moduleProblem", 8),
          ("moduleCompatibility", 9),
          ("switchCompatibility", 10),
          ("communicationTest", 11),
          ("missingReferenceTrace", 12),
          ("hardwareProblem", 13),
          ("softwareProblem", 14),
          ("measurementCycle", 15),
          ("alarmOverflow", 16),
          ("genericAlarm", 17),
          ("rebuildClear", 18),
          ("harddiskFailed", 19),
          ("harddiskBackup", 20),
          ("powerfailure", 21),
          ("peak", 22),
          ("referencedrift", 23),
          ("notUsed6", 24),
          ("notUsed7", 25),
          ("notUsed8", 26),
          ("notUsed9", 27),
          ("notUsed10", 28),
          ("notUsed11", 29),
          ("notUsed12", 30))
    )



# MIB Managed Objects in the order of their OIDs

_JdsuOtuObjects_ObjectIdentity = ObjectIdentity
jdsuOtuObjects = _JdsuOtuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1)
)
_JdsuOtuAlarmEvent_ObjectIdentity = ObjectIdentity
jdsuOtuAlarmEvent = _JdsuOtuAlarmEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1)
)
_JdsuOtuAlarmEventEntrySequence_Type = Unsigned32
_JdsuOtuAlarmEventEntrySequence_Object = MibScalar
jdsuOtuAlarmEventEntrySequence = _JdsuOtuAlarmEventEntrySequence_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 1),
    _JdsuOtuAlarmEventEntrySequence_Type()
)
jdsuOtuAlarmEventEntrySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntrySequence.setStatus("current")
_JdsuOtuAlarmEventEntryOtuSerialNumber_Type = DisplayString
_JdsuOtuAlarmEventEntryOtuSerialNumber_Object = MibScalar
jdsuOtuAlarmEventEntryOtuSerialNumber = _JdsuOtuAlarmEventEntryOtuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 2),
    _JdsuOtuAlarmEventEntryOtuSerialNumber_Type()
)
jdsuOtuAlarmEventEntryOtuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryOtuSerialNumber.setStatus("current")
_JdsuOtuAlarmEventEntryTrapData_Type = JdsuOnmsiUtf8String
_JdsuOtuAlarmEventEntryTrapData_Object = MibScalar
jdsuOtuAlarmEventEntryTrapData = _JdsuOtuAlarmEventEntryTrapData_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 3),
    _JdsuOtuAlarmEventEntryTrapData_Type()
)
jdsuOtuAlarmEventEntryTrapData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryTrapData.setStatus("deprecated")
_JdsuOtuAlarmEventEntryAlarmResource_Type = DisplayString
_JdsuOtuAlarmEventEntryAlarmResource_Object = MibScalar
jdsuOtuAlarmEventEntryAlarmResource = _JdsuOtuAlarmEventEntryAlarmResource_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 4),
    _JdsuOtuAlarmEventEntryAlarmResource_Type()
)
jdsuOtuAlarmEventEntryAlarmResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryAlarmResource.setStatus("current")
_JdsuOtuAlarmEventEntryAlarmSpecificProblem_Type = JdsuOtuAlarmSpecificProblem
_JdsuOtuAlarmEventEntryAlarmSpecificProblem_Object = MibScalar
jdsuOtuAlarmEventEntryAlarmSpecificProblem = _JdsuOtuAlarmEventEntryAlarmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 5),
    _JdsuOtuAlarmEventEntryAlarmSpecificProblem_Type()
)
jdsuOtuAlarmEventEntryAlarmSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryAlarmSpecificProblem.setStatus("current")
_JdsuOtuAlarmEventEntryAlarmType_Type = JdsuOtuAlarmType
_JdsuOtuAlarmEventEntryAlarmType_Object = MibScalar
jdsuOtuAlarmEventEntryAlarmType = _JdsuOtuAlarmEventEntryAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 6),
    _JdsuOtuAlarmEventEntryAlarmType_Type()
)
jdsuOtuAlarmEventEntryAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryAlarmType.setStatus("current")
_JdsuOtuAlarmEventEntryAlarmSeverity_Type = JdsuOtuAlarmSeverity
_JdsuOtuAlarmEventEntryAlarmSeverity_Object = MibScalar
jdsuOtuAlarmEventEntryAlarmSeverity = _JdsuOtuAlarmEventEntryAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 7),
    _JdsuOtuAlarmEventEntryAlarmSeverity_Type()
)
jdsuOtuAlarmEventEntryAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryAlarmSeverity.setStatus("current")
_JdsuOtuAlarmEventEntryAlarmTimestamp_Type = DateAndTime
_JdsuOtuAlarmEventEntryAlarmTimestamp_Object = MibScalar
jdsuOtuAlarmEventEntryAlarmTimestamp = _JdsuOtuAlarmEventEntryAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 8),
    _JdsuOtuAlarmEventEntryAlarmTimestamp_Type()
)
jdsuOtuAlarmEventEntryAlarmTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryAlarmTimestamp.setStatus("current")
_JdsuOtuAlarmEventEntryOtuName_Type = DisplayString
_JdsuOtuAlarmEventEntryOtuName_Object = MibScalar
jdsuOtuAlarmEventEntryOtuName = _JdsuOtuAlarmEventEntryOtuName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 9),
    _JdsuOtuAlarmEventEntryOtuName_Type()
)
jdsuOtuAlarmEventEntryOtuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryOtuName.setStatus("current")
_JdsuOtuAlarmEventOpticalAlarmSpecificInfos_ObjectIdentity = ObjectIdentity
jdsuOtuAlarmEventOpticalAlarmSpecificInfos = _JdsuOtuAlarmEventOpticalAlarmSpecificInfos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 10)
)
_JdsuOtuAlarmEventEntryOpticalAlarmLinkName_Type = JdsuOnmsiUtf8String
_JdsuOtuAlarmEventEntryOpticalAlarmLinkName_Object = MibScalar
jdsuOtuAlarmEventEntryOpticalAlarmLinkName = _JdsuOtuAlarmEventEntryOpticalAlarmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 10, 1),
    _JdsuOtuAlarmEventEntryOpticalAlarmLinkName_Type()
)
jdsuOtuAlarmEventEntryOpticalAlarmLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryOpticalAlarmLinkName.setStatus("current")
_JdsuOtuAlarmEventEntryOpticalAlarmSubProblem_Type = JdsuOtuOpticalAlarmSubProblem
_JdsuOtuAlarmEventEntryOpticalAlarmSubProblem_Object = MibScalar
jdsuOtuAlarmEventEntryOpticalAlarmSubProblem = _JdsuOtuAlarmEventEntryOpticalAlarmSubProblem_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 10, 2),
    _JdsuOtuAlarmEventEntryOpticalAlarmSubProblem_Type()
)
jdsuOtuAlarmEventEntryOpticalAlarmSubProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryOpticalAlarmSubProblem.setStatus("current")
_JdsuOtuAlarmEventEntryOpticalAlarmLeveldB_Type = DisplayString
_JdsuOtuAlarmEventEntryOpticalAlarmLeveldB_Object = MibScalar
jdsuOtuAlarmEventEntryOpticalAlarmLeveldB = _JdsuOtuAlarmEventEntryOpticalAlarmLeveldB_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 10, 3),
    _JdsuOtuAlarmEventEntryOpticalAlarmLeveldB_Type()
)
jdsuOtuAlarmEventEntryOpticalAlarmLeveldB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryOpticalAlarmLeveldB.setStatus("current")
_JdsuOtuAlarmEventEntryOpticalAlarmDistanceKm_Type = DisplayString
_JdsuOtuAlarmEventEntryOpticalAlarmDistanceKm_Object = MibScalar
jdsuOtuAlarmEventEntryOpticalAlarmDistanceKm = _JdsuOtuAlarmEventEntryOpticalAlarmDistanceKm_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 10, 4),
    _JdsuOtuAlarmEventEntryOpticalAlarmDistanceKm_Type()
)
jdsuOtuAlarmEventEntryOpticalAlarmDistanceKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryOpticalAlarmDistanceKm.setStatus("current")
_JdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong_Type = DisplayString
_JdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong_Object = MibScalar
jdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong = _JdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 10, 5),
    _JdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong_Type()
)
jdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong.setStatus("current")
_JdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText_Type = DisplayString
_JdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText_Object = MibScalar
jdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText = _JdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 10, 6),
    _JdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText_Type()
)
jdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText.setStatus("current")
_JdsuOtuAlarmEventPeakAlarmSpecificInfos_ObjectIdentity = ObjectIdentity
jdsuOtuAlarmEventPeakAlarmSpecificInfos = _JdsuOtuAlarmEventPeakAlarmSpecificInfos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 11)
)
_JdsuOtuAlarmEventEntryPeakAlarmLinkName_Type = JdsuOnmsiUtf8String
_JdsuOtuAlarmEventEntryPeakAlarmLinkName_Object = MibScalar
jdsuOtuAlarmEventEntryPeakAlarmLinkName = _JdsuOtuAlarmEventEntryPeakAlarmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 11, 1),
    _JdsuOtuAlarmEventEntryPeakAlarmLinkName_Type()
)
jdsuOtuAlarmEventEntryPeakAlarmLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryPeakAlarmLinkName.setStatus("current")
_JdsuOtuAlarmEventEntryPeakAlarmPeakName_Type = JdsuOnmsiUtf8String
_JdsuOtuAlarmEventEntryPeakAlarmPeakName_Object = MibScalar
jdsuOtuAlarmEventEntryPeakAlarmPeakName = _JdsuOtuAlarmEventEntryPeakAlarmPeakName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 11, 2),
    _JdsuOtuAlarmEventEntryPeakAlarmPeakName_Type()
)
jdsuOtuAlarmEventEntryPeakAlarmPeakName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryPeakAlarmPeakName.setStatus("current")
_JdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm_Type = DisplayString
_JdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm_Object = MibScalar
jdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm = _JdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 11, 3),
    _JdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm_Type()
)
jdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm.setStatus("current")
_JdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb_Type = DisplayString
_JdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb_Object = MibScalar
jdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb = _JdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 11, 4),
    _JdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb_Type()
)
jdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb.setStatus("current")
_JdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm_Type = DisplayString
_JdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm_Object = MibScalar
jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm = _JdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 11, 5),
    _JdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm_Type()
)
jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm.setStatus("current")
_JdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb_Type = DisplayString
_JdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb_Object = MibScalar
jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb = _JdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 11, 6),
    _JdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb_Type()
)
jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb.setStatus("current")
_JdsuOtuAlarmEventEntryPeakAlarmGpsLatLong_Type = DisplayString
_JdsuOtuAlarmEventEntryPeakAlarmGpsLatLong_Object = MibScalar
jdsuOtuAlarmEventEntryPeakAlarmGpsLatLong = _JdsuOtuAlarmEventEntryPeakAlarmGpsLatLong_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 1, 11, 7),
    _JdsuOtuAlarmEventEntryPeakAlarmGpsLatLong_Type()
)
jdsuOtuAlarmEventEntryPeakAlarmGpsLatLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventEntryPeakAlarmGpsLatLong.setStatus("current")
_JdsuOtuImAlive_ObjectIdentity = ObjectIdentity
jdsuOtuImAlive = _JdsuOtuImAlive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 2)
)
_JdsuOtuImAliveOtuSerialNumber_Type = DisplayString
_JdsuOtuImAliveOtuSerialNumber_Object = MibScalar
jdsuOtuImAliveOtuSerialNumber = _JdsuOtuImAliveOtuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 2, 1),
    _JdsuOtuImAliveOtuSerialNumber_Type()
)
jdsuOtuImAliveOtuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuImAliveOtuSerialNumber.setStatus("current")
_JdsuOtuImAliveLatestAlarmEventSequence_Type = Unsigned32
_JdsuOtuImAliveLatestAlarmEventSequence_Object = MibScalar
jdsuOtuImAliveLatestAlarmEventSequence = _JdsuOtuImAliveLatestAlarmEventSequence_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 2, 2),
    _JdsuOtuImAliveLatestAlarmEventSequence_Type()
)
jdsuOtuImAliveLatestAlarmEventSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuImAliveLatestAlarmEventSequence.setStatus("current")
_JdsuOtuConfigurationChange_ObjectIdentity = ObjectIdentity
jdsuOtuConfigurationChange = _JdsuOtuConfigurationChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 3)
)
_JdsuOtuConfigurationChangeOtuSerialNumber_Type = DisplayString
_JdsuOtuConfigurationChangeOtuSerialNumber_Object = MibScalar
jdsuOtuConfigurationChangeOtuSerialNumber = _JdsuOtuConfigurationChangeOtuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 3, 1),
    _JdsuOtuConfigurationChangeOtuSerialNumber_Type()
)
jdsuOtuConfigurationChangeOtuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuConfigurationChangeOtuSerialNumber.setStatus("current")
_JdsuOtuConfigurationChangeResource_Type = DisplayString
_JdsuOtuConfigurationChangeResource_Object = MibScalar
jdsuOtuConfigurationChangeResource = _JdsuOtuConfigurationChangeResource_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 3, 2),
    _JdsuOtuConfigurationChangeResource_Type()
)
jdsuOtuConfigurationChangeResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuConfigurationChangeResource.setStatus("current")
_JdsuOtuConfigurationChangeDescription_Type = DisplayString
_JdsuOtuConfigurationChangeDescription_Object = MibScalar
jdsuOtuConfigurationChangeDescription = _JdsuOtuConfigurationChangeDescription_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 3, 3),
    _JdsuOtuConfigurationChangeDescription_Type()
)
jdsuOtuConfigurationChangeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuConfigurationChangeDescription.setStatus("current")
_JdsuOtuDescription_ObjectIdentity = ObjectIdentity
jdsuOtuDescription = _JdsuOtuDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4)
)


class _JdsuOtuManufacturer_Type(DisplayString):
    """Custom type jdsuOtuManufacturer based on DisplayString"""
    defaultValue = OctetString("VIAVI Solutions")


_JdsuOtuManufacturer_Type.__name__ = "DisplayString"
_JdsuOtuManufacturer_Object = MibScalar
jdsuOtuManufacturer = _JdsuOtuManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 1),
    _JdsuOtuManufacturer_Type()
)
jdsuOtuManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuManufacturer.setStatus("current")


class _JdsuOtuModel_Type(DisplayString):
    """Custom type jdsuOtuModel based on DisplayString"""
    defaultValue = OctetString("")


_JdsuOtuModel_Type.__name__ = "DisplayString"
_JdsuOtuModel_Object = MibScalar
jdsuOtuModel = _JdsuOtuModel_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 2),
    _JdsuOtuModel_Type()
)
jdsuOtuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuModel.setStatus("current")


class _JdsuOtuSerialNumber_Type(DisplayString):
    """Custom type jdsuOtuSerialNumber based on DisplayString"""
    defaultValue = OctetString("")


_JdsuOtuSerialNumber_Type.__name__ = "DisplayString"
_JdsuOtuSerialNumber_Object = MibScalar
jdsuOtuSerialNumber = _JdsuOtuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 3),
    _JdsuOtuSerialNumber_Type()
)
jdsuOtuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuSerialNumber.setStatus("current")


class _JdsuOtuOtdrType_Type(DisplayString):
    """Custom type jdsuOtuOtdrType based on DisplayString"""
    defaultValue = OctetString("")


_JdsuOtuOtdrType_Type.__name__ = "DisplayString"
_JdsuOtuOtdrType_Object = MibScalar
jdsuOtuOtdrType = _JdsuOtuOtdrType_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 4),
    _JdsuOtuOtdrType_Type()
)
jdsuOtuOtdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuOtdrType.setStatus("current")


class _JdsuOtuOtdrWavelengths_Type(DisplayString):
    """Custom type jdsuOtuOtdrWavelengths based on DisplayString"""
    defaultValue = OctetString("")


_JdsuOtuOtdrWavelengths_Type.__name__ = "DisplayString"
_JdsuOtuOtdrWavelengths_Object = MibScalar
jdsuOtuOtdrWavelengths = _JdsuOtuOtdrWavelengths_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 5),
    _JdsuOtuOtdrWavelengths_Type()
)
jdsuOtuOtdrWavelengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuOtdrWavelengths.setStatus("current")
_JdsuOtuSwitchPortCount_Type = Unsigned32
_JdsuOtuSwitchPortCount_Object = MibScalar
jdsuOtuSwitchPortCount = _JdsuOtuSwitchPortCount_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 6),
    _JdsuOtuSwitchPortCount_Type()
)
jdsuOtuSwitchPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuSwitchPortCount.setStatus("current")


class _JdsuOtuFirmwareRelease_Type(DisplayString):
    """Custom type jdsuOtuFirmwareRelease based on DisplayString"""
    defaultValue = OctetString("")


_JdsuOtuFirmwareRelease_Type.__name__ = "DisplayString"
_JdsuOtuFirmwareRelease_Object = MibScalar
jdsuOtuFirmwareRelease = _JdsuOtuFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 7),
    _JdsuOtuFirmwareRelease_Type()
)
jdsuOtuFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuFirmwareRelease.setStatus("current")


class _JdsuOtuName_Type(DisplayString):
    """Custom type jdsuOtuName based on DisplayString"""
    defaultValue = OctetString("")


_JdsuOtuName_Type.__name__ = "DisplayString"
_JdsuOtuName_Object = MibScalar
jdsuOtuName = _JdsuOtuName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 8),
    _JdsuOtuName_Type()
)
jdsuOtuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuName.setStatus("current")
_JdsuOtuPortsLinksTable_Object = MibTable
jdsuOtuPortsLinksTable = _JdsuOtuPortsLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 9)
)
if mibBuilder.loadTexts:
    jdsuOtuPortsLinksTable.setStatus("current")
_JdsuOtuPortsLinksEntry_Object = MibTableRow
jdsuOtuPortsLinksEntry = _JdsuOtuPortsLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 9, 1)
)
jdsuOtuPortsLinksEntry.setIndexNames(
    (0, "JDSU-OTU-MIB", "jdsuOtuPortNumber"),
)
if mibBuilder.loadTexts:
    jdsuOtuPortsLinksEntry.setStatus("current")
_JdsuOtuPortNumber_Type = Unsigned32
_JdsuOtuPortNumber_Object = MibTableColumn
jdsuOtuPortNumber = _JdsuOtuPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 9, 1, 1),
    _JdsuOtuPortNumber_Type()
)
jdsuOtuPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuPortNumber.setStatus("current")
_JdsuOtuLinkName_Type = JdsuOnmsiUtf8String
_JdsuOtuLinkName_Object = MibTableColumn
jdsuOtuLinkName = _JdsuOtuLinkName_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 9, 1, 2),
    _JdsuOtuLinkName_Type()
)
jdsuOtuLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuLinkName.setStatus("current")
_JdsuOtuLinkMonitoringStatus_Type = JdsuOtuMonitoringStatus
_JdsuOtuLinkMonitoringStatus_Object = MibTableColumn
jdsuOtuLinkMonitoringStatus = _JdsuOtuLinkMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 9, 1, 3),
    _JdsuOtuLinkMonitoringStatus_Type()
)
jdsuOtuLinkMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuLinkMonitoringStatus.setStatus("current")
_JdsuOtuPortsAlarmsTable_Object = MibTable
jdsuOtuPortsAlarmsTable = _JdsuOtuPortsAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 10)
)
if mibBuilder.loadTexts:
    jdsuOtuPortsAlarmsTable.setStatus("current")
_JdsuOtuPortsAlarmsEntry_Object = MibTableRow
jdsuOtuPortsAlarmsEntry = _JdsuOtuPortsAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 10, 1)
)
jdsuOtuPortsAlarmsEntry.setIndexNames(
    (0, "JDSU-OTU-MIB", "jdsuOtuAlarmPortNumber"),
)
if mibBuilder.loadTexts:
    jdsuOtuPortsAlarmsEntry.setStatus("current")
_JdsuOtuAlarmPortNumber_Type = Unsigned32
_JdsuOtuAlarmPortNumber_Object = MibTableColumn
jdsuOtuAlarmPortNumber = _JdsuOtuAlarmPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 10, 1, 1),
    _JdsuOtuAlarmPortNumber_Type()
)
jdsuOtuAlarmPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuAlarmPortNumber.setStatus("current")
_JdsuOtuPortAlarmSeverity_Type = Unsigned32
_JdsuOtuPortAlarmSeverity_Object = MibTableColumn
jdsuOtuPortAlarmSeverity = _JdsuOtuPortAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 10, 1, 2),
    _JdsuOtuPortAlarmSeverity_Type()
)
jdsuOtuPortAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuPortAlarmSeverity.setStatus("current")
_JdsuOtuPortAlarmType_Type = JdsuOnmsiUtf8String
_JdsuOtuPortAlarmType_Object = MibTableColumn
jdsuOtuPortAlarmType = _JdsuOtuPortAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 10, 1, 3),
    _JdsuOtuPortAlarmType_Type()
)
jdsuOtuPortAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuPortAlarmType.setStatus("current")
_JdsuOtuPortAlarmTimeStamp_Type = Unsigned32
_JdsuOtuPortAlarmTimeStamp_Object = MibTableColumn
jdsuOtuPortAlarmTimeStamp = _JdsuOtuPortAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 10, 1, 4),
    _JdsuOtuPortAlarmTimeStamp_Type()
)
jdsuOtuPortAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuPortAlarmTimeStamp.setStatus("current")
_JdsuOtuPortAlarmDistance_Type = Unsigned32
_JdsuOtuPortAlarmDistance_Object = MibTableColumn
jdsuOtuPortAlarmDistance = _JdsuOtuPortAlarmDistance_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 10, 1, 5),
    _JdsuOtuPortAlarmDistance_Type()
)
jdsuOtuPortAlarmDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuPortAlarmDistance.setStatus("current")
_JdsuOtuPortAlarmProbableCause_Type = JdsuOnmsiUtf8String
_JdsuOtuPortAlarmProbableCause_Object = MibTableColumn
jdsuOtuPortAlarmProbableCause = _JdsuOtuPortAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 4, 10, 1, 6),
    _JdsuOtuPortAlarmProbableCause_Type()
)
jdsuOtuPortAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuPortAlarmProbableCause.setStatus("current")
_JdsuOtuPortTestOnDemand_ObjectIdentity = ObjectIdentity
jdsuOtuPortTestOnDemand = _JdsuOtuPortTestOnDemand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 5)
)
_JdsuOtuStartTestOnDemandOnPort_Type = DisplayString
_JdsuOtuStartTestOnDemandOnPort_Object = MibScalar
jdsuOtuStartTestOnDemandOnPort = _JdsuOtuStartTestOnDemandOnPort_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 5, 1),
    _JdsuOtuStartTestOnDemandOnPort_Type()
)
jdsuOtuStartTestOnDemandOnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jdsuOtuStartTestOnDemandOnPort.setStatus("current")


class _JdsuOtuPortTestOnDemandStatus_Type(DisplayString):
    """Custom type jdsuOtuPortTestOnDemandStatus based on DisplayString"""
    defaultValue = OctetString("NONE")


_JdsuOtuPortTestOnDemandStatus_Type.__name__ = "DisplayString"
_JdsuOtuPortTestOnDemandStatus_Object = MibScalar
jdsuOtuPortTestOnDemandStatus = _JdsuOtuPortTestOnDemandStatus_Object(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 1, 5, 2),
    _JdsuOtuPortTestOnDemandStatus_Type()
)
jdsuOtuPortTestOnDemandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdsuOtuPortTestOnDemandStatus.setStatus("current")
_JdsuOtuTraps_ObjectIdentity = ObjectIdentity
jdsuOtuTraps = _JdsuOtuTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 2)
)
_JdsuOtuConf_ObjectIdentity = ObjectIdentity
jdsuOtuConf = _JdsuOtuConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 3)
)

# Managed Objects groups

jdsuOtuObjectsConf = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 3, 1)
)
jdsuOtuObjectsConf.setObjects(
      *(("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntrySequence"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOtuSerialNumber"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryTrapData"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryAlarmResource"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryAlarmSpecificProblem"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryAlarmType"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryAlarmSeverity"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryAlarmTimestamp"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOtuName"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmLinkName"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmSubProblem"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmLeveldB"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmDistanceKm"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText"),
        ("JDSU-OTU-MIB", "jdsuOtuImAliveOtuSerialNumber"),
        ("JDSU-OTU-MIB", "jdsuOtuImAliveLatestAlarmEventSequence"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmLinkName"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmPeakName"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmGpsLatLong"),
        ("JDSU-OTU-MIB", "jdsuOtuConfigurationChangeOtuSerialNumber"),
        ("JDSU-OTU-MIB", "jdsuOtuConfigurationChangeResource"),
        ("JDSU-OTU-MIB", "jdsuOtuConfigurationChangeDescription"),
        ("JDSU-OTU-MIB", "jdsuOtuManufacturer"),
        ("JDSU-OTU-MIB", "jdsuOtuModel"),
        ("JDSU-OTU-MIB", "jdsuOtuSerialNumber"),
        ("JDSU-OTU-MIB", "jdsuOtuOtdrType"),
        ("JDSU-OTU-MIB", "jdsuOtuOtdrWavelengths"),
        ("JDSU-OTU-MIB", "jdsuOtuSwitchPortCount"),
        ("JDSU-OTU-MIB", "jdsuOtuFirmwareRelease"),
        ("JDSU-OTU-MIB", "jdsuOtuName"),
        ("JDSU-OTU-MIB", "jdsuOtuPortNumber"),
        ("JDSU-OTU-MIB", "jdsuOtuLinkName"),
        ("JDSU-OTU-MIB", "jdsuOtuLinkMonitoringStatus"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmPortNumber"),
        ("JDSU-OTU-MIB", "jdsuOtuPortAlarmSeverity"),
        ("JDSU-OTU-MIB", "jdsuOtuPortAlarmType"),
        ("JDSU-OTU-MIB", "jdsuOtuPortAlarmTimeStamp"),
        ("JDSU-OTU-MIB", "jdsuOtuPortAlarmDistance"),
        ("JDSU-OTU-MIB", "jdsuOtuPortAlarmProbableCause"),
        ("JDSU-OTU-MIB", "jdsuOtuStartTestOnDemandOnPort"),
        ("JDSU-OTU-MIB", "jdsuOtuPortTestOnDemandStatus"))
)
if mibBuilder.loadTexts:
    jdsuOtuObjectsConf.setStatus("current")


# Notification objects

jdsuOtuAlarmEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 2, 1)
)
jdsuOtuAlarmEventTrap.setObjects(
      *(("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntrySequence"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOtuSerialNumber"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryTrapData"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryAlarmSpecificProblem"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryAlarmResource"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryAlarmType"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryAlarmSeverity"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryAlarmTimestamp"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOtuName"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmLinkName"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmSubProblem"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmLeveldB"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmDistanceKm"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmLinkName"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmPeakName"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb"),
        ("JDSU-OTU-MIB", "jdsuOtuAlarmEventEntryPeakAlarmGpsLatLong"))
)
if mibBuilder.loadTexts:
    jdsuOtuAlarmEventTrap.setStatus(
        "current"
    )

jdsuOtuImAliveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 2, 2)
)
jdsuOtuImAliveTrap.setObjects(
      *(("JDSU-OTU-MIB", "jdsuOtuImAliveOtuSerialNumber"),
        ("JDSU-OTU-MIB", "jdsuOtuImAliveLatestAlarmEventSequence"))
)
if mibBuilder.loadTexts:
    jdsuOtuImAliveTrap.setStatus(
        "current"
    )

jdsuOtuConfigurationChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 2, 3)
)
jdsuOtuConfigurationChangeTrap.setObjects(
      *(("JDSU-OTU-MIB", "jdsuOtuConfigurationChangeOtuSerialNumber"),
        ("JDSU-OTU-MIB", "jdsuOtuConfigurationChangeResource"),
        ("JDSU-OTU-MIB", "jdsuOtuConfigurationChangeDescription"))
)
if mibBuilder.loadTexts:
    jdsuOtuConfigurationChangeTrap.setStatus(
        "current"
    )


# Notifications groups

jdsuOtuTrapsConf = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2, 1, 3, 2)
)
jdsuOtuTrapsConf.setObjects(
      *(("JDSU-OTU-MIB", "jdsuOtuAlarmEventTrap"),
        ("JDSU-OTU-MIB", "jdsuOtuImAliveTrap"),
        ("JDSU-OTU-MIB", "jdsuOtuConfigurationChangeTrap"))
)
if mibBuilder.loadTexts:
    jdsuOtuTrapsConf.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JDSU-OTU-MIB",
    **{"JdsuOnmsiUtf8String": JdsuOnmsiUtf8String,
       "JdsuOtuAlarmSeverity": JdsuOtuAlarmSeverity,
       "JdsuOtuAlarmType": JdsuOtuAlarmType,
       "JdsuOtuMonitoringStatus": JdsuOtuMonitoringStatus,
       "JdsuOtuOpticalAlarmSubProblem": JdsuOtuOpticalAlarmSubProblem,
       "JdsuOtuAlarmSpecificProblem": JdsuOtuAlarmSpecificProblem,
       "jdsuOtuMib": jdsuOtuMib,
       "jdsuOtuObjects": jdsuOtuObjects,
       "jdsuOtuAlarmEvent": jdsuOtuAlarmEvent,
       "jdsuOtuAlarmEventEntrySequence": jdsuOtuAlarmEventEntrySequence,
       "jdsuOtuAlarmEventEntryOtuSerialNumber": jdsuOtuAlarmEventEntryOtuSerialNumber,
       "jdsuOtuAlarmEventEntryTrapData": jdsuOtuAlarmEventEntryTrapData,
       "jdsuOtuAlarmEventEntryAlarmResource": jdsuOtuAlarmEventEntryAlarmResource,
       "jdsuOtuAlarmEventEntryAlarmSpecificProblem": jdsuOtuAlarmEventEntryAlarmSpecificProblem,
       "jdsuOtuAlarmEventEntryAlarmType": jdsuOtuAlarmEventEntryAlarmType,
       "jdsuOtuAlarmEventEntryAlarmSeverity": jdsuOtuAlarmEventEntryAlarmSeverity,
       "jdsuOtuAlarmEventEntryAlarmTimestamp": jdsuOtuAlarmEventEntryAlarmTimestamp,
       "jdsuOtuAlarmEventEntryOtuName": jdsuOtuAlarmEventEntryOtuName,
       "jdsuOtuAlarmEventOpticalAlarmSpecificInfos": jdsuOtuAlarmEventOpticalAlarmSpecificInfos,
       "jdsuOtuAlarmEventEntryOpticalAlarmLinkName": jdsuOtuAlarmEventEntryOpticalAlarmLinkName,
       "jdsuOtuAlarmEventEntryOpticalAlarmSubProblem": jdsuOtuAlarmEventEntryOpticalAlarmSubProblem,
       "jdsuOtuAlarmEventEntryOpticalAlarmLeveldB": jdsuOtuAlarmEventEntryOpticalAlarmLeveldB,
       "jdsuOtuAlarmEventEntryOpticalAlarmDistanceKm": jdsuOtuAlarmEventEntryOpticalAlarmDistanceKm,
       "jdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong": jdsuOtuAlarmEventEntryOpticalAlarmGpsLatLong,
       "jdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText": jdsuOtuAlarmEventEntryOpticalAlarmProbableCauseText,
       "jdsuOtuAlarmEventPeakAlarmSpecificInfos": jdsuOtuAlarmEventPeakAlarmSpecificInfos,
       "jdsuOtuAlarmEventEntryPeakAlarmLinkName": jdsuOtuAlarmEventEntryPeakAlarmLinkName,
       "jdsuOtuAlarmEventEntryPeakAlarmPeakName": jdsuOtuAlarmEventEntryPeakAlarmPeakName,
       "jdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm": jdsuOtuAlarmEventEntryPeakAlarmReferenceTopDistanceKm,
       "jdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb": jdsuOtuAlarmEventEntryPeakAlarmReferenceTopLevelDb,
       "jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm": jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopDistanceKm,
       "jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb": jdsuOtuAlarmEventEntryPeakAlarmMeasuredTopLevelDb,
       "jdsuOtuAlarmEventEntryPeakAlarmGpsLatLong": jdsuOtuAlarmEventEntryPeakAlarmGpsLatLong,
       "jdsuOtuImAlive": jdsuOtuImAlive,
       "jdsuOtuImAliveOtuSerialNumber": jdsuOtuImAliveOtuSerialNumber,
       "jdsuOtuImAliveLatestAlarmEventSequence": jdsuOtuImAliveLatestAlarmEventSequence,
       "jdsuOtuConfigurationChange": jdsuOtuConfigurationChange,
       "jdsuOtuConfigurationChangeOtuSerialNumber": jdsuOtuConfigurationChangeOtuSerialNumber,
       "jdsuOtuConfigurationChangeResource": jdsuOtuConfigurationChangeResource,
       "jdsuOtuConfigurationChangeDescription": jdsuOtuConfigurationChangeDescription,
       "jdsuOtuDescription": jdsuOtuDescription,
       "jdsuOtuManufacturer": jdsuOtuManufacturer,
       "jdsuOtuModel": jdsuOtuModel,
       "jdsuOtuSerialNumber": jdsuOtuSerialNumber,
       "jdsuOtuOtdrType": jdsuOtuOtdrType,
       "jdsuOtuOtdrWavelengths": jdsuOtuOtdrWavelengths,
       "jdsuOtuSwitchPortCount": jdsuOtuSwitchPortCount,
       "jdsuOtuFirmwareRelease": jdsuOtuFirmwareRelease,
       "jdsuOtuName": jdsuOtuName,
       "jdsuOtuPortsLinksTable": jdsuOtuPortsLinksTable,
       "jdsuOtuPortsLinksEntry": jdsuOtuPortsLinksEntry,
       "jdsuOtuPortNumber": jdsuOtuPortNumber,
       "jdsuOtuLinkName": jdsuOtuLinkName,
       "jdsuOtuLinkMonitoringStatus": jdsuOtuLinkMonitoringStatus,
       "jdsuOtuPortsAlarmsTable": jdsuOtuPortsAlarmsTable,
       "jdsuOtuPortsAlarmsEntry": jdsuOtuPortsAlarmsEntry,
       "jdsuOtuAlarmPortNumber": jdsuOtuAlarmPortNumber,
       "jdsuOtuPortAlarmSeverity": jdsuOtuPortAlarmSeverity,
       "jdsuOtuPortAlarmType": jdsuOtuPortAlarmType,
       "jdsuOtuPortAlarmTimeStamp": jdsuOtuPortAlarmTimeStamp,
       "jdsuOtuPortAlarmDistance": jdsuOtuPortAlarmDistance,
       "jdsuOtuPortAlarmProbableCause": jdsuOtuPortAlarmProbableCause,
       "jdsuOtuPortTestOnDemand": jdsuOtuPortTestOnDemand,
       "jdsuOtuStartTestOnDemandOnPort": jdsuOtuStartTestOnDemandOnPort,
       "jdsuOtuPortTestOnDemandStatus": jdsuOtuPortTestOnDemandStatus,
       "jdsuOtuTraps": jdsuOtuTraps,
       "jdsuOtuAlarmEventTrap": jdsuOtuAlarmEventTrap,
       "jdsuOtuImAliveTrap": jdsuOtuImAliveTrap,
       "jdsuOtuConfigurationChangeTrap": jdsuOtuConfigurationChangeTrap,
       "jdsuOtuConf": jdsuOtuConf,
       "jdsuOtuObjectsConf": jdsuOtuObjectsConf,
       "jdsuOtuTrapsConf": jdsuOtuTrapsConf}
)
