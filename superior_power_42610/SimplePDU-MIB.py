# SNMP MIB module (SimplePDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/superior_power_42610/SimplePDU-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:03:30 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(NonNegativeInteger,
 PositiveInteger) = mibBuilder.importSymbols(
    "UPS-MIB",
    "NonNegativeInteger",
    "PositiveInteger")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Powertek_ObjectIdentity = ObjectIdentity
powertek = _Powertek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1)
)
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4)
)
_Simple_ObjectIdentity = ObjectIdentity
simple = _Simple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2)
)
_PduObjects_ObjectIdentity = ObjectIdentity
pduObjects = _PduObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1)
)
_PduSumOverview_ObjectIdentity = ObjectIdentity
pduSumOverview = _PduSumOverview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1)
)
_PduSysOverview_ObjectIdentity = ObjectIdentity
pduSysOverview = _PduSysOverview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1)
)
_PduOverview_ObjectIdentity = ObjectIdentity
pduOverview = _PduOverview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 1)
)


class _PduOverviewSystemAgenetVersion_Type(DisplayString):
    """Custom type pduOverviewSystemAgenetVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduOverviewSystemAgenetVersion_Type.__name__ = "DisplayString"
_PduOverviewSystemAgenetVersion_Object = MibScalar
pduOverviewSystemAgenetVersion = _PduOverviewSystemAgenetVersion_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 1, 1),
    _PduOverviewSystemAgenetVersion_Type()
)
pduOverviewSystemAgenetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOverviewSystemAgenetVersion.setStatus("mandatory")


class _PduOverviewPduTypeName_Type(DisplayString):
    """Custom type pduOverviewPduTypeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduOverviewPduTypeName_Type.__name__ = "DisplayString"
_PduOverviewPduTypeName_Object = MibScalar
pduOverviewPduTypeName = _PduOverviewPduTypeName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 1, 2),
    _PduOverviewPduTypeName_Type()
)
pduOverviewPduTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOverviewPduTypeName.setStatus("mandatory")
_PduInputStat_ObjectIdentity = ObjectIdentity
pduInputStat = _PduInputStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2)
)
_PduInputStatTable_Object = MibTable
pduInputStatTable = _PduInputStatTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pduInputStatTable.setStatus("mandatory")
_PduInputStatEntry_Object = MibTableRow
pduInputStatEntry = _PduInputStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 1, 1)
)
pduInputStatEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduInputStatPhaseIndex"),
)
if mibBuilder.loadTexts:
    pduInputStatEntry.setStatus("mandatory")


class _PduInputStatPhaseIndex_Type(Integer32):
    """Custom type pduInputStatPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PduInputStatPhaseIndex_Type.__name__ = "Integer32"
_PduInputStatPhaseIndex_Object = MibTableColumn
pduInputStatPhaseIndex = _PduInputStatPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 1, 1, 1),
    _PduInputStatPhaseIndex_Type()
)
pduInputStatPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatPhaseIndex.setStatus("mandatory")
_PduInputStatVoltage_Type = Integer32
_PduInputStatVoltage_Object = MibTableColumn
pduInputStatVoltage = _PduInputStatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 1, 1, 2),
    _PduInputStatVoltage_Type()
)
pduInputStatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduInputStatVoltage.setUnits("0.1V")
_PduInputStatActivePower_Type = Integer32
_PduInputStatActivePower_Object = MibTableColumn
pduInputStatActivePower = _PduInputStatActivePower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 1, 1, 3),
    _PduInputStatActivePower_Type()
)
pduInputStatActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatActivePower.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduInputStatActivePower.setUnits("0.1W")
_PduInputStatApparentPower_Type = Integer32
_PduInputStatApparentPower_Object = MibTableColumn
pduInputStatApparentPower = _PduInputStatApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 1, 1, 4),
    _PduInputStatApparentPower_Type()
)
pduInputStatApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatApparentPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduInputStatApparentPower.setUnits("0.1VA")
_PduInputStatCB1Current_Type = Integer32
_PduInputStatCB1Current_Object = MibTableColumn
pduInputStatCB1Current = _PduInputStatCB1Current_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 1, 1, 5),
    _PduInputStatCB1Current_Type()
)
pduInputStatCB1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatCB1Current.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduInputStatCB1Current.setUnits("0.01A")
_PduInputStatCB2Current_Type = Integer32
_PduInputStatCB2Current_Object = MibTableColumn
pduInputStatCB2Current = _PduInputStatCB2Current_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 1, 1, 6),
    _PduInputStatCB2Current_Type()
)
pduInputStatCB2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatCB2Current.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduInputStatCB2Current.setUnits("0.01A")
_PduInputStatTotalCurrent_Type = Integer32
_PduInputStatTotalCurrent_Object = MibTableColumn
pduInputStatTotalCurrent = _PduInputStatTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 1, 1, 7),
    _PduInputStatTotalCurrent_Type()
)
pduInputStatTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatTotalCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduInputStatTotalCurrent.setUnits("0.01A")


class _PduInputStatStatus_Type(Integer32):
    """Custom type pduInputStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduInputStatStatus_Type.__name__ = "Integer32"
_PduInputStatStatus_Object = MibTableColumn
pduInputStatStatus = _PduInputStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 1, 1, 8),
    _PduInputStatStatus_Type()
)
pduInputStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatStatus.setStatus("mandatory")
_PduInputStatLoadBalanceVal_Type = Integer32
_PduInputStatLoadBalanceVal_Object = MibScalar
pduInputStatLoadBalanceVal = _PduInputStatLoadBalanceVal_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 2),
    _PduInputStatLoadBalanceVal_Type()
)
pduInputStatLoadBalanceVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatLoadBalanceVal.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduInputStatLoadBalanceVal.setUnits("%")


class _PduInputStatLoadBalanceStatus_Type(Integer32):
    """Custom type pduInputStatLoadBalanceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduInputStatLoadBalanceStatus_Type.__name__ = "Integer32"
_PduInputStatLoadBalanceStatus_Object = MibScalar
pduInputStatLoadBalanceStatus = _PduInputStatLoadBalanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 3),
    _PduInputStatLoadBalanceStatus_Type()
)
pduInputStatLoadBalanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatLoadBalanceStatus.setStatus("mandatory")
_PduInputStatResidualCurVal_Type = Integer32
_PduInputStatResidualCurVal_Object = MibScalar
pduInputStatResidualCurVal = _PduInputStatResidualCurVal_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 4),
    _PduInputStatResidualCurVal_Type()
)
pduInputStatResidualCurVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatResidualCurVal.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduInputStatResidualCurVal.setUnits("0.01A")


class _PduInputStatResidualCurStatus_Type(Integer32):
    """Custom type pduInputStatResidualCurStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduInputStatResidualCurStatus_Type.__name__ = "Integer32"
_PduInputStatResidualCurStatus_Object = MibScalar
pduInputStatResidualCurStatus = _PduInputStatResidualCurStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 1, 2, 5),
    _PduInputStatResidualCurStatus_Type()
)
pduInputStatResidualCurStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputStatResidualCurStatus.setStatus("mandatory")
_PduNetConnect_ObjectIdentity = ObjectIdentity
pduNetConnect = _PduNetConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 2)
)
_PduNetConnectTable_Object = MibTable
pduNetConnectTable = _PduNetConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pduNetConnectTable.setStatus("mandatory")
_PduNetConnectEntry_Object = MibTableRow
pduNetConnectEntry = _PduNetConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 2, 1, 1)
)
pduNetConnectEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduNetConnectIndex"),
)
if mibBuilder.loadTexts:
    pduNetConnectEntry.setStatus("mandatory")


class _PduNetConnectIndex_Type(Integer32):
    """Custom type pduNetConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PduNetConnectIndex_Type.__name__ = "Integer32"
_PduNetConnectIndex_Object = MibTableColumn
pduNetConnectIndex = _PduNetConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 2, 1, 1, 1),
    _PduNetConnectIndex_Type()
)
pduNetConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNetConnectIndex.setStatus("mandatory")
_PduNetConnectAddr_Type = DisplayString
_PduNetConnectAddr_Object = MibTableColumn
pduNetConnectAddr = _PduNetConnectAddr_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 2, 1, 1, 2),
    _PduNetConnectAddr_Type()
)
pduNetConnectAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNetConnectAddr.setStatus("mandatory")
_PduNetConnectType_Type = Integer32
_PduNetConnectType_Object = MibTableColumn
pduNetConnectType = _PduNetConnectType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 2, 1, 1, 3),
    _PduNetConnectType_Type()
)
pduNetConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNetConnectType.setStatus("mandatory")
_PduNetConnectUserName_Type = DisplayString
_PduNetConnectUserName_Object = MibTableColumn
pduNetConnectUserName = _PduNetConnectUserName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 1, 2, 1, 1, 4),
    _PduNetConnectUserName_Type()
)
pduNetConnectUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNetConnectUserName.setStatus("mandatory")
_PduPowMgmt_ObjectIdentity = ObjectIdentity
pduPowMgmt = _PduPowMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2)
)
_PduInletCfg_ObjectIdentity = ObjectIdentity
pduInletCfg = _PduInletCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1)
)
_PduPhaseLoadMgmt_ObjectIdentity = ObjectIdentity
pduPhaseLoadMgmt = _PduPhaseLoadMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1)
)
_PduPhaseLoadMgmtTable_Object = MibTable
pduPhaseLoadMgmtTable = _PduPhaseLoadMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtTable.setStatus("mandatory")
_PduPhaseLoadMgmtEntry_Object = MibTableRow
pduPhaseLoadMgmtEntry = _PduPhaseLoadMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1, 1, 1)
)
pduPhaseLoadMgmtEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduPhaseLoadMgmtPhaseIndex"),
)
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtEntry.setStatus("mandatory")


class _PduPhaseLoadMgmtPhaseIndex_Type(Integer32):
    """Custom type pduPhaseLoadMgmtPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PduPhaseLoadMgmtPhaseIndex_Type.__name__ = "Integer32"
_PduPhaseLoadMgmtPhaseIndex_Object = MibTableColumn
pduPhaseLoadMgmtPhaseIndex = _PduPhaseLoadMgmtPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1, 1, 1, 1),
    _PduPhaseLoadMgmtPhaseIndex_Type()
)
pduPhaseLoadMgmtPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtPhaseIndex.setStatus("mandatory")
_PduPhaseLoadMgmtCurrentTotal_Type = Integer32
_PduPhaseLoadMgmtCurrentTotal_Object = MibTableColumn
pduPhaseLoadMgmtCurrentTotal = _PduPhaseLoadMgmtCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1, 1, 1, 2),
    _PduPhaseLoadMgmtCurrentTotal_Type()
)
pduPhaseLoadMgmtCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtCurrentTotal.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtCurrentTotal.setUnits("0.01A")
_PduPhaseLoadMgmtVoltage_Type = Integer32
_PduPhaseLoadMgmtVoltage_Object = MibTableColumn
pduPhaseLoadMgmtVoltage = _PduPhaseLoadMgmtVoltage_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1, 1, 1, 3),
    _PduPhaseLoadMgmtVoltage_Type()
)
pduPhaseLoadMgmtVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtVoltage.setUnits("0.1V")
_PduPhaseLoadMgmtFrequency_Type = Integer32
_PduPhaseLoadMgmtFrequency_Object = MibTableColumn
pduPhaseLoadMgmtFrequency = _PduPhaseLoadMgmtFrequency_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1, 1, 1, 4),
    _PduPhaseLoadMgmtFrequency_Type()
)
pduPhaseLoadMgmtFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtFrequency.setUnits("0.01Hz")
_PduPhaseLoadMgmtPowerFactor_Type = Integer32
_PduPhaseLoadMgmtPowerFactor_Object = MibTableColumn
pduPhaseLoadMgmtPowerFactor = _PduPhaseLoadMgmtPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1, 1, 1, 5),
    _PduPhaseLoadMgmtPowerFactor_Type()
)
pduPhaseLoadMgmtPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtPowerFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtPowerFactor.setUnits("%")
_PduPhaseLoadMgmtPowerActiveApparent_Type = DisplayString
_PduPhaseLoadMgmtPowerActiveApparent_Object = MibTableColumn
pduPhaseLoadMgmtPowerActiveApparent = _PduPhaseLoadMgmtPowerActiveApparent_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1, 1, 1, 6),
    _PduPhaseLoadMgmtPowerActiveApparent_Type()
)
pduPhaseLoadMgmtPowerActiveApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtPowerActiveApparent.setStatus("mandatory")
_PduPhaseLoadMgmtReactivePower_Type = Integer32
_PduPhaseLoadMgmtReactivePower_Object = MibTableColumn
pduPhaseLoadMgmtReactivePower = _PduPhaseLoadMgmtReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1, 1, 1, 7),
    _PduPhaseLoadMgmtReactivePower_Type()
)
pduPhaseLoadMgmtReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtReactivePower.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtReactivePower.setUnits("0.1var")


class _PduPhaseLoadMgmtStatus_Type(Integer32):
    """Custom type pduPhaseLoadMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduPhaseLoadMgmtStatus_Type.__name__ = "Integer32"
_PduPhaseLoadMgmtStatus_Object = MibTableColumn
pduPhaseLoadMgmtStatus = _PduPhaseLoadMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 1, 1, 1, 8),
    _PduPhaseLoadMgmtStatus_Type()
)
pduPhaseLoadMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseLoadMgmtStatus.setStatus("mandatory")
_PduCfg_ObjectIdentity = ObjectIdentity
pduCfg = _PduCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2)
)


class _PduCfgCritOverLoadAlm_Type(Integer32):
    """Custom type pduCfgCritOverLoadAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 140800),
    )


_PduCfgCritOverLoadAlm_Type.__name__ = "Integer32"
_PduCfgCritOverLoadAlm_Object = MibScalar
pduCfgCritOverLoadAlm = _PduCfgCritOverLoadAlm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 1),
    _PduCfgCritOverLoadAlm_Type()
)
pduCfgCritOverLoadAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgCritOverLoadAlm.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgCritOverLoadAlm.setUnits("0.1W")


class _PduCfgCritLoadBalanceAlm_Type(Integer32):
    """Custom type pduCfgCritLoadBalanceAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PduCfgCritLoadBalanceAlm_Type.__name__ = "Integer32"
_PduCfgCritLoadBalanceAlm_Object = MibScalar
pduCfgCritLoadBalanceAlm = _PduCfgCritLoadBalanceAlm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 2),
    _PduCfgCritLoadBalanceAlm_Type()
)
pduCfgCritLoadBalanceAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgCritLoadBalanceAlm.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgCritLoadBalanceAlm.setUnits("0.1%")


class _PduCfgCritOverCurrAlmCB1Ph1_Type(Integer32):
    """Custom type pduCfgCritOverCurrAlmCB1Ph1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgCritOverCurrAlmCB1Ph1_Type.__name__ = "Integer32"
_PduCfgCritOverCurrAlmCB1Ph1_Object = MibScalar
pduCfgCritOverCurrAlmCB1Ph1 = _PduCfgCritOverCurrAlmCB1Ph1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 3),
    _PduCfgCritOverCurrAlmCB1Ph1_Type()
)
pduCfgCritOverCurrAlmCB1Ph1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB1Ph1.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB1Ph1.setUnits("0.01A")


class _PduCfgCritOverCurrAlmCB1Ph2_Type(Integer32):
    """Custom type pduCfgCritOverCurrAlmCB1Ph2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgCritOverCurrAlmCB1Ph2_Type.__name__ = "Integer32"
_PduCfgCritOverCurrAlmCB1Ph2_Object = MibScalar
pduCfgCritOverCurrAlmCB1Ph2 = _PduCfgCritOverCurrAlmCB1Ph2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 4),
    _PduCfgCritOverCurrAlmCB1Ph2_Type()
)
pduCfgCritOverCurrAlmCB1Ph2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB1Ph2.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB1Ph2.setUnits("0.01A")


class _PduCfgCritOverCurrAlmCB1Ph3_Type(Integer32):
    """Custom type pduCfgCritOverCurrAlmCB1Ph3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgCritOverCurrAlmCB1Ph3_Type.__name__ = "Integer32"
_PduCfgCritOverCurrAlmCB1Ph3_Object = MibScalar
pduCfgCritOverCurrAlmCB1Ph3 = _PduCfgCritOverCurrAlmCB1Ph3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 5),
    _PduCfgCritOverCurrAlmCB1Ph3_Type()
)
pduCfgCritOverCurrAlmCB1Ph3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB1Ph3.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB1Ph3.setUnits("0.01A")


class _PduCfgCritOverCurrAlmCB2Ph1_Type(Integer32):
    """Custom type pduCfgCritOverCurrAlmCB2Ph1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgCritOverCurrAlmCB2Ph1_Type.__name__ = "Integer32"
_PduCfgCritOverCurrAlmCB2Ph1_Object = MibScalar
pduCfgCritOverCurrAlmCB2Ph1 = _PduCfgCritOverCurrAlmCB2Ph1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 6),
    _PduCfgCritOverCurrAlmCB2Ph1_Type()
)
pduCfgCritOverCurrAlmCB2Ph1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB2Ph1.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB2Ph1.setUnits("0.01A")


class _PduCfgCritOverCurrAlmCB2Ph2_Type(Integer32):
    """Custom type pduCfgCritOverCurrAlmCB2Ph2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgCritOverCurrAlmCB2Ph2_Type.__name__ = "Integer32"
_PduCfgCritOverCurrAlmCB2Ph2_Object = MibScalar
pduCfgCritOverCurrAlmCB2Ph2 = _PduCfgCritOverCurrAlmCB2Ph2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 7),
    _PduCfgCritOverCurrAlmCB2Ph2_Type()
)
pduCfgCritOverCurrAlmCB2Ph2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB2Ph2.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB2Ph2.setUnits("0.01A")


class _PduCfgCritOverCurrAlmCB2Ph3_Type(Integer32):
    """Custom type pduCfgCritOverCurrAlmCB2Ph3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgCritOverCurrAlmCB2Ph3_Type.__name__ = "Integer32"
_PduCfgCritOverCurrAlmCB2Ph3_Object = MibScalar
pduCfgCritOverCurrAlmCB2Ph3 = _PduCfgCritOverCurrAlmCB2Ph3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 8),
    _PduCfgCritOverCurrAlmCB2Ph3_Type()
)
pduCfgCritOverCurrAlmCB2Ph3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB2Ph3.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgCritOverCurrAlmCB2Ph3.setUnits("0.01A")


class _PduCfgCritOverTotalCurrAlm_Type(Integer32):
    """Custom type pduCfgCritOverTotalCurrAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgCritOverTotalCurrAlm_Type.__name__ = "Integer32"
_PduCfgCritOverTotalCurrAlm_Object = MibScalar
pduCfgCritOverTotalCurrAlm = _PduCfgCritOverTotalCurrAlm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 9),
    _PduCfgCritOverTotalCurrAlm_Type()
)
pduCfgCritOverTotalCurrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgCritOverTotalCurrAlm.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgCritOverTotalCurrAlm.setUnits("0.01A")


class _PduCfgCritOverVolAlm_Type(Integer32):
    """Custom type pduCfgCritOverVolAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500),
    )


_PduCfgCritOverVolAlm_Type.__name__ = "Integer32"
_PduCfgCritOverVolAlm_Object = MibScalar
pduCfgCritOverVolAlm = _PduCfgCritOverVolAlm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 10),
    _PduCfgCritOverVolAlm_Type()
)
pduCfgCritOverVolAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgCritOverVolAlm.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgCritOverVolAlm.setUnits("0.1V")


class _PduCfgWarnOverLoadAlm_Type(Integer32):
    """Custom type pduCfgWarnOverLoadAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 140800),
    )


_PduCfgWarnOverLoadAlm_Type.__name__ = "Integer32"
_PduCfgWarnOverLoadAlm_Object = MibScalar
pduCfgWarnOverLoadAlm = _PduCfgWarnOverLoadAlm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 11),
    _PduCfgWarnOverLoadAlm_Type()
)
pduCfgWarnOverLoadAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgWarnOverLoadAlm.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgWarnOverLoadAlm.setUnits("0.1W")


