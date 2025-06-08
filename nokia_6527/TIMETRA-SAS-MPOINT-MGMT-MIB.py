# SNMP MIB module (TIMETRA-SAS-MPOINT-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SAS-MPOINT-MGMT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:16 2025
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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(TAdaptationRule,
 TBurstSize) = mibBuilder.importSymbols(
    "TIMETRA-SAS-QOS-MIB",
    "TAdaptationRule",
    "TBurstSize")

(TItemDescription,
 TNamedItem) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem")


# MODULE-IDENTITY

timetraSASMpointMgmtMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 54)
)
if mibBuilder.loadTexts:
    timetraSASMpointMgmtMIBModule.setRevisions(
        ("1910-05-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TSASMpQueueIdTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("none", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3),
          ("queue4", 4),
          ("queue5", 5),
          ("queue6", 6),
          ("queue7", 7),
          ("queue8", 8))
    )



# MIB Managed Objects in the order of their OIDs

_TSASMpConformance_ObjectIdentity = ObjectIdentity
tSASMpConformance = _TSASMpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 54)
)
_TSASMpCompliances_ObjectIdentity = ObjectIdentity
tSASMpCompliances = _TSASMpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 54, 1)
)
_TSASMpGroups_ObjectIdentity = ObjectIdentity
tSASMpGroups = _TSASMpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 54, 2)
)
_TSASMpObjects_ObjectIdentity = ObjectIdentity
tSASMpObjects = _TSASMpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54)
)
_TSASMpGlobalObjs_ObjectIdentity = ObjectIdentity
tSASMpGlobalObjs = _TSASMpGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1)
)
_TSASMpBwPlcyTable_Object = MibTable
tSASMpBwPlcyTable = _TSASMpBwPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 1)
)
if mibBuilder.loadTexts:
    tSASMpBwPlcyTable.setStatus("current")
_TSASMpBwPlcyEntry_Object = MibTableRow
tSASMpBwPlcyEntry = _TSASMpBwPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 1, 1)
)
tSASMpBwPlcyEntry.setIndexNames(
    (0, "TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyName"),
)
if mibBuilder.loadTexts:
    tSASMpBwPlcyEntry.setStatus("current")
_TSASMpBwPlcyName_Type = TNamedItem
_TSASMpBwPlcyName_Object = MibTableColumn
tSASMpBwPlcyName = _TSASMpBwPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 1, 1, 1),
    _TSASMpBwPlcyName_Type()
)
tSASMpBwPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSASMpBwPlcyName.setStatus("current")
_TSASMpBwPlcyRowStatus_Type = RowStatus
_TSASMpBwPlcyRowStatus_Object = MibTableColumn
tSASMpBwPlcyRowStatus = _TSASMpBwPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 1, 1, 2),
    _TSASMpBwPlcyRowStatus_Type()
)
tSASMpBwPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASMpBwPlcyRowStatus.setStatus("current")
_TSASMpBwPlcyLastChanged_Type = TimeStamp
_TSASMpBwPlcyLastChanged_Object = MibTableColumn
tSASMpBwPlcyLastChanged = _TSASMpBwPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 1, 1, 3),
    _TSASMpBwPlcyLastChanged_Type()
)
tSASMpBwPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSASMpBwPlcyLastChanged.setStatus("current")


class _TSASMpBwPlcyDescription_Type(TItemDescription):
    """Custom type tSASMpBwPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TSASMpBwPlcyDescription_Type.__name__ = "TItemDescription"
_TSASMpBwPlcyDescription_Object = MibTableColumn
tSASMpBwPlcyDescription = _TSASMpBwPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 1, 1, 4),
    _TSASMpBwPlcyDescription_Type()
)
tSASMpBwPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASMpBwPlcyDescription.setStatus("current")


class _TSASMpBwPlcyIngrAggrRate_Type(Integer32):
    """Custom type tSASMpBwPlcyIngrAggrRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000),
    )


