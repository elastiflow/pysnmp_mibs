# SNMP MIB module (TIMETRA-DYNAMIC-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-DYNAMIC-SERVICES-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:31 2025
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
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxPortID,
 TmnxServId,
 TmnxSubAcctSessionId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId",
    "TmnxSubAcctSessionId")


# MODULE-IDENTITY

timetraDynSrvMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 84)
)
if mibBuilder.loadTexts:
    timetraDynSrvMIBModule.setRevisions(
        ("2013-05-31 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxDynSrvAcctStatsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("volumeTime", 1),
          ("time", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxDynSvcConformance_ObjectIdentity = ObjectIdentity
tmnxDynSvcConformance = _TmnxDynSvcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84)
)
_TmnxDynSvcCompliances_ObjectIdentity = ObjectIdentity
tmnxDynSvcCompliances = _TmnxDynSvcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 1)
)
_TmnxDynSvcGroups_ObjectIdentity = ObjectIdentity
tmnxDynSvcGroups = _TmnxDynSvcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 2)
)
_TmnxDynSvc_ObjectIdentity = ObjectIdentity
tmnxDynSvc = _TmnxDynSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84)
)
_TmnxDynSvcObjs_ObjectIdentity = ObjectIdentity
tmnxDynSvcObjs = _TmnxDynSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1)
)
_TmnxDynSvcPlcyTable_Object = MibTable
tmnxDynSvcPlcyTable = _TmnxDynSvcPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyTable.setStatus("current")
_TmnxDynSvcPlcyEntry_Object = MibTableRow
tmnxDynSvcPlcyEntry = _TmnxDynSvcPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1)
)
tmnxDynSvcPlcyEntry.setIndexNames(
    (1, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyEntry.setStatus("current")
_TmnxDynSvcPlcyName_Type = TNamedItem
_TmnxDynSvcPlcyName_Object = MibTableColumn
tmnxDynSvcPlcyName = _TmnxDynSvcPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 1),
    _TmnxDynSvcPlcyName_Type()
)
tmnxDynSvcPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyName.setStatus("current")
_TmnxDynSvcPlcyRowStatus_Type = RowStatus
_TmnxDynSvcPlcyRowStatus_Object = MibTableColumn
tmnxDynSvcPlcyRowStatus = _TmnxDynSvcPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 2),
    _TmnxDynSvcPlcyRowStatus_Type()
)
tmnxDynSvcPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyRowStatus.setStatus("current")
_TmnxDynSvcPlcyLastCh_Type = TimeStamp
_TmnxDynSvcPlcyLastCh_Object = MibTableColumn
tmnxDynSvcPlcyLastCh = _TmnxDynSvcPlcyLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 3),
    _TmnxDynSvcPlcyLastCh_Type()
)
tmnxDynSvcPlcyLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyLastCh.setStatus("current")


class _TmnxDynSvcPlcyDescription_Type(TItemDescription):
    """Custom type tmnxDynSvcPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxDynSvcPlcyDescription_Object = MibTableColumn
tmnxDynSvcPlcyDescription = _TmnxDynSvcPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 4),
    _TmnxDynSvcPlcyDescription_Type()
)
tmnxDynSvcPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyDescription.setStatus("current")


class _TmnxDynSvcPlcyScriptPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxDynSvcPlcyScriptPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyScriptPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDynSvcPlcyScriptPlcy_Object = MibTableColumn
tmnxDynSvcPlcyScriptPlcy = _TmnxDynSvcPlcyScriptPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 5),
    _TmnxDynSvcPlcyScriptPlcy_Type()
)
tmnxDynSvcPlcyScriptPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyScriptPlcy.setStatus("current")


class _TmnxDynSvcPlcyCliUser_Type(TNamedItemOrEmpty):
    """Custom type tmnxDynSvcPlcyCliUser based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyCliUser_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDynSvcPlcyCliUser_Object = MibTableColumn
tmnxDynSvcPlcyCliUser = _TmnxDynSvcPlcyCliUser_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 6),
    _TmnxDynSvcPlcyCliUser_Type()
)
tmnxDynSvcPlcyCliUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyCliUser.setStatus("current")


class _TmnxDynSvcPlcySapLimit_Type(Unsigned32):
    """Custom type tmnxDynSvcPlcySapLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_TmnxDynSvcPlcySapLimit_Type.__name__ = "Unsigned32"
_TmnxDynSvcPlcySapLimit_Object = MibTableColumn
tmnxDynSvcPlcySapLimit = _TmnxDynSvcPlcySapLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 1, 1, 7),
    _TmnxDynSvcPlcySapLimit_Type()
)
tmnxDynSvcPlcySapLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcySapLimit.setStatus("current")
_TmnxDynSvcPlcyApTable_Object = MibTable
tmnxDynSvcPlcyApTable = _TmnxDynSvcPlcyApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApTable.setStatus("current")
_TmnxDynSvcPlcyApEntry_Object = MibTableRow
tmnxDynSvcPlcyApEntry = _TmnxDynSvcPlcyApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1)
)
tmnxDynSvcPlcyApEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApIndex"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApEntry.setStatus("current")


class _TmnxDynSvcPlcyApIndex_Type(Unsigned32):
    """Custom type tmnxDynSvcPlcyApIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxDynSvcPlcyApIndex_Type.__name__ = "Unsigned32"
_TmnxDynSvcPlcyApIndex_Object = MibTableColumn
tmnxDynSvcPlcyApIndex = _TmnxDynSvcPlcyApIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 1),
    _TmnxDynSvcPlcyApIndex_Type()
)
tmnxDynSvcPlcyApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApIndex.setStatus("current")
_TmnxDynSvcPlcyApLastCh_Type = TimeStamp
_TmnxDynSvcPlcyApLastCh_Object = MibTableColumn
tmnxDynSvcPlcyApLastCh = _TmnxDynSvcPlcyApLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 2),
    _TmnxDynSvcPlcyApLastCh_Type()
)
tmnxDynSvcPlcyApLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApLastCh.setStatus("current")