class _PduCfgWarnLoadBalanceAlm_Type(Integer32):
    """Custom type pduCfgWarnLoadBalanceAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PduCfgWarnLoadBalanceAlm_Type.__name__ = "Integer32"
_PduCfgWarnLoadBalanceAlm_Object = MibScalar
pduCfgWarnLoadBalanceAlm = _PduCfgWarnLoadBalanceAlm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 12),
    _PduCfgWarnLoadBalanceAlm_Type()
)
pduCfgWarnLoadBalanceAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgWarnLoadBalanceAlm.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgWarnLoadBalanceAlm.setUnits("0.1%")


class _PduCfgWarnOverCurrAlmCB1Ph1_Type(Integer32):
    """Custom type pduCfgWarnOverCurrAlmCB1Ph1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgWarnOverCurrAlmCB1Ph1_Type.__name__ = "Integer32"
_PduCfgWarnOverCurrAlmCB1Ph1_Object = MibScalar
pduCfgWarnOverCurrAlmCB1Ph1 = _PduCfgWarnOverCurrAlmCB1Ph1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 13),
    _PduCfgWarnOverCurrAlmCB1Ph1_Type()
)
pduCfgWarnOverCurrAlmCB1Ph1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB1Ph1.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB1Ph1.setUnits("0.01A")


class _PduCfgWarnOverCurrAlmCB1Ph2_Type(Integer32):
    """Custom type pduCfgWarnOverCurrAlmCB1Ph2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgWarnOverCurrAlmCB1Ph2_Type.__name__ = "Integer32"
_PduCfgWarnOverCurrAlmCB1Ph2_Object = MibScalar
pduCfgWarnOverCurrAlmCB1Ph2 = _PduCfgWarnOverCurrAlmCB1Ph2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 14),
    _PduCfgWarnOverCurrAlmCB1Ph2_Type()
)
pduCfgWarnOverCurrAlmCB1Ph2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB1Ph2.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB1Ph2.setUnits("0.01A")


class _PduCfgWarnOverCurrAlmCB1Ph3_Type(Integer32):
    """Custom type pduCfgWarnOverCurrAlmCB1Ph3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgWarnOverCurrAlmCB1Ph3_Type.__name__ = "Integer32"
_PduCfgWarnOverCurrAlmCB1Ph3_Object = MibScalar
pduCfgWarnOverCurrAlmCB1Ph3 = _PduCfgWarnOverCurrAlmCB1Ph3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 15),
    _PduCfgWarnOverCurrAlmCB1Ph3_Type()
)
pduCfgWarnOverCurrAlmCB1Ph3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB1Ph3.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB1Ph3.setUnits("0.01A")


class _PduCfgWarnOverCurrAlmCB2Ph1_Type(Integer32):
    """Custom type pduCfgWarnOverCurrAlmCB2Ph1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgWarnOverCurrAlmCB2Ph1_Type.__name__ = "Integer32"
_PduCfgWarnOverCurrAlmCB2Ph1_Object = MibScalar
pduCfgWarnOverCurrAlmCB2Ph1 = _PduCfgWarnOverCurrAlmCB2Ph1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 16),
    _PduCfgWarnOverCurrAlmCB2Ph1_Type()
)
pduCfgWarnOverCurrAlmCB2Ph1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB2Ph1.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB2Ph1.setUnits("0.01A")


class _PduCfgWarnOverCurrAlmCB2Ph2_Type(Integer32):
    """Custom type pduCfgWarnOverCurrAlmCB2Ph2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgWarnOverCurrAlmCB2Ph2_Type.__name__ = "Integer32"
_PduCfgWarnOverCurrAlmCB2Ph2_Object = MibScalar
pduCfgWarnOverCurrAlmCB2Ph2 = _PduCfgWarnOverCurrAlmCB2Ph2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 17),
    _PduCfgWarnOverCurrAlmCB2Ph2_Type()
)
pduCfgWarnOverCurrAlmCB2Ph2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB2Ph2.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB2Ph2.setUnits("0.01A")


class _PduCfgWarnOverCurrAlmCB2Ph3_Type(Integer32):
    """Custom type pduCfgWarnOverCurrAlmCB2Ph3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgWarnOverCurrAlmCB2Ph3_Type.__name__ = "Integer32"
_PduCfgWarnOverCurrAlmCB2Ph3_Object = MibScalar
pduCfgWarnOverCurrAlmCB2Ph3 = _PduCfgWarnOverCurrAlmCB2Ph3_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 18),
    _PduCfgWarnOverCurrAlmCB2Ph3_Type()
)
pduCfgWarnOverCurrAlmCB2Ph3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB2Ph3.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgWarnOverCurrAlmCB2Ph3.setUnits("0.01A")


class _PduCfgWarnOverTotalCurrAlm_Type(Integer32):
    """Custom type pduCfgWarnOverTotalCurrAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3200),
    )


_PduCfgWarnOverTotalCurrAlm_Type.__name__ = "Integer32"
_PduCfgWarnOverTotalCurrAlm_Object = MibScalar
pduCfgWarnOverTotalCurrAlm = _PduCfgWarnOverTotalCurrAlm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 19),
    _PduCfgWarnOverTotalCurrAlm_Type()
)
pduCfgWarnOverTotalCurrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgWarnOverTotalCurrAlm.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgWarnOverTotalCurrAlm.setUnits("0.01A")


class _PduCfgWarnOverVolAlm_Type(Integer32):
    """Custom type pduCfgWarnOverVolAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3500),
    )


_PduCfgWarnOverVolAlm_Type.__name__ = "Integer32"
_PduCfgWarnOverVolAlm_Object = MibScalar
pduCfgWarnOverVolAlm = _PduCfgWarnOverVolAlm_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 2, 20),
    _PduCfgWarnOverVolAlm_Type()
)
pduCfgWarnOverVolAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCfgWarnOverVolAlm.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduCfgWarnOverVolAlm.setUnits("0.1V")
_PduStat_ObjectIdentity = ObjectIdentity
pduStat = _PduStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3)
)
_PduStatPower_Type = Integer32
_PduStatPower_Object = MibScalar
pduStatPower = _PduStatPower_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 1),
    _PduStatPower_Type()
)
pduStatPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduStatPower.setUnits("0.1W")


class _PduStatPowerStat_Type(Integer32):
    """Custom type pduStatPowerStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduStatPowerStat_Type.__name__ = "Integer32"
_PduStatPowerStat_Object = MibScalar
pduStatPowerStat = _PduStatPowerStat_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 2),
    _PduStatPowerStat_Type()
)
pduStatPowerStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatPowerStat.setStatus("mandatory")
_PduStatTotalEnergy_Type = Integer32
_PduStatTotalEnergy_Object = MibScalar
pduStatTotalEnergy = _PduStatTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 3),
    _PduStatTotalEnergy_Type()
)
pduStatTotalEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatTotalEnergy.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduStatTotalEnergy.setUnits("0.01kWh")
_PduStatTotalEnergyRecord_Type = DisplayString
_PduStatTotalEnergyRecord_Object = MibScalar
pduStatTotalEnergyRecord = _PduStatTotalEnergyRecord_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 4),
    _PduStatTotalEnergyRecord_Type()
)
pduStatTotalEnergyRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatTotalEnergyRecord.setStatus("mandatory")
_PduStatPh1Energy_Type = Integer32
_PduStatPh1Energy_Object = MibScalar
pduStatPh1Energy = _PduStatPh1Energy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 5),
    _PduStatPh1Energy_Type()
)
pduStatPh1Energy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatPh1Energy.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduStatPh1Energy.setUnits("0.01kWh")
_PduStatPh1EnergyRecord_Type = DisplayString
_PduStatPh1EnergyRecord_Object = MibScalar
pduStatPh1EnergyRecord = _PduStatPh1EnergyRecord_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 6),
    _PduStatPh1EnergyRecord_Type()
)
pduStatPh1EnergyRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatPh1EnergyRecord.setStatus("mandatory")
_PduStatPh2Energy_Type = Integer32
_PduStatPh2Energy_Object = MibScalar
pduStatPh2Energy = _PduStatPh2Energy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 7),
    _PduStatPh2Energy_Type()
)
pduStatPh2Energy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatPh2Energy.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduStatPh2Energy.setUnits("0.01kWh")
_PduStatPh2EnergyRecord_Type = DisplayString
_PduStatPh2EnergyRecord_Object = MibScalar
pduStatPh2EnergyRecord = _PduStatPh2EnergyRecord_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 8),
    _PduStatPh2EnergyRecord_Type()
)
pduStatPh2EnergyRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatPh2EnergyRecord.setStatus("mandatory")
_PduStatPh3Energy_Type = Integer32
_PduStatPh3Energy_Object = MibScalar
pduStatPh3Energy = _PduStatPh3Energy_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 9),
    _PduStatPh3Energy_Type()
)
pduStatPh3Energy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatPh3Energy.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduStatPh3Energy.setUnits("0.01kWh")
_PduStatPh3EnergyRecord_Type = DisplayString
_PduStatPh3EnergyRecord_Object = MibScalar
pduStatPh3EnergyRecord = _PduStatPh3EnergyRecord_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 10),
    _PduStatPh3EnergyRecord_Type()
)
pduStatPh3EnergyRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatPh3EnergyRecord.setStatus("mandatory")
_PduStatLoadBalance_Type = Integer32
_PduStatLoadBalance_Object = MibScalar
pduStatLoadBalance = _PduStatLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 11),
    _PduStatLoadBalance_Type()
)
pduStatLoadBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatLoadBalance.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduStatLoadBalance.setUnits("%")
_PduStatLoadBalanceStat_Type = Integer32
_PduStatLoadBalanceStat_Object = MibScalar
pduStatLoadBalanceStat = _PduStatLoadBalanceStat_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 12),
    _PduStatLoadBalanceStat_Type()
)
pduStatLoadBalanceStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatLoadBalanceStat.setStatus("mandatory")


class _PduStatTotalEnergyCln_Type(Integer32):
    """Custom type pduStatTotalEnergyCln based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("reset", 2))
    )


_PduStatTotalEnergyCln_Type.__name__ = "Integer32"
_PduStatTotalEnergyCln_Object = MibScalar
pduStatTotalEnergyCln = _PduStatTotalEnergyCln_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 13),
    _PduStatTotalEnergyCln_Type()
)
pduStatTotalEnergyCln.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduStatTotalEnergyCln.setStatus("mandatory")


class _PduStatPh1EnergyCln_Type(Integer32):
    """Custom type pduStatPh1EnergyCln based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("reset", 2))
    )


_PduStatPh1EnergyCln_Type.__name__ = "Integer32"
_PduStatPh1EnergyCln_Object = MibScalar
pduStatPh1EnergyCln = _PduStatPh1EnergyCln_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 14),
    _PduStatPh1EnergyCln_Type()
)
pduStatPh1EnergyCln.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduStatPh1EnergyCln.setStatus("mandatory")


class _PduStatPh2EnergyCln_Type(Integer32):
    """Custom type pduStatPh2EnergyCln based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("reset", 2))
    )


_PduStatPh2EnergyCln_Type.__name__ = "Integer32"
_PduStatPh2EnergyCln_Object = MibScalar
pduStatPh2EnergyCln = _PduStatPh2EnergyCln_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 15),
    _PduStatPh2EnergyCln_Type()
)
pduStatPh2EnergyCln.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduStatPh2EnergyCln.setStatus("mandatory")


class _PduStatPh3EnergyCln_Type(Integer32):
    """Custom type pduStatPh3EnergyCln based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("reset", 2))
    )


_PduStatPh3EnergyCln_Type.__name__ = "Integer32"
_PduStatPh3EnergyCln_Object = MibScalar
pduStatPh3EnergyCln = _PduStatPh3EnergyCln_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 1, 3, 16),
    _PduStatPh3EnergyCln_Type()
)
pduStatPh3EnergyCln.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduStatPh3EnergyCln.setStatus("mandatory")
_PduEnvMon_ObjectIdentity = ObjectIdentity
pduEnvMon = _PduEnvMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2)
)
_PduEmdCurrInfo_ObjectIdentity = ObjectIdentity
pduEmdCurrInfo = _PduEmdCurrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1)
)
_PduEmdCurrInfoTable_Object = MibTable
pduEmdCurrInfoTable = _PduEmdCurrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pduEmdCurrInfoTable.setStatus("mandatory")
_PduEmdCurrInfoEntry_Object = MibTableRow
pduEmdCurrInfoEntry = _PduEmdCurrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1)
)
pduEmdCurrInfoEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduEmdCurrInfoEmdStatIndex"),
)
if mibBuilder.loadTexts:
    pduEmdCurrInfoEntry.setStatus("mandatory")


class _PduEmdCurrInfoEmdStatIndex_Type(Integer32):
    """Custom type pduEmdCurrInfoEmdStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PduEmdCurrInfoEmdStatIndex_Type.__name__ = "Integer32"
_PduEmdCurrInfoEmdStatIndex_Object = MibTableColumn
pduEmdCurrInfoEmdStatIndex = _PduEmdCurrInfoEmdStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 1),
    _PduEmdCurrInfoEmdStatIndex_Type()
)
pduEmdCurrInfoEmdStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoEmdStatIndex.setStatus("mandatory")
_PduEmdCurrInfoHumidityName_Type = DisplayString
_PduEmdCurrInfoHumidityName_Object = MibTableColumn
pduEmdCurrInfoHumidityName = _PduEmdCurrInfoHumidityName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 2),
    _PduEmdCurrInfoHumidityName_Type()
)
pduEmdCurrInfoHumidityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoHumidityName.setStatus("mandatory")


class _PduEmdCurrInfoHumidityStat_Type(Integer32):
    """Custom type pduEmdCurrInfoHumidityStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduEmdCurrInfoHumidityStat_Type.__name__ = "Integer32"
_PduEmdCurrInfoHumidityStat_Object = MibTableColumn
pduEmdCurrInfoHumidityStat = _PduEmdCurrInfoHumidityStat_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 3),
    _PduEmdCurrInfoHumidityStat_Type()
)
pduEmdCurrInfoHumidityStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoHumidityStat.setStatus("mandatory")
_PduEmdCurrInfoHumidityValue_Type = Integer32
_PduEmdCurrInfoHumidityValue_Object = MibTableColumn
pduEmdCurrInfoHumidityValue = _PduEmdCurrInfoHumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 4),
    _PduEmdCurrInfoHumidityValue_Type()
)
pduEmdCurrInfoHumidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoHumidityValue.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEmdCurrInfoHumidityValue.setUnits("0.1%")
_PduEmdCurrInfoTempName_Type = DisplayString
_PduEmdCurrInfoTempName_Object = MibTableColumn
pduEmdCurrInfoTempName = _PduEmdCurrInfoTempName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 5),
    _PduEmdCurrInfoTempName_Type()
)
pduEmdCurrInfoTempName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoTempName.setStatus("mandatory")


class _PduEmdCurrInfoTempStat_Type(Integer32):
    """Custom type pduEmdCurrInfoTempStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduEmdCurrInfoTempStat_Type.__name__ = "Integer32"
_PduEmdCurrInfoTempStat_Object = MibTableColumn
pduEmdCurrInfoTempStat = _PduEmdCurrInfoTempStat_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 6),
    _PduEmdCurrInfoTempStat_Type()
)
pduEmdCurrInfoTempStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoTempStat.setStatus("mandatory")
_PduEmdCurrInfoTempValue_Type = Integer32
_PduEmdCurrInfoTempValue_Object = MibTableColumn
pduEmdCurrInfoTempValue = _PduEmdCurrInfoTempValue_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 7),
    _PduEmdCurrInfoTempValue_Type()
)
pduEmdCurrInfoTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoTempValue.setStatus("mandatory")
_PduEmdCurrInfoAlm1Name_Type = DisplayString
_PduEmdCurrInfoAlm1Name_Object = MibTableColumn
pduEmdCurrInfoAlm1Name = _PduEmdCurrInfoAlm1Name_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 8),
    _PduEmdCurrInfoAlm1Name_Type()
)
pduEmdCurrInfoAlm1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoAlm1Name.setStatus("mandatory")


class _PduEmdCurrInfoAlm1Stat_Type(Integer32):
    """Custom type pduEmdCurrInfoAlm1Stat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alert", 2))
    )


_PduEmdCurrInfoAlm1Stat_Type.__name__ = "Integer32"
_PduEmdCurrInfoAlm1Stat_Object = MibTableColumn
pduEmdCurrInfoAlm1Stat = _PduEmdCurrInfoAlm1Stat_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 9),
    _PduEmdCurrInfoAlm1Stat_Type()
)
pduEmdCurrInfoAlm1Stat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoAlm1Stat.setStatus("mandatory")
_PduEmdCurrInfoAlm2Name_Type = DisplayString
_PduEmdCurrInfoAlm2Name_Object = MibTableColumn
pduEmdCurrInfoAlm2Name = _PduEmdCurrInfoAlm2Name_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 10),
    _PduEmdCurrInfoAlm2Name_Type()
)
pduEmdCurrInfoAlm2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoAlm2Name.setStatus("mandatory")


class _PduEmdCurrInfoAlm2Stat_Type(Integer32):
    """Custom type pduEmdCurrInfoAlm2Stat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alert", 2))
    )


_PduEmdCurrInfoAlm2Stat_Type.__name__ = "Integer32"
_PduEmdCurrInfoAlm2Stat_Object = MibTableColumn
pduEmdCurrInfoAlm2Stat = _PduEmdCurrInfoAlm2Stat_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 11),
    _PduEmdCurrInfoAlm2Stat_Type()
)
pduEmdCurrInfoAlm2Stat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoAlm2Stat.setStatus("mandatory")
_PduEmdCurrInfoLocName_Type = DisplayString
_PduEmdCurrInfoLocName_Object = MibTableColumn
pduEmdCurrInfoLocName = _PduEmdCurrInfoLocName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 12),
    _PduEmdCurrInfoLocName_Type()
)
pduEmdCurrInfoLocName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoLocName.setStatus("mandatory")
_PduEmdCurrInfoAddress_Type = Integer32
_PduEmdCurrInfoAddress_Object = MibTableColumn
pduEmdCurrInfoAddress = _PduEmdCurrInfoAddress_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 1, 1, 1, 13),
    _PduEmdCurrInfoAddress_Type()
)
pduEmdCurrInfoAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCurrInfoAddress.setStatus("mandatory")
_PduEmdCfg_ObjectIdentity = ObjectIdentity
pduEmdCfg = _PduEmdCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2)
)
_PduEmdCfgTable_Object = MibTable
pduEmdCfgTable = _PduEmdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pduEmdCfgTable.setStatus("mandatory")
_PduEmdCfgEntry_Object = MibTableRow
pduEmdCfgEntry = _PduEmdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1)
)
pduEmdCfgEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduEmdCfgEMDIndex"),
)
if mibBuilder.loadTexts:
    pduEmdCfgEntry.setStatus("mandatory")


class _PduEmdCfgEMDIndex_Type(Integer32):
    """Custom type pduEmdCfgEMDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PduEmdCfgEMDIndex_Type.__name__ = "Integer32"
_PduEmdCfgEMDIndex_Object = MibTableColumn
pduEmdCfgEMDIndex = _PduEmdCfgEMDIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 1),
    _PduEmdCfgEMDIndex_Type()
)
pduEmdCfgEMDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCfgEMDIndex.setStatus("mandatory")


class _PduEmdCfgEMDName_Type(DisplayString):
    """Custom type pduEmdCfgEMDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmdCfgEMDName_Type.__name__ = "DisplayString"
_PduEmdCfgEMDName_Object = MibTableColumn
pduEmdCfgEMDName = _PduEmdCfgEMDName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 2),
    _PduEmdCfgEMDName_Type()
)
pduEmdCfgEMDName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgEMDName.setStatus("mandatory")


class _PduEmdCfgEMDAddress_Type(Integer32):
    """Custom type pduEmdCfgEMDAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 247),
    )


_PduEmdCfgEMDAddress_Type.__name__ = "Integer32"
_PduEmdCfgEMDAddress_Object = MibTableColumn
pduEmdCfgEMDAddress = _PduEmdCfgEMDAddress_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 3),
    _PduEmdCfgEMDAddress_Type()
)
pduEmdCfgEMDAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCfgEMDAddress.setStatus("mandatory")