_TSASMpBwPlcyIngrAggrRate_Type.__name__ = "Integer32"
_TSASMpBwPlcyIngrAggrRate_Object = MibTableColumn
tSASMpBwPlcyIngrAggrRate = _TSASMpBwPlcyIngrAggrRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 1, 1, 5),
    _TSASMpBwPlcyIngrAggrRate_Type()
)
tSASMpBwPlcyIngrAggrRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASMpBwPlcyIngrAggrRate.setStatus("current")
if mibBuilder.loadTexts:
    tSASMpBwPlcyIngrAggrRate.setUnits("mega-bits-per-second")
_TSASMpBwPlcyQueueTable_Object = MibTable
tSASMpBwPlcyQueueTable = _TSASMpBwPlcyQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2)
)
if mibBuilder.loadTexts:
    tSASMpBwPlcyQueueTable.setStatus("current")
_TSASMpBwPlcyQueueEntry_Object = MibTableRow
tSASMpBwPlcyQueueEntry = _TSASMpBwPlcyQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1)
)
tSASMpBwPlcyQueueEntry.setIndexNames(
    (0, "TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyName"),
    (0, "TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyQueueId"),
)
if mibBuilder.loadTexts:
    tSASMpBwPlcyQueueEntry.setStatus("current")
_TSASMpBwPlcyQueueId_Type = TSASMpQueueIdTc
_TSASMpBwPlcyQueueId_Object = MibTableColumn
tSASMpBwPlcyQueueId = _TSASMpBwPlcyQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 1),
    _TSASMpBwPlcyQueueId_Type()
)
tSASMpBwPlcyQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSASMpBwPlcyQueueId.setStatus("current")


class _TSASMpBwPlcyCbs_Type(TBurstSize):
    """Custom type tSASMpBwPlcyCbs based on TBurstSize"""
    defaultValue = -1


_TSASMpBwPlcyCbs_Type.__name__ = "TBurstSize"
_TSASMpBwPlcyCbs_Object = MibTableColumn
tSASMpBwPlcyCbs = _TSASMpBwPlcyCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 2),
    _TSASMpBwPlcyCbs_Type()
)
tSASMpBwPlcyCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASMpBwPlcyCbs.setStatus("current")


class _TSASMpBwPlcyMbs_Type(Integer32):
    """Custom type tSASMpBwPlcyMbs based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 131072),
    )


_TSASMpBwPlcyMbs_Type.__name__ = "Integer32"
_TSASMpBwPlcyMbs_Object = MibTableColumn
tSASMpBwPlcyMbs = _TSASMpBwPlcyMbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 3),
    _TSASMpBwPlcyMbs_Type()
)
tSASMpBwPlcyMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASMpBwPlcyMbs.setStatus("current")


class _TSASMpBwPlcyCir_Type(Unsigned32):
    """Custom type tSASMpBwPlcyCir based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSASMpBwPlcyCir_Type.__name__ = "Unsigned32"
_TSASMpBwPlcyCir_Object = MibTableColumn
tSASMpBwPlcyCir = _TSASMpBwPlcyCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 4),
    _TSASMpBwPlcyCir_Type()
)
tSASMpBwPlcyCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASMpBwPlcyCir.setStatus("current")
if mibBuilder.loadTexts:
    tSASMpBwPlcyCir.setUnits("percent")


class _TSASMpBwPlcyPir_Type(Unsigned32):
    """Custom type tSASMpBwPlcyPir based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TSASMpBwPlcyPir_Type.__name__ = "Unsigned32"
_TSASMpBwPlcyPir_Object = MibTableColumn
tSASMpBwPlcyPir = _TSASMpBwPlcyPir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 5),
    _TSASMpBwPlcyPir_Type()
)
tSASMpBwPlcyPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASMpBwPlcyPir.setStatus("current")
if mibBuilder.loadTexts:
    tSASMpBwPlcyPir.setUnits("percent")


class _TSASMpBwPlcyCirAdaptation_Type(TAdaptationRule):
    """Custom type tSASMpBwPlcyCirAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TSASMpBwPlcyCirAdaptation_Type.__name__ = "TAdaptationRule"
