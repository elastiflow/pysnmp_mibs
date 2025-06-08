# SNMP MIB module (RUIJIE-RS485-CLASS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-RS485-CLASS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:02:06 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieRs485MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149)
)
if mibBuilder.loadTexts:
    ruijieRs485MIB.setRevisions(
        ("2007-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieRs485MIBObjects_ObjectIdentity = ObjectIdentity
ruijieRs485MIBObjects = _RuijieRs485MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1)
)
_RuijieRs485IpAddress_Type = IpAddress
_RuijieRs485IpAddress_Object = MibScalar
ruijieRs485IpAddress = _RuijieRs485IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 1),
    _RuijieRs485IpAddress_Type()
)
ruijieRs485IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485IpAddress.setStatus("current")
_RuijieRs485IpAddressMask_Type = IpAddress
_RuijieRs485IpAddressMask_Object = MibScalar
ruijieRs485IpAddressMask = _RuijieRs485IpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 2),
    _RuijieRs485IpAddressMask_Type()
)
ruijieRs485IpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485IpAddressMask.setStatus("current")
_RuijieRs485Gateway_Type = IpAddress
_RuijieRs485Gateway_Object = MibScalar
ruijieRs485Gateway = _RuijieRs485Gateway_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 3),
    _RuijieRs485Gateway_Type()
)
ruijieRs485Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485Gateway.setStatus("current")
_RuijieRs485Mac_Type = PhysAddress
_RuijieRs485Mac_Object = MibScalar
ruijieRs485Mac = _RuijieRs485Mac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 4),
    _RuijieRs485Mac_Type()
)
ruijieRs485Mac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485Mac.setStatus("current")


class _RuijieRs485ServerMode_Type(Integer32):
    """Custom type ruijieRs485ServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("client", 0),
          ("server", 1))
    )


_RuijieRs485ServerMode_Type.__name__ = "Integer32"
_RuijieRs485ServerMode_Object = MibScalar
ruijieRs485ServerMode = _RuijieRs485ServerMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 5),
    _RuijieRs485ServerMode_Type()
)
ruijieRs485ServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485ServerMode.setStatus("current")


class _RuijieRs485SerialNum_Type(Integer32):
    """Custom type ruijieRs485SerialNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuijieRs485SerialNum_Type.__name__ = "Integer32"
_RuijieRs485SerialNum_Object = MibScalar
ruijieRs485SerialNum = _RuijieRs485SerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 6),
    _RuijieRs485SerialNum_Type()
)
ruijieRs485SerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485SerialNum.setStatus("current")
_RuijieRs485TelnetIp_Type = IpAddress
_RuijieRs485TelnetIp_Object = MibScalar
ruijieRs485TelnetIp = _RuijieRs485TelnetIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 7),
    _RuijieRs485TelnetIp_Type()
)
ruijieRs485TelnetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485TelnetIp.setStatus("current")
_RuijieRs485State_Type = Integer32
_RuijieRs485State_Object = MibScalar
ruijieRs485State = _RuijieRs485State_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 8),
    _RuijieRs485State_Type()
)
ruijieRs485State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRs485State.setStatus("current")


class _RuijieRs485SerialPower1_Type(Integer32):
    """Custom type ruijieRs485SerialPower1 based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("short", 2),
          ("break", 3))
    )


_RuijieRs485SerialPower1_Type.__name__ = "Integer32"
_RuijieRs485SerialPower1_Object = MibScalar
ruijieRs485SerialPower1 = _RuijieRs485SerialPower1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 9),
    _RuijieRs485SerialPower1_Type()
)
ruijieRs485SerialPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRs485SerialPower1.setStatus("current")


class _RuijieRs485SerialPower2_Type(Integer32):
    """Custom type ruijieRs485SerialPower2 based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("short", 2),
          ("break", 3))
    )


_RuijieRs485SerialPower2_Type.__name__ = "Integer32"
_RuijieRs485SerialPower2_Object = MibScalar
ruijieRs485SerialPower2 = _RuijieRs485SerialPower2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 10),
    _RuijieRs485SerialPower2_Type()
)
ruijieRs485SerialPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRs485SerialPower2.setStatus("current")


class _RuijieRs485SerialPower3_Type(Integer32):
    """Custom type ruijieRs485SerialPower3 based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("short", 2),
          ("break", 3))
    )


_RuijieRs485SerialPower3_Type.__name__ = "Integer32"
_RuijieRs485SerialPower3_Object = MibScalar
ruijieRs485SerialPower3 = _RuijieRs485SerialPower3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 11),
    _RuijieRs485SerialPower3_Type()
)
ruijieRs485SerialPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRs485SerialPower3.setStatus("current")


class _RuijieRs485SerialPower4_Type(Integer32):
    """Custom type ruijieRs485SerialPower4 based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("short", 2),
          ("break", 3))
    )


_RuijieRs485SerialPower4_Type.__name__ = "Integer32"
_RuijieRs485SerialPower4_Object = MibScalar
ruijieRs485SerialPower4 = _RuijieRs485SerialPower4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 12),
    _RuijieRs485SerialPower4_Type()
)
ruijieRs485SerialPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRs485SerialPower4.setStatus("current")
_RuijieRs485VlanTable_Object = MibTable
ruijieRs485VlanTable = _RuijieRs485VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 13)
)
if mibBuilder.loadTexts:
    ruijieRs485VlanTable.setStatus("current")
_RuijieRs485VlanEntry_Object = MibTableRow
ruijieRs485VlanEntry = _RuijieRs485VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 13, 1)
)
ruijieRs485VlanEntry.setIndexNames(
    (0, "RUIJIE-RS485-CLASS-MIB", "ruijieRs485SerialPort"),
)
if mibBuilder.loadTexts:
    ruijieRs485VlanEntry.setStatus("current")
_RuijieRs485SerialPort_Type = Counter32
_RuijieRs485SerialPort_Object = MibTableColumn
ruijieRs485SerialPort = _RuijieRs485SerialPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 13, 1, 1),
    _RuijieRs485SerialPort_Type()
)
ruijieRs485SerialPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRs485SerialPort.setStatus("current")


class _RuijieRs485VLANID_Type(Integer32):
    """Custom type ruijieRs485VLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_RuijieRs485VLANID_Type.__name__ = "Integer32"
_RuijieRs485VLANID_Object = MibTableColumn
ruijieRs485VLANID = _RuijieRs485VLANID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 13, 1, 2),
    _RuijieRs485VLANID_Type()
)
ruijieRs485VLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485VLANID.setStatus("current")


class _RuijieRs485Baudrate_Type(Integer32):
    """Custom type ruijieRs485Baudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 999999),
    )


_RuijieRs485Baudrate_Type.__name__ = "Integer32"
_RuijieRs485Baudrate_Object = MibTableColumn
ruijieRs485Baudrate = _RuijieRs485Baudrate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 13, 1, 3),
    _RuijieRs485Baudrate_Type()
)
ruijieRs485Baudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485Baudrate.setStatus("current")


class _RuijieRs485Parity_Type(Integer32):
    """Custom type ruijieRs485Parity based on Integer32"""
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
        *(("none", 1),
          ("odd", 2),
          ("even", 3),
          ("mark", 4),
          ("space", 5))
    )


_RuijieRs485Parity_Type.__name__ = "Integer32"
_RuijieRs485Parity_Object = MibTableColumn
ruijieRs485Parity = _RuijieRs485Parity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 13, 1, 4),
    _RuijieRs485Parity_Type()
)
ruijieRs485Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485Parity.setStatus("current")


