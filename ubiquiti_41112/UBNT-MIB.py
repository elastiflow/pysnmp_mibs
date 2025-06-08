# SNMP MIB module (UBNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ubiquiti_41112/UBNT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:33:11 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ubntMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1)
)
if mibBuilder.loadTexts:
    ubntMIB.setRevisions(
        ("2014-08-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ubnt_ObjectIdentity = ObjectIdentity
ubnt = _Ubnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112)
)
_UbntORTable_Object = MibTable
ubntORTable = _UbntORTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1)
)
if mibBuilder.loadTexts:
    ubntORTable.setStatus("current")
_UbntOREntry_Object = MibTableRow
ubntOREntry = _UbntOREntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1)
)
ubntOREntry.setIndexNames(
    (0, "UBNT-MIB", "ubntORIndex"),
)
if mibBuilder.loadTexts:
    ubntOREntry.setStatus("current")


class _UbntORIndex_Type(Integer32):
    """Custom type ubntORIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntORIndex_Type.__name__ = "Integer32"
_UbntORIndex_Object = MibTableColumn
ubntORIndex = _UbntORIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 1),
    _UbntORIndex_Type()
)
ubntORIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntORIndex.setStatus("current")
_UbntORID_Type = ObjectIdentifier
_UbntORID_Object = MibTableColumn
ubntORID = _UbntORID_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 2),
    _UbntORID_Type()
)
ubntORID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntORID.setStatus("current")
_UbntORDescr_Type = DisplayString
_UbntORDescr_Object = MibTableColumn
ubntORDescr = _UbntORDescr_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 3),
    _UbntORDescr_Type()
)
ubntORDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntORDescr.setStatus("current")
_UbntSnmpInfo_ObjectIdentity = ObjectIdentity
ubntSnmpInfo = _UbntSnmpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2)
)
_UbntSnmpGroups_ObjectIdentity = ObjectIdentity
ubntSnmpGroups = _UbntSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 1)
)
_UbntAirosGroups_ObjectIdentity = ObjectIdentity
ubntAirosGroups = _UbntAirosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 2)
)
_UbntAirFiberGroups_ObjectIdentity = ObjectIdentity
ubntAirFiberGroups = _UbntAirFiberGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 3)
)
_UbntEdgeMaxGroups_ObjectIdentity = ObjectIdentity
ubntEdgeMaxGroups = _UbntEdgeMaxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 4)
)
_UbntUniFiGroups_ObjectIdentity = ObjectIdentity
ubntUniFiGroups = _UbntUniFiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 5)
)
_UbntAirVisionGroups_ObjectIdentity = ObjectIdentity
ubntAirVisionGroups = _UbntAirVisionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 6)
)
_UbntMFiGroups_ObjectIdentity = ObjectIdentity
ubntMFiGroups = _UbntMFiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 7)
)
_UbntUniTelGroups_ObjectIdentity = ObjectIdentity
ubntUniTelGroups = _UbntUniTelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 8)
)
_UbntAFLTUGroups_ObjectIdentity = ObjectIdentity
ubntAFLTUGroups = _UbntAFLTUGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 9)
)
_UbntAirFIBER_ObjectIdentity = ObjectIdentity
ubntAirFIBER = _UbntAirFIBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3)
)
_AirFiberConfig_Object = MibTable
airFiberConfig = _AirFiberConfig_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1)
)
if mibBuilder.loadTexts:
    airFiberConfig.setStatus("current")
_AirFiberConfigEntry_Object = MibTableRow
airFiberConfigEntry = _AirFiberConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1)
)
airFiberConfigEntry.setIndexNames(
    (0, "UBNT-MIB", "airFiberConfigIndex"),
)
if mibBuilder.loadTexts:
    airFiberConfigEntry.setStatus("current")


class _AirFiberConfigIndex_Type(Integer32):
    """Custom type airFiberConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AirFiberConfigIndex_Type.__name__ = "Integer32"
_AirFiberConfigIndex_Object = MibTableColumn
airFiberConfigIndex = _AirFiberConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 1),
    _AirFiberConfigIndex_Type()
)
airFiberConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    airFiberConfigIndex.setStatus("current")


class _RadioEnable_Type(Integer32):
    """Custom type radioEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RadioEnable_Type.__name__ = "Integer32"
_RadioEnable_Object = MibTableColumn
radioEnable = _RadioEnable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 2),
    _RadioEnable_Type()
)
radioEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioEnable.setStatus("current")


class _RadioLinkMode_Type(Integer32):
    """Custom type radioLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("spectral", 3))
    )


_RadioLinkMode_Type.__name__ = "Integer32"
_RadioLinkMode_Object = MibTableColumn
radioLinkMode = _RadioLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 3),
    _RadioLinkMode_Type()
)
radioLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLinkMode.setStatus("current")


class _RadioDuplex_Type(Integer32):
    """Custom type radioDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_RadioDuplex_Type.__name__ = "Integer32"
_RadioDuplex_Object = MibTableColumn
radioDuplex = _RadioDuplex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 4),
    _RadioDuplex_Type()
)
radioDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDuplex.setStatus("current")
_TxFrequency_Type = Integer32
_TxFrequency_Object = MibTableColumn
txFrequency = _TxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 5),
    _TxFrequency_Type()
)
txFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFrequency.setStatus("current")
_RxFrequency_Type = Integer32
_RxFrequency_Object = MibTableColumn
rxFrequency = _RxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 6),
    _RxFrequency_Type()
)
rxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFrequency.setStatus("current")
_RegDomain_Type = DisplayString
_RegDomain_Object = MibTableColumn
regDomain = _RegDomain_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 7),
    _RegDomain_Type()
)
regDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regDomain.setStatus("current")


class _GpsSync_Type(Integer32):
    """Custom type gpsSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_GpsSync_Type.__name__ = "Integer32"
_GpsSync_Object = MibTableColumn
gpsSync = _GpsSync_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 8),
    _GpsSync_Type()
)
gpsSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSync.setStatus("current")
_TxPower_Type = Integer32
_TxPower_Object = MibTableColumn
txPower = _TxPower_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 9),
    _TxPower_Type()
)
txPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPower.setStatus("current")


class _RxGain_Type(Integer32):
    """Custom type rxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_RxGain_Type.__name__ = "Integer32"
_RxGain_Object = MibTableColumn
rxGain = _RxGain_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 10),
    _RxGain_Type()
)
rxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxGain.setStatus("current")


class _MaxTxModRate_Type(Integer32):
    """Custom type maxTxModRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("qPSK-SISO-1-4x", 0),
          ("qPSK-SISO-1x", 1),
          ("qPSK-MIMO-2x", 2),
          ("qAM16-MIMO-4x", 4),
          ("qAM64-MIMO-6x", 6),
          ("qAM256-MIMO-8x", 8))
    )


_MaxTxModRate_Type.__name__ = "Integer32"
_MaxTxModRate_Object = MibTableColumn
maxTxModRate = _MaxTxModRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 11),
    _MaxTxModRate_Type()
)
maxTxModRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxTxModRate.setStatus("current")


class _ModRateControl_Type(Integer32):
    """Custom type modRateControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_ModRateControl_Type.__name__ = "Integer32"
_ModRateControl_Object = MibTableColumn
modRateControl = _ModRateControl_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 12),
    _ModRateControl_Type()
)
modRateControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modRateControl.setStatus("current")


class _EthDPortLinkSpeed_Type(Integer32):
    """Custom type ethDPortLinkSpeed based on Integer32"""
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
        *(("auto", 1),
          ("half-10Mbps", 2),
          ("half-100Mbps", 3),
          ("full-10Mbps", 4),
          ("full-100Mbps", 5),
          ("full-1000Mbps", 6))
    )


_EthDPortLinkSpeed_Type.__name__ = "Integer32"
_EthDPortLinkSpeed_Object = MibTableColumn
ethDPortLinkSpeed = _EthDPortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 13),
    _EthDPortLinkSpeed_Type()
)
ethDPortLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDPortLinkSpeed.setStatus("current")
_LinkName_Type = DisplayString
_LinkName_Object = MibTableColumn
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 14),
    _LinkName_Type()
)
linkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkName.setStatus("current")
_EncryptKey_Type = DisplayString
_EncryptKey_Object = MibTableColumn
encryptKey = _EncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 15),
    _EncryptKey_Type()
)
encryptKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptKey.setStatus("obsolete")


class _EthFlowControl_Type(Integer32):
    """Custom type ethFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EthFlowControl_Type.__name__ = "Integer32"
_EthFlowControl_Object = MibTableColumn
ethFlowControl = _EthFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 16),
    _EthFlowControl_Type()
)
ethFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFlowControl.setStatus("current")


class _EthMcastFilter_Type(Integer32):
    """Custom type ethMcastFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EthMcastFilter_Type.__name__ = "Integer32"
_EthMcastFilter_Object = MibTableColumn
ethMcastFilter = _EthMcastFilter_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 17),
    _EthMcastFilter_Type()
)
ethMcastFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethMcastFilter.setStatus("current")


class _EthTrackRFLink_Type(Integer32):
    """Custom type ethTrackRFLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("use-Timers", 1),
          ("enabled", 2))
    )


_EthTrackRFLink_Type.__name__ = "Integer32"
_EthTrackRFLink_Object = MibTableColumn
ethTrackRFLink = _EthTrackRFLink_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 18),
    _EthTrackRFLink_Type()
)
ethTrackRFLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethTrackRFLink.setStatus("current")
_EthLinkOffDuration_Type = Integer32
_EthLinkOffDuration_Object = MibTableColumn
ethLinkOffDuration = _EthLinkOffDuration_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 19),
    _EthLinkOffDuration_Type()
)
ethLinkOffDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethLinkOffDuration.setStatus("current")
_EthLinkOffSpacing_Type = Integer32
_EthLinkOffSpacing_Object = MibTableColumn
ethLinkOffSpacing = _EthLinkOffSpacing_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 20),
    _EthLinkOffSpacing_Type()
)
ethLinkOffSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethLinkOffSpacing.setStatus("current")
_TxFrequency1_Type = Integer32
_TxFrequency1_Object = MibTableColumn
txFrequency1 = _TxFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 21),
    _TxFrequency1_Type()
)
txFrequency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFrequency1.setStatus("current")
_RxFrequency1_Type = Integer32
_RxFrequency1_Object = MibTableColumn
rxFrequency1 = _RxFrequency1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 22),
    _RxFrequency1_Type()
)
rxFrequency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFrequency1.setStatus("current")
_TxFrequency2_Type = Integer32
_TxFrequency2_Object = MibTableColumn
txFrequency2 = _TxFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 23),
    _TxFrequency2_Type()
)
txFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFrequency2.setStatus("current")
_RxFrequency2_Type = Integer32
_RxFrequency2_Object = MibTableColumn
rxFrequency2 = _RxFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 24),
    _RxFrequency2_Type()
)
rxFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFrequency2.setStatus("current")
_TxFrequency3_Type = Integer32
_TxFrequency3_Object = MibTableColumn
txFrequency3 = _TxFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 25),
    _TxFrequency3_Type()
)
txFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFrequency3.setStatus("current")
_RxFrequency3_Type = Integer32
_RxFrequency3_Object = MibTableColumn
rxFrequency3 = _RxFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 26),
    _RxFrequency3_Type()
)
rxFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFrequency3.setStatus("current")
_ChannelWidth_Type = Integer32
_ChannelWidth_Object = MibTableColumn
channelWidth = _ChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 27),
    _ChannelWidth_Type()
)
channelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelWidth.setStatus("obsolete")
_TxChannelWidth_Type = Integer32
_TxChannelWidth_Object = MibTableColumn
txChannelWidth = _TxChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 28),
    _TxChannelWidth_Type()
)
txChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txChannelWidth.setStatus("current")
_RxChannelWidth_Type = Integer32
_RxChannelWidth_Object = MibTableColumn
rxChannelWidth = _RxChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 1, 1, 29),
    _RxChannelWidth_Type()
)
rxChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxChannelWidth.setStatus("current")
_AirFiberStatus_Object = MibTable
airFiberStatus = _AirFiberStatus_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2)
)
if mibBuilder.loadTexts:
    airFiberStatus.setStatus("current")