class _TmnxDynSvcPlcyApName_Type(TNamedItemOrEmpty):
    """Custom type tmnxDynSvcPlcyApName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxDynSvcPlcyApName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxDynSvcPlcyApName_Object = MibTableColumn
tmnxDynSvcPlcyApName = _TmnxDynSvcPlcyApName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 3),
    _TmnxDynSvcPlcyApName_Type()
)
tmnxDynSvcPlcyApName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApName.setStatus("current")


class _TmnxDynSvcPlcyApStatsType_Type(TmnxDynSrvAcctStatsType):
    """Custom type tmnxDynSvcPlcyApStatsType based on TmnxDynSrvAcctStatsType"""
    defaultValue = 1


_TmnxDynSvcPlcyApStatsType_Type.__name__ = "TmnxDynSrvAcctStatsType"
_TmnxDynSvcPlcyApStatsType_Object = MibTableColumn
tmnxDynSvcPlcyApStatsType = _TmnxDynSvcPlcyApStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 4),
    _TmnxDynSvcPlcyApStatsType_Type()
)
tmnxDynSvcPlcyApStatsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApStatsType.setStatus("current")


class _TmnxDynSvcPlcyApUpdateInterval_Type(Unsigned32):
    """Custom type tmnxDynSvcPlcyApUpdateInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 259200),
    )


_TmnxDynSvcPlcyApUpdateInterval_Type.__name__ = "Unsigned32"
_TmnxDynSvcPlcyApUpdateInterval_Object = MibTableColumn
tmnxDynSvcPlcyApUpdateInterval = _TmnxDynSvcPlcyApUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 5),
    _TmnxDynSvcPlcyApUpdateInterval_Type()
)
tmnxDynSvcPlcyApUpdateInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApUpdateInterval.setUnits("minutes")


class _TmnxDynSvcPlcyApUpdateIvlJitter_Type(Integer32):
    """Custom type tmnxDynSvcPlcyApUpdateIvlJitter based on Integer32"""
    defaultValue = -10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, -10),
        ValueRangeConstraint(0, 3600),
    )


_TmnxDynSvcPlcyApUpdateIvlJitter_Type.__name__ = "Integer32"
_TmnxDynSvcPlcyApUpdateIvlJitter_Object = MibTableColumn
tmnxDynSvcPlcyApUpdateIvlJitter = _TmnxDynSvcPlcyApUpdateIvlJitter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 2, 1, 6),
    _TmnxDynSvcPlcyApUpdateIvlJitter_Type()
)
tmnxDynSvcPlcyApUpdateIvlJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApUpdateIvlJitter.setStatus("current")
_TmnxDynSvcRange_ObjectIdentity = ObjectIdentity
tmnxDynSvcRange = _TmnxDynSvcRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 3)
)


class _TmnxDynSvcRangeStart_Type(TmnxServId):
    """Custom type tmnxDynSvcRangeStart based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_TmnxDynSvcRangeStart_Type.__name__ = "TmnxServId"
_TmnxDynSvcRangeStart_Object = MibScalar
tmnxDynSvcRangeStart = _TmnxDynSvcRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 3, 1),
    _TmnxDynSvcRangeStart_Type()
)
tmnxDynSvcRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDynSvcRangeStart.setStatus("current")


class _TmnxDynSvcRangeEnd_Type(TmnxServId):
    """Custom type tmnxDynSvcRangeEnd based on TmnxServId"""
    defaultValue = 0

    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_TmnxDynSvcRangeEnd_Type.__name__ = "TmnxServId"
_TmnxDynSvcRangeEnd_Object = MibScalar
tmnxDynSvcRangeEnd = _TmnxDynSvcRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 3, 2),
    _TmnxDynSvcRangeEnd_Type()
)
tmnxDynSvcRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDynSvcRangeEnd.setStatus("current")
_TmnxDynSvcSapTable_Object = MibTable
tmnxDynSvcSapTable = _TmnxDynSvcSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSapTable.setStatus("current")
_TmnxDynSvcSapEntry_Object = MibTableRow
tmnxDynSvcSapEntry = _TmnxDynSvcSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1)
)
tmnxDynSvcSapEntry.setIndexNames(
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSapEntry.setStatus("current")
_TmnxDynSvcSapAcctSessionId_Type = TmnxSubAcctSessionId
_TmnxDynSvcSapAcctSessionId_Object = MibTableColumn
tmnxDynSvcSapAcctSessionId = _TmnxDynSvcSapAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 1),
    _TmnxDynSvcSapAcctSessionId_Type()
)
tmnxDynSvcSapAcctSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctSessionId.setStatus("current")
_TmnxDynSvcSapAcctSessionIdCtrl_Type = TmnxSubAcctSessionId
_TmnxDynSvcSapAcctSessionIdCtrl_Object = MibTableColumn
tmnxDynSvcSapAcctSessionIdCtrl = _TmnxDynSvcSapAcctSessionIdCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 2),
    _TmnxDynSvcSapAcctSessionIdCtrl_Type()
)
tmnxDynSvcSapAcctSessionIdCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctSessionIdCtrl.setStatus("current")
_TmnxDynSvcSapPolicy_Type = TNamedItemOrEmpty
_TmnxDynSvcSapPolicy_Object = MibTableColumn
tmnxDynSvcSapPolicy = _TmnxDynSvcSapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 3),
    _TmnxDynSvcSapPolicy_Type()
)
tmnxDynSvcSapPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapPolicy.setStatus("current")
_TmnxDynSvcSapScriptsExecuted_Type = Counter32
_TmnxDynSvcSapScriptsExecuted_Object = MibTableColumn
tmnxDynSvcSapScriptsExecuted = _TmnxDynSvcSapScriptsExecuted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 4),
    _TmnxDynSvcSapScriptsExecuted_Type()
)
tmnxDynSvcSapScriptsExecuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapScriptsExecuted.setStatus("current")
_TmnxDynSvcSapScriptsSuccess_Type = Counter32
_TmnxDynSvcSapScriptsSuccess_Object = MibTableColumn
tmnxDynSvcSapScriptsSuccess = _TmnxDynSvcSapScriptsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 5),
    _TmnxDynSvcSapScriptsSuccess_Type()
)
tmnxDynSvcSapScriptsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapScriptsSuccess.setStatus("current")


class _TmnxDynSvcSapLastScriptAction_Type(Integer32):
    """Custom type tmnxDynSvcSapLastScriptAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("setup", 1),
          ("modify", 2),
          ("teardown", 3),
          ("commit", 4),
          ("revert", 5))
    )