class _RuijieClassSerialType_Type(Integer32):
    """Custom type ruijieClassSerialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rs485", 0),
          ("rs232", 1))
    )


_RuijieClassSerialType_Type.__name__ = "Integer32"
_RuijieClassSerialType_Object = MibTableColumn
ruijieClassSerialType = _RuijieClassSerialType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 13, 1, 5),
    _RuijieClassSerialType_Type()
)
ruijieClassSerialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassSerialType.setStatus("current")


class _RuijieClassStatus_Type(Integer32):
    """Custom type ruijieClassStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("unnormal", 1))
    )


_RuijieClassStatus_Type.__name__ = "Integer32"
_RuijieClassStatus_Object = MibTableColumn
ruijieClassStatus = _RuijieClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 13, 1, 6),
    _RuijieClassStatus_Type()
)
ruijieClassStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassStatus.setStatus("current")


class _RuijieClassIsTeleControl_Type(Integer32):
    """Custom type ruijieClassIsTeleControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieClassIsTeleControl_Type.__name__ = "Integer32"
_RuijieClassIsTeleControl_Object = MibTableColumn
ruijieClassIsTeleControl = _RuijieClassIsTeleControl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 13, 1, 7),
    _RuijieClassIsTeleControl_Type()
)
ruijieClassIsTeleControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassIsTeleControl.setStatus("current")
_RuijieSSIfTable_Object = MibTable
ruijieSSIfTable = _RuijieSSIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 14)
)
if mibBuilder.loadTexts:
    ruijieSSIfTable.setStatus("current")
_RuijieSSIfEntry_Object = MibTableRow
ruijieSSIfEntry = _RuijieSSIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 14, 1)
)
ruijieSSIfEntry.setIndexNames(
    (0, "RUIJIE-RS485-CLASS-MIB", "ruijieSSIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieSSIfEntry.setStatus("current")
_RuijieSSIfIndex_Type = Counter32
_RuijieSSIfIndex_Object = MibTableColumn
ruijieSSIfIndex = _RuijieSSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 14, 1, 1),
    _RuijieSSIfIndex_Type()
)
ruijieSSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSSIfIndex.setStatus("current")


class _RuijieSSIfAccessVlan_Type(Integer32):
    """Custom type ruijieSSIfAccessVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieSSIfAccessVlan_Type.__name__ = "Integer32"
_RuijieSSIfAccessVlan_Object = MibTableColumn
ruijieSSIfAccessVlan = _RuijieSSIfAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 14, 1, 2),
    _RuijieSSIfAccessVlan_Type()
)
ruijieSSIfAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSSIfAccessVlan.setStatus("current")


class _RuijieSSIfNativeVlan_Type(Integer32):
    """Custom type ruijieSSIfNativeVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieSSIfNativeVlan_Type.__name__ = "Integer32"
_RuijieSSIfNativeVlan_Object = MibTableColumn
ruijieSSIfNativeVlan = _RuijieSSIfNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 14, 1, 3),
    _RuijieSSIfNativeVlan_Type()
)
ruijieSSIfNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSSIfNativeVlan.setStatus("current")


class _RuijieSSIfTrunk_Type(Integer32):
    """Custom type ruijieSSIfTrunk based on Integer32"""
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


_RuijieSSIfTrunk_Type.__name__ = "Integer32"
_RuijieSSIfTrunk_Object = MibTableColumn
ruijieSSIfTrunk = _RuijieSSIfTrunk_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 14, 1, 4),
    _RuijieSSIfTrunk_Type()
)
ruijieSSIfTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSSIfTrunk.setStatus("current")


class _RuijieSSIfSpeed_Type(Integer32):
    """Custom type ruijieSSIfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed_10M", 0),
          ("speed_100M", 1),
          ("speed_1000M", 2))
    )


_RuijieSSIfSpeed_Type.__name__ = "Integer32"
_RuijieSSIfSpeed_Object = MibTableColumn
ruijieSSIfSpeed = _RuijieSSIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 14, 1, 5),
    _RuijieSSIfSpeed_Type()
)
ruijieSSIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSSIfSpeed.setStatus("current")


class _RuijieSSIfDuplex_Type(Integer32):
    """Custom type ruijieSSIfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1))
    )


_RuijieSSIfDuplex_Type.__name__ = "Integer32"
_RuijieSSIfDuplex_Object = MibTableColumn
ruijieSSIfDuplex = _RuijieSSIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 14, 1, 6),
    _RuijieSSIfDuplex_Type()
)
ruijieSSIfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSSIfDuplex.setStatus("current")


class _RuijieSSIfNegotiation_Type(Integer32):
    """Custom type ruijieSSIfNegotiation based on Integer32"""
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


_RuijieSSIfNegotiation_Type.__name__ = "Integer32"
_RuijieSSIfNegotiation_Object = MibTableColumn
ruijieSSIfNegotiation = _RuijieSSIfNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 14, 1, 7),
    _RuijieSSIfNegotiation_Type()
)
ruijieSSIfNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSSIfNegotiation.setStatus("current")


class _RuijieRs485IpSetStatus_Type(Integer32):
    """Custom type ruijieRs485IpSetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enable", 1),
          ("dhcp", 2))
    )


_RuijieRs485IpSetStatus_Type.__name__ = "Integer32"
_RuijieRs485IpSetStatus_Object = MibScalar
ruijieRs485IpSetStatus = _RuijieRs485IpSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 15),
    _RuijieRs485IpSetStatus_Type()
)
ruijieRs485IpSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485IpSetStatus.setStatus("current")
_RuijieLabelIDReg_Type = PhysAddress
_RuijieLabelIDReg_Object = MibScalar
ruijieLabelIDReg = _RuijieLabelIDReg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 16),
    _RuijieLabelIDReg_Type()
)
ruijieLabelIDReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLabelIDReg.setStatus("current")


class _RuijieLabelTypeReg_Type(Integer32):
    """Custom type ruijieLabelTypeReg based on Integer32"""
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
        *(("default", 0),
          ("rfid", 1),
          ("ble", 2),
          ("zibgee", 3))
    )


_RuijieLabelTypeReg_Type.__name__ = "Integer32"
_RuijieLabelTypeReg_Object = MibScalar
ruijieLabelTypeReg = _RuijieLabelTypeReg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 17),
    _RuijieLabelTypeReg_Type()
)
ruijieLabelTypeReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLabelTypeReg.setStatus("current")


class _RuijieLabelRegStatus_Type(Integer32):
    """Custom type ruijieLabelRegStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enable", 1))
    )


_RuijieLabelRegStatus_Type.__name__ = "Integer32"
_RuijieLabelRegStatus_Object = MibScalar
ruijieLabelRegStatus = _RuijieLabelRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 18),
    _RuijieLabelRegStatus_Type()
)
ruijieLabelRegStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLabelRegStatus.setStatus("current")
_RuijieLabelInfoTable_Object = MibTable
ruijieLabelInfoTable = _RuijieLabelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 19)
)
if mibBuilder.loadTexts:
    ruijieLabelInfoTable.setStatus("current")
_RuijieLabelInfoEntry_Object = MibTableRow
ruijieLabelInfoEntry = _RuijieLabelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 19, 1)
)
ruijieLabelInfoEntry.setIndexNames(
    (0, "RUIJIE-RS485-CLASS-MIB", "ruijieLabelType"),
    (0, "RUIJIE-RS485-CLASS-MIB", "ruijieLabelID"),
)
if mibBuilder.loadTexts:
    ruijieLabelInfoEntry.setStatus("current")


class _RuijieLabelType_Type(Integer32):
    """Custom type ruijieLabelType based on Integer32"""
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
        *(("unknown", 0),
          ("rfid", 1),
          ("ble", 2),
          ("zigbee", 3))
    )


_RuijieLabelType_Type.__name__ = "Integer32"
_RuijieLabelType_Object = MibTableColumn
ruijieLabelType = _RuijieLabelType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 19, 1, 1),
    _RuijieLabelType_Type()
)
ruijieLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLabelType.setStatus("current")
_RuijieLabelID_Type = PhysAddress
_RuijieLabelID_Object = MibTableColumn
ruijieLabelID = _RuijieLabelID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 19, 1, 2),
    _RuijieLabelID_Type()
)
ruijieLabelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLabelID.setStatus("current")


class _RuijieLabelActiveStatus_Type(Integer32):
    """Custom type ruijieLabelActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("active", 1),
          ("deactive", 2),
          ("active-success-ack", 3),
          ("active-fail-ack", 4),
          ("deactive-success-ack", 5),
          ("deactive-fail-ack", 6))
    )