_AirFiberStatusEntry_Object = MibTableRow
airFiberStatusEntry = _AirFiberStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1)
)
airFiberStatusEntry.setIndexNames(
    (0, "UBNT-MIB", "airFiberStatusIndex"),
)
if mibBuilder.loadTexts:
    airFiberStatusEntry.setStatus("current")


class _AirFiberStatusIndex_Type(Integer32):
    """Custom type airFiberStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AirFiberStatusIndex_Type.__name__ = "Integer32"
_AirFiberStatusIndex_Object = MibTableColumn
airFiberStatusIndex = _AirFiberStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 1),
    _AirFiberStatusIndex_Type()
)
airFiberStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    airFiberStatusIndex.setStatus("current")


class _CurTXModRate_Type(Integer32):
    """Custom type curTXModRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("qPSK-SISO-1-4x", 0),
          ("qPSK-SISO-1x", 1),
          ("qPSK-MIMO-2x", 2),
          ("qAM16-MIMO-4x", 4),
          ("qAM64-MIMO-6x", 6),
          ("qAM256-MIMO-8x", 8))
    )


_CurTXModRate_Type.__name__ = "Integer32"
_CurTXModRate_Object = MibTableColumn
curTXModRate = _CurTXModRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 2),
    _CurTXModRate_Type()
)
curTXModRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curTXModRate.setStatus("current")
_RadioLinkDistFt_Type = Integer32
_RadioLinkDistFt_Object = MibTableColumn
radioLinkDistFt = _RadioLinkDistFt_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 3),
    _RadioLinkDistFt_Type()
)
radioLinkDistFt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLinkDistFt.setStatus("current")
_RadioLinkDistM_Type = Integer32
_RadioLinkDistM_Object = MibTableColumn
radioLinkDistM = _RadioLinkDistM_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 4),
    _RadioLinkDistM_Type()
)
radioLinkDistM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLinkDistM.setStatus("current")
_RxCapacity_Type = Integer32
_RxCapacity_Object = MibTableColumn
rxCapacity = _RxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 5),
    _RxCapacity_Type()
)
rxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxCapacity.setStatus("current")
_TxCapacity_Type = Integer32
_TxCapacity_Object = MibTableColumn
txCapacity = _TxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 6),
    _TxCapacity_Type()
)
txCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCapacity.setStatus("current")
_Radio0TempF_Type = Integer32
_Radio0TempF_Object = MibTableColumn
radio0TempF = _Radio0TempF_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 7),
    _Radio0TempF_Type()
)
radio0TempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radio0TempF.setStatus("current")
_Radio0TempC_Type = Integer32
_Radio0TempC_Object = MibTableColumn
radio0TempC = _Radio0TempC_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 8),
    _Radio0TempC_Type()
)
radio0TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radio0TempC.setStatus("current")
_Radio1TempF_Type = Integer32
_Radio1TempF_Object = MibTableColumn
radio1TempF = _Radio1TempF_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 9),
    _Radio1TempF_Type()
)
radio1TempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radio1TempF.setStatus("current")
_Radio1TempC_Type = Integer32
_Radio1TempC_Object = MibTableColumn
radio1TempC = _Radio1TempC_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 10),
    _Radio1TempC_Type()
)
radio1TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radio1TempC.setStatus("current")
_RxPower0_Type = Integer32
_RxPower0_Object = MibTableColumn
rxPower0 = _RxPower0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 11),
    _RxPower0_Type()
)
rxPower0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPower0.setStatus("current")
_RxPower0Valid_Type = TruthValue
_RxPower0Valid_Object = MibTableColumn
rxPower0Valid = _RxPower0Valid_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 12),
    _RxPower0Valid_Type()
)
rxPower0Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPower0Valid.setStatus("current")
_RxOverload0_Type = TruthValue
_RxOverload0_Object = MibTableColumn
rxOverload0 = _RxOverload0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 13),
    _RxOverload0_Type()
)
rxOverload0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOverload0.setStatus("current")
_RxPower1_Type = Integer32
_RxPower1_Object = MibTableColumn
rxPower1 = _RxPower1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 14),
    _RxPower1_Type()
)
rxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPower1.setStatus("current")
_RxPower1Valid_Type = TruthValue
_RxPower1Valid_Object = MibTableColumn
rxPower1Valid = _RxPower1Valid_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 15),
    _RxPower1Valid_Type()
)
rxPower1Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPower1Valid.setStatus("current")
_RxOverload1_Type = TruthValue
_RxOverload1_Object = MibTableColumn
rxOverload1 = _RxOverload1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 16),
    _RxOverload1_Type()
)
rxOverload1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOverload1.setStatus("current")
_RemoteTXPower_Type = Integer32
_RemoteTXPower_Object = MibTableColumn
remoteTXPower = _RemoteTXPower_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 17),
    _RemoteTXPower_Type()
)
remoteTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteTXPower.setStatus("current")


class _RemoteTXModRate_Type(Integer32):
    """Custom type remoteTXModRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("qPSK-SISO-1-4x", 0),
          ("qPSK-SISO-1x", 1),
          ("qPSK-MIMO-2x", 2),
          ("qAM16-MIMO-4x", 4),
          ("qAM64-MIMO-6x", 6),
          ("qAM256-MIMO-8x", 8))
    )


_RemoteTXModRate_Type.__name__ = "Integer32"
_RemoteTXModRate_Object = MibTableColumn
remoteTXModRate = _RemoteTXModRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 18),
    _RemoteTXModRate_Type()
)
remoteTXModRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteTXModRate.setStatus("current")
_RemoteRXPower0_Type = Integer32
_RemoteRXPower0_Object = MibTableColumn
remoteRXPower0 = _RemoteRXPower0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 19),
    _RemoteRXPower0_Type()
)
remoteRXPower0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteRXPower0.setStatus("current")
_RemoteRXPower0Valid_Type = TruthValue
_RemoteRXPower0Valid_Object = MibTableColumn
remoteRXPower0Valid = _RemoteRXPower0Valid_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 20),
    _RemoteRXPower0Valid_Type()
)
remoteRXPower0Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteRXPower0Valid.setStatus("current")
_RemoteRXPower0Overload_Type = TruthValue
_RemoteRXPower0Overload_Object = MibTableColumn
remoteRXPower0Overload = _RemoteRXPower0Overload_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 21),
    _RemoteRXPower0Overload_Type()
)
remoteRXPower0Overload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteRXPower0Overload.setStatus("current")
_RemoteRXPower1_Type = Integer32
_RemoteRXPower1_Object = MibTableColumn
remoteRXPower1 = _RemoteRXPower1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 22),
    _RemoteRXPower1_Type()
)
remoteRXPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteRXPower1.setStatus("current")
_RemoteRXPower1Valid_Type = TruthValue
_RemoteRXPower1Valid_Object = MibTableColumn
remoteRXPower1Valid = _RemoteRXPower1Valid_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 23),
    _RemoteRXPower1Valid_Type()
)
remoteRXPower1Valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteRXPower1Valid.setStatus("current")
_RemoteRXPower1Overload_Type = TruthValue
_RemoteRXPower1Overload_Object = MibTableColumn
remoteRXPower1Overload = _RemoteRXPower1Overload_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 24),
    _RemoteRXPower1Overload_Type()
)
remoteRXPower1Overload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteRXPower1Overload.setStatus("current")
_CountryCode_Type = Integer32
_CountryCode_Object = MibTableColumn
countryCode = _CountryCode_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 25),
    _CountryCode_Type()
)
countryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countryCode.setStatus("current")


class _RadioLinkState_Type(Integer32):
    """Custom type radioLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_RadioLinkState_Type.__name__ = "Integer32"
_RadioLinkState_Object = MibTableColumn
radioLinkState = _RadioLinkState_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 26),
    _RadioLinkState_Type()
)
radioLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLinkState.setStatus("current")


