# SNMP MIB module (CISCO-SAA-APM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SAA-APM-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:57 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSaaApmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 177)
)
if mibBuilder.loadTexts:
    ciscoSaaApmMIB.setRevisions(
        ("2000-10-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SaaApmOperErrorCode(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("ftpDnldErr", 2),
          ("targetDown", 3),
          ("scriptErr", 4),
          ("socketErr", 5),
          ("internalErr", 6),
          ("digestErr", 7),
          ("fileHeaderErr", 8),
          ("fileFormatErr", 9),
          ("cacheFull", 10),
          ("lowMem", 11))
    )



class SaaApmDataTransErrorCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("ftpErr", 2),
          ("timeoutErr", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSaaApmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSaaApmMIBObjects = _CiscoSaaApmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1)
)
_SaaApmAppl_ObjectIdentity = ObjectIdentity
saaApmAppl = _SaaApmAppl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 1)
)


class _SaaApmApplMajorVersion_Type(Integer32):
    """Custom type saaApmApplMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SaaApmApplMajorVersion_Type.__name__ = "Integer32"
_SaaApmApplMajorVersion_Object = MibScalar
saaApmApplMajorVersion = _SaaApmApplMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 1, 1),
    _SaaApmApplMajorVersion_Type()
)
saaApmApplMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saaApmApplMajorVersion.setStatus("current")


class _SaaApmApplMinorVersion_Type(Integer32):
    """Custom type saaApmApplMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SaaApmApplMinorVersion_Type.__name__ = "Integer32"
_SaaApmApplMinorVersion_Object = MibScalar
saaApmApplMinorVersion = _SaaApmApplMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 1, 2),
    _SaaApmApplMinorVersion_Type()
)
saaApmApplMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saaApmApplMinorVersion.setStatus("current")


class _SaaApmApplMaxOper_Type(Integer32):
    """Custom type saaApmApplMaxOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SaaApmApplMaxOper_Type.__name__ = "Integer32"
_SaaApmApplMaxOper_Object = MibScalar
saaApmApplMaxOper = _SaaApmApplMaxOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 1, 3),
    _SaaApmApplMaxOper_Type()
)
saaApmApplMaxOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saaApmApplMaxOper.setStatus("current")


class _SaaApmApplFreeMemLowWaterMark_Type(Integer32):
    """Custom type saaApmApplFreeMemLowWaterMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SaaApmApplFreeMemLowWaterMark_Type.__name__ = "Integer32"
_SaaApmApplFreeMemLowWaterMark_Object = MibScalar
saaApmApplFreeMemLowWaterMark = _SaaApmApplFreeMemLowWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 1, 4),
    _SaaApmApplFreeMemLowWaterMark_Type()
)
saaApmApplFreeMemLowWaterMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saaApmApplFreeMemLowWaterMark.setStatus("current")
if mibBuilder.loadTexts:
    saaApmApplFreeMemLowWaterMark.setUnits("bytes")


class _SaaApmApplOperCapacity_Type(Gauge32):
    """Custom type saaApmApplOperCapacity based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SaaApmApplOperCapacity_Type.__name__ = "Gauge32"
_SaaApmApplOperCapacity_Object = MibScalar
saaApmApplOperCapacity = _SaaApmApplOperCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 1, 5),
    _SaaApmApplOperCapacity_Type()
)
saaApmApplOperCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saaApmApplOperCapacity.setStatus("current")
_SaaApmCtrl_ObjectIdentity = ObjectIdentity
saaApmCtrl = _SaaApmCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2)
)
_SaaApmCtrlTable_Object = MibTable
saaApmCtrlTable = _SaaApmCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2, 1)
)
if mibBuilder.loadTexts:
    saaApmCtrlTable.setStatus("current")
_SaaApmCtrlEntry_Object = MibTableRow
saaApmCtrlEntry = _SaaApmCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2, 1, 1)
)
saaApmCtrlEntry.setIndexNames(
    (0, "CISCO-SAA-APM-MIB", "saaApmCtrlIndex"),
)
if mibBuilder.loadTexts:
    saaApmCtrlEntry.setStatus("current")


class _SaaApmCtrlIndex_Type(Integer32):
    """Custom type saaApmCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SaaApmCtrlIndex_Type.__name__ = "Integer32"
_SaaApmCtrlIndex_Object = MibTableColumn
saaApmCtrlIndex = _SaaApmCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2, 1, 1, 1),
    _SaaApmCtrlIndex_Type()
)
saaApmCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saaApmCtrlIndex.setStatus("current")
_SaaApmCtrlScriptCfgURL_Type = SnmpAdminString
_SaaApmCtrlScriptCfgURL_Object = MibTableColumn
saaApmCtrlScriptCfgURL = _SaaApmCtrlScriptCfgURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2, 1, 1, 2),
    _SaaApmCtrlScriptCfgURL_Type()
)
saaApmCtrlScriptCfgURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saaApmCtrlScriptCfgURL.setStatus("current")