_RuijieLabelActiveStatus_Type.__name__ = "Integer32"
_RuijieLabelActiveStatus_Object = MibTableColumn
ruijieLabelActiveStatus = _RuijieLabelActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 19, 1, 3),
    _RuijieLabelActiveStatus_Type()
)
ruijieLabelActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLabelActiveStatus.setStatus("current")


class _RuijieLabelPowerStatus_Type(Integer32):
    """Custom type ruijieLabelPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieLabelPowerStatus_Type.__name__ = "Integer32"
_RuijieLabelPowerStatus_Object = MibTableColumn
ruijieLabelPowerStatus = _RuijieLabelPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 19, 1, 4),
    _RuijieLabelPowerStatus_Type()
)
ruijieLabelPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLabelPowerStatus.setStatus("current")


class _RuijieLabelWarningCancel_Type(Integer32):
    """Custom type ruijieLabelWarningCancel based on Integer32"""
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
        *(("unknown", 0),
          ("cancel-stolen", 1),
          ("cancel-power", 2),
          ("cancel-unnormal", 3))
    )


_RuijieLabelWarningCancel_Type.__name__ = "Integer32"
_RuijieLabelWarningCancel_Object = MibTableColumn
ruijieLabelWarningCancel = _RuijieLabelWarningCancel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 19, 1, 5),
    _RuijieLabelWarningCancel_Type()
)
ruijieLabelWarningCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLabelWarningCancel.setStatus("current")


class _RuijieLabelUnregStatus_Type(Integer32):
    """Custom type ruijieLabelUnregStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("apply-unreg", 1),
          ("unreg", 2),
          ("allow-unreg", 3),
          ("not-allow-unreg", 4),
          ("reg-success", 5),
          ("reg-failed", 6))
    )


_RuijieLabelUnregStatus_Type.__name__ = "Integer32"
_RuijieLabelUnregStatus_Object = MibTableColumn
ruijieLabelUnregStatus = _RuijieLabelUnregStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 19, 1, 6),
    _RuijieLabelUnregStatus_Type()
)
ruijieLabelUnregStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieLabelUnregStatus.setStatus("current")


class _RuijieLabelStolenWarningStatus_Type(Integer32):
    """Custom type ruijieLabelStolenWarningStatus based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("stolen", 2),
          ("unnormal", 3))
    )


_RuijieLabelStolenWarningStatus_Type.__name__ = "Integer32"
_RuijieLabelStolenWarningStatus_Object = MibTableColumn
ruijieLabelStolenWarningStatus = _RuijieLabelStolenWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 19, 1, 7),
    _RuijieLabelStolenWarningStatus_Type()
)
ruijieLabelStolenWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLabelStolenWarningStatus.setStatus("current")
_RuijieRs485TrapIp_Type = IpAddress
_RuijieRs485TrapIp_Object = MibScalar
ruijieRs485TrapIp = _RuijieRs485TrapIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 20),
    _RuijieRs485TrapIp_Type()
)
ruijieRs485TrapIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRs485TrapIp.setStatus("current")


class _RuijieRs485HeartbeatStatus_Type(Integer32):
    """Custom type ruijieRs485HeartbeatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("normal", 1))
    )


_RuijieRs485HeartbeatStatus_Type.__name__ = "Integer32"
_RuijieRs485HeartbeatStatus_Object = MibScalar
ruijieRs485HeartbeatStatus = _RuijieRs485HeartbeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 21),
    _RuijieRs485HeartbeatStatus_Type()
)
ruijieRs485HeartbeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRs485HeartbeatStatus.setStatus("current")


class _RuijieClassPDUPower1_Type(Integer32):
    """Custom type ruijieClassPDUPower1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("break", 1),
          ("normal", 2))
    )


_RuijieClassPDUPower1_Type.__name__ = "Integer32"
_RuijieClassPDUPower1_Object = MibScalar
ruijieClassPDUPower1 = _RuijieClassPDUPower1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 22),
    _RuijieClassPDUPower1_Type()
)
ruijieClassPDUPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassPDUPower1.setStatus("current")


class _RuijieClassPDUPower2_Type(Integer32):
    """Custom type ruijieClassPDUPower2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("break", 1),
          ("normal", 2))
    )


_RuijieClassPDUPower2_Type.__name__ = "Integer32"
_RuijieClassPDUPower2_Object = MibScalar
ruijieClassPDUPower2 = _RuijieClassPDUPower2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 23),
    _RuijieClassPDUPower2_Type()
)
ruijieClassPDUPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassPDUPower2.setStatus("current")


class _RuijieClassDeviceAddType_Type(Integer32):
    """Custom type ruijieClassDeviceAddType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("video", 1),
          ("audio", 2),
          ("videoandaudio", 3),
          ("light", 4),
          ("air-con", 5),
          ("record", 6),
          ("projector", 7),
          ("screen", 8),
          ("app-pad", 9),
          ("smart-switch", 10))
    )


_RuijieClassDeviceAddType_Type.__name__ = "Integer32"
_RuijieClassDeviceAddType_Object = MibScalar
ruijieClassDeviceAddType = _RuijieClassDeviceAddType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 24),
    _RuijieClassDeviceAddType_Type()
)
ruijieClassDeviceAddType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceAddType.setStatus("current")
_RuijieClassDeviceAddID_Type = Integer32
_RuijieClassDeviceAddID_Object = MibScalar
ruijieClassDeviceAddID = _RuijieClassDeviceAddID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 25),
    _RuijieClassDeviceAddID_Type()
)
ruijieClassDeviceAddID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceAddID.setStatus("current")


class _RuijieClassDeviceAddStatus_Type(Integer32):
    """Custom type ruijieClassDeviceAddStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("add", 1)
    )


_RuijieClassDeviceAddStatus_Type.__name__ = "Integer32"
_RuijieClassDeviceAddStatus_Object = MibScalar
ruijieClassDeviceAddStatus = _RuijieClassDeviceAddStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 26),
    _RuijieClassDeviceAddStatus_Type()
)
ruijieClassDeviceAddStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceAddStatus.setStatus("current")
_RuijieClassDeviceInfoTable_Object = MibTable
ruijieClassDeviceInfoTable = _RuijieClassDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27)
)
if mibBuilder.loadTexts:
    ruijieClassDeviceInfoTable.setStatus("current")
_RuijieClassDeviceInfoEntry_Object = MibTableRow
ruijieClassDeviceInfoEntry = _RuijieClassDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1)
)
ruijieClassDeviceInfoEntry.setIndexNames(
    (0, "RUIJIE-RS485-CLASS-MIB", "ruijieClassDeviceType"),
    (0, "RUIJIE-RS485-CLASS-MIB", "ruijieClassDeviceID"),
)
if mibBuilder.loadTexts:
    ruijieClassDeviceInfoEntry.setStatus("current")


