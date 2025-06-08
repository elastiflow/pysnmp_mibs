# SNMP MIB module (ALU-IEEE8021-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/ALU-IEEE8021-CFM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:55:46 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
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

(tmnxDot1agCfmMepEntry,) = mibBuilder.importSymbols(
    "TIMETRA-IEEE8021-CFM-MIB",
    "tmnxDot1agCfmMepEntry")

(SdpId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId")

(TmnxServId,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TmnxServId")


# MODULE-IDENTITY

aluIEEE8021CfmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    aluIEEE8021CfmMIBModule.setRevisions(
        ("1909-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TLossRatioHundrethsOfPercent(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_AluDot1agCfmMIBConformance_ObjectIdentity = ObjectIdentity
aluDot1agCfmMIBConformance = _AluDot1agCfmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10)
)
_AluDot1agCfmConformance_ObjectIdentity = ObjectIdentity
aluDot1agCfmConformance = _AluDot1agCfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10, 1)
)
_AluDot1agCfmCompliances_ObjectIdentity = ObjectIdentity
aluDot1agCfmCompliances = _AluDot1agCfmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10, 1, 1)
)
_AluDot1agComp7705_ObjectIdentity = ObjectIdentity
aluDot1agComp7705 = _AluDot1agComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10, 1, 1, 1)
)
_AluDot1agCfmGroups_ObjectIdentity = ObjectIdentity
aluDot1agCfmGroups = _AluDot1agCfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10, 1, 2)
)
_AluDot1agObjs_ObjectIdentity = ObjectIdentity
aluDot1agObjs = _AluDot1agObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10)
)
_AluDot1agCfmMepObjs_ObjectIdentity = ObjectIdentity
aluDot1agCfmMepObjs = _AluDot1agCfmMepObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1)
)
_AluExtDot1agCfmMepTable_Object = MibTable
aluExtDot1agCfmMepTable = _AluExtDot1agCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepTable.setStatus("current")
_AluExtDot1agCfmMepEntry_Object = MibTableRow
aluExtDot1agCfmMepEntry = _AluExtDot1agCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepEntry.setStatus("current")


class _AluExtDot1agCfmMepSingleLMMacAddress_Type(MacAddress):
    """Custom type aluExtDot1agCfmMepSingleLMMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_AluExtDot1agCfmMepSingleLMMacAddress_Type.__name__ = "MacAddress"
_AluExtDot1agCfmMepSingleLMMacAddress_Object = MibTableColumn
aluExtDot1agCfmMepSingleLMMacAddress = _AluExtDot1agCfmMepSingleLMMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 1),
    _AluExtDot1agCfmMepSingleLMMacAddress_Type()
)
aluExtDot1agCfmMepSingleLMMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepSingleLMMacAddress.setStatus("current")


class _AluExtDot1agCfmMepSingleLMPriority_Type(Unsigned32):
    """Custom type aluExtDot1agCfmMepSingleLMPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AluExtDot1agCfmMepSingleLMPriority_Type.__name__ = "Unsigned32"
_AluExtDot1agCfmMepSingleLMPriority_Object = MibTableColumn
aluExtDot1agCfmMepSingleLMPriority = _AluExtDot1agCfmMepSingleLMPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 2),
    _AluExtDot1agCfmMepSingleLMPriority_Type()
)
aluExtDot1agCfmMepSingleLMPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepSingleLMPriority.setStatus("current")


class _AluExtDot1agCfmMepSingleLMCount_Type(Unsigned32):
    """Custom type aluExtDot1agCfmMepSingleLMCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_AluExtDot1agCfmMepSingleLMCount_Type.__name__ = "Unsigned32"
_AluExtDot1agCfmMepSingleLMCount_Object = MibTableColumn
aluExtDot1agCfmMepSingleLMCount = _AluExtDot1agCfmMepSingleLMCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 3),
    _AluExtDot1agCfmMepSingleLMCount_Type()
)
aluExtDot1agCfmMepSingleLMCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepSingleLMCount.setStatus("current")


class _AluExtDot1agCfmMepSingleLMInterval_Type(Unsigned32):
    """Custom type aluExtDot1agCfmMepSingleLMInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_AluExtDot1agCfmMepSingleLMInterval_Type.__name__ = "Unsigned32"