class _SaaApmCtrlOwner_Type(OwnerString):
    """Custom type saaApmCtrlOwner based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SaaApmCtrlOwner_Type.__name__ = "OwnerString"
_SaaApmCtrlOwner_Object = MibTableColumn
saaApmCtrlOwner = _SaaApmCtrlOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2, 1, 1, 3),
    _SaaApmCtrlOwner_Type()
)
saaApmCtrlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saaApmCtrlOwner.setStatus("current")


class _SaaApmCtrlInitDataTrans_Type(TruthValue):
    """Custom type saaApmCtrlInitDataTrans based on TruthValue"""
    defaultValue = 2


_SaaApmCtrlInitDataTrans_Type.__name__ = "TruthValue"
_SaaApmCtrlInitDataTrans_Object = MibTableColumn
saaApmCtrlInitDataTrans = _SaaApmCtrlInitDataTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2, 1, 1, 4),
    _SaaApmCtrlInitDataTrans_Type()
)
saaApmCtrlInitDataTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saaApmCtrlInitDataTrans.setStatus("current")
_SaaApmCtrlDataTransTime_Type = TimeStamp
_SaaApmCtrlDataTransTime_Object = MibTableColumn
saaApmCtrlDataTransTime = _SaaApmCtrlDataTransTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2, 1, 1, 5),
    _SaaApmCtrlDataTransTime_Type()
)
saaApmCtrlDataTransTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saaApmCtrlDataTransTime.setStatus("current")
_SaaApmCtrlDataTransStatus_Type = SaaApmDataTransErrorCode
_SaaApmCtrlDataTransStatus_Object = MibTableColumn
saaApmCtrlDataTransStatus = _SaaApmCtrlDataTransStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2, 1, 1, 6),
    _SaaApmCtrlDataTransStatus_Type()
)
saaApmCtrlDataTransStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saaApmCtrlDataTransStatus.setStatus("current")
_SaaApmCtrlStatus_Type = RowStatus
_SaaApmCtrlStatus_Object = MibTableColumn
saaApmCtrlStatus = _SaaApmCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2, 1, 1, 7),
    _SaaApmCtrlStatus_Type()
)
saaApmCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saaApmCtrlStatus.setStatus("current")


class _SaaApmCtrlNvgen_Type(TruthValue):
    """Custom type saaApmCtrlNvgen based on TruthValue"""
    defaultValue = 2


_SaaApmCtrlNvgen_Type.__name__ = "TruthValue"
_SaaApmCtrlNvgen_Object = MibTableColumn
saaApmCtrlNvgen = _SaaApmCtrlNvgen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 2, 1, 1, 8),
    _SaaApmCtrlNvgen_Type()
)
saaApmCtrlNvgen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saaApmCtrlNvgen.setStatus("current")
_SaaApmOper_ObjectIdentity = ObjectIdentity
saaApmOper = _SaaApmOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 3)
)
_SaaApmOperTable_Object = MibTable
saaApmOperTable = _SaaApmOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 3, 1)
)
if mibBuilder.loadTexts:
    saaApmOperTable.setStatus("current")
_SaaApmOperEntry_Object = MibTableRow
saaApmOperEntry = _SaaApmOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    saaApmOperEntry.setStatus("current")
_SaaApmOperLastStartTime_Type = TimeStamp
_SaaApmOperLastStartTime_Object = MibTableColumn
saaApmOperLastStartTime = _SaaApmOperLastStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 3, 1, 1, 1),
    _SaaApmOperLastStartTime_Type()
)
saaApmOperLastStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saaApmOperLastStartTime.setStatus("current")
_SaaApmOperLastEndTime_Type = TimeStamp
_SaaApmOperLastEndTime_Object = MibTableColumn
saaApmOperLastEndTime = _SaaApmOperLastEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 3, 1, 1, 2),
    _SaaApmOperLastEndTime_Type()
)
saaApmOperLastEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saaApmOperLastEndTime.setStatus("current")
_SaaApmOperLastStatus_Type = SaaApmOperErrorCode
_SaaApmOperLastStatus_Object = MibTableColumn
saaApmOperLastStatus = _SaaApmOperLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 1, 3, 1, 1, 3),
    _SaaApmOperLastStatus_Type()
)
saaApmOperLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saaApmOperLastStatus.setStatus("current")
_CiscoSaaApmMIBNotifPrefix_ObjectIdentity = ObjectIdentity
ciscoSaaApmMIBNotifPrefix = _CiscoSaaApmMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 2)
)
_CiscoSaaApmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSaaApmMIBNotifs = _CiscoSaaApmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 2, 0)
)
_CiscoSaaApmMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSaaApmMIBConformance = _CiscoSaaApmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 3)
)
_CiscoSaaApmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSaaApmMIBCompliances = _CiscoSaaApmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 3, 1)
)
_CiscoSaaApmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSaaApmMIBGroups = _CiscoSaaApmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 3, 2)
)
saaApmCtrlEntry.registerAugmentions(
    ("CISCO-SAA-APM-MIB",
     "saaApmOperEntry")
)
saaApmOperEntry.setIndexNames(*saaApmCtrlEntry.getIndexNames())

# Managed Objects groups

ciscoSaaApmApplGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 3, 2, 1)
)
ciscoSaaApmApplGroup.setObjects(
      *(("CISCO-SAA-APM-MIB", "saaApmApplMajorVersion"),
        ("CISCO-SAA-APM-MIB", "saaApmApplMinorVersion"),
        ("CISCO-SAA-APM-MIB", "saaApmApplMaxOper"),
        ("CISCO-SAA-APM-MIB", "saaApmApplFreeMemLowWaterMark"),
        ("CISCO-SAA-APM-MIB", "saaApmApplOperCapacity"))
)
if mibBuilder.loadTexts:
    ciscoSaaApmApplGroup.setStatus("current")

ciscoSaaApmCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 3, 2, 2)
)
ciscoSaaApmCtrlGroup.setObjects(
      *(("CISCO-SAA-APM-MIB", "saaApmCtrlScriptCfgURL"),
        ("CISCO-SAA-APM-MIB", "saaApmCtrlOwner"),
        ("CISCO-SAA-APM-MIB", "saaApmCtrlInitDataTrans"),
        ("CISCO-SAA-APM-MIB", "saaApmCtrlDataTransTime"),
        ("CISCO-SAA-APM-MIB", "saaApmCtrlDataTransStatus"),
        ("CISCO-SAA-APM-MIB", "saaApmCtrlStatus"),
        ("CISCO-SAA-APM-MIB", "saaApmCtrlNvgen"))
)
if mibBuilder.loadTexts:
    ciscoSaaApmCtrlGroup.setStatus("current")

ciscoSaaApmOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 3, 2, 3)
)
ciscoSaaApmOperGroup.setObjects(
      *(("CISCO-SAA-APM-MIB", "saaApmOperLastStartTime"),
        ("CISCO-SAA-APM-MIB", "saaApmOperLastEndTime"),
        ("CISCO-SAA-APM-MIB", "saaApmOperLastStatus"))
)
if mibBuilder.loadTexts:
    ciscoSaaApmOperGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSaaApmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 177, 3, 1, 1)
)
ciscoSaaApmMIBCompliance.setObjects(
      *(("CISCO-SAA-APM-MIB", "ciscoSaaApmApplGroup"),
        ("CISCO-SAA-APM-MIB", "ciscoSaaApmCtrlGroup"),
        ("CISCO-SAA-APM-MIB", "ciscoSaaApmOperGroup"))
)
if mibBuilder.loadTexts:
    ciscoSaaApmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SAA-APM-MIB",
    **{"SaaApmOperErrorCode": SaaApmOperErrorCode,
       "SaaApmDataTransErrorCode": SaaApmDataTransErrorCode,
       "ciscoSaaApmMIB": ciscoSaaApmMIB,
       "ciscoSaaApmMIBObjects": ciscoSaaApmMIBObjects,
       "saaApmAppl": saaApmAppl,
       "saaApmApplMajorVersion": saaApmApplMajorVersion,
       "saaApmApplMinorVersion": saaApmApplMinorVersion,
       "saaApmApplMaxOper": saaApmApplMaxOper,
       "saaApmApplFreeMemLowWaterMark": saaApmApplFreeMemLowWaterMark,
       "saaApmApplOperCapacity": saaApmApplOperCapacity,
       "saaApmCtrl": saaApmCtrl,
       "saaApmCtrlTable": saaApmCtrlTable,
       "saaApmCtrlEntry": saaApmCtrlEntry,
       "saaApmCtrlIndex": saaApmCtrlIndex,
       "saaApmCtrlScriptCfgURL": saaApmCtrlScriptCfgURL,
       "saaApmCtrlOwner": saaApmCtrlOwner,
       "saaApmCtrlInitDataTrans": saaApmCtrlInitDataTrans,
       "saaApmCtrlDataTransTime": saaApmCtrlDataTransTime,
       "saaApmCtrlDataTransStatus": saaApmCtrlDataTransStatus,
       "saaApmCtrlStatus": saaApmCtrlStatus,
       "saaApmCtrlNvgen": saaApmCtrlNvgen,
       "saaApmOper": saaApmOper,
       "saaApmOperTable": saaApmOperTable,
       "saaApmOperEntry": saaApmOperEntry,
       "saaApmOperLastStartTime": saaApmOperLastStartTime,
       "saaApmOperLastEndTime": saaApmOperLastEndTime,
       "saaApmOperLastStatus": saaApmOperLastStatus,
       "ciscoSaaApmMIBNotifPrefix": ciscoSaaApmMIBNotifPrefix,
       "ciscoSaaApmMIBNotifs": ciscoSaaApmMIBNotifs,
       "ciscoSaaApmMIBConformance": ciscoSaaApmMIBConformance,
       "ciscoSaaApmMIBCompliances": ciscoSaaApmMIBCompliances,
       "ciscoSaaApmMIBCompliance": ciscoSaaApmMIBCompliance,
       "ciscoSaaApmMIBGroups": ciscoSaaApmMIBGroups,
       "ciscoSaaApmApplGroup": ciscoSaaApmApplGroup,
       "ciscoSaaApmCtrlGroup": ciscoSaaApmCtrlGroup,
       "ciscoSaaApmOperGroup": ciscoSaaApmOperGroup}
)
