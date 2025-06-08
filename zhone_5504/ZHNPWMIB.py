# SNMP MIB module (ZHNPWMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zhone_5504/ZHNPWMIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:24:44 2025
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

(IANAPwCapabilities,
 IANAPwPsnTypeTC,
 IANAPwTypeTC) = mibBuilder.importSymbols(
    "IANA-PWE3-MIB",
    "IANAPwCapabilities",
    "IANAPwPsnTypeTC",
    "IANAPwTypeTC")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PwIndexOrZeroType,
 PwIndexType,
 PwVlanCfg) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwIndexOrZeroType",
    "PwIndexType",
    "PwVlanCfg")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")


# MODULE-IDENTITY

zhnPwMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31)
)
if mibBuilder.loadTexts:
    zhnPwMib.setRevisions(
        ("2012-05-16 12:00",
         "2012-01-27 12:00",
         "2011-08-29 00:00",
         "2008-11-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PwClearStatisticsTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("clear", 1))
    )



# MIB Managed Objects in the order of their OIDs

_ZhnPwNotifications_ObjectIdentity = ObjectIdentity
zhnPwNotifications = _ZhnPwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 0)
)
_ZhnPwObjects_ObjectIdentity = ObjectIdentity
zhnPwObjects = _ZhnPwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1)
)
_ZhnPwTable_Object = MibTable
zhnPwTable = _ZhnPwTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1)
)
if mibBuilder.loadTexts:
    zhnPwTable.setStatus("current")
_ZhnPwEntry_Object = MibTableRow
zhnPwEntry = _ZhnPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1)
)
zhnPwEntry.setIndexNames(
    (0, "ZHNPWMIB", "zhnPwIndex"),
)
if mibBuilder.loadTexts:
    zhnPwEntry.setStatus("current")
_ZhnPwIndex_Type = PwIndexType
_ZhnPwIndex_Object = MibTableColumn
zhnPwIndex = _ZhnPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 1),
    _ZhnPwIndex_Type()
)
zhnPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhnPwIndex.setStatus("current")


class _ZhnPwVlanID_Type(PwVlanCfg):
    """Custom type zhnPwVlanID based on PwVlanCfg"""
    defaultValue = 0


_ZhnPwVlanID_Type.__name__ = "PwVlanCfg"
_ZhnPwVlanID_Object = MibTableColumn
zhnPwVlanID = _ZhnPwVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 2),
    _ZhnPwVlanID_Type()
)
zhnPwVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnPwVlanID.setStatus("current")


class _ZhnPwVlanPriority_Type(Unsigned32):
    """Custom type zhnPwVlanPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZhnPwVlanPriority_Type.__name__ = "Unsigned32"
_ZhnPwVlanPriority_Object = MibTableColumn
zhnPwVlanPriority = _ZhnPwVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 3),
    _ZhnPwVlanPriority_Type()
)
zhnPwVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnPwVlanPriority.setStatus("current")
_ZhnPwPeerMask_Type = IpAddress
_ZhnPwPeerMask_Object = MibTableColumn
zhnPwPeerMask = _ZhnPwPeerMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 4),
    _ZhnPwPeerMask_Type()
)
zhnPwPeerMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnPwPeerMask.setStatus("current")
_ZhnPwPeerGateway_Type = IpAddress
_ZhnPwPeerGateway_Object = MibTableColumn
zhnPwPeerGateway = _ZhnPwPeerGateway_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 5),
    _ZhnPwPeerGateway_Type()
)
zhnPwPeerGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnPwPeerGateway.setStatus("current")
_ZhnPwPeerMAC_Type = MacAddress
_ZhnPwPeerMAC_Object = MibTableColumn
zhnPwPeerMAC = _ZhnPwPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 6),
    _ZhnPwPeerMAC_Type()
)
zhnPwPeerMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnPwPeerMAC.setStatus("current")
_ZhnPwMappedIfName_Type = SnmpAdminString
_ZhnPwMappedIfName_Object = MibTableColumn
zhnPwMappedIfName = _ZhnPwMappedIfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 7),
    _ZhnPwMappedIfName_Type()
)
zhnPwMappedIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhnPwMappedIfName.setStatus("current")


class _ZhnPwLocalLMBits_Type(Integer32):
    """Custom type zhnPwLocalLMBits based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("noDefect", 0),
          ("reserved1", 1),
          ("rxRDI", 2),
          ("nonTDMData", 3),
          ("txAIS", 4),
          ("reserved2", 5),
          ("reserved3", 6),
          ("reserved4", 7))
    )


