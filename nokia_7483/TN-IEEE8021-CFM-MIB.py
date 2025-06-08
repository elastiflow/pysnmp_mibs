# SNMP MIB module (TN-IEEE8021-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-IEEE8021-CFM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:43 2025
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

(Dot1agCfmCcmInterval,
 Dot1agCfmMDLevel,
 Dot1agCfmMepId,
 Dot1agCfmMepIdOrZero,
 Dot1agCfmMpDirection,
 dot1agCfmMaIndex,
 dot1agCfmMaMepListEntry,
 dot1agCfmMaNetEntry,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier,
 dot1agCfmMepTransmitLbmDestMacAddress,
 dot1agCfmMepTransmitLtmSeqNumber) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmCcmInterval",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMepId",
    "Dot1agCfmMepIdOrZero",
    "Dot1agCfmMpDirection",
    "dot1agCfmMaIndex",
    "dot1agCfmMaMepListEntry",
    "dot1agCfmMaNetEntry",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier",
    "dot1agCfmMepTransmitLbmDestMacAddress",
    "dot1agCfmMepTransmitLtmSeqNumber")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(SdpId,) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "SdpId")

(TNamedItem,
 TmnxEnabledDisabled,
 TmnxServId) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TNamedItem",
    "TmnxEnabledDisabled",
    "TmnxServId")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnIEEE8021CfmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 52)
)
if mibBuilder.loadTexts:
    tnIEEE8021CfmMIBModule.setRevisions(
        ("1914-02-10 00:00",
         "1913-08-22 00:00",
         "1912-12-13 00:00",
         "1912-12-05 00:00",
         "1912-09-09 12:00",
         "1912-03-29 12:00",
         "1909-02-28 00:00",
         "1908-01-01 00:00",
         "1914-07-24 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDot1agMIBObjs_ObjectIdentity = ObjectIdentity
tnDot1agMIBObjs = _TnDot1agMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52)
)
_TnDot1agCfmStack_ObjectIdentity = ObjectIdentity
tnDot1agCfmStack = _TnDot1agCfmStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1)
)
_TnDot1agCfmStackTable_Object = MibTable
tnDot1agCfmStackTable = _TnDot1agCfmStackTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2)
)
if mibBuilder.loadTexts:
    tnDot1agCfmStackTable.setStatus("current")
_TnDot1agCfmStackEntry_Object = MibTableRow
tnDot1agCfmStackEntry = _TnDot1agCfmStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2, 1)
)
tnDot1agCfmStackEntry.setIndexNames(
    (0, "TN-IEEE8021-CFM-MIB", "tnDot1agCfmStackifIndex"),
    (0, "TN-IEEE8021-CFM-MIB", "tnDot1agCfmStackVlanIdOrNone"),
    (0, "TN-IEEE8021-CFM-MIB", "tnDot1agCfmStackMdLevel"),
    (0, "TN-IEEE8021-CFM-MIB", "tnDot1agCfmStackDirection"),
)
if mibBuilder.loadTexts:
    tnDot1agCfmStackEntry.setStatus("current")
_TnDot1agCfmStackifIndex_Type = InterfaceIndex
_TnDot1agCfmStackifIndex_Object = MibTableColumn
tnDot1agCfmStackifIndex = _TnDot1agCfmStackifIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2, 1, 1),
    _TnDot1agCfmStackifIndex_Type()
)
tnDot1agCfmStackifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDot1agCfmStackifIndex.setStatus("current")
_TnDot1agCfmStackVlanIdOrNone_Type = Unsigned32
_TnDot1agCfmStackVlanIdOrNone_Object = MibTableColumn
tnDot1agCfmStackVlanIdOrNone = _TnDot1agCfmStackVlanIdOrNone_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2, 1, 2),
    _TnDot1agCfmStackVlanIdOrNone_Type()
)
tnDot1agCfmStackVlanIdOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDot1agCfmStackVlanIdOrNone.setStatus("current")
_TnDot1agCfmStackMdLevel_Type = Dot1agCfmMDLevel
_TnDot1agCfmStackMdLevel_Object = MibTableColumn
tnDot1agCfmStackMdLevel = _TnDot1agCfmStackMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2, 1, 3),
    _TnDot1agCfmStackMdLevel_Type()
)
tnDot1agCfmStackMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDot1agCfmStackMdLevel.setStatus("current")
_TnDot1agCfmStackDirection_Type = Dot1agCfmMpDirection
_TnDot1agCfmStackDirection_Object = MibTableColumn
tnDot1agCfmStackDirection = _TnDot1agCfmStackDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2, 1, 4),
    _TnDot1agCfmStackDirection_Type()
)
tnDot1agCfmStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDot1agCfmStackDirection.setStatus("current")
_TnDot1agCfmStackMdIndex_Type = Unsigned32
_TnDot1agCfmStackMdIndex_Object = MibTableColumn
tnDot1agCfmStackMdIndex = _TnDot1agCfmStackMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2, 1, 5),
    _TnDot1agCfmStackMdIndex_Type()
)
tnDot1agCfmStackMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmStackMdIndex.setStatus("current")
_TnDot1agCfmStackMaIndex_Type = Unsigned32
_TnDot1agCfmStackMaIndex_Object = MibTableColumn
tnDot1agCfmStackMaIndex = _TnDot1agCfmStackMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2, 1, 6),
    _TnDot1agCfmStackMaIndex_Type()
)
tnDot1agCfmStackMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmStackMaIndex.setStatus("current")
_TnDot1agCfmStackMepId_Type = Dot1agCfmMepIdOrZero
_TnDot1agCfmStackMepId_Object = MibTableColumn
tnDot1agCfmStackMepId = _TnDot1agCfmStackMepId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2, 1, 7),
    _TnDot1agCfmStackMepId_Type()
)
tnDot1agCfmStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmStackMepId.setStatus("current")
_TnDot1agCfmStackMacAddress_Type = MacAddress
_TnDot1agCfmStackMacAddress_Object = MibTableColumn
tnDot1agCfmStackMacAddress = _TnDot1agCfmStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2, 1, 8),
    _TnDot1agCfmStackMacAddress_Type()
)
tnDot1agCfmStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmStackMacAddress.setStatus("current")


class _TnDot1agCfmStackMPType_Type(Integer32):
    """Custom type tnDot1agCfmStackMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("ethTun", 2))
    )


_TnDot1agCfmStackMPType_Type.__name__ = "Integer32"
_TnDot1agCfmStackMPType_Object = MibTableColumn
tnDot1agCfmStackMPType = _TnDot1agCfmStackMPType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 1, 2, 1, 9),
    _TnDot1agCfmStackMPType_Type()
)
tnDot1agCfmStackMPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmStackMPType.setStatus("current")
_TnDot1agCfmGlobalObjs_ObjectIdentity = ObjectIdentity
tnDot1agCfmGlobalObjs = _TnDot1agCfmGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2)
)
_TnDot1agCfmMcLagConfigTable_Object = MibTable
tnDot1agCfmMcLagConfigTable = _TnDot1agCfmMcLagConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMcLagConfigTable.setStatus("current")
_TnDot1agCfmMcLagConfigEntry_Object = MibTableRow
tnDot1agCfmMcLagConfigEntry = _TnDot1agCfmMcLagConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 1, 1)
)
tnDot1agCfmMcLagConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnDot1agCfmMcLagConfigEntry.setStatus("current")


class _TnDot1agCfmMcLagConfigStdbyInactive_Type(TruthValue):
    """Custom type tnDot1agCfmMcLagConfigStdbyInactive based on TruthValue"""
    defaultValue = 2


_TnDot1agCfmMcLagConfigStdbyInactive_Type.__name__ = "TruthValue"
_TnDot1agCfmMcLagConfigStdbyInactive_Object = MibTableColumn
tnDot1agCfmMcLagConfigStdbyInactive = _TnDot1agCfmMcLagConfigStdbyInactive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 1, 1, 1),
    _TnDot1agCfmMcLagConfigStdbyInactive_Type()
)
tnDot1agCfmMcLagConfigStdbyInactive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDot1agCfmMcLagConfigStdbyInactive.setStatus("current")


class _TnDot1agCfmMcLagConfigPropHoldTime_Type(Unsigned32):
    """Custom type tnDot1agCfmMcLagConfigPropHoldTime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TnDot1agCfmMcLagConfigPropHoldTime_Type.__name__ = "Unsigned32"
_TnDot1agCfmMcLagConfigPropHoldTime_Object = MibTableColumn
tnDot1agCfmMcLagConfigPropHoldTime = _TnDot1agCfmMcLagConfigPropHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 1, 1, 2),
    _TnDot1agCfmMcLagConfigPropHoldTime_Type()
)
tnDot1agCfmMcLagConfigPropHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDot1agCfmMcLagConfigPropHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMcLagConfigPropHoldTime.setUnits("seconds")
_TnDot1agCfmStatisticsGroup_ObjectIdentity = ObjectIdentity
tnDot1agCfmStatisticsGroup = _TnDot1agCfmStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 3)
)
_TnDot1agCfmComponentLimitTable_Object = MibTable
tnDot1agCfmComponentLimitTable = _TnDot1agCfmComponentLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmComponentLimitTable.setStatus("current")
_TnDot1agCfmComponentLimitEntry_Object = MibTableRow
tnDot1agCfmComponentLimitEntry = _TnDot1agCfmComponentLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 3, 1, 1)
)
tnDot1agCfmComponentLimitEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-IEEE8021-CFM-MIB", "tnDot1agCfmCompMajorIndex"),
    (0, "TN-IEEE8021-CFM-MIB", "tnDot1agCfmCompMinorIndex"),
)
if mibBuilder.loadTexts:
    tnDot1agCfmComponentLimitEntry.setStatus("current")