class _PduEmdCfgAppFWVer_Type(DisplayString):
    """Custom type pduEmdCfgAppFWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmdCfgAppFWVer_Type.__name__ = "DisplayString"
_PduEmdCfgAppFWVer_Object = MibTableColumn
pduEmdCfgAppFWVer = _PduEmdCfgAppFWVer_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 4),
    _PduEmdCfgAppFWVer_Type()
)
pduEmdCfgAppFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmdCfgAppFWVer.setStatus("mandatory")


class _PduEmdCfgLocName_Type(DisplayString):
    """Custom type pduEmdCfgLocName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmdCfgLocName_Type.__name__ = "DisplayString"
_PduEmdCfgLocName_Object = MibTableColumn
pduEmdCfgLocName = _PduEmdCfgLocName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 5),
    _PduEmdCfgLocName_Type()
)
pduEmdCfgLocName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgLocName.setStatus("mandatory")


class _PduEmdCfgAlm1Name_Type(DisplayString):
    """Custom type pduEmdCfgAlm1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmdCfgAlm1Name_Type.__name__ = "DisplayString"
_PduEmdCfgAlm1Name_Object = MibTableColumn
pduEmdCfgAlm1Name = _PduEmdCfgAlm1Name_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 6),
    _PduEmdCfgAlm1Name_Type()
)
pduEmdCfgAlm1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgAlm1Name.setStatus("mandatory")


class _PduEmdCfgAlm2Name_Type(DisplayString):
    """Custom type pduEmdCfgAlm2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmdCfgAlm2Name_Type.__name__ = "DisplayString"
_PduEmdCfgAlm2Name_Object = MibTableColumn
pduEmdCfgAlm2Name = _PduEmdCfgAlm2Name_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 7),
    _PduEmdCfgAlm2Name_Type()
)
pduEmdCfgAlm2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgAlm2Name.setStatus("mandatory")


class _PduEmdCfgAlm1Type_Type(Integer32):
    """Custom type pduEmdCfgAlm1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("normalOpen", 2),
          ("normalClose", 3))
    )


_PduEmdCfgAlm1Type_Type.__name__ = "Integer32"
_PduEmdCfgAlm1Type_Object = MibTableColumn
pduEmdCfgAlm1Type = _PduEmdCfgAlm1Type_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 8),
    _PduEmdCfgAlm1Type_Type()
)
pduEmdCfgAlm1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgAlm1Type.setStatus("mandatory")


class _PduEmdCfgAlm2Type_Type(Integer32):
    """Custom type pduEmdCfgAlm2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("normalOpen", 2),
          ("normalClose", 3))
    )


_PduEmdCfgAlm2Type_Type.__name__ = "Integer32"
_PduEmdCfgAlm2Type_Object = MibTableColumn
pduEmdCfgAlm2Type = _PduEmdCfgAlm2Type_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 9),
    _PduEmdCfgAlm2Type_Type()
)
pduEmdCfgAlm2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgAlm2Type.setStatus("mandatory")


class _PduEmdCfgTempSenName_Type(DisplayString):
    """Custom type pduEmdCfgTempSenName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmdCfgTempSenName_Type.__name__ = "DisplayString"
_PduEmdCfgTempSenName_Object = MibTableColumn
pduEmdCfgTempSenName = _PduEmdCfgTempSenName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 10),
    _PduEmdCfgTempSenName_Type()
)
pduEmdCfgTempSenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgTempSenName.setStatus("mandatory")


class _PduEmdCfgTempCritHigh_Type(Integer32):
    """Custom type pduEmdCfgTempCritHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 650),
    )


_PduEmdCfgTempCritHigh_Type.__name__ = "Integer32"
_PduEmdCfgTempCritHigh_Object = MibTableColumn
pduEmdCfgTempCritHigh = _PduEmdCfgTempCritHigh_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 11),
    _PduEmdCfgTempCritHigh_Type()
)
pduEmdCfgTempCritHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgTempCritHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEmdCfgTempCritHigh.setUnits("0.1")


class _PduEmdCfgTempCritHighType_Type(Integer32):
    """Custom type pduEmdCfgTempCritHighType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmdCfgTempCritHighType_Type.__name__ = "Integer32"
_PduEmdCfgTempCritHighType_Object = MibTableColumn
pduEmdCfgTempCritHighType = _PduEmdCfgTempCritHighType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 12),
    _PduEmdCfgTempCritHighType_Type()
)
pduEmdCfgTempCritHighType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgTempCritHighType.setStatus("mandatory")


class _PduEmdCfgTempCritLow_Type(Integer32):
    """Custom type pduEmdCfgTempCritLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 650),
    )


_PduEmdCfgTempCritLow_Type.__name__ = "Integer32"
_PduEmdCfgTempCritLow_Object = MibTableColumn
pduEmdCfgTempCritLow = _PduEmdCfgTempCritLow_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 13),
    _PduEmdCfgTempCritLow_Type()
)
pduEmdCfgTempCritLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgTempCritLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEmdCfgTempCritLow.setUnits("0.1")


class _PduEmdCfgTempCritLowType_Type(Integer32):
    """Custom type pduEmdCfgTempCritLowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmdCfgTempCritLowType_Type.__name__ = "Integer32"
_PduEmdCfgTempCritLowType_Object = MibTableColumn
pduEmdCfgTempCritLowType = _PduEmdCfgTempCritLowType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 14),
    _PduEmdCfgTempCritLowType_Type()
)
pduEmdCfgTempCritLowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgTempCritLowType.setStatus("mandatory")


class _PduEmdCfgTempWarnHigh_Type(Integer32):
    """Custom type pduEmdCfgTempWarnHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 650),
    )


_PduEmdCfgTempWarnHigh_Type.__name__ = "Integer32"
_PduEmdCfgTempWarnHigh_Object = MibTableColumn
pduEmdCfgTempWarnHigh = _PduEmdCfgTempWarnHigh_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 15),
    _PduEmdCfgTempWarnHigh_Type()
)
pduEmdCfgTempWarnHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgTempWarnHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEmdCfgTempWarnHigh.setUnits("0.1")


class _PduEmdCfgTempWarnHighType_Type(Integer32):
    """Custom type pduEmdCfgTempWarnHighType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmdCfgTempWarnHighType_Type.__name__ = "Integer32"
_PduEmdCfgTempWarnHighType_Object = MibTableColumn
pduEmdCfgTempWarnHighType = _PduEmdCfgTempWarnHighType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 16),
    _PduEmdCfgTempWarnHighType_Type()
)
pduEmdCfgTempWarnHighType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgTempWarnHighType.setStatus("mandatory")


class _PduEmdCfgTempWarnLow_Type(Integer32):
    """Custom type pduEmdCfgTempWarnLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 650),
    )


_PduEmdCfgTempWarnLow_Type.__name__ = "Integer32"
_PduEmdCfgTempWarnLow_Object = MibTableColumn
pduEmdCfgTempWarnLow = _PduEmdCfgTempWarnLow_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 17),
    _PduEmdCfgTempWarnLow_Type()
)
pduEmdCfgTempWarnLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgTempWarnLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduEmdCfgTempWarnLow.setUnits("0.1")


class _PduEmdCfgTempWarnLowType_Type(Integer32):
    """Custom type pduEmdCfgTempWarnLowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmdCfgTempWarnLowType_Type.__name__ = "Integer32"
_PduEmdCfgTempWarnLowType_Object = MibTableColumn
pduEmdCfgTempWarnLowType = _PduEmdCfgTempWarnLowType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 18),
    _PduEmdCfgTempWarnLowType_Type()
)
pduEmdCfgTempWarnLowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgTempWarnLowType.setStatus("mandatory")


class _PduEmdCfgTempCalOffset_Type(Integer32):
    """Custom type pduEmdCfgTempCalOffset based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("fivePointFour", 1),
          ("fourPointFive", 2),
          ("threePointSix", 3),
          ("twoPointSeven", 4),
          ("onePointEight", 5),
          ("zeroPointNine", 6),
          ("zeroPointZero", 7),
          ("negativeZeroPointNine", 8),
          ("negativeOnePointEight", 9),
          ("negativeTwoPointSeven", 10),
          ("negativeThreePointSix", 11),
          ("negativeFourPointFive", 12),
          ("negativeFivePointFour", 13))
    )


_PduEmdCfgTempCalOffset_Type.__name__ = "Integer32"
_PduEmdCfgTempCalOffset_Object = MibTableColumn
pduEmdCfgTempCalOffset = _PduEmdCfgTempCalOffset_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 19),
    _PduEmdCfgTempCalOffset_Type()
)
pduEmdCfgTempCalOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgTempCalOffset.setStatus("mandatory")


class _PduEmdCfgHumiditySenName_Type(DisplayString):
    """Custom type pduEmdCfgHumiditySenName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmdCfgHumiditySenName_Type.__name__ = "DisplayString"
_PduEmdCfgHumiditySenName_Object = MibTableColumn
pduEmdCfgHumiditySenName = _PduEmdCfgHumiditySenName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 20),
    _PduEmdCfgHumiditySenName_Type()
)
pduEmdCfgHumiditySenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgHumiditySenName.setStatus("mandatory")


class _PduEmdCfgHumidityCritHigh_Type(Integer32):
    """Custom type pduEmdCfgHumidityCritHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PduEmdCfgHumidityCritHigh_Type.__name__ = "Integer32"
_PduEmdCfgHumidityCritHigh_Object = MibTableColumn
pduEmdCfgHumidityCritHigh = _PduEmdCfgHumidityCritHigh_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 21),
    _PduEmdCfgHumidityCritHigh_Type()
)
pduEmdCfgHumidityCritHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgHumidityCritHigh.setStatus("mandatory")


class _PduEmdCfgHumidityCritHighType_Type(Integer32):
    """Custom type pduEmdCfgHumidityCritHighType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmdCfgHumidityCritHighType_Type.__name__ = "Integer32"
_PduEmdCfgHumidityCritHighType_Object = MibTableColumn
pduEmdCfgHumidityCritHighType = _PduEmdCfgHumidityCritHighType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 22),
    _PduEmdCfgHumidityCritHighType_Type()
)
pduEmdCfgHumidityCritHighType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgHumidityCritHighType.setStatus("mandatory")


class _PduEmdCfgHumidityCritLow_Type(Integer32):
    """Custom type pduEmdCfgHumidityCritLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PduEmdCfgHumidityCritLow_Type.__name__ = "Integer32"
_PduEmdCfgHumidityCritLow_Object = MibTableColumn
pduEmdCfgHumidityCritLow = _PduEmdCfgHumidityCritLow_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 23),
    _PduEmdCfgHumidityCritLow_Type()
)
pduEmdCfgHumidityCritLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgHumidityCritLow.setStatus("mandatory")


class _PduEmdCfgHumidityCritLowType_Type(Integer32):
    """Custom type pduEmdCfgHumidityCritLowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmdCfgHumidityCritLowType_Type.__name__ = "Integer32"
_PduEmdCfgHumidityCritLowType_Object = MibTableColumn
pduEmdCfgHumidityCritLowType = _PduEmdCfgHumidityCritLowType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 24),
    _PduEmdCfgHumidityCritLowType_Type()
)
pduEmdCfgHumidityCritLowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgHumidityCritLowType.setStatus("mandatory")


class _PduEmdCfgHumidityWarnHigh_Type(Integer32):
    """Custom type pduEmdCfgHumidityWarnHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PduEmdCfgHumidityWarnHigh_Type.__name__ = "Integer32"
_PduEmdCfgHumidityWarnHigh_Object = MibTableColumn
pduEmdCfgHumidityWarnHigh = _PduEmdCfgHumidityWarnHigh_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 25),
    _PduEmdCfgHumidityWarnHigh_Type()
)
pduEmdCfgHumidityWarnHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgHumidityWarnHigh.setStatus("mandatory")


class _PduEmdCfgHumidityWarnHighType_Type(Integer32):
    """Custom type pduEmdCfgHumidityWarnHighType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmdCfgHumidityWarnHighType_Type.__name__ = "Integer32"
_PduEmdCfgHumidityWarnHighType_Object = MibTableColumn
pduEmdCfgHumidityWarnHighType = _PduEmdCfgHumidityWarnHighType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 26),
    _PduEmdCfgHumidityWarnHighType_Type()
)
pduEmdCfgHumidityWarnHighType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgHumidityWarnHighType.setStatus("mandatory")


class _PduEmdCfgHumidityWarnLow_Type(Integer32):
    """Custom type pduEmdCfgHumidityWarnLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PduEmdCfgHumidityWarnLow_Type.__name__ = "Integer32"
_PduEmdCfgHumidityWarnLow_Object = MibTableColumn
pduEmdCfgHumidityWarnLow = _PduEmdCfgHumidityWarnLow_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 27),
    _PduEmdCfgHumidityWarnLow_Type()
)
pduEmdCfgHumidityWarnLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgHumidityWarnLow.setStatus("mandatory")


class _PduEmdCfgHumidityWarnLowType_Type(Integer32):
    """Custom type pduEmdCfgHumidityWarnLowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmdCfgHumidityWarnLowType_Type.__name__ = "Integer32"
_PduEmdCfgHumidityWarnLowType_Object = MibTableColumn
pduEmdCfgHumidityWarnLowType = _PduEmdCfgHumidityWarnLowType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 28),
    _PduEmdCfgHumidityWarnLowType_Type()
)
pduEmdCfgHumidityWarnLowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgHumidityWarnLowType.setStatus("mandatory")


class _PduEmdCfgHumidityCalOffset_Type(Integer32):
    """Custom type pduEmdCfgHumidityCalOffset based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("six", 1),
          ("five", 2),
          ("four", 3),
          ("three", 4),
          ("two", 5),
          ("one", 6),
          ("zero", 7),
          ("negativeOne", 8),
          ("negativeTwo", 9),
          ("negativeThree", 10),
          ("negativeFour", 11),
          ("negativeFive", 12),
          ("negativeSix", 13))
    )


_PduEmdCfgHumidityCalOffset_Type.__name__ = "Integer32"
_PduEmdCfgHumidityCalOffset_Object = MibTableColumn
pduEmdCfgHumidityCalOffset = _PduEmdCfgHumidityCalOffset_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 2, 2, 2, 1, 1, 29),
    _PduEmdCfgHumidityCalOffset_Type()
)
pduEmdCfgHumidityCalOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmdCfgHumidityCalOffset.setStatus("mandatory")
_PduSettings_ObjectIdentity = ObjectIdentity
pduSettings = _PduSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3)
)
_PduGeneralSet_ObjectIdentity = ObjectIdentity
pduGeneralSet = _PduGeneralSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1)
)
_PduSysAdm_ObjectIdentity = ObjectIdentity
pduSysAdm = _PduSysAdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 1)
)


class _PduSysAdmSysName_Type(DisplayString):
    """Custom type pduSysAdmSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSysAdmSysName_Type.__name__ = "DisplayString"
_PduSysAdmSysName_Object = MibScalar
pduSysAdmSysName = _PduSysAdmSysName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 1, 1),
    _PduSysAdmSysName_Type()
)
pduSysAdmSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSysAdmSysName.setStatus("mandatory")


class _PduSysAdmSysContact_Type(DisplayString):
    """Custom type pduSysAdmSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSysAdmSysContact_Type.__name__ = "DisplayString"
_PduSysAdmSysContact_Object = MibScalar
pduSysAdmSysContact = _PduSysAdmSysContact_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 1, 2),
    _PduSysAdmSysContact_Type()
)
pduSysAdmSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSysAdmSysContact.setStatus("mandatory")


class _PduSysAdmSysLocation_Type(DisplayString):
    """Custom type pduSysAdmSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSysAdmSysLocation_Type.__name__ = "DisplayString"
_PduSysAdmSysLocation_Object = MibScalar
pduSysAdmSysLocation = _PduSysAdmSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 1, 3),
    _PduSysAdmSysLocation_Type()
)
pduSysAdmSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSysAdmSysLocation.setStatus("mandatory")


class _PduSysAdmLogInterval_Type(Integer32):
    """Custom type pduSysAdmLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28800),
    )


_PduSysAdmLogInterval_Type.__name__ = "Integer32"
_PduSysAdmLogInterval_Object = MibScalar
pduSysAdmLogInterval = _PduSysAdmLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 1, 4),
    _PduSysAdmLogInterval_Type()
)
pduSysAdmLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSysAdmLogInterval.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduSysAdmLogInterval.setUnits("sec")


class _PduSysAdmWebRefresh_Type(Integer32):
    """Custom type pduSysAdmWebRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_PduSysAdmWebRefresh_Type.__name__ = "Integer32"
_PduSysAdmWebRefresh_Object = MibScalar
pduSysAdmWebRefresh = _PduSysAdmWebRefresh_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 1, 5),
    _PduSysAdmWebRefresh_Type()
)
pduSysAdmWebRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSysAdmWebRefresh.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduSysAdmWebRefresh.setUnits("sec")


class _PduSysAdmWebTimeout_Type(Integer32):
    """Custom type pduSysAdmWebTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PduSysAdmWebTimeout_Type.__name__ = "Integer32"
_PduSysAdmWebTimeout_Object = MibScalar
pduSysAdmWebTimeout = _PduSysAdmWebTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 1, 6),
    _PduSysAdmWebTimeout_Type()
)
pduSysAdmWebTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSysAdmWebTimeout.setStatus("mandatory")
if mibBuilder.loadTexts:
    pduSysAdmWebTimeout.setUnits("sec")
_PduDateAndTime_ObjectIdentity = ObjectIdentity
pduDateAndTime = _PduDateAndTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2)
)
_PduDateAndTimeCurrDateAndTime_Type = DisplayString
_PduDateAndTimeCurrDateAndTime_Object = MibScalar
pduDateAndTimeCurrDateAndTime = _PduDateAndTimeCurrDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2, 1),
    _PduDateAndTimeCurrDateAndTime_Type()
)
pduDateAndTimeCurrDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduDateAndTimeCurrDateAndTime.setStatus("mandatory")