_AluExtDot1agCfmMepSingleLMInterval_Object = MibTableColumn
aluExtDot1agCfmMepSingleLMInterval = _AluExtDot1agCfmMepSingleLMInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 4),
    _AluExtDot1agCfmMepSingleLMInterval_Type()
)
aluExtDot1agCfmMepSingleLMInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepSingleLMInterval.setStatus("current")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepSingleLMInterval.setUnits("milliseconds")


class _AluExtDot1agCfmMepDualLMEnable_Type(TruthValue):
    """Custom type aluExtDot1agCfmMepDualLMEnable based on TruthValue"""
    defaultValue = 2


_AluExtDot1agCfmMepDualLMEnable_Type.__name__ = "TruthValue"
_AluExtDot1agCfmMepDualLMEnable_Object = MibTableColumn
aluExtDot1agCfmMepDualLMEnable = _AluExtDot1agCfmMepDualLMEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 5),
    _AluExtDot1agCfmMepDualLMEnable_Type()
)
aluExtDot1agCfmMepDualLMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepDualLMEnable.setStatus("current")


class _AluExtDot1agCfmMepDualLMAlarmThreshold_Type(TLossRatioHundrethsOfPercent):
    """Custom type aluExtDot1agCfmMepDualLMAlarmThreshold based on TLossRatioHundrethsOfPercent"""
    defaultValue = 25


_AluExtDot1agCfmMepDualLMAlarmThreshold_Type.__name__ = "TLossRatioHundrethsOfPercent"
_AluExtDot1agCfmMepDualLMAlarmThreshold_Object = MibTableColumn
aluExtDot1agCfmMepDualLMAlarmThreshold = _AluExtDot1agCfmMepDualLMAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 6),
    _AluExtDot1agCfmMepDualLMAlarmThreshold_Type()
)
aluExtDot1agCfmMepDualLMAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepDualLMAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepDualLMAlarmThreshold.setUnits("hundredth of a percent")
_AluExtDot1agCfmMepDmrRepliesSent_Type = Counter32
_AluExtDot1agCfmMepDmrRepliesSent_Object = MibTableColumn
aluExtDot1agCfmMepDmrRepliesSent = _AluExtDot1agCfmMepDmrRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 7),
    _AluExtDot1agCfmMepDmrRepliesSent_Type()
)
aluExtDot1agCfmMepDmrRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepDmrRepliesSent.setStatus("current")
_AluExtDot1agCfmMepLmrRepliesSent_Type = Counter32
_AluExtDot1agCfmMepLmrRepliesSent_Object = MibTableColumn
aluExtDot1agCfmMepLmrRepliesSent = _AluExtDot1agCfmMepLmrRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 8),
    _AluExtDot1agCfmMepLmrRepliesSent_Type()
)
aluExtDot1agCfmMepLmrRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepLmrRepliesSent.setStatus("current")
_AluExtDot1agCfmMepLbrOutNoTLV_Type = Counter32
_AluExtDot1agCfmMepLbrOutNoTLV_Object = MibTableColumn
aluExtDot1agCfmMepLbrOutNoTLV = _AluExtDot1agCfmMepLbrOutNoTLV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 9),
    _AluExtDot1agCfmMepLbrOutNoTLV_Type()
)
aluExtDot1agCfmMepLbrOutNoTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepLbrOutNoTLV.setStatus("obsolete")
_AluExtDot1agCfmMepLbrOutWithTLV_Type = Counter32
_AluExtDot1agCfmMepLbrOutWithTLV_Object = MibTableColumn
aluExtDot1agCfmMepLbrOutWithTLV = _AluExtDot1agCfmMepLbrOutWithTLV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 10),
    _AluExtDot1agCfmMepLbrOutWithTLV_Type()
)
aluExtDot1agCfmMepLbrOutWithTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepLbrOutWithTLV.setStatus("obsolete")
_AluExtDot1agCfmMepLbByMdaNum_Type = Unsigned32
_AluExtDot1agCfmMepLbByMdaNum_Object = MibTableColumn
aluExtDot1agCfmMepLbByMdaNum = _AluExtDot1agCfmMepLbByMdaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 11),
    _AluExtDot1agCfmMepLbByMdaNum_Type()
)
aluExtDot1agCfmMepLbByMdaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepLbByMdaNum.setStatus("current")


