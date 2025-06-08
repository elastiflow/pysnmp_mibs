# SNMP MIB module (RUIJIE-LTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-LTE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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


# MODULE-IDENTITY

ruijieLteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148)
)
if mibBuilder.loadTexts:
    ruijieLteMIB.setRevisions(
        ("2010-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LteEnbSystemInfoConfigObjects_ObjectIdentity = ObjectIdentity
lteEnbSystemInfoConfigObjects = _LteEnbSystemInfoConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1)
)
_LteEnbGeneralInfoConfigTable_Object = MibTable
lteEnbGeneralInfoConfigTable = _LteEnbGeneralInfoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1)
)
if mibBuilder.loadTexts:
    lteEnbGeneralInfoConfigTable.setStatus("current")
_LteEnbGeneralInfoConfigEntry_Object = MibTableRow
lteEnbGeneralInfoConfigEntry = _LteEnbGeneralInfoConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1)
)
lteEnbGeneralInfoConfigEntry.setIndexNames(
    (0, "RUIJIE-LTE-MIB", "lteEnbMacAddr"),
)
if mibBuilder.loadTexts:
    lteEnbGeneralInfoConfigEntry.setStatus("current")
_LteEnbMacAddr_Type = MacAddress
_LteEnbMacAddr_Object = MibTableColumn
lteEnbMacAddr = _LteEnbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 1),
    _LteEnbMacAddr_Type()
)
lteEnbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteEnbMacAddr.setStatus("current")
_LteEnbName_Type = DisplayString
_LteEnbName_Object = MibTableColumn
lteEnbName = _LteEnbName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 2),
    _LteEnbName_Type()
)
lteEnbName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbName.setStatus("current")


class _LteEnbDLBandWidth_Type(Integer32):
    """Custom type lteEnbDLBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(25,
              50,
              75,
              100)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth-5M", 25),
          ("bandwidth-10M", 50),
          ("bandwidth-15M", 75),
          ("bandwidth-20M", 100))
    )


_LteEnbDLBandWidth_Type.__name__ = "Integer32"
_LteEnbDLBandWidth_Object = MibTableColumn
lteEnbDLBandWidth = _LteEnbDLBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 3),
    _LteEnbDLBandWidth_Type()
)
lteEnbDLBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbDLBandWidth.setStatus("current")


class _LteEnbMCC_Type(Integer32):
    """Custom type lteEnbMCC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_LteEnbMCC_Type.__name__ = "Integer32"
_LteEnbMCC_Object = MibTableColumn
lteEnbMCC = _LteEnbMCC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 4),
    _LteEnbMCC_Type()
)
lteEnbMCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMCC.setStatus("current")


class _LteEnbMNC_Type(Integer32):
    """Custom type lteEnbMNC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_LteEnbMNC_Type.__name__ = "Integer32"
_LteEnbMNC_Object = MibTableColumn
lteEnbMNC = _LteEnbMNC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 5),
    _LteEnbMNC_Type()
)
lteEnbMNC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMNC.setStatus("current")
_LteEnbTac_Type = Integer32
_LteEnbTac_Object = MibTableColumn
lteEnbTac = _LteEnbTac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 6),
    _LteEnbTac_Type()
)
lteEnbTac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbTac.setStatus("current")


class _LteEnbFrameType_Type(Integer32):
    """Custom type lteEnbFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fdd", 0),
          ("tdd", 1))
    )


_LteEnbFrameType_Type.__name__ = "Integer32"
_LteEnbFrameType_Object = MibTableColumn
lteEnbFrameType = _LteEnbFrameType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 7),
    _LteEnbFrameType_Type()
)
lteEnbFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbFrameType.setStatus("current")


class _LteEnbTddConfig_Type(Integer32):
    """Custom type lteEnbTddConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LteEnbTddConfig_Type.__name__ = "Integer32"
_LteEnbTddConfig_Object = MibTableColumn
lteEnbTddConfig = _LteEnbTddConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 8),
    _LteEnbTddConfig_Type()
)
lteEnbTddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbTddConfig.setStatus("current")


class _LteEnbTddConfigS_Type(Integer32):
    """Custom type lteEnbTddConfigS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LteEnbTddConfigS_Type.__name__ = "Integer32"