_TnDot1agCfmCompMajorIndex_Type = Unsigned32
_TnDot1agCfmCompMajorIndex_Object = MibTableColumn
tnDot1agCfmCompMajorIndex = _TnDot1agCfmCompMajorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 3, 1, 1, 1),
    _TnDot1agCfmCompMajorIndex_Type()
)
tnDot1agCfmCompMajorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDot1agCfmCompMajorIndex.setStatus("current")
_TnDot1agCfmCompMinorIndex_Type = Unsigned32
_TnDot1agCfmCompMinorIndex_Object = MibTableColumn
tnDot1agCfmCompMinorIndex = _TnDot1agCfmCompMinorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 3, 1, 1, 2),
    _TnDot1agCfmCompMinorIndex_Type()
)
tnDot1agCfmCompMinorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDot1agCfmCompMinorIndex.setStatus("current")
_TnDot1agCfmCompName_Type = TNamedItem
_TnDot1agCfmCompName_Object = MibTableColumn
tnDot1agCfmCompName = _TnDot1agCfmCompName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 3, 1, 1, 3),
    _TnDot1agCfmCompName_Type()
)
tnDot1agCfmCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmCompName.setStatus("current")
_TnDot1agCfmCompResourceUsage_Type = Unsigned32
_TnDot1agCfmCompResourceUsage_Object = MibTableColumn
tnDot1agCfmCompResourceUsage = _TnDot1agCfmCompResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 3, 1, 1, 4),
    _TnDot1agCfmCompResourceUsage_Type()
)
tnDot1agCfmCompResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmCompResourceUsage.setStatus("current")
_TnDot1agCfmCompResourceLimit_Type = Unsigned32
_TnDot1agCfmCompResourceLimit_Object = MibTableColumn
tnDot1agCfmCompResourceLimit = _TnDot1agCfmCompResourceLimit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 3, 1, 1, 5),
    _TnDot1agCfmCompResourceLimit_Type()
)
tnDot1agCfmCompResourceLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmCompResourceLimit.setStatus("current")
_TnDot1agCfmGlobalScalar1_Type = Unsigned32
_TnDot1agCfmGlobalScalar1_Object = MibScalar
tnDot1agCfmGlobalScalar1 = _TnDot1agCfmGlobalScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 101),
    _TnDot1agCfmGlobalScalar1_Type()
)
tnDot1agCfmGlobalScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmGlobalScalar1.setStatus("current")
_TnDot1agCfmGlobalScalar2_Type = Unsigned32
_TnDot1agCfmGlobalScalar2_Object = MibScalar
tnDot1agCfmGlobalScalar2 = _TnDot1agCfmGlobalScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 2, 102),
    _TnDot1agCfmGlobalScalar2_Type()
)
tnDot1agCfmGlobalScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmGlobalScalar2.setStatus("current")
_TnDot1agCfmMa_ObjectIdentity = ObjectIdentity
tnDot1agCfmMa = _TnDot1agCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 6)
)
_TnDot1agCfmMaNetTable_Object = MibTable
tnDot1agCfmMaNetTable = _TnDot1agCfmMaNetTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 6, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMaNetTable.setStatus("current")
_TnDot1agCfmMaNetEntry_Object = MibTableRow
tnDot1agCfmMaNetEntry = _TnDot1agCfmMaNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMaNetEntry.setStatus("current")
_TnDot1agCfmMaNetTotalMEPCount_Type = Counter32
_TnDot1agCfmMaNetTotalMEPCount_Object = MibTableColumn
tnDot1agCfmMaNetTotalMEPCount = _TnDot1agCfmMaNetTotalMEPCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 6, 1, 1, 1),
    _TnDot1agCfmMaNetTotalMEPCount_Type()
)
tnDot1agCfmMaNetTotalMEPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMaNetTotalMEPCount.setStatus("current")
_TnDot1agCfmMaMepListTable_Object = MibTable
tnDot1agCfmMaMepListTable = _TnDot1agCfmMaMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 6, 3)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMaMepListTable.setStatus("current")
_TnDot1agCfmMaMepListEntry_Object = MibTableRow
tnDot1agCfmMaMepListEntry = _TnDot1agCfmMaMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 6, 3, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMaMepListEntry.setStatus("current")


class _TnDot1agCfmMaMepListMacAddress_Type(MacAddress):
    """Custom type tnDot1agCfmMaMepListMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TnDot1agCfmMaMepListMacAddress_Type.__name__ = "MacAddress"
_TnDot1agCfmMaMepListMacAddress_Object = MibTableColumn
tnDot1agCfmMaMepListMacAddress = _TnDot1agCfmMaMepListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 6, 3, 1, 1),
    _TnDot1agCfmMaMepListMacAddress_Type()
)
tnDot1agCfmMaMepListMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMaMepListMacAddress.setStatus("current")
_TnDot1agCfmMep_ObjectIdentity = ObjectIdentity
tnDot1agCfmMep = _TnDot1agCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7)
)
_TnDot1agCfmMepTable_Object = MibTable
tnDot1agCfmMepTable = _TnDot1agCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepTable.setStatus("current")
_TnDot1agCfmMepEntry_Object = MibTableRow
tnDot1agCfmMepEntry = _TnDot1agCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepEntry.setStatus("current")
_TnDot1agCfmMepSdpId_Type = SdpId
_TnDot1agCfmMepSdpId_Object = MibTableColumn
tnDot1agCfmMepSdpId = _TnDot1agCfmMepSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 1),
    _TnDot1agCfmMepSdpId_Type()
)
tnDot1agCfmMepSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSdpId.setStatus("current")
_TnDot1agCfmMepVcId_Type = Unsigned32
_TnDot1agCfmMepVcId_Object = MibTableColumn
tnDot1agCfmMepVcId = _TnDot1agCfmMepVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 2),
    _TnDot1agCfmMepVcId_Type()
)
tnDot1agCfmMepVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepVcId.setStatus("current")
_TnDot1agCfmMepMacAddress_Type = MacAddress
_TnDot1agCfmMepMacAddress_Object = MibTableColumn
tnDot1agCfmMepMacAddress = _TnDot1agCfmMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 3),
    _TnDot1agCfmMepMacAddress_Type()
)
tnDot1agCfmMepMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepMacAddress.setStatus("current")


class _TnDot1agCfmMepAisEnable_Type(TruthValue):
    """Custom type tnDot1agCfmMepAisEnable based on TruthValue"""
    defaultValue = 2


_TnDot1agCfmMepAisEnable_Type.__name__ = "TruthValue"
_TnDot1agCfmMepAisEnable_Object = MibTableColumn
tnDot1agCfmMepAisEnable = _TnDot1agCfmMepAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 4),
    _TnDot1agCfmMepAisEnable_Type()
)
tnDot1agCfmMepAisEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepAisEnable.setStatus("current")


class _TnDot1agCfmMepAisMegLevel_Type(Bits):
    """Custom type tnDot1agCfmMepAisMegLevel based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("level1", 0),
          ("level2", 1),
          ("level3", 2),
          ("level4", 3),
          ("level5", 4),
          ("level6", 5),
          ("level7", 6))
    )

_TnDot1agCfmMepAisMegLevel_Type.__name__ = "Bits"
_TnDot1agCfmMepAisMegLevel_Object = MibTableColumn
tnDot1agCfmMepAisMegLevel = _TnDot1agCfmMepAisMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 5),
    _TnDot1agCfmMepAisMegLevel_Type()
)
tnDot1agCfmMepAisMegLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepAisMegLevel.setStatus("current")


class _TnDot1agCfmMepAisPriority_Type(Unsigned32):
    """Custom type tnDot1agCfmMepAisPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnDot1agCfmMepAisPriority_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepAisPriority_Object = MibTableColumn
tnDot1agCfmMepAisPriority = _TnDot1agCfmMepAisPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 6),
    _TnDot1agCfmMepAisPriority_Type()
)
tnDot1agCfmMepAisPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepAisPriority.setStatus("current")


class _TnDot1agCfmMepAisInterval_Type(Unsigned32):
    """Custom type tnDot1agCfmMepAisInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(60, 60),
    )


_TnDot1agCfmMepAisInterval_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepAisInterval_Object = MibTableColumn
tnDot1agCfmMepAisInterval = _TnDot1agCfmMepAisInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 7),
    _TnDot1agCfmMepAisInterval_Type()
)
tnDot1agCfmMepAisInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepAisInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepAisInterval.setUnits("seconds")