class _AluExtDot1agCfmMepLmAlarmClearThreshold_Type(TLossRatioHundrethsOfPercent):
    """Custom type aluExtDot1agCfmMepLmAlarmClearThreshold based on TLossRatioHundrethsOfPercent"""
    defaultValue = 0


_AluExtDot1agCfmMepLmAlarmClearThreshold_Type.__name__ = "TLossRatioHundrethsOfPercent"
_AluExtDot1agCfmMepLmAlarmClearThreshold_Object = MibTableColumn
aluExtDot1agCfmMepLmAlarmClearThreshold = _AluExtDot1agCfmMepLmAlarmClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 12),
    _AluExtDot1agCfmMepLmAlarmClearThreshold_Type()
)
aluExtDot1agCfmMepLmAlarmClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepLmAlarmClearThreshold.setStatus("current")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepLmAlarmClearThreshold.setUnits("hundredth of a percent")
_AluExtDot1agCfmMepLbrOutFastPath_Type = Counter32
_AluExtDot1agCfmMepLbrOutFastPath_Object = MibTableColumn
aluExtDot1agCfmMepLbrOutFastPath = _AluExtDot1agCfmMepLbrOutFastPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 13),
    _AluExtDot1agCfmMepLbrOutFastPath_Type()
)
aluExtDot1agCfmMepLbrOutFastPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepLbrOutFastPath.setStatus("current")
_AluExtDot1agCfmMepLbrOutSlowPath_Type = Counter32
_AluExtDot1agCfmMepLbrOutSlowPath_Object = MibTableColumn
aluExtDot1agCfmMepLbrOutSlowPath = _AluExtDot1agCfmMepLbrOutSlowPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 1, 1, 14),
    _AluExtDot1agCfmMepLbrOutSlowPath_Type()
)
aluExtDot1agCfmMepLbrOutSlowPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtDot1agCfmMepLbrOutSlowPath.setStatus("current")
_AluDot1agCfmMepLossRsltTable_Object = MibTable
aluDot1agCfmMepLossRsltTable = _AluDot1agCfmMepLossRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    aluDot1agCfmMepLossRsltTable.setStatus("current")
_AluDot1agCfmMepLossRsltEntry_Object = MibTableRow
aluDot1agCfmMepLossRsltEntry = _AluDot1agCfmMepLossRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1)
)
aluDot1agCfmMepLossRsltEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmMacAddr"),
    (0, "ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmType"),
)
if mibBuilder.loadTexts:
    aluDot1agCfmMepLossRsltEntry.setStatus("current")
_AluDot1agCfmMepLmMacAddr_Type = MacAddress
_AluDot1agCfmMepLmMacAddr_Object = MibTableColumn
aluDot1agCfmMepLmMacAddr = _AluDot1agCfmMepLmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 1),
    _AluDot1agCfmMepLmMacAddr_Type()
)
aluDot1agCfmMepLmMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmMacAddr.setStatus("current")