_ZhnPwLocalLMBits_Type.__name__ = "Integer32"
_ZhnPwLocalLMBits_Object = MibTableColumn
zhnPwLocalLMBits = _ZhnPwLocalLMBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 8),
    _ZhnPwLocalLMBits_Type()
)
zhnPwLocalLMBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnPwLocalLMBits.setStatus("current")


class _ZhnPwLocalRBit_Type(Integer32):
    """Custom type zhnPwLocalRBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ZhnPwLocalRBit_Type.__name__ = "Integer32"
_ZhnPwLocalRBit_Object = MibTableColumn
zhnPwLocalRBit = _ZhnPwLocalRBit_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 9),
    _ZhnPwLocalRBit_Type()
)
zhnPwLocalRBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnPwLocalRBit.setStatus("current")


class _ZhnPwRemoteLMBits_Type(Integer32):
    """Custom type zhnPwRemoteLMBits based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("noDefect", 0),
          ("reserved1", 1),
          ("rxRDI", 2),
          ("nonTDMData", 3),
          ("txAIS", 4),
          ("reserved2", 5),
          ("reserved3", 6),
          ("reserved4", 7))
    )


_ZhnPwRemoteLMBits_Type.__name__ = "Integer32"
_ZhnPwRemoteLMBits_Object = MibTableColumn
zhnPwRemoteLMBits = _ZhnPwRemoteLMBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 10),
    _ZhnPwRemoteLMBits_Type()
)
zhnPwRemoteLMBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnPwRemoteLMBits.setStatus("current")


class _ZhnPwRemoteRBit_Type(Integer32):
    """Custom type zhnPwRemoteRBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ZhnPwRemoteRBit_Type.__name__ = "Integer32"
_ZhnPwRemoteRBit_Object = MibTableColumn
zhnPwRemoteRBit = _ZhnPwRemoteRBit_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 11),
    _ZhnPwRemoteRBit_Type()
)
zhnPwRemoteRBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnPwRemoteRBit.setStatus("current")


class _ZhnPwPeerMACMode_Type(Integer32):
    """Custom type zhnPwPeerMACMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_ZhnPwPeerMACMode_Type.__name__ = "Integer32"
_ZhnPwPeerMACMode_Object = MibTableColumn
zhnPwPeerMACMode = _ZhnPwPeerMACMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 12),
    _ZhnPwPeerMACMode_Type()
)
zhnPwPeerMACMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwPeerMACMode.setStatus("current")