_TSASMpBwPlcyCirAdaptation_Object = MibTableColumn
tSASMpBwPlcyCirAdaptation = _TSASMpBwPlcyCirAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 6),
    _TSASMpBwPlcyCirAdaptation_Type()
)
tSASMpBwPlcyCirAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASMpBwPlcyCirAdaptation.setStatus("current")


class _TSASMpBwPlcyPirAdaptation_Type(TAdaptationRule):
    """Custom type tSASMpBwPlcyPirAdaptation based on TAdaptationRule"""
    defaultValue = 3


_TSASMpBwPlcyPirAdaptation_Type.__name__ = "TAdaptationRule"
_TSASMpBwPlcyPirAdaptation_Object = MibTableColumn
tSASMpBwPlcyPirAdaptation = _TSASMpBwPlcyPirAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 7),
    _TSASMpBwPlcyPirAdaptation_Type()
)
tSASMpBwPlcyPirAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASMpBwPlcyPirAdaptation.setStatus("current")


class _TSASMpBwPlcyQueMgmtPlcy_Type(TNamedItem):
    """Custom type tSASMpBwPlcyQueMgmtPlcy based on TNamedItem"""
    defaultValue = OctetString("default")


_TSASMpBwPlcyQueMgmtPlcy_Type.__name__ = "TNamedItem"
_TSASMpBwPlcyQueMgmtPlcy_Object = MibTableColumn
tSASMpBwPlcyQueMgmtPlcy = _TSASMpBwPlcyQueMgmtPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 8),
    _TSASMpBwPlcyQueMgmtPlcy_Type()
)
tSASMpBwPlcyQueMgmtPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSASMpBwPlcyQueMgmtPlcy.setStatus("current")
_TSASMpBwPlcyQueStatsFwdPkts_Type = Counter64
_TSASMpBwPlcyQueStatsFwdPkts_Object = MibTableColumn
tSASMpBwPlcyQueStatsFwdPkts = _TSASMpBwPlcyQueStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 9),
    _TSASMpBwPlcyQueStatsFwdPkts_Type()
)
tSASMpBwPlcyQueStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSASMpBwPlcyQueStatsFwdPkts.setStatus("current")
_TSASMpBwPlcyQueStatsFwdOcts_Type = Counter64
_TSASMpBwPlcyQueStatsFwdOcts_Object = MibTableColumn
tSASMpBwPlcyQueStatsFwdOcts = _TSASMpBwPlcyQueStatsFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 10),
    _TSASMpBwPlcyQueStatsFwdOcts_Type()
)
tSASMpBwPlcyQueStatsFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSASMpBwPlcyQueStatsFwdOcts.setStatus("current")
_TSASMpBwPlcyQueStatsDroPkts_Type = Counter64
_TSASMpBwPlcyQueStatsDroPkts_Object = MibTableColumn
tSASMpBwPlcyQueStatsDroPkts = _TSASMpBwPlcyQueStatsDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 11),
    _TSASMpBwPlcyQueStatsDroPkts_Type()
)
tSASMpBwPlcyQueStatsDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSASMpBwPlcyQueStatsDroPkts.setStatus("current")
_TSASMpBwPlcyQueStatsDroOcts_Type = Counter64
_TSASMpBwPlcyQueStatsDroOcts_Object = MibTableColumn
tSASMpBwPlcyQueStatsDroOcts = _TSASMpBwPlcyQueStatsDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 1, 2, 1, 12),
    _TSASMpBwPlcyQueStatsDroOcts_Type()
)
tSASMpBwPlcyQueStatsDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSASMpBwPlcyQueStatsDroOcts.setStatus("current")
_TSASMpNotifyObjs_ObjectIdentity = ObjectIdentity
tSASMpNotifyObjs = _TSASMpNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 54, 2)
)
_TSASMpNotifyPrefix_ObjectIdentity = ObjectIdentity
tSASMpNotifyPrefix = _TSASMpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 54)
)
_TSASMpNotifications_ObjectIdentity = ObjectIdentity
tSASMpNotifications = _TSASMpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 54, 0)
)