_TmnxDynSvcSapLastScriptAction_Type.__name__ = "Integer32"
_TmnxDynSvcSapLastScriptAction_Object = MibTableColumn
tmnxDynSvcSapLastScriptAction = _TmnxDynSvcSapLastScriptAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 6),
    _TmnxDynSvcSapLastScriptAction_Type()
)
tmnxDynSvcSapLastScriptAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapLastScriptAction.setStatus("current")


class _TmnxDynSvcSapLastScriptTime_Type(DateAndTime):
    """Custom type tmnxDynSvcSapLastScriptTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxDynSvcSapLastScriptTime_Type.__name__ = "DateAndTime"
_TmnxDynSvcSapLastScriptTime_Object = MibTableColumn
tmnxDynSvcSapLastScriptTime = _TmnxDynSvcSapLastScriptTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 7),
    _TmnxDynSvcSapLastScriptTime_Type()
)
tmnxDynSvcSapLastScriptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapLastScriptTime.setStatus("current")
_TmnxDynSvcSapOrphaned_Type = TruthValue
_TmnxDynSvcSapOrphaned_Object = MibTableColumn
tmnxDynSvcSapOrphaned = _TmnxDynSvcSapOrphaned_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 8),
    _TmnxDynSvcSapOrphaned_Type()
)
tmnxDynSvcSapOrphaned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapOrphaned.setStatus("current")
_TmnxDynSvcSapService_Type = TmnxServId
_TmnxDynSvcSapService_Object = MibTableColumn
tmnxDynSvcSapService = _TmnxDynSvcSapService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 9),
    _TmnxDynSvcSapService_Type()
)
tmnxDynSvcSapService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapService.setStatus("current")


class _TmnxDynSvcSapLastScriptParams_Type(OctetString):
    """Custom type tmnxDynSvcSapLastScriptParams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_TmnxDynSvcSapLastScriptParams_Type.__name__ = "OctetString"