class _ZhnPwActualPayloadSize_Type(Unsigned32):
    """Custom type zhnPwActualPayloadSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhnPwActualPayloadSize_Type.__name__ = "Unsigned32"
_ZhnPwActualPayloadSize_Object = MibTableColumn
zhnPwActualPayloadSize = _ZhnPwActualPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 13),
    _ZhnPwActualPayloadSize_Type()
)
zhnPwActualPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnPwActualPayloadSize.setStatus("current")


class _ZhnPwRxRaiAction_Type(Integer32):
    """Custom type zhnPwRxRaiAction based on Integer32"""
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
        *(("none", 1),
          ("txAIS", 2),
          ("txRAI", 3),
          ("txChlIdle", 4))
    )


_ZhnPwRxRaiAction_Type.__name__ = "Integer32"
_ZhnPwRxRaiAction_Object = MibTableColumn
zhnPwRxRaiAction = _ZhnPwRxRaiAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 14),
    _ZhnPwRxRaiAction_Type()
)
zhnPwRxRaiAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwRxRaiAction.setStatus("current")


class _ZhnPwRxAisAction_Type(Integer32):
    """Custom type zhnPwRxAisAction based on Integer32"""
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
        *(("none", 1),
          ("txAIS", 2),
          ("txRAI", 3),
          ("txChlIdle", 4))
    )


_ZhnPwRxAisAction_Type.__name__ = "Integer32"
_ZhnPwRxAisAction_Object = MibTableColumn
zhnPwRxAisAction = _ZhnPwRxAisAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 15),
    _ZhnPwRxAisAction_Type()
)
zhnPwRxAisAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwRxAisAction.setStatus("current")


class _ZhnPwLopAction_Type(Integer32):
    """Custom type zhnPwLopAction based on Integer32"""
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
        *(("none", 1),
          ("txAIS", 2),
          ("txRAI", 3),
          ("txChlIdle", 4))
    )


_ZhnPwLopAction_Type.__name__ = "Integer32"
_ZhnPwLopAction_Object = MibTableColumn
zhnPwLopAction = _ZhnPwLopAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 16),
    _ZhnPwLopAction_Type()
)
zhnPwLopAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwLopAction.setStatus("current")


class _ZhnPwAdaptState_Type(Integer32):
    """Custom type zhnPwAdaptState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("acquisition", 2),
          ("tracking1", 3),
          ("tracking2", 4),
          ("locked", 5),
          ("recovery", 6),
          ("restart", 7),
          ("disabled", 8))
    )


_ZhnPwAdaptState_Type.__name__ = "Integer32"
_ZhnPwAdaptState_Object = MibTableColumn
zhnPwAdaptState = _ZhnPwAdaptState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 17),
    _ZhnPwAdaptState_Type()
)
zhnPwAdaptState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwAdaptState.setStatus("current")


class _ZhnPwAdaptTime_Type(Integer32):
    """Custom type zhnPwAdaptTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhnPwAdaptTime_Type.__name__ = "Integer32"
_ZhnPwAdaptTime_Object = MibTableColumn
zhnPwAdaptTime = _ZhnPwAdaptTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 18),
    _ZhnPwAdaptTime_Type()
)
zhnPwAdaptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnPwAdaptTime.setStatus("current")


class _ZhnPwIsdn_Type(Integer32):
    """Custom type zhnPwIsdn based on Integer32"""
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
          ("lt", 2),
          ("nt1", 3))
    )


_ZhnPwIsdn_Type.__name__ = "Integer32"
_ZhnPwIsdn_Object = MibTableColumn
zhnPwIsdn = _ZhnPwIsdn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 19),
    _ZhnPwIsdn_Type()
)
zhnPwIsdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwIsdn.setStatus("current")


class _ZhnPwOuterLabel_Type(Unsigned32):
    """Custom type zhnPwOuterLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhnPwOuterLabel_Type.__name__ = "Unsigned32"
_ZhnPwOuterLabel_Object = MibTableColumn
zhnPwOuterLabel = _ZhnPwOuterLabel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 20),
    _ZhnPwOuterLabel_Type()
)
zhnPwOuterLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwOuterLabel.setStatus("current")


class _ZhnPwClkAcquisitionLevel_Type(Unsigned32):
    """Custom type zhnPwClkAcquisitionLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZhnPwClkAcquisitionLevel_Type.__name__ = "Unsigned32"
_ZhnPwClkAcquisitionLevel_Object = MibTableColumn
zhnPwClkAcquisitionLevel = _ZhnPwClkAcquisitionLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 21),
    _ZhnPwClkAcquisitionLevel_Type()
)
zhnPwClkAcquisitionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnPwClkAcquisitionLevel.setStatus("current")
_ZhnPwClearTotalStats_Type = PwClearStatisticsTC
_ZhnPwClearTotalStats_Object = MibTableColumn
zhnPwClearTotalStats = _ZhnPwClearTotalStats_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 1, 1, 22),
    _ZhnPwClearTotalStats_Type()
)
zhnPwClearTotalStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwClearTotalStats.setStatus("current")


class _ZhnPwRtpHeaderMode_Type(Integer32):
    """Custom type zhnPwRtpHeaderMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZhnPwRtpHeaderMode_Type.__name__ = "Integer32"
