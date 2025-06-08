# SNMP MIB module (ADVA-FSPR7-CFM-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/ADVA-FSPR7-CFM-EXTENSION-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:56 2025
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

(ServiceImpairment,
 TrapAlarmSeverity,
 fspR7,
 neEventLogIdentityTranslation,
 neEventLogTimeStamp) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "ServiceImpairment",
    "TrapAlarmSeverity",
    "fspR7",
    "neEventLogIdentityTranslation",
    "neEventLogTimeStamp")

(flowEntityIndexEth,
 flowEntityIndexFlow) = mibBuilder.importSymbols(
    "FspR7-LAYER2-MIB",
    "flowEntityIndexEth",
    "flowEntityIndexFlow")

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

cfmExtensionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6)
)
if mibBuilder.loadTexts:
    cfmExtensionMIB.setRevisions(
        ("2011-02-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CfmAlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              13000,
              13001,
              13002,
              13003,
              13004,
              13005,
              13006,
              13007,
              13008,
              13009,
              13010)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("cfmOosDisabled", 13000),
          ("cfmOosManagement", 13001),
          ("cfmOosMaintenance", 13002),
          ("cfmOosAins", 13003),
          ("cfmPriVidNotEqualExtVid", 13004),
          ("cfmServerSignalFailure", 13005),
          ("cfmRemoteDefectIndication", 13006),
          ("cfmCcmMacStatus", 13007),
          ("cfmCcmError", 13008),
          ("cfmCcmLost", 13009),
          ("cfmCcmXConn", 13010))
    )



# MIB Managed Objects in the order of their OIDs

_CfmAlarmMIB_ObjectIdentity = ObjectIdentity
cfmAlarmMIB = _CfmAlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1)
)
_CfmAlarmObjects_ObjectIdentity = ObjectIdentity
cfmAlarmObjects = _CfmAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1)
)
_MepAlarmSeverityTable_Object = MibTable
mepAlarmSeverityTable = _MepAlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10)
)
if mibBuilder.loadTexts:
    mepAlarmSeverityTable.setStatus("current")
_MepAlarmSeverityEntry_Object = MibTableRow
mepAlarmSeverityEntry = _MepAlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1)
)
mepAlarmSeverityEntry.setIndexNames(
    (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityMdIndex"),
    (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityMaNetIndex"),
    (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityMepIdentifier"),
    (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityType"),
)
if mibBuilder.loadTexts:
    mepAlarmSeverityEntry.setStatus("current")
_MepAlarmSeverityMdIndex_Type = Unsigned32
_MepAlarmSeverityMdIndex_Object = MibTableColumn
mepAlarmSeverityMdIndex = _MepAlarmSeverityMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 1),
    _MepAlarmSeverityMdIndex_Type()
)
mepAlarmSeverityMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mepAlarmSeverityMdIndex.setStatus("current")
_MepAlarmSeverityMaNetIndex_Type = Unsigned32
_MepAlarmSeverityMaNetIndex_Object = MibTableColumn
mepAlarmSeverityMaNetIndex = _MepAlarmSeverityMaNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 2),
    _MepAlarmSeverityMaNetIndex_Type()
)
mepAlarmSeverityMaNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mepAlarmSeverityMaNetIndex.setStatus("current")
_MepAlarmSeverityMepIdentifier_Type = Unsigned32
_MepAlarmSeverityMepIdentifier_Object = MibTableColumn
mepAlarmSeverityMepIdentifier = _MepAlarmSeverityMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 3),
    _MepAlarmSeverityMepIdentifier_Type()
)
mepAlarmSeverityMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mepAlarmSeverityMepIdentifier.setStatus("current")
_MepAlarmSeverityType_Type = CfmAlarmType
_MepAlarmSeverityType_Object = MibTableColumn
mepAlarmSeverityType = _MepAlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 4),
    _MepAlarmSeverityType_Type()
)
mepAlarmSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mepAlarmSeverityType.setStatus("current")
_MepAlarmSeverityValue_Type = TrapAlarmSeverity
_MepAlarmSeverityValue_Object = MibTableColumn
mepAlarmSeverityValue = _MepAlarmSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 10, 1, 5),
    _MepAlarmSeverityValue_Type()
)
mepAlarmSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepAlarmSeverityValue.setStatus("current")
_MepAlarmTable_Object = MibTable
mepAlarmTable = _MepAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11)
)
if mibBuilder.loadTexts:
    mepAlarmTable.setStatus("current")