_LteEnbTddConfigS_Object = MibTableColumn
lteEnbTddConfigS = _LteEnbTddConfigS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 9),
    _LteEnbTddConfigS_Type()
)
lteEnbTddConfigS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbTddConfigS.setStatus("current")
_LteEnbPrefixType_Type = Integer32
_LteEnbPrefixType_Object = MibTableColumn
lteEnbPrefixType = _LteEnbPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 10),
    _LteEnbPrefixType_Type()
)
lteEnbPrefixType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbPrefixType.setStatus("current")
_LteEnbFreqBandIndicator_Type = Integer32
_LteEnbFreqBandIndicator_Object = MibTableColumn
lteEnbFreqBandIndicator = _LteEnbFreqBandIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 11),
    _LteEnbFreqBandIndicator_Type()
)
lteEnbFreqBandIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbFreqBandIndicator.setStatus("current")
_LteEnbDownlinkFrequency_Type = Integer32
_LteEnbDownlinkFrequency_Object = MibTableColumn
lteEnbDownlinkFrequency = _LteEnbDownlinkFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 12),
    _LteEnbDownlinkFrequency_Type()
)
lteEnbDownlinkFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbDownlinkFrequency.setStatus("current")
_LteEnbUplinkFrequencyOffset_Type = Integer32
_LteEnbUplinkFrequencyOffset_Object = MibTableColumn
lteEnbUplinkFrequencyOffset = _LteEnbUplinkFrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 13),
    _LteEnbUplinkFrequencyOffset_Type()
)
lteEnbUplinkFrequencyOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbUplinkFrequencyOffset.setStatus("current")


class _LteEnbTxmode_Type(Integer32):
    """Custom type lteEnbTxmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_LteEnbTxmode_Type.__name__ = "Integer32"
_LteEnbTxmode_Object = MibTableColumn
lteEnbTxmode = _LteEnbTxmode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 14),
    _LteEnbTxmode_Type()
)
lteEnbTxmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbTxmode.setStatus("current")
_LteEnbNidCell_Type = Integer32
_LteEnbNidCell_Object = MibTableColumn
lteEnbNidCell = _LteEnbNidCell_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 15),
    _LteEnbNidCell_Type()
)
lteEnbNidCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbNidCell.setStatus("current")
_LteEnbRsPower_Type = Integer32
_LteEnbRsPower_Object = MibTableColumn
lteEnbRsPower = _LteEnbRsPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 16),
    _LteEnbRsPower_Type()
)
lteEnbRsPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbRsPower.setStatus("current")
_LteEnbReset_Type = Integer32
_LteEnbReset_Object = MibTableColumn
lteEnbReset = _LteEnbReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 17),
    _LteEnbReset_Type()
)
lteEnbReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbReset.setStatus("current")
_LteEnbTxpower_Type = Integer32
_LteEnbTxpower_Object = MibTableColumn
lteEnbTxpower = _LteEnbTxpower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 18),
    _LteEnbTxpower_Type()
)
lteEnbTxpower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbTxpower.setStatus("current")
_LteEnbqRxLvlmin_Type = Integer32
_LteEnbqRxLvlmin_Object = MibTableColumn
lteEnbqRxLvlmin = _LteEnbqRxLvlmin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 19),
    _LteEnbqRxLvlmin_Type()
)
lteEnbqRxLvlmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbqRxLvlmin.setStatus("current")
_LteEnbPdschRsPower_Type = Integer32
_LteEnbPdschRsPower_Object = MibTableColumn
lteEnbPdschRsPower = _LteEnbPdschRsPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 20),
    _LteEnbPdschRsPower_Type()
)
lteEnbPdschRsPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbPdschRsPower.setStatus("current")
_LteEnbPuschP0Nominal_Type = Integer32
_LteEnbPuschP0Nominal_Object = MibTableColumn
lteEnbPuschP0Nominal = _LteEnbPuschP0Nominal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 21),
    _LteEnbPuschP0Nominal_Type()
)
lteEnbPuschP0Nominal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbPuschP0Nominal.setStatus("current")
_LteEnbPuschAlpha_Type = Integer32
_LteEnbPuschAlpha_Object = MibTableColumn
lteEnbPuschAlpha = _LteEnbPuschAlpha_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 22),
    _LteEnbPuschAlpha_Type()
)
lteEnbPuschAlpha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbPuschAlpha.setStatus("current")
_LteEnbPucchP0Nominal_Type = Integer32
_LteEnbPucchP0Nominal_Object = MibTableColumn
lteEnbPucchP0Nominal = _LteEnbPucchP0Nominal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 23),
    _LteEnbPucchP0Nominal_Type()
)
lteEnbPucchP0Nominal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbPucchP0Nominal.setStatus("current")
_LteEnbDtchTimer_Type = Integer32
_LteEnbDtchTimer_Object = MibTableColumn
lteEnbDtchTimer = _LteEnbDtchTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 24),
    _LteEnbDtchTimer_Type()
)
lteEnbDtchTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbDtchTimer.setStatus("current")


class _LteEnbLB_Type(Integer32):
    """Custom type lteEnbLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LteEnbLB_Type.__name__ = "Integer32"