class _TnDot1agCfmMepEthRxAisInterval_Type(Unsigned32):
    """Custom type tnDot1agCfmMepEthRxAisInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(60, 60),
    )


_TnDot1agCfmMepEthRxAisInterval_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepEthRxAisInterval_Object = MibTableColumn
tnDot1agCfmMepEthRxAisInterval = _TnDot1agCfmMepEthRxAisInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 8),
    _TnDot1agCfmMepEthRxAisInterval_Type()
)
tnDot1agCfmMepEthRxAisInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthRxAisInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthRxAisInterval.setUnits("seconds")


class _TnDot1agCfmMepEthRxAis_Type(TruthValue):
    """Custom type tnDot1agCfmMepEthRxAis based on TruthValue"""
    defaultValue = 2


_TnDot1agCfmMepEthRxAis_Type.__name__ = "TruthValue"
_TnDot1agCfmMepEthRxAis_Object = MibTableColumn
tnDot1agCfmMepEthRxAis = _TnDot1agCfmMepEthRxAis_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 9),
    _TnDot1agCfmMepEthRxAis_Type()
)
tnDot1agCfmMepEthRxAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthRxAis.setStatus("current")
_TnDot1agCfmMepEthAisTxCount_Type = Counter32
_TnDot1agCfmMepEthAisTxCount_Object = MibTableColumn
tnDot1agCfmMepEthAisTxCount = _TnDot1agCfmMepEthAisTxCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 10),
    _TnDot1agCfmMepEthAisTxCount_Type()
)
tnDot1agCfmMepEthAisTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthAisTxCount.setStatus("current")


class _TnDot1agCfmMepEthTestEnable_Type(TruthValue):
    """Custom type tnDot1agCfmMepEthTestEnable based on TruthValue"""
    defaultValue = 2


_TnDot1agCfmMepEthTestEnable_Type.__name__ = "TruthValue"
_TnDot1agCfmMepEthTestEnable_Object = MibTableColumn
tnDot1agCfmMepEthTestEnable = _TnDot1agCfmMepEthTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 11),
    _TnDot1agCfmMepEthTestEnable_Type()
)
tnDot1agCfmMepEthTestEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthTestEnable.setStatus("current")


class _TnDot1agCfmMepEthTestPattern_Type(Integer32):
    """Custom type tnDot1agCfmMepEthTestPattern based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("allZerosNoCrc", 0),
          ("allZerosCrc", 1),
          ("prbsNoCrc", 2),
          ("prbsCrc", 3),
          ("allOnesNoCrc", 4),
          ("allOnesCrc", 5))
    )


_TnDot1agCfmMepEthTestPattern_Type.__name__ = "Integer32"
_TnDot1agCfmMepEthTestPattern_Object = MibTableColumn
tnDot1agCfmMepEthTestPattern = _TnDot1agCfmMepEthTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 12),
    _TnDot1agCfmMepEthTestPattern_Type()
)
tnDot1agCfmMepEthTestPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthTestPattern.setStatus("current")


class _TnDot1agCfmMepEthTestMacAddr_Type(MacAddress):
    """Custom type tnDot1agCfmMepEthTestMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TnDot1agCfmMepEthTestMacAddr_Type.__name__ = "MacAddress"
_TnDot1agCfmMepEthTestMacAddr_Object = MibTableColumn
tnDot1agCfmMepEthTestMacAddr = _TnDot1agCfmMepEthTestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 13),
    _TnDot1agCfmMepEthTestMacAddr_Type()
)
tnDot1agCfmMepEthTestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthTestMacAddr.setStatus("current")


class _TnDot1agCfmMepEthTestDataLen_Type(Unsigned32):
    """Custom type tnDot1agCfmMepEthTestDataLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_TnDot1agCfmMepEthTestDataLen_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepEthTestDataLen_Object = MibTableColumn
tnDot1agCfmMepEthTestDataLen = _TnDot1agCfmMepEthTestDataLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 14),
    _TnDot1agCfmMepEthTestDataLen_Type()
)
tnDot1agCfmMepEthTestDataLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthTestDataLen.setStatus("current")


class _TnDot1agCfmMepEthTestPriority_Type(Unsigned32):
    """Custom type tnDot1agCfmMepEthTestPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnDot1agCfmMepEthTestPriority_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepEthTestPriority_Object = MibTableColumn
tnDot1agCfmMepEthTestPriority = _TnDot1agCfmMepEthTestPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 15),
    _TnDot1agCfmMepEthTestPriority_Type()
)
tnDot1agCfmMepEthTestPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthTestPriority.setStatus("current")


class _TnDot1agCfmMepOWDTMacAddress_Type(MacAddress):
    """Custom type tnDot1agCfmMepOWDTMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TnDot1agCfmMepOWDTMacAddress_Type.__name__ = "MacAddress"
_TnDot1agCfmMepOWDTMacAddress_Object = MibTableColumn
tnDot1agCfmMepOWDTMacAddress = _TnDot1agCfmMepOWDTMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 16),
    _TnDot1agCfmMepOWDTMacAddress_Type()
)
tnDot1agCfmMepOWDTMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOWDTMacAddress.setStatus("current")


class _TnDot1agCfmMepOWDTPriority_Type(Unsigned32):
    """Custom type tnDot1agCfmMepOWDTPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnDot1agCfmMepOWDTPriority_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepOWDTPriority_Object = MibTableColumn
tnDot1agCfmMepOWDTPriority = _TnDot1agCfmMepOWDTPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 17),
    _TnDot1agCfmMepOWDTPriority_Type()
)
tnDot1agCfmMepOWDTPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOWDTPriority.setStatus("current")


class _TnDot1agCfmMepTWDTMacAddress_Type(MacAddress):
    """Custom type tnDot1agCfmMepTWDTMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TnDot1agCfmMepTWDTMacAddress_Type.__name__ = "MacAddress"
_TnDot1agCfmMepTWDTMacAddress_Object = MibTableColumn
tnDot1agCfmMepTWDTMacAddress = _TnDot1agCfmMepTWDTMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 18),
    _TnDot1agCfmMepTWDTMacAddress_Type()
)
tnDot1agCfmMepTWDTMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepTWDTMacAddress.setStatus("current")


class _TnDot1agCfmMepTWDTPriority_Type(Unsigned32):
    """Custom type tnDot1agCfmMepTWDTPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnDot1agCfmMepTWDTPriority_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepTWDTPriority_Object = MibTableColumn
tnDot1agCfmMepTWDTPriority = _TnDot1agCfmMepTWDTPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 19),
    _TnDot1agCfmMepTWDTPriority_Type()
)
tnDot1agCfmMepTWDTPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepTWDTPriority.setStatus("current")
_TnDot1agCfmMepSvcId_Type = TmnxServId
_TnDot1agCfmMepSvcId_Object = MibTableColumn
tnDot1agCfmMepSvcId = _TnDot1agCfmMepSvcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 20),
    _TnDot1agCfmMepSvcId_Type()
)
tnDot1agCfmMepSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSvcId.setStatus("current")


class _TnDot1agCfmMepControlMep_Type(TruthValue):
    """Custom type tnDot1agCfmMepControlMep based on TruthValue"""
    defaultValue = 2


_TnDot1agCfmMepControlMep_Type.__name__ = "TruthValue"
_TnDot1agCfmMepControlMep_Object = MibTableColumn
tnDot1agCfmMepControlMep = _TnDot1agCfmMepControlMep_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 21),
    _TnDot1agCfmMepControlMep_Type()
)
tnDot1agCfmMepControlMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepControlMep.setStatus("current")


class _TnDot1agCfmMepEthTestThreshold_Type(Unsigned32):
    """Custom type tnDot1agCfmMepEthTestThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11840),
    )


_TnDot1agCfmMepEthTestThreshold_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepEthTestThreshold_Object = MibTableColumn
tnDot1agCfmMepEthTestThreshold = _TnDot1agCfmMepEthTestThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 22),
    _TnDot1agCfmMepEthTestThreshold_Type()
)
tnDot1agCfmMepEthTestThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthTestThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepEthTestThreshold.setUnits("bit-errors")


class _TnDot1agCfmMepOWDTThreshold_Type(Unsigned32):
    """Custom type tnDot1agCfmMepOWDTThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TnDot1agCfmMepOWDTThreshold_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepOWDTThreshold_Object = MibTableColumn
tnDot1agCfmMepOWDTThreshold = _TnDot1agCfmMepOWDTThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 23),
    _TnDot1agCfmMepOWDTThreshold_Type()
)
tnDot1agCfmMepOWDTThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOWDTThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOWDTThreshold.setUnits("seconds")


class _TnDot1agCfmMepMcLagInactive_Type(Integer32):
    """Custom type tnDot1agCfmMepMcLagInactive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("standby", 1),
          ("active", 2))
    )


_TnDot1agCfmMepMcLagInactive_Type.__name__ = "Integer32"
_TnDot1agCfmMepMcLagInactive_Object = MibTableColumn
tnDot1agCfmMepMcLagInactive = _TnDot1agCfmMepMcLagInactive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 24),
    _TnDot1agCfmMepMcLagInactive_Type()
)
tnDot1agCfmMepMcLagInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepMcLagInactive.setStatus("current")