class _PduDateAndTimeTimeZone_Type(Integer32):
    """Custom type pduDateAndTimeTimeZone based on Integer32"""
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
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("gMT-1200InternationalDateLineWest", 1),
          ("gMT-1200Eniwetok-Kwajalein", 2),
          ("gMT-1100MidwayIsland-Samoa", 3),
          ("gMT-1000Hawaii", 4),
          ("gMT-0900Alaska", 5),
          ("gMT-0800PacificTime-Tijuana", 6),
          ("gMT-0700Arizona-MountainTime", 7),
          ("gMT-0700Chihuahua-LaPaz-Mazatlan", 8),
          ("gMT-0700MountainTime", 9),
          ("gMT-0600CentralAmerica", 10),
          ("gMT-0600CentralTime", 11),
          ("gMT-0600Guadalajara-MexicoCity-Monterrey", 12),
          ("gMT-0600Saskatchewan", 13),
          ("gMT-0500Bogota-Lima-Quito", 14),
          ("gMT-0500EasternTime", 15),
          ("gMT-0500Indiana", 16),
          ("gMT-0400AtlanticTime", 17),
          ("gMT-0400Caracas-LaPaz", 18),
          ("gMT-0400Santiago", 19),
          ("gMT-0330Newfoundland", 20),
          ("gMT-0300Brasilia", 21),
          ("gMT-0300BuenosAires-Georgetown", 22),
          ("gMT-0300Greenland", 23),
          ("gMT-0200Mid-Atlantic", 24),
          ("gMT-0100Azores", 25),
          ("gMT-0100CapeVerdeIs", 26),
          ("gMT-0000Casablanca-Monrovia", 27),
          ("gMT-0000GreenwichMeanTime-Dublin-Edinburgh-Lisbon-London", 28),
          ("gMT0100Amsterdam-Berlin-Bern-Rome-Stockholm-Vienna", 29),
          ("gMT0100Belgrade-Bratislava-Budapest-Ljubljana-Prague", 30),
          ("gMT0100Brussels-Copenhagen-Madrid-Paris", 31),
          ("gMT0100Sarajevo-Skopje-Warsaw-Zagreb", 32),
          ("gMT0100WestCentralAfrica", 33),
          ("gMT0200Athens-Istanbul-Minsk", 34),
          ("gMT0200Bucharest", 35),
          ("gMT0200Cairo", 36),
          ("gMT0200Harare-Pretoria", 37),
          ("gMT0200Helsinki-Kyiv-Riga-Sofia-Tallinn-Vilnius", 38),
          ("gMT0200Jerusalem", 39),
          ("gMT0300Baghdad", 40),
          ("gMT0300Kuwait-Riyadh", 41),
          ("gMT0300Moscow-StPetersburg-Volgograd", 42),
          ("gMT0300Nairobi", 43),
          ("gMT0330Tehran", 44),
          ("gMT0400AbuDhabi-Muscat", 45),
          ("gMT0400Baku-Tbilisi-Yerevan", 46),
          ("gMT0430Kabul", 47),
          ("gMT0500Ekaterinburg", 48),
          ("gMT0500Islamabad-Karachi-Tashkent", 49),
          ("gMT0530Bombay-Calcutta", 50),
          ("gMT0530Chennai-Kolkata-Mumbai-NewDelhi", 51),
          ("gMT0545Kathmandu", 52),
          ("gMT0600Almaty-Novosibirsk", 53),
          ("gMT0600Astana-Dhaka", 54),
          ("gMT0600SriJayawardenepura", 55),
          ("gMT0630Rangoon", 56),
          ("gMT0700Bangkok-Hanoi-Jakarta", 57),
          ("gMT0700Krasnoyarsk", 58),
          ("gMT0800Beijing-Chongqing-HongKong-Urumqi", 59),
          ("gMT0800Irkutsk-UlaanBataar", 60),
          ("gMT0800KualaLumpur-Singapore", 61),
          ("gMT0800Perth", 62),
          ("gMT0800Taipei", 63),
          ("gMT0900Osaka-Sapporo-Tokyo", 64),
          ("gMT0900Seoul", 65),
          ("gMT0900Yakutsk", 66),
          ("gMT0930Adelaide", 67),
          ("gMT0930Darwin", 68),
          ("gMT1000Brisbane", 69),
          ("gMT1000Canberra-Melbourne-Sydney", 70),
          ("gMT1000Guam-PortMoresby", 71),
          ("gMT1000Hobart", 72),
          ("gMT1000Vladivostok", 73),
          ("gMT1100Magadan-SolomonIs-NewCaledonia", 74),
          ("gMT1200Auckland-Wellington", 75),
          ("gMT1200Fiji-Kamchatka-MarshallIs", 76),
          ("gMT1300NukuAlofa", 77))
    )


_PduDateAndTimeTimeZone_Type.__name__ = "Integer32"
_PduDateAndTimeTimeZone_Object = MibScalar
pduDateAndTimeTimeZone = _PduDateAndTimeTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2, 2),
    _PduDateAndTimeTimeZone_Type()
)
pduDateAndTimeTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduDateAndTimeTimeZone.setStatus("mandatory")


class _PduDateAndTimeDateFormat_Type(Integer32):
    """Custom type pduDateAndTimeDateFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddmmyyy", 1),
          ("mmddyyyy", 2),
          ("yyyymmdd", 3))
    )


_PduDateAndTimeDateFormat_Type.__name__ = "Integer32"
_PduDateAndTimeDateFormat_Object = MibScalar
pduDateAndTimeDateFormat = _PduDateAndTimeDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2, 3),
    _PduDateAndTimeDateFormat_Type()
)
pduDateAndTimeDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduDateAndTimeDateFormat.setStatus("mandatory")


class _PduDateAndTimeSyncMode_Type(Integer32):
    """Custom type pduDateAndTimeSyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("withComputer", 1),
          ("withNTPServer", 2),
          ("setManually", 3))
    )


_PduDateAndTimeSyncMode_Type.__name__ = "Integer32"
_PduDateAndTimeSyncMode_Object = MibScalar
pduDateAndTimeSyncMode = _PduDateAndTimeSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2, 4),
    _PduDateAndTimeSyncMode_Type()
)
pduDateAndTimeSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduDateAndTimeSyncMode.setStatus("mandatory")


class _PduDateAndTimeManualDate_Type(DisplayString):
    """Custom type pduDateAndTimeManualDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_PduDateAndTimeManualDate_Type.__name__ = "DisplayString"
_PduDateAndTimeManualDate_Object = MibScalar
pduDateAndTimeManualDate = _PduDateAndTimeManualDate_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2, 5),
    _PduDateAndTimeManualDate_Type()
)
pduDateAndTimeManualDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduDateAndTimeManualDate.setStatus("mandatory")


class _PduDateAndTimeManualTime_Type(DisplayString):
    """Custom type pduDateAndTimeManualTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PduDateAndTimeManualTime_Type.__name__ = "DisplayString"
_PduDateAndTimeManualTime_Object = MibScalar
pduDateAndTimeManualTime = _PduDateAndTimeManualTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2, 6),
    _PduDateAndTimeManualTime_Type()
)
pduDateAndTimeManualTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduDateAndTimeManualTime.setStatus("mandatory")


class _PduDateAndTimeNtpServer_Type(DisplayString):
    """Custom type pduDateAndTimeNtpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduDateAndTimeNtpServer_Type.__name__ = "DisplayString"
_PduDateAndTimeNtpServer_Object = MibScalar
pduDateAndTimeNtpServer = _PduDateAndTimeNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2, 7),
    _PduDateAndTimeNtpServer_Type()
)
pduDateAndTimeNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduDateAndTimeNtpServer.setStatus("mandatory")


class _PduDateAndTimeNtpSyncIntervalType_Type(Integer32):
    """Custom type pduDateAndTimeNtpSyncIntervalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 1),
          ("month", 2))
    )


_PduDateAndTimeNtpSyncIntervalType_Type.__name__ = "Integer32"
_PduDateAndTimeNtpSyncIntervalType_Object = MibScalar
pduDateAndTimeNtpSyncIntervalType = _PduDateAndTimeNtpSyncIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2, 8),
    _PduDateAndTimeNtpSyncIntervalType_Type()
)
pduDateAndTimeNtpSyncIntervalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduDateAndTimeNtpSyncIntervalType.setStatus("mandatory")


class _PduDateAndTimeNtpSyncInterval_Type(Integer32):
    """Custom type pduDateAndTimeNtpSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PduDateAndTimeNtpSyncInterval_Type.__name__ = "Integer32"
_PduDateAndTimeNtpSyncInterval_Object = MibScalar
pduDateAndTimeNtpSyncInterval = _PduDateAndTimeNtpSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2, 9),
    _PduDateAndTimeNtpSyncInterval_Type()
)
pduDateAndTimeNtpSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduDateAndTimeNtpSyncInterval.setStatus("mandatory")


class _PduDateAndTimeNtpTimeDayLightSaving_Type(Integer32):
    """Custom type pduDateAndTimeNtpTimeDayLightSaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("auto", 2))
    )


_PduDateAndTimeNtpTimeDayLightSaving_Type.__name__ = "Integer32"
_PduDateAndTimeNtpTimeDayLightSaving_Object = MibScalar
pduDateAndTimeNtpTimeDayLightSaving = _PduDateAndTimeNtpTimeDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 1, 2, 10),
    _PduDateAndTimeNtpTimeDayLightSaving_Type()
)
pduDateAndTimeNtpTimeDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduDateAndTimeNtpTimeDayLightSaving.setStatus("mandatory")
_PduIecViewMgmt_ObjectIdentity = ObjectIdentity
pduIecViewMgmt = _PduIecViewMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 2)
)


class _PduIecViewMgmtEn_Type(Integer32):
    """Custom type pduIecViewMgmtEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduIecViewMgmtEn_Type.__name__ = "Integer32"
_PduIecViewMgmtEn_Object = MibScalar
pduIecViewMgmtEn = _PduIecViewMgmtEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 2, 1),
    _PduIecViewMgmtEn_Type()
)
pduIecViewMgmtEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIecViewMgmtEn.setStatus("mandatory")


class _PduIecViewMgmtServer_Type(DisplayString):
    """Custom type pduIecViewMgmtServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduIecViewMgmtServer_Type.__name__ = "DisplayString"
_PduIecViewMgmtServer_Object = MibScalar
pduIecViewMgmtServer = _PduIecViewMgmtServer_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 2, 2),
    _PduIecViewMgmtServer_Type()
)
pduIecViewMgmtServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIecViewMgmtServer.setStatus("mandatory")


class _PduIecViewMgmtGuid_Type(DisplayString):
    """Custom type pduIecViewMgmtGuid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduIecViewMgmtGuid_Type.__name__ = "DisplayString"
_PduIecViewMgmtGuid_Object = MibScalar
pduIecViewMgmtGuid = _PduIecViewMgmtGuid_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 2, 3),
    _PduIecViewMgmtGuid_Type()
)
pduIecViewMgmtGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduIecViewMgmtGuid.setStatus("mandatory")


class _PduIecViewMgmtPort_Type(Integer32):
    """Custom type pduIecViewMgmtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PduIecViewMgmtPort_Type.__name__ = "Integer32"
_PduIecViewMgmtPort_Object = MibScalar
pduIecViewMgmtPort = _PduIecViewMgmtPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 2, 4),
    _PduIecViewMgmtPort_Type()
)
pduIecViewMgmtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIecViewMgmtPort.setStatus("mandatory")


class _PduIecViewMgmtPasswd_Type(DisplayString):
    """Custom type pduIecViewMgmtPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduIecViewMgmtPasswd_Type.__name__ = "DisplayString"
_PduIecViewMgmtPasswd_Object = MibScalar
pduIecViewMgmtPasswd = _PduIecViewMgmtPasswd_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 2, 5),
    _PduIecViewMgmtPasswd_Type()
)
pduIecViewMgmtPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIecViewMgmtPasswd.setStatus("mandatory")
_PduTcpIp_ObjectIdentity = ObjectIdentity
pduTcpIp = _PduTcpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3)
)
_PduIpv4Setting_ObjectIdentity = ObjectIdentity
pduIpv4Setting = _PduIpv4Setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 1)
)


class _PduIpv4SettingDhcpEn_Type(Integer32):
    """Custom type pduIpv4SettingDhcpEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduIpv4SettingDhcpEn_Type.__name__ = "Integer32"
_PduIpv4SettingDhcpEn_Object = MibScalar
pduIpv4SettingDhcpEn = _PduIpv4SettingDhcpEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 1, 1),
    _PduIpv4SettingDhcpEn_Type()
)
pduIpv4SettingDhcpEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv4SettingDhcpEn.setStatus("mandatory")
_PduIpv4SettingAddress_Type = IpAddress
_PduIpv4SettingAddress_Object = MibScalar
pduIpv4SettingAddress = _PduIpv4SettingAddress_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 1, 2),
    _PduIpv4SettingAddress_Type()
)
pduIpv4SettingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv4SettingAddress.setStatus("mandatory")
_PduIpv4SettingMask_Type = IpAddress
_PduIpv4SettingMask_Object = MibScalar
pduIpv4SettingMask = _PduIpv4SettingMask_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 1, 3),
    _PduIpv4SettingMask_Type()
)
pduIpv4SettingMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv4SettingMask.setStatus("mandatory")
_PduIpv4SettingGateway_Type = IpAddress
_PduIpv4SettingGateway_Object = MibScalar
pduIpv4SettingGateway = _PduIpv4SettingGateway_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 1, 4),
    _PduIpv4SettingGateway_Type()
)
pduIpv4SettingGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv4SettingGateway.setStatus("mandatory")
_PduIpv4SettingDns1_Type = IpAddress
_PduIpv4SettingDns1_Object = MibScalar
pduIpv4SettingDns1 = _PduIpv4SettingDns1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 1, 5),
    _PduIpv4SettingDns1_Type()
)
pduIpv4SettingDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv4SettingDns1.setStatus("mandatory")
_PduIpv4SettingDns2_Type = IpAddress
_PduIpv4SettingDns2_Object = MibScalar
pduIpv4SettingDns2 = _PduIpv4SettingDns2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 1, 6),
    _PduIpv4SettingDns2_Type()
)
pduIpv4SettingDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv4SettingDns2.setStatus("mandatory")
_PduIpv6Setting_ObjectIdentity = ObjectIdentity
pduIpv6Setting = _PduIpv6Setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 2)
)


class _PduIpv6SettingEn_Type(Integer32):
    """Custom type pduIpv6SettingEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduIpv6SettingEn_Type.__name__ = "Integer32"
_PduIpv6SettingEn_Object = MibScalar
pduIpv6SettingEn = _PduIpv6SettingEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 2, 1),
    _PduIpv6SettingEn_Type()
)
pduIpv6SettingEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv6SettingEn.setStatus("mandatory")


class _PduIpv6SettingCfg_Type(Integer32):
    """Custom type pduIpv6SettingCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dhcpv6", 2),
          ("manual", 3))
    )


_PduIpv6SettingCfg_Type.__name__ = "Integer32"
_PduIpv6SettingCfg_Object = MibScalar
pduIpv6SettingCfg = _PduIpv6SettingCfg_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 2, 2),
    _PduIpv6SettingCfg_Type()
)
pduIpv6SettingCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv6SettingCfg.setStatus("mandatory")


class _PduIpv6SettingLocalAddress_Type(DisplayString):
    """Custom type pduIpv6SettingLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduIpv6SettingLocalAddress_Type.__name__ = "DisplayString"
_PduIpv6SettingLocalAddress_Object = MibScalar
pduIpv6SettingLocalAddress = _PduIpv6SettingLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 2, 3),
    _PduIpv6SettingLocalAddress_Type()
)
pduIpv6SettingLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduIpv6SettingLocalAddress.setStatus("mandatory")


class _PduIpv6SettingGlobalAddress_Type(DisplayString):
    """Custom type pduIpv6SettingGlobalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduIpv6SettingGlobalAddress_Type.__name__ = "DisplayString"
_PduIpv6SettingGlobalAddress_Object = MibScalar
pduIpv6SettingGlobalAddress = _PduIpv6SettingGlobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 2, 4),
    _PduIpv6SettingGlobalAddress_Type()
)
pduIpv6SettingGlobalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv6SettingGlobalAddress.setStatus("mandatory")


class _PduIpv6SettingRouter_Type(DisplayString):
    """Custom type pduIpv6SettingRouter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduIpv6SettingRouter_Type.__name__ = "DisplayString"
_PduIpv6SettingRouter_Object = MibScalar
pduIpv6SettingRouter = _PduIpv6SettingRouter_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 2, 5),
    _PduIpv6SettingRouter_Type()
)
pduIpv6SettingRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv6SettingRouter.setStatus("mandatory")


class _PduIpv6SettingDns1_Type(DisplayString):
    """Custom type pduIpv6SettingDns1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduIpv6SettingDns1_Type.__name__ = "DisplayString"
_PduIpv6SettingDns1_Object = MibScalar
pduIpv6SettingDns1 = _PduIpv6SettingDns1_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 2, 6),
    _PduIpv6SettingDns1_Type()
)
pduIpv6SettingDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv6SettingDns1.setStatus("mandatory")


class _PduIpv6SettingDns2_Type(DisplayString):
    """Custom type pduIpv6SettingDns2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduIpv6SettingDns2_Type.__name__ = "DisplayString"
_PduIpv6SettingDns2_Object = MibScalar
pduIpv6SettingDns2 = _PduIpv6SettingDns2_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 3, 2, 7),
    _PduIpv6SettingDns2_Type()
)
pduIpv6SettingDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduIpv6SettingDns2.setStatus("mandatory")
_PduAccessIpSetting_ObjectIdentity = ObjectIdentity
pduAccessIpSetting = _PduAccessIpSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 4)
)


class _PduAccessIpSettingEn_Type(Integer32):
    """Custom type pduAccessIpSettingEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduAccessIpSettingEn_Type.__name__ = "Integer32"
_PduAccessIpSettingEn_Object = MibScalar
pduAccessIpSettingEn = _PduAccessIpSettingEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 4, 1),
    _PduAccessIpSettingEn_Type()
)
pduAccessIpSettingEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduAccessIpSettingEn.setStatus("mandatory")
_PduAccessIpSettingTable_Object = MibTable
pduAccessIpSettingTable = _PduAccessIpSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    pduAccessIpSettingTable.setStatus("mandatory")
_PduAccessIpSettingTblEntry_Object = MibTableRow
pduAccessIpSettingTblEntry = _PduAccessIpSettingTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 4, 2, 1)
)
pduAccessIpSettingTblEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduAccessIpSettingTblIndex"),
)
if mibBuilder.loadTexts:
    pduAccessIpSettingTblEntry.setStatus("mandatory")


class _PduAccessIpSettingTblIndex_Type(Integer32):
    """Custom type pduAccessIpSettingTblIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PduAccessIpSettingTblIndex_Type.__name__ = "Integer32"
_PduAccessIpSettingTblIndex_Object = MibTableColumn
pduAccessIpSettingTblIndex = _PduAccessIpSettingTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 4, 2, 1, 1),
    _PduAccessIpSettingTblIndex_Type()
)
pduAccessIpSettingTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduAccessIpSettingTblIndex.setStatus("mandatory")


class _PduAccessIpSettingTblAddr_Type(DisplayString):
    """Custom type pduAccessIpSettingTblAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduAccessIpSettingTblAddr_Type.__name__ = "DisplayString"
_PduAccessIpSettingTblAddr_Object = MibTableColumn
pduAccessIpSettingTblAddr = _PduAccessIpSettingTblAddr_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 4, 2, 1, 2),
    _PduAccessIpSettingTblAddr_Type()
)
pduAccessIpSettingTblAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduAccessIpSettingTblAddr.setStatus("mandatory")


class _PduAccessIpSettingTblPrefix_Type(Integer32):
    """Custom type pduAccessIpSettingTblPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PduAccessIpSettingTblPrefix_Type.__name__ = "Integer32"
_PduAccessIpSettingTblPrefix_Object = MibTableColumn
pduAccessIpSettingTblPrefix = _PduAccessIpSettingTblPrefix_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 4, 2, 1, 3),
    _PduAccessIpSettingTblPrefix_Type()
)
pduAccessIpSettingTblPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduAccessIpSettingTblPrefix.setStatus("mandatory")


class _PduAccessIpSettingTblAction_Type(Integer32):
    """Custom type pduAccessIpSettingTblAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_PduAccessIpSettingTblAction_Type.__name__ = "Integer32"
_PduAccessIpSettingTblAction_Object = MibTableColumn
pduAccessIpSettingTblAction = _PduAccessIpSettingTblAction_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 4, 2, 1, 4),
    _PduAccessIpSettingTblAction_Type()
)
pduAccessIpSettingTblAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduAccessIpSettingTblAction.setStatus("mandatory")
_PduSecurity_ObjectIdentity = ObjectIdentity
pduSecurity = _PduSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5)
)


class _PduSecurityNetAccessProtectEn_Type(Integer32):
    """Custom type pduSecurityNetAccessProtectEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduSecurityNetAccessProtectEn_Type.__name__ = "Integer32"
_PduSecurityNetAccessProtectEn_Object = MibScalar
pduSecurityNetAccessProtectEn = _PduSecurityNetAccessProtectEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 1),
    _PduSecurityNetAccessProtectEn_Type()
)
pduSecurityNetAccessProtectEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecurityNetAccessProtectEn.setStatus("mandatory")


class _PduSecuritySshEn_Type(Integer32):
    """Custom type pduSecuritySshEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduSecuritySshEn_Type.__name__ = "Integer32"
_PduSecuritySshEn_Object = MibScalar
pduSecuritySshEn = _PduSecuritySshEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 2),
    _PduSecuritySshEn_Type()
)
pduSecuritySshEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecuritySshEn.setStatus("mandatory")


class _PduSecuritySshInterval_Type(Integer32):
    """Custom type pduSecuritySshInterval based on Integer32"""
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
        *(("value5", 1),
          ("value10", 2),
          ("value20", 3),
          ("value30", 4),
          ("value100", 5))
    )


_PduSecuritySshInterval_Type.__name__ = "Integer32"
_PduSecuritySshInterval_Object = MibScalar
pduSecuritySshInterval = _PduSecuritySshInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 3),
    _PduSecuritySshInterval_Type()
)
pduSecuritySshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecuritySshInterval.setStatus("mandatory")