_TmnxDynSvcSapLastScriptParams_Object = MibTableColumn
tmnxDynSvcSapLastScriptParams = _TmnxDynSvcSapLastScriptParams_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 4, 1, 10),
    _TmnxDynSvcSapLastScriptParams_Type()
)
tmnxDynSvcSapLastScriptParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapLastScriptParams.setStatus("current")
_TmnxDynSvcSapAcctTable_Object = MibTable
tmnxDynSvcSapAcctTable = _TmnxDynSvcSapAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctTable.setStatus("current")
_TmnxDynSvcSapAcctEntry_Object = MibTableRow
tmnxDynSvcSapAcctEntry = _TmnxDynSvcSapAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5, 1)
)
tmnxDynSvcSapAcctEntry.setIndexNames(
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctIndex"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctEntry.setStatus("current")


class _TmnxDynSvcSapAcctIndex_Type(Unsigned32):
    """Custom type tmnxDynSvcSapAcctIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxDynSvcSapAcctIndex_Type.__name__ = "Unsigned32"
_TmnxDynSvcSapAcctIndex_Object = MibTableColumn
tmnxDynSvcSapAcctIndex = _TmnxDynSvcSapAcctIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5, 1, 1),
    _TmnxDynSvcSapAcctIndex_Type()
)
tmnxDynSvcSapAcctIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctIndex.setStatus("current")
_TmnxDynSvcSapAcctAcctStatus_Type = TmnxEnabledDisabled
_TmnxDynSvcSapAcctAcctStatus_Object = MibTableColumn
tmnxDynSvcSapAcctAcctStatus = _TmnxDynSvcSapAcctAcctStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5, 1, 2),
    _TmnxDynSvcSapAcctAcctStatus_Type()
)
tmnxDynSvcSapAcctAcctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctAcctStatus.setStatus("current")
_TmnxDynSvcSapAcctStatsType_Type = TmnxDynSrvAcctStatsType
_TmnxDynSvcSapAcctStatsType_Object = MibTableColumn
tmnxDynSvcSapAcctStatsType = _TmnxDynSvcSapAcctStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5, 1, 3),
    _TmnxDynSvcSapAcctStatsType_Type()
)
tmnxDynSvcSapAcctStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctStatsType.setStatus("current")
_TmnxDynSvcSapAcctAcctInterval_Type = Unsigned32
_TmnxDynSvcSapAcctAcctInterval_Object = MibTableColumn
tmnxDynSvcSapAcctAcctInterval = _TmnxDynSvcSapAcctAcctInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 5, 1, 4),
    _TmnxDynSvcSapAcctAcctInterval_Type()
)
tmnxDynSvcSapAcctAcctInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctAcctInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDynSvcSapAcctAcctInterval.setUnits("minutes")
_TmnxDynSvcRootObjTable_Object = MibTable
tmnxDynSvcRootObjTable = _TmnxDynSvcRootObjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjTable.setStatus("current")
_TmnxDynSvcRootObjEntry_Object = MibTableRow
tmnxDynSvcRootObjEntry = _TmnxDynSvcRootObjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1)
)
tmnxDynSvcRootObjEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjIndex"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjEntry.setStatus("current")
_TmnxDynSvcRootObjIndex_Type = Unsigned32
_TmnxDynSvcRootObjIndex_Object = MibTableColumn
tmnxDynSvcRootObjIndex = _TmnxDynSvcRootObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1, 1),
    _TmnxDynSvcRootObjIndex_Type()
)
tmnxDynSvcRootObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjIndex.setStatus("current")
_TmnxDynSvcRootObjInstance_Type = RowPointer
_TmnxDynSvcRootObjInstance_Object = MibTableColumn
tmnxDynSvcRootObjInstance = _TmnxDynSvcRootObjInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1, 2),
    _TmnxDynSvcRootObjInstance_Type()
)
tmnxDynSvcRootObjInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjInstance.setStatus("current")
_TmnxDynSvcRootObjOrphanTime_Type = TimeStamp
_TmnxDynSvcRootObjOrphanTime_Object = MibTableColumn
tmnxDynSvcRootObjOrphanTime = _TmnxDynSvcRootObjOrphanTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1, 3),
    _TmnxDynSvcRootObjOrphanTime_Type()
)
tmnxDynSvcRootObjOrphanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjOrphanTime.setStatus("current")
_TmnxDynSvcRootObjSnippetName_Type = DisplayString
_TmnxDynSvcRootObjSnippetName_Object = MibTableColumn
tmnxDynSvcRootObjSnippetName = _TmnxDynSvcRootObjSnippetName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1, 4),
    _TmnxDynSvcRootObjSnippetName_Type()
)
tmnxDynSvcRootObjSnippetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjSnippetName.setStatus("current")
_TmnxDynSvcRootObjSnippetInstance_Type = DisplayString
_TmnxDynSvcRootObjSnippetInstance_Object = MibTableColumn
tmnxDynSvcRootObjSnippetInstance = _TmnxDynSvcRootObjSnippetInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 6, 1, 5),
    _TmnxDynSvcRootObjSnippetInstance_Type()
)
tmnxDynSvcRootObjSnippetInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjSnippetInstance.setStatus("current")
_TmnxDynSvcStatsTable_Object = MibTable
tmnxDynSvcStatsTable = _TmnxDynSvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxDynSvcStatsTable.setStatus("current")
_TmnxDynSvcStatsEntry_Object = MibTableRow
tmnxDynSvcStatsEntry = _TmnxDynSvcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 7, 1)
)
tmnxDynSvcStatsEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsId"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcStatsEntry.setStatus("current")
_TmnxDynSvcStatsId_Type = Unsigned32
_TmnxDynSvcStatsId_Object = MibTableColumn
tmnxDynSvcStatsId = _TmnxDynSvcStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 7, 1, 1),
    _TmnxDynSvcStatsId_Type()
)
tmnxDynSvcStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcStatsId.setStatus("current")
_TmnxDynSvcStatsDescr_Type = TItemDescription
_TmnxDynSvcStatsDescr_Object = MibTableColumn
tmnxDynSvcStatsDescr = _TmnxDynSvcStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 7, 1, 2),
    _TmnxDynSvcStatsDescr_Type()
)
tmnxDynSvcStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcStatsDescr.setStatus("current")
_TmnxDynSvcStatsVal_Type = Counter32
_TmnxDynSvcStatsVal_Object = MibTableColumn
tmnxDynSvcStatsVal = _TmnxDynSvcStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 7, 1, 3),
    _TmnxDynSvcStatsVal_Type()
)
tmnxDynSvcStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcStatsVal.setStatus("current")
_TmnxDynSvcSnippetTable_Object = MibTable
tmnxDynSvcSnippetTable = _TmnxDynSvcSnippetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetTable.setStatus("current")
_TmnxDynSvcSnippetEntry_Object = MibTableRow
tmnxDynSvcSnippetEntry = _TmnxDynSvcSnippetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8, 1)
)
tmnxDynSvcSnippetEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetInstance"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetEntry.setStatus("current")


class _TmnxDynSvcSnippetName_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxDynSvcSnippetName_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetName_Object = MibTableColumn
tmnxDynSvcSnippetName = _TmnxDynSvcSnippetName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8, 1, 1),
    _TmnxDynSvcSnippetName_Type()
)
tmnxDynSvcSnippetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetName.setStatus("current")


class _TmnxDynSvcSnippetInstance_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TmnxDynSvcSnippetInstance_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetInstance_Object = MibTableColumn
tmnxDynSvcSnippetInstance = _TmnxDynSvcSnippetInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8, 1, 2),
    _TmnxDynSvcSnippetInstance_Type()
)
tmnxDynSvcSnippetInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetInstance.setStatus("current")
_TmnxDynSvcSnippetRefCount_Type = Counter32
_TmnxDynSvcSnippetRefCount_Object = MibTableColumn
tmnxDynSvcSnippetRefCount = _TmnxDynSvcSnippetRefCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8, 1, 3),
    _TmnxDynSvcSnippetRefCount_Type()
)
tmnxDynSvcSnippetRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefCount.setStatus("current")
_TmnxDynSvcSnippetDictLength_Type = Unsigned32
_TmnxDynSvcSnippetDictLength_Object = MibTableColumn
tmnxDynSvcSnippetDictLength = _TmnxDynSvcSnippetDictLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 8, 1, 4),
    _TmnxDynSvcSnippetDictLength_Type()
)
tmnxDynSvcSnippetDictLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetDictLength.setStatus("current")
_TmnxDynSvcSnippetRootObjTable_Object = MibTable
tmnxDynSvcSnippetRootObjTable = _TmnxDynSvcSnippetRootObjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRootObjTable.setStatus("current")
_TmnxDynSvcSnippetRootObjEntry_Object = MibTableRow
tmnxDynSvcSnippetRootObjEntry = _TmnxDynSvcSnippetRootObjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 9, 1)
)
tmnxDynSvcSnippetRootObjEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetInstance"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRootObjIdx"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRootObjEntry.setStatus("current")
_TmnxDynSvcSnippetRootObjIdx_Type = Unsigned32
_TmnxDynSvcSnippetRootObjIdx_Object = MibTableColumn
tmnxDynSvcSnippetRootObjIdx = _TmnxDynSvcSnippetRootObjIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 9, 1, 1),
    _TmnxDynSvcSnippetRootObjIdx_Type()
)
tmnxDynSvcSnippetRootObjIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRootObjIdx.setStatus("current")
_TmnxDynSvcSnippetRootObjOid_Type = RowPointer
_TmnxDynSvcSnippetRootObjOid_Object = MibTableColumn
tmnxDynSvcSnippetRootObjOid = _TmnxDynSvcSnippetRootObjOid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 9, 1, 2),
    _TmnxDynSvcSnippetRootObjOid_Type()
)
tmnxDynSvcSnippetRootObjOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRootObjOid.setStatus("current")
_TmnxDynSvcSnippetRefTable_Object = MibTable
tmnxDynSvcSnippetRefTable = _TmnxDynSvcSnippetRefTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefTable.setStatus("current")
_TmnxDynSvcSnippetRefEntry_Object = MibTableRow
tmnxDynSvcSnippetRefEntry = _TmnxDynSvcSnippetRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 10, 1)
)
tmnxDynSvcSnippetRefEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetInstance"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefIdx"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefEntry.setStatus("current")
_TmnxDynSvcSnippetRefIdx_Type = Unsigned32
_TmnxDynSvcSnippetRefIdx_Object = MibTableColumn
tmnxDynSvcSnippetRefIdx = _TmnxDynSvcSnippetRefIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 10, 1, 1),
    _TmnxDynSvcSnippetRefIdx_Type()
)
tmnxDynSvcSnippetRefIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefIdx.setStatus("current")


class _TmnxDynSvcSnippetRefSnipName_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetRefSnipName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxDynSvcSnippetRefSnipName_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetRefSnipName_Object = MibTableColumn
tmnxDynSvcSnippetRefSnipName = _TmnxDynSvcSnippetRefSnipName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 10, 1, 2),
    _TmnxDynSvcSnippetRefSnipName_Type()
)
tmnxDynSvcSnippetRefSnipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefSnipName.setStatus("current")


class _TmnxDynSvcSnippetRefSnipInst_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetRefSnipInst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TmnxDynSvcSnippetRefSnipInst_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetRefSnipInst_Object = MibTableColumn
tmnxDynSvcSnippetRefSnipInst = _TmnxDynSvcSnippetRefSnipInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 10, 1, 3),
    _TmnxDynSvcSnippetRefSnipInst_Type()
)
tmnxDynSvcSnippetRefSnipInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefSnipInst.setStatus("current")
_TmnxDynSvcSnippetResIdTable_Object = MibTable
tmnxDynSvcSnippetResIdTable = _TmnxDynSvcSnippetResIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdTable.setStatus("current")
_TmnxDynSvcSnippetResIdEntry_Object = MibTableRow
tmnxDynSvcSnippetResIdEntry = _TmnxDynSvcSnippetResIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 11, 1)
)
tmnxDynSvcSnippetResIdEntry.setIndexNames(
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetName"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetInstance"),
    (0, "TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdIdx"),
)
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdEntry.setStatus("current")
_TmnxDynSvcSnippetResIdIdx_Type = Unsigned32
_TmnxDynSvcSnippetResIdIdx_Object = MibTableColumn
tmnxDynSvcSnippetResIdIdx = _TmnxDynSvcSnippetResIdIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 11, 1, 1),
    _TmnxDynSvcSnippetResIdIdx_Type()
)
tmnxDynSvcSnippetResIdIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdIdx.setStatus("current")


class _TmnxDynSvcSnippetResIdType_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetResIdType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxDynSvcSnippetResIdType_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetResIdType_Object = MibTableColumn
tmnxDynSvcSnippetResIdType = _TmnxDynSvcSnippetResIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 11, 1, 2),
    _TmnxDynSvcSnippetResIdType_Type()
)
tmnxDynSvcSnippetResIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdType.setStatus("current")


class _TmnxDynSvcSnippetResIdValue_Type(DisplayString):
    """Custom type tmnxDynSvcSnippetResIdValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TmnxDynSvcSnippetResIdValue_Type.__name__ = "DisplayString"
_TmnxDynSvcSnippetResIdValue_Object = MibTableColumn
tmnxDynSvcSnippetResIdValue = _TmnxDynSvcSnippetResIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 11, 1, 3),
    _TmnxDynSvcSnippetResIdValue_Type()
)
tmnxDynSvcSnippetResIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdValue.setStatus("current")
_TmnxDynSvcTimer_ObjectIdentity = ObjectIdentity
tmnxDynSvcTimer = _TmnxDynSvcTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 12)
)