class _TnDot1agCfmMepTWDTDataSize_Type(Unsigned32):
    """Custom type tnDot1agCfmMepTWDTDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9542),
    )


_TnDot1agCfmMepTWDTDataSize_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepTWDTDataSize_Object = MibTableColumn
tnDot1agCfmMepTWDTDataSize = _TnDot1agCfmMepTWDTDataSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 1, 1, 25),
    _TnDot1agCfmMepTWDTDataSize_Type()
)
tnDot1agCfmMepTWDTDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepTWDTDataSize.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepTWDTDataSize.setUnits("bytes")
_TnDot1agCfmMepDelayRsltTable_Object = MibTable
tnDot1agCfmMepDelayRsltTable = _TnDot1agCfmMepDelayRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 3)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepDelayRsltTable.setStatus("current")
_TnDot1agCfmMepDelayRsltEntry_Object = MibTableRow
tnDot1agCfmMepDelayRsltEntry = _TnDot1agCfmMepDelayRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 3, 1)
)
tnDot1agCfmMepDelayRsltEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepDelaySrcMacAddr"),
    (0, "TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepDelayTestType"),
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepDelayRsltEntry.setStatus("current")
_TnDot1agCfmMepDelaySrcMacAddr_Type = MacAddress
_TnDot1agCfmMepDelaySrcMacAddr_Object = MibTableColumn
tnDot1agCfmMepDelaySrcMacAddr = _TnDot1agCfmMepDelaySrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 3, 1, 1),
    _TnDot1agCfmMepDelaySrcMacAddr_Type()
)
tnDot1agCfmMepDelaySrcMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDot1agCfmMepDelaySrcMacAddr.setStatus("current")


class _TnDot1agCfmMepDelayTestType_Type(Integer32):
    """Custom type tnDot1agCfmMepDelayTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneWayTest", 1),
          ("twoWayTest", 2))
    )


_TnDot1agCfmMepDelayTestType_Type.__name__ = "Integer32"
_TnDot1agCfmMepDelayTestType_Object = MibTableColumn
tnDot1agCfmMepDelayTestType = _TnDot1agCfmMepDelayTestType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 3, 1, 2),
    _TnDot1agCfmMepDelayTestType_Type()
)
tnDot1agCfmMepDelayTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDot1agCfmMepDelayTestType.setStatus("current")
_TnDot1agCfmMepDelayTestDelay_Type = Integer32
_TnDot1agCfmMepDelayTestDelay_Object = MibTableColumn
tnDot1agCfmMepDelayTestDelay = _TnDot1agCfmMepDelayTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 3, 1, 3),
    _TnDot1agCfmMepDelayTestDelay_Type()
)
tnDot1agCfmMepDelayTestDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepDelayTestDelay.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepDelayTestDelay.setUnits("microseconds")
_TnDot1agCfmMepDelayVariation_Type = Unsigned32
_TnDot1agCfmMepDelayVariation_Object = MibTableColumn
tnDot1agCfmMepDelayVariation = _TnDot1agCfmMepDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 3, 1, 4),
    _TnDot1agCfmMepDelayVariation_Type()
)
tnDot1agCfmMepDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepDelayVariation.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepDelayVariation.setUnits("microseconds")
_TnDot1agCfmMepCsfTable_Object = MibTable
tnDot1agCfmMepCsfTable = _TnDot1agCfmMepCsfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 4)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepCsfTable.setStatus("current")
_TnDot1agCfmMepCsfEntry_Object = MibTableRow
tnDot1agCfmMepCsfEntry = _TnDot1agCfmMepCsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 4, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepCsfEntry.setStatus("current")


class _TnDot1agCfmMepCsfInterval_Type(Dot1agCfmCcmInterval):
    """Custom type tnDot1agCfmMepCsfInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 6


_TnDot1agCfmMepCsfInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_TnDot1agCfmMepCsfInterval_Object = MibTableColumn
tnDot1agCfmMepCsfInterval = _TnDot1agCfmMepCsfInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 4, 1, 1),
    _TnDot1agCfmMepCsfInterval_Type()
)
tnDot1agCfmMepCsfInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepCsfInterval.setStatus("current")


class _TnDot1agCfmMepCsfDirection_Type(Integer32):
    """Custom type tnDot1agCfmMepCsfDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("unidirection", 2),
          ("bi-dirction", 3))
    )


_TnDot1agCfmMepCsfDirection_Type.__name__ = "Integer32"
_TnDot1agCfmMepCsfDirection_Object = MibTableColumn
tnDot1agCfmMepCsfDirection = _TnDot1agCfmMepCsfDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 4, 1, 2),
    _TnDot1agCfmMepCsfDirection_Type()
)
tnDot1agCfmMepCsfDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDot1agCfmMepCsfDirection.setStatus("current")


class _TnDot1agCfmMepCsfPriority_Type(Integer32):
    """Custom type tnDot1agCfmMepCsfPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnDot1agCfmMepCsfPriority_Type.__name__ = "Integer32"
_TnDot1agCfmMepCsfPriority_Object = MibTableColumn
tnDot1agCfmMepCsfPriority = _TnDot1agCfmMepCsfPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 4, 1, 3),
    _TnDot1agCfmMepCsfPriority_Type()
)
tnDot1agCfmMepCsfPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepCsfPriority.setStatus("current")
_TnDot1agCfmMepSlmTWTestTable_Object = MibTable
tnDot1agCfmMepSlmTWTestTable = _TnDot1agCfmMepSlmTWTestTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWTestTable.setStatus("current")
_TnDot1agCfmMepSlmTWTestEntry_Object = MibTableRow
tnDot1agCfmMepSlmTWTestEntry = _TnDot1agCfmMepSlmTWTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWTestEntry.setStatus("current")


class _TnDot1agCfmMepSlmTWTestStatus_Type(TmnxEnabledDisabled):
    """Custom type tnDot1agCfmMepSlmTWTestStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnDot1agCfmMepSlmTWTestStatus_Type.__name__ = "TmnxEnabledDisabled"
_TnDot1agCfmMepSlmTWTestStatus_Object = MibTableColumn
tnDot1agCfmMepSlmTWTestStatus = _TnDot1agCfmMepSlmTWTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1, 1),
    _TnDot1agCfmMepSlmTWTestStatus_Type()
)
tnDot1agCfmMepSlmTWTestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWTestStatus.setStatus("current")
_TnDot1agCfmMepSlmTWTestId_Type = Unsigned32
_TnDot1agCfmMepSlmTWTestId_Object = MibTableColumn
tnDot1agCfmMepSlmTWTestId = _TnDot1agCfmMepSlmTWTestId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1, 2),
    _TnDot1agCfmMepSlmTWTestId_Type()
)
tnDot1agCfmMepSlmTWTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWTestId.setStatus("current")


class _TnDot1agCfmMepSlmTWMacAddress_Type(MacAddress):
    """Custom type tnDot1agCfmMepSlmTWMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TnDot1agCfmMepSlmTWMacAddress_Type.__name__ = "MacAddress"
_TnDot1agCfmMepSlmTWMacAddress_Object = MibTableColumn
tnDot1agCfmMepSlmTWMacAddress = _TnDot1agCfmMepSlmTWMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1, 3),
    _TnDot1agCfmMepSlmTWMacAddress_Type()
)
tnDot1agCfmMepSlmTWMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWMacAddress.setStatus("current")


class _TnDot1agCfmMepSlmTWPriority_Type(Unsigned32):
    """Custom type tnDot1agCfmMepSlmTWPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnDot1agCfmMepSlmTWPriority_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepSlmTWPriority_Object = MibTableColumn
tnDot1agCfmMepSlmTWPriority = _TnDot1agCfmMepSlmTWPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1, 4),
    _TnDot1agCfmMepSlmTWPriority_Type()
)
tnDot1agCfmMepSlmTWPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWPriority.setStatus("current")


class _TnDot1agCfmMepSlmTWInterval_Type(Unsigned32):
    """Custom type tnDot1agCfmMepSlmTWInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_TnDot1agCfmMepSlmTWInterval_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepSlmTWInterval_Object = MibTableColumn
tnDot1agCfmMepSlmTWInterval = _TnDot1agCfmMepSlmTWInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1, 5),
    _TnDot1agCfmMepSlmTWInterval_Type()
)
tnDot1agCfmMepSlmTWInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWInterval.setUnits("seconds")


class _TnDot1agCfmMepSlmTWTimeout_Type(Unsigned32):
    """Custom type tnDot1agCfmMepSlmTWTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnDot1agCfmMepSlmTWTimeout_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepSlmTWTimeout_Object = MibTableColumn
tnDot1agCfmMepSlmTWTimeout = _TnDot1agCfmMepSlmTWTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1, 6),
    _TnDot1agCfmMepSlmTWTimeout_Type()
)
tnDot1agCfmMepSlmTWTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWTimeout.setUnits("seconds")


class _TnDot1agCfmMepSlmTWDataSize_Type(Unsigned32):
    """Custom type tnDot1agCfmMepSlmTWDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9558),
    )


_TnDot1agCfmMepSlmTWDataSize_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepSlmTWDataSize_Object = MibTableColumn
tnDot1agCfmMepSlmTWDataSize = _TnDot1agCfmMepSlmTWDataSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1, 7),
    _TnDot1agCfmMepSlmTWDataSize_Type()
)
tnDot1agCfmMepSlmTWDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWDataSize.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWDataSize.setUnits("bytes")


class _TnDot1agCfmMepSlmTWSendCount_Type(Unsigned32):
    """Custom type tnDot1agCfmMepSlmTWSendCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TnDot1agCfmMepSlmTWSendCount_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepSlmTWSendCount_Object = MibTableColumn
tnDot1agCfmMepSlmTWSendCount = _TnDot1agCfmMepSlmTWSendCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1, 8),
    _TnDot1agCfmMepSlmTWSendCount_Type()
)
tnDot1agCfmMepSlmTWSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWSendCount.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWSendCount.setUnits("packets")