class _PduSecuritySshTime_Type(Integer32):
    """Custom type pduSecuritySshTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("value1Min", 1),
          ("value5Min", 2),
          ("value10Min", 3),
          ("value30Min", 4))
    )


_PduSecuritySshTime_Type.__name__ = "Integer32"
_PduSecuritySshTime_Object = MibScalar
pduSecuritySshTime = _PduSecuritySshTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 4),
    _PduSecuritySshTime_Type()
)
pduSecuritySshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecuritySshTime.setStatus("mandatory")


class _PduSecuritySshBlock_Type(Integer32):
    """Custom type pduSecuritySshBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("value1Min", 1),
          ("value30Min", 2),
          ("value1Hour", 3),
          ("value1Day", 4))
    )


_PduSecuritySshBlock_Type.__name__ = "Integer32"
_PduSecuritySshBlock_Object = MibScalar
pduSecuritySshBlock = _PduSecuritySshBlock_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 5),
    _PduSecuritySshBlock_Type()
)
pduSecuritySshBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecuritySshBlock.setStatus("mandatory")


class _PduSecuritySnmpv3En_Type(Integer32):
    """Custom type pduSecuritySnmpv3En based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduSecuritySnmpv3En_Type.__name__ = "Integer32"
_PduSecuritySnmpv3En_Object = MibScalar
pduSecuritySnmpv3En = _PduSecuritySnmpv3En_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 6),
    _PduSecuritySnmpv3En_Type()
)
pduSecuritySnmpv3En.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecuritySnmpv3En.setStatus("mandatory")


class _PduSecuritySnmpv3Interval_Type(Integer32):
    """Custom type pduSecuritySnmpv3Interval based on Integer32"""
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
        *(("value5", 1),
          ("value10", 2),
          ("value20", 3),
          ("value30", 4),
          ("value100", 5))
    )


_PduSecuritySnmpv3Interval_Type.__name__ = "Integer32"
_PduSecuritySnmpv3Interval_Object = MibScalar
pduSecuritySnmpv3Interval = _PduSecuritySnmpv3Interval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 7),
    _PduSecuritySnmpv3Interval_Type()
)
pduSecuritySnmpv3Interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecuritySnmpv3Interval.setStatus("mandatory")


class _PduSecuritySnmpv3Time_Type(Integer32):
    """Custom type pduSecuritySnmpv3Time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("value1Min", 1),
          ("value5Min", 2),
          ("value10Min", 3),
          ("value30Min", 4))
    )


_PduSecuritySnmpv3Time_Type.__name__ = "Integer32"
_PduSecuritySnmpv3Time_Object = MibScalar
pduSecuritySnmpv3Time = _PduSecuritySnmpv3Time_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 8),
    _PduSecuritySnmpv3Time_Type()
)
pduSecuritySnmpv3Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecuritySnmpv3Time.setStatus("mandatory")


class _PduSecuritySnmpv3Block_Type(Integer32):
    """Custom type pduSecuritySnmpv3Block based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("value1Min", 1),
          ("value30Min", 2),
          ("value1Hour", 3),
          ("value1Day", 4))
    )


_PduSecuritySnmpv3Block_Type.__name__ = "Integer32"
_PduSecuritySnmpv3Block_Object = MibScalar
pduSecuritySnmpv3Block = _PduSecuritySnmpv3Block_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 9),
    _PduSecuritySnmpv3Block_Type()
)
pduSecuritySnmpv3Block.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecuritySnmpv3Block.setStatus("mandatory")


class _PduSecurityHttpEn_Type(Integer32):
    """Custom type pduSecurityHttpEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduSecurityHttpEn_Type.__name__ = "Integer32"
_PduSecurityHttpEn_Object = MibScalar
pduSecurityHttpEn = _PduSecurityHttpEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 10),
    _PduSecurityHttpEn_Type()
)
pduSecurityHttpEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecurityHttpEn.setStatus("mandatory")


class _PduSecurityHttpInterval_Type(Integer32):
    """Custom type pduSecurityHttpInterval based on Integer32"""
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
        *(("value5", 1),
          ("value10", 2),
          ("value20", 3),
          ("value30", 4),
          ("value100", 5))
    )


_PduSecurityHttpInterval_Type.__name__ = "Integer32"
_PduSecurityHttpInterval_Object = MibScalar
pduSecurityHttpInterval = _PduSecurityHttpInterval_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 11),
    _PduSecurityHttpInterval_Type()
)
pduSecurityHttpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecurityHttpInterval.setStatus("mandatory")


class _PduSecurityHttpTime_Type(Integer32):
    """Custom type pduSecurityHttpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("value1Min", 1),
          ("value5Min", 2),
          ("value10Min", 3),
          ("value30Min", 4))
    )


_PduSecurityHttpTime_Type.__name__ = "Integer32"
_PduSecurityHttpTime_Object = MibScalar
pduSecurityHttpTime = _PduSecurityHttpTime_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 12),
    _PduSecurityHttpTime_Type()
)
pduSecurityHttpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecurityHttpTime.setStatus("mandatory")


class _PduSecurityHttpBlock_Type(Integer32):
    """Custom type pduSecurityHttpBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("value1Min", 1),
          ("value30Min", 2),
          ("value1Hour", 3),
          ("value1Day", 4))
    )


_PduSecurityHttpBlock_Type.__name__ = "Integer32"
_PduSecurityHttpBlock_Object = MibScalar
pduSecurityHttpBlock = _PduSecurityHttpBlock_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 5, 13),
    _PduSecurityHttpBlock_Type()
)
pduSecurityHttpBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSecurityHttpBlock.setStatus("mandatory")
_PduNetService_ObjectIdentity = ObjectIdentity
pduNetService = _PduNetService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6)
)
_PduNetServiceSsh_ObjectIdentity = ObjectIdentity
pduNetServiceSsh = _PduNetServiceSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 1)
)


class _PduNetServiceSshEn_Type(Integer32):
    """Custom type pduNetServiceSshEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduNetServiceSshEn_Type.__name__ = "Integer32"
_PduNetServiceSshEn_Object = MibScalar
pduNetServiceSshEn = _PduNetServiceSshEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 1, 1),
    _PduNetServiceSshEn_Type()
)
pduNetServiceSshEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceSshEn.setStatus("mandatory")


class _PduNetServiceSshPort_Type(Integer32):
    """Custom type pduNetServiceSshPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PduNetServiceSshPort_Type.__name__ = "Integer32"
_PduNetServiceSshPort_Object = MibScalar
pduNetServiceSshPort = _PduNetServiceSshPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 1, 2),
    _PduNetServiceSshPort_Type()
)
pduNetServiceSshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceSshPort.setStatus("mandatory")
_PduNetServiceSsl_ObjectIdentity = ObjectIdentity
pduNetServiceSsl = _PduNetServiceSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 2)
)


class _PduNetServiceSslEn_Type(Integer32):
    """Custom type pduNetServiceSslEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduNetServiceSslEn_Type.__name__ = "Integer32"
_PduNetServiceSslEn_Object = MibScalar
pduNetServiceSslEn = _PduNetServiceSslEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 2, 1),
    _PduNetServiceSslEn_Type()
)
pduNetServiceSslEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceSslEn.setStatus("mandatory")


class _PduNetServiceSslPort_Type(Integer32):
    """Custom type pduNetServiceSslPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PduNetServiceSslPort_Type.__name__ = "Integer32"
_PduNetServiceSslPort_Object = MibScalar
pduNetServiceSslPort = _PduNetServiceSslPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 2, 2),
    _PduNetServiceSslPort_Type()
)
pduNetServiceSslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceSslPort.setStatus("mandatory")


class _PduNetServiceSslForce_Type(Integer32):
    """Custom type pduNetServiceSslForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduNetServiceSslForce_Type.__name__ = "Integer32"
_PduNetServiceSslForce_Object = MibScalar
pduNetServiceSslForce = _PduNetServiceSslForce_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 2, 3),
    _PduNetServiceSslForce_Type()
)
pduNetServiceSslForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceSslForce.setStatus("mandatory")
_PduNetServicePing_ObjectIdentity = ObjectIdentity
pduNetServicePing = _PduNetServicePing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 3)
)


class _PduNetServicePingEn_Type(Integer32):
    """Custom type pduNetServicePingEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduNetServicePingEn_Type.__name__ = "Integer32"
_PduNetServicePingEn_Object = MibScalar
pduNetServicePingEn = _PduNetServicePingEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 3, 1),
    _PduNetServicePingEn_Type()
)
pduNetServicePingEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServicePingEn.setStatus("mandatory")
_PduNetServiceModbus_ObjectIdentity = ObjectIdentity
pduNetServiceModbus = _PduNetServiceModbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 4)
)


class _PduNetServiceModbusEn_Type(Integer32):
    """Custom type pduNetServiceModbusEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduNetServiceModbusEn_Type.__name__ = "Integer32"
_PduNetServiceModbusEn_Object = MibScalar
pduNetServiceModbusEn = _PduNetServiceModbusEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 4, 1),
    _PduNetServiceModbusEn_Type()
)
pduNetServiceModbusEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceModbusEn.setStatus("mandatory")


class _PduNetServiceModbusPort_Type(Integer32):
    """Custom type pduNetServiceModbusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PduNetServiceModbusPort_Type.__name__ = "Integer32"
_PduNetServiceModbusPort_Object = MibScalar
pduNetServiceModbusPort = _PduNetServiceModbusPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 4, 2),
    _PduNetServiceModbusPort_Type()
)
pduNetServiceModbusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceModbusPort.setStatus("mandatory")
_PduNetServiceRadius_ObjectIdentity = ObjectIdentity
pduNetServiceRadius = _PduNetServiceRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 5)
)


class _PduNetServiceRadiusEn_Type(Integer32):
    """Custom type pduNetServiceRadiusEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduNetServiceRadiusEn_Type.__name__ = "Integer32"
_PduNetServiceRadiusEn_Object = MibScalar
pduNetServiceRadiusEn = _PduNetServiceRadiusEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 5, 1),
    _PduNetServiceRadiusEn_Type()
)
pduNetServiceRadiusEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceRadiusEn.setStatus("mandatory")


class _PduNetServiceRadiusIp_Type(DisplayString):
    """Custom type pduNetServiceRadiusIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetServiceRadiusIp_Type.__name__ = "DisplayString"
_PduNetServiceRadiusIp_Object = MibScalar
pduNetServiceRadiusIp = _PduNetServiceRadiusIp_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 5, 2),
    _PduNetServiceRadiusIp_Type()
)
pduNetServiceRadiusIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceRadiusIp.setStatus("mandatory")


class _PduNetServiceRadiusPort_Type(Integer32):
    """Custom type pduNetServiceRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PduNetServiceRadiusPort_Type.__name__ = "Integer32"
_PduNetServiceRadiusPort_Object = MibScalar
pduNetServiceRadiusPort = _PduNetServiceRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 5, 3),
    _PduNetServiceRadiusPort_Type()
)
pduNetServiceRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceRadiusPort.setStatus("mandatory")


class _PduNetServiceRadiusSecKey_Type(DisplayString):
    """Custom type pduNetServiceRadiusSecKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduNetServiceRadiusSecKey_Type.__name__ = "DisplayString"
_PduNetServiceRadiusSecKey_Object = MibScalar
pduNetServiceRadiusSecKey = _PduNetServiceRadiusSecKey_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 5, 4),
    _PduNetServiceRadiusSecKey_Type()
)
pduNetServiceRadiusSecKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceRadiusSecKey.setStatus("mandatory")


class _PduNetServiceRadiusTimeout_Type(Integer32):
    """Custom type pduNetServiceRadiusTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PduNetServiceRadiusTimeout_Type.__name__ = "Integer32"
_PduNetServiceRadiusTimeout_Object = MibScalar
pduNetServiceRadiusTimeout = _PduNetServiceRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 5, 5),
    _PduNetServiceRadiusTimeout_Type()
)
pduNetServiceRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceRadiusTimeout.setStatus("mandatory")


class _PduNetServiceRadiusRetry_Type(Integer32):
    """Custom type pduNetServiceRadiusRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PduNetServiceRadiusRetry_Type.__name__ = "Integer32"
_PduNetServiceRadiusRetry_Object = MibScalar
pduNetServiceRadiusRetry = _PduNetServiceRadiusRetry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 6, 5, 6),
    _PduNetServiceRadiusRetry_Type()
)
pduNetServiceRadiusRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduNetServiceRadiusRetry.setStatus("mandatory")
_PduSnmpSetting_ObjectIdentity = ObjectIdentity
pduSnmpSetting = _PduSnmpSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7)
)
_PduSnmpSettingAgent_ObjectIdentity = ObjectIdentity
pduSnmpSettingAgent = _PduSnmpSettingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 1)
)


class _PduSnmpSettingAgentEn_Type(Integer32):
    """Custom type pduSnmpSettingAgentEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PduSnmpSettingAgentEn_Type.__name__ = "Integer32"
_PduSnmpSettingAgentEn_Object = MibScalar
pduSnmpSettingAgentEn = _PduSnmpSettingAgentEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 1, 1),
    _PduSnmpSettingAgentEn_Type()
)
pduSnmpSettingAgentEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingAgentEn.setStatus("mandatory")


class _PduSnmpSettingAgentPort_Type(Integer32):
    """Custom type pduSnmpSettingAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PduSnmpSettingAgentPort_Type.__name__ = "Integer32"
_PduSnmpSettingAgentPort_Object = MibScalar
pduSnmpSettingAgentPort = _PduSnmpSettingAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 1, 2),
    _PduSnmpSettingAgentPort_Type()
)
pduSnmpSettingAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingAgentPort.setStatus("mandatory")


class _PduSnmpSettingAgentComRead_Type(DisplayString):
    """Custom type pduSnmpSettingAgentComRead based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSnmpSettingAgentComRead_Type.__name__ = "DisplayString"
_PduSnmpSettingAgentComRead_Object = MibScalar
pduSnmpSettingAgentComRead = _PduSnmpSettingAgentComRead_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 1, 3),
    _PduSnmpSettingAgentComRead_Type()
)
pduSnmpSettingAgentComRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingAgentComRead.setStatus("mandatory")


class _PduSnmpSettingAgentComWrite_Type(DisplayString):
    """Custom type pduSnmpSettingAgentComWrite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSnmpSettingAgentComWrite_Type.__name__ = "DisplayString"
_PduSnmpSettingAgentComWrite_Object = MibScalar
pduSnmpSettingAgentComWrite = _PduSnmpSettingAgentComWrite_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 1, 4),
    _PduSnmpSettingAgentComWrite_Type()
)
pduSnmpSettingAgentComWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingAgentComWrite.setStatus("mandatory")
_PduSnmpSettingv3Usm_ObjectIdentity = ObjectIdentity
pduSnmpSettingv3Usm = _PduSnmpSettingv3Usm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 2)
)


class _PduSnmpSettingv3UsmUserName_Type(DisplayString):
    """Custom type pduSnmpSettingv3UsmUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSnmpSettingv3UsmUserName_Type.__name__ = "DisplayString"
_PduSnmpSettingv3UsmUserName_Object = MibScalar
pduSnmpSettingv3UsmUserName = _PduSnmpSettingv3UsmUserName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 2, 1),
    _PduSnmpSettingv3UsmUserName_Type()
)
pduSnmpSettingv3UsmUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingv3UsmUserName.setStatus("mandatory")


class _PduSnmpSettingv3UsmAuthPasswd_Type(DisplayString):
    """Custom type pduSnmpSettingv3UsmAuthPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSnmpSettingv3UsmAuthPasswd_Type.__name__ = "DisplayString"
_PduSnmpSettingv3UsmAuthPasswd_Object = MibScalar
pduSnmpSettingv3UsmAuthPasswd = _PduSnmpSettingv3UsmAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 2, 2),
    _PduSnmpSettingv3UsmAuthPasswd_Type()
)
pduSnmpSettingv3UsmAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingv3UsmAuthPasswd.setStatus("mandatory")


class _PduSnmpSettingv3UsmAuthMode_Type(Integer32):
    """Custom type pduSnmpSettingv3UsmAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_PduSnmpSettingv3UsmAuthMode_Type.__name__ = "Integer32"
_PduSnmpSettingv3UsmAuthMode_Object = MibScalar
pduSnmpSettingv3UsmAuthMode = _PduSnmpSettingv3UsmAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 2, 3),
    _PduSnmpSettingv3UsmAuthMode_Type()
)
pduSnmpSettingv3UsmAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingv3UsmAuthMode.setStatus("mandatory")


class _PduSnmpSettingv3UsmPrivPasswd_Type(DisplayString):
    """Custom type pduSnmpSettingv3UsmPrivPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSnmpSettingv3UsmPrivPasswd_Type.__name__ = "DisplayString"
_PduSnmpSettingv3UsmPrivPasswd_Object = MibScalar
pduSnmpSettingv3UsmPrivPasswd = _PduSnmpSettingv3UsmPrivPasswd_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 2, 4),
    _PduSnmpSettingv3UsmPrivPasswd_Type()
)
pduSnmpSettingv3UsmPrivPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingv3UsmPrivPasswd.setStatus("mandatory")


class _PduSnmpSettingv3UsmPrivMode_Type(Integer32):
    """Custom type pduSnmpSettingv3UsmPrivMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 1),
          ("aes", 2))
    )


_PduSnmpSettingv3UsmPrivMode_Type.__name__ = "Integer32"
_PduSnmpSettingv3UsmPrivMode_Object = MibScalar
pduSnmpSettingv3UsmPrivMode = _PduSnmpSettingv3UsmPrivMode_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 2, 5),
    _PduSnmpSettingv3UsmPrivMode_Type()
)
pduSnmpSettingv3UsmPrivMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingv3UsmPrivMode.setStatus("mandatory")


class _PduSnmpSettingv3UsmSecurityLevel_Type(Integer32):
    """Custom type pduSnmpSettingv3UsmSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_PduSnmpSettingv3UsmSecurityLevel_Type.__name__ = "Integer32"
_PduSnmpSettingv3UsmSecurityLevel_Object = MibScalar
pduSnmpSettingv3UsmSecurityLevel = _PduSnmpSettingv3UsmSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 2, 6),
    _PduSnmpSettingv3UsmSecurityLevel_Type()
)
pduSnmpSettingv3UsmSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingv3UsmSecurityLevel.setStatus("mandatory")
_PduSnmpSettingTrap_ObjectIdentity = ObjectIdentity
pduSnmpSettingTrap = _PduSnmpSettingTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 3)
)
_PduSnmpSettingTrapTable_Object = MibTable
pduSnmpSettingTrapTable = _PduSnmpSettingTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 3, 1)
)
if mibBuilder.loadTexts:
    pduSnmpSettingTrapTable.setStatus("mandatory")
_PduSnmpSettingTrapEntry_Object = MibTableRow
pduSnmpSettingTrapEntry = _PduSnmpSettingTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 3, 1, 1)
)
pduSnmpSettingTrapEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduSnmpSettingTrapIndex"),
)
if mibBuilder.loadTexts:
    pduSnmpSettingTrapEntry.setStatus("mandatory")


class _PduSnmpSettingTrapIndex_Type(Integer32):
    """Custom type pduSnmpSettingTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PduSnmpSettingTrapIndex_Type.__name__ = "Integer32"
_PduSnmpSettingTrapIndex_Object = MibTableColumn
pduSnmpSettingTrapIndex = _PduSnmpSettingTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 3, 1, 1, 1),
    _PduSnmpSettingTrapIndex_Type()
)
pduSnmpSettingTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSnmpSettingTrapIndex.setStatus("mandatory")


class _PduSnmpSettingTrapRcvrAddress_Type(DisplayString):
    """Custom type pduSnmpSettingTrapRcvrAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduSnmpSettingTrapRcvrAddress_Type.__name__ = "DisplayString"
_PduSnmpSettingTrapRcvrAddress_Object = MibTableColumn
pduSnmpSettingTrapRcvrAddress = _PduSnmpSettingTrapRcvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 3, 1, 1, 2),
    _PduSnmpSettingTrapRcvrAddress_Type()
)
pduSnmpSettingTrapRcvrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingTrapRcvrAddress.setStatus("mandatory")