# Managed Objects groups

tSASMpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 54, 2, 1)
)
tSASMpGlobalGroup.setObjects(
      *(("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyRowStatus"),
        ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyLastChanged"),
        ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyDescription"),
        ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyIngrAggrRate"),
        ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyCbs"),
        ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyMbs"),
        ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyCir"),
        ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyPir"),
        ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyCirAdaptation"),
        ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyPirAdaptation"),
        ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpBwPlcyQueMgmtPlcy"))
)
if mibBuilder.loadTexts:
    tSASMpGlobalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tSASMp7210V1v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 54, 1, 1)
)
tSASMp7210V1v0Compliance.setObjects(
    ("TIMETRA-SAS-MPOINT-MGMT-MIB", "tSASMpGlobalGroup")
)
if mibBuilder.loadTexts:
    tSASMp7210V1v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-MPOINT-MGMT-MIB",
    **{"TSASMpQueueIdTc": TSASMpQueueIdTc,
       "timetraSASMpointMgmtMIBModule": timetraSASMpointMgmtMIBModule,
       "tSASMpConformance": tSASMpConformance,
       "tSASMpCompliances": tSASMpCompliances,
       "tSASMp7210V1v0Compliance": tSASMp7210V1v0Compliance,
       "tSASMpGroups": tSASMpGroups,
       "tSASMpGlobalGroup": tSASMpGlobalGroup,
       "tSASMpObjects": tSASMpObjects,
       "tSASMpGlobalObjs": tSASMpGlobalObjs,
       "tSASMpBwPlcyTable": tSASMpBwPlcyTable,
       "tSASMpBwPlcyEntry": tSASMpBwPlcyEntry,
       "tSASMpBwPlcyName": tSASMpBwPlcyName,
       "tSASMpBwPlcyRowStatus": tSASMpBwPlcyRowStatus,
       "tSASMpBwPlcyLastChanged": tSASMpBwPlcyLastChanged,
       "tSASMpBwPlcyDescription": tSASMpBwPlcyDescription,
       "tSASMpBwPlcyIngrAggrRate": tSASMpBwPlcyIngrAggrRate,
       "tSASMpBwPlcyQueueTable": tSASMpBwPlcyQueueTable,
       "tSASMpBwPlcyQueueEntry": tSASMpBwPlcyQueueEntry,
       "tSASMpBwPlcyQueueId": tSASMpBwPlcyQueueId,
       "tSASMpBwPlcyCbs": tSASMpBwPlcyCbs,
       "tSASMpBwPlcyMbs": tSASMpBwPlcyMbs,
       "tSASMpBwPlcyCir": tSASMpBwPlcyCir,
       "tSASMpBwPlcyPir": tSASMpBwPlcyPir,
       "tSASMpBwPlcyCirAdaptation": tSASMpBwPlcyCirAdaptation,
       "tSASMpBwPlcyPirAdaptation": tSASMpBwPlcyPirAdaptation,
       "tSASMpBwPlcyQueMgmtPlcy": tSASMpBwPlcyQueMgmtPlcy,
       "tSASMpBwPlcyQueStatsFwdPkts": tSASMpBwPlcyQueStatsFwdPkts,
       "tSASMpBwPlcyQueStatsFwdOcts": tSASMpBwPlcyQueStatsFwdOcts,
       "tSASMpBwPlcyQueStatsDroPkts": tSASMpBwPlcyQueStatsDroPkts,
       "tSASMpBwPlcyQueStatsDroOcts": tSASMpBwPlcyQueStatsDroOcts,
       "tSASMpNotifyObjs": tSASMpNotifyObjs,
       "tSASMpNotifyPrefix": tSASMpNotifyPrefix,
       "tSASMpNotifications": tSASMpNotifications}
)