class _TnDot1agCfmMepSlmTWIntervalRedef_Type(Unsigned32):
    """Custom type tnDot1agCfmMepSlmTWIntervalRedef based on Unsigned32"""
    defaultValue = 1


_TnDot1agCfmMepSlmTWIntervalRedef_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepSlmTWIntervalRedef_Object = MibTableColumn
tnDot1agCfmMepSlmTWIntervalRedef = _TnDot1agCfmMepSlmTWIntervalRedef_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1, 9),
    _TnDot1agCfmMepSlmTWIntervalRedef_Type()
)
tnDot1agCfmMepSlmTWIntervalRedef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWIntervalRedef.setStatus("current")


class _TnDot1agCfmMepSlmTWIntrvlUnits_Type(Integer32):
    """Custom type tnDot1agCfmMepSlmTWIntrvlUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("seconds", 1),
          ("centiseconds", 2))
    )


_TnDot1agCfmMepSlmTWIntrvlUnits_Type.__name__ = "Integer32"
_TnDot1agCfmMepSlmTWIntrvlUnits_Object = MibTableColumn
tnDot1agCfmMepSlmTWIntrvlUnits = _TnDot1agCfmMepSlmTWIntrvlUnits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 5, 1, 10),
    _TnDot1agCfmMepSlmTWIntrvlUnits_Type()
)
tnDot1agCfmMepSlmTWIntrvlUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTWIntrvlUnits.setStatus("current")
_TnDot1agCfmMepSlmOWTestTable_Object = MibTable
tnDot1agCfmMepSlmOWTestTable = _TnDot1agCfmMepSlmOWTestTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 6)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWTestTable.setStatus("current")
_TnDot1agCfmMepSlmOWTestEntry_Object = MibTableRow
tnDot1agCfmMepSlmOWTestEntry = _TnDot1agCfmMepSlmOWTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 6, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWTestEntry.setStatus("current")


class _TnDot1agCfmMepSlmOWTestStatus_Type(TmnxEnabledDisabled):
    """Custom type tnDot1agCfmMepSlmOWTestStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnDot1agCfmMepSlmOWTestStatus_Type.__name__ = "TmnxEnabledDisabled"
_TnDot1agCfmMepSlmOWTestStatus_Object = MibTableColumn
tnDot1agCfmMepSlmOWTestStatus = _TnDot1agCfmMepSlmOWTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 6, 1, 1),
    _TnDot1agCfmMepSlmOWTestStatus_Type()
)
tnDot1agCfmMepSlmOWTestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWTestStatus.setStatus("current")
_TnDot1agCfmMepSlmOWTestId_Type = Unsigned32
_TnDot1agCfmMepSlmOWTestId_Object = MibTableColumn
tnDot1agCfmMepSlmOWTestId = _TnDot1agCfmMepSlmOWTestId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 6, 1, 2),
    _TnDot1agCfmMepSlmOWTestId_Type()
)
tnDot1agCfmMepSlmOWTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWTestId.setStatus("current")


class _TnDot1agCfmMepSlmOWMacAddress_Type(MacAddress):
    """Custom type tnDot1agCfmMepSlmOWMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TnDot1agCfmMepSlmOWMacAddress_Type.__name__ = "MacAddress"
_TnDot1agCfmMepSlmOWMacAddress_Object = MibTableColumn
tnDot1agCfmMepSlmOWMacAddress = _TnDot1agCfmMepSlmOWMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 6, 1, 3),
    _TnDot1agCfmMepSlmOWMacAddress_Type()
)
tnDot1agCfmMepSlmOWMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWMacAddress.setStatus("current")


class _TnDot1agCfmMepSlmOWPriority_Type(Unsigned32):
    """Custom type tnDot1agCfmMepSlmOWPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnDot1agCfmMepSlmOWPriority_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepSlmOWPriority_Object = MibTableColumn
tnDot1agCfmMepSlmOWPriority = _TnDot1agCfmMepSlmOWPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 6, 1, 4),
    _TnDot1agCfmMepSlmOWPriority_Type()
)
tnDot1agCfmMepSlmOWPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWPriority.setStatus("current")


class _TnDot1agCfmMepSlmOWInterval_Type(Unsigned32):
    """Custom type tnDot1agCfmMepSlmOWInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnDot1agCfmMepSlmOWInterval_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepSlmOWInterval_Object = MibTableColumn
tnDot1agCfmMepSlmOWInterval = _TnDot1agCfmMepSlmOWInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 6, 1, 5),
    _TnDot1agCfmMepSlmOWInterval_Type()
)
tnDot1agCfmMepSlmOWInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWInterval.setUnits("seconds")


class _TnDot1agCfmMepSlmOWDataSize_Type(Unsigned32):
    """Custom type tnDot1agCfmMepSlmOWDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_TnDot1agCfmMepSlmOWDataSize_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepSlmOWDataSize_Object = MibTableColumn
tnDot1agCfmMepSlmOWDataSize = _TnDot1agCfmMepSlmOWDataSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 6, 1, 6),
    _TnDot1agCfmMepSlmOWDataSize_Type()
)
tnDot1agCfmMepSlmOWDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWDataSize.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWDataSize.setUnits("bytes")


class _TnDot1agCfmMepSlmOWSendCount_Type(Unsigned32):
    """Custom type tnDot1agCfmMepSlmOWSendCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TnDot1agCfmMepSlmOWSendCount_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepSlmOWSendCount_Object = MibTableColumn
tnDot1agCfmMepSlmOWSendCount = _TnDot1agCfmMepSlmOWSendCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 6, 1, 7),
    _TnDot1agCfmMepSlmOWSendCount_Type()
)
tnDot1agCfmMepSlmOWSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWSendCount.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmOWSendCount.setUnits("packets")
_TnDot1agCfmMepSlmTestRsltTable_Object = MibTable
tnDot1agCfmMepSlmTestRsltTable = _TnDot1agCfmMepSlmTestRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTestRsltTable.setStatus("current")
_TnDot1agCfmMepSlmTestRsltEntry_Object = MibTableRow
tnDot1agCfmMepSlmTestRsltEntry = _TnDot1agCfmMepSlmTestRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7, 1)
)
tnDot1agCfmMepSlmTestRsltEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepSlmTestType"),
    (0, "TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepSlmRemoteMacAddr"),
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTestRsltEntry.setStatus("current")


class _TnDot1agCfmMepSlmTestType_Type(Integer32):
    """Custom type tnDot1agCfmMepSlmTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneWayTest", 1),
          ("twoWayTest", 2))
    )


_TnDot1agCfmMepSlmTestType_Type.__name__ = "Integer32"
_TnDot1agCfmMepSlmTestType_Object = MibTableColumn
tnDot1agCfmMepSlmTestType = _TnDot1agCfmMepSlmTestType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7, 1, 1),
    _TnDot1agCfmMepSlmTestType_Type()
)
tnDot1agCfmMepSlmTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTestType.setStatus("current")
_TnDot1agCfmMepSlmRemoteMacAddr_Type = MacAddress
_TnDot1agCfmMepSlmRemoteMacAddr_Object = MibTableColumn
tnDot1agCfmMepSlmRemoteMacAddr = _TnDot1agCfmMepSlmRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7, 1, 2),
    _TnDot1agCfmMepSlmRemoteMacAddr_Type()
)
tnDot1agCfmMepSlmRemoteMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmRemoteMacAddr.setStatus("current")
_TnDot1agCfmMepSlmTestId_Type = Unsigned32
_TnDot1agCfmMepSlmTestId_Object = MibTableColumn
tnDot1agCfmMepSlmTestId = _TnDot1agCfmMepSlmTestId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7, 1, 3),
    _TnDot1agCfmMepSlmTestId_Type()
)
tnDot1agCfmMepSlmTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmTestId.setStatus("current")
_TnDot1agCfmMepSlmRemoteMepId_Type = Dot1agCfmMepId
_TnDot1agCfmMepSlmRemoteMepId_Object = MibTableColumn
tnDot1agCfmMepSlmRemoteMepId = _TnDot1agCfmMepSlmRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7, 1, 4),
    _TnDot1agCfmMepSlmRemoteMepId_Type()
)
tnDot1agCfmMepSlmRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmRemoteMepId.setStatus("current")
_TnDot1agCfmMepSlmLastTxSeqF_Type = Unsigned32
_TnDot1agCfmMepSlmLastTxSeqF_Object = MibTableColumn
tnDot1agCfmMepSlmLastTxSeqF = _TnDot1agCfmMepSlmLastTxSeqF_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7, 1, 5),
    _TnDot1agCfmMepSlmLastTxSeqF_Type()
)
tnDot1agCfmMepSlmLastTxSeqF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmLastTxSeqF.setStatus("current")
_TnDot1agCfmMepSlmPacketIn_Type = Counter32
_TnDot1agCfmMepSlmPacketIn_Object = MibTableColumn
tnDot1agCfmMepSlmPacketIn = _TnDot1agCfmMepSlmPacketIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7, 1, 6),
    _TnDot1agCfmMepSlmPacketIn_Type()
)
tnDot1agCfmMepSlmPacketIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmPacketIn.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmPacketIn.setUnits("packets")
_TnDot1agCfmMepSlmPacketLossIn_Type = Integer32
_TnDot1agCfmMepSlmPacketLossIn_Object = MibTableColumn
tnDot1agCfmMepSlmPacketLossIn = _TnDot1agCfmMepSlmPacketLossIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7, 1, 7),
    _TnDot1agCfmMepSlmPacketLossIn_Type()
)
tnDot1agCfmMepSlmPacketLossIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmPacketLossIn.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmPacketLossIn.setUnits("packets")
_TnDot1agCfmMepSlmPacketLossOut_Type = Integer32
_TnDot1agCfmMepSlmPacketLossOut_Object = MibTableColumn
tnDot1agCfmMepSlmPacketLossOut = _TnDot1agCfmMepSlmPacketLossOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7, 1, 8),
    _TnDot1agCfmMepSlmPacketLossOut_Type()
)
tnDot1agCfmMepSlmPacketLossOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmPacketLossOut.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmPacketLossOut.setUnits("packets")
_TnDot1agCfmMepSlmPacketUnack_Type = Gauge32
_TnDot1agCfmMepSlmPacketUnack_Object = MibTableColumn
tnDot1agCfmMepSlmPacketUnack = _TnDot1agCfmMepSlmPacketUnack_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 7, 1, 9),
    _TnDot1agCfmMepSlmPacketUnack_Type()
)
tnDot1agCfmMepSlmPacketUnack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmPacketUnack.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepSlmPacketUnack.setUnits("packets")
_TnDot1agCfmMepOndemandLmTestTable_Object = MibTable
tnDot1agCfmMepOndemandLmTestTable = _TnDot1agCfmMepOndemandLmTestTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 8)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTestTable.setStatus("current")
_TnDot1agCfmMepOndemandLmTestEntry_Object = MibTableRow
tnDot1agCfmMepOndemandLmTestEntry = _TnDot1agCfmMepOndemandLmTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 8, 1)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTestEntry.setStatus("current")