class _RuijieClassDeviceType_Type(Integer32):
    """Custom type ruijieClassDeviceType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("video", 1),
          ("audio", 2),
          ("videoandaudio", 3),
          ("light", 4),
          ("air-con", 5),
          ("record", 6),
          ("projector", 7),
          ("screen", 8),
          ("app-pad", 9),
          ("smart-switch", 10))
    )


_RuijieClassDeviceType_Type.__name__ = "Integer32"
_RuijieClassDeviceType_Object = MibTableColumn
ruijieClassDeviceType = _RuijieClassDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 1),
    _RuijieClassDeviceType_Type()
)
ruijieClassDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassDeviceType.setStatus("current")
_RuijieClassDeviceID_Type = Integer32
_RuijieClassDeviceID_Object = MibTableColumn
ruijieClassDeviceID = _RuijieClassDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 2),
    _RuijieClassDeviceID_Type()
)
ruijieClassDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassDeviceID.setStatus("current")
_RuijieClassDeviceIconType_Type = Integer32
_RuijieClassDeviceIconType_Object = MibTableColumn
ruijieClassDeviceIconType = _RuijieClassDeviceIconType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 3),
    _RuijieClassDeviceIconType_Type()
)
ruijieClassDeviceIconType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceIconType.setStatus("current")


class _RuijieClassDeviceName_Type(OctetString):
    """Custom type ruijieClassDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RuijieClassDeviceName_Type.__name__ = "OctetString"
_RuijieClassDeviceName_Object = MibTableColumn
ruijieClassDeviceName = _RuijieClassDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 4),
    _RuijieClassDeviceName_Type()
)
ruijieClassDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceName.setStatus("current")
_RuijieClassDeviceModelID_Type = Integer32
_RuijieClassDeviceModelID_Object = MibTableColumn
ruijieClassDeviceModelID = _RuijieClassDeviceModelID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 5),
    _RuijieClassDeviceModelID_Type()
)
ruijieClassDeviceModelID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceModelID.setStatus("current")


class _RuijieClassDeviceControlSerial_Type(Integer32):
    """Custom type ruijieClassDeviceControlSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RuijieClassDeviceControlSerial_Type.__name__ = "Integer32"
_RuijieClassDeviceControlSerial_Object = MibTableColumn
ruijieClassDeviceControlSerial = _RuijieClassDeviceControlSerial_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 6),
    _RuijieClassDeviceControlSerial_Type()
)
ruijieClassDeviceControlSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceControlSerial.setStatus("current")


class _RuijieClassDeviceTeleControlPort_Type(Integer32):
    """Custom type ruijieClassDeviceTeleControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RuijieClassDeviceTeleControlPort_Type.__name__ = "Integer32"
_RuijieClassDeviceTeleControlPort_Object = MibTableColumn
ruijieClassDeviceTeleControlPort = _RuijieClassDeviceTeleControlPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 7),
    _RuijieClassDeviceTeleControlPort_Type()
)
ruijieClassDeviceTeleControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceTeleControlPort.setStatus("current")


class _RuijieClassDeviceIOType_Type(Integer32):
    """Custom type ruijieClassDeviceIOType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 0),
          ("output", 1),
          ("other", 2))
    )


_RuijieClassDeviceIOType_Type.__name__ = "Integer32"
_RuijieClassDeviceIOType_Object = MibTableColumn
ruijieClassDeviceIOType = _RuijieClassDeviceIOType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 8),
    _RuijieClassDeviceIOType_Type()
)
ruijieClassDeviceIOType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceIOType.setStatus("current")


class _RuijieClassDeviceVideoPort_Type(Integer32):
    """Custom type ruijieClassDeviceVideoPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RuijieClassDeviceVideoPort_Type.__name__ = "Integer32"
_RuijieClassDeviceVideoPort_Object = MibTableColumn
ruijieClassDeviceVideoPort = _RuijieClassDeviceVideoPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 9),
    _RuijieClassDeviceVideoPort_Type()
)
ruijieClassDeviceVideoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceVideoPort.setStatus("current")


class _RuijieClassDeviceAudioPort_Type(Integer32):
    """Custom type ruijieClassDeviceAudioPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RuijieClassDeviceAudioPort_Type.__name__ = "Integer32"
_RuijieClassDeviceAudioPort_Object = MibTableColumn
ruijieClassDeviceAudioPort = _RuijieClassDeviceAudioPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 10),
    _RuijieClassDeviceAudioPort_Type()
)
ruijieClassDeviceAudioPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceAudioPort.setStatus("current")


class _RuijieClassDeviceVideoUsedStatus_Type(Integer32):
    """Custom type ruijieClassDeviceVideoUsedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("used", 1))
    )


_RuijieClassDeviceVideoUsedStatus_Type.__name__ = "Integer32"
_RuijieClassDeviceVideoUsedStatus_Object = MibTableColumn
ruijieClassDeviceVideoUsedStatus = _RuijieClassDeviceVideoUsedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 11),
    _RuijieClassDeviceVideoUsedStatus_Type()
)
ruijieClassDeviceVideoUsedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceVideoUsedStatus.setStatus("current")


class _RuijieClassDeviceAudioUsedStatus_Type(Integer32):
    """Custom type ruijieClassDeviceAudioUsedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("used", 1))
    )


_RuijieClassDeviceAudioUsedStatus_Type.__name__ = "Integer32"
_RuijieClassDeviceAudioUsedStatus_Object = MibTableColumn
ruijieClassDeviceAudioUsedStatus = _RuijieClassDeviceAudioUsedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 12),
    _RuijieClassDeviceAudioUsedStatus_Type()
)
ruijieClassDeviceAudioUsedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceAudioUsedStatus.setStatus("current")
_RuijieClassDeviceSwitch_Type = Integer32
_RuijieClassDeviceSwitch_Object = MibTableColumn
ruijieClassDeviceSwitch = _RuijieClassDeviceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 13),
    _RuijieClassDeviceSwitch_Type()
)
ruijieClassDeviceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceSwitch.setStatus("current")


class _RuijieClassDeviceState_Type(Integer32):
    """Custom type ruijieClassDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("normal", 1),
          ("no-ack", 2))
    )


_RuijieClassDeviceState_Type.__name__ = "Integer32"
_RuijieClassDeviceState_Object = MibTableColumn
ruijieClassDeviceState = _RuijieClassDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 14),
    _RuijieClassDeviceState_Type()
)
ruijieClassDeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceState.setStatus("current")
_RuijieClassDeviceZigbeeID_Type = Integer32
_RuijieClassDeviceZigbeeID_Object = MibTableColumn
ruijieClassDeviceZigbeeID = _RuijieClassDeviceZigbeeID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 15),
    _RuijieClassDeviceZigbeeID_Type()
)
ruijieClassDeviceZigbeeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceZigbeeID.setStatus("current")


class _RuijieClassDeviceSetStatus_Type(Integer32):
    """Custom type ruijieClassDeviceSetStatus based on Integer32"""
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
        *(("unset", 0),
          ("set", 1),
          ("delete", 2),
          ("update", 3))
    )


_RuijieClassDeviceSetStatus_Type.__name__ = "Integer32"
_RuijieClassDeviceSetStatus_Object = MibTableColumn
ruijieClassDeviceSetStatus = _RuijieClassDeviceSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 16),
    _RuijieClassDeviceSetStatus_Type()
)
ruijieClassDeviceSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceSetStatus.setStatus("current")
_RuijieClassDeviceIP_Type = IpAddress
_RuijieClassDeviceIP_Object = MibTableColumn
ruijieClassDeviceIP = _RuijieClassDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 17),
    _RuijieClassDeviceIP_Type()
)
ruijieClassDeviceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeviceIP.setStatus("current")
_RuijieClassBindDeviceID_Type = Integer32
_RuijieClassBindDeviceID_Object = MibTableColumn
ruijieClassBindDeviceID = _RuijieClassBindDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 18),
    _RuijieClassBindDeviceID_Type()
)
ruijieClassBindDeviceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassBindDeviceID.setStatus("current")
_RuijieClassBatchSupport_Type = Integer32
_RuijieClassBatchSupport_Object = MibTableColumn
ruijieClassBatchSupport = _RuijieClassBatchSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 27, 1, 19),
    _RuijieClassBatchSupport_Type()
)
ruijieClassBatchSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassBatchSupport.setStatus("current")