_LteEnbLB_Object = MibTableColumn
lteEnbLB = _LteEnbLB_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 25),
    _LteEnbLB_Type()
)
lteEnbLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbLB.setStatus("current")


class _LteEnbICIC_Type(Integer32):
    """Custom type lteEnbICIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LteEnbICIC_Type.__name__ = "Integer32"
_LteEnbICIC_Object = MibTableColumn
lteEnbICIC = _LteEnbICIC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 26),
    _LteEnbICIC_Type()
)
lteEnbICIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbICIC.setStatus("current")
_LteEnbEdgeRbStart_Type = Integer32
_LteEnbEdgeRbStart_Object = MibTableColumn
lteEnbEdgeRbStart = _LteEnbEdgeRbStart_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 27),
    _LteEnbEdgeRbStart_Type()
)
lteEnbEdgeRbStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbEdgeRbStart.setStatus("current")
_LteEnbEdgeRbEnd_Type = Integer32
_LteEnbEdgeRbEnd_Object = MibTableColumn
lteEnbEdgeRbEnd = _LteEnbEdgeRbEnd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 28),
    _LteEnbEdgeRbEnd_Type()
)
lteEnbEdgeRbEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbEdgeRbEnd.setStatus("current")
_LteEnbEdgeRsrpThold_Type = Integer32
_LteEnbEdgeRsrpThold_Object = MibTableColumn
lteEnbEdgeRsrpThold = _LteEnbEdgeRsrpThold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 29),
    _LteEnbEdgeRsrpThold_Type()
)
lteEnbEdgeRsrpThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbEdgeRsrpThold.setStatus("current")
_LteEnbEdgeDifThold_Type = Integer32
_LteEnbEdgeDifThold_Object = MibTableColumn
lteEnbEdgeDifThold = _LteEnbEdgeDifThold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 30),
    _LteEnbEdgeDifThold_Type()
)
lteEnbEdgeDifThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbEdgeDifThold.setStatus("current")


class _LteEnbMeas_Type(Integer32):
    """Custom type lteEnbMeas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LteEnbMeas_Type.__name__ = "Integer32"
_LteEnbMeas_Object = MibTableColumn
lteEnbMeas = _LteEnbMeas_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 31),
    _LteEnbMeas_Type()
)
lteEnbMeas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMeas.setStatus("current")


class _LteEnbMeasGap_Type(Integer32):
    """Custom type lteEnbMeasGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LteEnbMeasGap_Type.__name__ = "Integer32"
_LteEnbMeasGap_Object = MibTableColumn
lteEnbMeasGap = _LteEnbMeasGap_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 32),
    _LteEnbMeasGap_Type()
)
lteEnbMeasGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMeasGap.setStatus("current")
_LteEnbMeasCarrfreq1_Type = Integer32
_LteEnbMeasCarrfreq1_Object = MibTableColumn
lteEnbMeasCarrfreq1 = _LteEnbMeasCarrfreq1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 33),
    _LteEnbMeasCarrfreq1_Type()
)
lteEnbMeasCarrfreq1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMeasCarrfreq1.setStatus("current")
_LteEnbMeasCarrfreq2_Type = Integer32
_LteEnbMeasCarrfreq2_Object = MibTableColumn
lteEnbMeasCarrfreq2 = _LteEnbMeasCarrfreq2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 34),
    _LteEnbMeasCarrfreq2_Type()
)
lteEnbMeasCarrfreq2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMeasCarrfreq2.setStatus("current")
_LteEnbMeasA1Thold_Type = Integer32
_LteEnbMeasA1Thold_Object = MibTableColumn
lteEnbMeasA1Thold = _LteEnbMeasA1Thold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 35),
    _LteEnbMeasA1Thold_Type()
)
lteEnbMeasA1Thold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMeasA1Thold.setStatus("current")
_LteEnbMeasA2Thold_Type = Integer32
_LteEnbMeasA2Thold_Object = MibTableColumn
lteEnbMeasA2Thold = _LteEnbMeasA2Thold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 36),
    _LteEnbMeasA2Thold_Type()
)
lteEnbMeasA2Thold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMeasA2Thold.setStatus("current")
_LteEnbMeasA3Offset_Type = Integer32
_LteEnbMeasA3Offset_Object = MibTableColumn
lteEnbMeasA3Offset = _LteEnbMeasA3Offset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 37),
    _LteEnbMeasA3Offset_Type()
)
lteEnbMeasA3Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMeasA3Offset.setStatus("current")
_LteEnbMeasA3Hys_Type = Integer32
_LteEnbMeasA3Hys_Object = MibTableColumn
lteEnbMeasA3Hys = _LteEnbMeasA3Hys_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 38),
    _LteEnbMeasA3Hys_Type()
)
lteEnbMeasA3Hys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMeasA3Hys.setStatus("current")


class _LteEnbMeasA3TimeTrig_Type(Integer32):
    """Custom type lteEnbMeasA3TimeTrig based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ms0", 0),
          ("ms40", 1),
          ("ms64", 2),
          ("ms80", 3),
          ("ms100", 4),
          ("ms128", 5),
          ("ms160", 6),
          ("ms256", 7),
          ("ms320", 8),
          ("ms480", 9),
          ("ms512", 10),
          ("ms640", 11),
          ("ms1024", 12),
          ("ms1280", 13),
          ("ms2560", 14),
          ("ms5120", 15))
    )