class _TnDot1agCfmMepOndemandLmTestStatus_Type(TmnxEnabledDisabled):
    """Custom type tnDot1agCfmMepOndemandLmTestStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnDot1agCfmMepOndemandLmTestStatus_Type.__name__ = "TmnxEnabledDisabled"
_TnDot1agCfmMepOndemandLmTestStatus_Object = MibTableColumn
tnDot1agCfmMepOndemandLmTestStatus = _TnDot1agCfmMepOndemandLmTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 8, 1, 1),
    _TnDot1agCfmMepOndemandLmTestStatus_Type()
)
tnDot1agCfmMepOndemandLmTestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTestStatus.setStatus("current")


class _TnDot1agCfmMepOndemandLmDestMacAddress_Type(MacAddress):
    """Custom type tnDot1agCfmMepOndemandLmDestMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TnDot1agCfmMepOndemandLmDestMacAddress_Type.__name__ = "MacAddress"
_TnDot1agCfmMepOndemandLmDestMacAddress_Object = MibTableColumn
tnDot1agCfmMepOndemandLmDestMacAddress = _TnDot1agCfmMepOndemandLmDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 8, 1, 2),
    _TnDot1agCfmMepOndemandLmDestMacAddress_Type()
)
tnDot1agCfmMepOndemandLmDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmDestMacAddress.setStatus("current")


class _TnDot1agCfmMepOndemandLmPriority_Type(Unsigned32):
    """Custom type tnDot1agCfmMepOndemandLmPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnDot1agCfmMepOndemandLmPriority_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepOndemandLmPriority_Object = MibTableColumn
tnDot1agCfmMepOndemandLmPriority = _TnDot1agCfmMepOndemandLmPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 8, 1, 3),
    _TnDot1agCfmMepOndemandLmPriority_Type()
)
tnDot1agCfmMepOndemandLmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmPriority.setStatus("current")


class _TnDot1agCfmMepOndemandLmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type tnDot1agCfmMepOndemandLmInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 4


_TnDot1agCfmMepOndemandLmInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_TnDot1agCfmMepOndemandLmInterval_Object = MibTableColumn
tnDot1agCfmMepOndemandLmInterval = _TnDot1agCfmMepOndemandLmInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 8, 1, 4),
    _TnDot1agCfmMepOndemandLmInterval_Type()
)
tnDot1agCfmMepOndemandLmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmInterval.setStatus("current")


class _TnDot1agCfmMepOndemandLmSendCount_Type(Unsigned32):
    """Custom type tnDot1agCfmMepOndemandLmSendCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 101),
    )


_TnDot1agCfmMepOndemandLmSendCount_Type.__name__ = "Unsigned32"
_TnDot1agCfmMepOndemandLmSendCount_Object = MibTableColumn
tnDot1agCfmMepOndemandLmSendCount = _TnDot1agCfmMepOndemandLmSendCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 8, 1, 5),
    _TnDot1agCfmMepOndemandLmSendCount_Type()
)
tnDot1agCfmMepOndemandLmSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmSendCount.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmSendCount.setUnits("packets")
_TnDot1agCfmMepOndemandLmTestRsltTable_Object = MibTable
tnDot1agCfmMepOndemandLmTestRsltTable = _TnDot1agCfmMepOndemandLmTestRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 9)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTestRsltTable.setStatus("current")
_TnDot1agCfmMepOndemandLmTestRsltEntry_Object = MibTableRow
tnDot1agCfmMepOndemandLmTestRsltEntry = _TnDot1agCfmMepOndemandLmTestRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 9, 1)
)
tnDot1agCfmMepOndemandLmTestRsltEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTestRsltEntry.setStatus("current")
_TnDot1agCfmMepOndemandLmTnTF_Type = Counter32
_TnDot1agCfmMepOndemandLmTnTF_Object = MibTableColumn
tnDot1agCfmMepOndemandLmTnTF = _TnDot1agCfmMepOndemandLmTnTF_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 9, 1, 1),
    _TnDot1agCfmMepOndemandLmTnTF_Type()
)
tnDot1agCfmMepOndemandLmTnTF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTnTF.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTnTF.setUnits("packets")
_TnDot1agCfmMepOndemandLmTnLF_Type = Counter32
_TnDot1agCfmMepOndemandLmTnLF_Object = MibTableColumn
tnDot1agCfmMepOndemandLmTnLF = _TnDot1agCfmMepOndemandLmTnLF_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 9, 1, 2),
    _TnDot1agCfmMepOndemandLmTnLF_Type()
)
tnDot1agCfmMepOndemandLmTnLF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTnLF.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTnLF.setUnits("packets")
_TnDot1agCfmMepOndemandLmTfTF_Type = Counter32
_TnDot1agCfmMepOndemandLmTfTF_Object = MibTableColumn
tnDot1agCfmMepOndemandLmTfTF = _TnDot1agCfmMepOndemandLmTfTF_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 9, 1, 3),
    _TnDot1agCfmMepOndemandLmTfTF_Type()
)
tnDot1agCfmMepOndemandLmTfTF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTfTF.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTfTF.setUnits("packets")
_TnDot1agCfmMepOndemandLmTfLF_Type = Counter32
_TnDot1agCfmMepOndemandLmTfLF_Object = MibTableColumn
tnDot1agCfmMepOndemandLmTfLF = _TnDot1agCfmMepOndemandLmTfLF_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 9, 1, 4),
    _TnDot1agCfmMepOndemandLmTfLF_Type()
)
tnDot1agCfmMepOndemandLmTfLF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTfLF.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTfLF.setUnits("packets")
_TnDot1agCfmMepOndemandLmUnack_Type = Gauge32
_TnDot1agCfmMepOndemandLmUnack_Object = MibTableColumn
tnDot1agCfmMepOndemandLmUnack = _TnDot1agCfmMepOndemandLmUnack_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 9, 1, 5),
    _TnDot1agCfmMepOndemandLmUnack_Type()
)
tnDot1agCfmMepOndemandLmUnack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmUnack.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmUnack.setUnits("packets")
_TnDot1agCfmMepOWDelayRsltExtTable_Object = MibTable
tnDot1agCfmMepOWDelayRsltExtTable = _TnDot1agCfmMepOWDelayRsltExtTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 10)
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepOWDelayRsltExtTable.setStatus("current")
_TnDot1agCfmMepOWDelayRsltExtEntry_Object = MibTableRow
tnDot1agCfmMepOWDelayRsltExtEntry = _TnDot1agCfmMepOWDelayRsltExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 10, 1)
)
tnDot1agCfmMepOWDelayRsltExtEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepOWDelayRsltExtEntry.setStatus("current")
_TnDot1agCfmMepOWDelayRsltExtTnFD_Type = Integer32
_TnDot1agCfmMepOWDelayRsltExtTnFD_Object = MibTableColumn
tnDot1agCfmMepOWDelayRsltExtTnFD = _TnDot1agCfmMepOWDelayRsltExtTnFD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 10, 1, 1),
    _TnDot1agCfmMepOWDelayRsltExtTnFD_Type()
)
tnDot1agCfmMepOWDelayRsltExtTnFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOWDelayRsltExtTnFD.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOWDelayRsltExtTnFD.setUnits("microseconds")
_TnDot1agCfmMepOWDelayRsltExtTnFDV_Type = Integer32
_TnDot1agCfmMepOWDelayRsltExtTnFDV_Object = MibTableColumn
tnDot1agCfmMepOWDelayRsltExtTnFDV = _TnDot1agCfmMepOWDelayRsltExtTnFDV_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 10, 1, 2),
    _TnDot1agCfmMepOWDelayRsltExtTnFDV_Type()
)
tnDot1agCfmMepOWDelayRsltExtTnFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOWDelayRsltExtTnFDV.setStatus("current")
if mibBuilder.loadTexts:
    tnDot1agCfmMepOWDelayRsltExtTnFDV.setUnits("microseconds")