class _PduSnmpSettingTrapEvtLevel_Type(Integer32):
    """Custom type pduSnmpSettingTrapEvtLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informational", 1),
          ("warning", 2),
          ("critical", 3))
    )


_PduSnmpSettingTrapEvtLevel_Type.__name__ = "Integer32"
_PduSnmpSettingTrapEvtLevel_Object = MibTableColumn
pduSnmpSettingTrapEvtLevel = _PduSnmpSettingTrapEvtLevel_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 3, 1, 1, 3),
    _PduSnmpSettingTrapEvtLevel_Type()
)
pduSnmpSettingTrapEvtLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingTrapEvtLevel.setStatus("mandatory")


class _PduSnmpSettingTrapVer_Type(Integer32):
    """Custom type pduSnmpSettingTrapVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_PduSnmpSettingTrapVer_Type.__name__ = "Integer32"
_PduSnmpSettingTrapVer_Object = MibTableColumn
pduSnmpSettingTrapVer = _PduSnmpSettingTrapVer_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 3, 1, 1, 4),
    _PduSnmpSettingTrapVer_Type()
)
pduSnmpSettingTrapVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingTrapVer.setStatus("mandatory")


class _PduSnmpSettingTrapDesc_Type(DisplayString):
    """Custom type pduSnmpSettingTrapDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduSnmpSettingTrapDesc_Type.__name__ = "DisplayString"
_PduSnmpSettingTrapDesc_Object = MibTableColumn
pduSnmpSettingTrapDesc = _PduSnmpSettingTrapDesc_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 7, 3, 1, 1, 5),
    _PduSnmpSettingTrapDesc_Type()
)
pduSnmpSettingTrapDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSnmpSettingTrapDesc.setStatus("mandatory")
_PduEmailSetting_ObjectIdentity = ObjectIdentity
pduEmailSetting = _PduEmailSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8)
)
_PduEmailSettingSmtp_ObjectIdentity = ObjectIdentity
pduEmailSettingSmtp = _PduEmailSettingSmtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 1)
)


class _PduEmailSettingSmtpIp_Type(DisplayString):
    """Custom type pduEmailSettingSmtpIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduEmailSettingSmtpIp_Type.__name__ = "DisplayString"
_PduEmailSettingSmtpIp_Object = MibScalar
pduEmailSettingSmtpIp = _PduEmailSettingSmtpIp_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 1, 1),
    _PduEmailSettingSmtpIp_Type()
)
pduEmailSettingSmtpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingSmtpIp.setStatus("mandatory")


class _PduEmailSettingSmtpPort_Type(Integer32):
    """Custom type pduEmailSettingSmtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PduEmailSettingSmtpPort_Type.__name__ = "Integer32"
_PduEmailSettingSmtpPort_Object = MibScalar
pduEmailSettingSmtpPort = _PduEmailSettingSmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 1, 2),
    _PduEmailSettingSmtpPort_Type()
)
pduEmailSettingSmtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingSmtpPort.setStatus("mandatory")


class _PduEmailSettingSmtpSender_Type(DisplayString):
    """Custom type pduEmailSettingSmtpSender based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduEmailSettingSmtpSender_Type.__name__ = "DisplayString"
_PduEmailSettingSmtpSender_Object = MibScalar
pduEmailSettingSmtpSender = _PduEmailSettingSmtpSender_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 1, 3),
    _PduEmailSettingSmtpSender_Type()
)
pduEmailSettingSmtpSender.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingSmtpSender.setStatus("mandatory")


class _PduEmailSettingSmtpSubject_Type(DisplayString):
    """Custom type pduEmailSettingSmtpSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduEmailSettingSmtpSubject_Type.__name__ = "DisplayString"
_PduEmailSettingSmtpSubject_Object = MibScalar
pduEmailSettingSmtpSubject = _PduEmailSettingSmtpSubject_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 1, 4),
    _PduEmailSettingSmtpSubject_Type()
)
pduEmailSettingSmtpSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingSmtpSubject.setStatus("mandatory")


class _PduEmailSettingSmtpAuthEn_Type(Integer32):
    """Custom type pduEmailSettingSmtpAuthEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduEmailSettingSmtpAuthEn_Type.__name__ = "Integer32"
_PduEmailSettingSmtpAuthEn_Object = MibScalar
pduEmailSettingSmtpAuthEn = _PduEmailSettingSmtpAuthEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 1, 5),
    _PduEmailSettingSmtpAuthEn_Type()
)
pduEmailSettingSmtpAuthEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingSmtpAuthEn.setStatus("mandatory")


class _PduEmailSettingSmtpAuthUser_Type(DisplayString):
    """Custom type pduEmailSettingSmtpAuthUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduEmailSettingSmtpAuthUser_Type.__name__ = "DisplayString"
_PduEmailSettingSmtpAuthUser_Object = MibScalar
pduEmailSettingSmtpAuthUser = _PduEmailSettingSmtpAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 1, 6),
    _PduEmailSettingSmtpAuthUser_Type()
)
pduEmailSettingSmtpAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingSmtpAuthUser.setStatus("mandatory")


class _PduEmailSettingSmtpAuthPasswd_Type(DisplayString):
    """Custom type pduEmailSettingSmtpAuthPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduEmailSettingSmtpAuthPasswd_Type.__name__ = "DisplayString"
_PduEmailSettingSmtpAuthPasswd_Object = MibScalar
pduEmailSettingSmtpAuthPasswd = _PduEmailSettingSmtpAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 1, 7),
    _PduEmailSettingSmtpAuthPasswd_Type()
)
pduEmailSettingSmtpAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingSmtpAuthPasswd.setStatus("mandatory")
_PduEmailSettingNotify_ObjectIdentity = ObjectIdentity
pduEmailSettingNotify = _PduEmailSettingNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 2)
)
_PduEmailSettingNotifyTable_Object = MibTable
pduEmailSettingNotifyTable = _PduEmailSettingNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 2, 1)
)
if mibBuilder.loadTexts:
    pduEmailSettingNotifyTable.setStatus("mandatory")
_PduEmailSettingNotifyEntry_Object = MibTableRow
pduEmailSettingNotifyEntry = _PduEmailSettingNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 2, 1, 1)
)
pduEmailSettingNotifyEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduEmailSettingNotifyIndex"),
)
if mibBuilder.loadTexts:
    pduEmailSettingNotifyEntry.setStatus("mandatory")


class _PduEmailSettingNotifyIndex_Type(Integer32):
    """Custom type pduEmailSettingNotifyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PduEmailSettingNotifyIndex_Type.__name__ = "Integer32"
_PduEmailSettingNotifyIndex_Object = MibTableColumn
pduEmailSettingNotifyIndex = _PduEmailSettingNotifyIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 2, 1, 1, 1),
    _PduEmailSettingNotifyIndex_Type()
)
pduEmailSettingNotifyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEmailSettingNotifyIndex.setStatus("mandatory")


class _PduEmailSettingNotifyRecvAddr_Type(DisplayString):
    """Custom type pduEmailSettingNotifyRecvAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduEmailSettingNotifyRecvAddr_Type.__name__ = "DisplayString"
_PduEmailSettingNotifyRecvAddr_Object = MibTableColumn
pduEmailSettingNotifyRecvAddr = _PduEmailSettingNotifyRecvAddr_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 2, 1, 1, 2),
    _PduEmailSettingNotifyRecvAddr_Type()
)
pduEmailSettingNotifyRecvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingNotifyRecvAddr.setStatus("mandatory")


class _PduEmailSettingNotifyType_Type(Integer32):
    """Custom type pduEmailSettingNotifyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("events", 2),
          ("eventsStatus", 3))
    )


_PduEmailSettingNotifyType_Type.__name__ = "Integer32"
_PduEmailSettingNotifyType_Object = MibTableColumn
pduEmailSettingNotifyType = _PduEmailSettingNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 2, 1, 1, 3),
    _PduEmailSettingNotifyType_Type()
)
pduEmailSettingNotifyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingNotifyType.setStatus("mandatory")


class _PduEmailSettingNotifyEvtLev_Type(Integer32):
    """Custom type pduEmailSettingNotifyEvtLev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("warning", 2),
          ("informational", 3))
    )


_PduEmailSettingNotifyEvtLev_Type.__name__ = "Integer32"
_PduEmailSettingNotifyEvtLev_Object = MibTableColumn
pduEmailSettingNotifyEvtLev = _PduEmailSettingNotifyEvtLev_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 2, 1, 1, 4),
    _PduEmailSettingNotifyEvtLev_Type()
)
pduEmailSettingNotifyEvtLev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingNotifyEvtLev.setStatus("mandatory")


class _PduEmailSettingNotifyDesc_Type(DisplayString):
    """Custom type pduEmailSettingNotifyDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduEmailSettingNotifyDesc_Type.__name__ = "DisplayString"
_PduEmailSettingNotifyDesc_Object = MibTableColumn
pduEmailSettingNotifyDesc = _PduEmailSettingNotifyDesc_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 8, 2, 1, 1, 5),
    _PduEmailSettingNotifyDesc_Type()
)
pduEmailSettingNotifyDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEmailSettingNotifyDesc.setStatus("mandatory")
_PduUserSetting_ObjectIdentity = ObjectIdentity
pduUserSetting = _PduUserSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9)
)
_PduUserSettingLocal_ObjectIdentity = ObjectIdentity
pduUserSettingLocal = _PduUserSettingLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 1)
)
_PduUserSettingLocalTable_Object = MibTable
pduUserSettingLocalTable = _PduUserSettingLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pduUserSettingLocalTable.setStatus("mandatory")
_PduUserSettingLocalEntry_Object = MibTableRow
pduUserSettingLocalEntry = _PduUserSettingLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 1, 1, 1)
)
pduUserSettingLocalEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduUserSettingLocalIndex"),
)
if mibBuilder.loadTexts:
    pduUserSettingLocalEntry.setStatus("mandatory")


class _PduUserSettingLocalIndex_Type(Integer32):
    """Custom type pduUserSettingLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PduUserSettingLocalIndex_Type.__name__ = "Integer32"
_PduUserSettingLocalIndex_Object = MibTableColumn
pduUserSettingLocalIndex = _PduUserSettingLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 1, 1, 1, 1),
    _PduUserSettingLocalIndex_Type()
)
pduUserSettingLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUserSettingLocalIndex.setStatus("mandatory")


class _PduUserSettingLocalUserName_Type(DisplayString):
    """Custom type pduUserSettingLocalUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduUserSettingLocalUserName_Type.__name__ = "DisplayString"
_PduUserSettingLocalUserName_Object = MibTableColumn
pduUserSettingLocalUserName = _PduUserSettingLocalUserName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 1, 1, 1, 2),
    _PduUserSettingLocalUserName_Type()
)
pduUserSettingLocalUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUserSettingLocalUserName.setStatus("mandatory")


class _PduUserSettingLocalPasswd_Type(DisplayString):
    """Custom type pduUserSettingLocalPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduUserSettingLocalPasswd_Type.__name__ = "DisplayString"
_PduUserSettingLocalPasswd_Object = MibTableColumn
pduUserSettingLocalPasswd = _PduUserSettingLocalPasswd_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 1, 1, 1, 3),
    _PduUserSettingLocalPasswd_Type()
)
pduUserSettingLocalPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUserSettingLocalPasswd.setStatus("mandatory")


class _PduUserSettingLocalPrivilege_Type(Integer32):
    """Custom type pduUserSettingLocalPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("readOnly", 2),
          ("readWrite", 3))
    )


_PduUserSettingLocalPrivilege_Type.__name__ = "Integer32"
_PduUserSettingLocalPrivilege_Object = MibTableColumn
pduUserSettingLocalPrivilege = _PduUserSettingLocalPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 1, 1, 1, 4),
    _PduUserSettingLocalPrivilege_Type()
)
pduUserSettingLocalPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUserSettingLocalPrivilege.setStatus("mandatory")
_PduUserSettingRadius_ObjectIdentity = ObjectIdentity
pduUserSettingRadius = _PduUserSettingRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 2)
)
_PduUserSettingRadiusTable_Object = MibTable
pduUserSettingRadiusTable = _PduUserSettingRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pduUserSettingRadiusTable.setStatus("mandatory")
_PduUserSettingRadiusEntry_Object = MibTableRow
pduUserSettingRadiusEntry = _PduUserSettingRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 2, 1, 1)
)
pduUserSettingRadiusEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduUserSettingRadiusIndex"),
)
if mibBuilder.loadTexts:
    pduUserSettingRadiusEntry.setStatus("mandatory")


class _PduUserSettingRadiusIndex_Type(Integer32):
    """Custom type pduUserSettingRadiusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PduUserSettingRadiusIndex_Type.__name__ = "Integer32"
_PduUserSettingRadiusIndex_Object = MibTableColumn
pduUserSettingRadiusIndex = _PduUserSettingRadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 2, 1, 1, 1),
    _PduUserSettingRadiusIndex_Type()
)
pduUserSettingRadiusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUserSettingRadiusIndex.setStatus("mandatory")


class _PduUserSettingRadiusUserName_Type(DisplayString):
    """Custom type pduUserSettingRadiusUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduUserSettingRadiusUserName_Type.__name__ = "DisplayString"
_PduUserSettingRadiusUserName_Object = MibTableColumn
pduUserSettingRadiusUserName = _PduUserSettingRadiusUserName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 2, 1, 1, 2),
    _PduUserSettingRadiusUserName_Type()
)
pduUserSettingRadiusUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUserSettingRadiusUserName.setStatus("mandatory")


class _PduUserSettingRadiusPrivilege_Type(Integer32):
    """Custom type pduUserSettingRadiusPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("readOnly", 2),
          ("readWrite", 3))
    )


_PduUserSettingRadiusPrivilege_Type.__name__ = "Integer32"
_PduUserSettingRadiusPrivilege_Object = MibTableColumn
pduUserSettingRadiusPrivilege = _PduUserSettingRadiusPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 2, 1, 1, 3),
    _PduUserSettingRadiusPrivilege_Type()
)
pduUserSettingRadiusPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUserSettingRadiusPrivilege.setStatus("mandatory")
_PduUserSettingAuthCfg_ObjectIdentity = ObjectIdentity
pduUserSettingAuthCfg = _PduUserSettingAuthCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 3)
)


class _PduUserSettingAuthCfgAdminName_Type(DisplayString):
    """Custom type pduUserSettingAuthCfgAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PduUserSettingAuthCfgAdminName_Type.__name__ = "DisplayString"
_PduUserSettingAuthCfgAdminName_Object = MibScalar
pduUserSettingAuthCfgAdminName = _PduUserSettingAuthCfgAdminName_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 3, 1),
    _PduUserSettingAuthCfgAdminName_Type()
)
pduUserSettingAuthCfgAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUserSettingAuthCfgAdminName.setStatus("mandatory")


class _PduUserSettingAuthCfgAdminPasswd_Type(DisplayString):
    """Custom type pduUserSettingAuthCfgAdminPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PduUserSettingAuthCfgAdminPasswd_Type.__name__ = "DisplayString"
_PduUserSettingAuthCfgAdminPasswd_Object = MibScalar
pduUserSettingAuthCfgAdminPasswd = _PduUserSettingAuthCfgAdminPasswd_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 3, 9, 3, 2),
    _PduUserSettingAuthCfgAdminPasswd_Type()
)
pduUserSettingAuthCfgAdminPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUserSettingAuthCfgAdminPasswd.setStatus("mandatory")
_PduAdvanced_ObjectIdentity = ObjectIdentity
pduAdvanced = _PduAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4)
)
_PduSyslogSetting_ObjectIdentity = ObjectIdentity
pduSyslogSetting = _PduSyslogSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 1)
)
_PduSysEvtLog_ObjectIdentity = ObjectIdentity
pduSysEvtLog = _PduSysEvtLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 1, 1)
)


class _PduSysEvtLogEn_Type(Integer32):
    """Custom type pduSysEvtLogEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduSysEvtLogEn_Type.__name__ = "Integer32"
_PduSysEvtLogEn_Object = MibScalar
pduSysEvtLogEn = _PduSysEvtLogEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 1, 1, 1),
    _PduSysEvtLogEn_Type()
)
pduSysEvtLogEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSysEvtLogEn.setStatus("mandatory")


class _PduSysEvtLogIp_Type(DisplayString):
    """Custom type pduSysEvtLogIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduSysEvtLogIp_Type.__name__ = "DisplayString"
_PduSysEvtLogIp_Object = MibScalar
pduSysEvtLogIp = _PduSysEvtLogIp_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 1, 1, 2),
    _PduSysEvtLogIp_Type()
)
pduSysEvtLogIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSysEvtLogIp.setStatus("mandatory")


class _PduSysEvtLogPort_Type(Integer32):
    """Custom type pduSysEvtLogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PduSysEvtLogPort_Type.__name__ = "Integer32"
_PduSysEvtLogPort_Object = MibScalar
pduSysEvtLogPort = _PduSysEvtLogPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 1, 1, 3),
    _PduSysEvtLogPort_Type()
)
pduSysEvtLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduSysEvtLogPort.setStatus("mandatory")
_PduHisLog_ObjectIdentity = ObjectIdentity
pduHisLog = _PduHisLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 1, 2)
)


class _PduHisLogEn_Type(Integer32):
    """Custom type pduHisLogEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PduHisLogEn_Type.__name__ = "Integer32"
_PduHisLogEn_Object = MibScalar
pduHisLogEn = _PduHisLogEn_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 1, 2, 1),
    _PduHisLogEn_Type()
)
pduHisLogEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduHisLogEn.setStatus("mandatory")


class _PduHisLogIp_Type(DisplayString):
    """Custom type pduHisLogIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduHisLogIp_Type.__name__ = "DisplayString"
_PduHisLogIp_Object = MibScalar
pduHisLogIp = _PduHisLogIp_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 1, 2, 2),
    _PduHisLogIp_Type()
)
pduHisLogIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduHisLogIp.setStatus("mandatory")


class _PduHisLogPort_Type(Integer32):
    """Custom type pduHisLogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PduHisLogPort_Type.__name__ = "Integer32"
_PduHisLogPort_Object = MibScalar
pduHisLogPort = _PduHisLogPort_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 1, 2, 3),
    _PduHisLogPort_Type()
)
pduHisLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduHisLogPort.setStatus("mandatory")
_PduLinksSetting_ObjectIdentity = ObjectIdentity
pduLinksSetting = _PduLinksSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 2)
)
_PduLinksSettingTable_Object = MibTable
pduLinksSettingTable = _PduLinksSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    pduLinksSettingTable.setStatus("mandatory")
_PduLinksSettingEntry_Object = MibTableRow
pduLinksSettingEntry = _PduLinksSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 2, 1, 1)
)
pduLinksSettingEntry.setIndexNames(
    (0, "SimplePDU-MIB", "pduLinksSettingIndex"),
)
if mibBuilder.loadTexts:
    pduLinksSettingEntry.setStatus("mandatory")


class _PduLinksSettingIndex_Type(Integer32):
    """Custom type pduLinksSettingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_PduLinksSettingIndex_Type.__name__ = "Integer32"
_PduLinksSettingIndex_Object = MibTableColumn
pduLinksSettingIndex = _PduLinksSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 2, 1, 1, 1),
    _PduLinksSettingIndex_Type()
)
pduLinksSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduLinksSettingIndex.setStatus("mandatory")


class _PduLinksSettingScreenText_Type(DisplayString):
    """Custom type pduLinksSettingScreenText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduLinksSettingScreenText_Type.__name__ = "DisplayString"
_PduLinksSettingScreenText_Object = MibTableColumn
pduLinksSettingScreenText = _PduLinksSettingScreenText_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 2, 1, 1, 2),
    _PduLinksSettingScreenText_Type()
)
pduLinksSettingScreenText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduLinksSettingScreenText.setStatus("mandatory")


class _PduLinksSettingAddress_Type(DisplayString):
    """Custom type pduLinksSettingAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduLinksSettingAddress_Type.__name__ = "DisplayString"
_PduLinksSettingAddress_Object = MibTableColumn
pduLinksSettingAddress = _PduLinksSettingAddress_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 2, 1, 1, 3),
    _PduLinksSettingAddress_Type()
)
pduLinksSettingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduLinksSettingAddress.setStatus("mandatory")


class _PduLinksSettingStatus_Type(Integer32):
    """Custom type pduLinksSettingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hide", 1),
          ("show", 2))
    )