_LteEnbMeasA3TimeTrig_Type.__name__ = "Integer32"
_LteEnbMeasA3TimeTrig_Object = MibTableColumn
lteEnbMeasA3TimeTrig = _LteEnbMeasA3TimeTrig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 39),
    _LteEnbMeasA3TimeTrig_Type()
)
lteEnbMeasA3TimeTrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMeasA3TimeTrig.setStatus("current")


class _LteEnbMeasA3RpIntval_Type(Integer32):
    """Custom type lteEnbMeasA3RpIntval based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ms120", 0),
          ("ms240", 1),
          ("ms480", 2),
          ("ms640", 3),
          ("ms1024", 4),
          ("ms2048", 5),
          ("ms5120", 6),
          ("ms10240", 7),
          ("min1", 8),
          ("min6", 9),
          ("min12", 10),
          ("min30", 11),
          ("min60", 12),
          ("spare3", 13),
          ("spare2", 14),
          ("spare1", 15))
    )


_LteEnbMeasA3RpIntval_Type.__name__ = "Integer32"
_LteEnbMeasA3RpIntval_Object = MibTableColumn
lteEnbMeasA3RpIntval = _LteEnbMeasA3RpIntval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 40),
    _LteEnbMeasA3RpIntval_Type()
)
lteEnbMeasA3RpIntval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbMeasA3RpIntval.setStatus("current")
_LteEnbID_Type = Integer32
_LteEnbID_Object = MibTableColumn
lteEnbID = _LteEnbID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 1, 1, 1, 41),
    _LteEnbID_Type()
)
lteEnbID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEnbID.setStatus("current")
_LteUEInfoGetObjects_ObjectIdentity = ObjectIdentity
lteUEInfoGetObjects = _LteUEInfoGetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2)
)
_LteUEInfoGetTable_Object = MibTable
lteUEInfoGetTable = _LteUEInfoGetTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1)
)
if mibBuilder.loadTexts:
    lteUEInfoGetTable.setStatus("current")
_LteUEInfoGetEntry_Object = MibTableRow
lteUEInfoGetEntry = _LteUEInfoGetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1)
)
lteUEInfoGetEntry.setIndexNames(
    (0, "RUIJIE-LTE-MIB", "lteUEImsi"),
)
if mibBuilder.loadTexts:
    lteUEInfoGetEntry.setStatus("current")
_LteUEImsi_Type = DisplayString
_LteUEImsi_Object = MibTableColumn
lteUEImsi = _LteUEImsi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 1),
    _LteUEImsi_Type()
)
lteUEImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUEImsi.setStatus("current")
_LteUEIpaddr_Type = IpAddress
_LteUEIpaddr_Object = MibTableColumn
lteUEIpaddr = _LteUEIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 2),
    _LteUEIpaddr_Type()
)
lteUEIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteUEIpaddr.setStatus("current")
_LteUEGuti_Type = DisplayString
_LteUEGuti_Object = MibTableColumn
lteUEGuti = _LteUEGuti_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 3),
    _LteUEGuti_Type()
)
lteUEGuti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUEGuti.setStatus("current")
_LteUEUptime_Type = TimeTicks
_LteUEUptime_Object = MibTableColumn
lteUEUptime = _LteUEUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 4),
    _LteUEUptime_Type()
)
lteUEUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUEUptime.setStatus("current")
_LteUERxpkt_Type = Counter64
_LteUERxpkt_Object = MibTableColumn
lteUERxpkt = _LteUERxpkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 5),
    _LteUERxpkt_Type()
)
lteUERxpkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUERxpkt.setStatus("current")
_LteUETxpkt_Type = Counter64
_LteUETxpkt_Object = MibTableColumn
lteUETxpkt = _LteUETxpkt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 6),
    _LteUETxpkt_Type()
)
lteUETxpkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUETxpkt.setStatus("current")
_LteUECellId_Type = Integer32
_LteUECellId_Object = MibTableColumn
lteUECellId = _LteUECellId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 7),
    _LteUECellId_Type()
)
lteUECellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUECellId.setStatus("current")
_LteUEIsAttached_Type = Integer32
_LteUEIsAttached_Object = MibTableColumn
lteUEIsAttached = _LteUEIsAttached_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 8),
    _LteUEIsAttached_Type()
)
lteUEIsAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUEIsAttached.setStatus("current")
_LteUECapbility_Type = Integer32
_LteUECapbility_Object = MibTableColumn
lteUECapbility = _LteUECapbility_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 9),
    _LteUECapbility_Type()
)
lteUECapbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUECapbility.setStatus("current")
_LteUEAssoEnbMac_Type = MacAddress
_LteUEAssoEnbMac_Object = MibTableColumn
lteUEAssoEnbMac = _LteUEAssoEnbMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 10),
    _LteUEAssoEnbMac_Type()
)
lteUEAssoEnbMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUEAssoEnbMac.setStatus("current")


class _LteUERrcState_Type(Integer32):
    """Custom type lteUERrcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dis-connected", 0),
          ("connected", 1))
    )