_ZhnPwRtpHeaderMode_Object = MibScalar
zhnPwRtpHeaderMode = _ZhnPwRtpHeaderMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 2),
    _ZhnPwRtpHeaderMode_Type()
)
zhnPwRtpHeaderMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwRtpHeaderMode.setStatus("current")


class _ZhnPwAdaptPllMode_Type(Integer32):
    """Custom type zhnPwAdaptPllMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fine", 2))
    )


_ZhnPwAdaptPllMode_Type.__name__ = "Integer32"
_ZhnPwAdaptPllMode_Object = MibScalar
zhnPwAdaptPllMode = _ZhnPwAdaptPllMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 3),
    _ZhnPwAdaptPllMode_Type()
)
zhnPwAdaptPllMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwAdaptPllMode.setStatus("current")


class _ZhnPwAutoAdclEnable_Type(Integer32):
    """Custom type zhnPwAutoAdclEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZhnPwAutoAdclEnable_Type.__name__ = "Integer32"
_ZhnPwAutoAdclEnable_Object = MibScalar
zhnPwAutoAdclEnable = _ZhnPwAutoAdclEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 4),
    _ZhnPwAutoAdclEnable_Type()
)
zhnPwAutoAdclEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwAutoAdclEnable.setStatus("current")
_ZhnPwAdaptSourceActual_Type = DisplayString
_ZhnPwAdaptSourceActual_Object = MibScalar
zhnPwAdaptSourceActual = _ZhnPwAdaptSourceActual_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 5),
    _ZhnPwAdaptSourceActual_Type()
)
zhnPwAdaptSourceActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnPwAdaptSourceActual.setStatus("current")
_ZhnPwSourceIPAddr_Type = IpAddress
_ZhnPwSourceIPAddr_Object = MibScalar
zhnPwSourceIPAddr = _ZhnPwSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 6),
    _ZhnPwSourceIPAddr_Type()
)
zhnPwSourceIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwSourceIPAddr.setStatus("current")
_ZhnPwSourceIPMask_Type = IpAddress
_ZhnPwSourceIPMask_Object = MibScalar
zhnPwSourceIPMask = _ZhnPwSourceIPMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 7),
    _ZhnPwSourceIPMask_Type()
)
zhnPwSourceIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwSourceIPMask.setStatus("current")
_ZhnPwSourceGateway_Type = IpAddress
_ZhnPwSourceGateway_Object = MibScalar
zhnPwSourceGateway = _ZhnPwSourceGateway_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 8),
    _ZhnPwSourceGateway_Type()
)
zhnPwSourceGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwSourceGateway.setStatus("current")


class _ZhnPwUdpDstPort_Type(Unsigned32):
    """Custom type zhnPwUdpDstPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZhnPwUdpDstPort_Type.__name__ = "Unsigned32"
_ZhnPwUdpDstPort_Object = MibScalar
zhnPwUdpDstPort = _ZhnPwUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 9),
    _ZhnPwUdpDstPort_Type()
)
zhnPwUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwUdpDstPort.setStatus("current")


class _ZhnPwT1E1Mode_Type(Integer32):
    """Custom type zhnPwT1E1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1", 1),
          ("e1", 2))
    )


_ZhnPwT1E1Mode_Type.__name__ = "Integer32"
_ZhnPwT1E1Mode_Object = MibScalar
zhnPwT1E1Mode = _ZhnPwT1E1Mode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 10),
    _ZhnPwT1E1Mode_Type()
)
zhnPwT1E1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPwT1E1Mode.setStatus("current")
_ZhnPeerPingName_Type = SnmpAdminString
_ZhnPeerPingName_Object = MibScalar
zhnPeerPingName = _ZhnPeerPingName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 11),
    _ZhnPeerPingName_Type()
)
zhnPeerPingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPeerPingName.setStatus("current")