_PduLinksSettingStatus_Type.__name__ = "Integer32"
_PduLinksSettingStatus_Object = MibTableColumn
pduLinksSettingStatus = _PduLinksSettingStatus_Object(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 1, 4, 2, 1, 1, 4),
    _PduLinksSettingStatus_Type()
)
pduLinksSettingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduLinksSettingStatus.setStatus("mandatory")
_PduTraps_ObjectIdentity = ObjectIdentity
pduTraps = _PduTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2)
)

# Managed Objects groups


# Notification objects

pduSysColdBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 1)
)
if mibBuilder.loadTexts:
    pduSysColdBoot.setStatus(
        ""
    )

pduSysWarmBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 2)
)
if mibBuilder.loadTexts:
    pduSysWarmBoot.setStatus(
        ""
    )

pduSysEMDRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 3)
)
if mibBuilder.loadTexts:
    pduSysEMDRestore.setStatus(
        ""
    )

pduSysEMDLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 4)
)
if mibBuilder.loadTexts:
    pduSysEMDLost.setStatus(
        ""
    )

pduSysInletRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 5)
)
if mibBuilder.loadTexts:
    pduSysInletRestore.setStatus(
        ""
    )

pduSysInletLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 6)
)
if mibBuilder.loadTexts:
    pduSysInletLost.setStatus(
        ""
    )

pduInletLoadWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 7)
)
if mibBuilder.loadTexts:
    pduInletLoadWarn.setStatus(
        ""
    )

pduInletLoadWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 8)
)
if mibBuilder.loadTexts:
    pduInletLoadWarnToNormal.setStatus(
        ""
    )

pduInletLoadCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 9)
)
if mibBuilder.loadTexts:
    pduInletLoadCritical.setStatus(
        ""
    )

pduInletLoadCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 10)
)
if mibBuilder.loadTexts:
    pduInletLoadCritToWarn.setStatus(
        ""
    )

pduInletLoadBalanceWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 11)
)
if mibBuilder.loadTexts:
    pduInletLoadBalanceWarn.setStatus(
        ""
    )

pduInletLoadBalanceWarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 12)
)
if mibBuilder.loadTexts:
    pduInletLoadBalanceWarnToNormal.setStatus(
        ""
    )

pduInletLoadBalanceCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 13)
)
if mibBuilder.loadTexts:
    pduInletLoadBalanceCritical.setStatus(
        ""
    )

pduInletLoadBalanceCritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 14)
)
if mibBuilder.loadTexts:
    pduInletLoadBalanceCritToWarn.setStatus(
        ""
    )

pduInletCurrPhase1CB1Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 15)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1CB1Warn.setStatus(
        ""
    )

pduInletCurrPhase1CB1WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 16)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1CB1WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase1CB1Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 17)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1CB1Critical.setStatus(
        ""
    )

pduInletCurrPhase1CB1CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 18)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1CB1CritToWarn.setStatus(
        ""
    )

pduInletCurrPhase2CB1Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 19)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2CB1Warn.setStatus(
        ""
    )

pduInletCurrPhase2CB1WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 20)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2CB1WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase2CB1Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 21)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2CB1Critical.setStatus(
        ""
    )

pduInletCurrPhase2CB1CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 22)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2CB1CritToWarn.setStatus(
        ""
    )

pduInletCurrPhase3CB1Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 23)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3CB1Warn.setStatus(
        ""
    )

pduInletCurrPhase3CB1WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 24)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3CB1WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase3CB1Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 25)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3CB1Critical.setStatus(
        ""
    )

pduInletCurrPhase3CB1CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 26)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3CB1CritToWarn.setStatus(
        ""
    )

pduInletTotalCurrPhase1Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 27)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase1Warn.setStatus(
        ""
    )

pduInletTotalCurrPhase1WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 28)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase1WarnToNormal.setStatus(
        ""
    )

pduInletTotalCurrPhase1Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 29)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase1Critical.setStatus(
        ""
    )

pduInletTotalCurrPhase1CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 30)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase1CritToWarn.setStatus(
        ""
    )

pduInletTotalCurrPhase2Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 31)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase2Warn.setStatus(
        ""
    )

pduInletTotalCurrPhase2WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 32)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase2WarnToNormal.setStatus(
        ""
    )

pduInletTotalCurrPhase2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 33)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase2Critical.setStatus(
        ""
    )

pduInletTotalCurrPhase2CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 34)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase2CritToWarn.setStatus(
        ""
    )

pduInletTotalCurrPhase3Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 35)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase3Warn.setStatus(
        ""
    )

pduInletTotalCurrPhase3WarnToNprmal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 36)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase3WarnToNprmal.setStatus(
        ""
    )

pduInletTotalCurrPhase3Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 37)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase3Critical.setStatus(
        ""
    )

pduInletTotalCurrPhase3CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 38)
)
if mibBuilder.loadTexts:
    pduInletTotalCurrPhase3CritToWarn.setStatus(
        ""
    )

pduInletVoltPhase1Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 39)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1Warn.setStatus(
        ""
    )

pduInletVoltPhase1WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 40)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1WarnToNormal.setStatus(
        ""
    )

pduInletVoltPhase1Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 41)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1Critical.setStatus(
        ""
    )

pduInletVoltPhase1CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 42)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase1CritToWarn.setStatus(
        ""
    )

pduInletVoltPhase2Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 43)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2Warn.setStatus(
        ""
    )

pduInletVoltPhase2WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 44)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2WarnToNormal.setStatus(
        ""
    )

pduInletVoltPhase2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 45)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2Critical.setStatus(
        ""
    )

pduInletVoltPhase2CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 46)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase2CritToWarn.setStatus(
        ""
    )

pduInletVoltPhase3Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 47)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3Warn.setStatus(
        ""
    )

pduInletVoltPhase3WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 48)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3WarnToNormal.setStatus(
        ""
    )

pduInletVoltPhase3Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 49)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3Critical.setStatus(
        ""
    )

pduInletVoltPhase3CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 50)
)
if mibBuilder.loadTexts:
    pduInletVoltPhase3CritToWarn.setStatus(
        ""
    )

pduEmdTempOverHighWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 51)
)
if mibBuilder.loadTexts:
    pduEmdTempOverHighWarn.setStatus(
        ""
    )

pduEmdTempNotOverHighWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 52)
)
if mibBuilder.loadTexts:
    pduEmdTempNotOverHighWarn.setStatus(
        ""
    )

pduEmdTempOverHighCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 53)
)
if mibBuilder.loadTexts:
    pduEmdTempOverHighCrit.setStatus(
        ""
    )

pduEmdTempNotOverHighCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 54)
)
if mibBuilder.loadTexts:
    pduEmdTempNotOverHighCrit.setStatus(
        ""
    )

pduEmdTempUnderLowWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 55)
)
if mibBuilder.loadTexts:
    pduEmdTempUnderLowWarn.setStatus(
        ""
    )

pduEmdTempNotUnderLowWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 56)
)
if mibBuilder.loadTexts:
    pduEmdTempNotUnderLowWarn.setStatus(
        ""
    )

pduEmdTempUnderLowCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 57)
)
if mibBuilder.loadTexts:
    pduEmdTempUnderLowCrit.setStatus(
        ""
    )

pduEmdTempNotUnderLowCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 58)
)
if mibBuilder.loadTexts:
    pduEmdTempNotUnderLowCrit.setStatus(
        ""
    )

pduEmdHumiOverHighWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 59)
)
if mibBuilder.loadTexts:
    pduEmdHumiOverHighWarn.setStatus(
        ""
    )

pduEmdHumiNotOverHighWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 60)
)
if mibBuilder.loadTexts:
    pduEmdHumiNotOverHighWarn.setStatus(
        ""
    )

pduEmdHumiOverHighCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 61)
)
if mibBuilder.loadTexts:
    pduEmdHumiOverHighCrit.setStatus(
        ""
    )

pduEmdHumiNotOverHighCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 62)
)
if mibBuilder.loadTexts:
    pduEmdHumiNotOverHighCrit.setStatus(
        ""
    )

pduEmdHumiUnderLowWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 63)
)
if mibBuilder.loadTexts:
    pduEmdHumiUnderLowWarn.setStatus(
        ""
    )

pduEmdHumiNotUnderLowWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 64)
)
if mibBuilder.loadTexts:
    pduEmdHumiNotUnderLowWarn.setStatus(
        ""
    )

pduEmdHumiUnderLowCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 65)
)
if mibBuilder.loadTexts:
    pduEmdHumiUnderLowCrit.setStatus(
        ""
    )

pduEmdHumiNotUnderLowCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 66)
)
if mibBuilder.loadTexts:
    pduEmdHumiNotUnderLowCrit.setStatus(
        ""
    )

pduAlarm1Triggered = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 67)
)
if mibBuilder.loadTexts:
    pduAlarm1Triggered.setStatus(
        ""
    )

pduAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 68)
)
if mibBuilder.loadTexts:
    pduAlarm1Normal.setStatus(
        ""
    )

pduAlarm2Triggered = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 69)
)
if mibBuilder.loadTexts:
    pduAlarm2Triggered.setStatus(
        ""
    )

pduAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 70)
)
if mibBuilder.loadTexts:
    pduAlarm2Normal.setStatus(
        ""
    )

pduInletCurrPhase1CB2Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 71)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1CB2Warn.setStatus(
        ""
    )

pduInletCurrPhase1CB2WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 72)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1CB2WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase1CB2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 73)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1CB2Critical.setStatus(
        ""
    )

pduInletCurrPhase1CB2CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 74)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase1CB2CritToWarn.setStatus(
        ""
    )

pduInletCurrPhase2CB2Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 75)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2CB2Warn.setStatus(
        ""
    )

pduInletCurrPhase2CB2WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 76)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2CB2WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase2CB2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 77)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2CB2Critical.setStatus(
        ""
    )

pduInletCurrPhase2CB2CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 78)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase2CB2CritToWarn.setStatus(
        ""
    )

pduInletCurrPhase3CB2Warn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 79)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3CB2Warn.setStatus(
        ""
    )

pduInletCurrPhase3CB2WarnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 80)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3CB2WarnToNormal.setStatus(
        ""
    )

pduInletCurrPhase3CB2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 81)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3CB2Critical.setStatus(
        ""
    )