_LteUERrcState_Type.__name__ = "Integer32"
_LteUERrcState_Object = MibTableColumn
lteUERrcState = _LteUERrcState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 11),
    _LteUERrcState_Type()
)
lteUERrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUERrcState.setStatus("current")
_LteUERxbytes_Type = Counter64
_LteUERxbytes_Object = MibTableColumn
lteUERxbytes = _LteUERxbytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 12),
    _LteUERxbytes_Type()
)
lteUERxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUERxbytes.setStatus("current")
_LteUETxbytes_Type = Counter64
_LteUETxbytes_Object = MibTableColumn
lteUETxbytes = _LteUETxbytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 2, 1, 1, 13),
    _LteUETxbytes_Type()
)
lteUETxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteUETxbytes.setStatus("current")
_LteEnbInfoGetObjects_ObjectIdentity = ObjectIdentity
lteEnbInfoGetObjects = _LteEnbInfoGetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 3)
)
_LteEnbInfoGetTable_Object = MibTable
lteEnbInfoGetTable = _LteEnbInfoGetTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 3, 1)
)
if mibBuilder.loadTexts:
    lteEnbInfoGetTable.setStatus("current")
_LteEnbInfoGetEntry_Object = MibTableRow
lteEnbInfoGetEntry = _LteEnbInfoGetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 3, 1, 1)
)
lteEnbInfoGetEntry.setIndexNames(
    (0, "RUIJIE-LTE-MIB", "lteEnbMacAddr"),
)
if mibBuilder.loadTexts:
    lteEnbInfoGetEntry.setStatus("current")