class _AluDot1agCfmMepLmType_Type(Integer32):
    """Custom type aluDot1agCfmMepLmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleEndedLm", 1),
          ("dualEndedLm", 2))
    )


_AluDot1agCfmMepLmType_Type.__name__ = "Integer32"
_AluDot1agCfmMepLmType_Object = MibTableColumn
aluDot1agCfmMepLmType = _AluDot1agCfmMepLmType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 2),
    _AluDot1agCfmMepLmType_Type()
)
aluDot1agCfmMepLmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmType.setStatus("current")
_AluDot1agCfmMepLmEnableDuration_Type = Unsigned32
_AluDot1agCfmMepLmEnableDuration_Object = MibTableColumn
aluDot1agCfmMepLmEnableDuration = _AluDot1agCfmMepLmEnableDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 3),
    _AluDot1agCfmMepLmEnableDuration_Type()
)
aluDot1agCfmMepLmEnableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmEnableDuration.setStatus("current")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmEnableDuration.setUnits("seconds")
_AluDot1agCfmMepLmChangeCount_Type = Unsigned32
_AluDot1agCfmMepLmChangeCount_Object = MibTableColumn
aluDot1agCfmMepLmChangeCount = _AluDot1agCfmMepLmChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 4),
    _AluDot1agCfmMepLmChangeCount_Type()
)
aluDot1agCfmMepLmChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmChangeCount.setStatus("current")
_AluDot1agCfmMepLmLatestChangeTime_Type = TimeStamp
_AluDot1agCfmMepLmLatestChangeTime_Object = MibTableColumn
aluDot1agCfmMepLmLatestChangeTime = _AluDot1agCfmMepLmLatestChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 5),
    _AluDot1agCfmMepLmLatestChangeTime_Type()
)
aluDot1agCfmMepLmLatestChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmLatestChangeTime.setStatus("current")
_AluDot1agCfmMepLmFramesRxLocal_Type = Counter64
_AluDot1agCfmMepLmFramesRxLocal_Object = MibTableColumn
aluDot1agCfmMepLmFramesRxLocal = _AluDot1agCfmMepLmFramesRxLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 6),
    _AluDot1agCfmMepLmFramesRxLocal_Type()
)
aluDot1agCfmMepLmFramesRxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmFramesRxLocal.setStatus("current")
_AluDot1agCfmMepLmFramesRxPeer_Type = Counter64
_AluDot1agCfmMepLmFramesRxPeer_Object = MibTableColumn
aluDot1agCfmMepLmFramesRxPeer = _AluDot1agCfmMepLmFramesRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 7),
    _AluDot1agCfmMepLmFramesRxPeer_Type()
)
aluDot1agCfmMepLmFramesRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmFramesRxPeer.setStatus("current")
_AluDot1agCfmMepLmFramesTxLocal_Type = Counter64
_AluDot1agCfmMepLmFramesTxLocal_Object = MibTableColumn
aluDot1agCfmMepLmFramesTxLocal = _AluDot1agCfmMepLmFramesTxLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 8),
    _AluDot1agCfmMepLmFramesTxLocal_Type()
)
aluDot1agCfmMepLmFramesTxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmFramesTxLocal.setStatus("current")
_AluDot1agCfmMepLmFramesTxPeer_Type = Counter64
_AluDot1agCfmMepLmFramesTxPeer_Object = MibTableColumn
aluDot1agCfmMepLmFramesTxPeer = _AluDot1agCfmMepLmFramesTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 9),
    _AluDot1agCfmMepLmFramesTxPeer_Type()
)
aluDot1agCfmMepLmFramesTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmFramesTxPeer.setStatus("current")
_AluDot1agCfmMepLmFramesLossLocal_Type = Counter64
_AluDot1agCfmMepLmFramesLossLocal_Object = MibTableColumn
aluDot1agCfmMepLmFramesLossLocal = _AluDot1agCfmMepLmFramesLossLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 10),
    _AluDot1agCfmMepLmFramesLossLocal_Type()
)
aluDot1agCfmMepLmFramesLossLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmFramesLossLocal.setStatus("current")
_AluDot1agCfmMepLmFramesLossPeer_Type = Counter64
_AluDot1agCfmMepLmFramesLossPeer_Object = MibTableColumn
aluDot1agCfmMepLmFramesLossPeer = _AluDot1agCfmMepLmFramesLossPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 11),
    _AluDot1agCfmMepLmFramesLossPeer_Type()
)
aluDot1agCfmMepLmFramesLossPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmFramesLossPeer.setStatus("current")
_AluDot1agCfmMepLmLossRatioLocal_Type = TLossRatioHundrethsOfPercent
_AluDot1agCfmMepLmLossRatioLocal_Object = MibTableColumn
aluDot1agCfmMepLmLossRatioLocal = _AluDot1agCfmMepLmLossRatioLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 12),
    _AluDot1agCfmMepLmLossRatioLocal_Type()
)
aluDot1agCfmMepLmLossRatioLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmLossRatioLocal.setStatus("current")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmLossRatioLocal.setUnits("hundredth of a percent")
_AluDot1agCfmMepLmLossRatioPeer_Type = TLossRatioHundrethsOfPercent
_AluDot1agCfmMepLmLossRatioPeer_Object = MibTableColumn
aluDot1agCfmMepLmLossRatioPeer = _AluDot1agCfmMepLmLossRatioPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 13),
    _AluDot1agCfmMepLmLossRatioPeer_Type()
)
aluDot1agCfmMepLmLossRatioPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmLossRatioPeer.setStatus("current")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmLossRatioPeer.setUnits("hundredth of a percent")
_AluDot1agCfmMepLmPrevTxLocal_Type = Counter32
_AluDot1agCfmMepLmPrevTxLocal_Object = MibTableColumn
aluDot1agCfmMepLmPrevTxLocal = _AluDot1agCfmMepLmPrevTxLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 14),
    _AluDot1agCfmMepLmPrevTxLocal_Type()
)
aluDot1agCfmMepLmPrevTxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmPrevTxLocal.setStatus("current")
_AluDot1agCfmMepLmPrevRxLocal_Type = Counter32
_AluDot1agCfmMepLmPrevRxLocal_Object = MibTableColumn
aluDot1agCfmMepLmPrevRxLocal = _AluDot1agCfmMepLmPrevRxLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 15),
    _AluDot1agCfmMepLmPrevRxLocal_Type()
)
aluDot1agCfmMepLmPrevRxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmPrevRxLocal.setStatus("current")
_AluDot1agCfmMepLmPrevTxPeer_Type = Counter32
_AluDot1agCfmMepLmPrevTxPeer_Object = MibTableColumn
aluDot1agCfmMepLmPrevTxPeer = _AluDot1agCfmMepLmPrevTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 16),
    _AluDot1agCfmMepLmPrevTxPeer_Type()
)
aluDot1agCfmMepLmPrevTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmPrevTxPeer.setStatus("current")
_AluDot1agCfmMepLmPrevRxPeer_Type = Counter32
_AluDot1agCfmMepLmPrevRxPeer_Object = MibTableColumn
aluDot1agCfmMepLmPrevRxPeer = _AluDot1agCfmMepLmPrevRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 17),
    _AluDot1agCfmMepLmPrevRxPeer_Type()
)
aluDot1agCfmMepLmPrevRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmPrevRxPeer.setStatus("current")
_AluDot1agCfmMepLmCurrTxLocal_Type = Counter32
_AluDot1agCfmMepLmCurrTxLocal_Object = MibTableColumn
aluDot1agCfmMepLmCurrTxLocal = _AluDot1agCfmMepLmCurrTxLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 18),
    _AluDot1agCfmMepLmCurrTxLocal_Type()
)
aluDot1agCfmMepLmCurrTxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmCurrTxLocal.setStatus("current")
_AluDot1agCfmMepLmCurrRxLocal_Type = Counter32
_AluDot1agCfmMepLmCurrRxLocal_Object = MibTableColumn
aluDot1agCfmMepLmCurrRxLocal = _AluDot1agCfmMepLmCurrRxLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 19),
    _AluDot1agCfmMepLmCurrRxLocal_Type()
)
aluDot1agCfmMepLmCurrRxLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmCurrRxLocal.setStatus("current")
_AluDot1agCfmMepLmCurrTxPeer_Type = Counter32
_AluDot1agCfmMepLmCurrTxPeer_Object = MibTableColumn
aluDot1agCfmMepLmCurrTxPeer = _AluDot1agCfmMepLmCurrTxPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 20),
    _AluDot1agCfmMepLmCurrTxPeer_Type()
)
aluDot1agCfmMepLmCurrTxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmCurrTxPeer.setStatus("current")
_AluDot1agCfmMepLmCurrRxPeer_Type = Counter32
_AluDot1agCfmMepLmCurrRxPeer_Object = MibTableColumn
aluDot1agCfmMepLmCurrRxPeer = _AluDot1agCfmMepLmCurrRxPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 1, 2, 1, 21),
    _AluDot1agCfmMepLmCurrRxPeer_Type()
)
aluDot1agCfmMepLmCurrRxPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmCurrRxPeer.setStatus("current")
_AluDot1agCfmNotificationObjs_ObjectIdentity = ObjectIdentity
aluDot1agCfmNotificationObjs = _AluDot1agCfmNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 10, 2)
)
_AluDot1agCfmNotifyPrefix_ObjectIdentity = ObjectIdentity
aluDot1agCfmNotifyPrefix = _AluDot1agCfmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 6)
)
_AluDot1agCfmNotification_ObjectIdentity = ObjectIdentity
aluDot1agCfmNotification = _AluDot1agCfmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 6, 0)
)
dot1agCfmMepEntry.registerAugmentions(
    ("ALU-IEEE8021-CFM-MIB",
     "aluExtDot1agCfmMepEntry")
)
aluExtDot1agCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups

aluDot1agCfmMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10, 1, 2, 2)
)
aluDot1agCfmMepGroup.setObjects(
      *(("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepSingleLMMacAddress"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepSingleLMPriority"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepSingleLMCount"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepSingleLMInterval"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepDualLMEnable"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepDualLMAlarmThreshold"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepDmrRepliesSent"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLmrRepliesSent"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmEnableDuration"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmChangeCount"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLatestChangeTime"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesRxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesRxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesTxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesTxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesLossLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesLossPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLossRatioLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLossRatioPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmPrevTxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmPrevRxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmPrevTxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmPrevRxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmCurrTxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmCurrRxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmCurrTxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmCurrRxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLbrOutNoTLV"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLbrOutWithTLV"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLbByMdaNum"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLmAlarmClearThreshold"))
)
if mibBuilder.loadTexts:
    aluDot1agCfmMepGroup.setStatus("obsolete")

aluDot1agCfmMepGroupV5v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10, 1, 2, 3)
)
aluDot1agCfmMepGroupV5v0.setObjects(
      *(("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepSingleLMMacAddress"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepSingleLMPriority"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepSingleLMCount"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepSingleLMInterval"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepDualLMEnable"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepDualLMAlarmThreshold"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepDmrRepliesSent"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLmrRepliesSent"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmEnableDuration"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmChangeCount"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLatestChangeTime"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesRxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesRxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesTxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesTxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesLossLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmFramesLossPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLossRatioLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLossRatioPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmPrevTxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmPrevRxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmPrevTxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmPrevRxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmCurrTxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmCurrRxLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmCurrTxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmCurrRxPeer"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLbrOutFastPath"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLbrOutSlowPath"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLbByMdaNum"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLmAlarmClearThreshold"))
)
if mibBuilder.loadTexts:
    aluDot1agCfmMepGroupV5v0.setStatus("current")

aluDot1agCfmMepObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10, 1, 2, 4)
)
aluDot1agCfmMepObsoletedGroup.setObjects(
      *(("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLbrOutNoTLV"),
        ("ALU-IEEE8021-CFM-MIB", "aluExtDot1agCfmMepLbrOutWithTLV"))
)
if mibBuilder.loadTexts:
    aluDot1agCfmMepObsoletedGroup.setStatus("current")


# Notification objects

aluDot1agCfmMepLmComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 6, 0, 1)
)
aluDot1agCfmMepLmComplete.setObjects(
      *(("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLossRatioLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLossRatioPeer"))
)
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmComplete.setStatus(
        "current"
    )

aluDot1agCfmMepLmAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 6, 0, 2)
)
aluDot1agCfmMepLmAlarm.setObjects(
      *(("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLossRatioLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLossRatioPeer"))
)
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmAlarm.setStatus(
        "current"
    )

aluDot1agCfmMepLmAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 6, 0, 3)
)
aluDot1agCfmMepLmAlarmClear.setObjects(
      *(("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLossRatioLocal"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmLossRatioPeer"))
)
if mibBuilder.loadTexts:
    aluDot1agCfmMepLmAlarmClear.setStatus(
        "current"
    )


# Notifications groups

aluY1731CfmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10, 1, 2, 1)
)
aluY1731CfmNotificationGroup.setObjects(
      *(("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmComplete"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmAlarm"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepLmAlarmClear"))
)
if mibBuilder.loadTexts:
    aluY1731CfmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluDot1agComp7705V1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10, 1, 1, 1, 1)
)
aluDot1agComp7705V1v0.setObjects(
      *(("ALU-IEEE8021-CFM-MIB", "aluY1731CfmNotificationGroup"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepGroup"))
)
if mibBuilder.loadTexts:
    aluDot1agComp7705V1v0.setStatus(
        "obsolete"
    )

aluDot1agComp7705V5v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 10, 1, 1, 1, 2)
)
aluDot1agComp7705V5v0.setObjects(
      *(("ALU-IEEE8021-CFM-MIB", "aluY1731CfmNotificationGroup"),
        ("ALU-IEEE8021-CFM-MIB", "aluDot1agCfmMepGroupV5v0"))
)
if mibBuilder.loadTexts:
    aluDot1agComp7705V5v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-IEEE8021-CFM-MIB",
    **{"TLossRatioHundrethsOfPercent": TLossRatioHundrethsOfPercent,
       "aluIEEE8021CfmMIBModule": aluIEEE8021CfmMIBModule,
       "aluDot1agCfmMIBConformance": aluDot1agCfmMIBConformance,
       "aluDot1agCfmConformance": aluDot1agCfmConformance,
       "aluDot1agCfmCompliances": aluDot1agCfmCompliances,
       "aluDot1agComp7705": aluDot1agComp7705,
       "aluDot1agComp7705V1v0": aluDot1agComp7705V1v0,
       "aluDot1agComp7705V5v0": aluDot1agComp7705V5v0,
       "aluDot1agCfmGroups": aluDot1agCfmGroups,
       "aluY1731CfmNotificationGroup": aluY1731CfmNotificationGroup,
       "aluDot1agCfmMepGroup": aluDot1agCfmMepGroup,
       "aluDot1agCfmMepGroupV5v0": aluDot1agCfmMepGroupV5v0,
       "aluDot1agCfmMepObsoletedGroup": aluDot1agCfmMepObsoletedGroup,
       "aluDot1agObjs": aluDot1agObjs,
       "aluDot1agCfmMepObjs": aluDot1agCfmMepObjs,
       "aluExtDot1agCfmMepTable": aluExtDot1agCfmMepTable,
       "aluExtDot1agCfmMepEntry": aluExtDot1agCfmMepEntry,
       "aluExtDot1agCfmMepSingleLMMacAddress": aluExtDot1agCfmMepSingleLMMacAddress,
       "aluExtDot1agCfmMepSingleLMPriority": aluExtDot1agCfmMepSingleLMPriority,
       "aluExtDot1agCfmMepSingleLMCount": aluExtDot1agCfmMepSingleLMCount,
       "aluExtDot1agCfmMepSingleLMInterval": aluExtDot1agCfmMepSingleLMInterval,
       "aluExtDot1agCfmMepDualLMEnable": aluExtDot1agCfmMepDualLMEnable,
       "aluExtDot1agCfmMepDualLMAlarmThreshold": aluExtDot1agCfmMepDualLMAlarmThreshold,
       "aluExtDot1agCfmMepDmrRepliesSent": aluExtDot1agCfmMepDmrRepliesSent,
       "aluExtDot1agCfmMepLmrRepliesSent": aluExtDot1agCfmMepLmrRepliesSent,
       "aluExtDot1agCfmMepLbrOutNoTLV": aluExtDot1agCfmMepLbrOutNoTLV,
       "aluExtDot1agCfmMepLbrOutWithTLV": aluExtDot1agCfmMepLbrOutWithTLV,
       "aluExtDot1agCfmMepLbByMdaNum": aluExtDot1agCfmMepLbByMdaNum,
       "aluExtDot1agCfmMepLmAlarmClearThreshold": aluExtDot1agCfmMepLmAlarmClearThreshold,
       "aluExtDot1agCfmMepLbrOutFastPath": aluExtDot1agCfmMepLbrOutFastPath,
       "aluExtDot1agCfmMepLbrOutSlowPath": aluExtDot1agCfmMepLbrOutSlowPath,
       "aluDot1agCfmMepLossRsltTable": aluDot1agCfmMepLossRsltTable,
       "aluDot1agCfmMepLossRsltEntry": aluDot1agCfmMepLossRsltEntry,
       "aluDot1agCfmMepLmMacAddr": aluDot1agCfmMepLmMacAddr,
       "aluDot1agCfmMepLmType": aluDot1agCfmMepLmType,
       "aluDot1agCfmMepLmEnableDuration": aluDot1agCfmMepLmEnableDuration,
       "aluDot1agCfmMepLmChangeCount": aluDot1agCfmMepLmChangeCount,
       "aluDot1agCfmMepLmLatestChangeTime": aluDot1agCfmMepLmLatestChangeTime,
       "aluDot1agCfmMepLmFramesRxLocal": aluDot1agCfmMepLmFramesRxLocal,
       "aluDot1agCfmMepLmFramesRxPeer": aluDot1agCfmMepLmFramesRxPeer,
       "aluDot1agCfmMepLmFramesTxLocal": aluDot1agCfmMepLmFramesTxLocal,
       "aluDot1agCfmMepLmFramesTxPeer": aluDot1agCfmMepLmFramesTxPeer,
       "aluDot1agCfmMepLmFramesLossLocal": aluDot1agCfmMepLmFramesLossLocal,
       "aluDot1agCfmMepLmFramesLossPeer": aluDot1agCfmMepLmFramesLossPeer,
       "aluDot1agCfmMepLmLossRatioLocal": aluDot1agCfmMepLmLossRatioLocal,
       "aluDot1agCfmMepLmLossRatioPeer": aluDot1agCfmMepLmLossRatioPeer,
       "aluDot1agCfmMepLmPrevTxLocal": aluDot1agCfmMepLmPrevTxLocal,
       "aluDot1agCfmMepLmPrevRxLocal": aluDot1agCfmMepLmPrevRxLocal,
       "aluDot1agCfmMepLmPrevTxPeer": aluDot1agCfmMepLmPrevTxPeer,
       "aluDot1agCfmMepLmPrevRxPeer": aluDot1agCfmMepLmPrevRxPeer,
       "aluDot1agCfmMepLmCurrTxLocal": aluDot1agCfmMepLmCurrTxLocal,
       "aluDot1agCfmMepLmCurrRxLocal": aluDot1agCfmMepLmCurrRxLocal,
       "aluDot1agCfmMepLmCurrTxPeer": aluDot1agCfmMepLmCurrTxPeer,
       "aluDot1agCfmMepLmCurrRxPeer": aluDot1agCfmMepLmCurrRxPeer,
       "aluDot1agCfmNotificationObjs": aluDot1agCfmNotificationObjs,
       "aluDot1agCfmNotifyPrefix": aluDot1agCfmNotifyPrefix,
       "aluDot1agCfmNotification": aluDot1agCfmNotification,
       "aluDot1agCfmMepLmComplete": aluDot1agCfmMepLmComplete,
       "aluDot1agCfmMepLmAlarm": aluDot1agCfmMepLmAlarm,
       "aluDot1agCfmMepLmAlarmClear": aluDot1agCfmMepLmAlarmClear}
)