pduInletCurrPhase3CB2CritToWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 42610, 1, 4, 2, 2, 0, 82)
)
if mibBuilder.loadTexts:
    pduInletCurrPhase3CB2CritToWarn.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SimplePDU-MIB",
    **{"powertek": powertek,
       "product": product,
       "pdu": pdu,
       "simple": simple,
       "pduObjects": pduObjects,
       "pduSumOverview": pduSumOverview,
       "pduSysOverview": pduSysOverview,
       "pduOverview": pduOverview,
       "pduOverviewSystemAgenetVersion": pduOverviewSystemAgenetVersion,
       "pduOverviewPduTypeName": pduOverviewPduTypeName,
       "pduInputStat": pduInputStat,
       "pduInputStatTable": pduInputStatTable,
       "pduInputStatEntry": pduInputStatEntry,
       "pduInputStatPhaseIndex": pduInputStatPhaseIndex,
       "pduInputStatVoltage": pduInputStatVoltage,
       "pduInputStatActivePower": pduInputStatActivePower,
       "pduInputStatApparentPower": pduInputStatApparentPower,
       "pduInputStatCB1Current": pduInputStatCB1Current,
       "pduInputStatCB2Current": pduInputStatCB2Current,
       "pduInputStatTotalCurrent": pduInputStatTotalCurrent,
       "pduInputStatStatus": pduInputStatStatus,
       "pduInputStatLoadBalanceVal": pduInputStatLoadBalanceVal,
       "pduInputStatLoadBalanceStatus": pduInputStatLoadBalanceStatus,
       "pduInputStatResidualCurVal": pduInputStatResidualCurVal,
       "pduInputStatResidualCurStatus": pduInputStatResidualCurStatus,
       "pduNetConnect": pduNetConnect,
       "pduNetConnectTable": pduNetConnectTable,
       "pduNetConnectEntry": pduNetConnectEntry,
       "pduNetConnectIndex": pduNetConnectIndex,
       "pduNetConnectAddr": pduNetConnectAddr,
       "pduNetConnectType": pduNetConnectType,
       "pduNetConnectUserName": pduNetConnectUserName,
       "pduPowMgmt": pduPowMgmt,
       "pduInletCfg": pduInletCfg,
       "pduPhaseLoadMgmt": pduPhaseLoadMgmt,
       "pduPhaseLoadMgmtTable": pduPhaseLoadMgmtTable,
       "pduPhaseLoadMgmtEntry": pduPhaseLoadMgmtEntry,
       "pduPhaseLoadMgmtPhaseIndex": pduPhaseLoadMgmtPhaseIndex,
       "pduPhaseLoadMgmtCurrentTotal": pduPhaseLoadMgmtCurrentTotal,
       "pduPhaseLoadMgmtVoltage": pduPhaseLoadMgmtVoltage,
       "pduPhaseLoadMgmtFrequency": pduPhaseLoadMgmtFrequency,
       "pduPhaseLoadMgmtPowerFactor": pduPhaseLoadMgmtPowerFactor,
       "pduPhaseLoadMgmtPowerActiveApparent": pduPhaseLoadMgmtPowerActiveApparent,
       "pduPhaseLoadMgmtReactivePower": pduPhaseLoadMgmtReactivePower,
       "pduPhaseLoadMgmtStatus": pduPhaseLoadMgmtStatus,
       "pduCfg": pduCfg,
       "pduCfgCritOverLoadAlm": pduCfgCritOverLoadAlm,
       "pduCfgCritLoadBalanceAlm": pduCfgCritLoadBalanceAlm,
       "pduCfgCritOverCurrAlmCB1Ph1": pduCfgCritOverCurrAlmCB1Ph1,
       "pduCfgCritOverCurrAlmCB1Ph2": pduCfgCritOverCurrAlmCB1Ph2,
       "pduCfgCritOverCurrAlmCB1Ph3": pduCfgCritOverCurrAlmCB1Ph3,
       "pduCfgCritOverCurrAlmCB2Ph1": pduCfgCritOverCurrAlmCB2Ph1,
       "pduCfgCritOverCurrAlmCB2Ph2": pduCfgCritOverCurrAlmCB2Ph2,
       "pduCfgCritOverCurrAlmCB2Ph3": pduCfgCritOverCurrAlmCB2Ph3,
       "pduCfgCritOverTotalCurrAlm": pduCfgCritOverTotalCurrAlm,
       "pduCfgCritOverVolAlm": pduCfgCritOverVolAlm,
       "pduCfgWarnOverLoadAlm": pduCfgWarnOverLoadAlm,
       "pduCfgWarnLoadBalanceAlm": pduCfgWarnLoadBalanceAlm,
       "pduCfgWarnOverCurrAlmCB1Ph1": pduCfgWarnOverCurrAlmCB1Ph1,
       "pduCfgWarnOverCurrAlmCB1Ph2": pduCfgWarnOverCurrAlmCB1Ph2,
       "pduCfgWarnOverCurrAlmCB1Ph3": pduCfgWarnOverCurrAlmCB1Ph3,
       "pduCfgWarnOverCurrAlmCB2Ph1": pduCfgWarnOverCurrAlmCB2Ph1,
       "pduCfgWarnOverCurrAlmCB2Ph2": pduCfgWarnOverCurrAlmCB2Ph2,
       "pduCfgWarnOverCurrAlmCB2Ph3": pduCfgWarnOverCurrAlmCB2Ph3,
       "pduCfgWarnOverTotalCurrAlm": pduCfgWarnOverTotalCurrAlm,
       "pduCfgWarnOverVolAlm": pduCfgWarnOverVolAlm,
       "pduStat": pduStat,
       "pduStatPower": pduStatPower,
       "pduStatPowerStat": pduStatPowerStat,
       "pduStatTotalEnergy": pduStatTotalEnergy,
       "pduStatTotalEnergyRecord": pduStatTotalEnergyRecord,
       "pduStatPh1Energy": pduStatPh1Energy,
       "pduStatPh1EnergyRecord": pduStatPh1EnergyRecord,
       "pduStatPh2Energy": pduStatPh2Energy,
       "pduStatPh2EnergyRecord": pduStatPh2EnergyRecord,
       "pduStatPh3Energy": pduStatPh3Energy,
       "pduStatPh3EnergyRecord": pduStatPh3EnergyRecord,
       "pduStatLoadBalance": pduStatLoadBalance,
       "pduStatLoadBalanceStat": pduStatLoadBalanceStat,
       "pduStatTotalEnergyCln": pduStatTotalEnergyCln,
       "pduStatPh1EnergyCln": pduStatPh1EnergyCln,
       "pduStatPh2EnergyCln": pduStatPh2EnergyCln,
       "pduStatPh3EnergyCln": pduStatPh3EnergyCln,
       "pduEnvMon": pduEnvMon,
       "pduEmdCurrInfo": pduEmdCurrInfo,
       "pduEmdCurrInfoTable": pduEmdCurrInfoTable,
       "pduEmdCurrInfoEntry": pduEmdCurrInfoEntry,
       "pduEmdCurrInfoEmdStatIndex": pduEmdCurrInfoEmdStatIndex,
       "pduEmdCurrInfoHumidityName": pduEmdCurrInfoHumidityName,
       "pduEmdCurrInfoHumidityStat": pduEmdCurrInfoHumidityStat,
       "pduEmdCurrInfoHumidityValue": pduEmdCurrInfoHumidityValue,
       "pduEmdCurrInfoTempName": pduEmdCurrInfoTempName,
       "pduEmdCurrInfoTempStat": pduEmdCurrInfoTempStat,
       "pduEmdCurrInfoTempValue": pduEmdCurrInfoTempValue,
       "pduEmdCurrInfoAlm1Name": pduEmdCurrInfoAlm1Name,
       "pduEmdCurrInfoAlm1Stat": pduEmdCurrInfoAlm1Stat,
       "pduEmdCurrInfoAlm2Name": pduEmdCurrInfoAlm2Name,
       "pduEmdCurrInfoAlm2Stat": pduEmdCurrInfoAlm2Stat,
       "pduEmdCurrInfoLocName": pduEmdCurrInfoLocName,
       "pduEmdCurrInfoAddress": pduEmdCurrInfoAddress,
       "pduEmdCfg": pduEmdCfg,
       "pduEmdCfgTable": pduEmdCfgTable,
       "pduEmdCfgEntry": pduEmdCfgEntry,
       "pduEmdCfgEMDIndex": pduEmdCfgEMDIndex,
       "pduEmdCfgEMDName": pduEmdCfgEMDName,
       "pduEmdCfgEMDAddress": pduEmdCfgEMDAddress,
       "pduEmdCfgAppFWVer": pduEmdCfgAppFWVer,
       "pduEmdCfgLocName": pduEmdCfgLocName,
       "pduEmdCfgAlm1Name": pduEmdCfgAlm1Name,
       "pduEmdCfgAlm2Name": pduEmdCfgAlm2Name,
       "pduEmdCfgAlm1Type": pduEmdCfgAlm1Type,
       "pduEmdCfgAlm2Type": pduEmdCfgAlm2Type,
       "pduEmdCfgTempSenName": pduEmdCfgTempSenName,
       "pduEmdCfgTempCritHigh": pduEmdCfgTempCritHigh,
       "pduEmdCfgTempCritHighType": pduEmdCfgTempCritHighType,
       "pduEmdCfgTempCritLow": pduEmdCfgTempCritLow,
       "pduEmdCfgTempCritLowType": pduEmdCfgTempCritLowType,
       "pduEmdCfgTempWarnHigh": pduEmdCfgTempWarnHigh,
       "pduEmdCfgTempWarnHighType": pduEmdCfgTempWarnHighType,
       "pduEmdCfgTempWarnLow": pduEmdCfgTempWarnLow,
       "pduEmdCfgTempWarnLowType": pduEmdCfgTempWarnLowType,
       "pduEmdCfgTempCalOffset": pduEmdCfgTempCalOffset,
       "pduEmdCfgHumiditySenName": pduEmdCfgHumiditySenName,
       "pduEmdCfgHumidityCritHigh": pduEmdCfgHumidityCritHigh,
       "pduEmdCfgHumidityCritHighType": pduEmdCfgHumidityCritHighType,
       "pduEmdCfgHumidityCritLow": pduEmdCfgHumidityCritLow,
       "pduEmdCfgHumidityCritLowType": pduEmdCfgHumidityCritLowType,
       "pduEmdCfgHumidityWarnHigh": pduEmdCfgHumidityWarnHigh,
       "pduEmdCfgHumidityWarnHighType": pduEmdCfgHumidityWarnHighType,
       "pduEmdCfgHumidityWarnLow": pduEmdCfgHumidityWarnLow,
       "pduEmdCfgHumidityWarnLowType": pduEmdCfgHumidityWarnLowType,
       "pduEmdCfgHumidityCalOffset": pduEmdCfgHumidityCalOffset,
       "pduSettings": pduSettings,
       "pduGeneralSet": pduGeneralSet,
       "pduSysAdm": pduSysAdm,
       "pduSysAdmSysName": pduSysAdmSysName,
       "pduSysAdmSysContact": pduSysAdmSysContact,
       "pduSysAdmSysLocation": pduSysAdmSysLocation,
       "pduSysAdmLogInterval": pduSysAdmLogInterval,
       "pduSysAdmWebRefresh": pduSysAdmWebRefresh,
       "pduSysAdmWebTimeout": pduSysAdmWebTimeout,
       "pduDateAndTime": pduDateAndTime,
       "pduDateAndTimeCurrDateAndTime": pduDateAndTimeCurrDateAndTime,
       "pduDateAndTimeTimeZone": pduDateAndTimeTimeZone,
       "pduDateAndTimeDateFormat": pduDateAndTimeDateFormat,
       "pduDateAndTimeSyncMode": pduDateAndTimeSyncMode,
       "pduDateAndTimeManualDate": pduDateAndTimeManualDate,
       "pduDateAndTimeManualTime": pduDateAndTimeManualTime,
       "pduDateAndTimeNtpServer": pduDateAndTimeNtpServer,
       "pduDateAndTimeNtpSyncIntervalType": pduDateAndTimeNtpSyncIntervalType,
       "pduDateAndTimeNtpSyncInterval": pduDateAndTimeNtpSyncInterval,
       "pduDateAndTimeNtpTimeDayLightSaving": pduDateAndTimeNtpTimeDayLightSaving,
       "pduIecViewMgmt": pduIecViewMgmt,
       "pduIecViewMgmtEn": pduIecViewMgmtEn,
       "pduIecViewMgmtServer": pduIecViewMgmtServer,
       "pduIecViewMgmtGuid": pduIecViewMgmtGuid,
       "pduIecViewMgmtPort": pduIecViewMgmtPort,
       "pduIecViewMgmtPasswd": pduIecViewMgmtPasswd,
       "pduTcpIp": pduTcpIp,
       "pduIpv4Setting": pduIpv4Setting,
       "pduIpv4SettingDhcpEn": pduIpv4SettingDhcpEn,
       "pduIpv4SettingAddress": pduIpv4SettingAddress,
       "pduIpv4SettingMask": pduIpv4SettingMask,
       "pduIpv4SettingGateway": pduIpv4SettingGateway,
       "pduIpv4SettingDns1": pduIpv4SettingDns1,
       "pduIpv4SettingDns2": pduIpv4SettingDns2,
       "pduIpv6Setting": pduIpv6Setting,
       "pduIpv6SettingEn": pduIpv6SettingEn,
       "pduIpv6SettingCfg": pduIpv6SettingCfg,
       "pduIpv6SettingLocalAddress": pduIpv6SettingLocalAddress,
       "pduIpv6SettingGlobalAddress": pduIpv6SettingGlobalAddress,
       "pduIpv6SettingRouter": pduIpv6SettingRouter,
       "pduIpv6SettingDns1": pduIpv6SettingDns1,
       "pduIpv6SettingDns2": pduIpv6SettingDns2,
       "pduAccessIpSetting": pduAccessIpSetting,
       "pduAccessIpSettingEn": pduAccessIpSettingEn,
       "pduAccessIpSettingTable": pduAccessIpSettingTable,
       "pduAccessIpSettingTblEntry": pduAccessIpSettingTblEntry,
       "pduAccessIpSettingTblIndex": pduAccessIpSettingTblIndex,
       "pduAccessIpSettingTblAddr": pduAccessIpSettingTblAddr,
       "pduAccessIpSettingTblPrefix": pduAccessIpSettingTblPrefix,
       "pduAccessIpSettingTblAction": pduAccessIpSettingTblAction,
       "pduSecurity": pduSecurity,
       "pduSecurityNetAccessProtectEn": pduSecurityNetAccessProtectEn,
       "pduSecuritySshEn": pduSecuritySshEn,
       "pduSecuritySshInterval": pduSecuritySshInterval,
       "pduSecuritySshTime": pduSecuritySshTime,
       "pduSecuritySshBlock": pduSecuritySshBlock,
       "pduSecuritySnmpv3En": pduSecuritySnmpv3En,
       "pduSecuritySnmpv3Interval": pduSecuritySnmpv3Interval,
       "pduSecuritySnmpv3Time": pduSecuritySnmpv3Time,
       "pduSecuritySnmpv3Block": pduSecuritySnmpv3Block,
       "pduSecurityHttpEn": pduSecurityHttpEn,
       "pduSecurityHttpInterval": pduSecurityHttpInterval,
       "pduSecurityHttpTime": pduSecurityHttpTime,
       "pduSecurityHttpBlock": pduSecurityHttpBlock,
       "pduNetService": pduNetService,
       "pduNetServiceSsh": pduNetServiceSsh,
       "pduNetServiceSshEn": pduNetServiceSshEn,
       "pduNetServiceSshPort": pduNetServiceSshPort,
       "pduNetServiceSsl": pduNetServiceSsl,
       "pduNetServiceSslEn": pduNetServiceSslEn,
       "pduNetServiceSslPort": pduNetServiceSslPort,
       "pduNetServiceSslForce": pduNetServiceSslForce,
       "pduNetServicePing": pduNetServicePing,
       "pduNetServicePingEn": pduNetServicePingEn,
       "pduNetServiceModbus": pduNetServiceModbus,
       "pduNetServiceModbusEn": pduNetServiceModbusEn,
       "pduNetServiceModbusPort": pduNetServiceModbusPort,
       "pduNetServiceRadius": pduNetServiceRadius,
       "pduNetServiceRadiusEn": pduNetServiceRadiusEn,
       "pduNetServiceRadiusIp": pduNetServiceRadiusIp,
       "pduNetServiceRadiusPort": pduNetServiceRadiusPort,
       "pduNetServiceRadiusSecKey": pduNetServiceRadiusSecKey,
       "pduNetServiceRadiusTimeout": pduNetServiceRadiusTimeout,
       "pduNetServiceRadiusRetry": pduNetServiceRadiusRetry,
       "pduSnmpSetting": pduSnmpSetting,
       "pduSnmpSettingAgent": pduSnmpSettingAgent,
       "pduSnmpSettingAgentEn": pduSnmpSettingAgentEn,
       "pduSnmpSettingAgentPort": pduSnmpSettingAgentPort,
       "pduSnmpSettingAgentComRead": pduSnmpSettingAgentComRead,
       "pduSnmpSettingAgentComWrite": pduSnmpSettingAgentComWrite,
       "pduSnmpSettingv3Usm": pduSnmpSettingv3Usm,
       "pduSnmpSettingv3UsmUserName": pduSnmpSettingv3UsmUserName,
       "pduSnmpSettingv3UsmAuthPasswd": pduSnmpSettingv3UsmAuthPasswd,
       "pduSnmpSettingv3UsmAuthMode": pduSnmpSettingv3UsmAuthMode,
       "pduSnmpSettingv3UsmPrivPasswd": pduSnmpSettingv3UsmPrivPasswd,
       "pduSnmpSettingv3UsmPrivMode": pduSnmpSettingv3UsmPrivMode,
       "pduSnmpSettingv3UsmSecurityLevel": pduSnmpSettingv3UsmSecurityLevel,
       "pduSnmpSettingTrap": pduSnmpSettingTrap,
       "pduSnmpSettingTrapTable": pduSnmpSettingTrapTable,
       "pduSnmpSettingTrapEntry": pduSnmpSettingTrapEntry,
       "pduSnmpSettingTrapIndex": pduSnmpSettingTrapIndex,
       "pduSnmpSettingTrapRcvrAddress": pduSnmpSettingTrapRcvrAddress,
       "pduSnmpSettingTrapEvtLevel": pduSnmpSettingTrapEvtLevel,
       "pduSnmpSettingTrapVer": pduSnmpSettingTrapVer,
       "pduSnmpSettingTrapDesc": pduSnmpSettingTrapDesc,
       "pduEmailSetting": pduEmailSetting,
       "pduEmailSettingSmtp": pduEmailSettingSmtp,
       "pduEmailSettingSmtpIp": pduEmailSettingSmtpIp,
       "pduEmailSettingSmtpPort": pduEmailSettingSmtpPort,
       "pduEmailSettingSmtpSender": pduEmailSettingSmtpSender,
       "pduEmailSettingSmtpSubject": pduEmailSettingSmtpSubject,
       "pduEmailSettingSmtpAuthEn": pduEmailSettingSmtpAuthEn,
       "pduEmailSettingSmtpAuthUser": pduEmailSettingSmtpAuthUser,
       "pduEmailSettingSmtpAuthPasswd": pduEmailSettingSmtpAuthPasswd,
       "pduEmailSettingNotify": pduEmailSettingNotify,
       "pduEmailSettingNotifyTable": pduEmailSettingNotifyTable,
       "pduEmailSettingNotifyEntry": pduEmailSettingNotifyEntry,
       "pduEmailSettingNotifyIndex": pduEmailSettingNotifyIndex,
       "pduEmailSettingNotifyRecvAddr": pduEmailSettingNotifyRecvAddr,
       "pduEmailSettingNotifyType": pduEmailSettingNotifyType,
       "pduEmailSettingNotifyEvtLev": pduEmailSettingNotifyEvtLev,
       "pduEmailSettingNotifyDesc": pduEmailSettingNotifyDesc,
       "pduUserSetting": pduUserSetting,
       "pduUserSettingLocal": pduUserSettingLocal,
       "pduUserSettingLocalTable": pduUserSettingLocalTable,
       "pduUserSettingLocalEntry": pduUserSettingLocalEntry,
       "pduUserSettingLocalIndex": pduUserSettingLocalIndex,
       "pduUserSettingLocalUserName": pduUserSettingLocalUserName,
       "pduUserSettingLocalPasswd": pduUserSettingLocalPasswd,
       "pduUserSettingLocalPrivilege": pduUserSettingLocalPrivilege,
       "pduUserSettingRadius": pduUserSettingRadius,
       "pduUserSettingRadiusTable": pduUserSettingRadiusTable,
       "pduUserSettingRadiusEntry": pduUserSettingRadiusEntry,
       "pduUserSettingRadiusIndex": pduUserSettingRadiusIndex,
       "pduUserSettingRadiusUserName": pduUserSettingRadiusUserName,
       "pduUserSettingRadiusPrivilege": pduUserSettingRadiusPrivilege,
       "pduUserSettingAuthCfg": pduUserSettingAuthCfg,
       "pduUserSettingAuthCfgAdminName": pduUserSettingAuthCfgAdminName,
       "pduUserSettingAuthCfgAdminPasswd": pduUserSettingAuthCfgAdminPasswd,
       "pduAdvanced": pduAdvanced,
       "pduSyslogSetting": pduSyslogSetting,
       "pduSysEvtLog": pduSysEvtLog,
       "pduSysEvtLogEn": pduSysEvtLogEn,
       "pduSysEvtLogIp": pduSysEvtLogIp,
       "pduSysEvtLogPort": pduSysEvtLogPort,
       "pduHisLog": pduHisLog,
       "pduHisLogEn": pduHisLogEn,
       "pduHisLogIp": pduHisLogIp,
       "pduHisLogPort": pduHisLogPort,
       "pduLinksSetting": pduLinksSetting,
       "pduLinksSettingTable": pduLinksSettingTable,
       "pduLinksSettingEntry": pduLinksSettingEntry,
       "pduLinksSettingIndex": pduLinksSettingIndex,
       "pduLinksSettingScreenText": pduLinksSettingScreenText,
       "pduLinksSettingAddress": pduLinksSettingAddress,
       "pduLinksSettingStatus": pduLinksSettingStatus,
       "pduTraps": pduTraps,
       "pduSysColdBoot": pduSysColdBoot,
       "pduSysWarmBoot": pduSysWarmBoot,
       "pduSysEMDRestore": pduSysEMDRestore,
       "pduSysEMDLost": pduSysEMDLost,
       "pduSysInletRestore": pduSysInletRestore,
       "pduSysInletLost": pduSysInletLost,
       "pduInletLoadWarn": pduInletLoadWarn,
       "pduInletLoadWarnToNormal": pduInletLoadWarnToNormal,
       "pduInletLoadCritical": pduInletLoadCritical,
       "pduInletLoadCritToWarn": pduInletLoadCritToWarn,
       "pduInletLoadBalanceWarn": pduInletLoadBalanceWarn,
       "pduInletLoadBalanceWarnToNormal": pduInletLoadBalanceWarnToNormal,
       "pduInletLoadBalanceCritical": pduInletLoadBalanceCritical,
       "pduInletLoadBalanceCritToWarn": pduInletLoadBalanceCritToWarn,
       "pduInletCurrPhase1CB1Warn": pduInletCurrPhase1CB1Warn,
       "pduInletCurrPhase1CB1WarnToNormal": pduInletCurrPhase1CB1WarnToNormal,
       "pduInletCurrPhase1CB1Critical": pduInletCurrPhase1CB1Critical,
       "pduInletCurrPhase1CB1CritToWarn": pduInletCurrPhase1CB1CritToWarn,
       "pduInletCurrPhase2CB1Warn": pduInletCurrPhase2CB1Warn,
       "pduInletCurrPhase2CB1WarnToNormal": pduInletCurrPhase2CB1WarnToNormal,
       "pduInletCurrPhase2CB1Critical": pduInletCurrPhase2CB1Critical,
       "pduInletCurrPhase2CB1CritToWarn": pduInletCurrPhase2CB1CritToWarn,
       "pduInletCurrPhase3CB1Warn": pduInletCurrPhase3CB1Warn,
       "pduInletCurrPhase3CB1WarnToNormal": pduInletCurrPhase3CB1WarnToNormal,
       "pduInletCurrPhase3CB1Critical": pduInletCurrPhase3CB1Critical,
       "pduInletCurrPhase3CB1CritToWarn": pduInletCurrPhase3CB1CritToWarn,
       "pduInletTotalCurrPhase1Warn": pduInletTotalCurrPhase1Warn,
       "pduInletTotalCurrPhase1WarnToNormal": pduInletTotalCurrPhase1WarnToNormal,
       "pduInletTotalCurrPhase1Critical": pduInletTotalCurrPhase1Critical,
       "pduInletTotalCurrPhase1CritToWarn": pduInletTotalCurrPhase1CritToWarn,
       "pduInletTotalCurrPhase2Warn": pduInletTotalCurrPhase2Warn,
       "pduInletTotalCurrPhase2WarnToNormal": pduInletTotalCurrPhase2WarnToNormal,
       "pduInletTotalCurrPhase2Critical": pduInletTotalCurrPhase2Critical,
       "pduInletTotalCurrPhase2CritToWarn": pduInletTotalCurrPhase2CritToWarn,
       "pduInletTotalCurrPhase3Warn": pduInletTotalCurrPhase3Warn,
       "pduInletTotalCurrPhase3WarnToNprmal": pduInletTotalCurrPhase3WarnToNprmal,
       "pduInletTotalCurrPhase3Critical": pduInletTotalCurrPhase3Critical,
       "pduInletTotalCurrPhase3CritToWarn": pduInletTotalCurrPhase3CritToWarn,
       "pduInletVoltPhase1Warn": pduInletVoltPhase1Warn,
       "pduInletVoltPhase1WarnToNormal": pduInletVoltPhase1WarnToNormal,
       "pduInletVoltPhase1Critical": pduInletVoltPhase1Critical,
       "pduInletVoltPhase1CritToWarn": pduInletVoltPhase1CritToWarn,
       "pduInletVoltPhase2Warn": pduInletVoltPhase2Warn,
       "pduInletVoltPhase2WarnToNormal": pduInletVoltPhase2WarnToNormal,
       "pduInletVoltPhase2Critical": pduInletVoltPhase2Critical,
       "pduInletVoltPhase2CritToWarn": pduInletVoltPhase2CritToWarn,
       "pduInletVoltPhase3Warn": pduInletVoltPhase3Warn,
       "pduInletVoltPhase3WarnToNormal": pduInletVoltPhase3WarnToNormal,
       "pduInletVoltPhase3Critical": pduInletVoltPhase3Critical,
       "pduInletVoltPhase3CritToWarn": pduInletVoltPhase3CritToWarn,
       "pduEmdTempOverHighWarn": pduEmdTempOverHighWarn,
       "pduEmdTempNotOverHighWarn": pduEmdTempNotOverHighWarn,
       "pduEmdTempOverHighCrit": pduEmdTempOverHighCrit,
       "pduEmdTempNotOverHighCrit": pduEmdTempNotOverHighCrit,
       "pduEmdTempUnderLowWarn": pduEmdTempUnderLowWarn,
       "pduEmdTempNotUnderLowWarn": pduEmdTempNotUnderLowWarn,
       "pduEmdTempUnderLowCrit": pduEmdTempUnderLowCrit,
       "pduEmdTempNotUnderLowCrit": pduEmdTempNotUnderLowCrit,
       "pduEmdHumiOverHighWarn": pduEmdHumiOverHighWarn,
       "pduEmdHumiNotOverHighWarn": pduEmdHumiNotOverHighWarn,
       "pduEmdHumiOverHighCrit": pduEmdHumiOverHighCrit,
       "pduEmdHumiNotOverHighCrit": pduEmdHumiNotOverHighCrit,
       "pduEmdHumiUnderLowWarn": pduEmdHumiUnderLowWarn,
       "pduEmdHumiNotUnderLowWarn": pduEmdHumiNotUnderLowWarn,
       "pduEmdHumiUnderLowCrit": pduEmdHumiUnderLowCrit,
       "pduEmdHumiNotUnderLowCrit": pduEmdHumiNotUnderLowCrit,
       "pduAlarm1Triggered": pduAlarm1Triggered,
       "pduAlarm1Normal": pduAlarm1Normal,
       "pduAlarm2Triggered": pduAlarm2Triggered,
       "pduAlarm2Normal": pduAlarm2Normal,
       "pduInletCurrPhase1CB2Warn": pduInletCurrPhase1CB2Warn,
       "pduInletCurrPhase1CB2WarnToNormal": pduInletCurrPhase1CB2WarnToNormal,
       "pduInletCurrPhase1CB2Critical": pduInletCurrPhase1CB2Critical,
       "pduInletCurrPhase1CB2CritToWarn": pduInletCurrPhase1CB2CritToWarn,
       "pduInletCurrPhase2CB2Warn": pduInletCurrPhase2CB2Warn,
       "pduInletCurrPhase2CB2WarnToNormal": pduInletCurrPhase2CB2WarnToNormal,
       "pduInletCurrPhase2CB2Critical": pduInletCurrPhase2CB2Critical,
       "pduInletCurrPhase2CB2CritToWarn": pduInletCurrPhase2CB2CritToWarn,
       "pduInletCurrPhase3CB2Warn": pduInletCurrPhase3CB2Warn,
       "pduInletCurrPhase3CB2WarnToNormal": pduInletCurrPhase3CB2WarnToNormal,
       "pduInletCurrPhase3CB2Critical": pduInletCurrPhase3CB2Critical,
       "pduInletCurrPhase3CB2CritToWarn": pduInletCurrPhase3CB2CritToWarn}
)