_LteEnbNameInfo_Type = DisplayString
_LteEnbNameInfo_Object = MibTableColumn
lteEnbNameInfo = _LteEnbNameInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 3, 1, 1, 1),
    _LteEnbNameInfo_Type()
)
lteEnbNameInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteEnbNameInfo.setStatus("current")
_LteEnbFreqBandNumber_Type = Integer32
_LteEnbFreqBandNumber_Object = MibTableColumn
lteEnbFreqBandNumber = _LteEnbFreqBandNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 3, 1, 1, 2),
    _LteEnbFreqBandNumber_Type()
)
lteEnbFreqBandNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteEnbFreqBandNumber.setStatus("current")
_LteEnbUENumber_Type = Integer32
_LteEnbUENumber_Object = MibTableColumn
lteEnbUENumber = _LteEnbUENumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 3, 1, 1, 3),
    _LteEnbUENumber_Type()
)
lteEnbUENumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lteEnbUENumber.setStatus("current")
_LteEpcStatusEntry_ObjectIdentity = ObjectIdentity
lteEpcStatusEntry = _LteEpcStatusEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 4)
)
_LteEpcAttachUENumber_Type = Integer32
_LteEpcAttachUENumber_Object = MibScalar
lteEpcAttachUENumber = _LteEpcAttachUENumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 4, 1),
    _LteEpcAttachUENumber_Type()
)
lteEpcAttachUENumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEpcAttachUENumber.setStatus("current")
_LteEpcConfigEntry_ObjectIdentity = ObjectIdentity
lteEpcConfigEntry = _LteEpcConfigEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 5)
)
_LteEpcEEA_Type = Integer32
_LteEpcEEA_Object = MibScalar
lteEpcEEA = _LteEpcEEA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 5, 1),
    _LteEpcEEA_Type()
)
lteEpcEEA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEpcEEA.setStatus("current")
_LteEpcEIA_Type = Integer32
_LteEpcEIA_Object = MibScalar
lteEpcEIA = _LteEpcEIA_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 5, 2),
    _LteEpcEIA_Type()
)
lteEpcEIA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEpcEIA.setStatus("current")
_LteEpcMMECode_Type = Integer32
_LteEpcMMECode_Object = MibScalar
lteEpcMMECode = _LteEpcMMECode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 5, 3),
    _LteEpcMMECode_Type()
)
lteEpcMMECode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEpcMMECode.setStatus("current")
_LteEpcMMEGid_Type = Integer32
_LteEpcMMEGid_Object = MibScalar
lteEpcMMEGid = _LteEpcMMEGid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 5, 4),
    _LteEpcMMEGid_Type()
)
lteEpcMMEGid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEpcMMEGid.setStatus("current")
_LteEpcMCC_Type = Integer32
_LteEpcMCC_Object = MibScalar
lteEpcMCC = _LteEpcMCC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 5, 5),
    _LteEpcMCC_Type()
)
lteEpcMCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEpcMCC.setStatus("current")
_LteEpcMNC_Type = Integer32
_LteEpcMNC_Object = MibScalar
lteEpcMNC = _LteEpcMNC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 5, 6),
    _LteEpcMNC_Type()
)
lteEpcMNC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEpcMNC.setStatus("current")
_LteEpcEnbKeepalivetimer_Type = Integer32
_LteEpcEnbKeepalivetimer_Object = MibScalar
lteEpcEnbKeepalivetimer = _LteEpcEnbKeepalivetimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 5, 7),
    _LteEpcEnbKeepalivetimer_Type()
)
lteEpcEnbKeepalivetimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEpcEnbKeepalivetimer.setStatus("current")
_LteEpcDNS_Type = IpAddress
_LteEpcDNS_Object = MibScalar
lteEpcDNS = _LteEpcDNS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 5, 8),
    _LteEpcDNS_Type()
)
lteEpcDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lteEpcDNS.setStatus("current")
_LteUEIMSIMapIpObjects_ObjectIdentity = ObjectIdentity
lteUEIMSIMapIpObjects = _LteUEIMSIMapIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 6)
)
_LteUEIMSIMapIpTable_Object = MibTable
lteUEIMSIMapIpTable = _LteUEIMSIMapIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 6, 1)
)
if mibBuilder.loadTexts:
    lteUEIMSIMapIpTable.setStatus("current")
_LteUEIMSIMapIpEntry_Object = MibTableRow
lteUEIMSIMapIpEntry = _LteUEIMSIMapIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 6, 1, 1)
)
lteUEIMSIMapIpEntry.setIndexNames(
    (0, "RUIJIE-LTE-MIB", "lteUEIMSI"),
)
if mibBuilder.loadTexts:
    lteUEIMSIMapIpEntry.setStatus("current")