_TnDot1agCfmMepScalar1_Type = Unsigned32
_TnDot1agCfmMepScalar1_Object = MibScalar
tnDot1agCfmMepScalar1 = _TnDot1agCfmMepScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 101),
    _TnDot1agCfmMepScalar1_Type()
)
tnDot1agCfmMepScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepScalar1.setStatus("current")
_TnDot1agCfmMepScalar2_Type = Unsigned32
_TnDot1agCfmMepScalar2_Object = MibScalar
tnDot1agCfmMepScalar2 = _TnDot1agCfmMepScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 52, 7, 102),
    _TnDot1agCfmMepScalar2_Type()
)
tnDot1agCfmMepScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDot1agCfmMepScalar2.setStatus("current")
_TnDot1agNotificationsPrefix_ObjectIdentity = ObjectIdentity
tnDot1agNotificationsPrefix = _TnDot1agNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 52)
)
_TnDot1agNotifications_ObjectIdentity = ObjectIdentity
tnDot1agNotifications = _TnDot1agNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 52, 0)
)
dot1agCfmMaNetEntry.registerAugmentions(
    ("TN-IEEE8021-CFM-MIB",
     "tnDot1agCfmMaNetEntry")
)
tnDot1agCfmMaNetEntry.setIndexNames(*dot1agCfmMaNetEntry.getIndexNames())
dot1agCfmMaMepListEntry.registerAugmentions(
    ("TN-IEEE8021-CFM-MIB",
     "tnDot1agCfmMaMepListEntry")
)
tnDot1agCfmMaMepListEntry.setIndexNames(*dot1agCfmMaMepListEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TN-IEEE8021-CFM-MIB",
     "tnDot1agCfmMepEntry")
)
tnDot1agCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TN-IEEE8021-CFM-MIB",
     "tnDot1agCfmMepCsfEntry")
)
tnDot1agCfmMepCsfEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TN-IEEE8021-CFM-MIB",
     "tnDot1agCfmMepSlmTWTestEntry")
)
tnDot1agCfmMepSlmTWTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TN-IEEE8021-CFM-MIB",
     "tnDot1agCfmMepSlmOWTestEntry")
)
tnDot1agCfmMepSlmOWTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TN-IEEE8021-CFM-MIB",
     "tnDot1agCfmMepOndemandLmTestEntry")
)
tnDot1agCfmMepOndemandLmTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups


# Notification objects

tnDot1agCfmMepLbmTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 52, 0, 1)
)
tnDot1agCfmMepLbmTestComplete.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestMacAddress")
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepLbmTestComplete.setStatus(
        "current"
    )

tnDot1agCfmMepLtmTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 52, 0, 2)
)
tnDot1agCfmMepLtmTestComplete.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmSeqNumber")
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepLtmTestComplete.setStatus(
        "current"
    )