_MepAlarmEntry_Object = MibTableRow
mepAlarmEntry = _MepAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1)
)
mepAlarmEntry.setIndexNames(
    (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmMdIndex"),
    (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmMaNetIndex"),
    (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmMepIdentifier"),
    (0, "ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmType"),
)
if mibBuilder.loadTexts:
    mepAlarmEntry.setStatus("current")
_MepAlarmMdIndex_Type = Unsigned32
_MepAlarmMdIndex_Object = MibTableColumn
mepAlarmMdIndex = _MepAlarmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 1),
    _MepAlarmMdIndex_Type()
)
mepAlarmMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mepAlarmMdIndex.setStatus("current")
_MepAlarmMaNetIndex_Type = Unsigned32
_MepAlarmMaNetIndex_Object = MibTableColumn
mepAlarmMaNetIndex = _MepAlarmMaNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 2),
    _MepAlarmMaNetIndex_Type()
)
mepAlarmMaNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mepAlarmMaNetIndex.setStatus("current")
_MepAlarmMepIdentifier_Type = Unsigned32
_MepAlarmMepIdentifier_Object = MibTableColumn
mepAlarmMepIdentifier = _MepAlarmMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 3),
    _MepAlarmMepIdentifier_Type()
)
mepAlarmMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mepAlarmMepIdentifier.setStatus("current")
_MepAlarmType_Type = CfmAlarmType
_MepAlarmType_Object = MibTableColumn
mepAlarmType = _MepAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 4),
    _MepAlarmType_Type()
)
mepAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mepAlarmType.setStatus("current")
_MepAlarmSeverity_Type = TrapAlarmSeverity
_MepAlarmSeverity_Object = MibTableColumn
mepAlarmSeverity = _MepAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 5),
    _MepAlarmSeverity_Type()
)
mepAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mepAlarmSeverity.setStatus("current")
_MepAlarmAffect_Type = ServiceImpairment
_MepAlarmAffect_Object = MibTableColumn
mepAlarmAffect = _MepAlarmAffect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 6),
    _MepAlarmAffect_Type()
)
mepAlarmAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mepAlarmAffect.setStatus("current")
_MepAlarmTimeStamp_Type = DateAndTime
_MepAlarmTimeStamp_Object = MibTableColumn
mepAlarmTimeStamp = _MepAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 1, 11, 1, 7),
    _MepAlarmTimeStamp_Type()
)
mepAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mepAlarmTimeStamp.setStatus("current")
_CfmAlarms_ObjectIdentity = ObjectIdentity
cfmAlarms = _CfmAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2)
)
_CfmAlarmsPrefix_ObjectIdentity = ObjectIdentity
cfmAlarmsPrefix = _CfmAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0)
)
_CfmStatusMIB_ObjectIdentity = ObjectIdentity
cfmStatusMIB = _CfmStatusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2)
)
_CfmExtensionMIBConformance_ObjectIdentity = ObjectIdentity
cfmExtensionMIBConformance = _CfmExtensionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2)
)
_CfmStatus_ObjectIdentity = ObjectIdentity
cfmStatus = _CfmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1)
)
_CfmExtensionMIBCompliances_ObjectIdentity = ObjectIdentity
cfmExtensionMIBCompliances = _CfmExtensionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1)
)
_MepOnFlowTable_Object = MibTable
mepOnFlowTable = _MepOnFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mepOnFlowTable.setStatus("current")
_MepOnFlowEntry_Object = MibTableRow
mepOnFlowEntry = _MepOnFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1, 1, 1)
)
mepOnFlowEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    mepOnFlowEntry.setStatus("current")
_MepOnFlowMepString_Type = SnmpAdminString
_MepOnFlowMepString_Object = MibTableColumn
mepOnFlowMepString = _MepOnFlowMepString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1, 1, 1, 1),
    _MepOnFlowMepString_Type()
)
mepOnFlowMepString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mepOnFlowMepString.setStatus("current")
_CfmExtensionMIBGroups_ObjectIdentity = ObjectIdentity
cfmExtensionMIBGroups = _CfmExtensionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 2)
)

# Managed Objects groups

cfmExtensionObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 2, 1)
)
cfmExtensionObjectGroup.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverityValue"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmTimeStamp"))
)
if mibBuilder.loadTexts:
    cfmExtensionObjectGroup.setStatus("current")


# Notification objects

alarmCfmOosDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13000)
)
alarmCfmOosDisabled.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmOosDisabled.setStatus(
        "current"
    )

alarmCfmOosManagement = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13001)
)
alarmCfmOosManagement.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmOosManagement.setStatus(
        "current"
    )

alarmCfmOosMaintenance = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13002)
)
alarmCfmOosMaintenance.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmOosMaintenance.setStatus(
        "current"
    )

alarmCfmOosAins = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13003)
)
alarmCfmOosAins.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmOosAins.setStatus(
        "current"
    )

alarmCfmPriVidNotEqualExtVid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13004)
)
alarmCfmPriVidNotEqualExtVid.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmPriVidNotEqualExtVid.setStatus(
        "current"
    )

alarmCfmServerSignalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13005)
)
alarmCfmServerSignalFailure.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmServerSignalFailure.setStatus(
        "current"
    )

alarmCfmRemoteDefectIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13006)
)
alarmCfmRemoteDefectIndication.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmRemoteDefectIndication.setStatus(
        "current"
    )

alarmCfmCcmMacStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13007)
)
alarmCfmCcmMacStatus.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmCcmMacStatus.setStatus(
        "current"
    )

alarmCfmCcmError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13008)
)
alarmCfmCcmError.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmCcmError.setStatus(
        "current"
    )

alarmCfmCcmLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13009)
)
alarmCfmCcmLost.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmCcmLost.setStatus(
        "current"
    )

alarmCfmCcmXConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 1, 2, 0, 13010)
)
alarmCfmCcmXConn.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmSeverity"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "mepAlarmAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmCfmCcmXConn.setStatus(
        "current"
    )


# Notifications groups

cfmExtensionNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 2, 2)
)
cfmExtensionNotificationGroup.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosDisabled"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosManagement"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosMaintenance"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmOosAins"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmPriVidNotEqualExtVid"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmServerSignalFailure"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmRemoteDefectIndication"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmMacStatus"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmError"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmLost"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "alarmCfmCcmXConn"))
)
if mibBuilder.loadTexts:
    cfmExtensionNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cfmExtensionMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 6, 2, 1, 1)
)
cfmExtensionMIBCompliance.setObjects(
      *(("ADVA-FSPR7-CFM-EXTENSION-MIB", "cfmExtensionObjectGroup"),
        ("ADVA-FSPR7-CFM-EXTENSION-MIB", "cfmExtensionNotificationGroup"))
)
if mibBuilder.loadTexts:
    cfmExtensionMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVA-FSPR7-CFM-EXTENSION-MIB",
    **{"CfmAlarmType": CfmAlarmType,
       "cfmExtensionMIB": cfmExtensionMIB,
       "cfmAlarmMIB": cfmAlarmMIB,
       "cfmAlarmObjects": cfmAlarmObjects,
       "mepAlarmSeverityTable": mepAlarmSeverityTable,
       "mepAlarmSeverityEntry": mepAlarmSeverityEntry,
       "mepAlarmSeverityMdIndex": mepAlarmSeverityMdIndex,
       "mepAlarmSeverityMaNetIndex": mepAlarmSeverityMaNetIndex,
       "mepAlarmSeverityMepIdentifier": mepAlarmSeverityMepIdentifier,
       "mepAlarmSeverityType": mepAlarmSeverityType,
       "mepAlarmSeverityValue": mepAlarmSeverityValue,
       "mepAlarmTable": mepAlarmTable,
       "mepAlarmEntry": mepAlarmEntry,
       "mepAlarmMdIndex": mepAlarmMdIndex,
       "mepAlarmMaNetIndex": mepAlarmMaNetIndex,
       "mepAlarmMepIdentifier": mepAlarmMepIdentifier,
       "mepAlarmType": mepAlarmType,
       "mepAlarmSeverity": mepAlarmSeverity,
       "mepAlarmAffect": mepAlarmAffect,
       "mepAlarmTimeStamp": mepAlarmTimeStamp,
       "cfmAlarms": cfmAlarms,
       "cfmAlarmsPrefix": cfmAlarmsPrefix,
       "alarmCfmOosDisabled": alarmCfmOosDisabled,
       "alarmCfmOosManagement": alarmCfmOosManagement,
       "alarmCfmOosMaintenance": alarmCfmOosMaintenance,
       "alarmCfmOosAins": alarmCfmOosAins,
       "alarmCfmPriVidNotEqualExtVid": alarmCfmPriVidNotEqualExtVid,
       "alarmCfmServerSignalFailure": alarmCfmServerSignalFailure,
       "alarmCfmRemoteDefectIndication": alarmCfmRemoteDefectIndication,
       "alarmCfmCcmMacStatus": alarmCfmCcmMacStatus,
       "alarmCfmCcmError": alarmCfmCcmError,
       "alarmCfmCcmLost": alarmCfmCcmLost,
       "alarmCfmCcmXConn": alarmCfmCcmXConn,
       "cfmStatusMIB": cfmStatusMIB,
       "cfmExtensionMIBConformance": cfmExtensionMIBConformance,
       "cfmStatus": cfmStatus,
       "cfmExtensionMIBCompliances": cfmExtensionMIBCompliances,
       "mepOnFlowTable": mepOnFlowTable,
       "cfmExtensionMIBCompliance": cfmExtensionMIBCompliance,
       "mepOnFlowEntry": mepOnFlowEntry,
       "mepOnFlowMepString": mepOnFlowMepString,
       "cfmExtensionMIBGroups": cfmExtensionMIBGroups,
       "cfmExtensionObjectGroup": cfmExtensionObjectGroup,
       "cfmExtensionNotificationGroup": cfmExtensionNotificationGroup}
)