class _RuijieClassAPPUsername_Type(OctetString):
    """Custom type ruijieClassAPPUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RuijieClassAPPUsername_Type.__name__ = "OctetString"
_RuijieClassAPPUsername_Object = MibScalar
ruijieClassAPPUsername = _RuijieClassAPPUsername_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 28),
    _RuijieClassAPPUsername_Type()
)
ruijieClassAPPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassAPPUsername.setStatus("current")


class _RuijieClassAPPPassword_Type(OctetString):
    """Custom type ruijieClassAPPPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RuijieClassAPPPassword_Type.__name__ = "OctetString"
_RuijieClassAPPPassword_Object = MibScalar
ruijieClassAPPPassword = _RuijieClassAPPPassword_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 29),
    _RuijieClassAPPPassword_Type()
)
ruijieClassAPPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassAPPPassword.setStatus("current")


class _RuijieClassAPPAuth_Type(Integer32):
    """Custom type ruijieClassAPPAuth based on Integer32"""
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
        *(("success", 0),
          ("failed", 1),
          ("success-update", 2),
          ("card-success", 3),
          ("card-failed", 4),
          ("user-info", 5))
    )


_RuijieClassAPPAuth_Type.__name__ = "Integer32"
_RuijieClassAPPAuth_Object = MibScalar
ruijieClassAPPAuth = _RuijieClassAPPAuth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 30),
    _RuijieClassAPPAuth_Type()
)
ruijieClassAPPAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassAPPAuth.setStatus("current")
_RuijieClassCMDDeviceModelID_Type = Integer32
_RuijieClassCMDDeviceModelID_Object = MibScalar
ruijieClassCMDDeviceModelID = _RuijieClassCMDDeviceModelID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 31),
    _RuijieClassCMDDeviceModelID_Type()
)
ruijieClassCMDDeviceModelID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassCMDDeviceModelID.setStatus("current")
_RuijieClassCMDType_Type = Integer32
_RuijieClassCMDType_Object = MibScalar
ruijieClassCMDType = _RuijieClassCMDType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 32),
    _RuijieClassCMDType_Type()
)
ruijieClassCMDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassCMDType.setStatus("current")


class _RuijieClassCommand_Type(OctetString):
    """Custom type ruijieClassCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RuijieClassCommand_Type.__name__ = "OctetString"
_RuijieClassCommand_Object = MibScalar
ruijieClassCommand = _RuijieClassCommand_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 33),
    _RuijieClassCommand_Type()
)
ruijieClassCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassCommand.setStatus("current")


class _RuijieClassCommandSetStatus_Type(Integer32):
    """Custom type ruijieClassCommandSetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-get", 1),
          ("set", 2),
          ("delete", 3))
    )


_RuijieClassCommandSetStatus_Type.__name__ = "Integer32"
_RuijieClassCommandSetStatus_Object = MibScalar
ruijieClassCommandSetStatus = _RuijieClassCommandSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 34),
    _RuijieClassCommandSetStatus_Type()
)
ruijieClassCommandSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassCommandSetStatus.setStatus("current")


class _RuijieClassOperAll_Type(Integer32):
    """Custom type ruijieClassOperAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open-all", 1),
          ("close-all", 2))
    )


_RuijieClassOperAll_Type.__name__ = "Integer32"
_RuijieClassOperAll_Object = MibScalar
ruijieClassOperAll = _RuijieClassOperAll_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 35),
    _RuijieClassOperAll_Type()
)
ruijieClassOperAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassOperAll.setStatus("current")


class _RuijieClassCardID_Type(OctetString):
    """Custom type ruijieClassCardID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RuijieClassCardID_Type.__name__ = "OctetString"
_RuijieClassCardID_Object = MibScalar
ruijieClassCardID = _RuijieClassCardID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 36),
    _RuijieClassCardID_Type()
)
ruijieClassCardID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassCardID.setStatus("current")
_RuijieClassDateTime_Type = Integer32
_RuijieClassDateTime_Object = MibScalar
ruijieClassDateTime = _RuijieClassDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 37),
    _RuijieClassDateTime_Type()
)
ruijieClassDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDateTime.setStatus("current")


class _RuijieClassAPPUpdateReq_Type(Integer32):
    """Custom type ruijieClassAPPUpdateReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("device_req", 1),
          ("user_auth_req", 2))
    )


_RuijieClassAPPUpdateReq_Type.__name__ = "Integer32"
_RuijieClassAPPUpdateReq_Object = MibScalar
ruijieClassAPPUpdateReq = _RuijieClassAPPUpdateReq_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 38),
    _RuijieClassAPPUpdateReq_Type()
)
ruijieClassAPPUpdateReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassAPPUpdateReq.setStatus("current")


class _RuijieClassUpdateFileName_Type(OctetString):
    """Custom type ruijieClassUpdateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieClassUpdateFileName_Type.__name__ = "OctetString"
_RuijieClassUpdateFileName_Object = MibScalar
ruijieClassUpdateFileName = _RuijieClassUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 39),
    _RuijieClassUpdateFileName_Type()
)
ruijieClassUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassUpdateFileName.setStatus("current")


class _RuijieClassUpdate_Type(Integer32):
    """Custom type ruijieClassUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_RuijieClassUpdate_Type.__name__ = "Integer32"
_RuijieClassUpdate_Object = MibScalar
ruijieClassUpdate = _RuijieClassUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 40),
    _RuijieClassUpdate_Type()
)
ruijieClassUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassUpdate.setStatus("current")


class _RuijieClassSoftVersion_Type(OctetString):
    """Custom type ruijieClassSoftVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieClassSoftVersion_Type.__name__ = "OctetString"
_RuijieClassSoftVersion_Object = MibScalar
ruijieClassSoftVersion = _RuijieClassSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 41),
    _RuijieClassSoftVersion_Type()
)
ruijieClassSoftVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassSoftVersion.setStatus("current")


class _RuijieClassChannel_Type(OctetString):
    """Custom type ruijieClassChannel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RuijieClassChannel_Type.__name__ = "OctetString"
_RuijieClassChannel_Object = MibScalar
ruijieClassChannel = _RuijieClassChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 42),
    _RuijieClassChannel_Type()
)
ruijieClassChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassChannel.setStatus("current")
_RuijieClassOldDeviceIP_Type = IpAddress
_RuijieClassOldDeviceIP_Object = MibScalar
ruijieClassOldDeviceIP = _RuijieClassOldDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 43),
    _RuijieClassOldDeviceIP_Type()
)
ruijieClassOldDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassOldDeviceIP.setStatus("current")


class _RuijieClassCommunity_Type(OctetString):
    """Custom type ruijieClassCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieClassCommunity_Type.__name__ = "OctetString"
_RuijieClassCommunity_Object = MibScalar
ruijieClassCommunity = _RuijieClassCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 44),
    _RuijieClassCommunity_Type()
)
ruijieClassCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassCommunity.setStatus("current")