class _TmnxDynSvcTimerAccSetupTimeout_Type(Unsigned32):
    """Custom type tmnxDynSvcTimerAccSetupTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_TmnxDynSvcTimerAccSetupTimeout_Type.__name__ = "Unsigned32"
_TmnxDynSvcTimerAccSetupTimeout_Object = MibScalar
tmnxDynSvcTimerAccSetupTimeout = _TmnxDynSvcTimerAccSetupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 12, 1),
    _TmnxDynSvcTimerAccSetupTimeout_Type()
)
tmnxDynSvcTimerAccSetupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDynSvcTimerAccSetupTimeout.setStatus("current")
_TmnxDynSvcPlcyTableLastCh_Type = TimeStamp
_TmnxDynSvcPlcyTableLastCh_Object = MibScalar
tmnxDynSvcPlcyTableLastCh = _TmnxDynSvcPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 100),
    _TmnxDynSvcPlcyTableLastCh_Type()
)
tmnxDynSvcPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyTableLastCh.setStatus("current")
_TmnxDynSvcPlcyApTableLastCh_Type = TimeStamp
_TmnxDynSvcPlcyApTableLastCh_Object = MibScalar
tmnxDynSvcPlcyApTableLastCh = _TmnxDynSvcPlcyApTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 101),
    _TmnxDynSvcPlcyApTableLastCh_Type()
)
tmnxDynSvcPlcyApTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcPlcyApTableLastCh.setStatus("current")
_TmnxDynSvcSapTableLastCh_Type = TimeStamp
_TmnxDynSvcSapTableLastCh_Object = MibScalar
tmnxDynSvcSapTableLastCh = _TmnxDynSvcSapTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 102),
    _TmnxDynSvcSapTableLastCh_Type()
)
tmnxDynSvcSapTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSapTableLastCh.setStatus("current")
_TmnxDynSvcRootObjTableLastCh_Type = TimeStamp
_TmnxDynSvcRootObjTableLastCh_Object = MibScalar
tmnxDynSvcRootObjTableLastCh = _TmnxDynSvcRootObjTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 103),
    _TmnxDynSvcRootObjTableLastCh_Type()
)
tmnxDynSvcRootObjTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcRootObjTableLastCh.setStatus("current")
_TmnxDynSvcNonStoredRootObjCount_Type = Counter32
_TmnxDynSvcNonStoredRootObjCount_Object = MibScalar
tmnxDynSvcNonStoredRootObjCount = _TmnxDynSvcNonStoredRootObjCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 104),
    _TmnxDynSvcNonStoredRootObjCount_Type()
)
tmnxDynSvcNonStoredRootObjCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcNonStoredRootObjCount.setStatus("current")
_TmnxDynSvcSnippetTableLastCh_Type = TimeStamp
_TmnxDynSvcSnippetTableLastCh_Object = MibScalar
tmnxDynSvcSnippetTableLastCh = _TmnxDynSvcSnippetTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 105),
    _TmnxDynSvcSnippetTableLastCh_Type()
)
tmnxDynSvcSnippetTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetTableLastCh.setStatus("current")
_TmnxDynSvcSnipRootObjTblLastCh_Type = TimeStamp
_TmnxDynSvcSnipRootObjTblLastCh_Object = MibScalar
tmnxDynSvcSnipRootObjTblLastCh = _TmnxDynSvcSnipRootObjTblLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 106),
    _TmnxDynSvcSnipRootObjTblLastCh_Type()
)
tmnxDynSvcSnipRootObjTblLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnipRootObjTblLastCh.setStatus("current")
_TmnxDynSvcSnippetRefTableLastCh_Type = TimeStamp
_TmnxDynSvcSnippetRefTableLastCh_Object = MibScalar
tmnxDynSvcSnippetRefTableLastCh = _TmnxDynSvcSnippetRefTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 107),
    _TmnxDynSvcSnippetRefTableLastCh_Type()
)
tmnxDynSvcSnippetRefTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetRefTableLastCh.setStatus("current")
_TmnxDynSvcSnippetResIdTblLastCh_Type = TimeStamp
_TmnxDynSvcSnippetResIdTblLastCh_Object = MibScalar
tmnxDynSvcSnippetResIdTblLastCh = _TmnxDynSvcSnippetResIdTblLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 108),
    _TmnxDynSvcSnippetResIdTblLastCh_Type()
)
tmnxDynSvcSnippetResIdTblLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcSnippetResIdTblLastCh.setStatus("current")
_TmnxDynSvcStatsLastClearedTime_Type = TimeStamp
_TmnxDynSvcStatsLastClearedTime_Object = MibScalar
tmnxDynSvcStatsLastClearedTime = _TmnxDynSvcStatsLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 1, 109),
    _TmnxDynSvcStatsLastClearedTime_Type()
)
tmnxDynSvcStatsLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDynSvcStatsLastClearedTime.setStatus("current")
_TmnxDynSvcNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxDynSvcNotificationObjs = _TmnxDynSvcNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 2)
)


class _TmnxDynSvcNotifDescription_Type(DisplayString):
    """Custom type tmnxDynSvcNotifDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxDynSvcNotifDescription_Type.__name__ = "DisplayString"