class _ZhnPeerPingRequest_Type(Integer32):
    """Custom type zhnPeerPingRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("nop", 3))
    )


_ZhnPeerPingRequest_Type.__name__ = "Integer32"
_ZhnPeerPingRequest_Object = MibScalar
zhnPeerPingRequest = _ZhnPeerPingRequest_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 12),
    _ZhnPeerPingRequest_Type()
)
zhnPeerPingRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPeerPingRequest.setStatus("current")


class _ZhnPeerPingStatus_Type(Integer32):
    """Custom type zhnPeerPingStatus based on Integer32"""
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
        *(("reply", 1),
          ("timedout", 2),
          ("none", 3),
          ("unconfigured", 4),
          ("failed", 5))
    )


_ZhnPeerPingStatus_Type.__name__ = "Integer32"
_ZhnPeerPingStatus_Object = MibScalar
zhnPeerPingStatus = _ZhnPeerPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 1, 13),
    _ZhnPeerPingStatus_Type()
)
zhnPeerPingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnPeerPingStatus.setStatus("current")
_ZhnPwConformance_ObjectIdentity = ObjectIdentity
zhnPwConformance = _ZhnPwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 2)
)
_ZhnPwMibConformance_ObjectIdentity = ObjectIdentity
zhnPwMibConformance = _ZhnPwMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 2)
)
_ZhnPwMibGroups_ObjectIdentity = ObjectIdentity
zhnPwMibGroups = _ZhnPwMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 2, 1)
)
_ZhnPwMibCompliances_ObjectIdentity = ObjectIdentity
zhnPwMibCompliances = _ZhnPwMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 2, 2)
)

# Managed Objects groups

zhnPwMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 2, 1, 1)
)
zhnPwMibGroup.setObjects(
      *(("ZHNPWMIB", "zhnPwVlanID"),
        ("ZHNPWMIB", "zhnPwVlanPriority"),
        ("ZHNPWMIB", "zhnPwPeerMask"),
        ("ZHNPWMIB", "zhnPwPeerGateway"),
        ("ZHNPWMIB", "zhnPwPeerMAC"),
        ("ZHNPWMIB", "zhnPwMappedIfName"),
        ("ZHNPWMIB", "zhnPwLocalLMBits"),
        ("ZHNPWMIB", "zhnPwLocalRBit"),
        ("ZHNPWMIB", "zhnPwRemoteLMBits"),
        ("ZHNPWMIB", "zhnPwRemoteRBit"),
        ("ZHNPWMIB", "zhnPwPeerMACMode"),
        ("ZHNPWMIB", "zhnPwActualPayloadSize"),
        ("ZHNPWMIB", "zhnPwRxRaiAction"),
        ("ZHNPWMIB", "zhnPwRxAisAction"),
        ("ZHNPWMIB", "zhnPwLopAction"),
        ("ZHNPWMIB", "zhnPwAdaptState"),
        ("ZHNPWMIB", "zhnPwAdaptTime"),
        ("ZHNPWMIB", "zhnPwIsdn"),
        ("ZHNPWMIB", "zhnPwOuterLabel"),
        ("ZHNPWMIB", "zhnPwClkAcquisitionLevel"),
        ("ZHNPWMIB", "zhnPwClearTotalStats"))
)
if mibBuilder.loadTexts:
    zhnPwMibGroup.setStatus("current")

zhnPwMibScalars = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 2, 1, 2)
)
zhnPwMibScalars.setObjects(
      *(("ZHNPWMIB", "zhnPwRtpHeaderMode"),
        ("ZHNPWMIB", "zhnPwAdaptPllMode"),
        ("ZHNPWMIB", "zhnPwAutoAdclEnable"),
        ("ZHNPWMIB", "zhnPwAdaptSourceActual"),
        ("ZHNPWMIB", "zhnPwSourceIPAddr"),
        ("ZHNPWMIB", "zhnPwSourceIPMask"),
        ("ZHNPWMIB", "zhnPwSourceGateway"),
        ("ZHNPWMIB", "zhnPwUdpDstPort"),
        ("ZHNPWMIB", "zhnPwT1E1Mode"),
        ("ZHNPWMIB", "zhnPeerPingName"),
        ("ZHNPWMIB", "zhnPeerPingRequest"),
        ("ZHNPWMIB", "zhnPeerPingStatus"))
)
if mibBuilder.loadTexts:
    zhnPwMibScalars.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zhnPwMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 31, 2, 2, 1)
)
zhnPwMibCompliance.setObjects(
      *(("ZHNPWMIB", "zhnPwMibGroup"),
        ("ZHNPWMIB", "zhnPwMibScalars"))
)
if mibBuilder.loadTexts:
    zhnPwMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNPWMIB",
    **{"PwClearStatisticsTC": PwClearStatisticsTC,
       "zhnPwMib": zhnPwMib,
       "zhnPwNotifications": zhnPwNotifications,
       "zhnPwObjects": zhnPwObjects,
       "zhnPwTable": zhnPwTable,
       "zhnPwEntry": zhnPwEntry,
       "zhnPwIndex": zhnPwIndex,
       "zhnPwVlanID": zhnPwVlanID,
       "zhnPwVlanPriority": zhnPwVlanPriority,
       "zhnPwPeerMask": zhnPwPeerMask,
       "zhnPwPeerGateway": zhnPwPeerGateway,
       "zhnPwPeerMAC": zhnPwPeerMAC,
       "zhnPwMappedIfName": zhnPwMappedIfName,
       "zhnPwLocalLMBits": zhnPwLocalLMBits,
       "zhnPwLocalRBit": zhnPwLocalRBit,
       "zhnPwRemoteLMBits": zhnPwRemoteLMBits,
       "zhnPwRemoteRBit": zhnPwRemoteRBit,
       "zhnPwPeerMACMode": zhnPwPeerMACMode,
       "zhnPwActualPayloadSize": zhnPwActualPayloadSize,
       "zhnPwRxRaiAction": zhnPwRxRaiAction,
       "zhnPwRxAisAction": zhnPwRxAisAction,
       "zhnPwLopAction": zhnPwLopAction,
       "zhnPwAdaptState": zhnPwAdaptState,
       "zhnPwAdaptTime": zhnPwAdaptTime,
       "zhnPwIsdn": zhnPwIsdn,
       "zhnPwOuterLabel": zhnPwOuterLabel,
       "zhnPwClkAcquisitionLevel": zhnPwClkAcquisitionLevel,
       "zhnPwClearTotalStats": zhnPwClearTotalStats,
       "zhnPwRtpHeaderMode": zhnPwRtpHeaderMode,
       "zhnPwAdaptPllMode": zhnPwAdaptPllMode,
       "zhnPwAutoAdclEnable": zhnPwAutoAdclEnable,
       "zhnPwAdaptSourceActual": zhnPwAdaptSourceActual,
       "zhnPwSourceIPAddr": zhnPwSourceIPAddr,
       "zhnPwSourceIPMask": zhnPwSourceIPMask,
       "zhnPwSourceGateway": zhnPwSourceGateway,
       "zhnPwUdpDstPort": zhnPwUdpDstPort,
       "zhnPwT1E1Mode": zhnPwT1E1Mode,
       "zhnPeerPingName": zhnPeerPingName,
       "zhnPeerPingRequest": zhnPeerPingRequest,
       "zhnPeerPingStatus": zhnPeerPingStatus,
       "zhnPwConformance": zhnPwConformance,
       "zhnPwMibConformance": zhnPwMibConformance,
       "zhnPwMibGroups": zhnPwMibGroups,
       "zhnPwMibGroup": zhnPwMibGroup,
       "zhnPwMibScalars": zhnPwMibScalars,
       "zhnPwMibCompliances": zhnPwMibCompliances,
       "zhnPwMibCompliance": zhnPwMibCompliance}
)