class _EthDataPortState_Type(Integer32):
    """Custom type ethDataPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_EthDataPortState_Type.__name__ = "Integer32"
_EthDataPortState_Object = MibTableColumn
ethDataPortState = _EthDataPortState_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 27),
    _EthDataPortState_Type()
)
ethDataPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDataPortState.setStatus("current")
_GpsPulse_Type = DisplayString
_GpsPulse_Object = MibTableColumn
gpsPulse = _GpsPulse_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 28),
    _GpsPulse_Type()
)
gpsPulse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsPulse.setStatus("current")
_GpsFix_Type = DisplayString
_GpsFix_Object = MibTableColumn
gpsFix = _GpsFix_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 29),
    _GpsFix_Type()
)
gpsFix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFix.setStatus("current")
_GpsLat_Type = DisplayString
_GpsLat_Object = MibTableColumn
gpsLat = _GpsLat_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 30),
    _GpsLat_Type()
)
gpsLat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLat.setStatus("current")
_GpsLong_Type = DisplayString
_GpsLong_Object = MibTableColumn
gpsLong = _GpsLong_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 31),
    _GpsLong_Type()
)
gpsLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLong.setStatus("current")
_GpsAltMeters_Type = DisplayString
_GpsAltMeters_Object = MibTableColumn
gpsAltMeters = _GpsAltMeters_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 32),
    _GpsAltMeters_Type()
)
gpsAltMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAltMeters.setStatus("current")
_GpsAltFeet_Type = DisplayString
_GpsAltFeet_Object = MibTableColumn
gpsAltFeet = _GpsAltFeet_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 33),
    _GpsAltFeet_Type()
)
gpsAltFeet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAltFeet.setStatus("current")
_GpsSatsVisible_Type = Integer32
_GpsSatsVisible_Object = MibTableColumn
gpsSatsVisible = _GpsSatsVisible_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 34),
    _GpsSatsVisible_Type()
)
gpsSatsVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatsVisible.setStatus("current")
_GpsSatsTracked_Type = Integer32
_GpsSatsTracked_Object = MibTableColumn
gpsSatsTracked = _GpsSatsTracked_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 35),
    _GpsSatsTracked_Type()
)
gpsSatsTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatsTracked.setStatus("current")
_GpsHDOP_Type = OctetString
_GpsHDOP_Object = MibTableColumn
gpsHDOP = _GpsHDOP_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 36),
    _GpsHDOP_Type()
)
gpsHDOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHDOP.setStatus("current")
_DfsState_Type = DisplayString
_DfsState_Object = MibTableColumn
dfsState = _DfsState_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 37),
    _DfsState_Type()
)
dfsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsState.setStatus("current")
_UpTime_Type = Integer32
_UpTime_Object = MibTableColumn
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 38),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("current")
_DateTime_Type = DisplayString
_DateTime_Object = MibTableColumn
dateTime = _DateTime_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 39),
    _DateTime_Type()
)
dateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateTime.setStatus("current")
_FwVersion_Type = DisplayString
_FwVersion_Object = MibTableColumn
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 40),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")
_RemoteRXGain_Type = DisplayString
_RemoteRXGain_Object = MibTableColumn
remoteRXGain = _RemoteRXGain_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 41),
    _RemoteRXGain_Type()
)
remoteRXGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteRXGain.setStatus("current")
_RadioLinkInfo_Type = DisplayString
_RadioLinkInfo_Object = MibTableColumn
radioLinkInfo = _RadioLinkInfo_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 42),
    _RadioLinkInfo_Type()
)
radioLinkInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLinkInfo.setStatus("current")
_EthDataPortInfo_Type = DisplayString
_EthDataPortInfo_Object = MibTableColumn
ethDataPortInfo = _EthDataPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 43),
    _EthDataPortInfo_Type()
)
ethDataPortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethDataPortInfo.setStatus("current")
_LinkUpTime_Type = Integer32
_LinkUpTime_Object = MibTableColumn
linkUpTime = _LinkUpTime_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 44),
    _LinkUpTime_Type()
)
linkUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkUpTime.setStatus("current")
_RemoteMAC_Type = DisplayString
_RemoteMAC_Object = MibTableColumn
remoteMAC = _RemoteMAC_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 45),
    _RemoteMAC_Type()
)
remoteMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMAC.setStatus("current")
_RemoteIP_Type = DisplayString
_RemoteIP_Object = MibTableColumn
remoteIP = _RemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 46),
    _RemoteIP_Type()
)
remoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIP.setStatus("current")
_DfsDetections_Type = Integer32
_DfsDetections_Object = MibTableColumn
dfsDetections = _DfsDetections_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 47),
    _DfsDetections_Type()
)
dfsDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsDetections.setStatus("current")
_DfsDomain_Type = DisplayString
_DfsDomain_Object = MibTableColumn
dfsDomain = _DfsDomain_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 48),
    _DfsDomain_Type()
)
dfsDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsDomain.setStatus("current")
_DfsStateTxFreq1_Type = DisplayString
_DfsStateTxFreq1_Object = MibTableColumn
dfsStateTxFreq1 = _DfsStateTxFreq1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 49),
    _DfsStateTxFreq1_Type()
)
dfsStateTxFreq1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsStateTxFreq1.setStatus("current")
_DfsStateTxFreq2_Type = DisplayString
_DfsStateTxFreq2_Object = MibTableColumn
dfsStateTxFreq2 = _DfsStateTxFreq2_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 50),
    _DfsStateTxFreq2_Type()
)
dfsStateTxFreq2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsStateTxFreq2.setStatus("current")
_DfsStateTxFreq3_Type = DisplayString
_DfsStateTxFreq3_Object = MibTableColumn
dfsStateTxFreq3 = _DfsStateTxFreq3_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 51),
    _DfsStateTxFreq3_Type()
)
dfsStateTxFreq3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsStateTxFreq3.setStatus("current")
_DfsTimerTxFreq1_Type = Integer32
_DfsTimerTxFreq1_Object = MibTableColumn
dfsTimerTxFreq1 = _DfsTimerTxFreq1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 52),
    _DfsTimerTxFreq1_Type()
)
dfsTimerTxFreq1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsTimerTxFreq1.setStatus("current")
_DfsTimerTxFreq2_Type = Integer32
_DfsTimerTxFreq2_Object = MibTableColumn
dfsTimerTxFreq2 = _DfsTimerTxFreq2_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 53),
    _DfsTimerTxFreq2_Type()
)
dfsTimerTxFreq2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsTimerTxFreq2.setStatus("current")
_DfsTimerTxFreq3_Type = Integer32
_DfsTimerTxFreq3_Object = MibTableColumn
dfsTimerTxFreq3 = _DfsTimerTxFreq3_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 2, 1, 54),
    _DfsTimerTxFreq3_Type()
)
dfsTimerTxFreq3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsTimerTxFreq3.setStatus("current")
_AirFiberStatistics_Object = MibTable
airFiberStatistics = _AirFiberStatistics_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3)
)
if mibBuilder.loadTexts:
    airFiberStatistics.setStatus("current")
_AirFiberStatisticsEntry_Object = MibTableRow
airFiberStatisticsEntry = _AirFiberStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1)
)
airFiberStatisticsEntry.setIndexNames(
    (0, "UBNT-MIB", "airFiberStatisticsIndex"),
)
if mibBuilder.loadTexts:
    airFiberStatisticsEntry.setStatus("current")


class _AirFiberStatisticsIndex_Type(Integer32):
    """Custom type airFiberStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AirFiberStatisticsIndex_Type.__name__ = "Integer32"