_TmnxDynSvcNotifDescription_Object = MibScalar
tmnxDynSvcNotifDescription = _TmnxDynSvcNotifDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 2, 1),
    _TmnxDynSvcNotifDescription_Type()
)
tmnxDynSvcNotifDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDynSvcNotifDescription.setStatus("current")
_TmnxDynSvcNotifSapPortId_Type = TmnxPortID
_TmnxDynSvcNotifSapPortId_Object = MibScalar
tmnxDynSvcNotifSapPortId = _TmnxDynSvcNotifSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 2, 2),
    _TmnxDynSvcNotifSapPortId_Type()
)
tmnxDynSvcNotifSapPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDynSvcNotifSapPortId.setStatus("current")
_TmnxDynSvcNotifSapEncapValue_Type = TmnxEncapVal
_TmnxDynSvcNotifSapEncapValue_Object = MibScalar
tmnxDynSvcNotifSapEncapValue = _TmnxDynSvcNotifSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 2, 3),
    _TmnxDynSvcNotifSapEncapValue_Type()
)
tmnxDynSvcNotifSapEncapValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDynSvcNotifSapEncapValue.setStatus("current")
_TmnxDynSvcNotifSapAcctSessionId_Type = TmnxSubAcctSessionId
_TmnxDynSvcNotifSapAcctSessionId_Object = MibScalar
tmnxDynSvcNotifSapAcctSessionId = _TmnxDynSvcNotifSapAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 84, 2, 4),
    _TmnxDynSvcNotifSapAcctSessionId_Type()
)
tmnxDynSvcNotifSapAcctSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDynSvcNotifSapAcctSessionId.setStatus("current")
_TmnxDynSvcNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxDynSvcNotifyPrefix = _TmnxDynSvcNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 84)
)
_TmnxDynSvcNotifications_ObjectIdentity = ObjectIdentity
tmnxDynSvcNotifications = _TmnxDynSvcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 84, 0)
)

# Managed Objects groups

tmnxDynSvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 2, 1)
)
tmnxDynSvcGroup.setObjects(
      *(("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyRowStatus"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyDescription"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyScriptPlcy"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyCliUser"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcySapLimit"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApName"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApStatsType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApUpdateInterval"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRangeStart"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRangeEnd"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctSessionId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctSessionIdCtrl"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapPolicy"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapScriptsExecuted"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapScriptsSuccess"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapLastScriptAction"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapLastScriptTime"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapOrphaned"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapService"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapLastScriptParams"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctAcctStatus"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctStatsType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapAcctAcctInterval"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcPlcyApUpdateIvlJitter"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjInstance"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjOrphanTime"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjSnippetName"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjSnippetInstance"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcRootObjTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNonStoredRootObjCount"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsDescr"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsVal"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefCount"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetDictLength"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRootObjOid"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefSnipName"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefSnipInst"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdType"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdValue"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnipRootObjTblLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetRefTableLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSnippetResIdTblLastCh"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcTimerAccSetupTimeout"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcStatsLastClearedTime"))
)
if mibBuilder.loadTexts:
    tmnxDynSvcGroup.setStatus("current")

tmnxDynSvcNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 2, 99)
)
tmnxDynSvcNotifyObjsGroup.setObjects(
      *(("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapAcctSessionId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapPortId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapEncapValue"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifDescription"))
)
if mibBuilder.loadTexts:
    tmnxDynSvcNotifyObjsGroup.setStatus("current")


# Notification objects

tmnxDynSvcSapFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 84, 0, 1)
)
tmnxDynSvcSapFailed.setObjects(
      *(("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapAcctSessionId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapPortId"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifSapEncapValue"),
        ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifDescription"))
)
if mibBuilder.loadTexts:
    tmnxDynSvcSapFailed.setStatus(
        "current"
    )


# Notifications groups

tmnxDynSvcNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 2, 100)
)
tmnxDynSvcNotifyGroup.setObjects(
    ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcSapFailed")
)
if mibBuilder.loadTexts:
    tmnxDynSvcNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxDynSvcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 1, 1)
)
tmnxDynSvcCompliance.setObjects(
    ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcGroup")
)
if mibBuilder.loadTexts:
    tmnxDynSvcCompliance.setStatus(
        "current"
    )

tmnxDynSvcNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 84, 1, 2)
)
tmnxDynSvcNotifyCompliance.setObjects(
    ("TIMETRA-DYNAMIC-SERVICES-MIB", "tmnxDynSvcNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxDynSvcNotifyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-DYNAMIC-SERVICES-MIB",
    **{"TmnxDynSrvAcctStatsType": TmnxDynSrvAcctStatsType,
       "timetraDynSrvMIBModule": timetraDynSrvMIBModule,
       "tmnxDynSvcConformance": tmnxDynSvcConformance,
       "tmnxDynSvcCompliances": tmnxDynSvcCompliances,
       "tmnxDynSvcCompliance": tmnxDynSvcCompliance,
       "tmnxDynSvcNotifyCompliance": tmnxDynSvcNotifyCompliance,
       "tmnxDynSvcGroups": tmnxDynSvcGroups,
       "tmnxDynSvcGroup": tmnxDynSvcGroup,
       "tmnxDynSvcNotifyObjsGroup": tmnxDynSvcNotifyObjsGroup,
       "tmnxDynSvcNotifyGroup": tmnxDynSvcNotifyGroup,
       "tmnxDynSvc": tmnxDynSvc,
       "tmnxDynSvcObjs": tmnxDynSvcObjs,
       "tmnxDynSvcPlcyTable": tmnxDynSvcPlcyTable,
       "tmnxDynSvcPlcyEntry": tmnxDynSvcPlcyEntry,
       "tmnxDynSvcPlcyName": tmnxDynSvcPlcyName,
       "tmnxDynSvcPlcyRowStatus": tmnxDynSvcPlcyRowStatus,
       "tmnxDynSvcPlcyLastCh": tmnxDynSvcPlcyLastCh,
       "tmnxDynSvcPlcyDescription": tmnxDynSvcPlcyDescription,
       "tmnxDynSvcPlcyScriptPlcy": tmnxDynSvcPlcyScriptPlcy,
       "tmnxDynSvcPlcyCliUser": tmnxDynSvcPlcyCliUser,
       "tmnxDynSvcPlcySapLimit": tmnxDynSvcPlcySapLimit,
       "tmnxDynSvcPlcyApTable": tmnxDynSvcPlcyApTable,
       "tmnxDynSvcPlcyApEntry": tmnxDynSvcPlcyApEntry,
       "tmnxDynSvcPlcyApIndex": tmnxDynSvcPlcyApIndex,
       "tmnxDynSvcPlcyApLastCh": tmnxDynSvcPlcyApLastCh,
       "tmnxDynSvcPlcyApName": tmnxDynSvcPlcyApName,
       "tmnxDynSvcPlcyApStatsType": tmnxDynSvcPlcyApStatsType,
       "tmnxDynSvcPlcyApUpdateInterval": tmnxDynSvcPlcyApUpdateInterval,
       "tmnxDynSvcPlcyApUpdateIvlJitter": tmnxDynSvcPlcyApUpdateIvlJitter,
       "tmnxDynSvcRange": tmnxDynSvcRange,
       "tmnxDynSvcRangeStart": tmnxDynSvcRangeStart,
       "tmnxDynSvcRangeEnd": tmnxDynSvcRangeEnd,
       "tmnxDynSvcSapTable": tmnxDynSvcSapTable,
       "tmnxDynSvcSapEntry": tmnxDynSvcSapEntry,
       "tmnxDynSvcSapAcctSessionId": tmnxDynSvcSapAcctSessionId,
       "tmnxDynSvcSapAcctSessionIdCtrl": tmnxDynSvcSapAcctSessionIdCtrl,
       "tmnxDynSvcSapPolicy": tmnxDynSvcSapPolicy,
       "tmnxDynSvcSapScriptsExecuted": tmnxDynSvcSapScriptsExecuted,
       "tmnxDynSvcSapScriptsSuccess": tmnxDynSvcSapScriptsSuccess,
       "tmnxDynSvcSapLastScriptAction": tmnxDynSvcSapLastScriptAction,
       "tmnxDynSvcSapLastScriptTime": tmnxDynSvcSapLastScriptTime,
       "tmnxDynSvcSapOrphaned": tmnxDynSvcSapOrphaned,
       "tmnxDynSvcSapService": tmnxDynSvcSapService,
       "tmnxDynSvcSapLastScriptParams": tmnxDynSvcSapLastScriptParams,
       "tmnxDynSvcSapAcctTable": tmnxDynSvcSapAcctTable,
       "tmnxDynSvcSapAcctEntry": tmnxDynSvcSapAcctEntry,
       "tmnxDynSvcSapAcctIndex": tmnxDynSvcSapAcctIndex,
       "tmnxDynSvcSapAcctAcctStatus": tmnxDynSvcSapAcctAcctStatus,
       "tmnxDynSvcSapAcctStatsType": tmnxDynSvcSapAcctStatsType,
       "tmnxDynSvcSapAcctAcctInterval": tmnxDynSvcSapAcctAcctInterval,
       "tmnxDynSvcRootObjTable": tmnxDynSvcRootObjTable,
       "tmnxDynSvcRootObjEntry": tmnxDynSvcRootObjEntry,
       "tmnxDynSvcRootObjIndex": tmnxDynSvcRootObjIndex,
       "tmnxDynSvcRootObjInstance": tmnxDynSvcRootObjInstance,
       "tmnxDynSvcRootObjOrphanTime": tmnxDynSvcRootObjOrphanTime,
       "tmnxDynSvcRootObjSnippetName": tmnxDynSvcRootObjSnippetName,
       "tmnxDynSvcRootObjSnippetInstance": tmnxDynSvcRootObjSnippetInstance,
       "tmnxDynSvcStatsTable": tmnxDynSvcStatsTable,
       "tmnxDynSvcStatsEntry": tmnxDynSvcStatsEntry,
       "tmnxDynSvcStatsId": tmnxDynSvcStatsId,
       "tmnxDynSvcStatsDescr": tmnxDynSvcStatsDescr,
       "tmnxDynSvcStatsVal": tmnxDynSvcStatsVal,
       "tmnxDynSvcSnippetTable": tmnxDynSvcSnippetTable,
       "tmnxDynSvcSnippetEntry": tmnxDynSvcSnippetEntry,
       "tmnxDynSvcSnippetName": tmnxDynSvcSnippetName,
       "tmnxDynSvcSnippetInstance": tmnxDynSvcSnippetInstance,
       "tmnxDynSvcSnippetRefCount": tmnxDynSvcSnippetRefCount,
       "tmnxDynSvcSnippetDictLength": tmnxDynSvcSnippetDictLength,
       "tmnxDynSvcSnippetRootObjTable": tmnxDynSvcSnippetRootObjTable,
       "tmnxDynSvcSnippetRootObjEntry": tmnxDynSvcSnippetRootObjEntry,
       "tmnxDynSvcSnippetRootObjIdx": tmnxDynSvcSnippetRootObjIdx,
       "tmnxDynSvcSnippetRootObjOid": tmnxDynSvcSnippetRootObjOid,
       "tmnxDynSvcSnippetRefTable": tmnxDynSvcSnippetRefTable,
       "tmnxDynSvcSnippetRefEntry": tmnxDynSvcSnippetRefEntry,
       "tmnxDynSvcSnippetRefIdx": tmnxDynSvcSnippetRefIdx,
       "tmnxDynSvcSnippetRefSnipName": tmnxDynSvcSnippetRefSnipName,
       "tmnxDynSvcSnippetRefSnipInst": tmnxDynSvcSnippetRefSnipInst,
       "tmnxDynSvcSnippetResIdTable": tmnxDynSvcSnippetResIdTable,
       "tmnxDynSvcSnippetResIdEntry": tmnxDynSvcSnippetResIdEntry,
       "tmnxDynSvcSnippetResIdIdx": tmnxDynSvcSnippetResIdIdx,
       "tmnxDynSvcSnippetResIdType": tmnxDynSvcSnippetResIdType,
       "tmnxDynSvcSnippetResIdValue": tmnxDynSvcSnippetResIdValue,
       "tmnxDynSvcTimer": tmnxDynSvcTimer,
       "tmnxDynSvcTimerAccSetupTimeout": tmnxDynSvcTimerAccSetupTimeout,
       "tmnxDynSvcPlcyTableLastCh": tmnxDynSvcPlcyTableLastCh,
       "tmnxDynSvcPlcyApTableLastCh": tmnxDynSvcPlcyApTableLastCh,
       "tmnxDynSvcSapTableLastCh": tmnxDynSvcSapTableLastCh,
       "tmnxDynSvcRootObjTableLastCh": tmnxDynSvcRootObjTableLastCh,
       "tmnxDynSvcNonStoredRootObjCount": tmnxDynSvcNonStoredRootObjCount,
       "tmnxDynSvcSnippetTableLastCh": tmnxDynSvcSnippetTableLastCh,
       "tmnxDynSvcSnipRootObjTblLastCh": tmnxDynSvcSnipRootObjTblLastCh,
       "tmnxDynSvcSnippetRefTableLastCh": tmnxDynSvcSnippetRefTableLastCh,
       "tmnxDynSvcSnippetResIdTblLastCh": tmnxDynSvcSnippetResIdTblLastCh,
       "tmnxDynSvcStatsLastClearedTime": tmnxDynSvcStatsLastClearedTime,
       "tmnxDynSvcNotificationObjs": tmnxDynSvcNotificationObjs,
       "tmnxDynSvcNotifDescription": tmnxDynSvcNotifDescription,
       "tmnxDynSvcNotifSapPortId": tmnxDynSvcNotifSapPortId,
       "tmnxDynSvcNotifSapEncapValue": tmnxDynSvcNotifSapEncapValue,
       "tmnxDynSvcNotifSapAcctSessionId": tmnxDynSvcNotifSapAcctSessionId,
       "tmnxDynSvcNotifyPrefix": tmnxDynSvcNotifyPrefix,
       "tmnxDynSvcNotifications": tmnxDynSvcNotifications,
       "tmnxDynSvcSapFailed": tmnxDynSvcSapFailed}
)