tnDot1agCfmMepDMTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 52, 0, 4)
)
tnDot1agCfmMepDMTestComplete.setObjects(
    ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepDelayTestDelay")
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepDMTestComplete.setStatus(
        "current"
    )

tnDot1agCfmMepAisStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 52, 0, 5)
)
tnDot1agCfmMepAisStateChanged.setObjects(
    ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepEthRxAis")
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepAisStateChanged.setStatus(
        "current"
    )

tnDot1agCfmMepSLMTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 52, 0, 7)
)
tnDot1agCfmMepSLMTestComplete.setObjects(
      *(("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepSlmTestId"),
        ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepSlmRemoteMepId"),
        ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepSlmLastTxSeqF"),
        ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepSlmPacketIn"),
        ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepSlmPacketLossIn"),
        ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepSlmPacketLossOut"),
        ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepSlmPacketUnack"))
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepSLMTestComplete.setStatus(
        "current"
    )

tnDot1agCfmMepOndemandLmTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 52, 0, 8)
)
tnDot1agCfmMepOndemandLmTestComplete.setObjects(
      *(("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepOndemandLmTnTF"),
        ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepOndemandLmTnLF"),
        ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepOndemandLmTfTF"),
        ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepOndemandLmTfLF"),
        ("TN-IEEE8021-CFM-MIB", "tnDot1agCfmMepOndemandLmUnack"))
)
if mibBuilder.loadTexts:
    tnDot1agCfmMepOndemandLmTestComplete.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-IEEE8021-CFM-MIB",
    **{"tnIEEE8021CfmMIBModule": tnIEEE8021CfmMIBModule,
       "tnDot1agMIBObjs": tnDot1agMIBObjs,
       "tnDot1agCfmStack": tnDot1agCfmStack,
       "tnDot1agCfmStackTable": tnDot1agCfmStackTable,
       "tnDot1agCfmStackEntry": tnDot1agCfmStackEntry,
       "tnDot1agCfmStackifIndex": tnDot1agCfmStackifIndex,
       "tnDot1agCfmStackVlanIdOrNone": tnDot1agCfmStackVlanIdOrNone,
       "tnDot1agCfmStackMdLevel": tnDot1agCfmStackMdLevel,
       "tnDot1agCfmStackDirection": tnDot1agCfmStackDirection,
       "tnDot1agCfmStackMdIndex": tnDot1agCfmStackMdIndex,
       "tnDot1agCfmStackMaIndex": tnDot1agCfmStackMaIndex,
       "tnDot1agCfmStackMepId": tnDot1agCfmStackMepId,
       "tnDot1agCfmStackMacAddress": tnDot1agCfmStackMacAddress,
       "tnDot1agCfmStackMPType": tnDot1agCfmStackMPType,
       "tnDot1agCfmGlobalObjs": tnDot1agCfmGlobalObjs,
       "tnDot1agCfmMcLagConfigTable": tnDot1agCfmMcLagConfigTable,
       "tnDot1agCfmMcLagConfigEntry": tnDot1agCfmMcLagConfigEntry,
       "tnDot1agCfmMcLagConfigStdbyInactive": tnDot1agCfmMcLagConfigStdbyInactive,
       "tnDot1agCfmMcLagConfigPropHoldTime": tnDot1agCfmMcLagConfigPropHoldTime,
       "tnDot1agCfmStatisticsGroup": tnDot1agCfmStatisticsGroup,
       "tnDot1agCfmComponentLimitTable": tnDot1agCfmComponentLimitTable,
       "tnDot1agCfmComponentLimitEntry": tnDot1agCfmComponentLimitEntry,
       "tnDot1agCfmCompMajorIndex": tnDot1agCfmCompMajorIndex,
       "tnDot1agCfmCompMinorIndex": tnDot1agCfmCompMinorIndex,
       "tnDot1agCfmCompName": tnDot1agCfmCompName,
       "tnDot1agCfmCompResourceUsage": tnDot1agCfmCompResourceUsage,
       "tnDot1agCfmCompResourceLimit": tnDot1agCfmCompResourceLimit,
       "tnDot1agCfmGlobalScalar1": tnDot1agCfmGlobalScalar1,
       "tnDot1agCfmGlobalScalar2": tnDot1agCfmGlobalScalar2,
       "tnDot1agCfmMa": tnDot1agCfmMa,
       "tnDot1agCfmMaNetTable": tnDot1agCfmMaNetTable,
       "tnDot1agCfmMaNetEntry": tnDot1agCfmMaNetEntry,
       "tnDot1agCfmMaNetTotalMEPCount": tnDot1agCfmMaNetTotalMEPCount,
       "tnDot1agCfmMaMepListTable": tnDot1agCfmMaMepListTable,
       "tnDot1agCfmMaMepListEntry": tnDot1agCfmMaMepListEntry,
       "tnDot1agCfmMaMepListMacAddress": tnDot1agCfmMaMepListMacAddress,
       "tnDot1agCfmMep": tnDot1agCfmMep,
       "tnDot1agCfmMepTable": tnDot1agCfmMepTable,
       "tnDot1agCfmMepEntry": tnDot1agCfmMepEntry,
       "tnDot1agCfmMepSdpId": tnDot1agCfmMepSdpId,
       "tnDot1agCfmMepVcId": tnDot1agCfmMepVcId,
       "tnDot1agCfmMepMacAddress": tnDot1agCfmMepMacAddress,
       "tnDot1agCfmMepAisEnable": tnDot1agCfmMepAisEnable,
       "tnDot1agCfmMepAisMegLevel": tnDot1agCfmMepAisMegLevel,
       "tnDot1agCfmMepAisPriority": tnDot1agCfmMepAisPriority,
       "tnDot1agCfmMepAisInterval": tnDot1agCfmMepAisInterval,
       "tnDot1agCfmMepEthRxAisInterval": tnDot1agCfmMepEthRxAisInterval,
       "tnDot1agCfmMepEthRxAis": tnDot1agCfmMepEthRxAis,
       "tnDot1agCfmMepEthAisTxCount": tnDot1agCfmMepEthAisTxCount,
       "tnDot1agCfmMepEthTestEnable": tnDot1agCfmMepEthTestEnable,
       "tnDot1agCfmMepEthTestPattern": tnDot1agCfmMepEthTestPattern,
       "tnDot1agCfmMepEthTestMacAddr": tnDot1agCfmMepEthTestMacAddr,
       "tnDot1agCfmMepEthTestDataLen": tnDot1agCfmMepEthTestDataLen,
       "tnDot1agCfmMepEthTestPriority": tnDot1agCfmMepEthTestPriority,
       "tnDot1agCfmMepOWDTMacAddress": tnDot1agCfmMepOWDTMacAddress,
       "tnDot1agCfmMepOWDTPriority": tnDot1agCfmMepOWDTPriority,
       "tnDot1agCfmMepTWDTMacAddress": tnDot1agCfmMepTWDTMacAddress,
       "tnDot1agCfmMepTWDTPriority": tnDot1agCfmMepTWDTPriority,
       "tnDot1agCfmMepSvcId": tnDot1agCfmMepSvcId,
       "tnDot1agCfmMepControlMep": tnDot1agCfmMepControlMep,
       "tnDot1agCfmMepEthTestThreshold": tnDot1agCfmMepEthTestThreshold,
       "tnDot1agCfmMepOWDTThreshold": tnDot1agCfmMepOWDTThreshold,
       "tnDot1agCfmMepMcLagInactive": tnDot1agCfmMepMcLagInactive,
       "tnDot1agCfmMepTWDTDataSize": tnDot1agCfmMepTWDTDataSize,
       "tnDot1agCfmMepDelayRsltTable": tnDot1agCfmMepDelayRsltTable,
       "tnDot1agCfmMepDelayRsltEntry": tnDot1agCfmMepDelayRsltEntry,
       "tnDot1agCfmMepDelaySrcMacAddr": tnDot1agCfmMepDelaySrcMacAddr,
       "tnDot1agCfmMepDelayTestType": tnDot1agCfmMepDelayTestType,
       "tnDot1agCfmMepDelayTestDelay": tnDot1agCfmMepDelayTestDelay,
       "tnDot1agCfmMepDelayVariation": tnDot1agCfmMepDelayVariation,
       "tnDot1agCfmMepCsfTable": tnDot1agCfmMepCsfTable,
       "tnDot1agCfmMepCsfEntry": tnDot1agCfmMepCsfEntry,
       "tnDot1agCfmMepCsfInterval": tnDot1agCfmMepCsfInterval,
       "tnDot1agCfmMepCsfDirection": tnDot1agCfmMepCsfDirection,
       "tnDot1agCfmMepCsfPriority": tnDot1agCfmMepCsfPriority,
       "tnDot1agCfmMepSlmTWTestTable": tnDot1agCfmMepSlmTWTestTable,
       "tnDot1agCfmMepSlmTWTestEntry": tnDot1agCfmMepSlmTWTestEntry,
       "tnDot1agCfmMepSlmTWTestStatus": tnDot1agCfmMepSlmTWTestStatus,
       "tnDot1agCfmMepSlmTWTestId": tnDot1agCfmMepSlmTWTestId,
       "tnDot1agCfmMepSlmTWMacAddress": tnDot1agCfmMepSlmTWMacAddress,
       "tnDot1agCfmMepSlmTWPriority": tnDot1agCfmMepSlmTWPriority,
       "tnDot1agCfmMepSlmTWInterval": tnDot1agCfmMepSlmTWInterval,
       "tnDot1agCfmMepSlmTWTimeout": tnDot1agCfmMepSlmTWTimeout,
       "tnDot1agCfmMepSlmTWDataSize": tnDot1agCfmMepSlmTWDataSize,
       "tnDot1agCfmMepSlmTWSendCount": tnDot1agCfmMepSlmTWSendCount,
       "tnDot1agCfmMepSlmTWIntervalRedef": tnDot1agCfmMepSlmTWIntervalRedef,
       "tnDot1agCfmMepSlmTWIntrvlUnits": tnDot1agCfmMepSlmTWIntrvlUnits,
       "tnDot1agCfmMepSlmOWTestTable": tnDot1agCfmMepSlmOWTestTable,
       "tnDot1agCfmMepSlmOWTestEntry": tnDot1agCfmMepSlmOWTestEntry,
       "tnDot1agCfmMepSlmOWTestStatus": tnDot1agCfmMepSlmOWTestStatus,
       "tnDot1agCfmMepSlmOWTestId": tnDot1agCfmMepSlmOWTestId,
       "tnDot1agCfmMepSlmOWMacAddress": tnDot1agCfmMepSlmOWMacAddress,
       "tnDot1agCfmMepSlmOWPriority": tnDot1agCfmMepSlmOWPriority,
       "tnDot1agCfmMepSlmOWInterval": tnDot1agCfmMepSlmOWInterval,
       "tnDot1agCfmMepSlmOWDataSize": tnDot1agCfmMepSlmOWDataSize,
       "tnDot1agCfmMepSlmOWSendCount": tnDot1agCfmMepSlmOWSendCount,
       "tnDot1agCfmMepSlmTestRsltTable": tnDot1agCfmMepSlmTestRsltTable,
       "tnDot1agCfmMepSlmTestRsltEntry": tnDot1agCfmMepSlmTestRsltEntry,
       "tnDot1agCfmMepSlmTestType": tnDot1agCfmMepSlmTestType,
       "tnDot1agCfmMepSlmRemoteMacAddr": tnDot1agCfmMepSlmRemoteMacAddr,
       "tnDot1agCfmMepSlmTestId": tnDot1agCfmMepSlmTestId,
       "tnDot1agCfmMepSlmRemoteMepId": tnDot1agCfmMepSlmRemoteMepId,
       "tnDot1agCfmMepSlmLastTxSeqF": tnDot1agCfmMepSlmLastTxSeqF,
       "tnDot1agCfmMepSlmPacketIn": tnDot1agCfmMepSlmPacketIn,
       "tnDot1agCfmMepSlmPacketLossIn": tnDot1agCfmMepSlmPacketLossIn,
       "tnDot1agCfmMepSlmPacketLossOut": tnDot1agCfmMepSlmPacketLossOut,
       "tnDot1agCfmMepSlmPacketUnack": tnDot1agCfmMepSlmPacketUnack,
       "tnDot1agCfmMepOndemandLmTestTable": tnDot1agCfmMepOndemandLmTestTable,
       "tnDot1agCfmMepOndemandLmTestEntry": tnDot1agCfmMepOndemandLmTestEntry,
       "tnDot1agCfmMepOndemandLmTestStatus": tnDot1agCfmMepOndemandLmTestStatus,
       "tnDot1agCfmMepOndemandLmDestMacAddress": tnDot1agCfmMepOndemandLmDestMacAddress,
       "tnDot1agCfmMepOndemandLmPriority": tnDot1agCfmMepOndemandLmPriority,
       "tnDot1agCfmMepOndemandLmInterval": tnDot1agCfmMepOndemandLmInterval,
       "tnDot1agCfmMepOndemandLmSendCount": tnDot1agCfmMepOndemandLmSendCount,
       "tnDot1agCfmMepOndemandLmTestRsltTable": tnDot1agCfmMepOndemandLmTestRsltTable,
       "tnDot1agCfmMepOndemandLmTestRsltEntry": tnDot1agCfmMepOndemandLmTestRsltEntry,
       "tnDot1agCfmMepOndemandLmTnTF": tnDot1agCfmMepOndemandLmTnTF,
       "tnDot1agCfmMepOndemandLmTnLF": tnDot1agCfmMepOndemandLmTnLF,
       "tnDot1agCfmMepOndemandLmTfTF": tnDot1agCfmMepOndemandLmTfTF,
       "tnDot1agCfmMepOndemandLmTfLF": tnDot1agCfmMepOndemandLmTfLF,
       "tnDot1agCfmMepOndemandLmUnack": tnDot1agCfmMepOndemandLmUnack,
       "tnDot1agCfmMepOWDelayRsltExtTable": tnDot1agCfmMepOWDelayRsltExtTable,
       "tnDot1agCfmMepOWDelayRsltExtEntry": tnDot1agCfmMepOWDelayRsltExtEntry,
       "tnDot1agCfmMepOWDelayRsltExtTnFD": tnDot1agCfmMepOWDelayRsltExtTnFD,
       "tnDot1agCfmMepOWDelayRsltExtTnFDV": tnDot1agCfmMepOWDelayRsltExtTnFDV,
       "tnDot1agCfmMepScalar1": tnDot1agCfmMepScalar1,
       "tnDot1agCfmMepScalar2": tnDot1agCfmMepScalar2,
       "tnDot1agNotificationsPrefix": tnDot1agNotificationsPrefix,
       "tnDot1agNotifications": tnDot1agNotifications,
       "tnDot1agCfmMepLbmTestComplete": tnDot1agCfmMepLbmTestComplete,
       "tnDot1agCfmMepLtmTestComplete": tnDot1agCfmMepLtmTestComplete,
       "tnDot1agCfmMepDMTestComplete": tnDot1agCfmMepDMTestComplete,
       "tnDot1agCfmMepAisStateChanged": tnDot1agCfmMepAisStateChanged,
       "tnDot1agCfmMepSLMTestComplete": tnDot1agCfmMepSLMTestComplete,
       "tnDot1agCfmMepOndemandLmTestComplete": tnDot1agCfmMepOndemandLmTestComplete}
)