class _RuijieClassUpdateStatus_Type(Integer32):
    """Custom type ruijieClassUpdateStatus based on Integer32"""
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
        *(("init", 0),
          ("scc_update_start", 1),
          ("scc_update_success", 2),
          ("scc_update_crc_error", 3),
          ("scc_update_product_id_error", 4),
          ("scc_update_tftp_timeout_error", 5),
          ("remote_device_update_no_existerror", 6),
          ("scc_update_file_too_big_error", 7))
    )


_RuijieClassUpdateStatus_Type.__name__ = "Integer32"
_RuijieClassUpdateStatus_Object = MibScalar
ruijieClassUpdateStatus = _RuijieClassUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 45),
    _RuijieClassUpdateStatus_Type()
)
ruijieClassUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassUpdateStatus.setStatus("current")


class _RuijieClassScheduleTableName_Type(OctetString):
    """Custom type ruijieClassScheduleTableName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieClassScheduleTableName_Type.__name__ = "OctetString"
_RuijieClassScheduleTableName_Object = MibScalar
ruijieClassScheduleTableName = _RuijieClassScheduleTableName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 46),
    _RuijieClassScheduleTableName_Type()
)
ruijieClassScheduleTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassScheduleTableName.setStatus("current")


class _RuijieClassUpdateScheduleTable_Type(Integer32):
    """Custom type ruijieClassUpdateScheduleTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_RuijieClassUpdateScheduleTable_Type.__name__ = "Integer32"
_RuijieClassUpdateScheduleTable_Object = MibScalar
ruijieClassUpdateScheduleTable = _RuijieClassUpdateScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 47),
    _RuijieClassUpdateScheduleTable_Type()
)
ruijieClassUpdateScheduleTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassUpdateScheduleTable.setStatus("current")


class _RuijieClassScheduleTableUpdateStatus_Type(Integer32):
    """Custom type ruijieClassScheduleTableUpdateStatus based on Integer32"""
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
        *(("init", 0),
          ("scc_update_start", 1),
          ("scc_update_success", 2),
          ("scc_update_crc_error", 3),
          ("scc_update_product_id_error", 4),
          ("scc_update_tftp_timeout_error", 5),
          ("scc_remote_no_exist_error", 6),
          ("scc_update_file_too_big_error", 7),
          ("scc_update_redo", 8))
    )


_RuijieClassScheduleTableUpdateStatus_Type.__name__ = "Integer32"
_RuijieClassScheduleTableUpdateStatus_Object = MibScalar
ruijieClassScheduleTableUpdateStatus = _RuijieClassScheduleTableUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 48),
    _RuijieClassScheduleTableUpdateStatus_Type()
)
ruijieClassScheduleTableUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassScheduleTableUpdateStatus.setStatus("current")


class _RuijieClassCheckTableName_Type(OctetString):
    """Custom type ruijieClassCheckTableName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieClassCheckTableName_Type.__name__ = "OctetString"
_RuijieClassCheckTableName_Object = MibScalar
ruijieClassCheckTableName = _RuijieClassCheckTableName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 49),
    _RuijieClassCheckTableName_Type()
)
ruijieClassCheckTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassCheckTableName.setStatus("current")


class _RuijieClassReadCheckTable_Type(Integer32):
    """Custom type ruijieClassReadCheckTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_RuijieClassReadCheckTable_Type.__name__ = "Integer32"
_RuijieClassReadCheckTable_Object = MibScalar
ruijieClassReadCheckTable = _RuijieClassReadCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 50),
    _RuijieClassReadCheckTable_Type()
)
ruijieClassReadCheckTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassReadCheckTable.setStatus("current")


class _RuijieClassReadCheckTable1UploadStatus_Type(Integer32):
    """Custom type ruijieClassReadCheckTable1UploadStatus based on Integer32"""
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
        *(("init", 0),
          ("scc_update_start", 1),
          ("scc_update_success", 2),
          ("scc_update_crc_error", 3),
          ("scc_update_product_id_error", 4),
          ("scc_update_tftp_timeout_error", 5),
          ("scc_remote_no_exist_error", 6),
          ("scc_update_file_too_big_error", 7))
    )


_RuijieClassReadCheckTable1UploadStatus_Type.__name__ = "Integer32"
_RuijieClassReadCheckTable1UploadStatus_Object = MibScalar
ruijieClassReadCheckTable1UploadStatus = _RuijieClassReadCheckTable1UploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 51),
    _RuijieClassReadCheckTable1UploadStatus_Type()
)
ruijieClassReadCheckTable1UploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassReadCheckTable1UploadStatus.setStatus("current")
_RuijieClassLampTimeClass_Type = Integer32
_RuijieClassLampTimeClass_Object = MibScalar
ruijieClassLampTimeClass = _RuijieClassLampTimeClass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 52),
    _RuijieClassLampTimeClass_Type()
)
ruijieClassLampTimeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassLampTimeClass.setStatus("current")


class _RuijieClassDeleteRecordTable_Type(Integer32):
    """Custom type ruijieClassDeleteRecordTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_RuijieClassDeleteRecordTable_Type.__name__ = "Integer32"
_RuijieClassDeleteRecordTable_Object = MibScalar
ruijieClassDeleteRecordTable = _RuijieClassDeleteRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 53),
    _RuijieClassDeleteRecordTable_Type()
)
ruijieClassDeleteRecordTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassDeleteRecordTable.setStatus("current")
_RuijieClassSystemTime_Type = Counter32
_RuijieClassSystemTime_Object = MibScalar
ruijieClassSystemTime = _RuijieClassSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 54),
    _RuijieClassSystemTime_Type()
)
ruijieClassSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieClassSystemTime.setStatus("current")


class _RuijieClassProjectorFact_Type(OctetString):
    """Custom type ruijieClassProjectorFact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieClassProjectorFact_Type.__name__ = "OctetString"
_RuijieClassProjectorFact_Object = MibScalar
ruijieClassProjectorFact = _RuijieClassProjectorFact_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 55),
    _RuijieClassProjectorFact_Type()
)
ruijieClassProjectorFact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassProjectorFact.setStatus("current")


class _RuijieClassProjectorModel_Type(OctetString):
    """Custom type ruijieClassProjectorModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieClassProjectorModel_Type.__name__ = "OctetString"
_RuijieClassProjectorModel_Object = MibScalar
ruijieClassProjectorModel = _RuijieClassProjectorModel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 56),
    _RuijieClassProjectorModel_Type()
)
ruijieClassProjectorModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassProjectorModel.setStatus("current")


class _RuijieClassAIOFact_Type(OctetString):
    """Custom type ruijieClassAIOFact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieClassAIOFact_Type.__name__ = "OctetString"
_RuijieClassAIOFact_Object = MibScalar
ruijieClassAIOFact = _RuijieClassAIOFact_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 57),
    _RuijieClassAIOFact_Type()
)
ruijieClassAIOFact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassAIOFact.setStatus("current")