_AirFiberStatisticsIndex_Object = MibTableColumn
airFiberStatisticsIndex = _AirFiberStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 1),
    _AirFiberStatisticsIndex_Type()
)
airFiberStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    airFiberStatisticsIndex.setStatus("current")
_TxFramesOK_Type = Counter64
_TxFramesOK_Object = MibTableColumn
txFramesOK = _TxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 2),
    _TxFramesOK_Type()
)
txFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFramesOK.setStatus("current")
_RxFramesOK_Type = Counter64
_RxFramesOK_Object = MibTableColumn
rxFramesOK = _RxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 3),
    _RxFramesOK_Type()
)
rxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFramesOK.setStatus("current")
_RxFrameCrcErr_Type = Counter64
_RxFrameCrcErr_Object = MibTableColumn
rxFrameCrcErr = _RxFrameCrcErr_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 4),
    _RxFrameCrcErr_Type()
)
rxFrameCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFrameCrcErr.setStatus("current")
_RxAlignErr_Type = Counter64
_RxAlignErr_Object = MibTableColumn
rxAlignErr = _RxAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 5),
    _RxAlignErr_Type()
)
rxAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAlignErr.setStatus("current")
_TxOctetsOK_Type = Counter64
_TxOctetsOK_Object = MibTableColumn
txOctetsOK = _TxOctetsOK_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 6),
    _TxOctetsOK_Type()
)
txOctetsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctetsOK.setStatus("current")
_RxOctetsOK_Type = Counter64
_RxOctetsOK_Object = MibTableColumn
rxOctetsOK = _RxOctetsOK_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 7),
    _RxOctetsOK_Type()
)
rxOctetsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctetsOK.setStatus("current")
_TxPauseFrames_Type = Counter64
_TxPauseFrames_Object = MibTableColumn
txPauseFrames = _TxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 8),
    _TxPauseFrames_Type()
)
txPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPauseFrames.setStatus("current")
_RxPauseFrames_Type = Counter64
_RxPauseFrames_Object = MibTableColumn
rxPauseFrames = _RxPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 9),
    _RxPauseFrames_Type()
)
rxPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPauseFrames.setStatus("current")
_RxErroredFrames_Type = Counter64
_RxErroredFrames_Object = MibTableColumn
rxErroredFrames = _RxErroredFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 10),
    _RxErroredFrames_Type()
)
rxErroredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxErroredFrames.setStatus("current")
_TxErroredFrames_Type = Counter64
_TxErroredFrames_Object = MibTableColumn
txErroredFrames = _TxErroredFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 11),
    _TxErroredFrames_Type()
)
txErroredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txErroredFrames.setStatus("current")
_RxValidUnicastFrames_Type = Counter64
_RxValidUnicastFrames_Object = MibTableColumn
rxValidUnicastFrames = _RxValidUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 12),
    _RxValidUnicastFrames_Type()
)
rxValidUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxValidUnicastFrames.setStatus("current")
_RxValidMulticastFrames_Type = Counter64
_RxValidMulticastFrames_Object = MibTableColumn
rxValidMulticastFrames = _RxValidMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 13),
    _RxValidMulticastFrames_Type()
)
rxValidMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxValidMulticastFrames.setStatus("current")
_RxValidBroadcastFrames_Type = Counter64
_RxValidBroadcastFrames_Object = MibTableColumn
rxValidBroadcastFrames = _RxValidBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 14),
    _RxValidBroadcastFrames_Type()
)
rxValidBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxValidBroadcastFrames.setStatus("current")
_TxValidUnicastFrames_Type = Counter64
_TxValidUnicastFrames_Object = MibTableColumn
txValidUnicastFrames = _TxValidUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 15),
    _TxValidUnicastFrames_Type()
)
txValidUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txValidUnicastFrames.setStatus("current")
_TxValidMulticastFrames_Type = Counter64
_TxValidMulticastFrames_Object = MibTableColumn
txValidMulticastFrames = _TxValidMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 16),
    _TxValidMulticastFrames_Type()
)
txValidMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txValidMulticastFrames.setStatus("current")
_TxValidBroadcastFrames_Type = Counter64
_TxValidBroadcastFrames_Object = MibTableColumn
txValidBroadcastFrames = _TxValidBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 17),
    _TxValidBroadcastFrames_Type()
)
txValidBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txValidBroadcastFrames.setStatus("current")
_RxDroppedMacErrFrames_Type = Counter64
_RxDroppedMacErrFrames_Object = MibTableColumn
rxDroppedMacErrFrames = _RxDroppedMacErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 18),
    _RxDroppedMacErrFrames_Type()
)
rxDroppedMacErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDroppedMacErrFrames.setStatus("current")
_RxTotalOctets_Type = Counter64
_RxTotalOctets_Object = MibTableColumn
rxTotalOctets = _RxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 19),
    _RxTotalOctets_Type()
)
rxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxTotalOctets.setStatus("current")
_RxTotalFrames_Type = Counter64
_RxTotalFrames_Object = MibTableColumn
rxTotalFrames = _RxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 20),
    _RxTotalFrames_Type()
)
rxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxTotalFrames.setStatus("current")
_RxLess64ByteFrames_Type = Counter64
_RxLess64ByteFrames_Object = MibTableColumn
rxLess64ByteFrames = _RxLess64ByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 21),
    _RxLess64ByteFrames_Type()
)
rxLess64ByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxLess64ByteFrames.setStatus("current")
_RxOverLengthFrames_Type = Counter64
_RxOverLengthFrames_Object = MibTableColumn
rxOverLengthFrames = _RxOverLengthFrames_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 22),
    _RxOverLengthFrames_Type()
)
rxOverLengthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOverLengthFrames.setStatus("current")
_Rx64BytePackets_Type = Counter64
_Rx64BytePackets_Object = MibTableColumn
rx64BytePackets = _Rx64BytePackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 23),
    _Rx64BytePackets_Type()
)
rx64BytePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx64BytePackets.setStatus("current")
_Rx65_127BytePackets_Type = Counter64
_Rx65_127BytePackets_Object = MibTableColumn
rx65_127BytePackets = _Rx65_127BytePackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 24),
    _Rx65_127BytePackets_Type()
)
rx65_127BytePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx65_127BytePackets.setStatus("current")
_Rx128_255BytePackets_Type = Counter64
_Rx128_255BytePackets_Object = MibTableColumn
rx128_255BytePackets = _Rx128_255BytePackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 25),
    _Rx128_255BytePackets_Type()
)
rx128_255BytePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx128_255BytePackets.setStatus("current")
_Rx256_511BytePackets_Type = Counter64
_Rx256_511BytePackets_Object = MibTableColumn
rx256_511BytePackets = _Rx256_511BytePackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 26),
    _Rx256_511BytePackets_Type()
)
rx256_511BytePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx256_511BytePackets.setStatus("current")
_Rx512_1023BytePackets_Type = Counter64
_Rx512_1023BytePackets_Object = MibTableColumn
rx512_1023BytePackets = _Rx512_1023BytePackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 27),
    _Rx512_1023BytePackets_Type()
)
rx512_1023BytePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx512_1023BytePackets.setStatus("current")
_Rx1024_1518BytesPackets_Type = Counter64
_Rx1024_1518BytesPackets_Object = MibTableColumn
rx1024_1518BytesPackets = _Rx1024_1518BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 28),
    _Rx1024_1518BytesPackets_Type()
)
rx1024_1518BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx1024_1518BytesPackets.setStatus("current")
_Rx1519PlusBytePackets_Type = Counter64
_Rx1519PlusBytePackets_Object = MibTableColumn
rx1519PlusBytePackets = _Rx1519PlusBytePackets_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 29),
    _Rx1519PlusBytePackets_Type()
)
rx1519PlusBytePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx1519PlusBytePackets.setStatus("current")
_RxTooLongFrameCrcErr_Type = Counter64
_RxTooLongFrameCrcErr_Object = MibTableColumn
rxTooLongFrameCrcErr = _RxTooLongFrameCrcErr_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 30),
    _RxTooLongFrameCrcErr_Type()
)
rxTooLongFrameCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxTooLongFrameCrcErr.setStatus("current")
_RxTooShortFrameCrcErr_Type = Counter64
_RxTooShortFrameCrcErr_Object = MibTableColumn
rxTooShortFrameCrcErr = _RxTooShortFrameCrcErr_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 31),
    _RxTooShortFrameCrcErr_Type()
)
rxTooShortFrameCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxTooShortFrameCrcErr.setStatus("current")
_Txqosoct0_Type = Counter64
_Txqosoct0_Object = MibTableColumn
txqosoct0 = _Txqosoct0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 32),
    _Txqosoct0_Type()
)
txqosoct0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqosoct0.setStatus("current")
_Txqosoct1_Type = Counter64
_Txqosoct1_Object = MibTableColumn
txqosoct1 = _Txqosoct1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 33),
    _Txqosoct1_Type()
)
txqosoct1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqosoct1.setStatus("current")
_Txqosoct2_Type = Counter64
_Txqosoct2_Object = MibTableColumn
txqosoct2 = _Txqosoct2_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 34),
    _Txqosoct2_Type()
)
txqosoct2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqosoct2.setStatus("current")
_Txqosoct3_Type = Counter64
_Txqosoct3_Object = MibTableColumn
txqosoct3 = _Txqosoct3_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 35),
    _Txqosoct3_Type()
)
txqosoct3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqosoct3.setStatus("current")
_Txqosoct4_Type = Counter64
_Txqosoct4_Object = MibTableColumn
txqosoct4 = _Txqosoct4_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 36),
    _Txqosoct4_Type()
)
txqosoct4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqosoct4.setStatus("current")
_Txqosoct5_Type = Counter64
_Txqosoct5_Object = MibTableColumn
txqosoct5 = _Txqosoct5_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 37),
    _Txqosoct5_Type()
)
txqosoct5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqosoct5.setStatus("current")
_Txqosoct6_Type = Counter64
_Txqosoct6_Object = MibTableColumn
txqosoct6 = _Txqosoct6_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 38),
    _Txqosoct6_Type()
)
txqosoct6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqosoct6.setStatus("current")
_Txqosoct7_Type = Counter64
_Txqosoct7_Object = MibTableColumn
txqosoct7 = _Txqosoct7_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 39),
    _Txqosoct7_Type()
)
txqosoct7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqosoct7.setStatus("current")
_Txqospkt0_Type = Counter64
_Txqospkt0_Object = MibTableColumn
txqospkt0 = _Txqospkt0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 40),
    _Txqospkt0_Type()
)
txqospkt0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqospkt0.setStatus("current")
_Txqospkt1_Type = Counter64
_Txqospkt1_Object = MibTableColumn
txqospkt1 = _Txqospkt1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 41),
    _Txqospkt1_Type()
)
txqospkt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqospkt1.setStatus("current")
_Txqospkt2_Type = Counter64
_Txqospkt2_Object = MibTableColumn
txqospkt2 = _Txqospkt2_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 42),
    _Txqospkt2_Type()
)
txqospkt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqospkt2.setStatus("current")
_Txqospkt3_Type = Counter64
_Txqospkt3_Object = MibTableColumn
txqospkt3 = _Txqospkt3_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 43),
    _Txqospkt3_Type()
)
txqospkt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqospkt3.setStatus("current")
_Txqospkt4_Type = Counter64
_Txqospkt4_Object = MibTableColumn
txqospkt4 = _Txqospkt4_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 44),
    _Txqospkt4_Type()
)
txqospkt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqospkt4.setStatus("current")
_Txqospkt5_Type = Counter64
_Txqospkt5_Object = MibTableColumn
txqospkt5 = _Txqospkt5_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 45),
    _Txqospkt5_Type()
)
txqospkt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqospkt5.setStatus("current")
_Txqospkt6_Type = Counter64
_Txqospkt6_Object = MibTableColumn
txqospkt6 = _Txqospkt6_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 46),
    _Txqospkt6_Type()
)
txqospkt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqospkt6.setStatus("current")
_Txqospkt7_Type = Counter64
_Txqospkt7_Object = MibTableColumn
txqospkt7 = _Txqospkt7_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 47),
    _Txqospkt7_Type()
)
txqospkt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txqospkt7.setStatus("current")
_Rxqosoct0_Type = Counter64
_Rxqosoct0_Object = MibTableColumn
rxqosoct0 = _Rxqosoct0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 48),
    _Rxqosoct0_Type()
)
rxqosoct0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqosoct0.setStatus("current")
_Rxqosoct1_Type = Counter64
_Rxqosoct1_Object = MibTableColumn
rxqosoct1 = _Rxqosoct1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 49),
    _Rxqosoct1_Type()
)
rxqosoct1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqosoct1.setStatus("current")
_Rxqosoct2_Type = Counter64
_Rxqosoct2_Object = MibTableColumn
rxqosoct2 = _Rxqosoct2_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 50),
    _Rxqosoct2_Type()
)
rxqosoct2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqosoct2.setStatus("current")
_Rxqosoct3_Type = Counter64
_Rxqosoct3_Object = MibTableColumn
rxqosoct3 = _Rxqosoct3_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 51),
    _Rxqosoct3_Type()
)
rxqosoct3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqosoct3.setStatus("current")
_Rxqosoct4_Type = Counter64
_Rxqosoct4_Object = MibTableColumn
rxqosoct4 = _Rxqosoct4_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 52),
    _Rxqosoct4_Type()
)
rxqosoct4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqosoct4.setStatus("current")
_Rxqosoct5_Type = Counter64
_Rxqosoct5_Object = MibTableColumn
rxqosoct5 = _Rxqosoct5_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 53),
    _Rxqosoct5_Type()
)
rxqosoct5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqosoct5.setStatus("current")
_Rxqosoct6_Type = Counter64
_Rxqosoct6_Object = MibTableColumn
rxqosoct6 = _Rxqosoct6_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 54),
    _Rxqosoct6_Type()
)
rxqosoct6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqosoct6.setStatus("current")
_Rxqosoct7_Type = Counter64
_Rxqosoct7_Object = MibTableColumn
rxqosoct7 = _Rxqosoct7_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 55),
    _Rxqosoct7_Type()
)
rxqosoct7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqosoct7.setStatus("current")
_Rxqospkt0_Type = Counter64
_Rxqospkt0_Object = MibTableColumn
rxqospkt0 = _Rxqospkt0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 56),
    _Rxqospkt0_Type()
)
rxqospkt0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqospkt0.setStatus("current")
_Rxqospkt1_Type = Counter64
_Rxqospkt1_Object = MibTableColumn
rxqospkt1 = _Rxqospkt1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 57),
    _Rxqospkt1_Type()
)
rxqospkt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqospkt1.setStatus("current")
_Rxqospkt2_Type = Counter64
_Rxqospkt2_Object = MibTableColumn
rxqospkt2 = _Rxqospkt2_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 58),
    _Rxqospkt2_Type()
)
rxqospkt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqospkt2.setStatus("current")
_Rxqospkt3_Type = Counter64
_Rxqospkt3_Object = MibTableColumn
rxqospkt3 = _Rxqospkt3_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 59),
    _Rxqospkt3_Type()
)
rxqospkt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqospkt3.setStatus("current")
_Rxqospkt4_Type = Counter64
_Rxqospkt4_Object = MibTableColumn
rxqospkt4 = _Rxqospkt4_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 60),
    _Rxqospkt4_Type()
)
rxqospkt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqospkt4.setStatus("current")
_Rxqospkt5_Type = Counter64
_Rxqospkt5_Object = MibTableColumn
rxqospkt5 = _Rxqospkt5_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 61),
    _Rxqospkt5_Type()
)
rxqospkt5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqospkt5.setStatus("current")
_Rxqospkt6_Type = Counter64
_Rxqospkt6_Object = MibTableColumn
rxqospkt6 = _Rxqospkt6_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 62),
    _Rxqospkt6_Type()
)
rxqospkt6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqospkt6.setStatus("current")
_Rxqospkt7_Type = Counter64
_Rxqospkt7_Object = MibTableColumn
rxqospkt7 = _Rxqospkt7_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 63),
    _Rxqospkt7_Type()
)
rxqospkt7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxqospkt7.setStatus("current")
_TxoctetsAll_Type = Counter64
_TxoctetsAll_Object = MibTableColumn
txoctetsAll = _TxoctetsAll_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 64),
    _TxoctetsAll_Type()
)
txoctetsAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txoctetsAll.setStatus("current")
_TxpktsAll_Type = Counter64
_TxpktsAll_Object = MibTableColumn
txpktsAll = _TxpktsAll_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 65),
    _TxpktsAll_Type()
)
txpktsAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txpktsAll.setStatus("current")
_RxoctetsAll_Type = Counter64
_RxoctetsAll_Object = MibTableColumn
rxoctetsAll = _RxoctetsAll_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 66),
    _RxoctetsAll_Type()
)
rxoctetsAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxoctetsAll.setStatus("current")
_RxpktsAll_Type = Counter64
_RxpktsAll_Object = MibTableColumn
rxpktsAll = _RxpktsAll_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3, 3, 1, 67),
    _RxpktsAll_Type()
)
rxpktsAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxpktsAll.setStatus("current")
_UbntAirMAX_ObjectIdentity = ObjectIdentity
ubntAirMAX = _UbntAirMAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4)
)
_UbntRadioTable_Object = MibTable
ubntRadioTable = _UbntRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ubntRadioTable.setStatus("current")
_UbntRadioEntry_Object = MibTableRow
ubntRadioEntry = _UbntRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1)
)
ubntRadioEntry.setIndexNames(
    (0, "UBNT-MIB", "ubntRadioIndex"),
)
if mibBuilder.loadTexts:
    ubntRadioEntry.setStatus("current")


class _UbntRadioIndex_Type(Integer32):
    """Custom type ubntRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntRadioIndex_Type.__name__ = "Integer32"
_UbntRadioIndex_Object = MibTableColumn
ubntRadioIndex = _UbntRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 1),
    _UbntRadioIndex_Type()
)
ubntRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntRadioIndex.setStatus("current")


class _UbntRadioMode_Type(Integer32):
    """Custom type ubntRadioMode based on Integer32"""
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
        *(("sta", 1),
          ("ap", 2),
          ("aprepeater", 3),
          ("apwds", 4))
    )


_UbntRadioMode_Type.__name__ = "Integer32"
_UbntRadioMode_Object = MibTableColumn
ubntRadioMode = _UbntRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 2),
    _UbntRadioMode_Type()
)
ubntRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioMode.setStatus("current")
_UbntRadioCCode_Type = Integer32
_UbntRadioCCode_Object = MibTableColumn
ubntRadioCCode = _UbntRadioCCode_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 3),
    _UbntRadioCCode_Type()
)
ubntRadioCCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioCCode.setStatus("current")


class _UbntRadioFreq_Type(Integer32):
    """Custom type ubntRadioFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UbntRadioFreq_Type.__name__ = "Integer32"
_UbntRadioFreq_Object = MibTableColumn
ubntRadioFreq = _UbntRadioFreq_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 4),
    _UbntRadioFreq_Type()
)
ubntRadioFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioFreq.setStatus("current")
_UbntRadioDfsEnabled_Type = TruthValue
_UbntRadioDfsEnabled_Object = MibTableColumn
ubntRadioDfsEnabled = _UbntRadioDfsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 5),
    _UbntRadioDfsEnabled_Type()
)
ubntRadioDfsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioDfsEnabled.setStatus("current")