_LteUEIMSI_Type = DisplayString
_LteUEIMSI_Object = MibTableColumn
lteUEIMSI = _LteUEIMSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 6, 1, 1, 1),
    _LteUEIMSI_Type()
)
lteUEIMSI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lteUEIMSI.setStatus("current")
_LteUEIP_Type = IpAddress
_LteUEIP_Object = MibTableColumn
lteUEIP = _LteUEIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 6, 1, 1, 2),
    _LteUEIP_Type()
)
lteUEIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lteUEIP.setStatus("current")
_LteUERowStatus_Type = RowStatus
_LteUERowStatus_Object = MibTableColumn
lteUERowStatus = _LteUERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 6, 1, 1, 3),
    _LteUERowStatus_Type()
)
lteUERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lteUERowStatus.setStatus("current")
_LteRuijieAlarmTraps_ObjectIdentity = ObjectIdentity
lteRuijieAlarmTraps = _LteRuijieAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 7)
)
_LteRuijieAlarmTrapObjects_ObjectIdentity = ObjectIdentity
lteRuijieAlarmTrapObjects = _LteRuijieAlarmTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 8)
)
_ENodeBmac_Type = MacAddress
_ENodeBmac_Object = MibScalar
eNodeBmac = _ENodeBmac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 8, 1),
    _ENodeBmac_Type()
)
eNodeBmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNodeBmac.setStatus("current")
_ENodeBname_Type = DisplayString
_ENodeBname_Object = MibScalar
eNodeBname = _ENodeBname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 8, 2),
    _ENodeBname_Type()
)
eNodeBname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNodeBname.setStatus("current")
_UeIMSI_Type = DisplayString
_UeIMSI_Object = MibScalar
ueIMSI = _UeIMSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 8, 3),
    _UeIMSI_Type()
)
ueIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ueIMSI.setStatus("current")
_UeIpaddr_Type = IpAddress
_UeIpaddr_Object = MibScalar
ueIpaddr = _UeIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 8, 4),
    _UeIpaddr_Type()
)
ueIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ueIpaddr.setStatus("current")

# Managed Objects groups


# Notification objects

lteEnbOnlineTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 7, 1)
)
lteEnbOnlineTraps.setObjects(
      *(("RUIJIE-LTE-MIB", "eNodeBmac"),
        ("RUIJIE-LTE-MIB", "eNodeBname"))
)
if mibBuilder.loadTexts:
    lteEnbOnlineTraps.setStatus(
        "current"
    )

lteEnbOfflineTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 7, 2)
)
lteEnbOfflineTraps.setObjects(
      *(("RUIJIE-LTE-MIB", "eNodeBmac"),
        ("RUIJIE-LTE-MIB", "eNodeBname"))
)
if mibBuilder.loadTexts:
    lteEnbOfflineTraps.setStatus(
        "current"
    )

lteUEAttachedTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 7, 3)
)
lteUEAttachedTraps.setObjects(
      *(("RUIJIE-LTE-MIB", "ueIMSI"),
        ("RUIJIE-LTE-MIB", "ueIpaddr"))
)
if mibBuilder.loadTexts:
    lteUEAttachedTraps.setStatus(
        "current"
    )

lteUEDetachedTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 148, 7, 4)
)
lteUEDetachedTraps.setObjects(
      *(("RUIJIE-LTE-MIB", "ueIMSI"),
        ("RUIJIE-LTE-MIB", "ueIpaddr"))
)
if mibBuilder.loadTexts:
    lteUEDetachedTraps.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-LTE-MIB",
    **{"ruijieLteMIB": ruijieLteMIB,
       "lteEnbSystemInfoConfigObjects": lteEnbSystemInfoConfigObjects,
       "lteEnbGeneralInfoConfigTable": lteEnbGeneralInfoConfigTable,
       "lteEnbGeneralInfoConfigEntry": lteEnbGeneralInfoConfigEntry,
       "lteEnbMacAddr": lteEnbMacAddr,
       "lteEnbName": lteEnbName,
       "lteEnbDLBandWidth": lteEnbDLBandWidth,
       "lteEnbMCC": lteEnbMCC,
       "lteEnbMNC": lteEnbMNC,
       "lteEnbTac": lteEnbTac,
       "lteEnbFrameType": lteEnbFrameType,
       "lteEnbTddConfig": lteEnbTddConfig,
       "lteEnbTddConfigS": lteEnbTddConfigS,
       "lteEnbPrefixType": lteEnbPrefixType,
       "lteEnbFreqBandIndicator": lteEnbFreqBandIndicator,
       "lteEnbDownlinkFrequency": lteEnbDownlinkFrequency,
       "lteEnbUplinkFrequencyOffset": lteEnbUplinkFrequencyOffset,
       "lteEnbTxmode": lteEnbTxmode,
       "lteEnbNidCell": lteEnbNidCell,
       "lteEnbRsPower": lteEnbRsPower,
       "lteEnbReset": lteEnbReset,
       "lteEnbTxpower": lteEnbTxpower,
       "lteEnbqRxLvlmin": lteEnbqRxLvlmin,
       "lteEnbPdschRsPower": lteEnbPdschRsPower,
       "lteEnbPuschP0Nominal": lteEnbPuschP0Nominal,
       "lteEnbPuschAlpha": lteEnbPuschAlpha,
       "lteEnbPucchP0Nominal": lteEnbPucchP0Nominal,
       "lteEnbDtchTimer": lteEnbDtchTimer,
       "lteEnbLB": lteEnbLB,
       "lteEnbICIC": lteEnbICIC,
       "lteEnbEdgeRbStart": lteEnbEdgeRbStart,
       "lteEnbEdgeRbEnd": lteEnbEdgeRbEnd,
       "lteEnbEdgeRsrpThold": lteEnbEdgeRsrpThold,
       "lteEnbEdgeDifThold": lteEnbEdgeDifThold,
       "lteEnbMeas": lteEnbMeas,
       "lteEnbMeasGap": lteEnbMeasGap,
       "lteEnbMeasCarrfreq1": lteEnbMeasCarrfreq1,
       "lteEnbMeasCarrfreq2": lteEnbMeasCarrfreq2,
       "lteEnbMeasA1Thold": lteEnbMeasA1Thold,
       "lteEnbMeasA2Thold": lteEnbMeasA2Thold,
       "lteEnbMeasA3Offset": lteEnbMeasA3Offset,
       "lteEnbMeasA3Hys": lteEnbMeasA3Hys,
       "lteEnbMeasA3TimeTrig": lteEnbMeasA3TimeTrig,
       "lteEnbMeasA3RpIntval": lteEnbMeasA3RpIntval,
       "lteEnbID": lteEnbID,
       "lteUEInfoGetObjects": lteUEInfoGetObjects,
       "lteUEInfoGetTable": lteUEInfoGetTable,
       "lteUEInfoGetEntry": lteUEInfoGetEntry,
       "lteUEImsi": lteUEImsi,
       "lteUEIpaddr": lteUEIpaddr,
       "lteUEGuti": lteUEGuti,
       "lteUEUptime": lteUEUptime,
       "lteUERxpkt": lteUERxpkt,
       "lteUETxpkt": lteUETxpkt,
       "lteUECellId": lteUECellId,
       "lteUEIsAttached": lteUEIsAttached,
       "lteUECapbility": lteUECapbility,
       "lteUEAssoEnbMac": lteUEAssoEnbMac,
       "lteUERrcState": lteUERrcState,
       "lteUERxbytes": lteUERxbytes,
       "lteUETxbytes": lteUETxbytes,
       "lteEnbInfoGetObjects": lteEnbInfoGetObjects,
       "lteEnbInfoGetTable": lteEnbInfoGetTable,
       "lteEnbInfoGetEntry": lteEnbInfoGetEntry,
       "lteEnbNameInfo": lteEnbNameInfo,
       "lteEnbFreqBandNumber": lteEnbFreqBandNumber,
       "lteEnbUENumber": lteEnbUENumber,
       "lteEpcStatusEntry": lteEpcStatusEntry,
       "lteEpcAttachUENumber": lteEpcAttachUENumber,
       "lteEpcConfigEntry": lteEpcConfigEntry,
       "lteEpcEEA": lteEpcEEA,
       "lteEpcEIA": lteEpcEIA,
       "lteEpcMMECode": lteEpcMMECode,
       "lteEpcMMEGid": lteEpcMMEGid,
       "lteEpcMCC": lteEpcMCC,
       "lteEpcMNC": lteEpcMNC,
       "lteEpcEnbKeepalivetimer": lteEpcEnbKeepalivetimer,
       "lteEpcDNS": lteEpcDNS,
       "lteUEIMSIMapIpObjects": lteUEIMSIMapIpObjects,
       "lteUEIMSIMapIpTable": lteUEIMSIMapIpTable,
       "lteUEIMSIMapIpEntry": lteUEIMSIMapIpEntry,
       "lteUEIMSI": lteUEIMSI,
       "lteUEIP": lteUEIP,
       "lteUERowStatus": lteUERowStatus,
       "lteRuijieAlarmTraps": lteRuijieAlarmTraps,
       "lteEnbOnlineTraps": lteEnbOnlineTraps,
       "lteEnbOfflineTraps": lteEnbOfflineTraps,
       "lteUEAttachedTraps": lteUEAttachedTraps,
       "lteUEDetachedTraps": lteUEDetachedTraps,
       "lteRuijieAlarmTrapObjects": lteRuijieAlarmTrapObjects,
       "eNodeBmac": eNodeBmac,
       "eNodeBname": eNodeBname,
       "ueIMSI": ueIMSI,
       "ueIpaddr": ueIpaddr}
)