class _RuijieClassAIOModel_Type(OctetString):
    """Custom type ruijieClassAIOModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieClassAIOModel_Type.__name__ = "OctetString"
_RuijieClassAIOModel_Object = MibScalar
ruijieClassAIOModel = _RuijieClassAIOModel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 1, 58),
    _RuijieClassAIOModel_Type()
)
ruijieClassAIOModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieClassAIOModel.setStatus("current")
_RuijieRs485MIBTrap_ObjectIdentity = ObjectIdentity
ruijieRs485MIBTrap = _RuijieRs485MIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2)
)

# Managed Objects groups


# Notification objects

ruijieRs485StateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 0)
)
ruijieRs485StateChange.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieRs485State")
)
if mibBuilder.loadTexts:
    ruijieRs485StateChange.setStatus(
        "current"
    )

ruijieRs485Power1Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 1)
)
ruijieRs485Power1Change.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieRs485SerialPower1")
)
if mibBuilder.loadTexts:
    ruijieRs485Power1Change.setStatus(
        "current"
    )

ruijieRs485Power2Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 2)
)
ruijieRs485Power2Change.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieRs485SerialPower2")
)
if mibBuilder.loadTexts:
    ruijieRs485Power2Change.setStatus(
        "current"
    )

ruijieRs485Power3Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 3)
)
ruijieRs485Power3Change.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieRs485SerialPower3")
)
if mibBuilder.loadTexts:
    ruijieRs485Power3Change.setStatus(
        "current"
    )

ruijieRs485Power4Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 4)
)
ruijieRs485Power4Change.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieRs485SerialPower4")
)
if mibBuilder.loadTexts:
    ruijieRs485Power4Change.setStatus(
        "current"
    )

ruijieRs485TelnetFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 5)
)
ruijieRs485TelnetFail.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieRs485TelnetIp")
)
if mibBuilder.loadTexts:
    ruijieRs485TelnetFail.setStatus(
        "current"
    )

ruijieLabelActiveACK = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 6)
)
ruijieLabelActiveACK.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieLabelType"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieLabelID"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieLabelActiveStatus"))
)
if mibBuilder.loadTexts:
    ruijieLabelActiveACK.setStatus(
        "current"
    )

ruijieLabelLowPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 7)
)
ruijieLabelLowPower.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieLabelType"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieLabelID"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieLabelPowerStatus"))
)
if mibBuilder.loadTexts:
    ruijieLabelLowPower.setStatus(
        "current"
    )

ruijieLabelStolen = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 8)
)
ruijieLabelStolen.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieLabelType"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieLabelID"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieLabelStolenWarningStatus"))
)
if mibBuilder.loadTexts:
    ruijieLabelStolen.setStatus(
        "current"
    )

ruijieLabelUnregACK = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 9)
)
ruijieLabelUnregACK.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieLabelType"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieLabelID"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieLabelUnregStatus"))
)
if mibBuilder.loadTexts:
    ruijieLabelUnregACK.setStatus(
        "current"
    )

ruijieRs485Heartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 10)
)
ruijieRs485Heartbeat.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieRs485HeartbeatStatus")
)
if mibBuilder.loadTexts:
    ruijieRs485Heartbeat.setStatus(
        "current"
    )

ruijieLabelRegACK = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 11)
)
ruijieLabelRegACK.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieLabelType"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieLabelID"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieLabelUnregStatus"))
)
if mibBuilder.loadTexts:
    ruijieLabelRegACK.setStatus(
        "current"
    )

ruijieClassAPPLoginREQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 12)
)
ruijieClassAPPLoginREQ.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieClassAPPUsername"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassAPPPassword"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassDateTime"))
)
if mibBuilder.loadTexts:
    ruijieClassAPPLoginREQ.setStatus(
        "current"
    )

ruijieClassAPPOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 13)
)
ruijieClassAPPOperation.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieClassDeviceType"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassDeviceID"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassDeviceSwitch"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassDeviceState"))
)
if mibBuilder.loadTexts:
    ruijieClassAPPOperation.setStatus(
        "current"
    )

ruijieClassTelecommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 14)
)
ruijieClassTelecommand.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieClassDeviceType"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassCMDType"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassCommand"))
)
if mibBuilder.loadTexts:
    ruijieClassTelecommand.setStatus(
        "current"
    )

ruijieClassSwipeCard = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 15)
)
ruijieClassSwipeCard.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieClassCardID")
)
if mibBuilder.loadTexts:
    ruijieClassSwipeCard.setStatus(
        "current"
    )

ruijieClassUpdateReq = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 16)
)
ruijieClassUpdateReq.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieClassAPPUpdateReq"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassDateTime"))
)
if mibBuilder.loadTexts:
    ruijieClassUpdateReq.setStatus(
        "current"
    )

ruijieClassOperationAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 17)
)
ruijieClassOperationAll.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieClassOperAll")
)
if mibBuilder.loadTexts:
    ruijieClassOperationAll.setStatus(
        "current"
    )

ruijieClassChannelToServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 18)
)
ruijieClassChannelToServer.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieClassChannel")
)
if mibBuilder.loadTexts:
    ruijieClassChannelToServer.setStatus(
        "current"
    )

ruijieClassDevIPChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 19)
)
ruijieClassDevIPChange.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieClassOldDeviceIP"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieRs485IpAddress"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieRs485Mac"))
)
if mibBuilder.loadTexts:
    ruijieClassDevIPChange.setStatus(
        "current"
    )

ruijieClassCardOperationAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 20)
)
ruijieClassCardOperationAll.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieClassCardID"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassOperAll"))
)
if mibBuilder.loadTexts:
    ruijieClassCardOperationAll.setStatus(
        "current"
    )

ruijieClassAccountOperationAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 21)
)
ruijieClassAccountOperationAll.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieClassAPPUsername"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassAPPPassword"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassOperAll"))
)
if mibBuilder.loadTexts:
    ruijieClassAccountOperationAll.setStatus(
        "current"
    )

ruijieClassTableRedo = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 22)
)
ruijieClassTableRedo.setObjects(
    ("RUIJIE-RS485-CLASS-MIB", "ruijieClassScheduleTableUpdateStatus")
)
if mibBuilder.loadTexts:
    ruijieClassTableRedo.setStatus(
        "current"
    )

ruijieClassDeviceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 149, 2, 23)
)
ruijieClassDeviceStateChange.setObjects(
      *(("RUIJIE-RS485-CLASS-MIB", "ruijieClassDeviceID"),
        ("RUIJIE-RS485-CLASS-MIB", "ruijieClassDeviceState"))
)
if mibBuilder.loadTexts:
    ruijieClassDeviceStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-RS485-CLASS-MIB",
    **{"ruijieRs485MIB": ruijieRs485MIB,
       "ruijieRs485MIBObjects": ruijieRs485MIBObjects,
       "ruijieRs485IpAddress": ruijieRs485IpAddress,
       "ruijieRs485IpAddressMask": ruijieRs485IpAddressMask,
       "ruijieRs485Gateway": ruijieRs485Gateway,
       "ruijieRs485Mac": ruijieRs485Mac,
       "ruijieRs485ServerMode": ruijieRs485ServerMode,
       "ruijieRs485SerialNum": ruijieRs485SerialNum,
       "ruijieRs485TelnetIp": ruijieRs485TelnetIp,
       "ruijieRs485State": ruijieRs485State,
       "ruijieRs485SerialPower1": ruijieRs485SerialPower1,
       "ruijieRs485SerialPower2": ruijieRs485SerialPower2,
       "ruijieRs485SerialPower3": ruijieRs485SerialPower3,
       "ruijieRs485SerialPower4": ruijieRs485SerialPower4,
       "ruijieRs485VlanTable": ruijieRs485VlanTable,
       "ruijieRs485VlanEntry": ruijieRs485VlanEntry,
       "ruijieRs485SerialPort": ruijieRs485SerialPort,
       "ruijieRs485VLANID": ruijieRs485VLANID,
       "ruijieRs485Baudrate": ruijieRs485Baudrate,
       "ruijieRs485Parity": ruijieRs485Parity,
       "ruijieClassSerialType": ruijieClassSerialType,
       "ruijieClassStatus": ruijieClassStatus,
       "ruijieClassIsTeleControl": ruijieClassIsTeleControl,
       "ruijieSSIfTable": ruijieSSIfTable,
       "ruijieSSIfEntry": ruijieSSIfEntry,
       "ruijieSSIfIndex": ruijieSSIfIndex,
       "ruijieSSIfAccessVlan": ruijieSSIfAccessVlan,
       "ruijieSSIfNativeVlan": ruijieSSIfNativeVlan,
       "ruijieSSIfTrunk": ruijieSSIfTrunk,
       "ruijieSSIfSpeed": ruijieSSIfSpeed,
       "ruijieSSIfDuplex": ruijieSSIfDuplex,
       "ruijieSSIfNegotiation": ruijieSSIfNegotiation,
       "ruijieRs485IpSetStatus": ruijieRs485IpSetStatus,
       "ruijieLabelIDReg": ruijieLabelIDReg,
       "ruijieLabelTypeReg": ruijieLabelTypeReg,
       "ruijieLabelRegStatus": ruijieLabelRegStatus,
       "ruijieLabelInfoTable": ruijieLabelInfoTable,
       "ruijieLabelInfoEntry": ruijieLabelInfoEntry,
       "ruijieLabelType": ruijieLabelType,
       "ruijieLabelID": ruijieLabelID,
       "ruijieLabelActiveStatus": ruijieLabelActiveStatus,
       "ruijieLabelPowerStatus": ruijieLabelPowerStatus,
       "ruijieLabelWarningCancel": ruijieLabelWarningCancel,
       "ruijieLabelUnregStatus": ruijieLabelUnregStatus,
       "ruijieLabelStolenWarningStatus": ruijieLabelStolenWarningStatus,
       "ruijieRs485TrapIp": ruijieRs485TrapIp,
       "ruijieRs485HeartbeatStatus": ruijieRs485HeartbeatStatus,
       "ruijieClassPDUPower1": ruijieClassPDUPower1,
       "ruijieClassPDUPower2": ruijieClassPDUPower2,
       "ruijieClassDeviceAddType": ruijieClassDeviceAddType,
       "ruijieClassDeviceAddID": ruijieClassDeviceAddID,
       "ruijieClassDeviceAddStatus": ruijieClassDeviceAddStatus,
       "ruijieClassDeviceInfoTable": ruijieClassDeviceInfoTable,
       "ruijieClassDeviceInfoEntry": ruijieClassDeviceInfoEntry,
       "ruijieClassDeviceType": ruijieClassDeviceType,
       "ruijieClassDeviceID": ruijieClassDeviceID,
       "ruijieClassDeviceIconType": ruijieClassDeviceIconType,
       "ruijieClassDeviceName": ruijieClassDeviceName,
       "ruijieClassDeviceModelID": ruijieClassDeviceModelID,
       "ruijieClassDeviceControlSerial": ruijieClassDeviceControlSerial,
       "ruijieClassDeviceTeleControlPort": ruijieClassDeviceTeleControlPort,
       "ruijieClassDeviceIOType": ruijieClassDeviceIOType,
       "ruijieClassDeviceVideoPort": ruijieClassDeviceVideoPort,
       "ruijieClassDeviceAudioPort": ruijieClassDeviceAudioPort,
       "ruijieClassDeviceVideoUsedStatus": ruijieClassDeviceVideoUsedStatus,
       "ruijieClassDeviceAudioUsedStatus": ruijieClassDeviceAudioUsedStatus,
       "ruijieClassDeviceSwitch": ruijieClassDeviceSwitch,
       "ruijieClassDeviceState": ruijieClassDeviceState,
       "ruijieClassDeviceZigbeeID": ruijieClassDeviceZigbeeID,
       "ruijieClassDeviceSetStatus": ruijieClassDeviceSetStatus,
       "ruijieClassDeviceIP": ruijieClassDeviceIP,
       "ruijieClassBindDeviceID": ruijieClassBindDeviceID,
       "ruijieClassBatchSupport": ruijieClassBatchSupport,
       "ruijieClassAPPUsername": ruijieClassAPPUsername,
       "ruijieClassAPPPassword": ruijieClassAPPPassword,
       "ruijieClassAPPAuth": ruijieClassAPPAuth,
       "ruijieClassCMDDeviceModelID": ruijieClassCMDDeviceModelID,
       "ruijieClassCMDType": ruijieClassCMDType,
       "ruijieClassCommand": ruijieClassCommand,
       "ruijieClassCommandSetStatus": ruijieClassCommandSetStatus,
       "ruijieClassOperAll": ruijieClassOperAll,
       "ruijieClassCardID": ruijieClassCardID,
       "ruijieClassDateTime": ruijieClassDateTime,
       "ruijieClassAPPUpdateReq": ruijieClassAPPUpdateReq,
       "ruijieClassUpdateFileName": ruijieClassUpdateFileName,
       "ruijieClassUpdate": ruijieClassUpdate,
       "ruijieClassSoftVersion": ruijieClassSoftVersion,
       "ruijieClassChannel": ruijieClassChannel,
       "ruijieClassOldDeviceIP": ruijieClassOldDeviceIP,
       "ruijieClassCommunity": ruijieClassCommunity,
       "ruijieClassUpdateStatus": ruijieClassUpdateStatus,
       "ruijieClassScheduleTableName": ruijieClassScheduleTableName,
       "ruijieClassUpdateScheduleTable": ruijieClassUpdateScheduleTable,
       "ruijieClassScheduleTableUpdateStatus": ruijieClassScheduleTableUpdateStatus,
       "ruijieClassCheckTableName": ruijieClassCheckTableName,
       "ruijieClassReadCheckTable": ruijieClassReadCheckTable,
       "ruijieClassReadCheckTable1UploadStatus": ruijieClassReadCheckTable1UploadStatus,
       "ruijieClassLampTimeClass": ruijieClassLampTimeClass,
       "ruijieClassDeleteRecordTable": ruijieClassDeleteRecordTable,
       "ruijieClassSystemTime": ruijieClassSystemTime,
       "ruijieClassProjectorFact": ruijieClassProjectorFact,
       "ruijieClassProjectorModel": ruijieClassProjectorModel,
       "ruijieClassAIOFact": ruijieClassAIOFact,
       "ruijieClassAIOModel": ruijieClassAIOModel,
       "ruijieRs485MIBTrap": ruijieRs485MIBTrap,
       "ruijieRs485StateChange": ruijieRs485StateChange,
       "ruijieRs485Power1Change": ruijieRs485Power1Change,
       "ruijieRs485Power2Change": ruijieRs485Power2Change,
       "ruijieRs485Power3Change": ruijieRs485Power3Change,
       "ruijieRs485Power4Change": ruijieRs485Power4Change,
       "ruijieRs485TelnetFail": ruijieRs485TelnetFail,
       "ruijieLabelActiveACK": ruijieLabelActiveACK,
       "ruijieLabelLowPower": ruijieLabelLowPower,
       "ruijieLabelStolen": ruijieLabelStolen,
       "ruijieLabelUnregACK": ruijieLabelUnregACK,
       "ruijieRs485Heartbeat": ruijieRs485Heartbeat,
       "ruijieLabelRegACK": ruijieLabelRegACK,
       "ruijieClassAPPLoginREQ": ruijieClassAPPLoginREQ,
       "ruijieClassAPPOperation": ruijieClassAPPOperation,
       "ruijieClassTelecommand": ruijieClassTelecommand,
       "ruijieClassSwipeCard": ruijieClassSwipeCard,
       "ruijieClassUpdateReq": ruijieClassUpdateReq,
       "ruijieClassOperationAll": ruijieClassOperationAll,
       "ruijieClassChannelToServer": ruijieClassChannelToServer,
       "ruijieClassDevIPChange": ruijieClassDevIPChange,
       "ruijieClassCardOperationAll": ruijieClassCardOperationAll,
       "ruijieClassAccountOperationAll": ruijieClassAccountOperationAll,
       "ruijieClassTableRedo": ruijieClassTableRedo,
       "ruijieClassDeviceStateChange": ruijieClassDeviceStateChange}
)
