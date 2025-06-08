# SNMP MIB module (FspR7-LAYER2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/FspR7-LAYER2-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:58 2025
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

(Counter64String,
 EntityClass,
 EntityIndex,
 LoopConfig,
 ProtectionMech,
 ProtectionMechCaps,
 ServiceImpairment,
 TrapAlarmSeverity,
 entityClass,
 entityIndex,
 fspR7,
 neEventLogIdentityTranslation,
 neEventLogTimeStamp,
 snmpProxyEntrySingleTargetOutNodeAgentStatus,
 snmpProxyServerSynchroStage) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "Counter64String",
    "EntityClass",
    "EntityIndex",
    "LoopConfig",
    "ProtectionMech",
    "ProtectionMechCaps",
    "ServiceImpairment",
    "TrapAlarmSeverity",
    "entityClass",
    "entityIndex",
    "fspR7",
    "neEventLogIdentityTranslation",
    "neEventLogTimeStamp",
    "snmpProxyEntrySingleTargetOutNodeAgentStatus",
    "snmpProxyServerSynchroStage")

(ApsDirection,
 ApsRevertMode,
 ApsRevertModeCaps,
 ApsType,
 FspR7APSCommand,
 FspR7APSCommandCaps,
 FspR7AdminState,
 FspR7AdminStateCaps,
 FspR7Conn,
 FspR7ConnCaps,
 FspR7ConnectState,
 FspR7EntitySecondaryStates,
 FspR7ForcedStatus,
 FspR7ForcedStatusCaps,
 FspR7FunctionCrs,
 FspR7Integer32Caps,
 FspR7InterfaceFunction,
 FspR7InterfaceType,
 FspR7InterfaceTypeCaps,
 FspR7OperState,
 FspR7PmReset,
 FspR7PmResetCaps,
 FspR7ProtectionRole,
 FspR7ProtectionType,
 FspR7RowStatusCaps,
 FspR7TypeCrs,
 FspR7TypeCrsCaps,
 FspR7Unsigned32Caps,
 FspR7YesNo,
 FspR7YesNoCaps) = mibBuilder.importSymbols(
    "FspR7-MIB",
    "ApsDirection",
    "ApsRevertMode",
    "ApsRevertModeCaps",
    "ApsType",
    "FspR7APSCommand",
    "FspR7APSCommandCaps",
    "FspR7AdminState",
    "FspR7AdminStateCaps",
    "FspR7Conn",
    "FspR7ConnCaps",
    "FspR7ConnectState",
    "FspR7EntitySecondaryStates",
    "FspR7ForcedStatus",
    "FspR7ForcedStatusCaps",
    "FspR7FunctionCrs",
    "FspR7Integer32Caps",
    "FspR7InterfaceFunction",
    "FspR7InterfaceType",
    "FspR7InterfaceTypeCaps",
    "FspR7OperState",
    "FspR7PmReset",
    "FspR7PmResetCaps",
    "FspR7ProtectionRole",
    "FspR7ProtectionType",
    "FspR7RowStatusCaps",
    "FspR7TypeCrs",
    "FspR7TypeCrsCaps",
    "FspR7Unsigned32Caps",
    "FspR7YesNo",
    "FspR7YesNoCaps")

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
 enterprises,
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2",
    "snmpModules")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

layer2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3)
)
if mibBuilder.loadTexts:
    layer2MIB.setRevisions(
        ("2011-02-21 00:00",
         "2010-10-29 00:00",
         "2010-10-22 00:00",
         "2010-08-31 00:00",
         "2010-06-14 00:00",
         "2010-03-24 00:00",
         "2009-11-20 00:00",
         "2009-06-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BridgeEntityIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class FspR7DisableEnable(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("disable", 1),
          ("enable", 2))
    )



class FspR7DisableEnableCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capDisable", 1),
          ("capEnable", 2))
    )


class FspR7Brigde(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("bridge1plus1", 1),
          ("bridge1for1", 2),
          ("bridge1plus1back2back", 3),
          ("bridge1for1extra", 4))
    )



class FspR7BrigdeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capBridge1plus1", 1),
          ("capBridge1for1", 2),
          ("capBridge1plus1back2back", 3),
          ("capBridge1for1extra", 4))
    )


class FspR7L2Brigde(TextualConvention, Integer32):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("bridge1plus1", 1),
          ("bridge1to1", 2))
    )



class FspR7L2BrigdeCaps(TextualConvention, Bits):
    status = "obsolete"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capBridge1plus1", 1),
          ("capBridge1to1", 2))
    )


class FspR7L2FlowType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("eline", 1),
          ("etree", 2),
          ("elan", 3))
    )



class FspR7L2FlowTypeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capEline", 1),
          ("capEtree", 2),
          ("capElan", 3))
    )


class FspR7L2LevelDomainMonitored(TextualConvention, Integer32):
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("notSupported", 1),
          ("levelMD0", 2),
          ("levelMD1", 3),
          ("levelMD2", 4),
          ("levelMD3", 5),
          ("levelMD4", 6),
          ("levelMD5", 7),
          ("levelMD6", 8),
          ("levelMD7", 9))
    )



class FspR7L2LevelDomainMonitoredCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capNotSupported", 1),
          ("capLevelMD0", 2),
          ("capLevelMD1", 3),
          ("capLevelMD2", 4),
          ("capLevelMD3", 5),
          ("capLevelMD4", 6),
          ("capLevelMD5", 7),
          ("capLevelMD6", 8),
          ("capLevelMD7", 9))
    )


class FspR7L2PmMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("enableAll", 1),
          ("enableCurrent", 2),
          ("disable", 3))
    )



class FspR7L2PmModeCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capEnableAll", 1),
          ("capEnableCurrent", 2),
          ("capDisable", 3))
    )


class FspR7L2StandingConditionTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100000,
              100001,
              100002,
              100003,
              100004,
              100005,
              100006,
              100007,
              100008,
              100009,
              100010,
              100011,
              100012,
              100013,
              100014,
              100015,
              100016,
              100019)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("oosDisabledL2", 100000),
          ("oosManagementL2", 100001),
          ("oosMaintenanceL2", 100002),
          ("oosAinsL2", 100003),
          ("serverSignalFailL2", 100004),
          ("mepNotPresentL2", 100005),
          ("priVidNotEqualExtVidL2", 100006),
          ("switchtoProtectionInhibitedL2", 100007),
          ("manswL2", 100008),
          ("sfCfmLevel0L2", 100009),
          ("sfCfmLevel1L2", 100010),
          ("sfCfmLevel2L2", 100011),
          ("sfCfmLevel3L2", 100012),
          ("sfCfmLevel4L2", 100013),
          ("sfCfmLevel5L2", 100014),
          ("sfCfmLevel6L2", 100015),
          ("sfCfmLevel7L2", 100016),
          ("switchtoWorkingInhibitedL2", 100019))
    )



class BridgeStandingConditionTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100017,
              100018)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("bridgeOosManagement", 100017),
          ("bridgeOosAins", 100018))
    )



class FspR7RedLinedState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("yes", 1),
          ("no", 2))
    )



class FspR7RedLinedStateCaps(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capYes", 1),
          ("capNo", 2))
    )


class QueueEntityIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Layer2EntitiesMIB_ObjectIdentity = ObjectIdentity
layer2EntitiesMIB = _Layer2EntitiesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11)
)
_FlowEntityTable_Object = MibTable
flowEntityTable = _FlowEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 10)
)
if mibBuilder.loadTexts:
    flowEntityTable.setStatus("current")
_FlowEntityEntry_Object = MibTableRow
flowEntityEntry = _FlowEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 10, 1)
)
flowEntityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowEntityEntry.setStatus("current")
_FlowEntityIndexEth_Type = EntityIndex
_FlowEntityIndexEth_Object = MibTableColumn
flowEntityIndexEth = _FlowEntityIndexEth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 10, 1, 1),
    _FlowEntityIndexEth_Type()
)
flowEntityIndexEth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    flowEntityIndexEth.setStatus("current")
_FlowEntityIndexFlow_Type = EntityIndex
_FlowEntityIndexFlow_Object = MibTableColumn
flowEntityIndexFlow = _FlowEntityIndexFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 10, 1, 2),
    _FlowEntityIndexFlow_Type()
)
flowEntityIndexFlow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    flowEntityIndexFlow.setStatus("current")
_FlowEntityClass_Type = EntityClass
_FlowEntityClass_Object = MibTableColumn
flowEntityClass = _FlowEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 10, 1, 3),
    _FlowEntityClass_Type()
)
flowEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityClass.setStatus("current")


class _FlowEntityClassInstanceNumber_Type(Integer32):
    """Custom type flowEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_FlowEntityClassInstanceNumber_Type.__name__ = "Integer32"
_FlowEntityClassInstanceNumber_Object = MibTableColumn
flowEntityClassInstanceNumber = _FlowEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 10, 1, 4),
    _FlowEntityClassInstanceNumber_Type()
)
flowEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityClassInstanceNumber.setStatus("current")
_FlowEntityIndexAid_Type = SnmpAdminString
_FlowEntityIndexAid_Object = MibTableColumn
flowEntityIndexAid = _FlowEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 10, 1, 5),
    _FlowEntityIndexAid_Type()
)
flowEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityIndexAid.setStatus("current")
_CtransEntityTable_Object = MibTable
ctransEntityTable = _CtransEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 11)
)
if mibBuilder.loadTexts:
    ctransEntityTable.setStatus("current")
_CtransEntityEntry_Object = MibTableRow
ctransEntityEntry = _CtransEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 11, 1)
)
ctransEntityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexCVlanId"),
)
if mibBuilder.loadTexts:
    ctransEntityEntry.setStatus("current")
_CtransEntityIndexEth_Type = EntityIndex
_CtransEntityIndexEth_Object = MibTableColumn
ctransEntityIndexEth = _CtransEntityIndexEth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 11, 1, 1),
    _CtransEntityIndexEth_Type()
)
ctransEntityIndexEth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctransEntityIndexEth.setStatus("current")
_CtransEntityIndexCVlanId_Type = EntityIndex
_CtransEntityIndexCVlanId_Object = MibTableColumn
ctransEntityIndexCVlanId = _CtransEntityIndexCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 11, 1, 2),
    _CtransEntityIndexCVlanId_Type()
)
ctransEntityIndexCVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctransEntityIndexCVlanId.setStatus("current")
_CtransEntityClass_Type = EntityClass
_CtransEntityClass_Object = MibTableColumn
ctransEntityClass = _CtransEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 11, 1, 3),
    _CtransEntityClass_Type()
)
ctransEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityClass.setStatus("current")


class _CtransEntityClassInstanceNumber_Type(Integer32):
    """Custom type ctransEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CtransEntityClassInstanceNumber_Type.__name__ = "Integer32"
_CtransEntityClassInstanceNumber_Object = MibTableColumn
ctransEntityClassInstanceNumber = _CtransEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 11, 1, 4),
    _CtransEntityClassInstanceNumber_Type()
)
ctransEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityClassInstanceNumber.setStatus("current")
_CtransEntityIndexAid_Type = SnmpAdminString
_CtransEntityIndexAid_Object = MibTableColumn
ctransEntityIndexAid = _CtransEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 11, 1, 5),
    _CtransEntityIndexAid_Type()
)
ctransEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityIndexAid.setStatus("current")
_BridgeEntityTable_Object = MibTable
bridgeEntityTable = _BridgeEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 12)
)
if mibBuilder.loadTexts:
    bridgeEntityTable.setStatus("current")
_BridgeEntityEntry_Object = MibTableRow
bridgeEntityEntry = _BridgeEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 12, 1)
)
bridgeEntityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
)
if mibBuilder.loadTexts:
    bridgeEntityEntry.setStatus("current")
_BridgeEntityContainedIn_Type = EntityIndex
_BridgeEntityContainedIn_Object = MibTableColumn
bridgeEntityContainedIn = _BridgeEntityContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 12, 1, 1),
    _BridgeEntityContainedIn_Type()
)
bridgeEntityContainedIn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeEntityContainedIn.setStatus("current")
_BridgeEntitySvid_Type = BridgeEntityIndex
_BridgeEntitySvid_Object = MibTableColumn
bridgeEntitySvid = _BridgeEntitySvid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 12, 1, 2),
    _BridgeEntitySvid_Type()
)
bridgeEntitySvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeEntitySvid.setStatus("current")
_BridgeEntityClass_Type = EntityClass
_BridgeEntityClass_Object = MibTableColumn
bridgeEntityClass = _BridgeEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 12, 1, 3),
    _BridgeEntityClass_Type()
)
bridgeEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityClass.setStatus("current")


class _BridgeEntityClassInstanceNumber_Type(Integer32):
    """Custom type bridgeEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_BridgeEntityClassInstanceNumber_Type.__name__ = "Integer32"
_BridgeEntityClassInstanceNumber_Object = MibTableColumn
bridgeEntityClassInstanceNumber = _BridgeEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 12, 1, 4),
    _BridgeEntityClassInstanceNumber_Type()
)
bridgeEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityClassInstanceNumber.setStatus("current")
_BridgeEntityIndexAid_Type = SnmpAdminString
_BridgeEntityIndexAid_Object = MibTableColumn
bridgeEntityIndexAid = _BridgeEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 12, 1, 5),
    _BridgeEntityIndexAid_Type()
)
bridgeEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityIndexAid.setStatus("current")
_PolicerOnFlowEntityTable_Object = MibTable
policerOnFlowEntityTable = _PolicerOnFlowEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 13)
)
if mibBuilder.loadTexts:
    policerOnFlowEntityTable.setStatus("current")
_PolicerOnFlowEntityEntry_Object = MibTableRow
policerOnFlowEntityEntry = _PolicerOnFlowEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 13, 1)
)
policerOnFlowEntityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexPolicer"),
)
if mibBuilder.loadTexts:
    policerOnFlowEntityEntry.setStatus("current")
_PolicerOnFlowEntityIndexEth_Type = EntityIndex
_PolicerOnFlowEntityIndexEth_Object = MibTableColumn
policerOnFlowEntityIndexEth = _PolicerOnFlowEntityIndexEth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 13, 1, 1),
    _PolicerOnFlowEntityIndexEth_Type()
)
policerOnFlowEntityIndexEth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    policerOnFlowEntityIndexEth.setStatus("current")
_PolicerOnFlowEntityIndexFlow_Type = EntityIndex
_PolicerOnFlowEntityIndexFlow_Object = MibTableColumn
policerOnFlowEntityIndexFlow = _PolicerOnFlowEntityIndexFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 13, 1, 2),
    _PolicerOnFlowEntityIndexFlow_Type()
)
policerOnFlowEntityIndexFlow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    policerOnFlowEntityIndexFlow.setStatus("current")
_PolicerOnFlowEntityIndexPolicer_Type = EntityIndex
_PolicerOnFlowEntityIndexPolicer_Object = MibTableColumn
policerOnFlowEntityIndexPolicer = _PolicerOnFlowEntityIndexPolicer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 13, 1, 3),
    _PolicerOnFlowEntityIndexPolicer_Type()
)
policerOnFlowEntityIndexPolicer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    policerOnFlowEntityIndexPolicer.setStatus("current")
_PolicerOnFlowEntityClass_Type = EntityClass
_PolicerOnFlowEntityClass_Object = MibTableColumn
policerOnFlowEntityClass = _PolicerOnFlowEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 13, 1, 4),
    _PolicerOnFlowEntityClass_Type()
)
policerOnFlowEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOnFlowEntityClass.setStatus("current")


class _PolicerOnFlowEntityClassInstanceNumber_Type(Integer32):
    """Custom type policerOnFlowEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_PolicerOnFlowEntityClassInstanceNumber_Type.__name__ = "Integer32"
_PolicerOnFlowEntityClassInstanceNumber_Object = MibTableColumn
policerOnFlowEntityClassInstanceNumber = _PolicerOnFlowEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 13, 1, 5),
    _PolicerOnFlowEntityClassInstanceNumber_Type()
)
policerOnFlowEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOnFlowEntityClassInstanceNumber.setStatus("current")
_PolicerOnFlowEntityIndexAid_Type = SnmpAdminString
_PolicerOnFlowEntityIndexAid_Object = MibTableColumn
policerOnFlowEntityIndexAid = _PolicerOnFlowEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 13, 1, 6),
    _PolicerOnFlowEntityIndexAid_Type()
)
policerOnFlowEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOnFlowEntityIndexAid.setStatus("current")
_QueOnPortEntityTable_Object = MibTable
queOnPortEntityTable = _QueOnPortEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 15)
)
if mibBuilder.loadTexts:
    queOnPortEntityTable.setStatus("current")
_QueOnPortEntityEntry_Object = MibTableRow
queOnPortEntityEntry = _QueOnPortEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 15, 1)
)
queOnPortEntityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexPrio"),
)
if mibBuilder.loadTexts:
    queOnPortEntityEntry.setStatus("current")
_QueOnPortEntityIndexEth_Type = EntityIndex
_QueOnPortEntityIndexEth_Object = MibTableColumn
queOnPortEntityIndexEth = _QueOnPortEntityIndexEth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 15, 1, 1),
    _QueOnPortEntityIndexEth_Type()
)
queOnPortEntityIndexEth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    queOnPortEntityIndexEth.setStatus("current")
_QueOnPortEntityIndexPrio_Type = EntityIndex
_QueOnPortEntityIndexPrio_Object = MibTableColumn
queOnPortEntityIndexPrio = _QueOnPortEntityIndexPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 15, 1, 2),
    _QueOnPortEntityIndexPrio_Type()
)
queOnPortEntityIndexPrio.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    queOnPortEntityIndexPrio.setStatus("current")
_QueOnPortEntityClass_Type = EntityClass
_QueOnPortEntityClass_Object = MibTableColumn
queOnPortEntityClass = _QueOnPortEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 15, 1, 3),
    _QueOnPortEntityClass_Type()
)
queOnPortEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnPortEntityClass.setStatus("current")


class _QueOnPortEntityClassInstanceNumber_Type(Integer32):
    """Custom type queOnPortEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_QueOnPortEntityClassInstanceNumber_Type.__name__ = "Integer32"
_QueOnPortEntityClassInstanceNumber_Object = MibTableColumn
queOnPortEntityClassInstanceNumber = _QueOnPortEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 15, 1, 4),
    _QueOnPortEntityClassInstanceNumber_Type()
)
queOnPortEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnPortEntityClassInstanceNumber.setStatus("current")
_QueOnPortEntityIndexAid_Type = SnmpAdminString
_QueOnPortEntityIndexAid_Object = MibTableColumn
queOnPortEntityIndexAid = _QueOnPortEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 15, 1, 5),
    _QueOnPortEntityIndexAid_Type()
)
queOnPortEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnPortEntityIndexAid.setStatus("current")
_QueOnFlowEntityTable_Object = MibTable
queOnFlowEntityTable = _QueOnFlowEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 16)
)
if mibBuilder.loadTexts:
    queOnFlowEntityTable.setStatus("current")
_QueOnFlowEntityEntry_Object = MibTableRow
queOnFlowEntityEntry = _QueOnFlowEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 16, 1)
)
queOnFlowEntityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexPrio"),
)
if mibBuilder.loadTexts:
    queOnFlowEntityEntry.setStatus("current")
_QueOnFlowEntityIndexEth_Type = EntityIndex
_QueOnFlowEntityIndexEth_Object = MibTableColumn
queOnFlowEntityIndexEth = _QueOnFlowEntityIndexEth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 16, 1, 1),
    _QueOnFlowEntityIndexEth_Type()
)
queOnFlowEntityIndexEth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    queOnFlowEntityIndexEth.setStatus("current")
_QueOnFlowEntityIndexFlow_Type = EntityIndex
_QueOnFlowEntityIndexFlow_Object = MibTableColumn
queOnFlowEntityIndexFlow = _QueOnFlowEntityIndexFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 16, 1, 2),
    _QueOnFlowEntityIndexFlow_Type()
)
queOnFlowEntityIndexFlow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    queOnFlowEntityIndexFlow.setStatus("current")
_QueOnFlowEntityIndexPrio_Type = EntityIndex
_QueOnFlowEntityIndexPrio_Object = MibTableColumn
queOnFlowEntityIndexPrio = _QueOnFlowEntityIndexPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 16, 1, 3),
    _QueOnFlowEntityIndexPrio_Type()
)
queOnFlowEntityIndexPrio.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    queOnFlowEntityIndexPrio.setStatus("current")
_QueOnFlowEntityClass_Type = EntityClass
_QueOnFlowEntityClass_Object = MibTableColumn
queOnFlowEntityClass = _QueOnFlowEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 16, 1, 4),
    _QueOnFlowEntityClass_Type()
)
queOnFlowEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnFlowEntityClass.setStatus("current")


class _QueOnFlowEntityClassInstanceNumber_Type(Integer32):
    """Custom type queOnFlowEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_QueOnFlowEntityClassInstanceNumber_Type.__name__ = "Integer32"
_QueOnFlowEntityClassInstanceNumber_Object = MibTableColumn
queOnFlowEntityClassInstanceNumber = _QueOnFlowEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 16, 1, 5),
    _QueOnFlowEntityClassInstanceNumber_Type()
)
queOnFlowEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnFlowEntityClassInstanceNumber.setStatus("current")
_QueOnFlowEntityIndexAid_Type = SnmpAdminString
_QueOnFlowEntityIndexAid_Object = MibTableColumn
queOnFlowEntityIndexAid = _QueOnFlowEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 16, 1, 6),
    _QueOnFlowEntityIndexAid_Type()
)
queOnFlowEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnFlowEntityIndexAid.setStatus("current")
_QueOnBridgeEntityTable_Object = MibTable
queOnBridgeEntityTable = _QueOnBridgeEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 17)
)
if mibBuilder.loadTexts:
    queOnBridgeEntityTable.setStatus("current")
_QueOnBridgeEntityEntry_Object = MibTableRow
queOnBridgeEntityEntry = _QueOnBridgeEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 17, 1)
)
queOnBridgeEntityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityIndex"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityPrio"),
)
if mibBuilder.loadTexts:
    queOnBridgeEntityEntry.setStatus("current")
_QueOnBridgeEntityIndex_Type = QueueEntityIndex
_QueOnBridgeEntityIndex_Object = MibTableColumn
queOnBridgeEntityIndex = _QueOnBridgeEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 17, 1, 1),
    _QueOnBridgeEntityIndex_Type()
)
queOnBridgeEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queOnBridgeEntityIndex.setStatus("current")
_QueOnBridgeEntitySvid_Type = QueueEntityIndex
_QueOnBridgeEntitySvid_Object = MibTableColumn
queOnBridgeEntitySvid = _QueOnBridgeEntitySvid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 17, 1, 2),
    _QueOnBridgeEntitySvid_Type()
)
queOnBridgeEntitySvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queOnBridgeEntitySvid.setStatus("current")
_QueOnBridgeEntityPrio_Type = QueueEntityIndex
_QueOnBridgeEntityPrio_Object = MibTableColumn
queOnBridgeEntityPrio = _QueOnBridgeEntityPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 17, 1, 3),
    _QueOnBridgeEntityPrio_Type()
)
queOnBridgeEntityPrio.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queOnBridgeEntityPrio.setStatus("current")
_QueOnBridgeEntityClass_Type = EntityClass
_QueOnBridgeEntityClass_Object = MibTableColumn
queOnBridgeEntityClass = _QueOnBridgeEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 17, 1, 4),
    _QueOnBridgeEntityClass_Type()
)
queOnBridgeEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityClass.setStatus("current")


class _QueOnBridgeEntityClassInstanceNumber_Type(Integer32):
    """Custom type queOnBridgeEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_QueOnBridgeEntityClassInstanceNumber_Type.__name__ = "Integer32"
_QueOnBridgeEntityClassInstanceNumber_Object = MibTableColumn
queOnBridgeEntityClassInstanceNumber = _QueOnBridgeEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 17, 1, 5),
    _QueOnBridgeEntityClassInstanceNumber_Type()
)
queOnBridgeEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityClassInstanceNumber.setStatus("current")
_QueOnBridgeEntityIndexAid_Type = SnmpAdminString
_QueOnBridgeEntityIndexAid_Object = MibTableColumn
queOnBridgeEntityIndexAid = _QueOnBridgeEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 11, 17, 1, 6),
    _QueOnBridgeEntityIndexAid_Type()
)
queOnBridgeEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityIndexAid.setStatus("current")
_Layer2ProvisioningMIB_ObjectIdentity = ObjectIdentity
layer2ProvisioningMIB = _Layer2ProvisioningMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12)
)
_FlowProvisioning_ObjectIdentity = ObjectIdentity
flowProvisioning = _FlowProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11)
)
_FlowEntityProvisionTable_Object = MibTable
flowEntityProvisionTable = _FlowEntityProvisionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11)
)
if mibBuilder.loadTexts:
    flowEntityProvisionTable.setStatus("current")
_FlowEntityProvisionEntry_Object = MibTableRow
flowEntityProvisionEntry = _FlowEntityProvisionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1)
)
flowEntityProvisionEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowEntityProvisionEntry.setStatus("current")
_FlowEntityProvisionRowStatus_Type = RowStatus
_FlowEntityProvisionRowStatus_Object = MibTableColumn
flowEntityProvisionRowStatus = _FlowEntityProvisionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 1),
    _FlowEntityProvisionRowStatus_Type()
)
flowEntityProvisionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionRowStatus.setStatus("current")
_FlowEntityProvisionType_Type = FspR7InterfaceType
_FlowEntityProvisionType_Object = MibTableColumn
flowEntityProvisionType = _FlowEntityProvisionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 2),
    _FlowEntityProvisionType_Type()
)
flowEntityProvisionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionType.setStatus("current")
_FlowEntityProvisionAdmin_Type = FspR7AdminState
_FlowEntityProvisionAdmin_Object = MibTableColumn
flowEntityProvisionAdmin = _FlowEntityProvisionAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 3),
    _FlowEntityProvisionAdmin_Type()
)
flowEntityProvisionAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionAdmin.setStatus("current")
_FlowEntityProvisionAlias_Type = SnmpAdminString
_FlowEntityProvisionAlias_Object = MibTableColumn
flowEntityProvisionAlias = _FlowEntityProvisionAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 4),
    _FlowEntityProvisionAlias_Type()
)
flowEntityProvisionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionAlias.setStatus("current")


class _FlowEntityProvisionPopCtagRcv_Type(Unsigned32):
    """Custom type flowEntityProvisionPopCtagRcv based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionPopCtagRcv_Type.__name__ = "Unsigned32"
_FlowEntityProvisionPopCtagRcv_Object = MibTableColumn
flowEntityProvisionPopCtagRcv = _FlowEntityProvisionPopCtagRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 5),
    _FlowEntityProvisionPopCtagRcv_Type()
)
flowEntityProvisionPopCtagRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionPopCtagRcv.setStatus("current")


class _FlowEntityProvisionPopCtagTrmt_Type(Unsigned32):
    """Custom type flowEntityProvisionPopCtagTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionPopCtagTrmt_Type.__name__ = "Unsigned32"
_FlowEntityProvisionPopCtagTrmt_Object = MibTableColumn
flowEntityProvisionPopCtagTrmt = _FlowEntityProvisionPopCtagTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 6),
    _FlowEntityProvisionPopCtagTrmt_Type()
)
flowEntityProvisionPopCtagTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionPopCtagTrmt.setStatus("current")
_FlowEntityProvisionCvidRegisteredInFlow_Type = SnmpAdminString
_FlowEntityProvisionCvidRegisteredInFlow_Object = MibTableColumn
flowEntityProvisionCvidRegisteredInFlow = _FlowEntityProvisionCvidRegisteredInFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 7),
    _FlowEntityProvisionCvidRegisteredInFlow_Type()
)
flowEntityProvisionCvidRegisteredInFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionCvidRegisteredInFlow.setStatus("current")


class _FlowEntityProvisionExternalVid_Type(Unsigned32):
    """Custom type flowEntityProvisionExternalVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionExternalVid_Type.__name__ = "Unsigned32"
_FlowEntityProvisionExternalVid_Object = MibTableColumn
flowEntityProvisionExternalVid = _FlowEntityProvisionExternalVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 8),
    _FlowEntityProvisionExternalVid_Type()
)
flowEntityProvisionExternalVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionExternalVid.setStatus("current")
_FlowEntityProvisionPmMode_Type = FspR7L2PmMode
_FlowEntityProvisionPmMode_Object = MibTableColumn
flowEntityProvisionPmMode = _FlowEntityProvisionPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 9),
    _FlowEntityProvisionPmMode_Type()
)
flowEntityProvisionPmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionPmMode.setStatus("current")
_FlowEntityProvisionShape_Type = FspR7DisableEnable
_FlowEntityProvisionShape_Object = MibTableColumn
flowEntityProvisionShape = _FlowEntityProvisionShape_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 10),
    _FlowEntityProvisionShape_Type()
)
flowEntityProvisionShape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionShape.setStatus("current")
_FlowEntityProvisionPolice_Type = FspR7DisableEnable
_FlowEntityProvisionPolice_Object = MibTableColumn
flowEntityProvisionPolice = _FlowEntityProvisionPolice_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 11),
    _FlowEntityProvisionPolice_Type()
)
flowEntityProvisionPolice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionPolice.setStatus("current")


class _FlowEntityProvisionDefaultEvcCos_Type(Integer32):
    """Custom type flowEntityProvisionDefaultEvcCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_FlowEntityProvisionDefaultEvcCos_Type.__name__ = "Integer32"
_FlowEntityProvisionDefaultEvcCos_Object = MibTableColumn
flowEntityProvisionDefaultEvcCos = _FlowEntityProvisionDefaultEvcCos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 12),
    _FlowEntityProvisionDefaultEvcCos_Type()
)
flowEntityProvisionDefaultEvcCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultEvcCos.setStatus("current")
_FlowEntityProvisionCirRcv_Type = Unsigned32
_FlowEntityProvisionCirRcv_Object = MibTableColumn
flowEntityProvisionCirRcv = _FlowEntityProvisionCirRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 13),
    _FlowEntityProvisionCirRcv_Type()
)
flowEntityProvisionCirRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionCirRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionCirRcv.setUnits("Mbit/s")
_FlowEntityProvisionCirTrmt_Type = Unsigned32
_FlowEntityProvisionCirTrmt_Object = MibTableColumn
flowEntityProvisionCirTrmt = _FlowEntityProvisionCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 14),
    _FlowEntityProvisionCirTrmt_Type()
)
flowEntityProvisionCirTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionCirTrmt.setUnits("Mbit/s")


class _FlowEntityProvisionCbsRcv_Type(Unsigned32):
    """Custom type flowEntityProvisionCbsRcv based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26214400),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionCbsRcv_Type.__name__ = "Unsigned32"
_FlowEntityProvisionCbsRcv_Object = MibTableColumn
flowEntityProvisionCbsRcv = _FlowEntityProvisionCbsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 15),
    _FlowEntityProvisionCbsRcv_Type()
)
flowEntityProvisionCbsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionCbsRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionCbsRcv.setUnits("bytes")


class _FlowEntityProvisionCbsTrmt_Type(Unsigned32):
    """Custom type flowEntityProvisionCbsTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionCbsTrmt_Type.__name__ = "Unsigned32"
_FlowEntityProvisionCbsTrmt_Object = MibTableColumn
flowEntityProvisionCbsTrmt = _FlowEntityProvisionCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 16),
    _FlowEntityProvisionCbsTrmt_Type()
)
flowEntityProvisionCbsTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionCbsTrmt.setUnits("Kbytes")


class _FlowEntityProvisionPushPvidTrmt_Type(Unsigned32):
    """Custom type flowEntityProvisionPushPvidTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionPushPvidTrmt_Type.__name__ = "Unsigned32"
_FlowEntityProvisionPushPvidTrmt_Object = MibTableColumn
flowEntityProvisionPushPvidTrmt = _FlowEntityProvisionPushPvidTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 17),
    _FlowEntityProvisionPushPvidTrmt_Type()
)
flowEntityProvisionPushPvidTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionPushPvidTrmt.setStatus("current")


class _FlowEntityProvisionPrioPvidTrmt_Type(Unsigned32):
    """Custom type flowEntityProvisionPrioPvidTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionPrioPvidTrmt_Type.__name__ = "Unsigned32"
_FlowEntityProvisionPrioPvidTrmt_Object = MibTableColumn
flowEntityProvisionPrioPvidTrmt = _FlowEntityProvisionPrioPvidTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 18),
    _FlowEntityProvisionPrioPvidTrmt_Type()
)
flowEntityProvisionPrioPvidTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionPrioPvidTrmt.setStatus("current")
_FlowEntityProvisionRedLineState_Type = FspR7RedLinedState
_FlowEntityProvisionRedLineState_Object = MibTableColumn
flowEntityProvisionRedLineState = _FlowEntityProvisionRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 19),
    _FlowEntityProvisionRedLineState_Type()
)
flowEntityProvisionRedLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionRedLineState.setStatus("current")
_FlowEntityProvisionTunnelAid_Type = SnmpAdminString
_FlowEntityProvisionTunnelAid_Object = MibTableColumn
flowEntityProvisionTunnelAid = _FlowEntityProvisionTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 11, 1, 20),
    _FlowEntityProvisionTunnelAid_Type()
)
flowEntityProvisionTunnelAid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityProvisionTunnelAid.setStatus("current")
_FlowEntityProvisionCapTable_Object = MibTable
flowEntityProvisionCapTable = _FlowEntityProvisionCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12)
)
if mibBuilder.loadTexts:
    flowEntityProvisionCapTable.setStatus("current")
_FlowEntityProvisionCapEntry_Object = MibTableRow
flowEntityProvisionCapEntry = _FlowEntityProvisionCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1)
)
flowEntityProvisionCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowEntityProvisionCapEntry.setStatus("current")
_FlowEntityProvisionCapRowStatus_Type = FspR7RowStatusCaps
_FlowEntityProvisionCapRowStatus_Object = MibTableColumn
flowEntityProvisionCapRowStatus = _FlowEntityProvisionCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 1),
    _FlowEntityProvisionCapRowStatus_Type()
)
flowEntityProvisionCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapRowStatus.setStatus("current")
_FlowEntityProvisionCapType_Type = FspR7InterfaceTypeCaps
_FlowEntityProvisionCapType_Object = MibTableColumn
flowEntityProvisionCapType = _FlowEntityProvisionCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 2),
    _FlowEntityProvisionCapType_Type()
)
flowEntityProvisionCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapType.setStatus("current")
_FlowEntityProvisionCapAdmin_Type = FspR7AdminStateCaps
_FlowEntityProvisionCapAdmin_Object = MibTableColumn
flowEntityProvisionCapAdmin = _FlowEntityProvisionCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 3),
    _FlowEntityProvisionCapAdmin_Type()
)
flowEntityProvisionCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapAdmin.setStatus("current")
_FlowEntityProvisionCapAlias_Type = Integer32
_FlowEntityProvisionCapAlias_Object = MibTableColumn
flowEntityProvisionCapAlias = _FlowEntityProvisionCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 4),
    _FlowEntityProvisionCapAlias_Type()
)
flowEntityProvisionCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapAlias.setStatus("current")
_FlowEntityProvisionCapPopCtagRcv_Type = Unsigned32
_FlowEntityProvisionCapPopCtagRcv_Object = MibTableColumn
flowEntityProvisionCapPopCtagRcv = _FlowEntityProvisionCapPopCtagRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 5),
    _FlowEntityProvisionCapPopCtagRcv_Type()
)
flowEntityProvisionCapPopCtagRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapPopCtagRcv.setStatus("current")
_FlowEntityProvisionCapPopCtagTrmt_Type = Unsigned32
_FlowEntityProvisionCapPopCtagTrmt_Object = MibTableColumn
flowEntityProvisionCapPopCtagTrmt = _FlowEntityProvisionCapPopCtagTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 6),
    _FlowEntityProvisionCapPopCtagTrmt_Type()
)
flowEntityProvisionCapPopCtagTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapPopCtagTrmt.setStatus("current")
_FlowEntityProvisionCapCvidRegisteredInFlow_Type = Integer32
_FlowEntityProvisionCapCvidRegisteredInFlow_Object = MibTableColumn
flowEntityProvisionCapCvidRegisteredInFlow = _FlowEntityProvisionCapCvidRegisteredInFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 7),
    _FlowEntityProvisionCapCvidRegisteredInFlow_Type()
)
flowEntityProvisionCapCvidRegisteredInFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapCvidRegisteredInFlow.setStatus("current")
_FlowEntityProvisionCapExternalVid_Type = Unsigned32
_FlowEntityProvisionCapExternalVid_Object = MibTableColumn
flowEntityProvisionCapExternalVid = _FlowEntityProvisionCapExternalVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 8),
    _FlowEntityProvisionCapExternalVid_Type()
)
flowEntityProvisionCapExternalVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapExternalVid.setStatus("current")
_FlowEntityProvisionCapPmMode_Type = FspR7L2PmModeCaps
_FlowEntityProvisionCapPmMode_Object = MibTableColumn
flowEntityProvisionCapPmMode = _FlowEntityProvisionCapPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 9),
    _FlowEntityProvisionCapPmMode_Type()
)
flowEntityProvisionCapPmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapPmMode.setStatus("current")
_FlowEntityProvisionCapShape_Type = FspR7DisableEnableCaps
_FlowEntityProvisionCapShape_Object = MibTableColumn
flowEntityProvisionCapShape = _FlowEntityProvisionCapShape_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 10),
    _FlowEntityProvisionCapShape_Type()
)
flowEntityProvisionCapShape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapShape.setStatus("current")
_FlowEntityProvisionCapPolice_Type = FspR7DisableEnableCaps
_FlowEntityProvisionCapPolice_Object = MibTableColumn
flowEntityProvisionCapPolice = _FlowEntityProvisionCapPolice_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 11),
    _FlowEntityProvisionCapPolice_Type()
)
flowEntityProvisionCapPolice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapPolice.setStatus("current")
_FlowEntityProvisionCapDefaultEvcCos_Type = FspR7Integer32Caps
_FlowEntityProvisionCapDefaultEvcCos_Object = MibTableColumn
flowEntityProvisionCapDefaultEvcCos = _FlowEntityProvisionCapDefaultEvcCos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 12),
    _FlowEntityProvisionCapDefaultEvcCos_Type()
)
flowEntityProvisionCapDefaultEvcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapDefaultEvcCos.setStatus("current")
_FlowEntityProvisionCapCirRcv_Type = FspR7Unsigned32Caps
_FlowEntityProvisionCapCirRcv_Object = MibTableColumn
flowEntityProvisionCapCirRcv = _FlowEntityProvisionCapCirRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 13),
    _FlowEntityProvisionCapCirRcv_Type()
)
flowEntityProvisionCapCirRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapCirRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionCapCirRcv.setUnits("Mbit/s")
_FlowEntityProvisionCapCirTrmt_Type = FspR7Unsigned32Caps
_FlowEntityProvisionCapCirTrmt_Object = MibTableColumn
flowEntityProvisionCapCirTrmt = _FlowEntityProvisionCapCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 14),
    _FlowEntityProvisionCapCirTrmt_Type()
)
flowEntityProvisionCapCirTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionCapCirTrmt.setUnits("Mbit/s")
_FlowEntityProvisionCapCbsRcv_Type = Unsigned32
_FlowEntityProvisionCapCbsRcv_Object = MibTableColumn
flowEntityProvisionCapCbsRcv = _FlowEntityProvisionCapCbsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 15),
    _FlowEntityProvisionCapCbsRcv_Type()
)
flowEntityProvisionCapCbsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapCbsRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionCapCbsRcv.setUnits("bytes")
_FlowEntityProvisionCapCbsTrmt_Type = FspR7Unsigned32Caps
_FlowEntityProvisionCapCbsTrmt_Object = MibTableColumn
flowEntityProvisionCapCbsTrmt = _FlowEntityProvisionCapCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 16),
    _FlowEntityProvisionCapCbsTrmt_Type()
)
flowEntityProvisionCapCbsTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionCapCbsTrmt.setUnits("Kbytes")
_FlowEntityProvisionCapPushPvidTrmt_Type = Unsigned32
_FlowEntityProvisionCapPushPvidTrmt_Object = MibTableColumn
flowEntityProvisionCapPushPvidTrmt = _FlowEntityProvisionCapPushPvidTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 17),
    _FlowEntityProvisionCapPushPvidTrmt_Type()
)
flowEntityProvisionCapPushPvidTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapPushPvidTrmt.setStatus("current")
_FlowEntityProvisionCapPrioPvidTrmt_Type = FspR7Unsigned32Caps
_FlowEntityProvisionCapPrioPvidTrmt_Object = MibTableColumn
flowEntityProvisionCapPrioPvidTrmt = _FlowEntityProvisionCapPrioPvidTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 18),
    _FlowEntityProvisionCapPrioPvidTrmt_Type()
)
flowEntityProvisionCapPrioPvidTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapPrioPvidTrmt.setStatus("current")
_FlowEntityProvisionCapRedLineState_Type = FspR7RedLinedStateCaps
_FlowEntityProvisionCapRedLineState_Object = MibTableColumn
flowEntityProvisionCapRedLineState = _FlowEntityProvisionCapRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 19),
    _FlowEntityProvisionCapRedLineState_Type()
)
flowEntityProvisionCapRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapRedLineState.setStatus("current")
_FlowEntityProvisionCapTunnelAid_Type = Integer32
_FlowEntityProvisionCapTunnelAid_Object = MibTableColumn
flowEntityProvisionCapTunnelAid = _FlowEntityProvisionCapTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 12, 1, 20),
    _FlowEntityProvisionCapTunnelAid_Type()
)
flowEntityProvisionCapTunnelAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCapTunnelAid.setStatus("current")
_FlowEntityProvisionDefaultsTable_Object = MibTable
flowEntityProvisionDefaultsTable = _FlowEntityProvisionDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13)
)
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsTable.setStatus("current")
_FlowEntityProvisionDefaultsEntry_Object = MibTableRow
flowEntityProvisionDefaultsEntry = _FlowEntityProvisionDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1)
)
flowEntityProvisionDefaultsEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsEntry.setStatus("current")
_FlowEntityProvisionDefaultsRowStatus_Type = RowStatus
_FlowEntityProvisionDefaultsRowStatus_Object = MibTableColumn
flowEntityProvisionDefaultsRowStatus = _FlowEntityProvisionDefaultsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 1),
    _FlowEntityProvisionDefaultsRowStatus_Type()
)
flowEntityProvisionDefaultsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsRowStatus.setStatus("current")
_FlowEntityProvisionDefaultsType_Type = FspR7InterfaceType
_FlowEntityProvisionDefaultsType_Object = MibTableColumn
flowEntityProvisionDefaultsType = _FlowEntityProvisionDefaultsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 2),
    _FlowEntityProvisionDefaultsType_Type()
)
flowEntityProvisionDefaultsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsType.setStatus("current")
_FlowEntityProvisionDefaultsAdmin_Type = FspR7AdminState
_FlowEntityProvisionDefaultsAdmin_Object = MibTableColumn
flowEntityProvisionDefaultsAdmin = _FlowEntityProvisionDefaultsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 3),
    _FlowEntityProvisionDefaultsAdmin_Type()
)
flowEntityProvisionDefaultsAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsAdmin.setStatus("current")
_FlowEntityProvisionDefaultsAlias_Type = SnmpAdminString
_FlowEntityProvisionDefaultsAlias_Object = MibTableColumn
flowEntityProvisionDefaultsAlias = _FlowEntityProvisionDefaultsAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 4),
    _FlowEntityProvisionDefaultsAlias_Type()
)
flowEntityProvisionDefaultsAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsAlias.setStatus("current")


class _FlowEntityProvisionDefaultsPopCtagRcv_Type(Unsigned32):
    """Custom type flowEntityProvisionDefaultsPopCtagRcv based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionDefaultsPopCtagRcv_Type.__name__ = "Unsigned32"
_FlowEntityProvisionDefaultsPopCtagRcv_Object = MibTableColumn
flowEntityProvisionDefaultsPopCtagRcv = _FlowEntityProvisionDefaultsPopCtagRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 5),
    _FlowEntityProvisionDefaultsPopCtagRcv_Type()
)
flowEntityProvisionDefaultsPopCtagRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsPopCtagRcv.setStatus("current")


class _FlowEntityProvisionDefaultsPopCtagTrmt_Type(Unsigned32):
    """Custom type flowEntityProvisionDefaultsPopCtagTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionDefaultsPopCtagTrmt_Type.__name__ = "Unsigned32"
_FlowEntityProvisionDefaultsPopCtagTrmt_Object = MibTableColumn
flowEntityProvisionDefaultsPopCtagTrmt = _FlowEntityProvisionDefaultsPopCtagTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 6),
    _FlowEntityProvisionDefaultsPopCtagTrmt_Type()
)
flowEntityProvisionDefaultsPopCtagTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsPopCtagTrmt.setStatus("current")
_FlowEntityProvisionDefaultsCvidRegisteredInFlow_Type = SnmpAdminString
_FlowEntityProvisionDefaultsCvidRegisteredInFlow_Object = MibTableColumn
flowEntityProvisionDefaultsCvidRegisteredInFlow = _FlowEntityProvisionDefaultsCvidRegisteredInFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 7),
    _FlowEntityProvisionDefaultsCvidRegisteredInFlow_Type()
)
flowEntityProvisionDefaultsCvidRegisteredInFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsCvidRegisteredInFlow.setStatus("current")


class _FlowEntityProvisionDefaultsExternalVid_Type(Unsigned32):
    """Custom type flowEntityProvisionDefaultsExternalVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionDefaultsExternalVid_Type.__name__ = "Unsigned32"
_FlowEntityProvisionDefaultsExternalVid_Object = MibTableColumn
flowEntityProvisionDefaultsExternalVid = _FlowEntityProvisionDefaultsExternalVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 8),
    _FlowEntityProvisionDefaultsExternalVid_Type()
)
flowEntityProvisionDefaultsExternalVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsExternalVid.setStatus("current")
_FlowEntityProvisionDefaultsPmMode_Type = FspR7L2PmMode
_FlowEntityProvisionDefaultsPmMode_Object = MibTableColumn
flowEntityProvisionDefaultsPmMode = _FlowEntityProvisionDefaultsPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 9),
    _FlowEntityProvisionDefaultsPmMode_Type()
)
flowEntityProvisionDefaultsPmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsPmMode.setStatus("current")
_FlowEntityProvisionDefaultsShape_Type = FspR7DisableEnable
_FlowEntityProvisionDefaultsShape_Object = MibTableColumn
flowEntityProvisionDefaultsShape = _FlowEntityProvisionDefaultsShape_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 10),
    _FlowEntityProvisionDefaultsShape_Type()
)
flowEntityProvisionDefaultsShape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsShape.setStatus("current")
_FlowEntityProvisionDefaultsPolice_Type = FspR7DisableEnable
_FlowEntityProvisionDefaultsPolice_Object = MibTableColumn
flowEntityProvisionDefaultsPolice = _FlowEntityProvisionDefaultsPolice_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 11),
    _FlowEntityProvisionDefaultsPolice_Type()
)
flowEntityProvisionDefaultsPolice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsPolice.setStatus("current")


class _FlowEntityProvisionDefaultsDefaultEvcCos_Type(Integer32):
    """Custom type flowEntityProvisionDefaultsDefaultEvcCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_FlowEntityProvisionDefaultsDefaultEvcCos_Type.__name__ = "Integer32"
_FlowEntityProvisionDefaultsDefaultEvcCos_Object = MibTableColumn
flowEntityProvisionDefaultsDefaultEvcCos = _FlowEntityProvisionDefaultsDefaultEvcCos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 12),
    _FlowEntityProvisionDefaultsDefaultEvcCos_Type()
)
flowEntityProvisionDefaultsDefaultEvcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsDefaultEvcCos.setStatus("current")
_FlowEntityProvisionDefaultsCirRcv_Type = Unsigned32
_FlowEntityProvisionDefaultsCirRcv_Object = MibTableColumn
flowEntityProvisionDefaultsCirRcv = _FlowEntityProvisionDefaultsCirRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 13),
    _FlowEntityProvisionDefaultsCirRcv_Type()
)
flowEntityProvisionDefaultsCirRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsCirRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsCirRcv.setUnits("Mbit/s")
_FlowEntityProvisionDefaultsCirTrmt_Type = Unsigned32
_FlowEntityProvisionDefaultsCirTrmt_Object = MibTableColumn
flowEntityProvisionDefaultsCirTrmt = _FlowEntityProvisionDefaultsCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 14),
    _FlowEntityProvisionDefaultsCirTrmt_Type()
)
flowEntityProvisionDefaultsCirTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsCirTrmt.setUnits("Mbit/s")


class _FlowEntityProvisionDefaultsCbsRcv_Type(Unsigned32):
    """Custom type flowEntityProvisionDefaultsCbsRcv based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26214400),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionDefaultsCbsRcv_Type.__name__ = "Unsigned32"
_FlowEntityProvisionDefaultsCbsRcv_Object = MibTableColumn
flowEntityProvisionDefaultsCbsRcv = _FlowEntityProvisionDefaultsCbsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 15),
    _FlowEntityProvisionDefaultsCbsRcv_Type()
)
flowEntityProvisionDefaultsCbsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsCbsRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsCbsRcv.setUnits("bytes")


class _FlowEntityProvisionDefaultsCbsTrmt_Type(Unsigned32):
    """Custom type flowEntityProvisionDefaultsCbsTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionDefaultsCbsTrmt_Type.__name__ = "Unsigned32"
_FlowEntityProvisionDefaultsCbsTrmt_Object = MibTableColumn
flowEntityProvisionDefaultsCbsTrmt = _FlowEntityProvisionDefaultsCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 16),
    _FlowEntityProvisionDefaultsCbsTrmt_Type()
)
flowEntityProvisionDefaultsCbsTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsCbsTrmt.setUnits("Kbytes")


class _FlowEntityProvisionDefaultsPushPvidTrmt_Type(Unsigned32):
    """Custom type flowEntityProvisionDefaultsPushPvidTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionDefaultsPushPvidTrmt_Type.__name__ = "Unsigned32"
_FlowEntityProvisionDefaultsPushPvidTrmt_Object = MibTableColumn
flowEntityProvisionDefaultsPushPvidTrmt = _FlowEntityProvisionDefaultsPushPvidTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 17),
    _FlowEntityProvisionDefaultsPushPvidTrmt_Type()
)
flowEntityProvisionDefaultsPushPvidTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsPushPvidTrmt.setStatus("current")


class _FlowEntityProvisionDefaultsPrioPvidTrmt_Type(Unsigned32):
    """Custom type flowEntityProvisionDefaultsPrioPvidTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityProvisionDefaultsPrioPvidTrmt_Type.__name__ = "Unsigned32"
_FlowEntityProvisionDefaultsPrioPvidTrmt_Object = MibTableColumn
flowEntityProvisionDefaultsPrioPvidTrmt = _FlowEntityProvisionDefaultsPrioPvidTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 18),
    _FlowEntityProvisionDefaultsPrioPvidTrmt_Type()
)
flowEntityProvisionDefaultsPrioPvidTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsPrioPvidTrmt.setStatus("current")
_FlowEntityProvisionDefaultsRedLineState_Type = FspR7RedLinedState
_FlowEntityProvisionDefaultsRedLineState_Object = MibTableColumn
flowEntityProvisionDefaultsRedLineState = _FlowEntityProvisionDefaultsRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 19),
    _FlowEntityProvisionDefaultsRedLineState_Type()
)
flowEntityProvisionDefaultsRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsRedLineState.setStatus("current")
_FlowEntityProvisionDefaultsTunnelAid_Type = SnmpAdminString
_FlowEntityProvisionDefaultsTunnelAid_Object = MibTableColumn
flowEntityProvisionDefaultsTunnelAid = _FlowEntityProvisionDefaultsTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 13, 1, 20),
    _FlowEntityProvisionDefaultsTunnelAid_Type()
)
flowEntityProvisionDefaultsTunnelAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionDefaultsTunnelAid.setStatus("current")
_FlowEntityProvisionCbsRcvCapTable_Object = MibTable
flowEntityProvisionCbsRcvCapTable = _FlowEntityProvisionCbsRcvCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 14)
)
if mibBuilder.loadTexts:
    flowEntityProvisionCbsRcvCapTable.setStatus("current")
_FlowEntityProvisionCbsRcvCapEntry_Object = MibTableRow
flowEntityProvisionCbsRcvCapEntry = _FlowEntityProvisionCbsRcvCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 14, 1)
)
flowEntityProvisionCbsRcvCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionCbsRcvCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityProvisionCbsRcvCapEntry.setStatus("current")
_FlowEntityProvisionCbsRcvCapIndexCap_Type = EntityIndex
_FlowEntityProvisionCbsRcvCapIndexCap_Object = MibTableColumn
flowEntityProvisionCbsRcvCapIndexCap = _FlowEntityProvisionCbsRcvCapIndexCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 14, 1, 1),
    _FlowEntityProvisionCbsRcvCapIndexCap_Type()
)
flowEntityProvisionCbsRcvCapIndexCap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    flowEntityProvisionCbsRcvCapIndexCap.setStatus("current")
_FlowEntityProvisionCbsRcvCapCbsRcv_Type = Unsigned32
_FlowEntityProvisionCbsRcvCapCbsRcv_Object = MibTableColumn
flowEntityProvisionCbsRcvCapCbsRcv = _FlowEntityProvisionCbsRcvCapCbsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 14, 1, 2),
    _FlowEntityProvisionCbsRcvCapCbsRcv_Type()
)
flowEntityProvisionCbsRcvCapCbsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionCbsRcvCapCbsRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityProvisionCbsRcvCapCbsRcv.setUnits("bytes")
_FlowEntityProvisionRegisterCapTable_Object = MibTable
flowEntityProvisionRegisterCapTable = _FlowEntityProvisionRegisterCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 15)
)
if mibBuilder.loadTexts:
    flowEntityProvisionRegisterCapTable.setStatus("current")
_FlowEntityProvisionRegisterCapEntry_Object = MibTableRow
flowEntityProvisionRegisterCapEntry = _FlowEntityProvisionRegisterCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 15, 1)
)
flowEntityProvisionRegisterCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionRegisterCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityProvisionRegisterCapEntry.setStatus("current")
_FlowEntityProvisionRegisterCapIndexCap_Type = EntityIndex
_FlowEntityProvisionRegisterCapIndexCap_Object = MibTableColumn
flowEntityProvisionRegisterCapIndexCap = _FlowEntityProvisionRegisterCapIndexCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 15, 1, 1),
    _FlowEntityProvisionRegisterCapIndexCap_Type()
)
flowEntityProvisionRegisterCapIndexCap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    flowEntityProvisionRegisterCapIndexCap.setStatus("current")
_FlowEntityProvisionRegisterCapStringCap_Type = SnmpAdminString
_FlowEntityProvisionRegisterCapStringCap_Object = MibTableColumn
flowEntityProvisionRegisterCapStringCap = _FlowEntityProvisionRegisterCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 15, 1, 2),
    _FlowEntityProvisionRegisterCapStringCap_Type()
)
flowEntityProvisionRegisterCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionRegisterCapStringCap.setStatus("current")
_FlowEntityProvisionExternalVidCapTable_Object = MibTable
flowEntityProvisionExternalVidCapTable = _FlowEntityProvisionExternalVidCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 16)
)
if mibBuilder.loadTexts:
    flowEntityProvisionExternalVidCapTable.setStatus("current")
_FlowEntityProvisionExternalVidCapEntry_Object = MibTableRow
flowEntityProvisionExternalVidCapEntry = _FlowEntityProvisionExternalVidCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 16, 1)
)
flowEntityProvisionExternalVidCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionExternalVidCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityProvisionExternalVidCapEntry.setStatus("current")
_FlowEntityProvisionExternalVidCapIndexCap_Type = EntityIndex
_FlowEntityProvisionExternalVidCapIndexCap_Object = MibTableColumn
flowEntityProvisionExternalVidCapIndexCap = _FlowEntityProvisionExternalVidCapIndexCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 16, 1, 1),
    _FlowEntityProvisionExternalVidCapIndexCap_Type()
)
flowEntityProvisionExternalVidCapIndexCap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    flowEntityProvisionExternalVidCapIndexCap.setStatus("current")
_FlowEntityProvisionExternalVidCapStringCap_Type = SnmpAdminString
_FlowEntityProvisionExternalVidCapStringCap_Object = MibTableColumn
flowEntityProvisionExternalVidCapStringCap = _FlowEntityProvisionExternalVidCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 16, 1, 2),
    _FlowEntityProvisionExternalVidCapStringCap_Type()
)
flowEntityProvisionExternalVidCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionExternalVidCapStringCap.setStatus("current")
_FlowEntityProvisionPopCtagRcvCapTable_Object = MibTable
flowEntityProvisionPopCtagRcvCapTable = _FlowEntityProvisionPopCtagRcvCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 17)
)
if mibBuilder.loadTexts:
    flowEntityProvisionPopCtagRcvCapTable.setStatus("current")
_FlowEntityProvisionPopCtagRcvCapEntry_Object = MibTableRow
flowEntityProvisionPopCtagRcvCapEntry = _FlowEntityProvisionPopCtagRcvCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 17, 1)
)
flowEntityProvisionPopCtagRcvCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionPopCtagRcvCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityProvisionPopCtagRcvCapEntry.setStatus("current")
_FlowEntityProvisionPopCtagRcvCapIndexCap_Type = EntityIndex
_FlowEntityProvisionPopCtagRcvCapIndexCap_Object = MibTableColumn
flowEntityProvisionPopCtagRcvCapIndexCap = _FlowEntityProvisionPopCtagRcvCapIndexCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 17, 1, 1),
    _FlowEntityProvisionPopCtagRcvCapIndexCap_Type()
)
flowEntityProvisionPopCtagRcvCapIndexCap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    flowEntityProvisionPopCtagRcvCapIndexCap.setStatus("current")
_FlowEntityProvisionPopCtagRcvCapStringCap_Type = SnmpAdminString
_FlowEntityProvisionPopCtagRcvCapStringCap_Object = MibTableColumn
flowEntityProvisionPopCtagRcvCapStringCap = _FlowEntityProvisionPopCtagRcvCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 17, 1, 2),
    _FlowEntityProvisionPopCtagRcvCapStringCap_Type()
)
flowEntityProvisionPopCtagRcvCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionPopCtagRcvCapStringCap.setStatus("current")
_FlowEntityProvisionPopCtagTrmtCapTable_Object = MibTable
flowEntityProvisionPopCtagTrmtCapTable = _FlowEntityProvisionPopCtagTrmtCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 18)
)
if mibBuilder.loadTexts:
    flowEntityProvisionPopCtagTrmtCapTable.setStatus("current")
_FlowEntityProvisionPopCtagTrmtCapEntry_Object = MibTableRow
flowEntityProvisionPopCtagTrmtCapEntry = _FlowEntityProvisionPopCtagTrmtCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 18, 1)
)
flowEntityProvisionPopCtagTrmtCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionPopCtagTrmtCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityProvisionPopCtagTrmtCapEntry.setStatus("current")
_FlowEntityProvisionPopCtagTrmtCapIndexCap_Type = EntityIndex
_FlowEntityProvisionPopCtagTrmtCapIndexCap_Object = MibTableColumn
flowEntityProvisionPopCtagTrmtCapIndexCap = _FlowEntityProvisionPopCtagTrmtCapIndexCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 18, 1, 1),
    _FlowEntityProvisionPopCtagTrmtCapIndexCap_Type()
)
flowEntityProvisionPopCtagTrmtCapIndexCap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    flowEntityProvisionPopCtagTrmtCapIndexCap.setStatus("current")
_FlowEntityProvisionPopCtagTrmtCapStringCap_Type = SnmpAdminString
_FlowEntityProvisionPopCtagTrmtCapStringCap_Object = MibTableColumn
flowEntityProvisionPopCtagTrmtCapStringCap = _FlowEntityProvisionPopCtagTrmtCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 18, 1, 2),
    _FlowEntityProvisionPopCtagTrmtCapStringCap_Type()
)
flowEntityProvisionPopCtagTrmtCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionPopCtagTrmtCapStringCap.setStatus("current")
_FlowEntityProvisionPushTrmtCapTable_Object = MibTable
flowEntityProvisionPushTrmtCapTable = _FlowEntityProvisionPushTrmtCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 19)
)
if mibBuilder.loadTexts:
    flowEntityProvisionPushTrmtCapTable.setStatus("current")
_FlowEntityProvisionPushTrmtCapEntry_Object = MibTableRow
flowEntityProvisionPushTrmtCapEntry = _FlowEntityProvisionPushTrmtCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 19, 1)
)
flowEntityProvisionPushTrmtCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionPushTrmtCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityProvisionPushTrmtCapEntry.setStatus("current")
_FlowEntityProvisionPushTrmtCapIndexCap_Type = EntityIndex
_FlowEntityProvisionPushTrmtCapIndexCap_Object = MibTableColumn
flowEntityProvisionPushTrmtCapIndexCap = _FlowEntityProvisionPushTrmtCapIndexCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 19, 1, 1),
    _FlowEntityProvisionPushTrmtCapIndexCap_Type()
)
flowEntityProvisionPushTrmtCapIndexCap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    flowEntityProvisionPushTrmtCapIndexCap.setStatus("current")
_FlowEntityProvisionPushTrmtCapStringCap_Type = SnmpAdminString
_FlowEntityProvisionPushTrmtCapStringCap_Object = MibTableColumn
flowEntityProvisionPushTrmtCapStringCap = _FlowEntityProvisionPushTrmtCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 11, 19, 1, 2),
    _FlowEntityProvisionPushTrmtCapStringCap_Type()
)
flowEntityProvisionPushTrmtCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityProvisionPushTrmtCapStringCap.setStatus("current")
_CtransProvisioning_ObjectIdentity = ObjectIdentity
ctransProvisioning = _CtransProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12)
)
_CtransEntityProvisionTable_Object = MibTable
ctransEntityProvisionTable = _CtransEntityProvisionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 11)
)
if mibBuilder.loadTexts:
    ctransEntityProvisionTable.setStatus("current")
_CtransEntityProvisionEntry_Object = MibTableRow
ctransEntityProvisionEntry = _CtransEntityProvisionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 11, 1)
)
ctransEntityProvisionEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexCVlanId"),
)
if mibBuilder.loadTexts:
    ctransEntityProvisionEntry.setStatus("current")
_CtransEntityProvisionRowStatus_Type = RowStatus
_CtransEntityProvisionRowStatus_Object = MibTableColumn
ctransEntityProvisionRowStatus = _CtransEntityProvisionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 11, 1, 1),
    _CtransEntityProvisionRowStatus_Type()
)
ctransEntityProvisionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctransEntityProvisionRowStatus.setStatus("current")
_CtransEntityProvisionType_Type = FspR7InterfaceType
_CtransEntityProvisionType_Object = MibTableColumn
ctransEntityProvisionType = _CtransEntityProvisionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 11, 1, 2),
    _CtransEntityProvisionType_Type()
)
ctransEntityProvisionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctransEntityProvisionType.setStatus("current")


class _CtransEntityProvisionCvidInternal_Type(Unsigned32):
    """Custom type ctransEntityProvisionCvidInternal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_CtransEntityProvisionCvidInternal_Type.__name__ = "Unsigned32"
_CtransEntityProvisionCvidInternal_Object = MibTableColumn
ctransEntityProvisionCvidInternal = _CtransEntityProvisionCvidInternal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 11, 1, 3),
    _CtransEntityProvisionCvidInternal_Type()
)
ctransEntityProvisionCvidInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctransEntityProvisionCvidInternal.setStatus("current")


class _CtransEntityProvisionRange_Type(Unsigned32):
    """Custom type ctransEntityProvisionRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_CtransEntityProvisionRange_Type.__name__ = "Unsigned32"
_CtransEntityProvisionRange_Object = MibTableColumn
ctransEntityProvisionRange = _CtransEntityProvisionRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 11, 1, 4),
    _CtransEntityProvisionRange_Type()
)
ctransEntityProvisionRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctransEntityProvisionRange.setStatus("current")
_CtransEntityProvisionCapTable_Object = MibTable
ctransEntityProvisionCapTable = _CtransEntityProvisionCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 12)
)
if mibBuilder.loadTexts:
    ctransEntityProvisionCapTable.setStatus("current")
_CtransEntityProvisionCapEntry_Object = MibTableRow
ctransEntityProvisionCapEntry = _CtransEntityProvisionCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 12, 1)
)
ctransEntityProvisionCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexCVlanId"),
)
if mibBuilder.loadTexts:
    ctransEntityProvisionCapEntry.setStatus("current")
_CtransEntityProvisionCapRowStatus_Type = FspR7RowStatusCaps
_CtransEntityProvisionCapRowStatus_Object = MibTableColumn
ctransEntityProvisionCapRowStatus = _CtransEntityProvisionCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 12, 1, 1),
    _CtransEntityProvisionCapRowStatus_Type()
)
ctransEntityProvisionCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityProvisionCapRowStatus.setStatus("current")
_CtransEntityProvisionCapType_Type = FspR7InterfaceTypeCaps
_CtransEntityProvisionCapType_Object = MibTableColumn
ctransEntityProvisionCapType = _CtransEntityProvisionCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 12, 1, 2),
    _CtransEntityProvisionCapType_Type()
)
ctransEntityProvisionCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityProvisionCapType.setStatus("current")
_CtransEntityProvisionCapCvidInternal_Type = Unsigned32
_CtransEntityProvisionCapCvidInternal_Object = MibTableColumn
ctransEntityProvisionCapCvidInternal = _CtransEntityProvisionCapCvidInternal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 12, 1, 3),
    _CtransEntityProvisionCapCvidInternal_Type()
)
ctransEntityProvisionCapCvidInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityProvisionCapCvidInternal.setStatus("current")
_CtransEntityProvisionCapRange_Type = FspR7Unsigned32Caps
_CtransEntityProvisionCapRange_Object = MibTableColumn
ctransEntityProvisionCapRange = _CtransEntityProvisionCapRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 12, 1, 4),
    _CtransEntityProvisionCapRange_Type()
)
ctransEntityProvisionCapRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityProvisionCapRange.setStatus("current")
_CtransEntityProvisionDefaultsTable_Object = MibTable
ctransEntityProvisionDefaultsTable = _CtransEntityProvisionDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 13)
)
if mibBuilder.loadTexts:
    ctransEntityProvisionDefaultsTable.setStatus("current")
_CtransEntityProvisionDefaultsEntry_Object = MibTableRow
ctransEntityProvisionDefaultsEntry = _CtransEntityProvisionDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 13, 1)
)
ctransEntityProvisionDefaultsEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexCVlanId"),
)
if mibBuilder.loadTexts:
    ctransEntityProvisionDefaultsEntry.setStatus("current")
_CtransEntityProvisionDefaultsRowStatus_Type = RowStatus
_CtransEntityProvisionDefaultsRowStatus_Object = MibTableColumn
ctransEntityProvisionDefaultsRowStatus = _CtransEntityProvisionDefaultsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 13, 1, 1),
    _CtransEntityProvisionDefaultsRowStatus_Type()
)
ctransEntityProvisionDefaultsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityProvisionDefaultsRowStatus.setStatus("current")
_CtransEntityProvisionDefaultsType_Type = FspR7InterfaceType
_CtransEntityProvisionDefaultsType_Object = MibTableColumn
ctransEntityProvisionDefaultsType = _CtransEntityProvisionDefaultsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 13, 1, 2),
    _CtransEntityProvisionDefaultsType_Type()
)
ctransEntityProvisionDefaultsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityProvisionDefaultsType.setStatus("current")


class _CtransEntityProvisionDefaultsCvidInternal_Type(Unsigned32):
    """Custom type ctransEntityProvisionDefaultsCvidInternal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_CtransEntityProvisionDefaultsCvidInternal_Type.__name__ = "Unsigned32"
_CtransEntityProvisionDefaultsCvidInternal_Object = MibTableColumn
ctransEntityProvisionDefaultsCvidInternal = _CtransEntityProvisionDefaultsCvidInternal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 13, 1, 3),
    _CtransEntityProvisionDefaultsCvidInternal_Type()
)
ctransEntityProvisionDefaultsCvidInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityProvisionDefaultsCvidInternal.setStatus("current")


class _CtransEntityProvisionDefaultsRange_Type(Unsigned32):
    """Custom type ctransEntityProvisionDefaultsRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_CtransEntityProvisionDefaultsRange_Type.__name__ = "Unsigned32"
_CtransEntityProvisionDefaultsRange_Object = MibTableColumn
ctransEntityProvisionDefaultsRange = _CtransEntityProvisionDefaultsRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 13, 1, 4),
    _CtransEntityProvisionDefaultsRange_Type()
)
ctransEntityProvisionDefaultsRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityProvisionDefaultsRange.setStatus("current")
_CtransEntityProvisionCvidInternalCapTable_Object = MibTable
ctransEntityProvisionCvidInternalCapTable = _CtransEntityProvisionCvidInternalCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 14)
)
if mibBuilder.loadTexts:
    ctransEntityProvisionCvidInternalCapTable.setStatus("current")
_CtransEntityProvisionCvidInternalCapEntry_Object = MibTableRow
ctransEntityProvisionCvidInternalCapEntry = _CtransEntityProvisionCvidInternalCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 14, 1)
)
ctransEntityProvisionCvidInternalCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexCVlanId"),
    (0, "FspR7-LAYER2-MIB", "ctransEntityProvisionCvidInternalCapIndexCap"),
)
if mibBuilder.loadTexts:
    ctransEntityProvisionCvidInternalCapEntry.setStatus("current")
_CtransEntityProvisionCvidInternalCapIndexCap_Type = EntityIndex
_CtransEntityProvisionCvidInternalCapIndexCap_Object = MibTableColumn
ctransEntityProvisionCvidInternalCapIndexCap = _CtransEntityProvisionCvidInternalCapIndexCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 14, 1, 1),
    _CtransEntityProvisionCvidInternalCapIndexCap_Type()
)
ctransEntityProvisionCvidInternalCapIndexCap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctransEntityProvisionCvidInternalCapIndexCap.setStatus("current")
_CtransEntityProvisionCvidInternalCapStringCap_Type = SnmpAdminString
_CtransEntityProvisionCvidInternalCapStringCap_Object = MibTableColumn
ctransEntityProvisionCvidInternalCapStringCap = _CtransEntityProvisionCvidInternalCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 12, 14, 1, 2),
    _CtransEntityProvisionCvidInternalCapStringCap_Type()
)
ctransEntityProvisionCvidInternalCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityProvisionCvidInternalCapStringCap.setStatus("current")
_BridgeProvisioning_ObjectIdentity = ObjectIdentity
bridgeProvisioning = _BridgeProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13)
)
_BridgeToAssignEntityTable_Object = MibTable
bridgeToAssignEntityTable = _BridgeToAssignEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 11)
)
if mibBuilder.loadTexts:
    bridgeToAssignEntityTable.setStatus("current")
_BridgeToAssignEntityEntry_Object = MibTableRow
bridgeToAssignEntityEntry = _BridgeToAssignEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 11, 1)
)
bridgeToAssignEntityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
)
if mibBuilder.loadTexts:
    bridgeToAssignEntityEntry.setStatus("current")
_BridgeToAssignEntityIndexAid_Type = SnmpAdminString
_BridgeToAssignEntityIndexAid_Object = MibTableColumn
bridgeToAssignEntityIndexAid = _BridgeToAssignEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 11, 1, 1),
    _BridgeToAssignEntityIndexAid_Type()
)
bridgeToAssignEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeToAssignEntityIndexAid.setStatus("current")
_BridgeEntityProvisionTable_Object = MibTable
bridgeEntityProvisionTable = _BridgeEntityProvisionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 12)
)
if mibBuilder.loadTexts:
    bridgeEntityProvisionTable.setStatus("current")
_BridgeEntityProvisionEntry_Object = MibTableRow
bridgeEntityProvisionEntry = _BridgeEntityProvisionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 12, 1)
)
bridgeEntityProvisionEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
)
if mibBuilder.loadTexts:
    bridgeEntityProvisionEntry.setStatus("current")
_BridgeEntityProvisionRowStatus_Type = RowStatus
_BridgeEntityProvisionRowStatus_Object = MibTableColumn
bridgeEntityProvisionRowStatus = _BridgeEntityProvisionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 12, 1, 1),
    _BridgeEntityProvisionRowStatus_Type()
)
bridgeEntityProvisionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeEntityProvisionRowStatus.setStatus("current")
_BridgeEntityProvisionFacilityType_Type = FspR7InterfaceType
_BridgeEntityProvisionFacilityType_Object = MibTableColumn
bridgeEntityProvisionFacilityType = _BridgeEntityProvisionFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 12, 1, 2),
    _BridgeEntityProvisionFacilityType_Type()
)
bridgeEntityProvisionFacilityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeEntityProvisionFacilityType.setStatus("current")
_BridgeEntityProvisionAlias_Type = SnmpAdminString
_BridgeEntityProvisionAlias_Object = MibTableColumn
bridgeEntityProvisionAlias = _BridgeEntityProvisionAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 12, 1, 3),
    _BridgeEntityProvisionAlias_Type()
)
bridgeEntityProvisionAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeEntityProvisionAlias.setStatus("current")
_BridgeEntityProvisionShapeState_Type = FspR7DisableEnable
_BridgeEntityProvisionShapeState_Object = MibTableColumn
bridgeEntityProvisionShapeState = _BridgeEntityProvisionShapeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 12, 1, 4),
    _BridgeEntityProvisionShapeState_Type()
)
bridgeEntityProvisionShapeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeEntityProvisionShapeState.setStatus("current")
_BridgeEntityProvisionPmMode_Type = FspR7L2PmMode
_BridgeEntityProvisionPmMode_Object = MibTableColumn
bridgeEntityProvisionPmMode = _BridgeEntityProvisionPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 12, 1, 5),
    _BridgeEntityProvisionPmMode_Type()
)
bridgeEntityProvisionPmMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeEntityProvisionPmMode.setStatus("current")
_BridgeEntityProvisionCirTrmt_Type = Unsigned32
_BridgeEntityProvisionCirTrmt_Object = MibTableColumn
bridgeEntityProvisionCirTrmt = _BridgeEntityProvisionCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 12, 1, 6),
    _BridgeEntityProvisionCirTrmt_Type()
)
bridgeEntityProvisionCirTrmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCirTrmt.setUnits("Mbit/s")


class _BridgeEntityProvisionCbsTrmt_Type(Unsigned32):
    """Custom type bridgeEntityProvisionCbsTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_BridgeEntityProvisionCbsTrmt_Type.__name__ = "Unsigned32"
_BridgeEntityProvisionCbsTrmt_Object = MibTableColumn
bridgeEntityProvisionCbsTrmt = _BridgeEntityProvisionCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 12, 1, 7),
    _BridgeEntityProvisionCbsTrmt_Type()
)
bridgeEntityProvisionCbsTrmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCbsTrmt.setUnits("Kbytes")
_BridgeEntityProvisionAdminState_Type = FspR7AdminState
_BridgeEntityProvisionAdminState_Object = MibTableColumn
bridgeEntityProvisionAdminState = _BridgeEntityProvisionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 12, 1, 8),
    _BridgeEntityProvisionAdminState_Type()
)
bridgeEntityProvisionAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeEntityProvisionAdminState.setStatus("current")
_BridgeEntityProvisionCapTable_Object = MibTable
bridgeEntityProvisionCapTable = _BridgeEntityProvisionCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 13)
)
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapTable.setStatus("current")
_BridgeEntityProvisionCapEntry_Object = MibTableRow
bridgeEntityProvisionCapEntry = _BridgeEntityProvisionCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 13, 1)
)
bridgeEntityProvisionCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
)
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapEntry.setStatus("current")
_BridgeEntityProvisionCapRowStatus_Type = FspR7RowStatusCaps
_BridgeEntityProvisionCapRowStatus_Object = MibTableColumn
bridgeEntityProvisionCapRowStatus = _BridgeEntityProvisionCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 13, 1, 1),
    _BridgeEntityProvisionCapRowStatus_Type()
)
bridgeEntityProvisionCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapRowStatus.setStatus("current")
_BridgeEntityProvisionCapFacilityType_Type = FspR7InterfaceTypeCaps
_BridgeEntityProvisionCapFacilityType_Object = MibTableColumn
bridgeEntityProvisionCapFacilityType = _BridgeEntityProvisionCapFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 13, 1, 2),
    _BridgeEntityProvisionCapFacilityType_Type()
)
bridgeEntityProvisionCapFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapFacilityType.setStatus("current")
_BridgeEntityProvisionCapAlias_Type = Integer32
_BridgeEntityProvisionCapAlias_Object = MibTableColumn
bridgeEntityProvisionCapAlias = _BridgeEntityProvisionCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 13, 1, 3),
    _BridgeEntityProvisionCapAlias_Type()
)
bridgeEntityProvisionCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapAlias.setStatus("current")
_BridgeEntityProvisionCapShapeState_Type = FspR7DisableEnableCaps
_BridgeEntityProvisionCapShapeState_Object = MibTableColumn
bridgeEntityProvisionCapShapeState = _BridgeEntityProvisionCapShapeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 13, 1, 4),
    _BridgeEntityProvisionCapShapeState_Type()
)
bridgeEntityProvisionCapShapeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapShapeState.setStatus("current")
_BridgeEntityProvisionCapPmMode_Type = FspR7L2PmModeCaps
_BridgeEntityProvisionCapPmMode_Object = MibTableColumn
bridgeEntityProvisionCapPmMode = _BridgeEntityProvisionCapPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 13, 1, 5),
    _BridgeEntityProvisionCapPmMode_Type()
)
bridgeEntityProvisionCapPmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapPmMode.setStatus("current")
_BridgeEntityProvisionCapCirTrmt_Type = FspR7Unsigned32Caps
_BridgeEntityProvisionCapCirTrmt_Object = MibTableColumn
bridgeEntityProvisionCapCirTrmt = _BridgeEntityProvisionCapCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 13, 1, 6),
    _BridgeEntityProvisionCapCirTrmt_Type()
)
bridgeEntityProvisionCapCirTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapCirTrmt.setUnits("Mbit/s")
_BridgeEntityProvisionCapCbsTrmt_Type = FspR7Unsigned32Caps
_BridgeEntityProvisionCapCbsTrmt_Object = MibTableColumn
bridgeEntityProvisionCapCbsTrmt = _BridgeEntityProvisionCapCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 13, 1, 7),
    _BridgeEntityProvisionCapCbsTrmt_Type()
)
bridgeEntityProvisionCapCbsTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapCbsTrmt.setUnits("Kbytes")
_BridgeEntityProvisionCapAdminState_Type = FspR7AdminStateCaps
_BridgeEntityProvisionCapAdminState_Object = MibTableColumn
bridgeEntityProvisionCapAdminState = _BridgeEntityProvisionCapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 13, 1, 8),
    _BridgeEntityProvisionCapAdminState_Type()
)
bridgeEntityProvisionCapAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionCapAdminState.setStatus("current")
_BridgeEntityProvisionDefaultsTable_Object = MibTable
bridgeEntityProvisionDefaultsTable = _BridgeEntityProvisionDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 14)
)
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsTable.setStatus("current")
_BridgeEntityProvisionDefaultsEntry_Object = MibTableRow
bridgeEntityProvisionDefaultsEntry = _BridgeEntityProvisionDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 14, 1)
)
bridgeEntityProvisionDefaultsEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
)
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsEntry.setStatus("current")
_BridgeEntityProvisionDefaultsRowStatus_Type = RowStatus
_BridgeEntityProvisionDefaultsRowStatus_Object = MibTableColumn
bridgeEntityProvisionDefaultsRowStatus = _BridgeEntityProvisionDefaultsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 14, 1, 1),
    _BridgeEntityProvisionDefaultsRowStatus_Type()
)
bridgeEntityProvisionDefaultsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsRowStatus.setStatus("current")
_BridgeEntityProvisionDefaultsFacilityType_Type = FspR7InterfaceType
_BridgeEntityProvisionDefaultsFacilityType_Object = MibTableColumn
bridgeEntityProvisionDefaultsFacilityType = _BridgeEntityProvisionDefaultsFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 14, 1, 2),
    _BridgeEntityProvisionDefaultsFacilityType_Type()
)
bridgeEntityProvisionDefaultsFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsFacilityType.setStatus("current")
_BridgeEntityProvisionDefaultsAlias_Type = SnmpAdminString
_BridgeEntityProvisionDefaultsAlias_Object = MibTableColumn
bridgeEntityProvisionDefaultsAlias = _BridgeEntityProvisionDefaultsAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 14, 1, 3),
    _BridgeEntityProvisionDefaultsAlias_Type()
)
bridgeEntityProvisionDefaultsAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsAlias.setStatus("current")
_BridgeEntityProvisionDefaultsShapeState_Type = FspR7DisableEnable
_BridgeEntityProvisionDefaultsShapeState_Object = MibTableColumn
bridgeEntityProvisionDefaultsShapeState = _BridgeEntityProvisionDefaultsShapeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 14, 1, 4),
    _BridgeEntityProvisionDefaultsShapeState_Type()
)
bridgeEntityProvisionDefaultsShapeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsShapeState.setStatus("current")
_BridgeEntityProvisionDefaultsPmMode_Type = FspR7L2PmMode
_BridgeEntityProvisionDefaultsPmMode_Object = MibTableColumn
bridgeEntityProvisionDefaultsPmMode = _BridgeEntityProvisionDefaultsPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 14, 1, 5),
    _BridgeEntityProvisionDefaultsPmMode_Type()
)
bridgeEntityProvisionDefaultsPmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsPmMode.setStatus("current")
_BridgeEntityProvisionDefaultsCirTrmt_Type = Unsigned32
_BridgeEntityProvisionDefaultsCirTrmt_Object = MibTableColumn
bridgeEntityProvisionDefaultsCirTrmt = _BridgeEntityProvisionDefaultsCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 14, 1, 6),
    _BridgeEntityProvisionDefaultsCirTrmt_Type()
)
bridgeEntityProvisionDefaultsCirTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsCirTrmt.setUnits("Mbit/s")


class _BridgeEntityProvisionDefaultsCbsTrmt_Type(Unsigned32):
    """Custom type bridgeEntityProvisionDefaultsCbsTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_BridgeEntityProvisionDefaultsCbsTrmt_Type.__name__ = "Unsigned32"
_BridgeEntityProvisionDefaultsCbsTrmt_Object = MibTableColumn
bridgeEntityProvisionDefaultsCbsTrmt = _BridgeEntityProvisionDefaultsCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 14, 1, 7),
    _BridgeEntityProvisionDefaultsCbsTrmt_Type()
)
bridgeEntityProvisionDefaultsCbsTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsCbsTrmt.setUnits("Kbytes")
_BridgeEntityProvisionDefaultsAdminState_Type = FspR7AdminState
_BridgeEntityProvisionDefaultsAdminState_Object = MibTableColumn
bridgeEntityProvisionDefaultsAdminState = _BridgeEntityProvisionDefaultsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 12, 13, 14, 1, 8),
    _BridgeEntityProvisionDefaultsAdminState_Type()
)
bridgeEntityProvisionDefaultsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityProvisionDefaultsAdminState.setStatus("current")
_Layer2ConfigurationMIB_ObjectIdentity = ObjectIdentity
layer2ConfigurationMIB = _Layer2ConfigurationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13)
)
_FlowConfiguration_ObjectIdentity = ObjectIdentity
flowConfiguration = _FlowConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11)
)
_FlowEntityConfigTable_Object = MibTable
flowEntityConfigTable = _FlowEntityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11)
)
if mibBuilder.loadTexts:
    flowEntityConfigTable.setStatus("current")
_FlowEntityConfigEntry_Object = MibTableRow
flowEntityConfigEntry = _FlowEntityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1)
)
flowEntityConfigEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowEntityConfigEntry.setStatus("current")
_FlowEntityConfigAdmin_Type = FspR7AdminState
_FlowEntityConfigAdmin_Object = MibTableColumn
flowEntityConfigAdmin = _FlowEntityConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 1),
    _FlowEntityConfigAdmin_Type()
)
flowEntityConfigAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigAdmin.setStatus("current")
_FlowEntityConfigAlias_Type = SnmpAdminString
_FlowEntityConfigAlias_Object = MibTableColumn
flowEntityConfigAlias = _FlowEntityConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 2),
    _FlowEntityConfigAlias_Type()
)
flowEntityConfigAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigAlias.setStatus("current")


class _FlowEntityConfigPopCtagRcv_Type(Unsigned32):
    """Custom type flowEntityConfigPopCtagRcv based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityConfigPopCtagRcv_Type.__name__ = "Unsigned32"
_FlowEntityConfigPopCtagRcv_Object = MibTableColumn
flowEntityConfigPopCtagRcv = _FlowEntityConfigPopCtagRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 3),
    _FlowEntityConfigPopCtagRcv_Type()
)
flowEntityConfigPopCtagRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigPopCtagRcv.setStatus("current")


class _FlowEntityConfigPopCtagTrmt_Type(Unsigned32):
    """Custom type flowEntityConfigPopCtagTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityConfigPopCtagTrmt_Type.__name__ = "Unsigned32"
_FlowEntityConfigPopCtagTrmt_Object = MibTableColumn
flowEntityConfigPopCtagTrmt = _FlowEntityConfigPopCtagTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 4),
    _FlowEntityConfigPopCtagTrmt_Type()
)
flowEntityConfigPopCtagTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigPopCtagTrmt.setStatus("current")
_FlowEntityConfigCvidRegisteredInFlow_Type = SnmpAdminString
_FlowEntityConfigCvidRegisteredInFlow_Object = MibTableColumn
flowEntityConfigCvidRegisteredInFlow = _FlowEntityConfigCvidRegisteredInFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 5),
    _FlowEntityConfigCvidRegisteredInFlow_Type()
)
flowEntityConfigCvidRegisteredInFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigCvidRegisteredInFlow.setStatus("current")


class _FlowEntityConfigExternalVid_Type(Unsigned32):
    """Custom type flowEntityConfigExternalVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityConfigExternalVid_Type.__name__ = "Unsigned32"
_FlowEntityConfigExternalVid_Object = MibTableColumn
flowEntityConfigExternalVid = _FlowEntityConfigExternalVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 6),
    _FlowEntityConfigExternalVid_Type()
)
flowEntityConfigExternalVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigExternalVid.setStatus("current")
_FlowEntityConfigPmMode_Type = FspR7L2PmMode
_FlowEntityConfigPmMode_Object = MibTableColumn
flowEntityConfigPmMode = _FlowEntityConfigPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 7),
    _FlowEntityConfigPmMode_Type()
)
flowEntityConfigPmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigPmMode.setStatus("current")
_FlowEntityConfigShape_Type = FspR7DisableEnable
_FlowEntityConfigShape_Object = MibTableColumn
flowEntityConfigShape = _FlowEntityConfigShape_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 8),
    _FlowEntityConfigShape_Type()
)
flowEntityConfigShape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigShape.setStatus("current")
_FlowEntityConfigPolice_Type = FspR7DisableEnable
_FlowEntityConfigPolice_Object = MibTableColumn
flowEntityConfigPolice = _FlowEntityConfigPolice_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 9),
    _FlowEntityConfigPolice_Type()
)
flowEntityConfigPolice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigPolice.setStatus("current")


class _FlowEntityConfigDefaultEvcCos_Type(Integer32):
    """Custom type flowEntityConfigDefaultEvcCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_FlowEntityConfigDefaultEvcCos_Type.__name__ = "Integer32"
_FlowEntityConfigDefaultEvcCos_Object = MibTableColumn
flowEntityConfigDefaultEvcCos = _FlowEntityConfigDefaultEvcCos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 10),
    _FlowEntityConfigDefaultEvcCos_Type()
)
flowEntityConfigDefaultEvcCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigDefaultEvcCos.setStatus("current")
_FlowEntityConfigCirRcv_Type = Unsigned32
_FlowEntityConfigCirRcv_Object = MibTableColumn
flowEntityConfigCirRcv = _FlowEntityConfigCirRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 11),
    _FlowEntityConfigCirRcv_Type()
)
flowEntityConfigCirRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigCirRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityConfigCirRcv.setUnits("Mbit/s")
_FlowEntityConfigCirTrmt_Type = Unsigned32
_FlowEntityConfigCirTrmt_Object = MibTableColumn
flowEntityConfigCirTrmt = _FlowEntityConfigCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 12),
    _FlowEntityConfigCirTrmt_Type()
)
flowEntityConfigCirTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityConfigCirTrmt.setUnits("Mbit/s")


class _FlowEntityConfigCbsRcv_Type(Unsigned32):
    """Custom type flowEntityConfigCbsRcv based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26214400),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityConfigCbsRcv_Type.__name__ = "Unsigned32"
_FlowEntityConfigCbsRcv_Object = MibTableColumn
flowEntityConfigCbsRcv = _FlowEntityConfigCbsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 13),
    _FlowEntityConfigCbsRcv_Type()
)
flowEntityConfigCbsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigCbsRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityConfigCbsRcv.setUnits("bytes")


class _FlowEntityConfigCbsTrmt_Type(Unsigned32):
    """Custom type flowEntityConfigCbsTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityConfigCbsTrmt_Type.__name__ = "Unsigned32"
_FlowEntityConfigCbsTrmt_Object = MibTableColumn
flowEntityConfigCbsTrmt = _FlowEntityConfigCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 14),
    _FlowEntityConfigCbsTrmt_Type()
)
flowEntityConfigCbsTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityConfigCbsTrmt.setUnits("Kbytes")
_FlowEntityConfigDataLayerPmReset_Type = FspR7PmReset
_FlowEntityConfigDataLayerPmReset_Object = MibTableColumn
flowEntityConfigDataLayerPmReset = _FlowEntityConfigDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 15),
    _FlowEntityConfigDataLayerPmReset_Type()
)
flowEntityConfigDataLayerPmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigDataLayerPmReset.setStatus("current")


class _FlowEntityConfigPushPvidTrmt_Type(Unsigned32):
    """Custom type flowEntityConfigPushPvidTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityConfigPushPvidTrmt_Type.__name__ = "Unsigned32"
_FlowEntityConfigPushPvidTrmt_Object = MibTableColumn
flowEntityConfigPushPvidTrmt = _FlowEntityConfigPushPvidTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 16),
    _FlowEntityConfigPushPvidTrmt_Type()
)
flowEntityConfigPushPvidTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigPushPvidTrmt.setStatus("current")


class _FlowEntityConfigPrioPvidTrmt_Type(Unsigned32):
    """Custom type flowEntityConfigPrioPvidTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityConfigPrioPvidTrmt_Type.__name__ = "Unsigned32"
_FlowEntityConfigPrioPvidTrmt_Object = MibTableColumn
flowEntityConfigPrioPvidTrmt = _FlowEntityConfigPrioPvidTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 17),
    _FlowEntityConfigPrioPvidTrmt_Type()
)
flowEntityConfigPrioPvidTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigPrioPvidTrmt.setStatus("current")
_FlowEntityConfigRedLineState_Type = FspR7RedLinedState
_FlowEntityConfigRedLineState_Object = MibTableColumn
flowEntityConfigRedLineState = _FlowEntityConfigRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 18),
    _FlowEntityConfigRedLineState_Type()
)
flowEntityConfigRedLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigRedLineState.setStatus("current")
_FlowEntityConfigTunnelAid_Type = SnmpAdminString
_FlowEntityConfigTunnelAid_Object = MibTableColumn
flowEntityConfigTunnelAid = _FlowEntityConfigTunnelAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 19),
    _FlowEntityConfigTunnelAid_Type()
)
flowEntityConfigTunnelAid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigTunnelAid.setStatus("current")
_FlowEntityConfigSwitchCommand_Type = FspR7APSCommand
_FlowEntityConfigSwitchCommand_Object = MibTableColumn
flowEntityConfigSwitchCommand = _FlowEntityConfigSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 20),
    _FlowEntityConfigSwitchCommand_Type()
)
flowEntityConfigSwitchCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigSwitchCommand.setStatus("current")
_FlowEntityConfigInhibitSwitchToProt_Type = FspR7YesNo
_FlowEntityConfigInhibitSwitchToProt_Object = MibTableColumn
flowEntityConfigInhibitSwitchToProt = _FlowEntityConfigInhibitSwitchToProt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 21),
    _FlowEntityConfigInhibitSwitchToProt_Type()
)
flowEntityConfigInhibitSwitchToProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigInhibitSwitchToProt.setStatus("current")
_FlowEntityConfigInhibitSwitchToWork_Type = FspR7YesNo
_FlowEntityConfigInhibitSwitchToWork_Object = MibTableColumn
flowEntityConfigInhibitSwitchToWork = _FlowEntityConfigInhibitSwitchToWork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 11, 1, 22),
    _FlowEntityConfigInhibitSwitchToWork_Type()
)
flowEntityConfigInhibitSwitchToWork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowEntityConfigInhibitSwitchToWork.setStatus("current")
_FlowEntityConfigCapTable_Object = MibTable
flowEntityConfigCapTable = _FlowEntityConfigCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12)
)
if mibBuilder.loadTexts:
    flowEntityConfigCapTable.setStatus("current")
_FlowEntityConfigCapEntry_Object = MibTableRow
flowEntityConfigCapEntry = _FlowEntityConfigCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1)
)
flowEntityConfigCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowEntityConfigCapEntry.setStatus("current")
_FlowEntityConfigCapAdmin_Type = FspR7AdminStateCaps
_FlowEntityConfigCapAdmin_Object = MibTableColumn
flowEntityConfigCapAdmin = _FlowEntityConfigCapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 1),
    _FlowEntityConfigCapAdmin_Type()
)
flowEntityConfigCapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapAdmin.setStatus("current")
_FlowEntityConfigCapPmMode_Type = FspR7L2PmModeCaps
_FlowEntityConfigCapPmMode_Object = MibTableColumn
flowEntityConfigCapPmMode = _FlowEntityConfigCapPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 2),
    _FlowEntityConfigCapPmMode_Type()
)
flowEntityConfigCapPmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapPmMode.setStatus("current")
_FlowEntityConfigCapShape_Type = FspR7DisableEnableCaps
_FlowEntityConfigCapShape_Object = MibTableColumn
flowEntityConfigCapShape = _FlowEntityConfigCapShape_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 3),
    _FlowEntityConfigCapShape_Type()
)
flowEntityConfigCapShape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapShape.setStatus("current")
_FlowEntityConfigCapPolice_Type = FspR7DisableEnableCaps
_FlowEntityConfigCapPolice_Object = MibTableColumn
flowEntityConfigCapPolice = _FlowEntityConfigCapPolice_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 4),
    _FlowEntityConfigCapPolice_Type()
)
flowEntityConfigCapPolice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapPolice.setStatus("current")
_FlowEntityConfigCapDefaultEvcCos_Type = FspR7Integer32Caps
_FlowEntityConfigCapDefaultEvcCos_Object = MibTableColumn
flowEntityConfigCapDefaultEvcCos = _FlowEntityConfigCapDefaultEvcCos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 5),
    _FlowEntityConfigCapDefaultEvcCos_Type()
)
flowEntityConfigCapDefaultEvcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapDefaultEvcCos.setStatus("current")
_FlowEntityConfigCapDataLayerPmReset_Type = FspR7PmResetCaps
_FlowEntityConfigCapDataLayerPmReset_Object = MibTableColumn
flowEntityConfigCapDataLayerPmReset = _FlowEntityConfigCapDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 6),
    _FlowEntityConfigCapDataLayerPmReset_Type()
)
flowEntityConfigCapDataLayerPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapDataLayerPmReset.setStatus("current")
_FlowEntityConfigCapPopCtagRcv_Type = Unsigned32
_FlowEntityConfigCapPopCtagRcv_Object = MibTableColumn
flowEntityConfigCapPopCtagRcv = _FlowEntityConfigCapPopCtagRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 7),
    _FlowEntityConfigCapPopCtagRcv_Type()
)
flowEntityConfigCapPopCtagRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapPopCtagRcv.setStatus("current")
_FlowEntityConfigCapPopCtagTrmt_Type = Unsigned32
_FlowEntityConfigCapPopCtagTrmt_Object = MibTableColumn
flowEntityConfigCapPopCtagTrmt = _FlowEntityConfigCapPopCtagTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 8),
    _FlowEntityConfigCapPopCtagTrmt_Type()
)
flowEntityConfigCapPopCtagTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapPopCtagTrmt.setStatus("current")
_FlowEntityConfigCapCvidRegisteredInFlow_Type = Integer32
_FlowEntityConfigCapCvidRegisteredInFlow_Object = MibTableColumn
flowEntityConfigCapCvidRegisteredInFlow = _FlowEntityConfigCapCvidRegisteredInFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 9),
    _FlowEntityConfigCapCvidRegisteredInFlow_Type()
)
flowEntityConfigCapCvidRegisteredInFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapCvidRegisteredInFlow.setStatus("current")
_FlowEntityConfigCapExternalVid_Type = Unsigned32
_FlowEntityConfigCapExternalVid_Object = MibTableColumn
flowEntityConfigCapExternalVid = _FlowEntityConfigCapExternalVid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 10),
    _FlowEntityConfigCapExternalVid_Type()
)
flowEntityConfigCapExternalVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapExternalVid.setStatus("current")
_FlowEntityConfigCapCbsRcv_Type = Unsigned32
_FlowEntityConfigCapCbsRcv_Object = MibTableColumn
flowEntityConfigCapCbsRcv = _FlowEntityConfigCapCbsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 11),
    _FlowEntityConfigCapCbsRcv_Type()
)
flowEntityConfigCapCbsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapCbsRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityConfigCapCbsRcv.setUnits("bytes")
_FlowEntityConfigCapPushTrmt_Type = Unsigned32
_FlowEntityConfigCapPushTrmt_Object = MibTableColumn
flowEntityConfigCapPushTrmt = _FlowEntityConfigCapPushTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 12),
    _FlowEntityConfigCapPushTrmt_Type()
)
flowEntityConfigCapPushTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapPushTrmt.setStatus("current")
_FlowEntityConfigCapRedLineState_Type = FspR7RedLinedStateCaps
_FlowEntityConfigCapRedLineState_Object = MibTableColumn
flowEntityConfigCapRedLineState = _FlowEntityConfigCapRedLineState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 13),
    _FlowEntityConfigCapRedLineState_Type()
)
flowEntityConfigCapRedLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapRedLineState.setStatus("current")
_FlowEntityConfigCapSwitchCommand_Type = FspR7APSCommandCaps
_FlowEntityConfigCapSwitchCommand_Object = MibTableColumn
flowEntityConfigCapSwitchCommand = _FlowEntityConfigCapSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 14),
    _FlowEntityConfigCapSwitchCommand_Type()
)
flowEntityConfigCapSwitchCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapSwitchCommand.setStatus("current")
_FlowEntityConfigCapInhibitSwitchToProt_Type = FspR7YesNoCaps
_FlowEntityConfigCapInhibitSwitchToProt_Object = MibTableColumn
flowEntityConfigCapInhibitSwitchToProt = _FlowEntityConfigCapInhibitSwitchToProt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 15),
    _FlowEntityConfigCapInhibitSwitchToProt_Type()
)
flowEntityConfigCapInhibitSwitchToProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapInhibitSwitchToProt.setStatus("current")
_FlowEntityConfigCapInhibitSwitchToWork_Type = FspR7YesNoCaps
_FlowEntityConfigCapInhibitSwitchToWork_Object = MibTableColumn
flowEntityConfigCapInhibitSwitchToWork = _FlowEntityConfigCapInhibitSwitchToWork_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 12, 1, 16),
    _FlowEntityConfigCapInhibitSwitchToWork_Type()
)
flowEntityConfigCapInhibitSwitchToWork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCapInhibitSwitchToWork.setStatus("current")
_FlowEntityConfigCbsRcvCapTable_Object = MibTable
flowEntityConfigCbsRcvCapTable = _FlowEntityConfigCbsRcvCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 13)
)
if mibBuilder.loadTexts:
    flowEntityConfigCbsRcvCapTable.setStatus("current")
_FlowEntityConfigCbsRcvCapEntry_Object = MibTableRow
flowEntityConfigCbsRcvCapEntry = _FlowEntityConfigCbsRcvCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 13, 1)
)
flowEntityConfigCbsRcvCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionCbsRcvCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityConfigCbsRcvCapEntry.setStatus("current")
_FlowEntityConfigCbsRcvCapCbsRcv_Type = Unsigned32
_FlowEntityConfigCbsRcvCapCbsRcv_Object = MibTableColumn
flowEntityConfigCbsRcvCapCbsRcv = _FlowEntityConfigCbsRcvCapCbsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 13, 1, 1),
    _FlowEntityConfigCbsRcvCapCbsRcv_Type()
)
flowEntityConfigCbsRcvCapCbsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigCbsRcvCapCbsRcv.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityConfigCbsRcvCapCbsRcv.setUnits("bytes")
_FlowEntityConfigRegisterCapTable_Object = MibTable
flowEntityConfigRegisterCapTable = _FlowEntityConfigRegisterCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 14)
)
if mibBuilder.loadTexts:
    flowEntityConfigRegisterCapTable.setStatus("current")
_FlowEntityConfigRegisterCapEntry_Object = MibTableRow
flowEntityConfigRegisterCapEntry = _FlowEntityConfigRegisterCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 14, 1)
)
flowEntityConfigRegisterCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionRegisterCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityConfigRegisterCapEntry.setStatus("current")
_FlowEntityConfigRegisterCapStringCap_Type = SnmpAdminString
_FlowEntityConfigRegisterCapStringCap_Object = MibTableColumn
flowEntityConfigRegisterCapStringCap = _FlowEntityConfigRegisterCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 14, 1, 1),
    _FlowEntityConfigRegisterCapStringCap_Type()
)
flowEntityConfigRegisterCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigRegisterCapStringCap.setStatus("current")
_FlowEntityConfigExternalVidCapTable_Object = MibTable
flowEntityConfigExternalVidCapTable = _FlowEntityConfigExternalVidCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 15)
)
if mibBuilder.loadTexts:
    flowEntityConfigExternalVidCapTable.setStatus("current")
_FlowEntityConfigExternalVidCapEntry_Object = MibTableRow
flowEntityConfigExternalVidCapEntry = _FlowEntityConfigExternalVidCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 15, 1)
)
flowEntityConfigExternalVidCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionExternalVidCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityConfigExternalVidCapEntry.setStatus("current")
_FlowEntityConfigExternalVidCapStringCap_Type = SnmpAdminString
_FlowEntityConfigExternalVidCapStringCap_Object = MibTableColumn
flowEntityConfigExternalVidCapStringCap = _FlowEntityConfigExternalVidCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 15, 1, 1),
    _FlowEntityConfigExternalVidCapStringCap_Type()
)
flowEntityConfigExternalVidCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigExternalVidCapStringCap.setStatus("current")
_FlowEntityConfigPopCtagRcvCapTable_Object = MibTable
flowEntityConfigPopCtagRcvCapTable = _FlowEntityConfigPopCtagRcvCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 16)
)
if mibBuilder.loadTexts:
    flowEntityConfigPopCtagRcvCapTable.setStatus("current")
_FlowEntityConfigPopCtagRcvCapEntry_Object = MibTableRow
flowEntityConfigPopCtagRcvCapEntry = _FlowEntityConfigPopCtagRcvCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 16, 1)
)
flowEntityConfigPopCtagRcvCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionPopCtagRcvCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityConfigPopCtagRcvCapEntry.setStatus("current")
_FlowEntityConfigPopCtagRcvCapStringCap_Type = SnmpAdminString
_FlowEntityConfigPopCtagRcvCapStringCap_Object = MibTableColumn
flowEntityConfigPopCtagRcvCapStringCap = _FlowEntityConfigPopCtagRcvCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 16, 1, 1),
    _FlowEntityConfigPopCtagRcvCapStringCap_Type()
)
flowEntityConfigPopCtagRcvCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigPopCtagRcvCapStringCap.setStatus("current")
_FlowEntityConfigPopCtagTrmtCapTable_Object = MibTable
flowEntityConfigPopCtagTrmtCapTable = _FlowEntityConfigPopCtagTrmtCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 17)
)
if mibBuilder.loadTexts:
    flowEntityConfigPopCtagTrmtCapTable.setStatus("current")
_FlowEntityConfigPopCtagTrmtCapEntry_Object = MibTableRow
flowEntityConfigPopCtagTrmtCapEntry = _FlowEntityConfigPopCtagTrmtCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 17, 1)
)
flowEntityConfigPopCtagTrmtCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionPopCtagTrmtCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityConfigPopCtagTrmtCapEntry.setStatus("current")
_FlowEntityConfigPopCtagTrmtCapStringCap_Type = SnmpAdminString
_FlowEntityConfigPopCtagTrmtCapStringCap_Object = MibTableColumn
flowEntityConfigPopCtagTrmtCapStringCap = _FlowEntityConfigPopCtagTrmtCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 17, 1, 1),
    _FlowEntityConfigPopCtagTrmtCapStringCap_Type()
)
flowEntityConfigPopCtagTrmtCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigPopCtagTrmtCapStringCap.setStatus("current")
_FlowEntityConfigPushTrmtCapTable_Object = MibTable
flowEntityConfigPushTrmtCapTable = _FlowEntityConfigPushTrmtCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 18)
)
if mibBuilder.loadTexts:
    flowEntityConfigPushTrmtCapTable.setStatus("current")
_FlowEntityConfigPushTrmtCapEntry_Object = MibTableRow
flowEntityConfigPushTrmtCapEntry = _FlowEntityConfigPushTrmtCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 18, 1)
)
flowEntityConfigPushTrmtCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowEntityProvisionPushTrmtCapIndexCap"),
)
if mibBuilder.loadTexts:
    flowEntityConfigPushTrmtCapEntry.setStatus("current")
_FlowEntityConfigPushTrmtCapStringCap_Type = SnmpAdminString
_FlowEntityConfigPushTrmtCapStringCap_Object = MibTableColumn
flowEntityConfigPushTrmtCapStringCap = _FlowEntityConfigPushTrmtCapStringCap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 11, 18, 1, 1),
    _FlowEntityConfigPushTrmtCapStringCap_Type()
)
flowEntityConfigPushTrmtCapStringCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityConfigPushTrmtCapStringCap.setStatus("current")
_BridgeConfiguration_ObjectIdentity = ObjectIdentity
bridgeConfiguration = _BridgeConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12)
)
_BridgeEntityConfigTable_Object = MibTable
bridgeEntityConfigTable = _BridgeEntityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 11)
)
if mibBuilder.loadTexts:
    bridgeEntityConfigTable.setStatus("current")
_BridgeEntityConfigEntry_Object = MibTableRow
bridgeEntityConfigEntry = _BridgeEntityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 11, 1)
)
bridgeEntityConfigEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
)
if mibBuilder.loadTexts:
    bridgeEntityConfigEntry.setStatus("current")
_BridgeEntityConfigAlias_Type = SnmpAdminString
_BridgeEntityConfigAlias_Object = MibTableColumn
bridgeEntityConfigAlias = _BridgeEntityConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 11, 1, 1),
    _BridgeEntityConfigAlias_Type()
)
bridgeEntityConfigAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEntityConfigAlias.setStatus("current")
_BridgeEntityConfigShapeState_Type = FspR7DisableEnable
_BridgeEntityConfigShapeState_Object = MibTableColumn
bridgeEntityConfigShapeState = _BridgeEntityConfigShapeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 11, 1, 2),
    _BridgeEntityConfigShapeState_Type()
)
bridgeEntityConfigShapeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEntityConfigShapeState.setStatus("current")
_BridgeEntityConfigPmMode_Type = FspR7L2PmMode
_BridgeEntityConfigPmMode_Object = MibTableColumn
bridgeEntityConfigPmMode = _BridgeEntityConfigPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 11, 1, 3),
    _BridgeEntityConfigPmMode_Type()
)
bridgeEntityConfigPmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEntityConfigPmMode.setStatus("current")
_BridgeEntityConfigCirTrmt_Type = Unsigned32
_BridgeEntityConfigCirTrmt_Object = MibTableColumn
bridgeEntityConfigCirTrmt = _BridgeEntityConfigCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 11, 1, 4),
    _BridgeEntityConfigCirTrmt_Type()
)
bridgeEntityConfigCirTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEntityConfigCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntityConfigCirTrmt.setUnits("Mbit/s")


class _BridgeEntityConfigCbsTrmt_Type(Unsigned32):
    """Custom type bridgeEntityConfigCbsTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_BridgeEntityConfigCbsTrmt_Type.__name__ = "Unsigned32"
_BridgeEntityConfigCbsTrmt_Object = MibTableColumn
bridgeEntityConfigCbsTrmt = _BridgeEntityConfigCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 11, 1, 5),
    _BridgeEntityConfigCbsTrmt_Type()
)
bridgeEntityConfigCbsTrmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEntityConfigCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntityConfigCbsTrmt.setUnits("Kbytes")
_BridgeEntityConfigAdminState_Type = FspR7AdminState
_BridgeEntityConfigAdminState_Object = MibTableColumn
bridgeEntityConfigAdminState = _BridgeEntityConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 11, 1, 6),
    _BridgeEntityConfigAdminState_Type()
)
bridgeEntityConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEntityConfigAdminState.setStatus("current")
_BridgeEntityConfigCapTable_Object = MibTable
bridgeEntityConfigCapTable = _BridgeEntityConfigCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 12)
)
if mibBuilder.loadTexts:
    bridgeEntityConfigCapTable.setStatus("current")
_BridgeEntityConfigCapEntry_Object = MibTableRow
bridgeEntityConfigCapEntry = _BridgeEntityConfigCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 12, 1)
)
bridgeEntityConfigCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
)
if mibBuilder.loadTexts:
    bridgeEntityConfigCapEntry.setStatus("current")
_BridgeEntityConfigCapAlias_Type = Integer32
_BridgeEntityConfigCapAlias_Object = MibTableColumn
bridgeEntityConfigCapAlias = _BridgeEntityConfigCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 12, 1, 1),
    _BridgeEntityConfigCapAlias_Type()
)
bridgeEntityConfigCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityConfigCapAlias.setStatus("current")
_BridgeEntityConfigCapShapeState_Type = FspR7DisableEnableCaps
_BridgeEntityConfigCapShapeState_Object = MibTableColumn
bridgeEntityConfigCapShapeState = _BridgeEntityConfigCapShapeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 12, 1, 2),
    _BridgeEntityConfigCapShapeState_Type()
)
bridgeEntityConfigCapShapeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityConfigCapShapeState.setStatus("current")
_BridgeEntityConfigCapPmMode_Type = FspR7L2PmModeCaps
_BridgeEntityConfigCapPmMode_Object = MibTableColumn
bridgeEntityConfigCapPmMode = _BridgeEntityConfigCapPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 12, 1, 3),
    _BridgeEntityConfigCapPmMode_Type()
)
bridgeEntityConfigCapPmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityConfigCapPmMode.setStatus("current")
_BridgeEntityConfigCapCirTrmt_Type = FspR7Unsigned32Caps
_BridgeEntityConfigCapCirTrmt_Object = MibTableColumn
bridgeEntityConfigCapCirTrmt = _BridgeEntityConfigCapCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 12, 1, 4),
    _BridgeEntityConfigCapCirTrmt_Type()
)
bridgeEntityConfigCapCirTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityConfigCapCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntityConfigCapCirTrmt.setUnits("Mbit/s")
_BridgeEntityConfigCapCbsTrmt_Type = FspR7Unsigned32Caps
_BridgeEntityConfigCapCbsTrmt_Object = MibTableColumn
bridgeEntityConfigCapCbsTrmt = _BridgeEntityConfigCapCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 12, 1, 5),
    _BridgeEntityConfigCapCbsTrmt_Type()
)
bridgeEntityConfigCapCbsTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityConfigCapCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    bridgeEntityConfigCapCbsTrmt.setUnits("Kbytes")
_BridgeEntityConfigCapAdminState_Type = FspR7AdminStateCaps
_BridgeEntityConfigCapAdminState_Object = MibTableColumn
bridgeEntityConfigCapAdminState = _BridgeEntityConfigCapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 12, 12, 1, 6),
    _BridgeEntityConfigCapAdminState_Type()
)
bridgeEntityConfigCapAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityConfigCapAdminState.setStatus("current")
_QueOnBridgeConfiguration_ObjectIdentity = ObjectIdentity
queOnBridgeConfiguration = _QueOnBridgeConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 13)
)
_QueOnBridgeEntityConfigTable_Object = MibTable
queOnBridgeEntityConfigTable = _QueOnBridgeEntityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 13, 11)
)
if mibBuilder.loadTexts:
    queOnBridgeEntityConfigTable.setStatus("current")
_QueOnBridgeEntityConfigEntry_Object = MibTableRow
queOnBridgeEntityConfigEntry = _QueOnBridgeEntityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 13, 11, 1)
)
queOnBridgeEntityConfigEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityIndex"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityPrio"),
)
if mibBuilder.loadTexts:
    queOnBridgeEntityConfigEntry.setStatus("current")
_QueOnBridgeEntityConfigDataLayerPmReset_Type = FspR7PmReset
_QueOnBridgeEntityConfigDataLayerPmReset_Object = MibTableColumn
queOnBridgeEntityConfigDataLayerPmReset = _QueOnBridgeEntityConfigDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 13, 11, 1, 1),
    _QueOnBridgeEntityConfigDataLayerPmReset_Type()
)
queOnBridgeEntityConfigDataLayerPmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queOnBridgeEntityConfigDataLayerPmReset.setStatus("current")
_QueOnBridgeEntityConfigCapTable_Object = MibTable
queOnBridgeEntityConfigCapTable = _QueOnBridgeEntityConfigCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 13, 12)
)
if mibBuilder.loadTexts:
    queOnBridgeEntityConfigCapTable.setStatus("current")
_QueOnBridgeEntityConfigCapEntry_Object = MibTableRow
queOnBridgeEntityConfigCapEntry = _QueOnBridgeEntityConfigCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 13, 12, 1)
)
queOnBridgeEntityConfigCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityIndex"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityPrio"),
)
if mibBuilder.loadTexts:
    queOnBridgeEntityConfigCapEntry.setStatus("current")
_QueOnBridgeEntityConfigCapDataLayerPmReset_Type = FspR7PmResetCaps
_QueOnBridgeEntityConfigCapDataLayerPmReset_Object = MibTableColumn
queOnBridgeEntityConfigCapDataLayerPmReset = _QueOnBridgeEntityConfigCapDataLayerPmReset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 13, 13, 12, 1, 1),
    _QueOnBridgeEntityConfigCapDataLayerPmReset_Type()
)
queOnBridgeEntityConfigCapDataLayerPmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityConfigCapDataLayerPmReset.setStatus("current")
_Layer2StatusMIB_ObjectIdentity = ObjectIdentity
layer2StatusMIB = _Layer2StatusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14)
)
_FlowStatus_ObjectIdentity = ObjectIdentity
flowStatus = _FlowStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11)
)
_FlowEntityStatusTable_Object = MibTable
flowEntityStatusTable = _FlowEntityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11)
)
if mibBuilder.loadTexts:
    flowEntityStatusTable.setStatus("current")
_FlowEntityStatusEntry_Object = MibTableRow
flowEntityStatusEntry = _FlowEntityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11, 1)
)
flowEntityStatusEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowEntityStatusEntry.setStatus("current")
_FlowEntityStatusOper_Type = FspR7OperState
_FlowEntityStatusOper_Object = MibTableColumn
flowEntityStatusOper = _FlowEntityStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11, 1, 1),
    _FlowEntityStatusOper_Type()
)
flowEntityStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityStatusOper.setStatus("current")
_FlowEntityStatusSecondaryStates_Type = FspR7EntitySecondaryStates
_FlowEntityStatusSecondaryStates_Object = MibTableColumn
flowEntityStatusSecondaryStates = _FlowEntityStatusSecondaryStates_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11, 1, 2),
    _FlowEntityStatusSecondaryStates_Type()
)
flowEntityStatusSecondaryStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityStatusSecondaryStates.setStatus("current")
_FlowEntityStatusType_Type = FspR7InterfaceType
_FlowEntityStatusType_Object = MibTableColumn
flowEntityStatusType = _FlowEntityStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11, 1, 3),
    _FlowEntityStatusType_Type()
)
flowEntityStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityStatusType.setStatus("current")
_FlowEntityStatusInternalSvid_Type = Unsigned32
_FlowEntityStatusInternalSvid_Object = MibTableColumn
flowEntityStatusInternalSvid = _FlowEntityStatusInternalSvid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11, 1, 4),
    _FlowEntityStatusInternalSvid_Type()
)
flowEntityStatusInternalSvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityStatusInternalSvid.setStatus("current")
_FlowEntityStatusConnectionState_Type = FspR7ConnectState
_FlowEntityStatusConnectionState_Object = MibTableColumn
flowEntityStatusConnectionState = _FlowEntityStatusConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11, 1, 5),
    _FlowEntityStatusConnectionState_Type()
)
flowEntityStatusConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityStatusConnectionState.setStatus("current")


class _FlowEntityStatusValidSignalTimer_Type(Unsigned32):
    """Custom type flowEntityStatusValidSignalTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5760),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_FlowEntityStatusValidSignalTimer_Type.__name__ = "Unsigned32"
_FlowEntityStatusValidSignalTimer_Object = MibTableColumn
flowEntityStatusValidSignalTimer = _FlowEntityStatusValidSignalTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11, 1, 6),
    _FlowEntityStatusValidSignalTimer_Type()
)
flowEntityStatusValidSignalTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityStatusValidSignalTimer.setStatus("current")
if mibBuilder.loadTexts:
    flowEntityStatusValidSignalTimer.setUnits("min")
_FlowEntityStatusProtectionRole_Type = FspR7ProtectionRole
_FlowEntityStatusProtectionRole_Object = MibTableColumn
flowEntityStatusProtectionRole = _FlowEntityStatusProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11, 1, 7),
    _FlowEntityStatusProtectionRole_Type()
)
flowEntityStatusProtectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityStatusProtectionRole.setStatus("current")
_FlowEntityStatusIngressTid_Type = SnmpAdminString
_FlowEntityStatusIngressTid_Object = MibTableColumn
flowEntityStatusIngressTid = _FlowEntityStatusIngressTid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11, 1, 8),
    _FlowEntityStatusIngressTid_Type()
)
flowEntityStatusIngressTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityStatusIngressTid.setStatus("current")
_FlowEntityStatusIngressNodeIp_Type = IpAddress
_FlowEntityStatusIngressNodeIp_Object = MibTableColumn
flowEntityStatusIngressNodeIp = _FlowEntityStatusIngressNodeIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 11, 11, 1, 9),
    _FlowEntityStatusIngressNodeIp_Type()
)
flowEntityStatusIngressNodeIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowEntityStatusIngressNodeIp.setStatus("current")
_CtransStatus_ObjectIdentity = ObjectIdentity
ctransStatus = _CtransStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 12)
)
_CtransEntityStatusTable_Object = MibTable
ctransEntityStatusTable = _CtransEntityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 12, 11)
)
if mibBuilder.loadTexts:
    ctransEntityStatusTable.setStatus("current")
_CtransEntityStatusEntry_Object = MibTableRow
ctransEntityStatusEntry = _CtransEntityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 12, 11, 1)
)
ctransEntityStatusEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "ctransEntityIndexCVlanId"),
)
if mibBuilder.loadTexts:
    ctransEntityStatusEntry.setStatus("current")
_CtransEntityStatusType_Type = FspR7InterfaceType
_CtransEntityStatusType_Object = MibTableColumn
ctransEntityStatusType = _CtransEntityStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 12, 11, 1, 1),
    _CtransEntityStatusType_Type()
)
ctransEntityStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityStatusType.setStatus("current")


class _CtransEntityStatusCvidInternal_Type(Unsigned32):
    """Custom type ctransEntityStatusCvidInternal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_CtransEntityStatusCvidInternal_Type.__name__ = "Unsigned32"
_CtransEntityStatusCvidInternal_Object = MibTableColumn
ctransEntityStatusCvidInternal = _CtransEntityStatusCvidInternal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 12, 11, 1, 2),
    _CtransEntityStatusCvidInternal_Type()
)
ctransEntityStatusCvidInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityStatusCvidInternal.setStatus("current")


class _CtransEntityStatusRange_Type(Unsigned32):
    """Custom type ctransEntityStatusRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_CtransEntityStatusRange_Type.__name__ = "Unsigned32"
_CtransEntityStatusRange_Object = MibTableColumn
ctransEntityStatusRange = _CtransEntityStatusRange_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 12, 11, 1, 3),
    _CtransEntityStatusRange_Type()
)
ctransEntityStatusRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctransEntityStatusRange.setStatus("current")
_PolicerStatus_ObjectIdentity = ObjectIdentity
policerStatus = _PolicerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 13)
)
_PolicerOnFlowEntityStatusTable_Object = MibTable
policerOnFlowEntityStatusTable = _PolicerOnFlowEntityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 13, 12)
)
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusTable.setStatus("current")
_PolicerOnFlowEntityStatusEntry_Object = MibTableRow
policerOnFlowEntityStatusEntry = _PolicerOnFlowEntityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 13, 12, 1)
)
policerOnFlowEntityStatusEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexPolicer"),
)
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusEntry.setStatus("current")
_PolicerOnFlowEntityStatusOper_Type = FspR7OperState
_PolicerOnFlowEntityStatusOper_Object = MibTableColumn
policerOnFlowEntityStatusOper = _PolicerOnFlowEntityStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 13, 12, 1, 1),
    _PolicerOnFlowEntityStatusOper_Type()
)
policerOnFlowEntityStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusOper.setStatus("current")
_PolicerOnFlowEntityStatusSecondaryStates_Type = FspR7EntitySecondaryStates
_PolicerOnFlowEntityStatusSecondaryStates_Object = MibTableColumn
policerOnFlowEntityStatusSecondaryStates = _PolicerOnFlowEntityStatusSecondaryStates_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 13, 12, 1, 2),
    _PolicerOnFlowEntityStatusSecondaryStates_Type()
)
policerOnFlowEntityStatusSecondaryStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusSecondaryStates.setStatus("current")
_PolicerOnFlowEntityStatusType_Type = FspR7InterfaceType
_PolicerOnFlowEntityStatusType_Object = MibTableColumn
policerOnFlowEntityStatusType = _PolicerOnFlowEntityStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 13, 12, 1, 3),
    _PolicerOnFlowEntityStatusType_Type()
)
policerOnFlowEntityStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusType.setStatus("current")
_PolicerOnFlowEntityStatusAdmin_Type = FspR7AdminState
_PolicerOnFlowEntityStatusAdmin_Object = MibTableColumn
policerOnFlowEntityStatusAdmin = _PolicerOnFlowEntityStatusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 13, 12, 1, 4),
    _PolicerOnFlowEntityStatusAdmin_Type()
)
policerOnFlowEntityStatusAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusAdmin.setStatus("current")
_PolicerOnFlowEntityStatusAlias_Type = SnmpAdminString
_PolicerOnFlowEntityStatusAlias_Object = MibTableColumn
policerOnFlowEntityStatusAlias = _PolicerOnFlowEntityStatusAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 13, 12, 1, 5),
    _PolicerOnFlowEntityStatusAlias_Type()
)
policerOnFlowEntityStatusAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusAlias.setStatus("current")
_PolicerOnFlowEntityStatusCirRcv_Type = Unsigned32
_PolicerOnFlowEntityStatusCirRcv_Object = MibTableColumn
policerOnFlowEntityStatusCirRcv = _PolicerOnFlowEntityStatusCirRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 13, 12, 1, 6),
    _PolicerOnFlowEntityStatusCirRcv_Type()
)
policerOnFlowEntityStatusCirRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusCirRcv.setStatus("current")
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusCirRcv.setUnits("Mbit/s")


class _PolicerOnFlowEntityStatusCbsRcv_Type(Unsigned32):
    """Custom type policerOnFlowEntityStatusCbsRcv based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26214400),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_PolicerOnFlowEntityStatusCbsRcv_Type.__name__ = "Unsigned32"
_PolicerOnFlowEntityStatusCbsRcv_Object = MibTableColumn
policerOnFlowEntityStatusCbsRcv = _PolicerOnFlowEntityStatusCbsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 13, 12, 1, 7),
    _PolicerOnFlowEntityStatusCbsRcv_Type()
)
policerOnFlowEntityStatusCbsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusCbsRcv.setStatus("current")
if mibBuilder.loadTexts:
    policerOnFlowEntityStatusCbsRcv.setUnits("bytes")
_QueStatus_ObjectIdentity = ObjectIdentity
queStatus = _QueStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14)
)
_QueOnPortEntityStatusTable_Object = MibTable
queOnPortEntityStatusTable = _QueOnPortEntityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 11)
)
if mibBuilder.loadTexts:
    queOnPortEntityStatusTable.setStatus("current")
_QueOnPortEntityStatusEntry_Object = MibTableRow
queOnPortEntityStatusEntry = _QueOnPortEntityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 11, 1)
)
queOnPortEntityStatusEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexPrio"),
)
if mibBuilder.loadTexts:
    queOnPortEntityStatusEntry.setStatus("current")
_QueOnPortEntityStatusOper_Type = FspR7OperState
_QueOnPortEntityStatusOper_Object = MibTableColumn
queOnPortEntityStatusOper = _QueOnPortEntityStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 11, 1, 1),
    _QueOnPortEntityStatusOper_Type()
)
queOnPortEntityStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnPortEntityStatusOper.setStatus("current")
_QueOnPortEntityStatusSecondaryStates_Type = FspR7EntitySecondaryStates
_QueOnPortEntityStatusSecondaryStates_Object = MibTableColumn
queOnPortEntityStatusSecondaryStates = _QueOnPortEntityStatusSecondaryStates_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 11, 1, 2),
    _QueOnPortEntityStatusSecondaryStates_Type()
)
queOnPortEntityStatusSecondaryStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnPortEntityStatusSecondaryStates.setStatus("current")
_QueOnPortEntityStatusType_Type = FspR7InterfaceType
_QueOnPortEntityStatusType_Object = MibTableColumn
queOnPortEntityStatusType = _QueOnPortEntityStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 11, 1, 3),
    _QueOnPortEntityStatusType_Type()
)
queOnPortEntityStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnPortEntityStatusType.setStatus("current")
_QueOnPortEntityStatusAdmin_Type = FspR7AdminState
_QueOnPortEntityStatusAdmin_Object = MibTableColumn
queOnPortEntityStatusAdmin = _QueOnPortEntityStatusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 11, 1, 4),
    _QueOnPortEntityStatusAdmin_Type()
)
queOnPortEntityStatusAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnPortEntityStatusAdmin.setStatus("current")
_QueOnPortEntityStatusAlias_Type = SnmpAdminString
_QueOnPortEntityStatusAlias_Object = MibTableColumn
queOnPortEntityStatusAlias = _QueOnPortEntityStatusAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 11, 1, 5),
    _QueOnPortEntityStatusAlias_Type()
)
queOnPortEntityStatusAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnPortEntityStatusAlias.setStatus("current")
_QueOnPortEntityStatusCirTrmt_Type = Unsigned32
_QueOnPortEntityStatusCirTrmt_Object = MibTableColumn
queOnPortEntityStatusCirTrmt = _QueOnPortEntityStatusCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 11, 1, 6),
    _QueOnPortEntityStatusCirTrmt_Type()
)
queOnPortEntityStatusCirTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnPortEntityStatusCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    queOnPortEntityStatusCirTrmt.setUnits("Mbit/s")


class _QueOnPortEntityStatusCbsTrmt_Type(Unsigned32):
    """Custom type queOnPortEntityStatusCbsTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_QueOnPortEntityStatusCbsTrmt_Type.__name__ = "Unsigned32"
_QueOnPortEntityStatusCbsTrmt_Object = MibTableColumn
queOnPortEntityStatusCbsTrmt = _QueOnPortEntityStatusCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 11, 1, 7),
    _QueOnPortEntityStatusCbsTrmt_Type()
)
queOnPortEntityStatusCbsTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnPortEntityStatusCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    queOnPortEntityStatusCbsTrmt.setUnits("Kbytes")
_QueOnFlowEntityStatusTable_Object = MibTable
queOnFlowEntityStatusTable = _QueOnFlowEntityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 12)
)
if mibBuilder.loadTexts:
    queOnFlowEntityStatusTable.setStatus("current")
_QueOnFlowEntityStatusEntry_Object = MibTableRow
queOnFlowEntityStatusEntry = _QueOnFlowEntityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 12, 1)
)
queOnFlowEntityStatusEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexPrio"),
)
if mibBuilder.loadTexts:
    queOnFlowEntityStatusEntry.setStatus("current")
_QueOnFlowEntityStatusOper_Type = FspR7OperState
_QueOnFlowEntityStatusOper_Object = MibTableColumn
queOnFlowEntityStatusOper = _QueOnFlowEntityStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 12, 1, 1),
    _QueOnFlowEntityStatusOper_Type()
)
queOnFlowEntityStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnFlowEntityStatusOper.setStatus("current")
_QueOnFlowEntityStatusSecondaryStates_Type = FspR7EntitySecondaryStates
_QueOnFlowEntityStatusSecondaryStates_Object = MibTableColumn
queOnFlowEntityStatusSecondaryStates = _QueOnFlowEntityStatusSecondaryStates_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 12, 1, 2),
    _QueOnFlowEntityStatusSecondaryStates_Type()
)
queOnFlowEntityStatusSecondaryStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnFlowEntityStatusSecondaryStates.setStatus("current")
_QueOnFlowEntityStatusType_Type = FspR7InterfaceType
_QueOnFlowEntityStatusType_Object = MibTableColumn
queOnFlowEntityStatusType = _QueOnFlowEntityStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 12, 1, 3),
    _QueOnFlowEntityStatusType_Type()
)
queOnFlowEntityStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnFlowEntityStatusType.setStatus("current")
_QueOnFlowEntityStatusAdmin_Type = FspR7AdminState
_QueOnFlowEntityStatusAdmin_Object = MibTableColumn
queOnFlowEntityStatusAdmin = _QueOnFlowEntityStatusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 12, 1, 4),
    _QueOnFlowEntityStatusAdmin_Type()
)
queOnFlowEntityStatusAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnFlowEntityStatusAdmin.setStatus("current")
_QueOnFlowEntityStatusAlias_Type = SnmpAdminString
_QueOnFlowEntityStatusAlias_Object = MibTableColumn
queOnFlowEntityStatusAlias = _QueOnFlowEntityStatusAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 12, 1, 5),
    _QueOnFlowEntityStatusAlias_Type()
)
queOnFlowEntityStatusAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnFlowEntityStatusAlias.setStatus("current")
_QueOnFlowEntityStatusCirTrmt_Type = Unsigned32
_QueOnFlowEntityStatusCirTrmt_Object = MibTableColumn
queOnFlowEntityStatusCirTrmt = _QueOnFlowEntityStatusCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 12, 1, 6),
    _QueOnFlowEntityStatusCirTrmt_Type()
)
queOnFlowEntityStatusCirTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnFlowEntityStatusCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    queOnFlowEntityStatusCirTrmt.setUnits("Mbit/s")


class _QueOnFlowEntityStatusCbsTrmt_Type(Unsigned32):
    """Custom type queOnFlowEntityStatusCbsTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_QueOnFlowEntityStatusCbsTrmt_Type.__name__ = "Unsigned32"
_QueOnFlowEntityStatusCbsTrmt_Object = MibTableColumn
queOnFlowEntityStatusCbsTrmt = _QueOnFlowEntityStatusCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 12, 1, 7),
    _QueOnFlowEntityStatusCbsTrmt_Type()
)
queOnFlowEntityStatusCbsTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnFlowEntityStatusCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    queOnFlowEntityStatusCbsTrmt.setUnits("Kbytes")
_QueOnBridgeEntityStatusTable_Object = MibTable
queOnBridgeEntityStatusTable = _QueOnBridgeEntityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13)
)
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusTable.setStatus("current")
_QueOnBridgeEntityStatusEntry_Object = MibTableRow
queOnBridgeEntityStatusEntry = _QueOnBridgeEntityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1)
)
queOnBridgeEntityStatusEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityIndex"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityPrio"),
)
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusEntry.setStatus("current")
_QueOnBridgeEntityStatusAdminState_Type = FspR7AdminState
_QueOnBridgeEntityStatusAdminState_Object = MibTableColumn
queOnBridgeEntityStatusAdminState = _QueOnBridgeEntityStatusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1, 1),
    _QueOnBridgeEntityStatusAdminState_Type()
)
queOnBridgeEntityStatusAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusAdminState.setStatus("current")
_QueOnBridgeEntityStatusFacilityType_Type = FspR7InterfaceType
_QueOnBridgeEntityStatusFacilityType_Object = MibTableColumn
queOnBridgeEntityStatusFacilityType = _QueOnBridgeEntityStatusFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1, 2),
    _QueOnBridgeEntityStatusFacilityType_Type()
)
queOnBridgeEntityStatusFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusFacilityType.setStatus("current")
_QueOnBridgeEntityStatusFunction_Type = FspR7InterfaceFunction
_QueOnBridgeEntityStatusFunction_Object = MibTableColumn
queOnBridgeEntityStatusFunction = _QueOnBridgeEntityStatusFunction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1, 3),
    _QueOnBridgeEntityStatusFunction_Type()
)
queOnBridgeEntityStatusFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusFunction.setStatus("current")
_QueOnBridgeEntityStatusAlias_Type = SnmpAdminString
_QueOnBridgeEntityStatusAlias_Object = MibTableColumn
queOnBridgeEntityStatusAlias = _QueOnBridgeEntityStatusAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1, 4),
    _QueOnBridgeEntityStatusAlias_Type()
)
queOnBridgeEntityStatusAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusAlias.setStatus("current")
_QueOnBridgeEntityStatusCirTrmt_Type = Unsigned32
_QueOnBridgeEntityStatusCirTrmt_Object = MibTableColumn
queOnBridgeEntityStatusCirTrmt = _QueOnBridgeEntityStatusCirTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1, 5),
    _QueOnBridgeEntityStatusCirTrmt_Type()
)
queOnBridgeEntityStatusCirTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusCirTrmt.setStatus("current")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusCirTrmt.setUnits("Mbit/s")


class _QueOnBridgeEntityStatusCbsTrmt_Type(Unsigned32):
    """Custom type queOnBridgeEntityStatusCbsTrmt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25600),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_QueOnBridgeEntityStatusCbsTrmt_Type.__name__ = "Unsigned32"
_QueOnBridgeEntityStatusCbsTrmt_Object = MibTableColumn
queOnBridgeEntityStatusCbsTrmt = _QueOnBridgeEntityStatusCbsTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1, 6),
    _QueOnBridgeEntityStatusCbsTrmt_Type()
)
queOnBridgeEntityStatusCbsTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusCbsTrmt.setStatus("current")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusCbsTrmt.setUnits("Kbytes")
_QueOnBridgeEntityStatusShapeState_Type = FspR7DisableEnable
_QueOnBridgeEntityStatusShapeState_Object = MibTableColumn
queOnBridgeEntityStatusShapeState = _QueOnBridgeEntityStatusShapeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1, 7),
    _QueOnBridgeEntityStatusShapeState_Type()
)
queOnBridgeEntityStatusShapeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusShapeState.setStatus("current")
_QueOnBridgeEntityStatusPmMode_Type = FspR7L2PmMode
_QueOnBridgeEntityStatusPmMode_Object = MibTableColumn
queOnBridgeEntityStatusPmMode = _QueOnBridgeEntityStatusPmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1, 8),
    _QueOnBridgeEntityStatusPmMode_Type()
)
queOnBridgeEntityStatusPmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusPmMode.setStatus("current")
_QueOnBridgeEntityStatusOper_Type = FspR7OperState
_QueOnBridgeEntityStatusOper_Object = MibTableColumn
queOnBridgeEntityStatusOper = _QueOnBridgeEntityStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1, 9),
    _QueOnBridgeEntityStatusOper_Type()
)
queOnBridgeEntityStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusOper.setStatus("current")
_QueOnBridgeEntityStatusSecondaryStates_Type = FspR7EntitySecondaryStates
_QueOnBridgeEntityStatusSecondaryStates_Object = MibTableColumn
queOnBridgeEntityStatusSecondaryStates = _QueOnBridgeEntityStatusSecondaryStates_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 14, 13, 1, 10),
    _QueOnBridgeEntityStatusSecondaryStates_Type()
)
queOnBridgeEntityStatusSecondaryStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queOnBridgeEntityStatusSecondaryStates.setStatus("current")
_BridgeStatus_ObjectIdentity = ObjectIdentity
bridgeStatus = _BridgeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 15)
)
_BridgeEntityStatusTable_Object = MibTable
bridgeEntityStatusTable = _BridgeEntityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 15, 11)
)
if mibBuilder.loadTexts:
    bridgeEntityStatusTable.setStatus("current")
_BridgeEntityStatusEntry_Object = MibTableRow
bridgeEntityStatusEntry = _BridgeEntityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 15, 11, 1)
)
bridgeEntityStatusEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
)
if mibBuilder.loadTexts:
    bridgeEntityStatusEntry.setStatus("current")
_BridgeEntityStatusFacilityType_Type = FspR7InterfaceType
_BridgeEntityStatusFacilityType_Object = MibTableColumn
bridgeEntityStatusFacilityType = _BridgeEntityStatusFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 15, 11, 1, 1),
    _BridgeEntityStatusFacilityType_Type()
)
bridgeEntityStatusFacilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityStatusFacilityType.setStatus("current")
_BridgeEntityFlowTable_Object = MibTable
bridgeEntityFlowTable = _BridgeEntityFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 15, 12)
)
if mibBuilder.loadTexts:
    bridgeEntityFlowTable.setStatus("current")
_BridgeEntityFlowEntry_Object = MibTableRow
bridgeEntityFlowEntry = _BridgeEntityFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 15, 12, 1)
)
bridgeEntityFlowEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntityFlowId"),
)
if mibBuilder.loadTexts:
    bridgeEntityFlowEntry.setStatus("current")
_BridgeEntityFlowId_Type = BridgeEntityIndex
_BridgeEntityFlowId_Object = MibTableColumn
bridgeEntityFlowId = _BridgeEntityFlowId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 15, 12, 1, 1),
    _BridgeEntityFlowId_Type()
)
bridgeEntityFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeEntityFlowId.setStatus("current")
_BridgeEntityFlowIndex_Type = EntityIndex
_BridgeEntityFlowIndex_Object = MibTableColumn
bridgeEntityFlowIndex = _BridgeEntityFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 14, 15, 12, 1, 2),
    _BridgeEntityFlowIndex_Type()
)
bridgeEntityFlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeEntityFlowIndex.setStatus("current")
_Layer2CrossConnections_ObjectIdentity = ObjectIdentity
layer2CrossConnections = _Layer2CrossConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15)
)
_CrossConnectionsProvisioningTable_Object = MibTable
crossConnectionsProvisioningTable = _CrossConnectionsProvisioningTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11)
)
if mibBuilder.loadTexts:
    crossConnectionsProvisioningTable.setStatus("current")
_CrossConnectionsProvisioningEntry_Object = MibTableRow
crossConnectionsProvisioningEntry = _CrossConnectionsProvisioningEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11, 1)
)
crossConnectionsProvisioningEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthTo"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowTo"),
)
if mibBuilder.loadTexts:
    crossConnectionsProvisioningEntry.setStatus("current")
_CrossConnectionsProvisioningIndexEthFrom_Type = EntityIndex
_CrossConnectionsProvisioningIndexEthFrom_Object = MibTableColumn
crossConnectionsProvisioningIndexEthFrom = _CrossConnectionsProvisioningIndexEthFrom_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11, 1, 1),
    _CrossConnectionsProvisioningIndexEthFrom_Type()
)
crossConnectionsProvisioningIndexEthFrom.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningIndexEthFrom.setStatus("current")
_CrossConnectionsProvisioningIndexFlowFrom_Type = EntityIndex
_CrossConnectionsProvisioningIndexFlowFrom_Object = MibTableColumn
crossConnectionsProvisioningIndexFlowFrom = _CrossConnectionsProvisioningIndexFlowFrom_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11, 1, 2),
    _CrossConnectionsProvisioningIndexFlowFrom_Type()
)
crossConnectionsProvisioningIndexFlowFrom.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningIndexFlowFrom.setStatus("current")
_CrossConnectionsProvisioningIndexEthTo_Type = EntityIndex
_CrossConnectionsProvisioningIndexEthTo_Object = MibTableColumn
crossConnectionsProvisioningIndexEthTo = _CrossConnectionsProvisioningIndexEthTo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11, 1, 3),
    _CrossConnectionsProvisioningIndexEthTo_Type()
)
crossConnectionsProvisioningIndexEthTo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningIndexEthTo.setStatus("current")
_CrossConnectionsProvisioningIndexFlowTo_Type = EntityIndex
_CrossConnectionsProvisioningIndexFlowTo_Object = MibTableColumn
crossConnectionsProvisioningIndexFlowTo = _CrossConnectionsProvisioningIndexFlowTo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11, 1, 4),
    _CrossConnectionsProvisioningIndexFlowTo_Type()
)
crossConnectionsProvisioningIndexFlowTo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningIndexFlowTo.setStatus("current")
_CrossConnectionsProvisioningRowStatus_Type = RowStatus
_CrossConnectionsProvisioningRowStatus_Object = MibTableColumn
crossConnectionsProvisioningRowStatus = _CrossConnectionsProvisioningRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11, 1, 5),
    _CrossConnectionsProvisioningRowStatus_Type()
)
crossConnectionsProvisioningRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningRowStatus.setStatus("current")
_CrossConnectionsProvisioningAlias_Type = SnmpAdminString
_CrossConnectionsProvisioningAlias_Object = MibTableColumn
crossConnectionsProvisioningAlias = _CrossConnectionsProvisioningAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11, 1, 6),
    _CrossConnectionsProvisioningAlias_Type()
)
crossConnectionsProvisioningAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningAlias.setStatus("current")
_CrossConnectionsProvisioningType_Type = FspR7InterfaceType
_CrossConnectionsProvisioningType_Object = MibTableColumn
crossConnectionsProvisioningType = _CrossConnectionsProvisioningType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11, 1, 7),
    _CrossConnectionsProvisioningType_Type()
)
crossConnectionsProvisioningType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningType.setStatus("current")
_CrossConnectionsProvisioningCrsType_Type = FspR7TypeCrs
_CrossConnectionsProvisioningCrsType_Object = MibTableColumn
crossConnectionsProvisioningCrsType = _CrossConnectionsProvisioningCrsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11, 1, 8),
    _CrossConnectionsProvisioningCrsType_Type()
)
crossConnectionsProvisioningCrsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCrsType.setStatus("current")
_CrossConnectionsProvisioningConn_Type = FspR7Conn
_CrossConnectionsProvisioningConn_Object = MibTableColumn
crossConnectionsProvisioningConn = _CrossConnectionsProvisioningConn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 11, 1, 9),
    _CrossConnectionsProvisioningConn_Type()
)
crossConnectionsProvisioningConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningConn.setStatus("current")
_CrossConnectionsProvisioningCapTable_Object = MibTable
crossConnectionsProvisioningCapTable = _CrossConnectionsProvisioningCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12)
)
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapTable.setStatus("current")
_CrossConnectionsProvisioningCapEntry_Object = MibTableRow
crossConnectionsProvisioningCapEntry = _CrossConnectionsProvisioningCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12, 1)
)
crossConnectionsProvisioningCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthTo"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowTo"),
)
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapEntry.setStatus("current")
_CrossConnectionsProvisioningCapIndexEthFrom_Type = Integer32
_CrossConnectionsProvisioningCapIndexEthFrom_Object = MibTableColumn
crossConnectionsProvisioningCapIndexEthFrom = _CrossConnectionsProvisioningCapIndexEthFrom_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12, 1, 1),
    _CrossConnectionsProvisioningCapIndexEthFrom_Type()
)
crossConnectionsProvisioningCapIndexEthFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapIndexEthFrom.setStatus("current")
_CrossConnectionsProvisioningCapIndexFlowFrom_Type = Integer32
_CrossConnectionsProvisioningCapIndexFlowFrom_Object = MibTableColumn
crossConnectionsProvisioningCapIndexFlowFrom = _CrossConnectionsProvisioningCapIndexFlowFrom_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12, 1, 2),
    _CrossConnectionsProvisioningCapIndexFlowFrom_Type()
)
crossConnectionsProvisioningCapIndexFlowFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapIndexFlowFrom.setStatus("current")
_CrossConnectionsProvisioningCapIndexEthTo_Type = Integer32
_CrossConnectionsProvisioningCapIndexEthTo_Object = MibTableColumn
crossConnectionsProvisioningCapIndexEthTo = _CrossConnectionsProvisioningCapIndexEthTo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12, 1, 3),
    _CrossConnectionsProvisioningCapIndexEthTo_Type()
)
crossConnectionsProvisioningCapIndexEthTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapIndexEthTo.setStatus("current")
_CrossConnectionsProvisioningCapIndexFlowTo_Type = Integer32
_CrossConnectionsProvisioningCapIndexFlowTo_Object = MibTableColumn
crossConnectionsProvisioningCapIndexFlowTo = _CrossConnectionsProvisioningCapIndexFlowTo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12, 1, 4),
    _CrossConnectionsProvisioningCapIndexFlowTo_Type()
)
crossConnectionsProvisioningCapIndexFlowTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapIndexFlowTo.setStatus("current")
_CrossConnectionsProvisioningCapRowStatus_Type = FspR7RowStatusCaps
_CrossConnectionsProvisioningCapRowStatus_Object = MibTableColumn
crossConnectionsProvisioningCapRowStatus = _CrossConnectionsProvisioningCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12, 1, 5),
    _CrossConnectionsProvisioningCapRowStatus_Type()
)
crossConnectionsProvisioningCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapRowStatus.setStatus("current")
_CrossConnectionsProvisioningCapAlias_Type = Integer32
_CrossConnectionsProvisioningCapAlias_Object = MibTableColumn
crossConnectionsProvisioningCapAlias = _CrossConnectionsProvisioningCapAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12, 1, 6),
    _CrossConnectionsProvisioningCapAlias_Type()
)
crossConnectionsProvisioningCapAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapAlias.setStatus("current")
_CrossConnectionsProvisioningCapType_Type = FspR7InterfaceTypeCaps
_CrossConnectionsProvisioningCapType_Object = MibTableColumn
crossConnectionsProvisioningCapType = _CrossConnectionsProvisioningCapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12, 1, 7),
    _CrossConnectionsProvisioningCapType_Type()
)
crossConnectionsProvisioningCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapType.setStatus("current")
_CrossConnectionsProvisioningCapCrsType_Type = FspR7TypeCrsCaps
_CrossConnectionsProvisioningCapCrsType_Object = MibTableColumn
crossConnectionsProvisioningCapCrsType = _CrossConnectionsProvisioningCapCrsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12, 1, 8),
    _CrossConnectionsProvisioningCapCrsType_Type()
)
crossConnectionsProvisioningCapCrsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapCrsType.setStatus("current")
_CrossConnectionsProvisioningCapConn_Type = FspR7ConnCaps
_CrossConnectionsProvisioningCapConn_Object = MibTableColumn
crossConnectionsProvisioningCapConn = _CrossConnectionsProvisioningCapConn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 12, 1, 9),
    _CrossConnectionsProvisioningCapConn_Type()
)
crossConnectionsProvisioningCapConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningCapConn.setStatus("current")
_CrossConnectionsProvisioningDefaultsTable_Object = MibTable
crossConnectionsProvisioningDefaultsTable = _CrossConnectionsProvisioningDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13)
)
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsTable.setStatus("current")
_CrossConnectionsProvisioningDefaultsEntry_Object = MibTableRow
crossConnectionsProvisioningDefaultsEntry = _CrossConnectionsProvisioningDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13, 1)
)
crossConnectionsProvisioningDefaultsEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthTo"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowTo"),
)
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsEntry.setStatus("current")
_CrossConnectionsProvisioningDefaultsIndexEthFrom_Type = EntityIndex
_CrossConnectionsProvisioningDefaultsIndexEthFrom_Object = MibTableColumn
crossConnectionsProvisioningDefaultsIndexEthFrom = _CrossConnectionsProvisioningDefaultsIndexEthFrom_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13, 1, 1),
    _CrossConnectionsProvisioningDefaultsIndexEthFrom_Type()
)
crossConnectionsProvisioningDefaultsIndexEthFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsIndexEthFrom.setStatus("current")
_CrossConnectionsProvisioningDefaultsIndexFlowFrom_Type = EntityIndex
_CrossConnectionsProvisioningDefaultsIndexFlowFrom_Object = MibTableColumn
crossConnectionsProvisioningDefaultsIndexFlowFrom = _CrossConnectionsProvisioningDefaultsIndexFlowFrom_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13, 1, 2),
    _CrossConnectionsProvisioningDefaultsIndexFlowFrom_Type()
)
crossConnectionsProvisioningDefaultsIndexFlowFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsIndexFlowFrom.setStatus("current")
_CrossConnectionsProvisioningDefaultsIndexEthTo_Type = EntityIndex
_CrossConnectionsProvisioningDefaultsIndexEthTo_Object = MibTableColumn
crossConnectionsProvisioningDefaultsIndexEthTo = _CrossConnectionsProvisioningDefaultsIndexEthTo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13, 1, 3),
    _CrossConnectionsProvisioningDefaultsIndexEthTo_Type()
)
crossConnectionsProvisioningDefaultsIndexEthTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsIndexEthTo.setStatus("current")
_CrossConnectionsProvisioningDefaultsIndexFlowTo_Type = EntityIndex
_CrossConnectionsProvisioningDefaultsIndexFlowTo_Object = MibTableColumn
crossConnectionsProvisioningDefaultsIndexFlowTo = _CrossConnectionsProvisioningDefaultsIndexFlowTo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13, 1, 4),
    _CrossConnectionsProvisioningDefaultsIndexFlowTo_Type()
)
crossConnectionsProvisioningDefaultsIndexFlowTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsIndexFlowTo.setStatus("current")
_CrossConnectionsProvisioningDefaultsRowStatus_Type = RowStatus
_CrossConnectionsProvisioningDefaultsRowStatus_Object = MibTableColumn
crossConnectionsProvisioningDefaultsRowStatus = _CrossConnectionsProvisioningDefaultsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13, 1, 5),
    _CrossConnectionsProvisioningDefaultsRowStatus_Type()
)
crossConnectionsProvisioningDefaultsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsRowStatus.setStatus("current")
_CrossConnectionsProvisioningDefaultsAlias_Type = SnmpAdminString
_CrossConnectionsProvisioningDefaultsAlias_Object = MibTableColumn
crossConnectionsProvisioningDefaultsAlias = _CrossConnectionsProvisioningDefaultsAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13, 1, 6),
    _CrossConnectionsProvisioningDefaultsAlias_Type()
)
crossConnectionsProvisioningDefaultsAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsAlias.setStatus("current")
_CrossConnectionsProvisioningDefaultsType_Type = FspR7InterfaceType
_CrossConnectionsProvisioningDefaultsType_Object = MibTableColumn
crossConnectionsProvisioningDefaultsType = _CrossConnectionsProvisioningDefaultsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13, 1, 7),
    _CrossConnectionsProvisioningDefaultsType_Type()
)
crossConnectionsProvisioningDefaultsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsType.setStatus("current")
_CrossConnectionsProvisioningDefaultsCrsType_Type = FspR7TypeCrs
_CrossConnectionsProvisioningDefaultsCrsType_Object = MibTableColumn
crossConnectionsProvisioningDefaultsCrsType = _CrossConnectionsProvisioningDefaultsCrsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13, 1, 8),
    _CrossConnectionsProvisioningDefaultsCrsType_Type()
)
crossConnectionsProvisioningDefaultsCrsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsCrsType.setStatus("current")
_CrossConnectionsProvisioningDefaultsConn_Type = FspR7Conn
_CrossConnectionsProvisioningDefaultsConn_Object = MibTableColumn
crossConnectionsProvisioningDefaultsConn = _CrossConnectionsProvisioningDefaultsConn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 13, 1, 9),
    _CrossConnectionsProvisioningDefaultsConn_Type()
)
crossConnectionsProvisioningDefaultsConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsProvisioningDefaultsConn.setStatus("current")
_CrossConnectionsConfigTable_Object = MibTable
crossConnectionsConfigTable = _CrossConnectionsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 14)
)
if mibBuilder.loadTexts:
    crossConnectionsConfigTable.setStatus("current")
_CrossConnectionsConfigEntry_Object = MibTableRow
crossConnectionsConfigEntry = _CrossConnectionsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 14, 1)
)
crossConnectionsConfigEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthTo"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowFrom"),
)
if mibBuilder.loadTexts:
    crossConnectionsConfigEntry.setStatus("current")
_CrossConnectionsConfigAlias_Type = SnmpAdminString
_CrossConnectionsConfigAlias_Object = MibTableColumn
crossConnectionsConfigAlias = _CrossConnectionsConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 14, 1, 1),
    _CrossConnectionsConfigAlias_Type()
)
crossConnectionsConfigAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crossConnectionsConfigAlias.setStatus("current")
_CrossConnectionsStatusTable_Object = MibTable
crossConnectionsStatusTable = _CrossConnectionsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 16)
)
if mibBuilder.loadTexts:
    crossConnectionsStatusTable.setStatus("current")
_CrossConnectionsStatusEntry_Object = MibTableRow
crossConnectionsStatusEntry = _CrossConnectionsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 16, 1)
)
crossConnectionsStatusEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthTo"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowTo"),
)
if mibBuilder.loadTexts:
    crossConnectionsStatusEntry.setStatus("current")
_CrossConnectionsStatusFromEth_Type = EntityIndex
_CrossConnectionsStatusFromEth_Object = MibTableColumn
crossConnectionsStatusFromEth = _CrossConnectionsStatusFromEth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 16, 1, 1),
    _CrossConnectionsStatusFromEth_Type()
)
crossConnectionsStatusFromEth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsStatusFromEth.setStatus("current")
_CrossConnectionsStatusToEth_Type = EntityIndex
_CrossConnectionsStatusToEth_Object = MibTableColumn
crossConnectionsStatusToEth = _CrossConnectionsStatusToEth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 16, 1, 2),
    _CrossConnectionsStatusToEth_Type()
)
crossConnectionsStatusToEth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsStatusToEth.setStatus("current")
_CrossConnectionsStatusType_Type = FspR7InterfaceType
_CrossConnectionsStatusType_Object = MibTableColumn
crossConnectionsStatusType = _CrossConnectionsStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 16, 1, 3),
    _CrossConnectionsStatusType_Type()
)
crossConnectionsStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsStatusType.setStatus("current")
_CrossConnectionsStatusCrsFunction_Type = FspR7FunctionCrs
_CrossConnectionsStatusCrsFunction_Object = MibTableColumn
crossConnectionsStatusCrsFunction = _CrossConnectionsStatusCrsFunction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 16, 1, 4),
    _CrossConnectionsStatusCrsFunction_Type()
)
crossConnectionsStatusCrsFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsStatusCrsFunction.setStatus("current")
_CrossConnectionsStatusCrsType_Type = FspR7TypeCrs
_CrossConnectionsStatusCrsType_Object = MibTableColumn
crossConnectionsStatusCrsType = _CrossConnectionsStatusCrsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 16, 1, 5),
    _CrossConnectionsStatusCrsType_Type()
)
crossConnectionsStatusCrsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsStatusCrsType.setStatus("current")
_CrossConnectionsStatusConn_Type = FspR7Conn
_CrossConnectionsStatusConn_Object = MibTableColumn
crossConnectionsStatusConn = _CrossConnectionsStatusConn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 16, 1, 6),
    _CrossConnectionsStatusConn_Type()
)
crossConnectionsStatusConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsStatusConn.setStatus("current")
_CrossConnectionsPointsFromTable_Object = MibTable
crossConnectionsPointsFromTable = _CrossConnectionsPointsFromTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 17)
)
if mibBuilder.loadTexts:
    crossConnectionsPointsFromTable.setStatus("current")
_CrossConnectionsPointsFromEntry_Object = MibTableRow
crossConnectionsPointsFromEntry = _CrossConnectionsPointsFromEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 17, 1)
)
crossConnectionsPointsFromEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowFrom"),
)
if mibBuilder.loadTexts:
    crossConnectionsPointsFromEntry.setStatus("current")
_CrossConnectionsPointsFromFlow_Type = EntityIndex
_CrossConnectionsPointsFromFlow_Object = MibTableColumn
crossConnectionsPointsFromFlow = _CrossConnectionsPointsFromFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 17, 1, 1),
    _CrossConnectionsPointsFromFlow_Type()
)
crossConnectionsPointsFromFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsPointsFromFlow.setStatus("current")
_CrossConnectionsPointsToTable_Object = MibTable
crossConnectionsPointsToTable = _CrossConnectionsPointsToTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 18)
)
if mibBuilder.loadTexts:
    crossConnectionsPointsToTable.setStatus("current")
_CrossConnectionsPointsToEntry_Object = MibTableRow
crossConnectionsPointsToEntry = _CrossConnectionsPointsToEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 18, 1)
)
crossConnectionsPointsToEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowFrom"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexEthTo"),
    (0, "FspR7-LAYER2-MIB", "crossConnectionsProvisioningIndexFlowTo"),
)
if mibBuilder.loadTexts:
    crossConnectionsPointsToEntry.setStatus("current")
_CrossConnectionsPointsToFlow_Type = EntityIndex
_CrossConnectionsPointsToFlow_Object = MibTableColumn
crossConnectionsPointsToFlow = _CrossConnectionsPointsToFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 15, 18, 1, 1),
    _CrossConnectionsPointsToFlow_Type()
)
crossConnectionsPointsToFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crossConnectionsPointsToFlow.setStatus("current")
_Layer2PerformanceMonitoring_ObjectIdentity = ObjectIdentity
layer2PerformanceMonitoring = _Layer2PerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16)
)
_FlowPerformanceMonitoring_ObjectIdentity = ObjectIdentity
flowPerformanceMonitoring = _FlowPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1)
)
_CurrentFlowEntityRx15minTable_Object = MibTable
currentFlowEntityRx15minTable = _CurrentFlowEntityRx15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 1)
)
if mibBuilder.loadTexts:
    currentFlowEntityRx15minTable.setStatus("current")
_CurrentFlowEntityRx15minEntry_Object = MibTableRow
currentFlowEntityRx15minEntry = _CurrentFlowEntityRx15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 1, 1)
)
currentFlowEntityRx15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    currentFlowEntityRx15minEntry.setStatus("current")
_CurrentFlowEntityRx15minUnicastFramesPerEvcRcv_Type = Counter64String
_CurrentFlowEntityRx15minUnicastFramesPerEvcRcv_Object = MibTableColumn
currentFlowEntityRx15minUnicastFramesPerEvcRcv = _CurrentFlowEntityRx15minUnicastFramesPerEvcRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 1, 1, 1),
    _CurrentFlowEntityRx15minUnicastFramesPerEvcRcv_Type()
)
currentFlowEntityRx15minUnicastFramesPerEvcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityRx15minUnicastFramesPerEvcRcv.setStatus("current")
_CurrentFlowEntityRx15minMcBcFramesPerEvcRcv_Type = Counter64String
_CurrentFlowEntityRx15minMcBcFramesPerEvcRcv_Object = MibTableColumn
currentFlowEntityRx15minMcBcFramesPerEvcRcv = _CurrentFlowEntityRx15minMcBcFramesPerEvcRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 1, 1, 2),
    _CurrentFlowEntityRx15minMcBcFramesPerEvcRcv_Type()
)
currentFlowEntityRx15minMcBcFramesPerEvcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityRx15minMcBcFramesPerEvcRcv.setStatus("current")


class _CurrentFlowEntityRx15minElapsedTime_Type(Integer32):
    """Custom type currentFlowEntityRx15minElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentFlowEntityRx15minElapsedTime_Type.__name__ = "Integer32"
_CurrentFlowEntityRx15minElapsedTime_Object = MibTableColumn
currentFlowEntityRx15minElapsedTime = _CurrentFlowEntityRx15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 1, 1, 3),
    _CurrentFlowEntityRx15minElapsedTime_Type()
)
currentFlowEntityRx15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityRx15minElapsedTime.setStatus("current")
_CurrentFlowEntityRx1dayTable_Object = MibTable
currentFlowEntityRx1dayTable = _CurrentFlowEntityRx1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 2)
)
if mibBuilder.loadTexts:
    currentFlowEntityRx1dayTable.setStatus("current")
_CurrentFlowEntityRx1dayEntry_Object = MibTableRow
currentFlowEntityRx1dayEntry = _CurrentFlowEntityRx1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 2, 1)
)
currentFlowEntityRx1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    currentFlowEntityRx1dayEntry.setStatus("current")
_CurrentFlowEntityRx1dayUnicastFramesPerEvcRcv_Type = Counter64String
_CurrentFlowEntityRx1dayUnicastFramesPerEvcRcv_Object = MibTableColumn
currentFlowEntityRx1dayUnicastFramesPerEvcRcv = _CurrentFlowEntityRx1dayUnicastFramesPerEvcRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 2, 1, 1),
    _CurrentFlowEntityRx1dayUnicastFramesPerEvcRcv_Type()
)
currentFlowEntityRx1dayUnicastFramesPerEvcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityRx1dayUnicastFramesPerEvcRcv.setStatus("current")
_CurrentFlowEntityRx1dayMcBcFramesPerEvcRcv_Type = Counter64String
_CurrentFlowEntityRx1dayMcBcFramesPerEvcRcv_Object = MibTableColumn
currentFlowEntityRx1dayMcBcFramesPerEvcRcv = _CurrentFlowEntityRx1dayMcBcFramesPerEvcRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 2, 1, 2),
    _CurrentFlowEntityRx1dayMcBcFramesPerEvcRcv_Type()
)
currentFlowEntityRx1dayMcBcFramesPerEvcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityRx1dayMcBcFramesPerEvcRcv.setStatus("current")


class _CurrentFlowEntityRx1dayElapsedTime_Type(Integer32):
    """Custom type currentFlowEntityRx1dayElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentFlowEntityRx1dayElapsedTime_Type.__name__ = "Integer32"
_CurrentFlowEntityRx1dayElapsedTime_Object = MibTableColumn
currentFlowEntityRx1dayElapsedTime = _CurrentFlowEntityRx1dayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 2, 1, 3),
    _CurrentFlowEntityRx1dayElapsedTime_Type()
)
currentFlowEntityRx1dayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityRx1dayElapsedTime.setStatus("current")
_IntervalFlowEntityRx15minTable_Object = MibTable
intervalFlowEntityRx15minTable = _IntervalFlowEntityRx15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 3)
)
if mibBuilder.loadTexts:
    intervalFlowEntityRx15minTable.setStatus("current")
_IntervalFlowEntityRx15minEntry_Object = MibTableRow
intervalFlowEntityRx15minEntry = _IntervalFlowEntityRx15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 3, 1)
)
intervalFlowEntityRx15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "intervalFlowEntityRx15minNumber"),
)
if mibBuilder.loadTexts:
    intervalFlowEntityRx15minEntry.setStatus("current")


class _IntervalFlowEntityRx15minNumber_Type(Integer32):
    """Custom type intervalFlowEntityRx15minNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IntervalFlowEntityRx15minNumber_Type.__name__ = "Integer32"
_IntervalFlowEntityRx15minNumber_Object = MibTableColumn
intervalFlowEntityRx15minNumber = _IntervalFlowEntityRx15minNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 3, 1, 1),
    _IntervalFlowEntityRx15minNumber_Type()
)
intervalFlowEntityRx15minNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalFlowEntityRx15minNumber.setStatus("current")
_IntervalFlowEntityRx15minUnicastFramesPerEvcRcv_Type = Counter64String
_IntervalFlowEntityRx15minUnicastFramesPerEvcRcv_Object = MibTableColumn
intervalFlowEntityRx15minUnicastFramesPerEvcRcv = _IntervalFlowEntityRx15minUnicastFramesPerEvcRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 3, 1, 2),
    _IntervalFlowEntityRx15minUnicastFramesPerEvcRcv_Type()
)
intervalFlowEntityRx15minUnicastFramesPerEvcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityRx15minUnicastFramesPerEvcRcv.setStatus("current")
_IntervalFlowEntityRx15minMcBcFramesPerEvcRcv_Type = Counter64String
_IntervalFlowEntityRx15minMcBcFramesPerEvcRcv_Object = MibTableColumn
intervalFlowEntityRx15minMcBcFramesPerEvcRcv = _IntervalFlowEntityRx15minMcBcFramesPerEvcRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 3, 1, 3),
    _IntervalFlowEntityRx15minMcBcFramesPerEvcRcv_Type()
)
intervalFlowEntityRx15minMcBcFramesPerEvcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityRx15minMcBcFramesPerEvcRcv.setStatus("current")
_IntervalFlowEntityRx15minValidFlag_Type = TruthValue
_IntervalFlowEntityRx15minValidFlag_Object = MibTableColumn
intervalFlowEntityRx15minValidFlag = _IntervalFlowEntityRx15minValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 3, 1, 4),
    _IntervalFlowEntityRx15minValidFlag_Type()
)
intervalFlowEntityRx15minValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityRx15minValidFlag.setStatus("current")
_IntervalFlowEntityRx15minTimeStamp_Type = DateAndTime
_IntervalFlowEntityRx15minTimeStamp_Object = MibTableColumn
intervalFlowEntityRx15minTimeStamp = _IntervalFlowEntityRx15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 3, 1, 5),
    _IntervalFlowEntityRx15minTimeStamp_Type()
)
intervalFlowEntityRx15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityRx15minTimeStamp.setStatus("current")
_IntervalFlowEntityRx1dayTable_Object = MibTable
intervalFlowEntityRx1dayTable = _IntervalFlowEntityRx1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 4)
)
if mibBuilder.loadTexts:
    intervalFlowEntityRx1dayTable.setStatus("current")
_IntervalFlowEntityRx1dayEntry_Object = MibTableRow
intervalFlowEntityRx1dayEntry = _IntervalFlowEntityRx1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 4, 1)
)
intervalFlowEntityRx1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "intervalFlowEntityRx1dayNumber"),
)
if mibBuilder.loadTexts:
    intervalFlowEntityRx1dayEntry.setStatus("current")


class _IntervalFlowEntityRx1dayNumber_Type(Integer32):
    """Custom type intervalFlowEntityRx1dayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IntervalFlowEntityRx1dayNumber_Type.__name__ = "Integer32"
_IntervalFlowEntityRx1dayNumber_Object = MibTableColumn
intervalFlowEntityRx1dayNumber = _IntervalFlowEntityRx1dayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 4, 1, 1),
    _IntervalFlowEntityRx1dayNumber_Type()
)
intervalFlowEntityRx1dayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalFlowEntityRx1dayNumber.setStatus("current")
_IntervalFlowEntityRx1dayUnicastFramesPerEvcRcv_Type = Counter64String
_IntervalFlowEntityRx1dayUnicastFramesPerEvcRcv_Object = MibTableColumn
intervalFlowEntityRx1dayUnicastFramesPerEvcRcv = _IntervalFlowEntityRx1dayUnicastFramesPerEvcRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 4, 1, 2),
    _IntervalFlowEntityRx1dayUnicastFramesPerEvcRcv_Type()
)
intervalFlowEntityRx1dayUnicastFramesPerEvcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityRx1dayUnicastFramesPerEvcRcv.setStatus("current")
_IntervalFlowEntityRx1dayMcBcFramesPerEvcRcv_Type = Counter64String
_IntervalFlowEntityRx1dayMcBcFramesPerEvcRcv_Object = MibTableColumn
intervalFlowEntityRx1dayMcBcFramesPerEvcRcv = _IntervalFlowEntityRx1dayMcBcFramesPerEvcRcv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 4, 1, 3),
    _IntervalFlowEntityRx1dayMcBcFramesPerEvcRcv_Type()
)
intervalFlowEntityRx1dayMcBcFramesPerEvcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityRx1dayMcBcFramesPerEvcRcv.setStatus("current")
_IntervalFlowEntityRx1dayValidFlag_Type = TruthValue
_IntervalFlowEntityRx1dayValidFlag_Object = MibTableColumn
intervalFlowEntityRx1dayValidFlag = _IntervalFlowEntityRx1dayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 4, 1, 4),
    _IntervalFlowEntityRx1dayValidFlag_Type()
)
intervalFlowEntityRx1dayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityRx1dayValidFlag.setStatus("current")
_IntervalFlowEntityRx1dayTimeStamp_Type = DateAndTime
_IntervalFlowEntityRx1dayTimeStamp_Object = MibTableColumn
intervalFlowEntityRx1dayTimeStamp = _IntervalFlowEntityRx1dayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 4, 1, 5),
    _IntervalFlowEntityRx1dayTimeStamp_Type()
)
intervalFlowEntityRx1dayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityRx1dayTimeStamp.setStatus("current")
_CurrentFlowEntityTx15minTable_Object = MibTable
currentFlowEntityTx15minTable = _CurrentFlowEntityTx15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 5)
)
if mibBuilder.loadTexts:
    currentFlowEntityTx15minTable.setStatus("current")
_CurrentFlowEntityTx15minEntry_Object = MibTableRow
currentFlowEntityTx15minEntry = _CurrentFlowEntityTx15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 5, 1)
)
currentFlowEntityTx15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    currentFlowEntityTx15minEntry.setStatus("current")
_CurrentFlowEntityTx15minUnicastFramesPerEvcTrmt_Type = Counter64String
_CurrentFlowEntityTx15minUnicastFramesPerEvcTrmt_Object = MibTableColumn
currentFlowEntityTx15minUnicastFramesPerEvcTrmt = _CurrentFlowEntityTx15minUnicastFramesPerEvcTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 5, 1, 1),
    _CurrentFlowEntityTx15minUnicastFramesPerEvcTrmt_Type()
)
currentFlowEntityTx15minUnicastFramesPerEvcTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityTx15minUnicastFramesPerEvcTrmt.setStatus("current")
_CurrentFlowEntityTx15minMcBcFramesPerEvcTrmt_Type = Counter64String
_CurrentFlowEntityTx15minMcBcFramesPerEvcTrmt_Object = MibTableColumn
currentFlowEntityTx15minMcBcFramesPerEvcTrmt = _CurrentFlowEntityTx15minMcBcFramesPerEvcTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 5, 1, 2),
    _CurrentFlowEntityTx15minMcBcFramesPerEvcTrmt_Type()
)
currentFlowEntityTx15minMcBcFramesPerEvcTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityTx15minMcBcFramesPerEvcTrmt.setStatus("current")


class _CurrentFlowEntityTx15minElapsedTime_Type(Integer32):
    """Custom type currentFlowEntityTx15minElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentFlowEntityTx15minElapsedTime_Type.__name__ = "Integer32"
_CurrentFlowEntityTx15minElapsedTime_Object = MibTableColumn
currentFlowEntityTx15minElapsedTime = _CurrentFlowEntityTx15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 5, 1, 3),
    _CurrentFlowEntityTx15minElapsedTime_Type()
)
currentFlowEntityTx15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityTx15minElapsedTime.setStatus("current")
_CurrentFlowEntityTx1dayTable_Object = MibTable
currentFlowEntityTx1dayTable = _CurrentFlowEntityTx1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 6)
)
if mibBuilder.loadTexts:
    currentFlowEntityTx1dayTable.setStatus("current")
_CurrentFlowEntityTx1dayEntry_Object = MibTableRow
currentFlowEntityTx1dayEntry = _CurrentFlowEntityTx1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 6, 1)
)
currentFlowEntityTx1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    currentFlowEntityTx1dayEntry.setStatus("current")
_CurrentFlowEntityTx1dayUnicastFramesPerEvcTrmt_Type = Counter64String
_CurrentFlowEntityTx1dayUnicastFramesPerEvcTrmt_Object = MibTableColumn
currentFlowEntityTx1dayUnicastFramesPerEvcTrmt = _CurrentFlowEntityTx1dayUnicastFramesPerEvcTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 6, 1, 1),
    _CurrentFlowEntityTx1dayUnicastFramesPerEvcTrmt_Type()
)
currentFlowEntityTx1dayUnicastFramesPerEvcTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityTx1dayUnicastFramesPerEvcTrmt.setStatus("current")
_CurrentFlowEntityTx1dayMcBcFramesPerEvcTrmt_Type = Counter64String
_CurrentFlowEntityTx1dayMcBcFramesPerEvcTrmt_Object = MibTableColumn
currentFlowEntityTx1dayMcBcFramesPerEvcTrmt = _CurrentFlowEntityTx1dayMcBcFramesPerEvcTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 6, 1, 2),
    _CurrentFlowEntityTx1dayMcBcFramesPerEvcTrmt_Type()
)
currentFlowEntityTx1dayMcBcFramesPerEvcTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityTx1dayMcBcFramesPerEvcTrmt.setStatus("current")


class _CurrentFlowEntityTx1dayElapsedTime_Type(Integer32):
    """Custom type currentFlowEntityTx1dayElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentFlowEntityTx1dayElapsedTime_Type.__name__ = "Integer32"
_CurrentFlowEntityTx1dayElapsedTime_Object = MibTableColumn
currentFlowEntityTx1dayElapsedTime = _CurrentFlowEntityTx1dayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 6, 1, 3),
    _CurrentFlowEntityTx1dayElapsedTime_Type()
)
currentFlowEntityTx1dayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentFlowEntityTx1dayElapsedTime.setStatus("current")
_IntervalFlowEntityTx15minTable_Object = MibTable
intervalFlowEntityTx15minTable = _IntervalFlowEntityTx15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 7)
)
if mibBuilder.loadTexts:
    intervalFlowEntityTx15minTable.setStatus("current")
_IntervalFlowEntityTx15minEntry_Object = MibTableRow
intervalFlowEntityTx15minEntry = _IntervalFlowEntityTx15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 7, 1)
)
intervalFlowEntityTx15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "intervalFlowEntityTx15minNumber"),
)
if mibBuilder.loadTexts:
    intervalFlowEntityTx15minEntry.setStatus("current")


class _IntervalFlowEntityTx15minNumber_Type(Integer32):
    """Custom type intervalFlowEntityTx15minNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IntervalFlowEntityTx15minNumber_Type.__name__ = "Integer32"
_IntervalFlowEntityTx15minNumber_Object = MibTableColumn
intervalFlowEntityTx15minNumber = _IntervalFlowEntityTx15minNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 7, 1, 1),
    _IntervalFlowEntityTx15minNumber_Type()
)
intervalFlowEntityTx15minNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalFlowEntityTx15minNumber.setStatus("current")
_IntervalFlowEntityTx15minUnicastFramesPerEvcTrmt_Type = Counter64String
_IntervalFlowEntityTx15minUnicastFramesPerEvcTrmt_Object = MibTableColumn
intervalFlowEntityTx15minUnicastFramesPerEvcTrmt = _IntervalFlowEntityTx15minUnicastFramesPerEvcTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 7, 1, 2),
    _IntervalFlowEntityTx15minUnicastFramesPerEvcTrmt_Type()
)
intervalFlowEntityTx15minUnicastFramesPerEvcTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityTx15minUnicastFramesPerEvcTrmt.setStatus("current")
_IntervalFlowEntityTx15minMcBcFramesPerEvcTrmt_Type = Counter64String
_IntervalFlowEntityTx15minMcBcFramesPerEvcTrmt_Object = MibTableColumn
intervalFlowEntityTx15minMcBcFramesPerEvcTrmt = _IntervalFlowEntityTx15minMcBcFramesPerEvcTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 7, 1, 3),
    _IntervalFlowEntityTx15minMcBcFramesPerEvcTrmt_Type()
)
intervalFlowEntityTx15minMcBcFramesPerEvcTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityTx15minMcBcFramesPerEvcTrmt.setStatus("current")
_IntervalFlowEntityTx15minValidFlag_Type = TruthValue
_IntervalFlowEntityTx15minValidFlag_Object = MibTableColumn
intervalFlowEntityTx15minValidFlag = _IntervalFlowEntityTx15minValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 7, 1, 4),
    _IntervalFlowEntityTx15minValidFlag_Type()
)
intervalFlowEntityTx15minValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityTx15minValidFlag.setStatus("current")
_IntervalFlowEntityTx15minTimeStamp_Type = DateAndTime
_IntervalFlowEntityTx15minTimeStamp_Object = MibTableColumn
intervalFlowEntityTx15minTimeStamp = _IntervalFlowEntityTx15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 7, 1, 5),
    _IntervalFlowEntityTx15minTimeStamp_Type()
)
intervalFlowEntityTx15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityTx15minTimeStamp.setStatus("current")
_IntervalFlowEntityTx1dayTable_Object = MibTable
intervalFlowEntityTx1dayTable = _IntervalFlowEntityTx1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 8)
)
if mibBuilder.loadTexts:
    intervalFlowEntityTx1dayTable.setStatus("current")
_IntervalFlowEntityTx1dayEntry_Object = MibTableRow
intervalFlowEntityTx1dayEntry = _IntervalFlowEntityTx1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 8, 1)
)
intervalFlowEntityTx1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "intervalFlowEntityTx15minNumber"),
)
if mibBuilder.loadTexts:
    intervalFlowEntityTx1dayEntry.setStatus("current")


class _IntervalFlowEntityTx1dayNumber_Type(Integer32):
    """Custom type intervalFlowEntityTx1dayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IntervalFlowEntityTx1dayNumber_Type.__name__ = "Integer32"
_IntervalFlowEntityTx1dayNumber_Object = MibTableColumn
intervalFlowEntityTx1dayNumber = _IntervalFlowEntityTx1dayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 8, 1, 1),
    _IntervalFlowEntityTx1dayNumber_Type()
)
intervalFlowEntityTx1dayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalFlowEntityTx1dayNumber.setStatus("current")
_IntervalFlowEntityTx1dayUnicastFramesPerEvcTrmt_Type = Counter64String
_IntervalFlowEntityTx1dayUnicastFramesPerEvcTrmt_Object = MibTableColumn
intervalFlowEntityTx1dayUnicastFramesPerEvcTrmt = _IntervalFlowEntityTx1dayUnicastFramesPerEvcTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 8, 1, 2),
    _IntervalFlowEntityTx1dayUnicastFramesPerEvcTrmt_Type()
)
intervalFlowEntityTx1dayUnicastFramesPerEvcTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityTx1dayUnicastFramesPerEvcTrmt.setStatus("current")
_IntervalFlowEntityTx1dayMcBcFramesPerEvcTrmt_Type = Counter64String
_IntervalFlowEntityTx1dayMcBcFramesPerEvcTrmt_Object = MibTableColumn
intervalFlowEntityTx1dayMcBcFramesPerEvcTrmt = _IntervalFlowEntityTx1dayMcBcFramesPerEvcTrmt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 8, 1, 3),
    _IntervalFlowEntityTx1dayMcBcFramesPerEvcTrmt_Type()
)
intervalFlowEntityTx1dayMcBcFramesPerEvcTrmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityTx1dayMcBcFramesPerEvcTrmt.setStatus("current")
_IntervalFlowEntityTx1dayValidFlag_Type = TruthValue
_IntervalFlowEntityTx1dayValidFlag_Object = MibTableColumn
intervalFlowEntityTx1dayValidFlag = _IntervalFlowEntityTx1dayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 8, 1, 4),
    _IntervalFlowEntityTx1dayValidFlag_Type()
)
intervalFlowEntityTx1dayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityTx1dayValidFlag.setStatus("current")
_IntervalFlowEntityTx1dayTimeStamp_Type = DateAndTime
_IntervalFlowEntityTx1dayTimeStamp_Object = MibTableColumn
intervalFlowEntityTx1dayTimeStamp = _IntervalFlowEntityTx1dayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 1, 8, 1, 5),
    _IntervalFlowEntityTx1dayTimeStamp_Type()
)
intervalFlowEntityTx1dayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalFlowEntityTx1dayTimeStamp.setStatus("current")
_PolicerPerformanceMonitoring_ObjectIdentity = ObjectIdentity
policerPerformanceMonitoring = _PolicerPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2)
)
_CurrentpolicerOnFlowEntity15minTable_Object = MibTable
currentpolicerOnFlowEntity15minTable = _CurrentpolicerOnFlowEntity15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 5)
)
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity15minTable.setStatus("current")
_CurrentpolicerOnFlowEntity15minEntry_Object = MibTableRow
currentpolicerOnFlowEntity15minEntry = _CurrentpolicerOnFlowEntity15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 5, 1)
)
currentpolicerOnFlowEntity15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexPolicer"),
)
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity15minEntry.setStatus("current")
_CurrentpolicerOnFlowEntity15minBytesMarkedGreen_Type = Counter64String
_CurrentpolicerOnFlowEntity15minBytesMarkedGreen_Object = MibTableColumn
currentpolicerOnFlowEntity15minBytesMarkedGreen = _CurrentpolicerOnFlowEntity15minBytesMarkedGreen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 5, 1, 1),
    _CurrentpolicerOnFlowEntity15minBytesMarkedGreen_Type()
)
currentpolicerOnFlowEntity15minBytesMarkedGreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity15minBytesMarkedGreen.setStatus("current")
_CurrentpolicerOnFlowEntity15minFramesMarkedGreen_Type = Counter64String
_CurrentpolicerOnFlowEntity15minFramesMarkedGreen_Object = MibTableColumn
currentpolicerOnFlowEntity15minFramesMarkedGreen = _CurrentpolicerOnFlowEntity15minFramesMarkedGreen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 5, 1, 2),
    _CurrentpolicerOnFlowEntity15minFramesMarkedGreen_Type()
)
currentpolicerOnFlowEntity15minFramesMarkedGreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity15minFramesMarkedGreen.setStatus("current")
_CurrentpolicerOnFlowEntity15minBytesMarkedRed_Type = Counter64String
_CurrentpolicerOnFlowEntity15minBytesMarkedRed_Object = MibTableColumn
currentpolicerOnFlowEntity15minBytesMarkedRed = _CurrentpolicerOnFlowEntity15minBytesMarkedRed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 5, 1, 3),
    _CurrentpolicerOnFlowEntity15minBytesMarkedRed_Type()
)
currentpolicerOnFlowEntity15minBytesMarkedRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity15minBytesMarkedRed.setStatus("current")
_CurrentpolicerOnFlowEntity15minFramesMarkedRed_Type = Counter64String
_CurrentpolicerOnFlowEntity15minFramesMarkedRed_Object = MibTableColumn
currentpolicerOnFlowEntity15minFramesMarkedRed = _CurrentpolicerOnFlowEntity15minFramesMarkedRed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 5, 1, 4),
    _CurrentpolicerOnFlowEntity15minFramesMarkedRed_Type()
)
currentpolicerOnFlowEntity15minFramesMarkedRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity15minFramesMarkedRed.setStatus("current")


class _CurrentpolicerOnFlowEntity15minElapsedTime_Type(Integer32):
    """Custom type currentpolicerOnFlowEntity15minElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentpolicerOnFlowEntity15minElapsedTime_Type.__name__ = "Integer32"
_CurrentpolicerOnFlowEntity15minElapsedTime_Object = MibTableColumn
currentpolicerOnFlowEntity15minElapsedTime = _CurrentpolicerOnFlowEntity15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 5, 1, 5),
    _CurrentpolicerOnFlowEntity15minElapsedTime_Type()
)
currentpolicerOnFlowEntity15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity15minElapsedTime.setStatus("current")
_CurrentpolicerOnFlowEntity1dayTable_Object = MibTable
currentpolicerOnFlowEntity1dayTable = _CurrentpolicerOnFlowEntity1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 6)
)
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity1dayTable.setStatus("current")
_CurrentpolicerOnFlowEntity1dayEntry_Object = MibTableRow
currentpolicerOnFlowEntity1dayEntry = _CurrentpolicerOnFlowEntity1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 6, 1)
)
currentpolicerOnFlowEntity1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexPolicer"),
)
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity1dayEntry.setStatus("current")
_CurrentpolicerOnFlowEntity1dayBytesMarkedGreen_Type = Counter64String
_CurrentpolicerOnFlowEntity1dayBytesMarkedGreen_Object = MibTableColumn
currentpolicerOnFlowEntity1dayBytesMarkedGreen = _CurrentpolicerOnFlowEntity1dayBytesMarkedGreen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 6, 1, 1),
    _CurrentpolicerOnFlowEntity1dayBytesMarkedGreen_Type()
)
currentpolicerOnFlowEntity1dayBytesMarkedGreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity1dayBytesMarkedGreen.setStatus("current")
_CurrentpolicerOnFlowEntity1dayFramesMarkedGreen_Type = Counter64String
_CurrentpolicerOnFlowEntity1dayFramesMarkedGreen_Object = MibTableColumn
currentpolicerOnFlowEntity1dayFramesMarkedGreen = _CurrentpolicerOnFlowEntity1dayFramesMarkedGreen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 6, 1, 2),
    _CurrentpolicerOnFlowEntity1dayFramesMarkedGreen_Type()
)
currentpolicerOnFlowEntity1dayFramesMarkedGreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity1dayFramesMarkedGreen.setStatus("current")
_CurrentpolicerOnFlowEntity1dayBytesMarkedRed_Type = Counter64String
_CurrentpolicerOnFlowEntity1dayBytesMarkedRed_Object = MibTableColumn
currentpolicerOnFlowEntity1dayBytesMarkedRed = _CurrentpolicerOnFlowEntity1dayBytesMarkedRed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 6, 1, 3),
    _CurrentpolicerOnFlowEntity1dayBytesMarkedRed_Type()
)
currentpolicerOnFlowEntity1dayBytesMarkedRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity1dayBytesMarkedRed.setStatus("current")
_CurrentpolicerOnFlowEntity1dayFramesMarkedRed_Type = Counter64String
_CurrentpolicerOnFlowEntity1dayFramesMarkedRed_Object = MibTableColumn
currentpolicerOnFlowEntity1dayFramesMarkedRed = _CurrentpolicerOnFlowEntity1dayFramesMarkedRed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 6, 1, 4),
    _CurrentpolicerOnFlowEntity1dayFramesMarkedRed_Type()
)
currentpolicerOnFlowEntity1dayFramesMarkedRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity1dayFramesMarkedRed.setStatus("current")


class _CurrentpolicerOnFlowEntity1dayElapsedTime_Type(Integer32):
    """Custom type currentpolicerOnFlowEntity1dayElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentpolicerOnFlowEntity1dayElapsedTime_Type.__name__ = "Integer32"
_CurrentpolicerOnFlowEntity1dayElapsedTime_Object = MibTableColumn
currentpolicerOnFlowEntity1dayElapsedTime = _CurrentpolicerOnFlowEntity1dayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 6, 1, 5),
    _CurrentpolicerOnFlowEntity1dayElapsedTime_Type()
)
currentpolicerOnFlowEntity1dayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentpolicerOnFlowEntity1dayElapsedTime.setStatus("current")
_IntervalpolicerOnFlowEntity15minTable_Object = MibTable
intervalpolicerOnFlowEntity15minTable = _IntervalpolicerOnFlowEntity15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 7)
)
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity15minTable.setStatus("current")
_IntervalpolicerOnFlowEntity15minEntry_Object = MibTableRow
intervalpolicerOnFlowEntity15minEntry = _IntervalpolicerOnFlowEntity15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 7, 1)
)
intervalpolicerOnFlowEntity15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexPolicer"),
    (0, "FspR7-LAYER2-MIB", "intervalpolicerOnFlowEntity15minNumber"),
)
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity15minEntry.setStatus("current")


class _IntervalpolicerOnFlowEntity15minNumber_Type(Integer32):
    """Custom type intervalpolicerOnFlowEntity15minNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IntervalpolicerOnFlowEntity15minNumber_Type.__name__ = "Integer32"
_IntervalpolicerOnFlowEntity15minNumber_Object = MibTableColumn
intervalpolicerOnFlowEntity15minNumber = _IntervalpolicerOnFlowEntity15minNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 7, 1, 1),
    _IntervalpolicerOnFlowEntity15minNumber_Type()
)
intervalpolicerOnFlowEntity15minNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity15minNumber.setStatus("current")
_IntervalpolicerOnFlowEntity15minBytesMarkedGreen_Type = Counter64String
_IntervalpolicerOnFlowEntity15minBytesMarkedGreen_Object = MibTableColumn
intervalpolicerOnFlowEntity15minBytesMarkedGreen = _IntervalpolicerOnFlowEntity15minBytesMarkedGreen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 7, 1, 2),
    _IntervalpolicerOnFlowEntity15minBytesMarkedGreen_Type()
)
intervalpolicerOnFlowEntity15minBytesMarkedGreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity15minBytesMarkedGreen.setStatus("current")
_IntervalpolicerOnFlowEntity15minFramesMarkedGreen_Type = Counter64String
_IntervalpolicerOnFlowEntity15minFramesMarkedGreen_Object = MibTableColumn
intervalpolicerOnFlowEntity15minFramesMarkedGreen = _IntervalpolicerOnFlowEntity15minFramesMarkedGreen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 7, 1, 3),
    _IntervalpolicerOnFlowEntity15minFramesMarkedGreen_Type()
)
intervalpolicerOnFlowEntity15minFramesMarkedGreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity15minFramesMarkedGreen.setStatus("current")
_IntervalpolicerOnFlowEntity15minBytesMarkedRed_Type = Counter64String
_IntervalpolicerOnFlowEntity15minBytesMarkedRed_Object = MibTableColumn
intervalpolicerOnFlowEntity15minBytesMarkedRed = _IntervalpolicerOnFlowEntity15minBytesMarkedRed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 7, 1, 4),
    _IntervalpolicerOnFlowEntity15minBytesMarkedRed_Type()
)
intervalpolicerOnFlowEntity15minBytesMarkedRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity15minBytesMarkedRed.setStatus("current")
_IntervalpolicerOnFlowEntity15minFramesMarkedRed_Type = Counter64String
_IntervalpolicerOnFlowEntity15minFramesMarkedRed_Object = MibTableColumn
intervalpolicerOnFlowEntity15minFramesMarkedRed = _IntervalpolicerOnFlowEntity15minFramesMarkedRed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 7, 1, 5),
    _IntervalpolicerOnFlowEntity15minFramesMarkedRed_Type()
)
intervalpolicerOnFlowEntity15minFramesMarkedRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity15minFramesMarkedRed.setStatus("current")
_IntervalpolicerOnFlowEntity15minValidFlag_Type = TruthValue
_IntervalpolicerOnFlowEntity15minValidFlag_Object = MibTableColumn
intervalpolicerOnFlowEntity15minValidFlag = _IntervalpolicerOnFlowEntity15minValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 7, 1, 6),
    _IntervalpolicerOnFlowEntity15minValidFlag_Type()
)
intervalpolicerOnFlowEntity15minValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity15minValidFlag.setStatus("current")
_IntervalpolicerOnFlowEntity15minTimeStamp_Type = DateAndTime
_IntervalpolicerOnFlowEntity15minTimeStamp_Object = MibTableColumn
intervalpolicerOnFlowEntity15minTimeStamp = _IntervalpolicerOnFlowEntity15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 7, 1, 7),
    _IntervalpolicerOnFlowEntity15minTimeStamp_Type()
)
intervalpolicerOnFlowEntity15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity15minTimeStamp.setStatus("current")
_IntervalpolicerOnFlowEntity1dayTable_Object = MibTable
intervalpolicerOnFlowEntity1dayTable = _IntervalpolicerOnFlowEntity1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 8)
)
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity1dayTable.setStatus("current")
_IntervalpolicerOnFlowEntity1dayEntry_Object = MibTableRow
intervalpolicerOnFlowEntity1dayEntry = _IntervalpolicerOnFlowEntity1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 8, 1)
)
intervalpolicerOnFlowEntity1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "policerOnFlowEntityIndexPolicer"),
    (0, "FspR7-LAYER2-MIB", "intervalpolicerOnFlowEntity1dayNumber"),
)
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity1dayEntry.setStatus("current")


class _IntervalpolicerOnFlowEntity1dayNumber_Type(Integer32):
    """Custom type intervalpolicerOnFlowEntity1dayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IntervalpolicerOnFlowEntity1dayNumber_Type.__name__ = "Integer32"
_IntervalpolicerOnFlowEntity1dayNumber_Object = MibTableColumn
intervalpolicerOnFlowEntity1dayNumber = _IntervalpolicerOnFlowEntity1dayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 8, 1, 1),
    _IntervalpolicerOnFlowEntity1dayNumber_Type()
)
intervalpolicerOnFlowEntity1dayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity1dayNumber.setStatus("current")
_IntervalpolicerOnFlowEntity1dayBytesMarkedGreen_Type = Counter64String
_IntervalpolicerOnFlowEntity1dayBytesMarkedGreen_Object = MibTableColumn
intervalpolicerOnFlowEntity1dayBytesMarkedGreen = _IntervalpolicerOnFlowEntity1dayBytesMarkedGreen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 8, 1, 2),
    _IntervalpolicerOnFlowEntity1dayBytesMarkedGreen_Type()
)
intervalpolicerOnFlowEntity1dayBytesMarkedGreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity1dayBytesMarkedGreen.setStatus("current")
_IntervalpolicerOnFlowEntity1dayFramesMarkedGreen_Type = Counter64String
_IntervalpolicerOnFlowEntity1dayFramesMarkedGreen_Object = MibTableColumn
intervalpolicerOnFlowEntity1dayFramesMarkedGreen = _IntervalpolicerOnFlowEntity1dayFramesMarkedGreen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 8, 1, 3),
    _IntervalpolicerOnFlowEntity1dayFramesMarkedGreen_Type()
)
intervalpolicerOnFlowEntity1dayFramesMarkedGreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity1dayFramesMarkedGreen.setStatus("current")
_IntervalpolicerOnFlowEntity1dayBytesMarkedRed_Type = Counter64String
_IntervalpolicerOnFlowEntity1dayBytesMarkedRed_Object = MibTableColumn
intervalpolicerOnFlowEntity1dayBytesMarkedRed = _IntervalpolicerOnFlowEntity1dayBytesMarkedRed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 8, 1, 4),
    _IntervalpolicerOnFlowEntity1dayBytesMarkedRed_Type()
)
intervalpolicerOnFlowEntity1dayBytesMarkedRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity1dayBytesMarkedRed.setStatus("current")
_IntervalpolicerOnFlowEntity1dayFramesMarkedRed_Type = Counter64String
_IntervalpolicerOnFlowEntity1dayFramesMarkedRed_Object = MibTableColumn
intervalpolicerOnFlowEntity1dayFramesMarkedRed = _IntervalpolicerOnFlowEntity1dayFramesMarkedRed_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 8, 1, 5),
    _IntervalpolicerOnFlowEntity1dayFramesMarkedRed_Type()
)
intervalpolicerOnFlowEntity1dayFramesMarkedRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity1dayFramesMarkedRed.setStatus("current")
_IntervalpolicerOnFlowEntity1dayValidFlag_Type = TruthValue
_IntervalpolicerOnFlowEntity1dayValidFlag_Object = MibTableColumn
intervalpolicerOnFlowEntity1dayValidFlag = _IntervalpolicerOnFlowEntity1dayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 8, 1, 6),
    _IntervalpolicerOnFlowEntity1dayValidFlag_Type()
)
intervalpolicerOnFlowEntity1dayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity1dayValidFlag.setStatus("current")
_IntervalpolicerOnFlowEntity1dayTimeStamp_Type = DateAndTime
_IntervalpolicerOnFlowEntity1dayTimeStamp_Object = MibTableColumn
intervalpolicerOnFlowEntity1dayTimeStamp = _IntervalpolicerOnFlowEntity1dayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 2, 8, 1, 7),
    _IntervalpolicerOnFlowEntity1dayTimeStamp_Type()
)
intervalpolicerOnFlowEntity1dayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalpolicerOnFlowEntity1dayTimeStamp.setStatus("current")
_QuePerformanceMonitoring_ObjectIdentity = ObjectIdentity
quePerformanceMonitoring = _QuePerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3)
)
_CurrentQueOnPortEntity15minTable_Object = MibTable
currentQueOnPortEntity15minTable = _CurrentQueOnPortEntity15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 1)
)
if mibBuilder.loadTexts:
    currentQueOnPortEntity15minTable.setStatus("current")
_CurrentQueOnPortEntity15minEntry_Object = MibTableRow
currentQueOnPortEntity15minEntry = _CurrentQueOnPortEntity15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 1, 1)
)
currentQueOnPortEntity15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexPrio"),
)
if mibBuilder.loadTexts:
    currentQueOnPortEntity15minEntry.setStatus("current")
_CurrentQueOnPortEntity15minBytesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnPortEntity15minBytesDroppedBufOverflow_Object = MibTableColumn
currentQueOnPortEntity15minBytesDroppedBufOverflow = _CurrentQueOnPortEntity15minBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 1, 1, 1),
    _CurrentQueOnPortEntity15minBytesDroppedBufOverflow_Type()
)
currentQueOnPortEntity15minBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnPortEntity15minBytesDroppedBufOverflow.setStatus("current")
_CurrentQueOnPortEntity15minFramesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnPortEntity15minFramesDroppedBufOverflow_Object = MibTableColumn
currentQueOnPortEntity15minFramesDroppedBufOverflow = _CurrentQueOnPortEntity15minFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 1, 1, 2),
    _CurrentQueOnPortEntity15minFramesDroppedBufOverflow_Type()
)
currentQueOnPortEntity15minFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnPortEntity15minFramesDroppedBufOverflow.setStatus("current")


class _CurrentQueOnPortEntity15minElapsedTime_Type(Integer32):
    """Custom type currentQueOnPortEntity15minElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentQueOnPortEntity15minElapsedTime_Type.__name__ = "Integer32"
_CurrentQueOnPortEntity15minElapsedTime_Object = MibTableColumn
currentQueOnPortEntity15minElapsedTime = _CurrentQueOnPortEntity15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 1, 1, 3),
    _CurrentQueOnPortEntity15minElapsedTime_Type()
)
currentQueOnPortEntity15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnPortEntity15minElapsedTime.setStatus("current")
_CurrentQueOnPortEntity1dayTable_Object = MibTable
currentQueOnPortEntity1dayTable = _CurrentQueOnPortEntity1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 2)
)
if mibBuilder.loadTexts:
    currentQueOnPortEntity1dayTable.setStatus("current")
_CurrentQueOnPortEntity1dayEntry_Object = MibTableRow
currentQueOnPortEntity1dayEntry = _CurrentQueOnPortEntity1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 2, 1)
)
currentQueOnPortEntity1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexPrio"),
)
if mibBuilder.loadTexts:
    currentQueOnPortEntity1dayEntry.setStatus("current")
_CurrentQueOnPortEntity1dayBytesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnPortEntity1dayBytesDroppedBufOverflow_Object = MibTableColumn
currentQueOnPortEntity1dayBytesDroppedBufOverflow = _CurrentQueOnPortEntity1dayBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 2, 1, 1),
    _CurrentQueOnPortEntity1dayBytesDroppedBufOverflow_Type()
)
currentQueOnPortEntity1dayBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnPortEntity1dayBytesDroppedBufOverflow.setStatus("current")
_CurrentQueOnPortEntity1dayFramesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnPortEntity1dayFramesDroppedBufOverflow_Object = MibTableColumn
currentQueOnPortEntity1dayFramesDroppedBufOverflow = _CurrentQueOnPortEntity1dayFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 2, 1, 2),
    _CurrentQueOnPortEntity1dayFramesDroppedBufOverflow_Type()
)
currentQueOnPortEntity1dayFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnPortEntity1dayFramesDroppedBufOverflow.setStatus("current")


class _CurrentQueOnPortEntity1dayElapsedTime_Type(Integer32):
    """Custom type currentQueOnPortEntity1dayElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentQueOnPortEntity1dayElapsedTime_Type.__name__ = "Integer32"
_CurrentQueOnPortEntity1dayElapsedTime_Object = MibTableColumn
currentQueOnPortEntity1dayElapsedTime = _CurrentQueOnPortEntity1dayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 2, 1, 3),
    _CurrentQueOnPortEntity1dayElapsedTime_Type()
)
currentQueOnPortEntity1dayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnPortEntity1dayElapsedTime.setStatus("current")
_IntervalQueOnPortEntity15minTable_Object = MibTable
intervalQueOnPortEntity15minTable = _IntervalQueOnPortEntity15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 3)
)
if mibBuilder.loadTexts:
    intervalQueOnPortEntity15minTable.setStatus("current")
_IntervalQueOnPortEntity15minEntry_Object = MibTableRow
intervalQueOnPortEntity15minEntry = _IntervalQueOnPortEntity15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 3, 1)
)
intervalQueOnPortEntity15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexPrio"),
    (0, "FspR7-LAYER2-MIB", "intervalQueOnPortEntity15minNumber"),
)
if mibBuilder.loadTexts:
    intervalQueOnPortEntity15minEntry.setStatus("current")


class _IntervalQueOnPortEntity15minNumber_Type(Integer32):
    """Custom type intervalQueOnPortEntity15minNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IntervalQueOnPortEntity15minNumber_Type.__name__ = "Integer32"
_IntervalQueOnPortEntity15minNumber_Object = MibTableColumn
intervalQueOnPortEntity15minNumber = _IntervalQueOnPortEntity15minNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 3, 1, 1),
    _IntervalQueOnPortEntity15minNumber_Type()
)
intervalQueOnPortEntity15minNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalQueOnPortEntity15minNumber.setStatus("current")
_IntervalQueOnPortEntity15minBytesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnPortEntity15minBytesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnPortEntity15minBytesDroppedBufOverflow = _IntervalQueOnPortEntity15minBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 3, 1, 2),
    _IntervalQueOnPortEntity15minBytesDroppedBufOverflow_Type()
)
intervalQueOnPortEntity15minBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnPortEntity15minBytesDroppedBufOverflow.setStatus("current")
_IntervalQueOnPortEntity15minFramesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnPortEntity15minFramesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnPortEntity15minFramesDroppedBufOverflow = _IntervalQueOnPortEntity15minFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 3, 1, 3),
    _IntervalQueOnPortEntity15minFramesDroppedBufOverflow_Type()
)
intervalQueOnPortEntity15minFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnPortEntity15minFramesDroppedBufOverflow.setStatus("current")
_IntervalQueOnPortEntity15minValidFlag_Type = TruthValue
_IntervalQueOnPortEntity15minValidFlag_Object = MibTableColumn
intervalQueOnPortEntity15minValidFlag = _IntervalQueOnPortEntity15minValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 3, 1, 4),
    _IntervalQueOnPortEntity15minValidFlag_Type()
)
intervalQueOnPortEntity15minValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnPortEntity15minValidFlag.setStatus("current")
_IntervalQueOnPortEntity15minTimeStamp_Type = DateAndTime
_IntervalQueOnPortEntity15minTimeStamp_Object = MibTableColumn
intervalQueOnPortEntity15minTimeStamp = _IntervalQueOnPortEntity15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 3, 1, 5),
    _IntervalQueOnPortEntity15minTimeStamp_Type()
)
intervalQueOnPortEntity15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnPortEntity15minTimeStamp.setStatus("current")
_IntervalQueOnPortEntity1dayTable_Object = MibTable
intervalQueOnPortEntity1dayTable = _IntervalQueOnPortEntity1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 4)
)
if mibBuilder.loadTexts:
    intervalQueOnPortEntity1dayTable.setStatus("current")
_IntervalQueOnPortEntity1dayEntry_Object = MibTableRow
intervalQueOnPortEntity1dayEntry = _IntervalQueOnPortEntity1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 4, 1)
)
intervalQueOnPortEntity1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnPortEntityIndexPrio"),
    (0, "FspR7-LAYER2-MIB", "intervalQueOnPortEntity1dayNumber"),
)
if mibBuilder.loadTexts:
    intervalQueOnPortEntity1dayEntry.setStatus("current")


class _IntervalQueOnPortEntity1dayNumber_Type(Integer32):
    """Custom type intervalQueOnPortEntity1dayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IntervalQueOnPortEntity1dayNumber_Type.__name__ = "Integer32"
_IntervalQueOnPortEntity1dayNumber_Object = MibTableColumn
intervalQueOnPortEntity1dayNumber = _IntervalQueOnPortEntity1dayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 4, 1, 1),
    _IntervalQueOnPortEntity1dayNumber_Type()
)
intervalQueOnPortEntity1dayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalQueOnPortEntity1dayNumber.setStatus("current")
_IntervalQueOnPortEntity1dayBytesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnPortEntity1dayBytesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnPortEntity1dayBytesDroppedBufOverflow = _IntervalQueOnPortEntity1dayBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 4, 1, 2),
    _IntervalQueOnPortEntity1dayBytesDroppedBufOverflow_Type()
)
intervalQueOnPortEntity1dayBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnPortEntity1dayBytesDroppedBufOverflow.setStatus("current")
_IntervalQueOnPortEntity1dayFramesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnPortEntity1dayFramesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnPortEntity1dayFramesDroppedBufOverflow = _IntervalQueOnPortEntity1dayFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 4, 1, 3),
    _IntervalQueOnPortEntity1dayFramesDroppedBufOverflow_Type()
)
intervalQueOnPortEntity1dayFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnPortEntity1dayFramesDroppedBufOverflow.setStatus("current")
_IntervalQueOnPortEntity1dayValidFlag_Type = TruthValue
_IntervalQueOnPortEntity1dayValidFlag_Object = MibTableColumn
intervalQueOnPortEntity1dayValidFlag = _IntervalQueOnPortEntity1dayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 4, 1, 4),
    _IntervalQueOnPortEntity1dayValidFlag_Type()
)
intervalQueOnPortEntity1dayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnPortEntity1dayValidFlag.setStatus("current")
_IntervalQueOnPortEntity1dayTimeStamp_Type = DateAndTime
_IntervalQueOnPortEntity1dayTimeStamp_Object = MibTableColumn
intervalQueOnPortEntity1dayTimeStamp = _IntervalQueOnPortEntity1dayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 4, 1, 5),
    _IntervalQueOnPortEntity1dayTimeStamp_Type()
)
intervalQueOnPortEntity1dayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnPortEntity1dayTimeStamp.setStatus("current")
_CurrentQueOnFlowEntity15minTable_Object = MibTable
currentQueOnFlowEntity15minTable = _CurrentQueOnFlowEntity15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 5)
)
if mibBuilder.loadTexts:
    currentQueOnFlowEntity15minTable.setStatus("current")
_CurrentQueOnFlowEntity15minEntry_Object = MibTableRow
currentQueOnFlowEntity15minEntry = _CurrentQueOnFlowEntity15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 5, 1)
)
currentQueOnFlowEntity15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexPrio"),
)
if mibBuilder.loadTexts:
    currentQueOnFlowEntity15minEntry.setStatus("current")
_CurrentQueOnFlowEntity15minBytesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnFlowEntity15minBytesDroppedBufOverflow_Object = MibTableColumn
currentQueOnFlowEntity15minBytesDroppedBufOverflow = _CurrentQueOnFlowEntity15minBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 5, 1, 1),
    _CurrentQueOnFlowEntity15minBytesDroppedBufOverflow_Type()
)
currentQueOnFlowEntity15minBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnFlowEntity15minBytesDroppedBufOverflow.setStatus("current")
_CurrentQueOnFlowEntity15minFramesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnFlowEntity15minFramesDroppedBufOverflow_Object = MibTableColumn
currentQueOnFlowEntity15minFramesDroppedBufOverflow = _CurrentQueOnFlowEntity15minFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 5, 1, 2),
    _CurrentQueOnFlowEntity15minFramesDroppedBufOverflow_Type()
)
currentQueOnFlowEntity15minFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnFlowEntity15minFramesDroppedBufOverflow.setStatus("current")


class _CurrentQueOnFlowEntity15minElapsedTime_Type(Integer32):
    """Custom type currentQueOnFlowEntity15minElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentQueOnFlowEntity15minElapsedTime_Type.__name__ = "Integer32"
_CurrentQueOnFlowEntity15minElapsedTime_Object = MibTableColumn
currentQueOnFlowEntity15minElapsedTime = _CurrentQueOnFlowEntity15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 5, 1, 3),
    _CurrentQueOnFlowEntity15minElapsedTime_Type()
)
currentQueOnFlowEntity15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnFlowEntity15minElapsedTime.setStatus("current")
_CurrentQueOnFlowEntity1dayTable_Object = MibTable
currentQueOnFlowEntity1dayTable = _CurrentQueOnFlowEntity1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 6)
)
if mibBuilder.loadTexts:
    currentQueOnFlowEntity1dayTable.setStatus("current")
_CurrentQueOnFlowEntity1dayEntry_Object = MibTableRow
currentQueOnFlowEntity1dayEntry = _CurrentQueOnFlowEntity1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 6, 1)
)
currentQueOnFlowEntity1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexPrio"),
)
if mibBuilder.loadTexts:
    currentQueOnFlowEntity1dayEntry.setStatus("current")
_CurrentQueOnFlowEntity1dayBytesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnFlowEntity1dayBytesDroppedBufOverflow_Object = MibTableColumn
currentQueOnFlowEntity1dayBytesDroppedBufOverflow = _CurrentQueOnFlowEntity1dayBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 6, 1, 1),
    _CurrentQueOnFlowEntity1dayBytesDroppedBufOverflow_Type()
)
currentQueOnFlowEntity1dayBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnFlowEntity1dayBytesDroppedBufOverflow.setStatus("current")
_CurrentQueOnFlowEntity1dayFramesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnFlowEntity1dayFramesDroppedBufOverflow_Object = MibTableColumn
currentQueOnFlowEntity1dayFramesDroppedBufOverflow = _CurrentQueOnFlowEntity1dayFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 6, 1, 2),
    _CurrentQueOnFlowEntity1dayFramesDroppedBufOverflow_Type()
)
currentQueOnFlowEntity1dayFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnFlowEntity1dayFramesDroppedBufOverflow.setStatus("current")


class _CurrentQueOnFlowEntity1dayElapsedTime_Type(Integer32):
    """Custom type currentQueOnFlowEntity1dayElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentQueOnFlowEntity1dayElapsedTime_Type.__name__ = "Integer32"
_CurrentQueOnFlowEntity1dayElapsedTime_Object = MibTableColumn
currentQueOnFlowEntity1dayElapsedTime = _CurrentQueOnFlowEntity1dayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 6, 1, 3),
    _CurrentQueOnFlowEntity1dayElapsedTime_Type()
)
currentQueOnFlowEntity1dayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnFlowEntity1dayElapsedTime.setStatus("current")
_IntervalQueOnFlowEntity15minTable_Object = MibTable
intervalQueOnFlowEntity15minTable = _IntervalQueOnFlowEntity15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 7)
)
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity15minTable.setStatus("current")
_IntervalQueOnFlowEntity15minEntry_Object = MibTableRow
intervalQueOnFlowEntity15minEntry = _IntervalQueOnFlowEntity15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 7, 1)
)
intervalQueOnFlowEntity15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexPrio"),
    (0, "FspR7-LAYER2-MIB", "intervalQueOnFlowEntity15minNumber"),
)
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity15minEntry.setStatus("current")


class _IntervalQueOnFlowEntity15minNumber_Type(Integer32):
    """Custom type intervalQueOnFlowEntity15minNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IntervalQueOnFlowEntity15minNumber_Type.__name__ = "Integer32"
_IntervalQueOnFlowEntity15minNumber_Object = MibTableColumn
intervalQueOnFlowEntity15minNumber = _IntervalQueOnFlowEntity15minNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 7, 1, 1),
    _IntervalQueOnFlowEntity15minNumber_Type()
)
intervalQueOnFlowEntity15minNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity15minNumber.setStatus("current")
_IntervalQueOnFlowEntity15minBytesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnFlowEntity15minBytesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnFlowEntity15minBytesDroppedBufOverflow = _IntervalQueOnFlowEntity15minBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 7, 1, 2),
    _IntervalQueOnFlowEntity15minBytesDroppedBufOverflow_Type()
)
intervalQueOnFlowEntity15minBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity15minBytesDroppedBufOverflow.setStatus("current")
_IntervalQueOnFlowEntity15minFramesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnFlowEntity15minFramesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnFlowEntity15minFramesDroppedBufOverflow = _IntervalQueOnFlowEntity15minFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 7, 1, 3),
    _IntervalQueOnFlowEntity15minFramesDroppedBufOverflow_Type()
)
intervalQueOnFlowEntity15minFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity15minFramesDroppedBufOverflow.setStatus("current")
_IntervalQueOnFlowEntity15minValidFlag_Type = TruthValue
_IntervalQueOnFlowEntity15minValidFlag_Object = MibTableColumn
intervalQueOnFlowEntity15minValidFlag = _IntervalQueOnFlowEntity15minValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 7, 1, 4),
    _IntervalQueOnFlowEntity15minValidFlag_Type()
)
intervalQueOnFlowEntity15minValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity15minValidFlag.setStatus("current")
_IntervalQueOnFlowEntity15minTimeStamp_Type = DateAndTime
_IntervalQueOnFlowEntity15minTimeStamp_Object = MibTableColumn
intervalQueOnFlowEntity15minTimeStamp = _IntervalQueOnFlowEntity15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 7, 1, 5),
    _IntervalQueOnFlowEntity15minTimeStamp_Type()
)
intervalQueOnFlowEntity15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity15minTimeStamp.setStatus("current")
_IntervalQueOnFlowEntity1dayTable_Object = MibTable
intervalQueOnFlowEntity1dayTable = _IntervalQueOnFlowEntity1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 8)
)
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity1dayTable.setStatus("current")
_IntervalQueOnFlowEntity1dayEntry_Object = MibTableRow
intervalQueOnFlowEntity1dayEntry = _IntervalQueOnFlowEntity1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 8, 1)
)
intervalQueOnFlowEntity1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "queOnFlowEntityIndexPrio"),
    (0, "FspR7-LAYER2-MIB", "intervalQueOnFlowEntity1dayNumber"),
)
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity1dayEntry.setStatus("current")


class _IntervalQueOnFlowEntity1dayNumber_Type(Integer32):
    """Custom type intervalQueOnFlowEntity1dayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IntervalQueOnFlowEntity1dayNumber_Type.__name__ = "Integer32"
_IntervalQueOnFlowEntity1dayNumber_Object = MibTableColumn
intervalQueOnFlowEntity1dayNumber = _IntervalQueOnFlowEntity1dayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 8, 1, 1),
    _IntervalQueOnFlowEntity1dayNumber_Type()
)
intervalQueOnFlowEntity1dayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity1dayNumber.setStatus("current")
_IntervalQueOnFlowEntity1dayBytesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnFlowEntity1dayBytesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnFlowEntity1dayBytesDroppedBufOverflow = _IntervalQueOnFlowEntity1dayBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 8, 1, 2),
    _IntervalQueOnFlowEntity1dayBytesDroppedBufOverflow_Type()
)
intervalQueOnFlowEntity1dayBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity1dayBytesDroppedBufOverflow.setStatus("current")
_IntervalQueOnFlowEntity1dayFramesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnFlowEntity1dayFramesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnFlowEntity1dayFramesDroppedBufOverflow = _IntervalQueOnFlowEntity1dayFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 8, 1, 3),
    _IntervalQueOnFlowEntity1dayFramesDroppedBufOverflow_Type()
)
intervalQueOnFlowEntity1dayFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity1dayFramesDroppedBufOverflow.setStatus("current")
_IntervalQueOnFlowEntity1dayValidFlag_Type = TruthValue
_IntervalQueOnFlowEntity1dayValidFlag_Object = MibTableColumn
intervalQueOnFlowEntity1dayValidFlag = _IntervalQueOnFlowEntity1dayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 8, 1, 4),
    _IntervalQueOnFlowEntity1dayValidFlag_Type()
)
intervalQueOnFlowEntity1dayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity1dayValidFlag.setStatus("current")
_IntervalQueOnFlowEntity1dayTimeStamp_Type = DateAndTime
_IntervalQueOnFlowEntity1dayTimeStamp_Object = MibTableColumn
intervalQueOnFlowEntity1dayTimeStamp = _IntervalQueOnFlowEntity1dayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 8, 1, 5),
    _IntervalQueOnFlowEntity1dayTimeStamp_Type()
)
intervalQueOnFlowEntity1dayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnFlowEntity1dayTimeStamp.setStatus("current")
_CurrentQueOnBridgeEntity15minTable_Object = MibTable
currentQueOnBridgeEntity15minTable = _CurrentQueOnBridgeEntity15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 9)
)
if mibBuilder.loadTexts:
    currentQueOnBridgeEntity15minTable.setStatus("current")
_CurrentQueOnBridgeEntity15minEntry_Object = MibTableRow
currentQueOnBridgeEntity15minEntry = _CurrentQueOnBridgeEntity15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 9, 1)
)
currentQueOnBridgeEntity15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityIndex"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityPrio"),
)
if mibBuilder.loadTexts:
    currentQueOnBridgeEntity15minEntry.setStatus("current")
_CurrentQueOnBridgeEntity15minBytesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnBridgeEntity15minBytesDroppedBufOverflow_Object = MibTableColumn
currentQueOnBridgeEntity15minBytesDroppedBufOverflow = _CurrentQueOnBridgeEntity15minBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 9, 1, 1),
    _CurrentQueOnBridgeEntity15minBytesDroppedBufOverflow_Type()
)
currentQueOnBridgeEntity15minBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnBridgeEntity15minBytesDroppedBufOverflow.setStatus("current")
_CurrentQueOnBridgeEntity15minFramesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnBridgeEntity15minFramesDroppedBufOverflow_Object = MibTableColumn
currentQueOnBridgeEntity15minFramesDroppedBufOverflow = _CurrentQueOnBridgeEntity15minFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 9, 1, 2),
    _CurrentQueOnBridgeEntity15minFramesDroppedBufOverflow_Type()
)
currentQueOnBridgeEntity15minFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnBridgeEntity15minFramesDroppedBufOverflow.setStatus("current")


class _CurrentQueOnBridgeEntity15minElapsedTime_Type(Integer32):
    """Custom type currentQueOnBridgeEntity15minElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentQueOnBridgeEntity15minElapsedTime_Type.__name__ = "Integer32"
_CurrentQueOnBridgeEntity15minElapsedTime_Object = MibTableColumn
currentQueOnBridgeEntity15minElapsedTime = _CurrentQueOnBridgeEntity15minElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 9, 1, 3),
    _CurrentQueOnBridgeEntity15minElapsedTime_Type()
)
currentQueOnBridgeEntity15minElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnBridgeEntity15minElapsedTime.setStatus("current")
_CurrentQueOnBridgeEntity1dayTable_Object = MibTable
currentQueOnBridgeEntity1dayTable = _CurrentQueOnBridgeEntity1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 10)
)
if mibBuilder.loadTexts:
    currentQueOnBridgeEntity1dayTable.setStatus("current")
_CurrentQueOnBridgeEntity1dayEntry_Object = MibTableRow
currentQueOnBridgeEntity1dayEntry = _CurrentQueOnBridgeEntity1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 10, 1)
)
currentQueOnBridgeEntity1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityIndex"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityPrio"),
)
if mibBuilder.loadTexts:
    currentQueOnBridgeEntity1dayEntry.setStatus("current")
_CurrentQueOnBridgeEntity1dayBytesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnBridgeEntity1dayBytesDroppedBufOverflow_Object = MibTableColumn
currentQueOnBridgeEntity1dayBytesDroppedBufOverflow = _CurrentQueOnBridgeEntity1dayBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 10, 1, 1),
    _CurrentQueOnBridgeEntity1dayBytesDroppedBufOverflow_Type()
)
currentQueOnBridgeEntity1dayBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnBridgeEntity1dayBytesDroppedBufOverflow.setStatus("current")
_CurrentQueOnBridgeEntity1dayFramesDroppedBufOverflow_Type = Counter64String
_CurrentQueOnBridgeEntity1dayFramesDroppedBufOverflow_Object = MibTableColumn
currentQueOnBridgeEntity1dayFramesDroppedBufOverflow = _CurrentQueOnBridgeEntity1dayFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 10, 1, 2),
    _CurrentQueOnBridgeEntity1dayFramesDroppedBufOverflow_Type()
)
currentQueOnBridgeEntity1dayFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnBridgeEntity1dayFramesDroppedBufOverflow.setStatus("current")


class _CurrentQueOnBridgeEntity1dayElapsedTime_Type(Integer32):
    """Custom type currentQueOnBridgeEntity1dayElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_CurrentQueOnBridgeEntity1dayElapsedTime_Type.__name__ = "Integer32"
_CurrentQueOnBridgeEntity1dayElapsedTime_Object = MibTableColumn
currentQueOnBridgeEntity1dayElapsedTime = _CurrentQueOnBridgeEntity1dayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 10, 1, 3),
    _CurrentQueOnBridgeEntity1dayElapsedTime_Type()
)
currentQueOnBridgeEntity1dayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentQueOnBridgeEntity1dayElapsedTime.setStatus("current")
_IntervalQueOnBridgeEntity15minTable_Object = MibTable
intervalQueOnBridgeEntity15minTable = _IntervalQueOnBridgeEntity15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 11)
)
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity15minTable.setStatus("current")
_IntervalQueOnBridgeEntity15minEntry_Object = MibTableRow
intervalQueOnBridgeEntity15minEntry = _IntervalQueOnBridgeEntity15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 11, 1)
)
intervalQueOnBridgeEntity15minEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityIndex"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityPrio"),
    (0, "FspR7-LAYER2-MIB", "intervalQueOnBridgeEntity15minNumber"),
)
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity15minEntry.setStatus("current")


class _IntervalQueOnBridgeEntity15minNumber_Type(Integer32):
    """Custom type intervalQueOnBridgeEntity15minNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IntervalQueOnBridgeEntity15minNumber_Type.__name__ = "Integer32"
_IntervalQueOnBridgeEntity15minNumber_Object = MibTableColumn
intervalQueOnBridgeEntity15minNumber = _IntervalQueOnBridgeEntity15minNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 11, 1, 1),
    _IntervalQueOnBridgeEntity15minNumber_Type()
)
intervalQueOnBridgeEntity15minNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity15minNumber.setStatus("current")
_IntervalQueOnBridgeEntity15minBytesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnBridgeEntity15minBytesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnBridgeEntity15minBytesDroppedBufOverflow = _IntervalQueOnBridgeEntity15minBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 11, 1, 2),
    _IntervalQueOnBridgeEntity15minBytesDroppedBufOverflow_Type()
)
intervalQueOnBridgeEntity15minBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity15minBytesDroppedBufOverflow.setStatus("current")
_IntervalQueOnBridgeEntity15minFramesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnBridgeEntity15minFramesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnBridgeEntity15minFramesDroppedBufOverflow = _IntervalQueOnBridgeEntity15minFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 11, 1, 3),
    _IntervalQueOnBridgeEntity15minFramesDroppedBufOverflow_Type()
)
intervalQueOnBridgeEntity15minFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity15minFramesDroppedBufOverflow.setStatus("current")
_IntervalQueOnBridgeEntity15minValidFlag_Type = TruthValue
_IntervalQueOnBridgeEntity15minValidFlag_Object = MibTableColumn
intervalQueOnBridgeEntity15minValidFlag = _IntervalQueOnBridgeEntity15minValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 11, 1, 4),
    _IntervalQueOnBridgeEntity15minValidFlag_Type()
)
intervalQueOnBridgeEntity15minValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity15minValidFlag.setStatus("current")
_IntervalQueOnBridgeEntity15minTimeStamp_Type = DateAndTime
_IntervalQueOnBridgeEntity15minTimeStamp_Object = MibTableColumn
intervalQueOnBridgeEntity15minTimeStamp = _IntervalQueOnBridgeEntity15minTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 11, 1, 5),
    _IntervalQueOnBridgeEntity15minTimeStamp_Type()
)
intervalQueOnBridgeEntity15minTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity15minTimeStamp.setStatus("current")
_IntervalQueOnBridgeEntity1dayTable_Object = MibTable
intervalQueOnBridgeEntity1dayTable = _IntervalQueOnBridgeEntity1dayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 12)
)
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity1dayTable.setStatus("current")
_IntervalQueOnBridgeEntity1dayEntry_Object = MibTableRow
intervalQueOnBridgeEntity1dayEntry = _IntervalQueOnBridgeEntity1dayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 12, 1)
)
intervalQueOnBridgeEntity1dayEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityIndex"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "queOnBridgeEntityPrio"),
    (0, "FspR7-LAYER2-MIB", "intervalQueOnBridgeEntity1dayNumber"),
)
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity1dayEntry.setStatus("current")


class _IntervalQueOnBridgeEntity1dayNumber_Type(Integer32):
    """Custom type intervalQueOnBridgeEntity1dayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IntervalQueOnBridgeEntity1dayNumber_Type.__name__ = "Integer32"
_IntervalQueOnBridgeEntity1dayNumber_Object = MibTableColumn
intervalQueOnBridgeEntity1dayNumber = _IntervalQueOnBridgeEntity1dayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 12, 1, 1),
    _IntervalQueOnBridgeEntity1dayNumber_Type()
)
intervalQueOnBridgeEntity1dayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity1dayNumber.setStatus("current")
_IntervalQueOnBridgeEntity1dayBytesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnBridgeEntity1dayBytesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnBridgeEntity1dayBytesDroppedBufOverflow = _IntervalQueOnBridgeEntity1dayBytesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 12, 1, 2),
    _IntervalQueOnBridgeEntity1dayBytesDroppedBufOverflow_Type()
)
intervalQueOnBridgeEntity1dayBytesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity1dayBytesDroppedBufOverflow.setStatus("current")
_IntervalQueOnBridgeEntity1dayFramesDroppedBufOverflow_Type = Counter64String
_IntervalQueOnBridgeEntity1dayFramesDroppedBufOverflow_Object = MibTableColumn
intervalQueOnBridgeEntity1dayFramesDroppedBufOverflow = _IntervalQueOnBridgeEntity1dayFramesDroppedBufOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 12, 1, 3),
    _IntervalQueOnBridgeEntity1dayFramesDroppedBufOverflow_Type()
)
intervalQueOnBridgeEntity1dayFramesDroppedBufOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity1dayFramesDroppedBufOverflow.setStatus("current")
_IntervalQueOnBridgeEntity1dayValidFlag_Type = TruthValue
_IntervalQueOnBridgeEntity1dayValidFlag_Object = MibTableColumn
intervalQueOnBridgeEntity1dayValidFlag = _IntervalQueOnBridgeEntity1dayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 12, 1, 4),
    _IntervalQueOnBridgeEntity1dayValidFlag_Type()
)
intervalQueOnBridgeEntity1dayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity1dayValidFlag.setStatus("current")
_IntervalQueOnBridgeEntity1dayTimeStamp_Type = DateAndTime
_IntervalQueOnBridgeEntity1dayTimeStamp_Object = MibTableColumn
intervalQueOnBridgeEntity1dayTimeStamp = _IntervalQueOnBridgeEntity1dayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 16, 3, 12, 1, 5),
    _IntervalQueOnBridgeEntity1dayTimeStamp_Type()
)
intervalQueOnBridgeEntity1dayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalQueOnBridgeEntity1dayTimeStamp.setStatus("current")
_Layer2Alarms_ObjectIdentity = ObjectIdentity
layer2Alarms = _Layer2Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17)
)
_Layer2Traps_ObjectIdentity = ObjectIdentity
layer2Traps = _Layer2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1)
)
_Layer2TrapsPrefix_ObjectIdentity = ObjectIdentity
layer2TrapsPrefix = _Layer2TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0)
)
_Layer2Conditions_ObjectIdentity = ObjectIdentity
layer2Conditions = _Layer2Conditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2)
)
_FlowConditionSeverityTable_Object = MibTable
flowConditionSeverityTable = _FlowConditionSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 1)
)
if mibBuilder.loadTexts:
    flowConditionSeverityTable.setStatus("current")
_FlowConditionSeverityEntry_Object = MibTableRow
flowConditionSeverityEntry = _FlowConditionSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 1, 1)
)
flowConditionSeverityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowConditionSeverityType"),
)
if mibBuilder.loadTexts:
    flowConditionSeverityEntry.setStatus("current")
_FlowConditionSeverityType_Type = FspR7L2StandingConditionTypes
_FlowConditionSeverityType_Object = MibTableColumn
flowConditionSeverityType = _FlowConditionSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 1, 1, 1),
    _FlowConditionSeverityType_Type()
)
flowConditionSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowConditionSeverityType.setStatus("current")
_FlowConditionSeverityValue_Type = TrapAlarmSeverity
_FlowConditionSeverityValue_Object = MibTableColumn
flowConditionSeverityValue = _FlowConditionSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 1, 1, 2),
    _FlowConditionSeverityValue_Type()
)
flowConditionSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowConditionSeverityValue.setStatus("current")
_BridgeConditionSeverityTable_Object = MibTable
bridgeConditionSeverityTable = _BridgeConditionSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 2)
)
if mibBuilder.loadTexts:
    bridgeConditionSeverityTable.setStatus("current")
_BridgeConditionSeverityEntry_Object = MibTableRow
bridgeConditionSeverityEntry = _BridgeConditionSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 2, 1)
)
bridgeConditionSeverityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "bridgeConditionSeverityType"),
)
if mibBuilder.loadTexts:
    bridgeConditionSeverityEntry.setStatus("current")
_BridgeConditionSeverityType_Type = BridgeStandingConditionTypes
_BridgeConditionSeverityType_Object = MibTableColumn
bridgeConditionSeverityType = _BridgeConditionSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 2, 1, 1),
    _BridgeConditionSeverityType_Type()
)
bridgeConditionSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeConditionSeverityType.setStatus("current")
_BridgeConditionSeverityValue_Type = TrapAlarmSeverity
_BridgeConditionSeverityValue_Object = MibTableColumn
bridgeConditionSeverityValue = _BridgeConditionSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 2, 1, 2),
    _BridgeConditionSeverityValue_Type()
)
bridgeConditionSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConditionSeverityValue.setStatus("current")
_FlowCurrentConditionTable_Object = MibTable
flowCurrentConditionTable = _FlowCurrentConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 6)
)
if mibBuilder.loadTexts:
    flowCurrentConditionTable.setStatus("current")
_FlowCurrentConditionEntry_Object = MibTableRow
flowCurrentConditionEntry = _FlowCurrentConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 6, 1)
)
flowCurrentConditionEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
    (0, "FspR7-LAYER2-MIB", "flowCurrentConditionType"),
)
if mibBuilder.loadTexts:
    flowCurrentConditionEntry.setStatus("current")
_FlowCurrentConditionType_Type = FspR7L2StandingConditionTypes
_FlowCurrentConditionType_Object = MibTableColumn
flowCurrentConditionType = _FlowCurrentConditionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 6, 1, 1),
    _FlowCurrentConditionType_Type()
)
flowCurrentConditionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowCurrentConditionType.setStatus("current")
_FlowCurrentConditionSeverity_Type = TrapAlarmSeverity
_FlowCurrentConditionSeverity_Object = MibTableColumn
flowCurrentConditionSeverity = _FlowCurrentConditionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 6, 1, 2),
    _FlowCurrentConditionSeverity_Type()
)
flowCurrentConditionSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowCurrentConditionSeverity.setStatus("current")
_FlowCurrentConditionAffect_Type = ServiceImpairment
_FlowCurrentConditionAffect_Object = MibTableColumn
flowCurrentConditionAffect = _FlowCurrentConditionAffect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 6, 1, 3),
    _FlowCurrentConditionAffect_Type()
)
flowCurrentConditionAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowCurrentConditionAffect.setStatus("current")
_FlowCurrentConditionTimeStamp_Type = DateAndTime
_FlowCurrentConditionTimeStamp_Object = MibTableColumn
flowCurrentConditionTimeStamp = _FlowCurrentConditionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 6, 1, 4),
    _FlowCurrentConditionTimeStamp_Type()
)
flowCurrentConditionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowCurrentConditionTimeStamp.setStatus("current")
_BridgeCurrentConditionTable_Object = MibTable
bridgeCurrentConditionTable = _BridgeCurrentConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 7)
)
if mibBuilder.loadTexts:
    bridgeCurrentConditionTable.setStatus("current")
_BridgeCurrentConditionEntry_Object = MibTableRow
bridgeCurrentConditionEntry = _BridgeCurrentConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 7, 1)
)
bridgeCurrentConditionEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
    (0, "FspR7-LAYER2-MIB", "bridgeEntitySvid"),
    (0, "FspR7-LAYER2-MIB", "bridgeCurrentConditionType"),
)
if mibBuilder.loadTexts:
    bridgeCurrentConditionEntry.setStatus("current")
_BridgeCurrentConditionType_Type = BridgeStandingConditionTypes
_BridgeCurrentConditionType_Object = MibTableColumn
bridgeCurrentConditionType = _BridgeCurrentConditionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 7, 1, 1),
    _BridgeCurrentConditionType_Type()
)
bridgeCurrentConditionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeCurrentConditionType.setStatus("current")
_BridgeCurrentConditionSeverity_Type = TrapAlarmSeverity
_BridgeCurrentConditionSeverity_Object = MibTableColumn
bridgeCurrentConditionSeverity = _BridgeCurrentConditionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 7, 1, 2),
    _BridgeCurrentConditionSeverity_Type()
)
bridgeCurrentConditionSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCurrentConditionSeverity.setStatus("current")
_BridgeCurrentConditionAffect_Type = ServiceImpairment
_BridgeCurrentConditionAffect_Object = MibTableColumn
bridgeCurrentConditionAffect = _BridgeCurrentConditionAffect_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 7, 1, 3),
    _BridgeCurrentConditionAffect_Type()
)
bridgeCurrentConditionAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCurrentConditionAffect.setStatus("current")
_BridgeCurrentConditionTimeStamp_Type = DateAndTime
_BridgeCurrentConditionTimeStamp_Object = MibTableColumn
bridgeCurrentConditionTimeStamp = _BridgeCurrentConditionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 2, 7, 1, 4),
    _BridgeCurrentConditionTimeStamp_Type()
)
bridgeCurrentConditionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeCurrentConditionTimeStamp.setStatus("current")
_Layer2FlowProtection_ObjectIdentity = ObjectIdentity
layer2FlowProtection = _Layer2FlowProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18)
)
_FlowProtectionToAssignEntityTable_Object = MibTable
flowProtectionToAssignEntityTable = _FlowProtectionToAssignEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 11)
)
if mibBuilder.loadTexts:
    flowProtectionToAssignEntityTable.setStatus("current")
_FlowProtectionToAssignEntityEntry_Object = MibTableRow
flowProtectionToAssignEntityEntry = _FlowProtectionToAssignEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 11, 1)
)
flowProtectionToAssignEntityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowProtectionToAssignEntityEntry.setStatus("current")
_FlowProtectionToAssignEntityIndexAid_Type = SnmpAdminString
_FlowProtectionToAssignEntityIndexAid_Object = MibTableColumn
flowProtectionToAssignEntityIndexAid = _FlowProtectionToAssignEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 11, 1, 1),
    _FlowProtectionToAssignEntityIndexAid_Type()
)
flowProtectionToAssignEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionToAssignEntityIndexAid.setStatus("current")
_FlowProtectionToAssignEntityClass_Type = EntityClass
_FlowProtectionToAssignEntityClass_Object = MibTableColumn
flowProtectionToAssignEntityClass = _FlowProtectionToAssignEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 11, 1, 2),
    _FlowProtectionToAssignEntityClass_Type()
)
flowProtectionToAssignEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionToAssignEntityClass.setStatus("current")


class _FlowProtectionToAssignEntityClassInstanceNumber_Type(Integer32):
    """Custom type flowProtectionToAssignEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_FlowProtectionToAssignEntityClassInstanceNumber_Type.__name__ = "Integer32"
_FlowProtectionToAssignEntityClassInstanceNumber_Object = MibTableColumn
flowProtectionToAssignEntityClassInstanceNumber = _FlowProtectionToAssignEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 11, 1, 3),
    _FlowProtectionToAssignEntityClassInstanceNumber_Type()
)
flowProtectionToAssignEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionToAssignEntityClassInstanceNumber.setStatus("current")
_FlowProtectionAssignedEntityTable_Object = MibTable
flowProtectionAssignedEntityTable = _FlowProtectionAssignedEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 12)
)
if mibBuilder.loadTexts:
    flowProtectionAssignedEntityTable.setStatus("current")
_FlowProtectionAssignedEntityEntry_Object = MibTableRow
flowProtectionAssignedEntityEntry = _FlowProtectionAssignedEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 12, 1)
)
flowProtectionAssignedEntityEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowProtectionAssignedEntityEntry.setStatus("current")
_FlowProtectionAssignedEntityIndexAid_Type = SnmpAdminString
_FlowProtectionAssignedEntityIndexAid_Object = MibTableColumn
flowProtectionAssignedEntityIndexAid = _FlowProtectionAssignedEntityIndexAid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 12, 1, 1),
    _FlowProtectionAssignedEntityIndexAid_Type()
)
flowProtectionAssignedEntityIndexAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionAssignedEntityIndexAid.setStatus("current")
_FlowProtectionAssignedEntityClass_Type = EntityClass
_FlowProtectionAssignedEntityClass_Object = MibTableColumn
flowProtectionAssignedEntityClass = _FlowProtectionAssignedEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 12, 1, 2),
    _FlowProtectionAssignedEntityClass_Type()
)
flowProtectionAssignedEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionAssignedEntityClass.setStatus("current")


class _FlowProtectionAssignedEntityClassInstanceNumber_Type(Integer32):
    """Custom type flowProtectionAssignedEntityClassInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_FlowProtectionAssignedEntityClassInstanceNumber_Type.__name__ = "Integer32"
_FlowProtectionAssignedEntityClassInstanceNumber_Object = MibTableColumn
flowProtectionAssignedEntityClassInstanceNumber = _FlowProtectionAssignedEntityClassInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 12, 1, 3),
    _FlowProtectionAssignedEntityClassInstanceNumber_Type()
)
flowProtectionAssignedEntityClassInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionAssignedEntityClassInstanceNumber.setStatus("current")
_FlowProtectionProvisionTable_Object = MibTable
flowProtectionProvisionTable = _FlowProtectionProvisionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13)
)
if mibBuilder.loadTexts:
    flowProtectionProvisionTable.setStatus("current")
_FlowProtectionProvisionEntry_Object = MibTableRow
flowProtectionProvisionEntry = _FlowProtectionProvisionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1)
)
flowProtectionProvisionEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowProtectionProvisionEntry.setStatus("current")
_FlowProtectionProvisionRowStatus_Type = RowStatus
_FlowProtectionProvisionRowStatus_Object = MibTableColumn
flowProtectionProvisionRowStatus = _FlowProtectionProvisionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1, 1),
    _FlowProtectionProvisionRowStatus_Type()
)
flowProtectionProvisionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowProtectionProvisionRowStatus.setStatus("current")
_FlowProtectionProvisionWorkingEthIndex_Type = EntityIndex
_FlowProtectionProvisionWorkingEthIndex_Object = MibTableColumn
flowProtectionProvisionWorkingEthIndex = _FlowProtectionProvisionWorkingEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1, 2),
    _FlowProtectionProvisionWorkingEthIndex_Type()
)
flowProtectionProvisionWorkingEthIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowProtectionProvisionWorkingEthIndex.setStatus("current")
_FlowProtectionProvisionWorkingFlwIndex_Type = Unsigned32
_FlowProtectionProvisionWorkingFlwIndex_Object = MibTableColumn
flowProtectionProvisionWorkingFlwIndex = _FlowProtectionProvisionWorkingFlwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1, 3),
    _FlowProtectionProvisionWorkingFlwIndex_Type()
)
flowProtectionProvisionWorkingFlwIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowProtectionProvisionWorkingFlwIndex.setStatus("current")
_FlowProtectionProvisionProtectionEthIndex_Type = EntityIndex
_FlowProtectionProvisionProtectionEthIndex_Object = MibTableColumn
flowProtectionProvisionProtectionEthIndex = _FlowProtectionProvisionProtectionEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1, 4),
    _FlowProtectionProvisionProtectionEthIndex_Type()
)
flowProtectionProvisionProtectionEthIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowProtectionProvisionProtectionEthIndex.setStatus("current")
_FlowProtectionProvisionProtectionFlwIndex_Type = Unsigned32
_FlowProtectionProvisionProtectionFlwIndex_Object = MibTableColumn
flowProtectionProvisionProtectionFlwIndex = _FlowProtectionProvisionProtectionFlwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1, 5),
    _FlowProtectionProvisionProtectionFlwIndex_Type()
)
flowProtectionProvisionProtectionFlwIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowProtectionProvisionProtectionFlwIndex.setStatus("current")
_FlowProtectionProvisionProtectionMech_Type = ProtectionMech
_FlowProtectionProvisionProtectionMech_Object = MibTableColumn
flowProtectionProvisionProtectionMech = _FlowProtectionProvisionProtectionMech_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1, 6),
    _FlowProtectionProvisionProtectionMech_Type()
)
flowProtectionProvisionProtectionMech.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowProtectionProvisionProtectionMech.setStatus("current")
_FlowProtectionProvisionRevertiveMode_Type = ApsRevertMode
_FlowProtectionProvisionRevertiveMode_Object = MibTableColumn
flowProtectionProvisionRevertiveMode = _FlowProtectionProvisionRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1, 7),
    _FlowProtectionProvisionRevertiveMode_Type()
)
flowProtectionProvisionRevertiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowProtectionProvisionRevertiveMode.setStatus("current")
_FlowProtectionProvisionBridge_Type = FspR7L2Brigde
_FlowProtectionProvisionBridge_Object = MibTableColumn
flowProtectionProvisionBridge = _FlowProtectionProvisionBridge_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1, 8),
    _FlowProtectionProvisionBridge_Type()
)
flowProtectionProvisionBridge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowProtectionProvisionBridge.setStatus("obsolete")
_FlowProtectionProvisionLevelDomainMonitored_Type = FspR7L2LevelDomainMonitored
_FlowProtectionProvisionLevelDomainMonitored_Object = MibTableColumn
flowProtectionProvisionLevelDomainMonitored = _FlowProtectionProvisionLevelDomainMonitored_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1, 9),
    _FlowProtectionProvisionLevelDomainMonitored_Type()
)
flowProtectionProvisionLevelDomainMonitored.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowProtectionProvisionLevelDomainMonitored.setStatus("current")
_FlowProtectionProvisionBridgeType_Type = FspR7Brigde
_FlowProtectionProvisionBridgeType_Object = MibTableColumn
flowProtectionProvisionBridgeType = _FlowProtectionProvisionBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 13, 1, 10),
    _FlowProtectionProvisionBridgeType_Type()
)
flowProtectionProvisionBridgeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    flowProtectionProvisionBridgeType.setStatus("current")
_FlowProtectionProvisionCapTable_Object = MibTable
flowProtectionProvisionCapTable = _FlowProtectionProvisionCapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14)
)
if mibBuilder.loadTexts:
    flowProtectionProvisionCapTable.setStatus("current")
_FlowProtectionProvisionCapEntry_Object = MibTableRow
flowProtectionProvisionCapEntry = _FlowProtectionProvisionCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1)
)
flowProtectionProvisionCapEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowProtectionProvisionCapEntry.setStatus("current")
_FlowProtectionProvisionCapRowStatus_Type = FspR7RowStatusCaps
_FlowProtectionProvisionCapRowStatus_Object = MibTableColumn
flowProtectionProvisionCapRowStatus = _FlowProtectionProvisionCapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1, 1),
    _FlowProtectionProvisionCapRowStatus_Type()
)
flowProtectionProvisionCapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionCapRowStatus.setStatus("current")
_FlowProtectionProvisionCapWorkingEthIndex_Type = Integer32
_FlowProtectionProvisionCapWorkingEthIndex_Object = MibTableColumn
flowProtectionProvisionCapWorkingEthIndex = _FlowProtectionProvisionCapWorkingEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1, 2),
    _FlowProtectionProvisionCapWorkingEthIndex_Type()
)
flowProtectionProvisionCapWorkingEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionCapWorkingEthIndex.setStatus("current")
_FlowProtectionProvisionCapWorkingFlwIndex_Type = FspR7Unsigned32Caps
_FlowProtectionProvisionCapWorkingFlwIndex_Object = MibTableColumn
flowProtectionProvisionCapWorkingFlwIndex = _FlowProtectionProvisionCapWorkingFlwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1, 3),
    _FlowProtectionProvisionCapWorkingFlwIndex_Type()
)
flowProtectionProvisionCapWorkingFlwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionCapWorkingFlwIndex.setStatus("current")
_FlowProtectionProvisionCapProtectionEthIndex_Type = Integer32
_FlowProtectionProvisionCapProtectionEthIndex_Object = MibTableColumn
flowProtectionProvisionCapProtectionEthIndex = _FlowProtectionProvisionCapProtectionEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1, 4),
    _FlowProtectionProvisionCapProtectionEthIndex_Type()
)
flowProtectionProvisionCapProtectionEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionCapProtectionEthIndex.setStatus("current")
_FlowProtectionProvisionCapProtectionFlwIndex_Type = FspR7Unsigned32Caps
_FlowProtectionProvisionCapProtectionFlwIndex_Object = MibTableColumn
flowProtectionProvisionCapProtectionFlwIndex = _FlowProtectionProvisionCapProtectionFlwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1, 5),
    _FlowProtectionProvisionCapProtectionFlwIndex_Type()
)
flowProtectionProvisionCapProtectionFlwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionCapProtectionFlwIndex.setStatus("current")
_FlowProtectionProvisionCapProtectionMech_Type = ProtectionMechCaps
_FlowProtectionProvisionCapProtectionMech_Object = MibTableColumn
flowProtectionProvisionCapProtectionMech = _FlowProtectionProvisionCapProtectionMech_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1, 6),
    _FlowProtectionProvisionCapProtectionMech_Type()
)
flowProtectionProvisionCapProtectionMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionCapProtectionMech.setStatus("current")
_FlowProtectionProvisionCapRevertiveMode_Type = ApsRevertModeCaps
_FlowProtectionProvisionCapRevertiveMode_Object = MibTableColumn
flowProtectionProvisionCapRevertiveMode = _FlowProtectionProvisionCapRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1, 7),
    _FlowProtectionProvisionCapRevertiveMode_Type()
)
flowProtectionProvisionCapRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionCapRevertiveMode.setStatus("current")
_FlowProtectionProvisionCapBridge_Type = FspR7L2BrigdeCaps
_FlowProtectionProvisionCapBridge_Object = MibTableColumn
flowProtectionProvisionCapBridge = _FlowProtectionProvisionCapBridge_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1, 8),
    _FlowProtectionProvisionCapBridge_Type()
)
flowProtectionProvisionCapBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionCapBridge.setStatus("obsolete")
_FlowProtectionProvisionCapLevelDomainMonitored_Type = FspR7L2LevelDomainMonitoredCaps
_FlowProtectionProvisionCapLevelDomainMonitored_Object = MibTableColumn
flowProtectionProvisionCapLevelDomainMonitored = _FlowProtectionProvisionCapLevelDomainMonitored_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1, 9),
    _FlowProtectionProvisionCapLevelDomainMonitored_Type()
)
flowProtectionProvisionCapLevelDomainMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionCapLevelDomainMonitored.setStatus("current")
_FlowProtectionProvisionCapBridgeType_Type = FspR7BrigdeCaps
_FlowProtectionProvisionCapBridgeType_Object = MibTableColumn
flowProtectionProvisionCapBridgeType = _FlowProtectionProvisionCapBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 14, 1, 10),
    _FlowProtectionProvisionCapBridgeType_Type()
)
flowProtectionProvisionCapBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionCapBridgeType.setStatus("current")
_FlowProtectionProvisionDefaultsTable_Object = MibTable
flowProtectionProvisionDefaultsTable = _FlowProtectionProvisionDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15)
)
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsTable.setStatus("current")
_FlowProtectionProvisionDefaultsEntry_Object = MibTableRow
flowProtectionProvisionDefaultsEntry = _FlowProtectionProvisionDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1)
)
flowProtectionProvisionDefaultsEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsEntry.setStatus("current")
_FlowProtectionProvisionDefaultsRowStatus_Type = RowStatus
_FlowProtectionProvisionDefaultsRowStatus_Object = MibTableColumn
flowProtectionProvisionDefaultsRowStatus = _FlowProtectionProvisionDefaultsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1, 1),
    _FlowProtectionProvisionDefaultsRowStatus_Type()
)
flowProtectionProvisionDefaultsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsRowStatus.setStatus("current")
_FlowProtectionProvisionDefaultsWorkingEthIndex_Type = EntityIndex
_FlowProtectionProvisionDefaultsWorkingEthIndex_Object = MibTableColumn
flowProtectionProvisionDefaultsWorkingEthIndex = _FlowProtectionProvisionDefaultsWorkingEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1, 2),
    _FlowProtectionProvisionDefaultsWorkingEthIndex_Type()
)
flowProtectionProvisionDefaultsWorkingEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsWorkingEthIndex.setStatus("current")
_FlowProtectionProvisionDefaultsWorkingFlwIndex_Type = Unsigned32
_FlowProtectionProvisionDefaultsWorkingFlwIndex_Object = MibTableColumn
flowProtectionProvisionDefaultsWorkingFlwIndex = _FlowProtectionProvisionDefaultsWorkingFlwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1, 3),
    _FlowProtectionProvisionDefaultsWorkingFlwIndex_Type()
)
flowProtectionProvisionDefaultsWorkingFlwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsWorkingFlwIndex.setStatus("current")
_FlowProtectionProvisionDefaultsProtectionEthIndex_Type = EntityIndex
_FlowProtectionProvisionDefaultsProtectionEthIndex_Object = MibTableColumn
flowProtectionProvisionDefaultsProtectionEthIndex = _FlowProtectionProvisionDefaultsProtectionEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1, 4),
    _FlowProtectionProvisionDefaultsProtectionEthIndex_Type()
)
flowProtectionProvisionDefaultsProtectionEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsProtectionEthIndex.setStatus("current")
_FlowProtectionProvisionDefaultsProtectionFlwIndex_Type = Unsigned32
_FlowProtectionProvisionDefaultsProtectionFlwIndex_Object = MibTableColumn
flowProtectionProvisionDefaultsProtectionFlwIndex = _FlowProtectionProvisionDefaultsProtectionFlwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1, 5),
    _FlowProtectionProvisionDefaultsProtectionFlwIndex_Type()
)
flowProtectionProvisionDefaultsProtectionFlwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsProtectionFlwIndex.setStatus("current")
_FlowProtectionProvisionDefaultsProtectionMech_Type = ProtectionMech
_FlowProtectionProvisionDefaultsProtectionMech_Object = MibTableColumn
flowProtectionProvisionDefaultsProtectionMech = _FlowProtectionProvisionDefaultsProtectionMech_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1, 6),
    _FlowProtectionProvisionDefaultsProtectionMech_Type()
)
flowProtectionProvisionDefaultsProtectionMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsProtectionMech.setStatus("current")
_FlowProtectionProvisionDefaultsRevertiveMode_Type = ApsRevertMode
_FlowProtectionProvisionDefaultsRevertiveMode_Object = MibTableColumn
flowProtectionProvisionDefaultsRevertiveMode = _FlowProtectionProvisionDefaultsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1, 7),
    _FlowProtectionProvisionDefaultsRevertiveMode_Type()
)
flowProtectionProvisionDefaultsRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsRevertiveMode.setStatus("current")
_FlowProtectionProvisionDefaultsBridge_Type = FspR7L2Brigde
_FlowProtectionProvisionDefaultsBridge_Object = MibTableColumn
flowProtectionProvisionDefaultsBridge = _FlowProtectionProvisionDefaultsBridge_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1, 8),
    _FlowProtectionProvisionDefaultsBridge_Type()
)
flowProtectionProvisionDefaultsBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsBridge.setStatus("obsolete")
_FlowProtectionProvisionDefaultsLevelDomainMonitored_Type = FspR7L2LevelDomainMonitored
_FlowProtectionProvisionDefaultsLevelDomainMonitored_Object = MibTableColumn
flowProtectionProvisionDefaultsLevelDomainMonitored = _FlowProtectionProvisionDefaultsLevelDomainMonitored_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1, 9),
    _FlowProtectionProvisionDefaultsLevelDomainMonitored_Type()
)
flowProtectionProvisionDefaultsLevelDomainMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsLevelDomainMonitored.setStatus("current")
_FlowProtectionProvisionDefaultsBridgeType_Type = FspR7Brigde
_FlowProtectionProvisionDefaultsBridgeType_Object = MibTableColumn
flowProtectionProvisionDefaultsBridgeType = _FlowProtectionProvisionDefaultsBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 15, 1, 10),
    _FlowProtectionProvisionDefaultsBridgeType_Type()
)
flowProtectionProvisionDefaultsBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionDefaultsBridgeType.setStatus("current")
_FlowProtectionProvisionProtectionAidCapsTable_Object = MibTable
flowProtectionProvisionProtectionAidCapsTable = _FlowProtectionProvisionProtectionAidCapsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 16)
)
if mibBuilder.loadTexts:
    flowProtectionProvisionProtectionAidCapsTable.setStatus("current")
_FlowProtectionProvisionProtectionAidCapsEntry_Object = MibTableRow
flowProtectionProvisionProtectionAidCapsEntry = _FlowProtectionProvisionProtectionAidCapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 16, 1)
)
flowProtectionProvisionProtectionAidCapsEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowProtectionProvisionProtectionAidCapsEntry.setStatus("current")
_FlowProtectionProvisionProtectionAidCapsIndex_Type = EntityIndex
_FlowProtectionProvisionProtectionAidCapsIndex_Object = MibTableColumn
flowProtectionProvisionProtectionAidCapsIndex = _FlowProtectionProvisionProtectionAidCapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 16, 1, 1),
    _FlowProtectionProvisionProtectionAidCapsIndex_Type()
)
flowProtectionProvisionProtectionAidCapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionProvisionProtectionAidCapsIndex.setStatus("current")
_FlowProtectionStatusTable_Object = MibTable
flowProtectionStatusTable = _FlowProtectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23)
)
if mibBuilder.loadTexts:
    flowProtectionStatusTable.setStatus("current")
_FlowProtectionStatusEntry_Object = MibTableRow
flowProtectionStatusEntry = _FlowProtectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1)
)
flowProtectionStatusEntry.setIndexNames(
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexEth"),
    (0, "FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
)
if mibBuilder.loadTexts:
    flowProtectionStatusEntry.setStatus("current")
_FlowProtectionStatusWorkingEthIndex_Type = EntityIndex
_FlowProtectionStatusWorkingEthIndex_Object = MibTableColumn
flowProtectionStatusWorkingEthIndex = _FlowProtectionStatusWorkingEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 1),
    _FlowProtectionStatusWorkingEthIndex_Type()
)
flowProtectionStatusWorkingEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusWorkingEthIndex.setStatus("current")
_FlowProtectionStatusWorkingFlwIndex_Type = Unsigned32
_FlowProtectionStatusWorkingFlwIndex_Object = MibTableColumn
flowProtectionStatusWorkingFlwIndex = _FlowProtectionStatusWorkingFlwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 2),
    _FlowProtectionStatusWorkingFlwIndex_Type()
)
flowProtectionStatusWorkingFlwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusWorkingFlwIndex.setStatus("current")
_FlowProtectionStatusProtectionEthIndex_Type = EntityIndex
_FlowProtectionStatusProtectionEthIndex_Object = MibTableColumn
flowProtectionStatusProtectionEthIndex = _FlowProtectionStatusProtectionEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 3),
    _FlowProtectionStatusProtectionEthIndex_Type()
)
flowProtectionStatusProtectionEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusProtectionEthIndex.setStatus("current")
_FlowProtectionStatusProtectionFlwIndex_Type = Unsigned32
_FlowProtectionStatusProtectionFlwIndex_Object = MibTableColumn
flowProtectionStatusProtectionFlwIndex = _FlowProtectionStatusProtectionFlwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 4),
    _FlowProtectionStatusProtectionFlwIndex_Type()
)
flowProtectionStatusProtectionFlwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusProtectionFlwIndex.setStatus("current")
_FlowProtectionStatusApsType_Type = ApsType
_FlowProtectionStatusApsType_Object = MibTableColumn
flowProtectionStatusApsType = _FlowProtectionStatusApsType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 5),
    _FlowProtectionStatusApsType_Type()
)
flowProtectionStatusApsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusApsType.setStatus("current")
_FlowProtectionStatusProtectionType_Type = FspR7ProtectionType
_FlowProtectionStatusProtectionType_Object = MibTableColumn
flowProtectionStatusProtectionType = _FlowProtectionStatusProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 6),
    _FlowProtectionStatusProtectionType_Type()
)
flowProtectionStatusProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusProtectionType.setStatus("current")
_FlowProtectionStatusProtectionMech_Type = ProtectionMech
_FlowProtectionStatusProtectionMech_Object = MibTableColumn
flowProtectionStatusProtectionMech = _FlowProtectionStatusProtectionMech_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 7),
    _FlowProtectionStatusProtectionMech_Type()
)
flowProtectionStatusProtectionMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusProtectionMech.setStatus("current")
_FlowProtectionStatusDirection_Type = ApsDirection
_FlowProtectionStatusDirection_Object = MibTableColumn
flowProtectionStatusDirection = _FlowProtectionStatusDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 8),
    _FlowProtectionStatusDirection_Type()
)
flowProtectionStatusDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusDirection.setStatus("current")
_FlowProtectionStatusRevertiveMode_Type = ApsRevertMode
_FlowProtectionStatusRevertiveMode_Object = MibTableColumn
flowProtectionStatusRevertiveMode = _FlowProtectionStatusRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 9),
    _FlowProtectionStatusRevertiveMode_Type()
)
flowProtectionStatusRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusRevertiveMode.setStatus("current")
_FlowProtectionStatusBridge_Type = FspR7L2Brigde
_FlowProtectionStatusBridge_Object = MibTableColumn
flowProtectionStatusBridge = _FlowProtectionStatusBridge_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 10),
    _FlowProtectionStatusBridge_Type()
)
flowProtectionStatusBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusBridge.setStatus("obsolete")
_FlowProtectionStatusLevelDomainMonitored_Type = FspR7L2LevelDomainMonitored
_FlowProtectionStatusLevelDomainMonitored_Object = MibTableColumn
flowProtectionStatusLevelDomainMonitored = _FlowProtectionStatusLevelDomainMonitored_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 11),
    _FlowProtectionStatusLevelDomainMonitored_Type()
)
flowProtectionStatusLevelDomainMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusLevelDomainMonitored.setStatus("current")
_FlowProtectionStatusBridgeType_Type = FspR7L2Brigde
_FlowProtectionStatusBridgeType_Object = MibTableColumn
flowProtectionStatusBridgeType = _FlowProtectionStatusBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 18, 23, 1, 12),
    _FlowProtectionStatusBridgeType_Type()
)
flowProtectionStatusBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowProtectionStatusBridgeType.setStatus("current")

# Managed Objects groups


# Notification objects

alarmOosDisabledL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100000)
)
alarmOosDisabledL2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmOosDisabledL2.setStatus(
        "current"
    )

alarmOosManagementL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100001)
)
alarmOosManagementL2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmOosManagementL2.setStatus(
        "current"
    )

alarmOosMaintenanceL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100002)
)
alarmOosMaintenanceL2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmOosMaintenanceL2.setStatus(
        "current"
    )

alarmOosAinsL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100003)
)
alarmOosAinsL2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmOosAinsL2.setStatus(
        "current"
    )

alarmServerSignalFailL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100004)
)
alarmServerSignalFailL2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmServerSignalFailL2.setStatus(
        "current"
    )

alarmMepNotPresentL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100005)
)
alarmMepNotPresentL2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmMepNotPresentL2.setStatus(
        "current"
    )

alarmPriVidNotEqualExtVidL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100006)
)
alarmPriVidNotEqualExtVidL2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmPriVidNotEqualExtVidL2.setStatus(
        "current"
    )

alarmSwitchtoProtectionInhibitedL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100007)
)
alarmSwitchtoProtectionInhibitedL2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmSwitchtoProtectionInhibitedL2.setStatus(
        "current"
    )

alarmManswL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100008)
)
alarmManswL2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmManswL2.setStatus(
        "current"
    )

alarmSfCfmLevel0L2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100009)
)
alarmSfCfmLevel0L2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmSfCfmLevel0L2.setStatus(
        "current"
    )

alarmSfCfmLevel1L2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100010)
)
alarmSfCfmLevel1L2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmSfCfmLevel1L2.setStatus(
        "current"
    )

alarmSfCfmLevel2L2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100011)
)
alarmSfCfmLevel2L2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmSfCfmLevel2L2.setStatus(
        "current"
    )

alarmSfCfmLevel3L2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100012)
)
alarmSfCfmLevel3L2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmSfCfmLevel3L2.setStatus(
        "current"
    )

alarmSfCfmLevel4L2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100013)
)
alarmSfCfmLevel4L2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmSfCfmLevel4L2.setStatus(
        "current"
    )

alarmSfCfmLevel5L2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100014)
)
alarmSfCfmLevel5L2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmSfCfmLevel5L2.setStatus(
        "current"
    )

alarmSfCfmLevel6L2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100015)
)
alarmSfCfmLevel6L2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmSfCfmLevel6L2.setStatus(
        "current"
    )

alarmSfCfmLevel7L2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100016)
)
alarmSfCfmLevel7L2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmSfCfmLevel7L2.setStatus(
        "current"
    )

alarmBridgeOosManagement = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100017)
)
alarmBridgeOosManagement.setObjects(
      *(("FspR7-LAYER2-MIB", "bridgeCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "bridgeCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmBridgeOosManagement.setStatus(
        "current"
    )

alarmBridgeOosAins = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100018)
)
alarmBridgeOosAins.setObjects(
      *(("FspR7-LAYER2-MIB", "bridgeCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "bridgeCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmBridgeOosAins.setStatus(
        "current"
    )

alarmSwitchtoWorkingInhibitedL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 100019)
)
alarmSwitchtoWorkingInhibitedL2.setObjects(
      *(("FspR7-LAYER2-MIB", "flowCurrentConditionSeverity"),
        ("FspR7-LAYER2-MIB", "flowCurrentConditionAffect"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    alarmSwitchtoWorkingInhibitedL2.setStatus(
        "current"
    )

flowEntityCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110001)
)
flowEntityCreation.setObjects(
      *(("FspR7-LAYER2-MIB", "flowEntityIndexEth"),
        ("FspR7-LAYER2-MIB", "flowEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    flowEntityCreation.setStatus(
        "current"
    )

ctransEntityCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110002)
)
ctransEntityCreation.setObjects(
      *(("FspR7-LAYER2-MIB", "ctransEntityIndexEth"),
        ("FspR7-LAYER2-MIB", "ctransEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    ctransEntityCreation.setStatus(
        "current"
    )

bridgeEntityCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110003)
)
bridgeEntityCreation.setObjects(
      *(("FspR7-LAYER2-MIB", "bridgeEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    bridgeEntityCreation.setStatus(
        "current"
    )

flowEntityDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110008)
)
flowEntityDeletion.setObjects(
      *(("FspR7-LAYER2-MIB", "flowEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    flowEntityDeletion.setStatus(
        "current"
    )

ctransEntityDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110009)
)
ctransEntityDeletion.setObjects(
      *(("FspR7-LAYER2-MIB", "ctransEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    ctransEntityDeletion.setStatus(
        "current"
    )

bridgeEntityDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110010)
)
bridgeEntityDeletion.setObjects(
      *(("FspR7-LAYER2-MIB", "bridgeEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    bridgeEntityDeletion.setStatus(
        "current"
    )

layer2EntityStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110015)
)
layer2EntityStateChange.setObjects(
      *(("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    layer2EntityStateChange.setStatus(
        "current"
    )

flowEntityObjectChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110016)
)
flowEntityObjectChange.setObjects(
      *(("FspR7-LAYER2-MIB", "flowEntityIndexEth"),
        ("FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
        ("FspR7-LAYER2-MIB", "flowEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    flowEntityObjectChange.setStatus(
        "current"
    )

ctransEntityObjectChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110017)
)
ctransEntityObjectChange.setObjects(
      *(("FspR7-LAYER2-MIB", "ctransEntityIndexEth"),
        ("FspR7-LAYER2-MIB", "ctransEntityIndexCVlanId"),
        ("FspR7-LAYER2-MIB", "ctransEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    ctransEntityObjectChange.setStatus(
        "current"
    )

bridgeEntityObjectChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110018)
)
bridgeEntityObjectChange.setObjects(
      *(("FspR7-LAYER2-MIB", "bridgeEntityContainedIn"),
        ("FspR7-LAYER2-MIB", "bridgeEntitySvid"),
        ("FspR7-LAYER2-MIB", "bridgeEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    bridgeEntityObjectChange.setStatus(
        "current"
    )

crossConnectionCreationLayer2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110030)
)
crossConnectionCreationLayer2.setObjects(
      *(("FspR7-LAYER2-MIB", "crossConnectionsStatusFromEth"),
        ("FspR7-LAYER2-MIB", "crossConnectionsStatusToEth"),
        ("FspR7-LAYER2-MIB", "crossConnectionsProvisioningConn"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    crossConnectionCreationLayer2.setStatus(
        "current"
    )

crossConnectionDeletionLayer2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110031)
)
crossConnectionDeletionLayer2.setObjects(
      *(("FspR7-LAYER2-MIB", "crossConnectionsStatusFromEth"),
        ("FspR7-LAYER2-MIB", "crossConnectionsStatusToEth"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    crossConnectionDeletionLayer2.setStatus(
        "current"
    )

crossConnectionObjectChangeLayer2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110032)
)
crossConnectionObjectChangeLayer2.setObjects(
      *(("FspR7-LAYER2-MIB", "crossConnectionsStatusFromEth"),
        ("FspR7-LAYER2-MIB", "crossConnectionsStatusToEth"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    crossConnectionObjectChangeLayer2.setStatus(
        "current"
    )

ffpFlowEntityCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110033)
)
ffpFlowEntityCreation.setObjects(
      *(("FspR7-LAYER2-MIB", "flowEntityIndexEth"),
        ("FspR7-LAYER2-MIB", "flowProtectionAssignedEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    ffpFlowEntityCreation.setStatus(
        "current"
    )

ffpFlowEntityDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110034)
)
ffpFlowEntityDeletion.setObjects(
      *(("FspR7-LAYER2-MIB", "flowProtectionAssignedEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    ffpFlowEntityDeletion.setStatus(
        "current"
    )

ffpFlowEntityObjectChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 110035)
)
ffpFlowEntityObjectChange.setObjects(
      *(("FspR7-LAYER2-MIB", "flowEntityIndexEth"),
        ("FspR7-LAYER2-MIB", "flowEntityIndexFlow"),
        ("FspR7-LAYER2-MIB", "flowProtectionAssignedEntityClass"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    ffpFlowEntityObjectChange.setStatus(
        "current"
    )

transientWorkingSwitchedtoProtectionL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 111001)
)
transientWorkingSwitchedtoProtectionL2.setObjects(
      *(("ADVA-MIB", "entityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientWorkingSwitchedtoProtectionL2.setStatus(
        "current"
    )

transientWorkingSwitchedBacktoWorkingL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 111002)
)
transientWorkingSwitchedBacktoWorkingL2.setObjects(
      *(("ADVA-MIB", "entityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientWorkingSwitchedBacktoWorkingL2.setStatus(
        "current"
    )

transientManualWorkingSwitchedtoProtectionL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 111003)
)
transientManualWorkingSwitchedtoProtectionL2.setObjects(
      *(("ADVA-MIB", "entityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientManualWorkingSwitchedtoProtectionL2.setStatus(
        "current"
    )

transientManualWorkingSwitchedBacktoWorkingL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 11, 3, 17, 1, 0, 111004)
)
transientManualWorkingSwitchedBacktoWorkingL2.setObjects(
      *(("ADVA-MIB", "entityIndex"),
        ("ADVA-MIB", "neEventLogTimeStamp"),
        ("ADVA-MIB", "neEventLogIdentityTranslation"))
)
if mibBuilder.loadTexts:
    transientManualWorkingSwitchedBacktoWorkingL2.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FspR7-LAYER2-MIB",
    **{"BridgeEntityIndex": BridgeEntityIndex,
       "FspR7DisableEnable": FspR7DisableEnable,
       "FspR7DisableEnableCaps": FspR7DisableEnableCaps,
       "FspR7Brigde": FspR7Brigde,
       "FspR7BrigdeCaps": FspR7BrigdeCaps,
       "FspR7L2Brigde": FspR7L2Brigde,
       "FspR7L2BrigdeCaps": FspR7L2BrigdeCaps,
       "FspR7L2FlowType": FspR7L2FlowType,
       "FspR7L2FlowTypeCaps": FspR7L2FlowTypeCaps,
       "FspR7L2LevelDomainMonitored": FspR7L2LevelDomainMonitored,
       "FspR7L2LevelDomainMonitoredCaps": FspR7L2LevelDomainMonitoredCaps,
       "FspR7L2PmMode": FspR7L2PmMode,
       "FspR7L2PmModeCaps": FspR7L2PmModeCaps,
       "FspR7L2StandingConditionTypes": FspR7L2StandingConditionTypes,
       "BridgeStandingConditionTypes": BridgeStandingConditionTypes,
       "FspR7RedLinedState": FspR7RedLinedState,
       "FspR7RedLinedStateCaps": FspR7RedLinedStateCaps,
       "QueueEntityIndex": QueueEntityIndex,
       "layer2MIB": layer2MIB,
       "layer2EntitiesMIB": layer2EntitiesMIB,
       "flowEntityTable": flowEntityTable,
       "flowEntityEntry": flowEntityEntry,
       "flowEntityIndexEth": flowEntityIndexEth,
       "flowEntityIndexFlow": flowEntityIndexFlow,
       "flowEntityClass": flowEntityClass,
       "flowEntityClassInstanceNumber": flowEntityClassInstanceNumber,
       "flowEntityIndexAid": flowEntityIndexAid,
       "ctransEntityTable": ctransEntityTable,
       "ctransEntityEntry": ctransEntityEntry,
       "ctransEntityIndexEth": ctransEntityIndexEth,
       "ctransEntityIndexCVlanId": ctransEntityIndexCVlanId,
       "ctransEntityClass": ctransEntityClass,
       "ctransEntityClassInstanceNumber": ctransEntityClassInstanceNumber,
       "ctransEntityIndexAid": ctransEntityIndexAid,
       "bridgeEntityTable": bridgeEntityTable,
       "bridgeEntityEntry": bridgeEntityEntry,
       "bridgeEntityContainedIn": bridgeEntityContainedIn,
       "bridgeEntitySvid": bridgeEntitySvid,
       "bridgeEntityClass": bridgeEntityClass,
       "bridgeEntityClassInstanceNumber": bridgeEntityClassInstanceNumber,
       "bridgeEntityIndexAid": bridgeEntityIndexAid,
       "policerOnFlowEntityTable": policerOnFlowEntityTable,
       "policerOnFlowEntityEntry": policerOnFlowEntityEntry,
       "policerOnFlowEntityIndexEth": policerOnFlowEntityIndexEth,
       "policerOnFlowEntityIndexFlow": policerOnFlowEntityIndexFlow,
       "policerOnFlowEntityIndexPolicer": policerOnFlowEntityIndexPolicer,
       "policerOnFlowEntityClass": policerOnFlowEntityClass,
       "policerOnFlowEntityClassInstanceNumber": policerOnFlowEntityClassInstanceNumber,
       "policerOnFlowEntityIndexAid": policerOnFlowEntityIndexAid,
       "queOnPortEntityTable": queOnPortEntityTable,
       "queOnPortEntityEntry": queOnPortEntityEntry,
       "queOnPortEntityIndexEth": queOnPortEntityIndexEth,
       "queOnPortEntityIndexPrio": queOnPortEntityIndexPrio,
       "queOnPortEntityClass": queOnPortEntityClass,
       "queOnPortEntityClassInstanceNumber": queOnPortEntityClassInstanceNumber,
       "queOnPortEntityIndexAid": queOnPortEntityIndexAid,
       "queOnFlowEntityTable": queOnFlowEntityTable,
       "queOnFlowEntityEntry": queOnFlowEntityEntry,
       "queOnFlowEntityIndexEth": queOnFlowEntityIndexEth,
       "queOnFlowEntityIndexFlow": queOnFlowEntityIndexFlow,
       "queOnFlowEntityIndexPrio": queOnFlowEntityIndexPrio,
       "queOnFlowEntityClass": queOnFlowEntityClass,
       "queOnFlowEntityClassInstanceNumber": queOnFlowEntityClassInstanceNumber,
       "queOnFlowEntityIndexAid": queOnFlowEntityIndexAid,
       "queOnBridgeEntityTable": queOnBridgeEntityTable,
       "queOnBridgeEntityEntry": queOnBridgeEntityEntry,
       "queOnBridgeEntityIndex": queOnBridgeEntityIndex,
       "queOnBridgeEntitySvid": queOnBridgeEntitySvid,
       "queOnBridgeEntityPrio": queOnBridgeEntityPrio,
       "queOnBridgeEntityClass": queOnBridgeEntityClass,
       "queOnBridgeEntityClassInstanceNumber": queOnBridgeEntityClassInstanceNumber,
       "queOnBridgeEntityIndexAid": queOnBridgeEntityIndexAid,
       "layer2ProvisioningMIB": layer2ProvisioningMIB,
       "flowProvisioning": flowProvisioning,
       "flowEntityProvisionTable": flowEntityProvisionTable,
       "flowEntityProvisionEntry": flowEntityProvisionEntry,
       "flowEntityProvisionRowStatus": flowEntityProvisionRowStatus,
       "flowEntityProvisionType": flowEntityProvisionType,
       "flowEntityProvisionAdmin": flowEntityProvisionAdmin,
       "flowEntityProvisionAlias": flowEntityProvisionAlias,
       "flowEntityProvisionPopCtagRcv": flowEntityProvisionPopCtagRcv,
       "flowEntityProvisionPopCtagTrmt": flowEntityProvisionPopCtagTrmt,
       "flowEntityProvisionCvidRegisteredInFlow": flowEntityProvisionCvidRegisteredInFlow,
       "flowEntityProvisionExternalVid": flowEntityProvisionExternalVid,
       "flowEntityProvisionPmMode": flowEntityProvisionPmMode,
       "flowEntityProvisionShape": flowEntityProvisionShape,
       "flowEntityProvisionPolice": flowEntityProvisionPolice,
       "flowEntityProvisionDefaultEvcCos": flowEntityProvisionDefaultEvcCos,
       "flowEntityProvisionCirRcv": flowEntityProvisionCirRcv,
       "flowEntityProvisionCirTrmt": flowEntityProvisionCirTrmt,
       "flowEntityProvisionCbsRcv": flowEntityProvisionCbsRcv,
       "flowEntityProvisionCbsTrmt": flowEntityProvisionCbsTrmt,
       "flowEntityProvisionPushPvidTrmt": flowEntityProvisionPushPvidTrmt,
       "flowEntityProvisionPrioPvidTrmt": flowEntityProvisionPrioPvidTrmt,
       "flowEntityProvisionRedLineState": flowEntityProvisionRedLineState,
       "flowEntityProvisionTunnelAid": flowEntityProvisionTunnelAid,
       "flowEntityProvisionCapTable": flowEntityProvisionCapTable,
       "flowEntityProvisionCapEntry": flowEntityProvisionCapEntry,
       "flowEntityProvisionCapRowStatus": flowEntityProvisionCapRowStatus,
       "flowEntityProvisionCapType": flowEntityProvisionCapType,
       "flowEntityProvisionCapAdmin": flowEntityProvisionCapAdmin,
       "flowEntityProvisionCapAlias": flowEntityProvisionCapAlias,
       "flowEntityProvisionCapPopCtagRcv": flowEntityProvisionCapPopCtagRcv,
       "flowEntityProvisionCapPopCtagTrmt": flowEntityProvisionCapPopCtagTrmt,
       "flowEntityProvisionCapCvidRegisteredInFlow": flowEntityProvisionCapCvidRegisteredInFlow,
       "flowEntityProvisionCapExternalVid": flowEntityProvisionCapExternalVid,
       "flowEntityProvisionCapPmMode": flowEntityProvisionCapPmMode,
       "flowEntityProvisionCapShape": flowEntityProvisionCapShape,
       "flowEntityProvisionCapPolice": flowEntityProvisionCapPolice,
       "flowEntityProvisionCapDefaultEvcCos": flowEntityProvisionCapDefaultEvcCos,
       "flowEntityProvisionCapCirRcv": flowEntityProvisionCapCirRcv,
       "flowEntityProvisionCapCirTrmt": flowEntityProvisionCapCirTrmt,
       "flowEntityProvisionCapCbsRcv": flowEntityProvisionCapCbsRcv,
       "flowEntityProvisionCapCbsTrmt": flowEntityProvisionCapCbsTrmt,
       "flowEntityProvisionCapPushPvidTrmt": flowEntityProvisionCapPushPvidTrmt,
       "flowEntityProvisionCapPrioPvidTrmt": flowEntityProvisionCapPrioPvidTrmt,
       "flowEntityProvisionCapRedLineState": flowEntityProvisionCapRedLineState,
       "flowEntityProvisionCapTunnelAid": flowEntityProvisionCapTunnelAid,
       "flowEntityProvisionDefaultsTable": flowEntityProvisionDefaultsTable,
       "flowEntityProvisionDefaultsEntry": flowEntityProvisionDefaultsEntry,
       "flowEntityProvisionDefaultsRowStatus": flowEntityProvisionDefaultsRowStatus,
       "flowEntityProvisionDefaultsType": flowEntityProvisionDefaultsType,
       "flowEntityProvisionDefaultsAdmin": flowEntityProvisionDefaultsAdmin,
       "flowEntityProvisionDefaultsAlias": flowEntityProvisionDefaultsAlias,
       "flowEntityProvisionDefaultsPopCtagRcv": flowEntityProvisionDefaultsPopCtagRcv,
       "flowEntityProvisionDefaultsPopCtagTrmt": flowEntityProvisionDefaultsPopCtagTrmt,
       "flowEntityProvisionDefaultsCvidRegisteredInFlow": flowEntityProvisionDefaultsCvidRegisteredInFlow,
       "flowEntityProvisionDefaultsExternalVid": flowEntityProvisionDefaultsExternalVid,
       "flowEntityProvisionDefaultsPmMode": flowEntityProvisionDefaultsPmMode,
       "flowEntityProvisionDefaultsShape": flowEntityProvisionDefaultsShape,
       "flowEntityProvisionDefaultsPolice": flowEntityProvisionDefaultsPolice,
       "flowEntityProvisionDefaultsDefaultEvcCos": flowEntityProvisionDefaultsDefaultEvcCos,
       "flowEntityProvisionDefaultsCirRcv": flowEntityProvisionDefaultsCirRcv,
       "flowEntityProvisionDefaultsCirTrmt": flowEntityProvisionDefaultsCirTrmt,
       "flowEntityProvisionDefaultsCbsRcv": flowEntityProvisionDefaultsCbsRcv,
       "flowEntityProvisionDefaultsCbsTrmt": flowEntityProvisionDefaultsCbsTrmt,
       "flowEntityProvisionDefaultsPushPvidTrmt": flowEntityProvisionDefaultsPushPvidTrmt,
       "flowEntityProvisionDefaultsPrioPvidTrmt": flowEntityProvisionDefaultsPrioPvidTrmt,
       "flowEntityProvisionDefaultsRedLineState": flowEntityProvisionDefaultsRedLineState,
       "flowEntityProvisionDefaultsTunnelAid": flowEntityProvisionDefaultsTunnelAid,
       "flowEntityProvisionCbsRcvCapTable": flowEntityProvisionCbsRcvCapTable,
       "flowEntityProvisionCbsRcvCapEntry": flowEntityProvisionCbsRcvCapEntry,
       "flowEntityProvisionCbsRcvCapIndexCap": flowEntityProvisionCbsRcvCapIndexCap,
       "flowEntityProvisionCbsRcvCapCbsRcv": flowEntityProvisionCbsRcvCapCbsRcv,
       "flowEntityProvisionRegisterCapTable": flowEntityProvisionRegisterCapTable,
       "flowEntityProvisionRegisterCapEntry": flowEntityProvisionRegisterCapEntry,
       "flowEntityProvisionRegisterCapIndexCap": flowEntityProvisionRegisterCapIndexCap,
       "flowEntityProvisionRegisterCapStringCap": flowEntityProvisionRegisterCapStringCap,
       "flowEntityProvisionExternalVidCapTable": flowEntityProvisionExternalVidCapTable,
       "flowEntityProvisionExternalVidCapEntry": flowEntityProvisionExternalVidCapEntry,
       "flowEntityProvisionExternalVidCapIndexCap": flowEntityProvisionExternalVidCapIndexCap,
       "flowEntityProvisionExternalVidCapStringCap": flowEntityProvisionExternalVidCapStringCap,
       "flowEntityProvisionPopCtagRcvCapTable": flowEntityProvisionPopCtagRcvCapTable,
       "flowEntityProvisionPopCtagRcvCapEntry": flowEntityProvisionPopCtagRcvCapEntry,
       "flowEntityProvisionPopCtagRcvCapIndexCap": flowEntityProvisionPopCtagRcvCapIndexCap,
       "flowEntityProvisionPopCtagRcvCapStringCap": flowEntityProvisionPopCtagRcvCapStringCap,
       "flowEntityProvisionPopCtagTrmtCapTable": flowEntityProvisionPopCtagTrmtCapTable,
       "flowEntityProvisionPopCtagTrmtCapEntry": flowEntityProvisionPopCtagTrmtCapEntry,
       "flowEntityProvisionPopCtagTrmtCapIndexCap": flowEntityProvisionPopCtagTrmtCapIndexCap,
       "flowEntityProvisionPopCtagTrmtCapStringCap": flowEntityProvisionPopCtagTrmtCapStringCap,
       "flowEntityProvisionPushTrmtCapTable": flowEntityProvisionPushTrmtCapTable,
       "flowEntityProvisionPushTrmtCapEntry": flowEntityProvisionPushTrmtCapEntry,
       "flowEntityProvisionPushTrmtCapIndexCap": flowEntityProvisionPushTrmtCapIndexCap,
       "flowEntityProvisionPushTrmtCapStringCap": flowEntityProvisionPushTrmtCapStringCap,
       "ctransProvisioning": ctransProvisioning,
       "ctransEntityProvisionTable": ctransEntityProvisionTable,
       "ctransEntityProvisionEntry": ctransEntityProvisionEntry,
       "ctransEntityProvisionRowStatus": ctransEntityProvisionRowStatus,
       "ctransEntityProvisionType": ctransEntityProvisionType,
       "ctransEntityProvisionCvidInternal": ctransEntityProvisionCvidInternal,
       "ctransEntityProvisionRange": ctransEntityProvisionRange,
       "ctransEntityProvisionCapTable": ctransEntityProvisionCapTable,
       "ctransEntityProvisionCapEntry": ctransEntityProvisionCapEntry,
       "ctransEntityProvisionCapRowStatus": ctransEntityProvisionCapRowStatus,
       "ctransEntityProvisionCapType": ctransEntityProvisionCapType,
       "ctransEntityProvisionCapCvidInternal": ctransEntityProvisionCapCvidInternal,
       "ctransEntityProvisionCapRange": ctransEntityProvisionCapRange,
       "ctransEntityProvisionDefaultsTable": ctransEntityProvisionDefaultsTable,
       "ctransEntityProvisionDefaultsEntry": ctransEntityProvisionDefaultsEntry,
       "ctransEntityProvisionDefaultsRowStatus": ctransEntityProvisionDefaultsRowStatus,
       "ctransEntityProvisionDefaultsType": ctransEntityProvisionDefaultsType,
       "ctransEntityProvisionDefaultsCvidInternal": ctransEntityProvisionDefaultsCvidInternal,
       "ctransEntityProvisionDefaultsRange": ctransEntityProvisionDefaultsRange,
       "ctransEntityProvisionCvidInternalCapTable": ctransEntityProvisionCvidInternalCapTable,
       "ctransEntityProvisionCvidInternalCapEntry": ctransEntityProvisionCvidInternalCapEntry,
       "ctransEntityProvisionCvidInternalCapIndexCap": ctransEntityProvisionCvidInternalCapIndexCap,
       "ctransEntityProvisionCvidInternalCapStringCap": ctransEntityProvisionCvidInternalCapStringCap,
       "bridgeProvisioning": bridgeProvisioning,
       "bridgeToAssignEntityTable": bridgeToAssignEntityTable,
       "bridgeToAssignEntityEntry": bridgeToAssignEntityEntry,
       "bridgeToAssignEntityIndexAid": bridgeToAssignEntityIndexAid,
       "bridgeEntityProvisionTable": bridgeEntityProvisionTable,
       "bridgeEntityProvisionEntry": bridgeEntityProvisionEntry,
       "bridgeEntityProvisionRowStatus": bridgeEntityProvisionRowStatus,
       "bridgeEntityProvisionFacilityType": bridgeEntityProvisionFacilityType,
       "bridgeEntityProvisionAlias": bridgeEntityProvisionAlias,
       "bridgeEntityProvisionShapeState": bridgeEntityProvisionShapeState,
       "bridgeEntityProvisionPmMode": bridgeEntityProvisionPmMode,
       "bridgeEntityProvisionCirTrmt": bridgeEntityProvisionCirTrmt,
       "bridgeEntityProvisionCbsTrmt": bridgeEntityProvisionCbsTrmt,
       "bridgeEntityProvisionAdminState": bridgeEntityProvisionAdminState,
       "bridgeEntityProvisionCapTable": bridgeEntityProvisionCapTable,
       "bridgeEntityProvisionCapEntry": bridgeEntityProvisionCapEntry,
       "bridgeEntityProvisionCapRowStatus": bridgeEntityProvisionCapRowStatus,
       "bridgeEntityProvisionCapFacilityType": bridgeEntityProvisionCapFacilityType,
       "bridgeEntityProvisionCapAlias": bridgeEntityProvisionCapAlias,
       "bridgeEntityProvisionCapShapeState": bridgeEntityProvisionCapShapeState,
       "bridgeEntityProvisionCapPmMode": bridgeEntityProvisionCapPmMode,
       "bridgeEntityProvisionCapCirTrmt": bridgeEntityProvisionCapCirTrmt,
       "bridgeEntityProvisionCapCbsTrmt": bridgeEntityProvisionCapCbsTrmt,
       "bridgeEntityProvisionCapAdminState": bridgeEntityProvisionCapAdminState,
       "bridgeEntityProvisionDefaultsTable": bridgeEntityProvisionDefaultsTable,
       "bridgeEntityProvisionDefaultsEntry": bridgeEntityProvisionDefaultsEntry,
       "bridgeEntityProvisionDefaultsRowStatus": bridgeEntityProvisionDefaultsRowStatus,
       "bridgeEntityProvisionDefaultsFacilityType": bridgeEntityProvisionDefaultsFacilityType,
       "bridgeEntityProvisionDefaultsAlias": bridgeEntityProvisionDefaultsAlias,
       "bridgeEntityProvisionDefaultsShapeState": bridgeEntityProvisionDefaultsShapeState,
       "bridgeEntityProvisionDefaultsPmMode": bridgeEntityProvisionDefaultsPmMode,
       "bridgeEntityProvisionDefaultsCirTrmt": bridgeEntityProvisionDefaultsCirTrmt,
       "bridgeEntityProvisionDefaultsCbsTrmt": bridgeEntityProvisionDefaultsCbsTrmt,
       "bridgeEntityProvisionDefaultsAdminState": bridgeEntityProvisionDefaultsAdminState,
       "layer2ConfigurationMIB": layer2ConfigurationMIB,
       "flowConfiguration": flowConfiguration,
       "flowEntityConfigTable": flowEntityConfigTable,
       "flowEntityConfigEntry": flowEntityConfigEntry,
       "flowEntityConfigAdmin": flowEntityConfigAdmin,
       "flowEntityConfigAlias": flowEntityConfigAlias,
       "flowEntityConfigPopCtagRcv": flowEntityConfigPopCtagRcv,
       "flowEntityConfigPopCtagTrmt": flowEntityConfigPopCtagTrmt,
       "flowEntityConfigCvidRegisteredInFlow": flowEntityConfigCvidRegisteredInFlow,
       "flowEntityConfigExternalVid": flowEntityConfigExternalVid,
       "flowEntityConfigPmMode": flowEntityConfigPmMode,
       "flowEntityConfigShape": flowEntityConfigShape,
       "flowEntityConfigPolice": flowEntityConfigPolice,
       "flowEntityConfigDefaultEvcCos": flowEntityConfigDefaultEvcCos,
       "flowEntityConfigCirRcv": flowEntityConfigCirRcv,
       "flowEntityConfigCirTrmt": flowEntityConfigCirTrmt,
       "flowEntityConfigCbsRcv": flowEntityConfigCbsRcv,
       "flowEntityConfigCbsTrmt": flowEntityConfigCbsTrmt,
       "flowEntityConfigDataLayerPmReset": flowEntityConfigDataLayerPmReset,
       "flowEntityConfigPushPvidTrmt": flowEntityConfigPushPvidTrmt,
       "flowEntityConfigPrioPvidTrmt": flowEntityConfigPrioPvidTrmt,
       "flowEntityConfigRedLineState": flowEntityConfigRedLineState,
       "flowEntityConfigTunnelAid": flowEntityConfigTunnelAid,
       "flowEntityConfigSwitchCommand": flowEntityConfigSwitchCommand,
       "flowEntityConfigInhibitSwitchToProt": flowEntityConfigInhibitSwitchToProt,
       "flowEntityConfigInhibitSwitchToWork": flowEntityConfigInhibitSwitchToWork,
       "flowEntityConfigCapTable": flowEntityConfigCapTable,
       "flowEntityConfigCapEntry": flowEntityConfigCapEntry,
       "flowEntityConfigCapAdmin": flowEntityConfigCapAdmin,
       "flowEntityConfigCapPmMode": flowEntityConfigCapPmMode,
       "flowEntityConfigCapShape": flowEntityConfigCapShape,
       "flowEntityConfigCapPolice": flowEntityConfigCapPolice,
       "flowEntityConfigCapDefaultEvcCos": flowEntityConfigCapDefaultEvcCos,
       "flowEntityConfigCapDataLayerPmReset": flowEntityConfigCapDataLayerPmReset,
       "flowEntityConfigCapPopCtagRcv": flowEntityConfigCapPopCtagRcv,
       "flowEntityConfigCapPopCtagTrmt": flowEntityConfigCapPopCtagTrmt,
       "flowEntityConfigCapCvidRegisteredInFlow": flowEntityConfigCapCvidRegisteredInFlow,
       "flowEntityConfigCapExternalVid": flowEntityConfigCapExternalVid,
       "flowEntityConfigCapCbsRcv": flowEntityConfigCapCbsRcv,
       "flowEntityConfigCapPushTrmt": flowEntityConfigCapPushTrmt,
       "flowEntityConfigCapRedLineState": flowEntityConfigCapRedLineState,
       "flowEntityConfigCapSwitchCommand": flowEntityConfigCapSwitchCommand,
       "flowEntityConfigCapInhibitSwitchToProt": flowEntityConfigCapInhibitSwitchToProt,
       "flowEntityConfigCapInhibitSwitchToWork": flowEntityConfigCapInhibitSwitchToWork,
       "flowEntityConfigCbsRcvCapTable": flowEntityConfigCbsRcvCapTable,
       "flowEntityConfigCbsRcvCapEntry": flowEntityConfigCbsRcvCapEntry,
       "flowEntityConfigCbsRcvCapCbsRcv": flowEntityConfigCbsRcvCapCbsRcv,
       "flowEntityConfigRegisterCapTable": flowEntityConfigRegisterCapTable,
       "flowEntityConfigRegisterCapEntry": flowEntityConfigRegisterCapEntry,
       "flowEntityConfigRegisterCapStringCap": flowEntityConfigRegisterCapStringCap,
       "flowEntityConfigExternalVidCapTable": flowEntityConfigExternalVidCapTable,
       "flowEntityConfigExternalVidCapEntry": flowEntityConfigExternalVidCapEntry,
       "flowEntityConfigExternalVidCapStringCap": flowEntityConfigExternalVidCapStringCap,
       "flowEntityConfigPopCtagRcvCapTable": flowEntityConfigPopCtagRcvCapTable,
       "flowEntityConfigPopCtagRcvCapEntry": flowEntityConfigPopCtagRcvCapEntry,
       "flowEntityConfigPopCtagRcvCapStringCap": flowEntityConfigPopCtagRcvCapStringCap,
       "flowEntityConfigPopCtagTrmtCapTable": flowEntityConfigPopCtagTrmtCapTable,
       "flowEntityConfigPopCtagTrmtCapEntry": flowEntityConfigPopCtagTrmtCapEntry,
       "flowEntityConfigPopCtagTrmtCapStringCap": flowEntityConfigPopCtagTrmtCapStringCap,
       "flowEntityConfigPushTrmtCapTable": flowEntityConfigPushTrmtCapTable,
       "flowEntityConfigPushTrmtCapEntry": flowEntityConfigPushTrmtCapEntry,
       "flowEntityConfigPushTrmtCapStringCap": flowEntityConfigPushTrmtCapStringCap,
       "bridgeConfiguration": bridgeConfiguration,
       "bridgeEntityConfigTable": bridgeEntityConfigTable,
       "bridgeEntityConfigEntry": bridgeEntityConfigEntry,
       "bridgeEntityConfigAlias": bridgeEntityConfigAlias,
       "bridgeEntityConfigShapeState": bridgeEntityConfigShapeState,
       "bridgeEntityConfigPmMode": bridgeEntityConfigPmMode,
       "bridgeEntityConfigCirTrmt": bridgeEntityConfigCirTrmt,
       "bridgeEntityConfigCbsTrmt": bridgeEntityConfigCbsTrmt,
       "bridgeEntityConfigAdminState": bridgeEntityConfigAdminState,
       "bridgeEntityConfigCapTable": bridgeEntityConfigCapTable,
       "bridgeEntityConfigCapEntry": bridgeEntityConfigCapEntry,
       "bridgeEntityConfigCapAlias": bridgeEntityConfigCapAlias,
       "bridgeEntityConfigCapShapeState": bridgeEntityConfigCapShapeState,
       "bridgeEntityConfigCapPmMode": bridgeEntityConfigCapPmMode,
       "bridgeEntityConfigCapCirTrmt": bridgeEntityConfigCapCirTrmt,
       "bridgeEntityConfigCapCbsTrmt": bridgeEntityConfigCapCbsTrmt,
       "bridgeEntityConfigCapAdminState": bridgeEntityConfigCapAdminState,
       "queOnBridgeConfiguration": queOnBridgeConfiguration,
       "queOnBridgeEntityConfigTable": queOnBridgeEntityConfigTable,
       "queOnBridgeEntityConfigEntry": queOnBridgeEntityConfigEntry,
       "queOnBridgeEntityConfigDataLayerPmReset": queOnBridgeEntityConfigDataLayerPmReset,
       "queOnBridgeEntityConfigCapTable": queOnBridgeEntityConfigCapTable,
       "queOnBridgeEntityConfigCapEntry": queOnBridgeEntityConfigCapEntry,
       "queOnBridgeEntityConfigCapDataLayerPmReset": queOnBridgeEntityConfigCapDataLayerPmReset,
       "layer2StatusMIB": layer2StatusMIB,
       "flowStatus": flowStatus,
       "flowEntityStatusTable": flowEntityStatusTable,
       "flowEntityStatusEntry": flowEntityStatusEntry,
       "flowEntityStatusOper": flowEntityStatusOper,
       "flowEntityStatusSecondaryStates": flowEntityStatusSecondaryStates,
       "flowEntityStatusType": flowEntityStatusType,
       "flowEntityStatusInternalSvid": flowEntityStatusInternalSvid,
       "flowEntityStatusConnectionState": flowEntityStatusConnectionState,
       "flowEntityStatusValidSignalTimer": flowEntityStatusValidSignalTimer,
       "flowEntityStatusProtectionRole": flowEntityStatusProtectionRole,
       "flowEntityStatusIngressTid": flowEntityStatusIngressTid,
       "flowEntityStatusIngressNodeIp": flowEntityStatusIngressNodeIp,
       "ctransStatus": ctransStatus,
       "ctransEntityStatusTable": ctransEntityStatusTable,
       "ctransEntityStatusEntry": ctransEntityStatusEntry,
       "ctransEntityStatusType": ctransEntityStatusType,
       "ctransEntityStatusCvidInternal": ctransEntityStatusCvidInternal,
       "ctransEntityStatusRange": ctransEntityStatusRange,
       "policerStatus": policerStatus,
       "policerOnFlowEntityStatusTable": policerOnFlowEntityStatusTable,
       "policerOnFlowEntityStatusEntry": policerOnFlowEntityStatusEntry,
       "policerOnFlowEntityStatusOper": policerOnFlowEntityStatusOper,
       "policerOnFlowEntityStatusSecondaryStates": policerOnFlowEntityStatusSecondaryStates,
       "policerOnFlowEntityStatusType": policerOnFlowEntityStatusType,
       "policerOnFlowEntityStatusAdmin": policerOnFlowEntityStatusAdmin,
       "policerOnFlowEntityStatusAlias": policerOnFlowEntityStatusAlias,
       "policerOnFlowEntityStatusCirRcv": policerOnFlowEntityStatusCirRcv,
       "policerOnFlowEntityStatusCbsRcv": policerOnFlowEntityStatusCbsRcv,
       "queStatus": queStatus,
       "queOnPortEntityStatusTable": queOnPortEntityStatusTable,
       "queOnPortEntityStatusEntry": queOnPortEntityStatusEntry,
       "queOnPortEntityStatusOper": queOnPortEntityStatusOper,
       "queOnPortEntityStatusSecondaryStates": queOnPortEntityStatusSecondaryStates,
       "queOnPortEntityStatusType": queOnPortEntityStatusType,
       "queOnPortEntityStatusAdmin": queOnPortEntityStatusAdmin,
       "queOnPortEntityStatusAlias": queOnPortEntityStatusAlias,
       "queOnPortEntityStatusCirTrmt": queOnPortEntityStatusCirTrmt,
       "queOnPortEntityStatusCbsTrmt": queOnPortEntityStatusCbsTrmt,
       "queOnFlowEntityStatusTable": queOnFlowEntityStatusTable,
       "queOnFlowEntityStatusEntry": queOnFlowEntityStatusEntry,
       "queOnFlowEntityStatusOper": queOnFlowEntityStatusOper,
       "queOnFlowEntityStatusSecondaryStates": queOnFlowEntityStatusSecondaryStates,
       "queOnFlowEntityStatusType": queOnFlowEntityStatusType,
       "queOnFlowEntityStatusAdmin": queOnFlowEntityStatusAdmin,
       "queOnFlowEntityStatusAlias": queOnFlowEntityStatusAlias,
       "queOnFlowEntityStatusCirTrmt": queOnFlowEntityStatusCirTrmt,
       "queOnFlowEntityStatusCbsTrmt": queOnFlowEntityStatusCbsTrmt,
       "queOnBridgeEntityStatusTable": queOnBridgeEntityStatusTable,
       "queOnBridgeEntityStatusEntry": queOnBridgeEntityStatusEntry,
       "queOnBridgeEntityStatusAdminState": queOnBridgeEntityStatusAdminState,
       "queOnBridgeEntityStatusFacilityType": queOnBridgeEntityStatusFacilityType,
       "queOnBridgeEntityStatusFunction": queOnBridgeEntityStatusFunction,
       "queOnBridgeEntityStatusAlias": queOnBridgeEntityStatusAlias,
       "queOnBridgeEntityStatusCirTrmt": queOnBridgeEntityStatusCirTrmt,
       "queOnBridgeEntityStatusCbsTrmt": queOnBridgeEntityStatusCbsTrmt,
       "queOnBridgeEntityStatusShapeState": queOnBridgeEntityStatusShapeState,
       "queOnBridgeEntityStatusPmMode": queOnBridgeEntityStatusPmMode,
       "queOnBridgeEntityStatusOper": queOnBridgeEntityStatusOper,
       "queOnBridgeEntityStatusSecondaryStates": queOnBridgeEntityStatusSecondaryStates,
       "bridgeStatus": bridgeStatus,
       "bridgeEntityStatusTable": bridgeEntityStatusTable,
       "bridgeEntityStatusEntry": bridgeEntityStatusEntry,
       "bridgeEntityStatusFacilityType": bridgeEntityStatusFacilityType,
       "bridgeEntityFlowTable": bridgeEntityFlowTable,
       "bridgeEntityFlowEntry": bridgeEntityFlowEntry,
       "bridgeEntityFlowId": bridgeEntityFlowId,
       "bridgeEntityFlowIndex": bridgeEntityFlowIndex,
       "layer2CrossConnections": layer2CrossConnections,
       "crossConnectionsProvisioningTable": crossConnectionsProvisioningTable,
       "crossConnectionsProvisioningEntry": crossConnectionsProvisioningEntry,
       "crossConnectionsProvisioningIndexEthFrom": crossConnectionsProvisioningIndexEthFrom,
       "crossConnectionsProvisioningIndexFlowFrom": crossConnectionsProvisioningIndexFlowFrom,
       "crossConnectionsProvisioningIndexEthTo": crossConnectionsProvisioningIndexEthTo,
       "crossConnectionsProvisioningIndexFlowTo": crossConnectionsProvisioningIndexFlowTo,
       "crossConnectionsProvisioningRowStatus": crossConnectionsProvisioningRowStatus,
       "crossConnectionsProvisioningAlias": crossConnectionsProvisioningAlias,
       "crossConnectionsProvisioningType": crossConnectionsProvisioningType,
       "crossConnectionsProvisioningCrsType": crossConnectionsProvisioningCrsType,
       "crossConnectionsProvisioningConn": crossConnectionsProvisioningConn,
       "crossConnectionsProvisioningCapTable": crossConnectionsProvisioningCapTable,
       "crossConnectionsProvisioningCapEntry": crossConnectionsProvisioningCapEntry,
       "crossConnectionsProvisioningCapIndexEthFrom": crossConnectionsProvisioningCapIndexEthFrom,
       "crossConnectionsProvisioningCapIndexFlowFrom": crossConnectionsProvisioningCapIndexFlowFrom,
       "crossConnectionsProvisioningCapIndexEthTo": crossConnectionsProvisioningCapIndexEthTo,
       "crossConnectionsProvisioningCapIndexFlowTo": crossConnectionsProvisioningCapIndexFlowTo,
       "crossConnectionsProvisioningCapRowStatus": crossConnectionsProvisioningCapRowStatus,
       "crossConnectionsProvisioningCapAlias": crossConnectionsProvisioningCapAlias,
       "crossConnectionsProvisioningCapType": crossConnectionsProvisioningCapType,
       "crossConnectionsProvisioningCapCrsType": crossConnectionsProvisioningCapCrsType,
       "crossConnectionsProvisioningCapConn": crossConnectionsProvisioningCapConn,
       "crossConnectionsProvisioningDefaultsTable": crossConnectionsProvisioningDefaultsTable,
       "crossConnectionsProvisioningDefaultsEntry": crossConnectionsProvisioningDefaultsEntry,
       "crossConnectionsProvisioningDefaultsIndexEthFrom": crossConnectionsProvisioningDefaultsIndexEthFrom,
       "crossConnectionsProvisioningDefaultsIndexFlowFrom": crossConnectionsProvisioningDefaultsIndexFlowFrom,
       "crossConnectionsProvisioningDefaultsIndexEthTo": crossConnectionsProvisioningDefaultsIndexEthTo,
       "crossConnectionsProvisioningDefaultsIndexFlowTo": crossConnectionsProvisioningDefaultsIndexFlowTo,
       "crossConnectionsProvisioningDefaultsRowStatus": crossConnectionsProvisioningDefaultsRowStatus,
       "crossConnectionsProvisioningDefaultsAlias": crossConnectionsProvisioningDefaultsAlias,
       "crossConnectionsProvisioningDefaultsType": crossConnectionsProvisioningDefaultsType,
       "crossConnectionsProvisioningDefaultsCrsType": crossConnectionsProvisioningDefaultsCrsType,
       "crossConnectionsProvisioningDefaultsConn": crossConnectionsProvisioningDefaultsConn,
       "crossConnectionsConfigTable": crossConnectionsConfigTable,
       "crossConnectionsConfigEntry": crossConnectionsConfigEntry,
       "crossConnectionsConfigAlias": crossConnectionsConfigAlias,
       "crossConnectionsStatusTable": crossConnectionsStatusTable,
       "crossConnectionsStatusEntry": crossConnectionsStatusEntry,
       "crossConnectionsStatusFromEth": crossConnectionsStatusFromEth,
       "crossConnectionsStatusToEth": crossConnectionsStatusToEth,
       "crossConnectionsStatusType": crossConnectionsStatusType,
       "crossConnectionsStatusCrsFunction": crossConnectionsStatusCrsFunction,
       "crossConnectionsStatusCrsType": crossConnectionsStatusCrsType,
       "crossConnectionsStatusConn": crossConnectionsStatusConn,
       "crossConnectionsPointsFromTable": crossConnectionsPointsFromTable,
       "crossConnectionsPointsFromEntry": crossConnectionsPointsFromEntry,
       "crossConnectionsPointsFromFlow": crossConnectionsPointsFromFlow,
       "crossConnectionsPointsToTable": crossConnectionsPointsToTable,
       "crossConnectionsPointsToEntry": crossConnectionsPointsToEntry,
       "crossConnectionsPointsToFlow": crossConnectionsPointsToFlow,
       "layer2PerformanceMonitoring": layer2PerformanceMonitoring,
       "flowPerformanceMonitoring": flowPerformanceMonitoring,
       "currentFlowEntityRx15minTable": currentFlowEntityRx15minTable,
       "currentFlowEntityRx15minEntry": currentFlowEntityRx15minEntry,
       "currentFlowEntityRx15minUnicastFramesPerEvcRcv": currentFlowEntityRx15minUnicastFramesPerEvcRcv,
       "currentFlowEntityRx15minMcBcFramesPerEvcRcv": currentFlowEntityRx15minMcBcFramesPerEvcRcv,
       "currentFlowEntityRx15minElapsedTime": currentFlowEntityRx15minElapsedTime,
       "currentFlowEntityRx1dayTable": currentFlowEntityRx1dayTable,
       "currentFlowEntityRx1dayEntry": currentFlowEntityRx1dayEntry,
       "currentFlowEntityRx1dayUnicastFramesPerEvcRcv": currentFlowEntityRx1dayUnicastFramesPerEvcRcv,
       "currentFlowEntityRx1dayMcBcFramesPerEvcRcv": currentFlowEntityRx1dayMcBcFramesPerEvcRcv,
       "currentFlowEntityRx1dayElapsedTime": currentFlowEntityRx1dayElapsedTime,
       "intervalFlowEntityRx15minTable": intervalFlowEntityRx15minTable,
       "intervalFlowEntityRx15minEntry": intervalFlowEntityRx15minEntry,
       "intervalFlowEntityRx15minNumber": intervalFlowEntityRx15minNumber,
       "intervalFlowEntityRx15minUnicastFramesPerEvcRcv": intervalFlowEntityRx15minUnicastFramesPerEvcRcv,
       "intervalFlowEntityRx15minMcBcFramesPerEvcRcv": intervalFlowEntityRx15minMcBcFramesPerEvcRcv,
       "intervalFlowEntityRx15minValidFlag": intervalFlowEntityRx15minValidFlag,
       "intervalFlowEntityRx15minTimeStamp": intervalFlowEntityRx15minTimeStamp,
       "intervalFlowEntityRx1dayTable": intervalFlowEntityRx1dayTable,
       "intervalFlowEntityRx1dayEntry": intervalFlowEntityRx1dayEntry,
       "intervalFlowEntityRx1dayNumber": intervalFlowEntityRx1dayNumber,
       "intervalFlowEntityRx1dayUnicastFramesPerEvcRcv": intervalFlowEntityRx1dayUnicastFramesPerEvcRcv,
       "intervalFlowEntityRx1dayMcBcFramesPerEvcRcv": intervalFlowEntityRx1dayMcBcFramesPerEvcRcv,
       "intervalFlowEntityRx1dayValidFlag": intervalFlowEntityRx1dayValidFlag,
       "intervalFlowEntityRx1dayTimeStamp": intervalFlowEntityRx1dayTimeStamp,
       "currentFlowEntityTx15minTable": currentFlowEntityTx15minTable,
       "currentFlowEntityTx15minEntry": currentFlowEntityTx15minEntry,
       "currentFlowEntityTx15minUnicastFramesPerEvcTrmt": currentFlowEntityTx15minUnicastFramesPerEvcTrmt,
       "currentFlowEntityTx15minMcBcFramesPerEvcTrmt": currentFlowEntityTx15minMcBcFramesPerEvcTrmt,
       "currentFlowEntityTx15minElapsedTime": currentFlowEntityTx15minElapsedTime,
       "currentFlowEntityTx1dayTable": currentFlowEntityTx1dayTable,
       "currentFlowEntityTx1dayEntry": currentFlowEntityTx1dayEntry,
       "currentFlowEntityTx1dayUnicastFramesPerEvcTrmt": currentFlowEntityTx1dayUnicastFramesPerEvcTrmt,
       "currentFlowEntityTx1dayMcBcFramesPerEvcTrmt": currentFlowEntityTx1dayMcBcFramesPerEvcTrmt,
       "currentFlowEntityTx1dayElapsedTime": currentFlowEntityTx1dayElapsedTime,
       "intervalFlowEntityTx15minTable": intervalFlowEntityTx15minTable,
       "intervalFlowEntityTx15minEntry": intervalFlowEntityTx15minEntry,
       "intervalFlowEntityTx15minNumber": intervalFlowEntityTx15minNumber,
       "intervalFlowEntityTx15minUnicastFramesPerEvcTrmt": intervalFlowEntityTx15minUnicastFramesPerEvcTrmt,
       "intervalFlowEntityTx15minMcBcFramesPerEvcTrmt": intervalFlowEntityTx15minMcBcFramesPerEvcTrmt,
       "intervalFlowEntityTx15minValidFlag": intervalFlowEntityTx15minValidFlag,
       "intervalFlowEntityTx15minTimeStamp": intervalFlowEntityTx15minTimeStamp,
       "intervalFlowEntityTx1dayTable": intervalFlowEntityTx1dayTable,
       "intervalFlowEntityTx1dayEntry": intervalFlowEntityTx1dayEntry,
       "intervalFlowEntityTx1dayNumber": intervalFlowEntityTx1dayNumber,
       "intervalFlowEntityTx1dayUnicastFramesPerEvcTrmt": intervalFlowEntityTx1dayUnicastFramesPerEvcTrmt,
       "intervalFlowEntityTx1dayMcBcFramesPerEvcTrmt": intervalFlowEntityTx1dayMcBcFramesPerEvcTrmt,
       "intervalFlowEntityTx1dayValidFlag": intervalFlowEntityTx1dayValidFlag,
       "intervalFlowEntityTx1dayTimeStamp": intervalFlowEntityTx1dayTimeStamp,
       "policerPerformanceMonitoring": policerPerformanceMonitoring,
       "currentpolicerOnFlowEntity15minTable": currentpolicerOnFlowEntity15minTable,
       "currentpolicerOnFlowEntity15minEntry": currentpolicerOnFlowEntity15minEntry,
       "currentpolicerOnFlowEntity15minBytesMarkedGreen": currentpolicerOnFlowEntity15minBytesMarkedGreen,
       "currentpolicerOnFlowEntity15minFramesMarkedGreen": currentpolicerOnFlowEntity15minFramesMarkedGreen,
       "currentpolicerOnFlowEntity15minBytesMarkedRed": currentpolicerOnFlowEntity15minBytesMarkedRed,
       "currentpolicerOnFlowEntity15minFramesMarkedRed": currentpolicerOnFlowEntity15minFramesMarkedRed,
       "currentpolicerOnFlowEntity15minElapsedTime": currentpolicerOnFlowEntity15minElapsedTime,
       "currentpolicerOnFlowEntity1dayTable": currentpolicerOnFlowEntity1dayTable,
       "currentpolicerOnFlowEntity1dayEntry": currentpolicerOnFlowEntity1dayEntry,
       "currentpolicerOnFlowEntity1dayBytesMarkedGreen": currentpolicerOnFlowEntity1dayBytesMarkedGreen,
       "currentpolicerOnFlowEntity1dayFramesMarkedGreen": currentpolicerOnFlowEntity1dayFramesMarkedGreen,
       "currentpolicerOnFlowEntity1dayBytesMarkedRed": currentpolicerOnFlowEntity1dayBytesMarkedRed,
       "currentpolicerOnFlowEntity1dayFramesMarkedRed": currentpolicerOnFlowEntity1dayFramesMarkedRed,
       "currentpolicerOnFlowEntity1dayElapsedTime": currentpolicerOnFlowEntity1dayElapsedTime,
       "intervalpolicerOnFlowEntity15minTable": intervalpolicerOnFlowEntity15minTable,
       "intervalpolicerOnFlowEntity15minEntry": intervalpolicerOnFlowEntity15minEntry,
       "intervalpolicerOnFlowEntity15minNumber": intervalpolicerOnFlowEntity15minNumber,
       "intervalpolicerOnFlowEntity15minBytesMarkedGreen": intervalpolicerOnFlowEntity15minBytesMarkedGreen,
       "intervalpolicerOnFlowEntity15minFramesMarkedGreen": intervalpolicerOnFlowEntity15minFramesMarkedGreen,
       "intervalpolicerOnFlowEntity15minBytesMarkedRed": intervalpolicerOnFlowEntity15minBytesMarkedRed,
       "intervalpolicerOnFlowEntity15minFramesMarkedRed": intervalpolicerOnFlowEntity15minFramesMarkedRed,
       "intervalpolicerOnFlowEntity15minValidFlag": intervalpolicerOnFlowEntity15minValidFlag,
       "intervalpolicerOnFlowEntity15minTimeStamp": intervalpolicerOnFlowEntity15minTimeStamp,
       "intervalpolicerOnFlowEntity1dayTable": intervalpolicerOnFlowEntity1dayTable,
       "intervalpolicerOnFlowEntity1dayEntry": intervalpolicerOnFlowEntity1dayEntry,
       "intervalpolicerOnFlowEntity1dayNumber": intervalpolicerOnFlowEntity1dayNumber,
       "intervalpolicerOnFlowEntity1dayBytesMarkedGreen": intervalpolicerOnFlowEntity1dayBytesMarkedGreen,
       "intervalpolicerOnFlowEntity1dayFramesMarkedGreen": intervalpolicerOnFlowEntity1dayFramesMarkedGreen,
       "intervalpolicerOnFlowEntity1dayBytesMarkedRed": intervalpolicerOnFlowEntity1dayBytesMarkedRed,
       "intervalpolicerOnFlowEntity1dayFramesMarkedRed": intervalpolicerOnFlowEntity1dayFramesMarkedRed,
       "intervalpolicerOnFlowEntity1dayValidFlag": intervalpolicerOnFlowEntity1dayValidFlag,
       "intervalpolicerOnFlowEntity1dayTimeStamp": intervalpolicerOnFlowEntity1dayTimeStamp,
       "quePerformanceMonitoring": quePerformanceMonitoring,
       "currentQueOnPortEntity15minTable": currentQueOnPortEntity15minTable,
       "currentQueOnPortEntity15minEntry": currentQueOnPortEntity15minEntry,
       "currentQueOnPortEntity15minBytesDroppedBufOverflow": currentQueOnPortEntity15minBytesDroppedBufOverflow,
       "currentQueOnPortEntity15minFramesDroppedBufOverflow": currentQueOnPortEntity15minFramesDroppedBufOverflow,
       "currentQueOnPortEntity15minElapsedTime": currentQueOnPortEntity15minElapsedTime,
       "currentQueOnPortEntity1dayTable": currentQueOnPortEntity1dayTable,
       "currentQueOnPortEntity1dayEntry": currentQueOnPortEntity1dayEntry,
       "currentQueOnPortEntity1dayBytesDroppedBufOverflow": currentQueOnPortEntity1dayBytesDroppedBufOverflow,
       "currentQueOnPortEntity1dayFramesDroppedBufOverflow": currentQueOnPortEntity1dayFramesDroppedBufOverflow,
       "currentQueOnPortEntity1dayElapsedTime": currentQueOnPortEntity1dayElapsedTime,
       "intervalQueOnPortEntity15minTable": intervalQueOnPortEntity15minTable,
       "intervalQueOnPortEntity15minEntry": intervalQueOnPortEntity15minEntry,
       "intervalQueOnPortEntity15minNumber": intervalQueOnPortEntity15minNumber,
       "intervalQueOnPortEntity15minBytesDroppedBufOverflow": intervalQueOnPortEntity15minBytesDroppedBufOverflow,
       "intervalQueOnPortEntity15minFramesDroppedBufOverflow": intervalQueOnPortEntity15minFramesDroppedBufOverflow,
       "intervalQueOnPortEntity15minValidFlag": intervalQueOnPortEntity15minValidFlag,
       "intervalQueOnPortEntity15minTimeStamp": intervalQueOnPortEntity15minTimeStamp,
       "intervalQueOnPortEntity1dayTable": intervalQueOnPortEntity1dayTable,
       "intervalQueOnPortEntity1dayEntry": intervalQueOnPortEntity1dayEntry,
       "intervalQueOnPortEntity1dayNumber": intervalQueOnPortEntity1dayNumber,
       "intervalQueOnPortEntity1dayBytesDroppedBufOverflow": intervalQueOnPortEntity1dayBytesDroppedBufOverflow,
       "intervalQueOnPortEntity1dayFramesDroppedBufOverflow": intervalQueOnPortEntity1dayFramesDroppedBufOverflow,
       "intervalQueOnPortEntity1dayValidFlag": intervalQueOnPortEntity1dayValidFlag,
       "intervalQueOnPortEntity1dayTimeStamp": intervalQueOnPortEntity1dayTimeStamp,
       "currentQueOnFlowEntity15minTable": currentQueOnFlowEntity15minTable,
       "currentQueOnFlowEntity15minEntry": currentQueOnFlowEntity15minEntry,
       "currentQueOnFlowEntity15minBytesDroppedBufOverflow": currentQueOnFlowEntity15minBytesDroppedBufOverflow,
       "currentQueOnFlowEntity15minFramesDroppedBufOverflow": currentQueOnFlowEntity15minFramesDroppedBufOverflow,
       "currentQueOnFlowEntity15minElapsedTime": currentQueOnFlowEntity15minElapsedTime,
       "currentQueOnFlowEntity1dayTable": currentQueOnFlowEntity1dayTable,
       "currentQueOnFlowEntity1dayEntry": currentQueOnFlowEntity1dayEntry,
       "currentQueOnFlowEntity1dayBytesDroppedBufOverflow": currentQueOnFlowEntity1dayBytesDroppedBufOverflow,
       "currentQueOnFlowEntity1dayFramesDroppedBufOverflow": currentQueOnFlowEntity1dayFramesDroppedBufOverflow,
       "currentQueOnFlowEntity1dayElapsedTime": currentQueOnFlowEntity1dayElapsedTime,
       "intervalQueOnFlowEntity15minTable": intervalQueOnFlowEntity15minTable,
       "intervalQueOnFlowEntity15minEntry": intervalQueOnFlowEntity15minEntry,
       "intervalQueOnFlowEntity15minNumber": intervalQueOnFlowEntity15minNumber,
       "intervalQueOnFlowEntity15minBytesDroppedBufOverflow": intervalQueOnFlowEntity15minBytesDroppedBufOverflow,
       "intervalQueOnFlowEntity15minFramesDroppedBufOverflow": intervalQueOnFlowEntity15minFramesDroppedBufOverflow,
       "intervalQueOnFlowEntity15minValidFlag": intervalQueOnFlowEntity15minValidFlag,
       "intervalQueOnFlowEntity15minTimeStamp": intervalQueOnFlowEntity15minTimeStamp,
       "intervalQueOnFlowEntity1dayTable": intervalQueOnFlowEntity1dayTable,
       "intervalQueOnFlowEntity1dayEntry": intervalQueOnFlowEntity1dayEntry,
       "intervalQueOnFlowEntity1dayNumber": intervalQueOnFlowEntity1dayNumber,
       "intervalQueOnFlowEntity1dayBytesDroppedBufOverflow": intervalQueOnFlowEntity1dayBytesDroppedBufOverflow,
       "intervalQueOnFlowEntity1dayFramesDroppedBufOverflow": intervalQueOnFlowEntity1dayFramesDroppedBufOverflow,
       "intervalQueOnFlowEntity1dayValidFlag": intervalQueOnFlowEntity1dayValidFlag,
       "intervalQueOnFlowEntity1dayTimeStamp": intervalQueOnFlowEntity1dayTimeStamp,
       "currentQueOnBridgeEntity15minTable": currentQueOnBridgeEntity15minTable,
       "currentQueOnBridgeEntity15minEntry": currentQueOnBridgeEntity15minEntry,
       "currentQueOnBridgeEntity15minBytesDroppedBufOverflow": currentQueOnBridgeEntity15minBytesDroppedBufOverflow,
       "currentQueOnBridgeEntity15minFramesDroppedBufOverflow": currentQueOnBridgeEntity15minFramesDroppedBufOverflow,
       "currentQueOnBridgeEntity15minElapsedTime": currentQueOnBridgeEntity15minElapsedTime,
       "currentQueOnBridgeEntity1dayTable": currentQueOnBridgeEntity1dayTable,
       "currentQueOnBridgeEntity1dayEntry": currentQueOnBridgeEntity1dayEntry,
       "currentQueOnBridgeEntity1dayBytesDroppedBufOverflow": currentQueOnBridgeEntity1dayBytesDroppedBufOverflow,
       "currentQueOnBridgeEntity1dayFramesDroppedBufOverflow": currentQueOnBridgeEntity1dayFramesDroppedBufOverflow,
       "currentQueOnBridgeEntity1dayElapsedTime": currentQueOnBridgeEntity1dayElapsedTime,
       "intervalQueOnBridgeEntity15minTable": intervalQueOnBridgeEntity15minTable,
       "intervalQueOnBridgeEntity15minEntry": intervalQueOnBridgeEntity15minEntry,
       "intervalQueOnBridgeEntity15minNumber": intervalQueOnBridgeEntity15minNumber,
       "intervalQueOnBridgeEntity15minBytesDroppedBufOverflow": intervalQueOnBridgeEntity15minBytesDroppedBufOverflow,
       "intervalQueOnBridgeEntity15minFramesDroppedBufOverflow": intervalQueOnBridgeEntity15minFramesDroppedBufOverflow,
       "intervalQueOnBridgeEntity15minValidFlag": intervalQueOnBridgeEntity15minValidFlag,
       "intervalQueOnBridgeEntity15minTimeStamp": intervalQueOnBridgeEntity15minTimeStamp,
       "intervalQueOnBridgeEntity1dayTable": intervalQueOnBridgeEntity1dayTable,
       "intervalQueOnBridgeEntity1dayEntry": intervalQueOnBridgeEntity1dayEntry,
       "intervalQueOnBridgeEntity1dayNumber": intervalQueOnBridgeEntity1dayNumber,
       "intervalQueOnBridgeEntity1dayBytesDroppedBufOverflow": intervalQueOnBridgeEntity1dayBytesDroppedBufOverflow,
       "intervalQueOnBridgeEntity1dayFramesDroppedBufOverflow": intervalQueOnBridgeEntity1dayFramesDroppedBufOverflow,
       "intervalQueOnBridgeEntity1dayValidFlag": intervalQueOnBridgeEntity1dayValidFlag,
       "intervalQueOnBridgeEntity1dayTimeStamp": intervalQueOnBridgeEntity1dayTimeStamp,
       "layer2Alarms": layer2Alarms,
       "layer2Traps": layer2Traps,
       "layer2TrapsPrefix": layer2TrapsPrefix,
       "alarmOosDisabledL2": alarmOosDisabledL2,
       "alarmOosManagementL2": alarmOosManagementL2,
       "alarmOosMaintenanceL2": alarmOosMaintenanceL2,
       "alarmOosAinsL2": alarmOosAinsL2,
       "alarmServerSignalFailL2": alarmServerSignalFailL2,
       "alarmMepNotPresentL2": alarmMepNotPresentL2,
       "alarmPriVidNotEqualExtVidL2": alarmPriVidNotEqualExtVidL2,
       "alarmSwitchtoProtectionInhibitedL2": alarmSwitchtoProtectionInhibitedL2,
       "alarmManswL2": alarmManswL2,
       "alarmSfCfmLevel0L2": alarmSfCfmLevel0L2,
       "alarmSfCfmLevel1L2": alarmSfCfmLevel1L2,
       "alarmSfCfmLevel2L2": alarmSfCfmLevel2L2,
       "alarmSfCfmLevel3L2": alarmSfCfmLevel3L2,
       "alarmSfCfmLevel4L2": alarmSfCfmLevel4L2,
       "alarmSfCfmLevel5L2": alarmSfCfmLevel5L2,
       "alarmSfCfmLevel6L2": alarmSfCfmLevel6L2,
       "alarmSfCfmLevel7L2": alarmSfCfmLevel7L2,
       "alarmBridgeOosManagement": alarmBridgeOosManagement,
       "alarmBridgeOosAins": alarmBridgeOosAins,
       "alarmSwitchtoWorkingInhibitedL2": alarmSwitchtoWorkingInhibitedL2,
       "flowEntityCreation": flowEntityCreation,
       "ctransEntityCreation": ctransEntityCreation,
       "bridgeEntityCreation": bridgeEntityCreation,
       "flowEntityDeletion": flowEntityDeletion,
       "ctransEntityDeletion": ctransEntityDeletion,
       "bridgeEntityDeletion": bridgeEntityDeletion,
       "layer2EntityStateChange": layer2EntityStateChange,
       "flowEntityObjectChange": flowEntityObjectChange,
       "ctransEntityObjectChange": ctransEntityObjectChange,
       "bridgeEntityObjectChange": bridgeEntityObjectChange,
       "crossConnectionCreationLayer2": crossConnectionCreationLayer2,
       "crossConnectionDeletionLayer2": crossConnectionDeletionLayer2,
       "crossConnectionObjectChangeLayer2": crossConnectionObjectChangeLayer2,
       "ffpFlowEntityCreation": ffpFlowEntityCreation,
       "ffpFlowEntityDeletion": ffpFlowEntityDeletion,
       "ffpFlowEntityObjectChange": ffpFlowEntityObjectChange,
       "transientWorkingSwitchedtoProtectionL2": transientWorkingSwitchedtoProtectionL2,
       "transientWorkingSwitchedBacktoWorkingL2": transientWorkingSwitchedBacktoWorkingL2,
       "transientManualWorkingSwitchedtoProtectionL2": transientManualWorkingSwitchedtoProtectionL2,
       "transientManualWorkingSwitchedBacktoWorkingL2": transientManualWorkingSwitchedBacktoWorkingL2,
       "layer2Conditions": layer2Conditions,
       "flowConditionSeverityTable": flowConditionSeverityTable,
       "flowConditionSeverityEntry": flowConditionSeverityEntry,
       "flowConditionSeverityType": flowConditionSeverityType,
       "flowConditionSeverityValue": flowConditionSeverityValue,
       "bridgeConditionSeverityTable": bridgeConditionSeverityTable,
       "bridgeConditionSeverityEntry": bridgeConditionSeverityEntry,
       "bridgeConditionSeverityType": bridgeConditionSeverityType,
       "bridgeConditionSeverityValue": bridgeConditionSeverityValue,
       "flowCurrentConditionTable": flowCurrentConditionTable,
       "flowCurrentConditionEntry": flowCurrentConditionEntry,
       "flowCurrentConditionType": flowCurrentConditionType,
       "flowCurrentConditionSeverity": flowCurrentConditionSeverity,
       "flowCurrentConditionAffect": flowCurrentConditionAffect,
       "flowCurrentConditionTimeStamp": flowCurrentConditionTimeStamp,
       "bridgeCurrentConditionTable": bridgeCurrentConditionTable,
       "bridgeCurrentConditionEntry": bridgeCurrentConditionEntry,
       "bridgeCurrentConditionType": bridgeCurrentConditionType,
       "bridgeCurrentConditionSeverity": bridgeCurrentConditionSeverity,
       "bridgeCurrentConditionAffect": bridgeCurrentConditionAffect,
       "bridgeCurrentConditionTimeStamp": bridgeCurrentConditionTimeStamp,
       "layer2FlowProtection": layer2FlowProtection,
       "flowProtectionToAssignEntityTable": flowProtectionToAssignEntityTable,
       "flowProtectionToAssignEntityEntry": flowProtectionToAssignEntityEntry,
       "flowProtectionToAssignEntityIndexAid": flowProtectionToAssignEntityIndexAid,
       "flowProtectionToAssignEntityClass": flowProtectionToAssignEntityClass,
       "flowProtectionToAssignEntityClassInstanceNumber": flowProtectionToAssignEntityClassInstanceNumber,
       "flowProtectionAssignedEntityTable": flowProtectionAssignedEntityTable,
       "flowProtectionAssignedEntityEntry": flowProtectionAssignedEntityEntry,
       "flowProtectionAssignedEntityIndexAid": flowProtectionAssignedEntityIndexAid,
       "flowProtectionAssignedEntityClass": flowProtectionAssignedEntityClass,
       "flowProtectionAssignedEntityClassInstanceNumber": flowProtectionAssignedEntityClassInstanceNumber,
       "flowProtectionProvisionTable": flowProtectionProvisionTable,
       "flowProtectionProvisionEntry": flowProtectionProvisionEntry,
       "flowProtectionProvisionRowStatus": flowProtectionProvisionRowStatus,
       "flowProtectionProvisionWorkingEthIndex": flowProtectionProvisionWorkingEthIndex,
       "flowProtectionProvisionWorkingFlwIndex": flowProtectionProvisionWorkingFlwIndex,
       "flowProtectionProvisionProtectionEthIndex": flowProtectionProvisionProtectionEthIndex,
       "flowProtectionProvisionProtectionFlwIndex": flowProtectionProvisionProtectionFlwIndex,
       "flowProtectionProvisionProtectionMech": flowProtectionProvisionProtectionMech,
       "flowProtectionProvisionRevertiveMode": flowProtectionProvisionRevertiveMode,
       "flowProtectionProvisionBridge": flowProtectionProvisionBridge,
       "flowProtectionProvisionLevelDomainMonitored": flowProtectionProvisionLevelDomainMonitored,
       "flowProtectionProvisionBridgeType": flowProtectionProvisionBridgeType,
       "flowProtectionProvisionCapTable": flowProtectionProvisionCapTable,
       "flowProtectionProvisionCapEntry": flowProtectionProvisionCapEntry,
       "flowProtectionProvisionCapRowStatus": flowProtectionProvisionCapRowStatus,
       "flowProtectionProvisionCapWorkingEthIndex": flowProtectionProvisionCapWorkingEthIndex,
       "flowProtectionProvisionCapWorkingFlwIndex": flowProtectionProvisionCapWorkingFlwIndex,
       "flowProtectionProvisionCapProtectionEthIndex": flowProtectionProvisionCapProtectionEthIndex,
       "flowProtectionProvisionCapProtectionFlwIndex": flowProtectionProvisionCapProtectionFlwIndex,
       "flowProtectionProvisionCapProtectionMech": flowProtectionProvisionCapProtectionMech,
       "flowProtectionProvisionCapRevertiveMode": flowProtectionProvisionCapRevertiveMode,
       "flowProtectionProvisionCapBridge": flowProtectionProvisionCapBridge,
       "flowProtectionProvisionCapLevelDomainMonitored": flowProtectionProvisionCapLevelDomainMonitored,
       "flowProtectionProvisionCapBridgeType": flowProtectionProvisionCapBridgeType,
       "flowProtectionProvisionDefaultsTable": flowProtectionProvisionDefaultsTable,
       "flowProtectionProvisionDefaultsEntry": flowProtectionProvisionDefaultsEntry,
       "flowProtectionProvisionDefaultsRowStatus": flowProtectionProvisionDefaultsRowStatus,
       "flowProtectionProvisionDefaultsWorkingEthIndex": flowProtectionProvisionDefaultsWorkingEthIndex,
       "flowProtectionProvisionDefaultsWorkingFlwIndex": flowProtectionProvisionDefaultsWorkingFlwIndex,
       "flowProtectionProvisionDefaultsProtectionEthIndex": flowProtectionProvisionDefaultsProtectionEthIndex,
       "flowProtectionProvisionDefaultsProtectionFlwIndex": flowProtectionProvisionDefaultsProtectionFlwIndex,
       "flowProtectionProvisionDefaultsProtectionMech": flowProtectionProvisionDefaultsProtectionMech,
       "flowProtectionProvisionDefaultsRevertiveMode": flowProtectionProvisionDefaultsRevertiveMode,
       "flowProtectionProvisionDefaultsBridge": flowProtectionProvisionDefaultsBridge,
       "flowProtectionProvisionDefaultsLevelDomainMonitored": flowProtectionProvisionDefaultsLevelDomainMonitored,
       "flowProtectionProvisionDefaultsBridgeType": flowProtectionProvisionDefaultsBridgeType,
       "flowProtectionProvisionProtectionAidCapsTable": flowProtectionProvisionProtectionAidCapsTable,
       "flowProtectionProvisionProtectionAidCapsEntry": flowProtectionProvisionProtectionAidCapsEntry,
       "flowProtectionProvisionProtectionAidCapsIndex": flowProtectionProvisionProtectionAidCapsIndex,
       "flowProtectionStatusTable": flowProtectionStatusTable,
       "flowProtectionStatusEntry": flowProtectionStatusEntry,
       "flowProtectionStatusWorkingEthIndex": flowProtectionStatusWorkingEthIndex,
       "flowProtectionStatusWorkingFlwIndex": flowProtectionStatusWorkingFlwIndex,
       "flowProtectionStatusProtectionEthIndex": flowProtectionStatusProtectionEthIndex,
       "flowProtectionStatusProtectionFlwIndex": flowProtectionStatusProtectionFlwIndex,
       "flowProtectionStatusApsType": flowProtectionStatusApsType,
       "flowProtectionStatusProtectionType": flowProtectionStatusProtectionType,
       "flowProtectionStatusProtectionMech": flowProtectionStatusProtectionMech,
       "flowProtectionStatusDirection": flowProtectionStatusDirection,
       "flowProtectionStatusRevertiveMode": flowProtectionStatusRevertiveMode,
       "flowProtectionStatusBridge": flowProtectionStatusBridge,
       "flowProtectionStatusLevelDomainMonitored": flowProtectionStatusLevelDomainMonitored,
       "flowProtectionStatusBridgeType": flowProtectionStatusBridgeType}
)