class _UbntRadioTxPower_Type(Integer32):
    """Custom type ubntRadioTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UbntRadioTxPower_Type.__name__ = "Integer32"
_UbntRadioTxPower_Object = MibTableColumn
ubntRadioTxPower = _UbntRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 6),
    _UbntRadioTxPower_Type()
)
ubntRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioTxPower.setStatus("current")


class _UbntRadioDistance_Type(Integer32):
    """Custom type ubntRadioDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UbntRadioDistance_Type.__name__ = "Integer32"
_UbntRadioDistance_Object = MibTableColumn
ubntRadioDistance = _UbntRadioDistance_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 7),
    _UbntRadioDistance_Type()
)
ubntRadioDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioDistance.setStatus("current")


class _UbntRadioChainmask_Type(Integer32):
    """Custom type ubntRadioChainmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntRadioChainmask_Type.__name__ = "Integer32"
_UbntRadioChainmask_Object = MibTableColumn
ubntRadioChainmask = _UbntRadioChainmask_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 8),
    _UbntRadioChainmask_Type()
)
ubntRadioChainmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioChainmask.setStatus("current")
_UbntRadioAntenna_Type = DisplayString
_UbntRadioAntenna_Object = MibTableColumn
ubntRadioAntenna = _UbntRadioAntenna_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 9),
    _UbntRadioAntenna_Type()
)
ubntRadioAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioAntenna.setStatus("current")
_UbntRadioRssiTable_Object = MibTable
ubntRadioRssiTable = _UbntRadioRssiTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ubntRadioRssiTable.setStatus("current")
_UbntRadioRssiEntry_Object = MibTableRow
ubntRadioRssiEntry = _UbntRadioRssiEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1)
)
ubntRadioRssiEntry.setIndexNames(
    (0, "UBNT-MIB", "ubntRadioIndex"),
    (0, "UBNT-MIB", "ubntRadioRssiIndex"),
)
if mibBuilder.loadTexts:
    ubntRadioRssiEntry.setStatus("current")


class _UbntRadioRssiIndex_Type(Integer32):
    """Custom type ubntRadioRssiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntRadioRssiIndex_Type.__name__ = "Integer32"
_UbntRadioRssiIndex_Object = MibTableColumn
ubntRadioRssiIndex = _UbntRadioRssiIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 1),
    _UbntRadioRssiIndex_Type()
)
ubntRadioRssiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntRadioRssiIndex.setStatus("current")
_UbntRadioRssi_Type = Integer32
_UbntRadioRssi_Object = MibTableColumn
ubntRadioRssi = _UbntRadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 2),
    _UbntRadioRssi_Type()
)
ubntRadioRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioRssi.setStatus("current")
_UbntRadioRssiMgmt_Type = Integer32
_UbntRadioRssiMgmt_Object = MibTableColumn
ubntRadioRssiMgmt = _UbntRadioRssiMgmt_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 3),
    _UbntRadioRssiMgmt_Type()
)
ubntRadioRssiMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioRssiMgmt.setStatus("current")
_UbntRadioRssiExt_Type = Integer32
_UbntRadioRssiExt_Object = MibTableColumn
ubntRadioRssiExt = _UbntRadioRssiExt_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 4),
    _UbntRadioRssiExt_Type()
)
ubntRadioRssiExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioRssiExt.setStatus("current")
_UbntAirSyncTable_Object = MibTable
ubntAirSyncTable = _UbntAirSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ubntAirSyncTable.setStatus("current")
_UbntAirSyncEntry_Object = MibTableRow
ubntAirSyncEntry = _UbntAirSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1)
)
ubntAirSyncEntry.setIndexNames(
    (0, "UBNT-MIB", "ubntAirSyncIfIndex"),
)
if mibBuilder.loadTexts:
    ubntAirSyncEntry.setStatus("current")


class _UbntAirSyncIfIndex_Type(Integer32):
    """Custom type ubntAirSyncIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntAirSyncIfIndex_Type.__name__ = "Integer32"
_UbntAirSyncIfIndex_Object = MibTableColumn
ubntAirSyncIfIndex = _UbntAirSyncIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 1),
    _UbntAirSyncIfIndex_Type()
)
ubntAirSyncIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntAirSyncIfIndex.setStatus("current")


class _UbntAirSyncMode_Type(Integer32):
    """Custom type ubntAirSyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("master", 1),
          ("slave", 2))
    )


_UbntAirSyncMode_Type.__name__ = "Integer32"
_UbntAirSyncMode_Object = MibTableColumn
ubntAirSyncMode = _UbntAirSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 2),
    _UbntAirSyncMode_Type()
)
ubntAirSyncMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSyncMode.setStatus("current")


class _UbntAirSyncCount_Type(Integer32):
    """Custom type ubntAirSyncCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UbntAirSyncCount_Type.__name__ = "Integer32"
_UbntAirSyncCount_Object = MibTableColumn
ubntAirSyncCount = _UbntAirSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 3),
    _UbntAirSyncCount_Type()
)
ubntAirSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSyncCount.setStatus("current")


class _UbntAirSyncDownUtil_Type(Integer32):
    """Custom type ubntAirSyncDownUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UbntAirSyncDownUtil_Type.__name__ = "Integer32"
_UbntAirSyncDownUtil_Object = MibTableColumn
ubntAirSyncDownUtil = _UbntAirSyncDownUtil_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 4),
    _UbntAirSyncDownUtil_Type()
)
ubntAirSyncDownUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSyncDownUtil.setStatus("current")


class _UbntAirSyncUpUtil_Type(Integer32):
    """Custom type ubntAirSyncUpUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UbntAirSyncUpUtil_Type.__name__ = "Integer32"
_UbntAirSyncUpUtil_Object = MibTableColumn
ubntAirSyncUpUtil = _UbntAirSyncUpUtil_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 5),
    _UbntAirSyncUpUtil_Type()
)
ubntAirSyncUpUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSyncUpUtil.setStatus("current")
_UbntAirSelTable_Object = MibTable
ubntAirSelTable = _UbntAirSelTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ubntAirSelTable.setStatus("current")
_UbntAirSelEntry_Object = MibTableRow
ubntAirSelEntry = _UbntAirSelEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1)
)
ubntAirSelEntry.setIndexNames(
    (0, "UBNT-MIB", "ubntAirSelIfIndex"),
)
if mibBuilder.loadTexts:
    ubntAirSelEntry.setStatus("current")


class _UbntAirSelIfIndex_Type(Integer32):
    """Custom type ubntAirSelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntAirSelIfIndex_Type.__name__ = "Integer32"
_UbntAirSelIfIndex_Object = MibTableColumn
ubntAirSelIfIndex = _UbntAirSelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1, 1),
    _UbntAirSelIfIndex_Type()
)
ubntAirSelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntAirSelIfIndex.setStatus("current")
_UbntAirSelEnabled_Type = TruthValue
_UbntAirSelEnabled_Object = MibTableColumn
ubntAirSelEnabled = _UbntAirSelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1, 2),
    _UbntAirSelEnabled_Type()
)
ubntAirSelEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSelEnabled.setStatus("current")


class _UbntAirSelInterval_Type(Integer32):
    """Custom type ubntAirSelInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UbntAirSelInterval_Type.__name__ = "Integer32"
_UbntAirSelInterval_Object = MibTableColumn
ubntAirSelInterval = _UbntAirSelInterval_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1, 3),
    _UbntAirSelInterval_Type()
)
ubntAirSelInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSelInterval.setStatus("current")
_UbntWlStatTable_Object = MibTable
ubntWlStatTable = _UbntWlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5)
)
if mibBuilder.loadTexts:
    ubntWlStatTable.setStatus("current")
_UbntWlStatEntry_Object = MibTableRow
ubntWlStatEntry = _UbntWlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1)
)
ubntWlStatEntry.setIndexNames(
    (0, "UBNT-MIB", "ubntWlStatIndex"),
)
if mibBuilder.loadTexts:
    ubntWlStatEntry.setStatus("current")


class _UbntWlStatIndex_Type(Integer32):
    """Custom type ubntWlStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntWlStatIndex_Type.__name__ = "Integer32"
_UbntWlStatIndex_Object = MibTableColumn
ubntWlStatIndex = _UbntWlStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 1),
    _UbntWlStatIndex_Type()
)
ubntWlStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntWlStatIndex.setStatus("current")
_UbntWlStatSsid_Type = DisplayString
_UbntWlStatSsid_Object = MibTableColumn
ubntWlStatSsid = _UbntWlStatSsid_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 2),
    _UbntWlStatSsid_Type()
)
ubntWlStatSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatSsid.setStatus("current")
_UbntWlStatHideSsid_Type = TruthValue
_UbntWlStatHideSsid_Object = MibTableColumn
ubntWlStatHideSsid = _UbntWlStatHideSsid_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 3),
    _UbntWlStatHideSsid_Type()
)
ubntWlStatHideSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatHideSsid.setStatus("current")
_UbntWlStatApMac_Type = MacAddress
_UbntWlStatApMac_Object = MibTableColumn
ubntWlStatApMac = _UbntWlStatApMac_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 4),
    _UbntWlStatApMac_Type()
)
ubntWlStatApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatApMac.setStatus("current")
_UbntWlStatSignal_Type = Integer32
_UbntWlStatSignal_Object = MibTableColumn
ubntWlStatSignal = _UbntWlStatSignal_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 5),
    _UbntWlStatSignal_Type()
)
ubntWlStatSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatSignal.setStatus("current")
_UbntWlStatRssi_Type = Integer32
_UbntWlStatRssi_Object = MibTableColumn
ubntWlStatRssi = _UbntWlStatRssi_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 6),
    _UbntWlStatRssi_Type()
)
ubntWlStatRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatRssi.setStatus("current")
_UbntWlStatCcq_Type = Integer32
_UbntWlStatCcq_Object = MibTableColumn
ubntWlStatCcq = _UbntWlStatCcq_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 7),
    _UbntWlStatCcq_Type()
)
ubntWlStatCcq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatCcq.setStatus("current")
_UbntWlStatNoiseFloor_Type = Integer32
_UbntWlStatNoiseFloor_Object = MibTableColumn
ubntWlStatNoiseFloor = _UbntWlStatNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 8),
    _UbntWlStatNoiseFloor_Type()
)
ubntWlStatNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatNoiseFloor.setStatus("current")
_UbntWlStatTxRate_Type = Integer32
_UbntWlStatTxRate_Object = MibTableColumn
ubntWlStatTxRate = _UbntWlStatTxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 9),
    _UbntWlStatTxRate_Type()
)
ubntWlStatTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatTxRate.setStatus("current")
_UbntWlStatRxRate_Type = Integer32
_UbntWlStatRxRate_Object = MibTableColumn
ubntWlStatRxRate = _UbntWlStatRxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 10),
    _UbntWlStatRxRate_Type()
)
ubntWlStatRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatRxRate.setStatus("current")
_UbntWlStatSecurity_Type = DisplayString
_UbntWlStatSecurity_Object = MibTableColumn
ubntWlStatSecurity = _UbntWlStatSecurity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 11),
    _UbntWlStatSecurity_Type()
)
ubntWlStatSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatSecurity.setStatus("current")
_UbntWlStatWdsEnabled_Type = TruthValue
_UbntWlStatWdsEnabled_Object = MibTableColumn
ubntWlStatWdsEnabled = _UbntWlStatWdsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 12),
    _UbntWlStatWdsEnabled_Type()
)
ubntWlStatWdsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatWdsEnabled.setStatus("current")
_UbntWlStatApRepeater_Type = TruthValue
_UbntWlStatApRepeater_Object = MibTableColumn
ubntWlStatApRepeater = _UbntWlStatApRepeater_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 13),
    _UbntWlStatApRepeater_Type()
)
ubntWlStatApRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatApRepeater.setStatus("current")
_UbntWlStatChanWidth_Type = Integer32
_UbntWlStatChanWidth_Object = MibTableColumn
ubntWlStatChanWidth = _UbntWlStatChanWidth_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 14),
    _UbntWlStatChanWidth_Type()
)
ubntWlStatChanWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatChanWidth.setStatus("current")
_UbntWlStatStaCount_Type = Gauge32
_UbntWlStatStaCount_Object = MibTableColumn
ubntWlStatStaCount = _UbntWlStatStaCount_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 15),
    _UbntWlStatStaCount_Type()
)
ubntWlStatStaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatStaCount.setStatus("current")
_UbntAirMaxTable_Object = MibTable
ubntAirMaxTable = _UbntAirMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6)
)
if mibBuilder.loadTexts:
    ubntAirMaxTable.setStatus("current")
_UbntAirMaxEntry_Object = MibTableRow
ubntAirMaxEntry = _UbntAirMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1)
)
ubntAirMaxEntry.setIndexNames(
    (0, "UBNT-MIB", "ubntAirMaxIfIndex"),
)
if mibBuilder.loadTexts:
    ubntAirMaxEntry.setStatus("current")


class _UbntAirMaxIfIndex_Type(Integer32):
    """Custom type ubntAirMaxIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntAirMaxIfIndex_Type.__name__ = "Integer32"
_UbntAirMaxIfIndex_Object = MibTableColumn
ubntAirMaxIfIndex = _UbntAirMaxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 1),
    _UbntAirMaxIfIndex_Type()
)
ubntAirMaxIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntAirMaxIfIndex.setStatus("current")
_UbntAirMaxEnabled_Type = TruthValue
_UbntAirMaxEnabled_Object = MibTableColumn
ubntAirMaxEnabled = _UbntAirMaxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 2),
    _UbntAirMaxEnabled_Type()
)
ubntAirMaxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirMaxEnabled.setStatus("current")


class _UbntAirMaxQuality_Type(Integer32):
    """Custom type ubntAirMaxQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UbntAirMaxQuality_Type.__name__ = "Integer32"
_UbntAirMaxQuality_Object = MibTableColumn
ubntAirMaxQuality = _UbntAirMaxQuality_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 3),
    _UbntAirMaxQuality_Type()
)
ubntAirMaxQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirMaxQuality.setStatus("current")


class _UbntAirMaxCapacity_Type(Integer32):
    """Custom type ubntAirMaxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UbntAirMaxCapacity_Type.__name__ = "Integer32"
_UbntAirMaxCapacity_Object = MibTableColumn
ubntAirMaxCapacity = _UbntAirMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 4),
    _UbntAirMaxCapacity_Type()
)
ubntAirMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirMaxCapacity.setStatus("current")


class _UbntAirMaxPriority_Type(Integer32):
    """Custom type ubntAirMaxPriority based on Integer32"""
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
        *(("high", 0),
          ("medium", 1),
          ("low", 2),
          ("none", 3))
    )


_UbntAirMaxPriority_Type.__name__ = "Integer32"
_UbntAirMaxPriority_Object = MibTableColumn
ubntAirMaxPriority = _UbntAirMaxPriority_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 5),
    _UbntAirMaxPriority_Type()
)
ubntAirMaxPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirMaxPriority.setStatus("current")
_UbntAirMaxNoAck_Type = TruthValue
_UbntAirMaxNoAck_Object = MibTableColumn
ubntAirMaxNoAck = _UbntAirMaxNoAck_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 6),
    _UbntAirMaxNoAck_Type()
)
ubntAirMaxNoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirMaxNoAck.setStatus("current")
_UbntStaTable_Object = MibTable
ubntStaTable = _UbntStaTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7)
)
if mibBuilder.loadTexts:
    ubntStaTable.setStatus("current")
_UbntStaEntry_Object = MibTableRow
ubntStaEntry = _UbntStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1)
)
ubntStaEntry.setIndexNames(
    (0, "UBNT-MIB", "ubntWlStatIndex"),
    (0, "UBNT-MIB", "ubntStaMac"),
)
if mibBuilder.loadTexts:
    ubntStaEntry.setStatus("current")
_UbntStaMac_Type = MacAddress
_UbntStaMac_Object = MibTableColumn
ubntStaMac = _UbntStaMac_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 1),
    _UbntStaMac_Type()
)
ubntStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntStaMac.setStatus("current")
_UbntStaName_Type = DisplayString
_UbntStaName_Object = MibTableColumn
ubntStaName = _UbntStaName_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 2),
    _UbntStaName_Type()
)
ubntStaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaName.setStatus("current")
_UbntStaSignal_Type = Integer32
_UbntStaSignal_Object = MibTableColumn
ubntStaSignal = _UbntStaSignal_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 3),
    _UbntStaSignal_Type()
)
ubntStaSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaSignal.setStatus("current")
_UbntStaNoiseFloor_Type = Integer32
_UbntStaNoiseFloor_Object = MibTableColumn
ubntStaNoiseFloor = _UbntStaNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 4),
    _UbntStaNoiseFloor_Type()
)
ubntStaNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaNoiseFloor.setStatus("current")


class _UbntStaDistance_Type(Integer32):
    """Custom type ubntStaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UbntStaDistance_Type.__name__ = "Integer32"
_UbntStaDistance_Object = MibTableColumn
ubntStaDistance = _UbntStaDistance_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 5),
    _UbntStaDistance_Type()
)
ubntStaDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaDistance.setStatus("current")
_UbntStaCcq_Type = Integer32
_UbntStaCcq_Object = MibTableColumn
ubntStaCcq = _UbntStaCcq_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 6),
    _UbntStaCcq_Type()
)
ubntStaCcq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaCcq.setStatus("current")
_UbntStaAmp_Type = Integer32
_UbntStaAmp_Object = MibTableColumn
ubntStaAmp = _UbntStaAmp_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 7),
    _UbntStaAmp_Type()
)
ubntStaAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaAmp.setStatus("current")
_UbntStaAmq_Type = Integer32
_UbntStaAmq_Object = MibTableColumn
ubntStaAmq = _UbntStaAmq_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 8),
    _UbntStaAmq_Type()
)
ubntStaAmq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaAmq.setStatus("current")
_UbntStaAmc_Type = Integer32
_UbntStaAmc_Object = MibTableColumn
ubntStaAmc = _UbntStaAmc_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 9),
    _UbntStaAmc_Type()
)
ubntStaAmc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaAmc.setStatus("current")
_UbntStaLastIp_Type = IpAddress
_UbntStaLastIp_Object = MibTableColumn
ubntStaLastIp = _UbntStaLastIp_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 10),
    _UbntStaLastIp_Type()
)
ubntStaLastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaLastIp.setStatus("current")
_UbntStaTxRate_Type = Integer32
_UbntStaTxRate_Object = MibTableColumn
ubntStaTxRate = _UbntStaTxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 11),
    _UbntStaTxRate_Type()
)
ubntStaTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaTxRate.setStatus("current")
_UbntStaRxRate_Type = Integer32
_UbntStaRxRate_Object = MibTableColumn
ubntStaRxRate = _UbntStaRxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 12),
    _UbntStaRxRate_Type()
)
ubntStaRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaRxRate.setStatus("current")
_UbntStaTxBytes_Type = Counter64
_UbntStaTxBytes_Object = MibTableColumn
ubntStaTxBytes = _UbntStaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 13),
    _UbntStaTxBytes_Type()
)
ubntStaTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaTxBytes.setStatus("current")
_UbntStaRxBytes_Type = Counter64
_UbntStaRxBytes_Object = MibTableColumn
ubntStaRxBytes = _UbntStaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 14),
    _UbntStaRxBytes_Type()
)
ubntStaRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaRxBytes.setStatus("current")
_UbntStaConnTime_Type = TimeTicks
_UbntStaConnTime_Object = MibTableColumn
ubntStaConnTime = _UbntStaConnTime_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 15),
    _UbntStaConnTime_Type()
)
ubntStaConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaConnTime.setStatus("current")
_UbntEdgeMax_ObjectIdentity = ObjectIdentity
ubntEdgeMax = _UbntEdgeMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5)
)
_UbntUniFi_ObjectIdentity = ObjectIdentity
ubntUniFi = _UbntUniFi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6)
)
_UbntAirVision_ObjectIdentity = ObjectIdentity
ubntAirVision = _UbntAirVision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 7)
)
_UbntMFi_ObjectIdentity = ObjectIdentity
ubntMFi = _UbntMFi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 8)
)
_UbntUniTel_ObjectIdentity = ObjectIdentity
ubntUniTel = _UbntUniTel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 9)
)
_UbntAFLTU_ObjectIdentity = ObjectIdentity
ubntAFLTU = _UbntAFLTU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10)
)

# Managed Objects groups

ubntORInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 1, 1)
)
ubntORInfoGroup.setObjects(
      *(("UBNT-MIB", "ubntORID"),
        ("UBNT-MIB", "ubntORDescr"))
)
if mibBuilder.loadTexts:
    ubntORInfoGroup.setStatus("current")

ubntAirMAXStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 2, 1)
)
ubntAirMAXStatusGroup.setObjects(
      *(("UBNT-MIB", "ubntStaName"),
        ("UBNT-MIB", "ubntStaSignal"),
        ("UBNT-MIB", "ubntStaNoiseFloor"),
        ("UBNT-MIB", "ubntStaDistance"),
        ("UBNT-MIB", "ubntStaCcq"),
        ("UBNT-MIB", "ubntStaAmp"),
        ("UBNT-MIB", "ubntStaAmq"),
        ("UBNT-MIB", "ubntStaAmc"),
        ("UBNT-MIB", "ubntStaLastIp"),
        ("UBNT-MIB", "ubntStaTxRate"),
        ("UBNT-MIB", "ubntStaRxRate"),
        ("UBNT-MIB", "ubntStaTxBytes"),
        ("UBNT-MIB", "ubntStaRxBytes"),
        ("UBNT-MIB", "ubntStaConnTime"),
        ("UBNT-MIB", "ubntRadioMode"),
        ("UBNT-MIB", "ubntRadioCCode"),
        ("UBNT-MIB", "ubntRadioFreq"),
        ("UBNT-MIB", "ubntRadioDfsEnabled"),
        ("UBNT-MIB", "ubntRadioTxPower"),
        ("UBNT-MIB", "ubntRadioDistance"),
        ("UBNT-MIB", "ubntRadioChainmask"),
        ("UBNT-MIB", "ubntRadioAntenna"),
        ("UBNT-MIB", "ubntRadioRssi"),
        ("UBNT-MIB", "ubntRadioRssiMgmt"),
        ("UBNT-MIB", "ubntRadioRssiExt"),
        ("UBNT-MIB", "ubntAirMaxEnabled"),
        ("UBNT-MIB", "ubntAirMaxQuality"),
        ("UBNT-MIB", "ubntAirMaxCapacity"),
        ("UBNT-MIB", "ubntAirMaxPriority"),
        ("UBNT-MIB", "ubntAirMaxNoAck"),
        ("UBNT-MIB", "ubntAirSyncMode"),
        ("UBNT-MIB", "ubntAirSyncCount"),
        ("UBNT-MIB", "ubntAirSyncDownUtil"),
        ("UBNT-MIB", "ubntAirSyncUpUtil"),
        ("UBNT-MIB", "ubntAirSelEnabled"),
        ("UBNT-MIB", "ubntAirSelInterval"),
        ("UBNT-MIB", "ubntWlStatSsid"),
        ("UBNT-MIB", "ubntWlStatHideSsid"),
        ("UBNT-MIB", "ubntWlStatApMac"),
        ("UBNT-MIB", "ubntWlStatSignal"),
        ("UBNT-MIB", "ubntWlStatRssi"),
        ("UBNT-MIB", "ubntWlStatCcq"),
        ("UBNT-MIB", "ubntWlStatNoiseFloor"),
        ("UBNT-MIB", "ubntWlStatTxRate"),
        ("UBNT-MIB", "ubntWlStatRxRate"),
        ("UBNT-MIB", "ubntWlStatSecurity"),
        ("UBNT-MIB", "ubntWlStatWdsEnabled"),
        ("UBNT-MIB", "ubntWlStatApRepeater"),
        ("UBNT-MIB", "ubntWlStatChanWidth"),
        ("UBNT-MIB", "ubntWlStatStaCount"))
)
if mibBuilder.loadTexts:
    ubntAirMAXStatusGroup.setStatus("current")

ubntAirFiberStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 3, 1)
)
ubntAirFiberStatusGroup.setObjects(
      *(("UBNT-MIB", "radioEnable"),
        ("UBNT-MIB", "radioLinkMode"),
        ("UBNT-MIB", "radioDuplex"),
        ("UBNT-MIB", "txFrequency"),
        ("UBNT-MIB", "rxFrequency"),
        ("UBNT-MIB", "regDomain"),
        ("UBNT-MIB", "gpsSync"),
        ("UBNT-MIB", "txPower"),
        ("UBNT-MIB", "rxGain"),
        ("UBNT-MIB", "maxTxModRate"),
        ("UBNT-MIB", "modRateControl"),
        ("UBNT-MIB", "ethDPortLinkSpeed"),
        ("UBNT-MIB", "linkName"),
        ("UBNT-MIB", "encryptKey"),
        ("UBNT-MIB", "ethFlowControl"),
        ("UBNT-MIB", "ethMcastFilter"),
        ("UBNT-MIB", "ethTrackRFLink"),
        ("UBNT-MIB", "ethLinkOffDuration"),
        ("UBNT-MIB", "ethLinkOffSpacing"),
        ("UBNT-MIB", "txFrequency1"),
        ("UBNT-MIB", "rxFrequency1"),
        ("UBNT-MIB", "txFrequency2"),
        ("UBNT-MIB", "rxFrequency2"),
        ("UBNT-MIB", "txFrequency3"),
        ("UBNT-MIB", "rxFrequency3"),
        ("UBNT-MIB", "channelWidth"),
        ("UBNT-MIB", "txChannelWidth"),
        ("UBNT-MIB", "rxChannelWidth"),
        ("UBNT-MIB", "curTXModRate"),
        ("UBNT-MIB", "radioLinkDistFt"),
        ("UBNT-MIB", "radioLinkDistM"),
        ("UBNT-MIB", "rxCapacity"),
        ("UBNT-MIB", "txCapacity"),
        ("UBNT-MIB", "radio0TempC"),
        ("UBNT-MIB", "radio0TempF"),
        ("UBNT-MIB", "radio1TempC"),
        ("UBNT-MIB", "radio1TempF"),
        ("UBNT-MIB", "rxPower0"),
        ("UBNT-MIB", "rxPower0Valid"),
        ("UBNT-MIB", "rxOverload0"),
        ("UBNT-MIB", "rxPower1"),
        ("UBNT-MIB", "rxPower1Valid"),
        ("UBNT-MIB", "rxOverload1"),
        ("UBNT-MIB", "remoteTXPower"),
        ("UBNT-MIB", "remoteTXModRate"),
        ("UBNT-MIB", "remoteRXPower0"),
        ("UBNT-MIB", "remoteRXPower0Valid"),
        ("UBNT-MIB", "remoteRXPower0Overload"),
        ("UBNT-MIB", "remoteRXPower1"),
        ("UBNT-MIB", "remoteRXPower1Valid"),
        ("UBNT-MIB", "remoteRXPower1Overload"),
        ("UBNT-MIB", "countryCode"),
        ("UBNT-MIB", "radioLinkState"),
        ("UBNT-MIB", "ethDataPortState"),
        ("UBNT-MIB", "gpsPulse"),
        ("UBNT-MIB", "gpsFix"),
        ("UBNT-MIB", "gpsLat"),
        ("UBNT-MIB", "gpsLong"),
        ("UBNT-MIB", "gpsAltMeters"),
        ("UBNT-MIB", "gpsAltFeet"),
        ("UBNT-MIB", "gpsSatsVisible"),
        ("UBNT-MIB", "gpsSatsTracked"),
        ("UBNT-MIB", "gpsHDOP"),
        ("UBNT-MIB", "dfsState"),
        ("UBNT-MIB", "upTime"),
        ("UBNT-MIB", "dateTime"),
        ("UBNT-MIB", "fwVersion"),
        ("UBNT-MIB", "remoteRXGain"),
        ("UBNT-MIB", "radioLinkInfo"),
        ("UBNT-MIB", "ethDataPortInfo"),
        ("UBNT-MIB", "linkUpTime"),
        ("UBNT-MIB", "remoteMAC"),
        ("UBNT-MIB", "remoteIP"),
        ("UBNT-MIB", "dfsDetections"),
        ("UBNT-MIB", "dfsDomain"),
        ("UBNT-MIB", "dfsStateTxFreq1"),
        ("UBNT-MIB", "dfsStateTxFreq2"),
        ("UBNT-MIB", "dfsStateTxFreq3"),
        ("UBNT-MIB", "dfsTimerTxFreq1"),
        ("UBNT-MIB", "dfsTimerTxFreq2"),
        ("UBNT-MIB", "dfsTimerTxFreq3"),
        ("UBNT-MIB", "txFramesOK"),
        ("UBNT-MIB", "rxFramesOK"),
        ("UBNT-MIB", "rxFrameCrcErr"),
        ("UBNT-MIB", "rxAlignErr"),
        ("UBNT-MIB", "txOctetsOK"),
        ("UBNT-MIB", "rxOctetsOK"),
        ("UBNT-MIB", "txPauseFrames"),
        ("UBNT-MIB", "rxPauseFrames"),
        ("UBNT-MIB", "rxErroredFrames"),
        ("UBNT-MIB", "txErroredFrames"),
        ("UBNT-MIB", "rxValidUnicastFrames"),
        ("UBNT-MIB", "rxValidMulticastFrames"),
        ("UBNT-MIB", "rxValidBroadcastFrames"),
        ("UBNT-MIB", "txValidUnicastFrames"),
        ("UBNT-MIB", "txValidMulticastFrames"),
        ("UBNT-MIB", "txValidBroadcastFrames"),
        ("UBNT-MIB", "rxDroppedMacErrFrames"),
        ("UBNT-MIB", "rxTotalOctets"),
        ("UBNT-MIB", "rxTotalFrames"),
        ("UBNT-MIB", "rxLess64ByteFrames"),
        ("UBNT-MIB", "rxOverLengthFrames"),
        ("UBNT-MIB", "rx64BytePackets"),
        ("UBNT-MIB", "rx65-127BytePackets"),
        ("UBNT-MIB", "rx128-255BytePackets"),
        ("UBNT-MIB", "rx256-511BytePackets"),
        ("UBNT-MIB", "rx512-1023BytePackets"),
        ("UBNT-MIB", "rx1024-1518BytesPackets"),
        ("UBNT-MIB", "rx1519PlusBytePackets"),
        ("UBNT-MIB", "rxTooLongFrameCrcErr"),
        ("UBNT-MIB", "rxTooShortFrameCrcErr"),
        ("UBNT-MIB", "txqosoct0"),
        ("UBNT-MIB", "txqosoct1"),
        ("UBNT-MIB", "txqosoct2"),
        ("UBNT-MIB", "txqosoct3"),
        ("UBNT-MIB", "txqosoct4"),
        ("UBNT-MIB", "txqosoct5"),
        ("UBNT-MIB", "txqosoct6"),
        ("UBNT-MIB", "txqosoct7"),
        ("UBNT-MIB", "txqospkt0"),
        ("UBNT-MIB", "txqospkt1"),
        ("UBNT-MIB", "txqospkt2"),
        ("UBNT-MIB", "txqospkt3"),
        ("UBNT-MIB", "txqospkt4"),
        ("UBNT-MIB", "txqospkt5"),
        ("UBNT-MIB", "txqospkt6"),
        ("UBNT-MIB", "txqospkt7"),
        ("UBNT-MIB", "rxqosoct0"),
        ("UBNT-MIB", "rxqosoct1"),
        ("UBNT-MIB", "rxqosoct2"),
        ("UBNT-MIB", "rxqosoct3"),
        ("UBNT-MIB", "rxqosoct4"),
        ("UBNT-MIB", "rxqosoct5"),
        ("UBNT-MIB", "rxqosoct6"),
        ("UBNT-MIB", "rxqosoct7"),
        ("UBNT-MIB", "rxqospkt0"),
        ("UBNT-MIB", "rxqospkt1"),
        ("UBNT-MIB", "rxqospkt2"),
        ("UBNT-MIB", "rxqospkt3"),
        ("UBNT-MIB", "rxqospkt4"),
        ("UBNT-MIB", "rxqospkt5"),
        ("UBNT-MIB", "rxqospkt6"),
        ("UBNT-MIB", "rxqospkt7"),
        ("UBNT-MIB", "txoctetsAll"),
        ("UBNT-MIB", "txpktsAll"),
        ("UBNT-MIB", "rxoctetsAll"),
        ("UBNT-MIB", "rxpktsAll"))
)
if mibBuilder.loadTexts:
    ubntAirFiberStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ubntAirMAXStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 2, 2)
)
ubntAirMAXStatusCompliance.setObjects(
    ("UBNT-MIB", "ubntAirMAXStatusGroup")
)
if mibBuilder.loadTexts:
    ubntAirMAXStatusCompliance.setStatus(
        "current"
    )

ubntAirFiberStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 3, 2)
)
ubntAirFiberStatusCompliance.setObjects(
    ("UBNT-MIB", "ubntAirFiberStatusGroup")
)
if mibBuilder.loadTexts:
    ubntAirFiberStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBNT-MIB",
    **{"ubnt": ubnt,
       "ubntMIB": ubntMIB,
       "ubntORTable": ubntORTable,
       "ubntOREntry": ubntOREntry,
       "ubntORIndex": ubntORIndex,
       "ubntORID": ubntORID,
       "ubntORDescr": ubntORDescr,
       "ubntSnmpInfo": ubntSnmpInfo,
       "ubntSnmpGroups": ubntSnmpGroups,
       "ubntORInfoGroup": ubntORInfoGroup,
       "ubntAirosGroups": ubntAirosGroups,
       "ubntAirMAXStatusGroup": ubntAirMAXStatusGroup,
       "ubntAirMAXStatusCompliance": ubntAirMAXStatusCompliance,
       "ubntAirFiberGroups": ubntAirFiberGroups,
       "ubntAirFiberStatusGroup": ubntAirFiberStatusGroup,
       "ubntAirFiberStatusCompliance": ubntAirFiberStatusCompliance,
       "ubntEdgeMaxGroups": ubntEdgeMaxGroups,
       "ubntUniFiGroups": ubntUniFiGroups,
       "ubntAirVisionGroups": ubntAirVisionGroups,
       "ubntMFiGroups": ubntMFiGroups,
       "ubntUniTelGroups": ubntUniTelGroups,
       "ubntAFLTUGroups": ubntAFLTUGroups,
       "ubntAirFIBER": ubntAirFIBER,
       "airFiberConfig": airFiberConfig,
       "airFiberConfigEntry": airFiberConfigEntry,
       "airFiberConfigIndex": airFiberConfigIndex,
       "radioEnable": radioEnable,
       "radioLinkMode": radioLinkMode,
       "radioDuplex": radioDuplex,
       "txFrequency": txFrequency,
       "rxFrequency": rxFrequency,
       "regDomain": regDomain,
       "gpsSync": gpsSync,
       "txPower": txPower,
       "rxGain": rxGain,
       "maxTxModRate": maxTxModRate,
       "modRateControl": modRateControl,
       "ethDPortLinkSpeed": ethDPortLinkSpeed,
       "linkName": linkName,
       "encryptKey": encryptKey,
       "ethFlowControl": ethFlowControl,
       "ethMcastFilter": ethMcastFilter,
       "ethTrackRFLink": ethTrackRFLink,
       "ethLinkOffDuration": ethLinkOffDuration,
       "ethLinkOffSpacing": ethLinkOffSpacing,
       "txFrequency1": txFrequency1,
       "rxFrequency1": rxFrequency1,
       "txFrequency2": txFrequency2,
       "rxFrequency2": rxFrequency2,
       "txFrequency3": txFrequency3,
       "rxFrequency3": rxFrequency3,
       "channelWidth": channelWidth,
       "txChannelWidth": txChannelWidth,
       "rxChannelWidth": rxChannelWidth,
       "airFiberStatus": airFiberStatus,
       "airFiberStatusEntry": airFiberStatusEntry,
       "airFiberStatusIndex": airFiberStatusIndex,
       "curTXModRate": curTXModRate,
       "radioLinkDistFt": radioLinkDistFt,
       "radioLinkDistM": radioLinkDistM,
       "rxCapacity": rxCapacity,
       "txCapacity": txCapacity,
       "radio0TempF": radio0TempF,
       "radio0TempC": radio0TempC,
       "radio1TempF": radio1TempF,
       "radio1TempC": radio1TempC,
       "rxPower0": rxPower0,
       "rxPower0Valid": rxPower0Valid,
       "rxOverload0": rxOverload0,
       "rxPower1": rxPower1,
       "rxPower1Valid": rxPower1Valid,
       "rxOverload1": rxOverload1,
       "remoteTXPower": remoteTXPower,
       "remoteTXModRate": remoteTXModRate,
       "remoteRXPower0": remoteRXPower0,
       "remoteRXPower0Valid": remoteRXPower0Valid,
       "remoteRXPower0Overload": remoteRXPower0Overload,
       "remoteRXPower1": remoteRXPower1,
       "remoteRXPower1Valid": remoteRXPower1Valid,
       "remoteRXPower1Overload": remoteRXPower1Overload,
       "countryCode": countryCode,
       "radioLinkState": radioLinkState,
       "ethDataPortState": ethDataPortState,
       "gpsPulse": gpsPulse,
       "gpsFix": gpsFix,
       "gpsLat": gpsLat,
       "gpsLong": gpsLong,
       "gpsAltMeters": gpsAltMeters,
       "gpsAltFeet": gpsAltFeet,
       "gpsSatsVisible": gpsSatsVisible,
       "gpsSatsTracked": gpsSatsTracked,
       "gpsHDOP": gpsHDOP,
       "dfsState": dfsState,
       "upTime": upTime,
       "dateTime": dateTime,
       "fwVersion": fwVersion,
       "remoteRXGain": remoteRXGain,
       "radioLinkInfo": radioLinkInfo,
       "ethDataPortInfo": ethDataPortInfo,
       "linkUpTime": linkUpTime,
       "remoteMAC": remoteMAC,
       "remoteIP": remoteIP,
       "dfsDetections": dfsDetections,
       "dfsDomain": dfsDomain,
       "dfsStateTxFreq1": dfsStateTxFreq1,
       "dfsStateTxFreq2": dfsStateTxFreq2,
       "dfsStateTxFreq3": dfsStateTxFreq3,
       "dfsTimerTxFreq1": dfsTimerTxFreq1,
       "dfsTimerTxFreq2": dfsTimerTxFreq2,
       "dfsTimerTxFreq3": dfsTimerTxFreq3,
       "airFiberStatistics": airFiberStatistics,
       "airFiberStatisticsEntry": airFiberStatisticsEntry,
       "airFiberStatisticsIndex": airFiberStatisticsIndex,
       "txFramesOK": txFramesOK,
       "rxFramesOK": rxFramesOK,
       "rxFrameCrcErr": rxFrameCrcErr,
       "rxAlignErr": rxAlignErr,
       "txOctetsOK": txOctetsOK,
       "rxOctetsOK": rxOctetsOK,
       "txPauseFrames": txPauseFrames,
       "rxPauseFrames": rxPauseFrames,
       "rxErroredFrames": rxErroredFrames,
       "txErroredFrames": txErroredFrames,
       "rxValidUnicastFrames": rxValidUnicastFrames,
       "rxValidMulticastFrames": rxValidMulticastFrames,
       "rxValidBroadcastFrames": rxValidBroadcastFrames,
       "txValidUnicastFrames": txValidUnicastFrames,
       "txValidMulticastFrames": txValidMulticastFrames,
       "txValidBroadcastFrames": txValidBroadcastFrames,
       "rxDroppedMacErrFrames": rxDroppedMacErrFrames,
       "rxTotalOctets": rxTotalOctets,
       "rxTotalFrames": rxTotalFrames,
       "rxLess64ByteFrames": rxLess64ByteFrames,
       "rxOverLengthFrames": rxOverLengthFrames,
       "rx64BytePackets": rx64BytePackets,
       "rx65-127BytePackets": rx65_127BytePackets,
       "rx128-255BytePackets": rx128_255BytePackets,
       "rx256-511BytePackets": rx256_511BytePackets,
       "rx512-1023BytePackets": rx512_1023BytePackets,
       "rx1024-1518BytesPackets": rx1024_1518BytesPackets,
       "rx1519PlusBytePackets": rx1519PlusBytePackets,
       "rxTooLongFrameCrcErr": rxTooLongFrameCrcErr,
       "rxTooShortFrameCrcErr": rxTooShortFrameCrcErr,
       "txqosoct0": txqosoct0,
       "txqosoct1": txqosoct1,
       "txqosoct2": txqosoct2,
       "txqosoct3": txqosoct3,
       "txqosoct4": txqosoct4,
       "txqosoct5": txqosoct5,
       "txqosoct6": txqosoct6,
       "txqosoct7": txqosoct7,
       "txqospkt0": txqospkt0,
       "txqospkt1": txqospkt1,
       "txqospkt2": txqospkt2,
       "txqospkt3": txqospkt3,
       "txqospkt4": txqospkt4,
       "txqospkt5": txqospkt5,
       "txqospkt6": txqospkt6,
       "txqospkt7": txqospkt7,
       "rxqosoct0": rxqosoct0,
       "rxqosoct1": rxqosoct1,
       "rxqosoct2": rxqosoct2,
       "rxqosoct3": rxqosoct3,
       "rxqosoct4": rxqosoct4,
       "rxqosoct5": rxqosoct5,
       "rxqosoct6": rxqosoct6,
       "rxqosoct7": rxqosoct7,
       "rxqospkt0": rxqospkt0,
       "rxqospkt1": rxqospkt1,
       "rxqospkt2": rxqospkt2,
       "rxqospkt3": rxqospkt3,
       "rxqospkt4": rxqospkt4,
       "rxqospkt5": rxqospkt5,
       "rxqospkt6": rxqospkt6,
       "rxqospkt7": rxqospkt7,
       "txoctetsAll": txoctetsAll,
       "txpktsAll": txpktsAll,
       "rxoctetsAll": rxoctetsAll,
       "rxpktsAll": rxpktsAll,
       "ubntAirMAX": ubntAirMAX,
       "ubntRadioTable": ubntRadioTable,
       "ubntRadioEntry": ubntRadioEntry,
       "ubntRadioIndex": ubntRadioIndex,
       "ubntRadioMode": ubntRadioMode,
       "ubntRadioCCode": ubntRadioCCode,
       "ubntRadioFreq": ubntRadioFreq,
       "ubntRadioDfsEnabled": ubntRadioDfsEnabled,
       "ubntRadioTxPower": ubntRadioTxPower,
       "ubntRadioDistance": ubntRadioDistance,
       "ubntRadioChainmask": ubntRadioChainmask,
       "ubntRadioAntenna": ubntRadioAntenna,
       "ubntRadioRssiTable": ubntRadioRssiTable,
       "ubntRadioRssiEntry": ubntRadioRssiEntry,
       "ubntRadioRssiIndex": ubntRadioRssiIndex,
       "ubntRadioRssi": ubntRadioRssi,
       "ubntRadioRssiMgmt": ubntRadioRssiMgmt,
       "ubntRadioRssiExt": ubntRadioRssiExt,
       "ubntAirSyncTable": ubntAirSyncTable,
       "ubntAirSyncEntry": ubntAirSyncEntry,
       "ubntAirSyncIfIndex": ubntAirSyncIfIndex,
       "ubntAirSyncMode": ubntAirSyncMode,
       "ubntAirSyncCount": ubntAirSyncCount,
       "ubntAirSyncDownUtil": ubntAirSyncDownUtil,
       "ubntAirSyncUpUtil": ubntAirSyncUpUtil,
       "ubntAirSelTable": ubntAirSelTable,
       "ubntAirSelEntry": ubntAirSelEntry,
       "ubntAirSelIfIndex": ubntAirSelIfIndex,
       "ubntAirSelEnabled": ubntAirSelEnabled,
       "ubntAirSelInterval": ubntAirSelInterval,
       "ubntWlStatTable": ubntWlStatTable,
       "ubntWlStatEntry": ubntWlStatEntry,
       "ubntWlStatIndex": ubntWlStatIndex,
       "ubntWlStatSsid": ubntWlStatSsid,
       "ubntWlStatHideSsid": ubntWlStatHideSsid,
       "ubntWlStatApMac": ubntWlStatApMac,
       "ubntWlStatSignal": ubntWlStatSignal,
       "ubntWlStatRssi": ubntWlStatRssi,
       "ubntWlStatCcq": ubntWlStatCcq,
       "ubntWlStatNoiseFloor": ubntWlStatNoiseFloor,
       "ubntWlStatTxRate": ubntWlStatTxRate,
       "ubntWlStatRxRate": ubntWlStatRxRate,
       "ubntWlStatSecurity": ubntWlStatSecurity,
       "ubntWlStatWdsEnabled": ubntWlStatWdsEnabled,
       "ubntWlStatApRepeater": ubntWlStatApRepeater,
       "ubntWlStatChanWidth": ubntWlStatChanWidth,
       "ubntWlStatStaCount": ubntWlStatStaCount,
       "ubntAirMaxTable": ubntAirMaxTable,
       "ubntAirMaxEntry": ubntAirMaxEntry,
       "ubntAirMaxIfIndex": ubntAirMaxIfIndex,
       "ubntAirMaxEnabled": ubntAirMaxEnabled,
       "ubntAirMaxQuality": ubntAirMaxQuality,
       "ubntAirMaxCapacity": ubntAirMaxCapacity,
       "ubntAirMaxPriority": ubntAirMaxPriority,
       "ubntAirMaxNoAck": ubntAirMaxNoAck,
       "ubntStaTable": ubntStaTable,
       "ubntStaEntry": ubntStaEntry,
       "ubntStaMac": ubntStaMac,
       "ubntStaName": ubntStaName,
       "ubntStaSignal": ubntStaSignal,
       "ubntStaNoiseFloor": ubntStaNoiseFloor,
       "ubntStaDistance": ubntStaDistance,
       "ubntStaCcq": ubntStaCcq,
       "ubntStaAmp": ubntStaAmp,
       "ubntStaAmq": ubntStaAmq,
       "ubntStaAmc": ubntStaAmc,
       "ubntStaLastIp": ubntStaLastIp,
       "ubntStaTxRate": ubntStaTxRate,
       "ubntStaRxRate": ubntStaRxRate,
       "ubntStaTxBytes": ubntStaTxBytes,
       "ubntStaRxBytes": ubntStaRxBytes,
       "ubntStaConnTime": ubntStaConnTime,
       "ubntEdgeMax": ubntEdgeMax,
       "ubntUniFi": ubntUniFi,
       "ubntAirVision": ubntAirVision,
       "ubntMFi": ubntMFi,
       "ubntUniTel": ubntUniTel,
       "ubntAFLTU": ubntAFLTU}
)
