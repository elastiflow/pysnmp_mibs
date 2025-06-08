# SNMP MIB module (DSLite-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/DSLite-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:30:43 2025
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(Natv2InstanceIndex,
 Natv2SubscriberIndex,
 ProtocolNumber) = mibBuilder.importSymbols(
    "NATV2-MIB",
    "Natv2InstanceIndex",
    "Natv2SubscriberIndex",
    "ProtocolNumber")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dsliteMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 240)
)
if mibBuilder.loadTexts:
    dsliteMIB.setRevisions(
        ("2016-05-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DsliteNotifications_ObjectIdentity = ObjectIdentity
dsliteNotifications = _DsliteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 240, 0)
)
_DsliteMIBObjects_ObjectIdentity = ObjectIdentity
dsliteMIBObjects = _DsliteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 240, 1)
)
_DsliteTunnel_ObjectIdentity = ObjectIdentity
dsliteTunnel = _DsliteTunnel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 240, 1, 1)
)
_DsliteTunnelTable_Object = MibTable
dsliteTunnelTable = _DsliteTunnelTable_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dsliteTunnelTable.setStatus("current")
_DsliteTunnelEntry_Object = MibTableRow
dsliteTunnelEntry = _DsliteTunnelEntry_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 1, 1, 1)
)
dsliteTunnelEntry.setIndexNames(
    (0, "DSLite-MIB", "dsliteTunnelAddressType"),
    (0, "DSLite-MIB", "dsliteTunnelStartAddress"),
    (0, "DSLite-MIB", "dsliteTunnelEndAddress"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsliteTunnelEntry.setStatus("current")
_DsliteTunnelAddressType_Type = InetAddressType
_DsliteTunnelAddressType_Object = MibTableColumn
dsliteTunnelAddressType = _DsliteTunnelAddressType_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 1, 1, 1, 1),
    _DsliteTunnelAddressType_Type()
)
dsliteTunnelAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsliteTunnelAddressType.setStatus("current")


class _DsliteTunnelStartAddress_Type(InetAddress):
    """Custom type dsliteTunnelStartAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DsliteTunnelStartAddress_Type.__name__ = "InetAddress"
_DsliteTunnelStartAddress_Object = MibTableColumn
dsliteTunnelStartAddress = _DsliteTunnelStartAddress_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 1, 1, 1, 2),
    _DsliteTunnelStartAddress_Type()
)
dsliteTunnelStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsliteTunnelStartAddress.setStatus("current")


class _DsliteTunnelEndAddress_Type(InetAddress):
    """Custom type dsliteTunnelEndAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DsliteTunnelEndAddress_Type.__name__ = "InetAddress"
_DsliteTunnelEndAddress_Object = MibTableColumn
dsliteTunnelEndAddress = _DsliteTunnelEndAddress_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 1, 1, 1, 3),
    _DsliteTunnelEndAddress_Type()
)
dsliteTunnelEndAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsliteTunnelEndAddress.setStatus("current")
_DsliteTunnelStartAddPreLen_Type = InetAddressPrefixLength
_DsliteTunnelStartAddPreLen_Object = MibTableColumn
dsliteTunnelStartAddPreLen = _DsliteTunnelStartAddPreLen_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 1, 1, 1, 4),
    _DsliteTunnelStartAddPreLen_Type()
)
dsliteTunnelStartAddPreLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteTunnelStartAddPreLen.setStatus("current")
_DsliteNAT_ObjectIdentity = ObjectIdentity
dsliteNAT = _DsliteNAT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 240, 1, 2)
)
_DsliteNATBindTable_Object = MibTable
dsliteNATBindTable = _DsliteNATBindTable_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsliteNATBindTable.setStatus("current")
_DsliteNATBindEntry_Object = MibTableRow
dsliteNATBindEntry = _DsliteNATBindEntry_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1)
)
dsliteNATBindEntry.setIndexNames(
    (0, "DSLite-MIB", "dsliteNATBindMappingInstanceIndex"),
    (0, "DSLite-MIB", "dsliteNATBindMappingProto"),
    (0, "DSLite-MIB", "dsliteNATBindMappingExtRealm"),
    (0, "DSLite-MIB", "dsliteNATBindMappingExtAddressType"),
    (0, "DSLite-MIB", "dsliteNATBindMappingExtAddress"),
    (0, "DSLite-MIB", "dsliteNATBindMappingExtPort"),
    (0, "IF-MIB", "ifIndex"),
    (0, "DSLite-MIB", "dsliteTunnelStartAddress"),
)
if mibBuilder.loadTexts:
    dsliteNATBindEntry.setStatus("current")
_DsliteNATBindMappingInstanceIndex_Type = Natv2InstanceIndex
_DsliteNATBindMappingInstanceIndex_Object = MibTableColumn
dsliteNATBindMappingInstanceIndex = _DsliteNATBindMappingInstanceIndex_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 1),
    _DsliteNATBindMappingInstanceIndex_Type()
)
dsliteNATBindMappingInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsliteNATBindMappingInstanceIndex.setStatus("current")
_DsliteNATBindMappingProto_Type = ProtocolNumber
_DsliteNATBindMappingProto_Object = MibTableColumn
dsliteNATBindMappingProto = _DsliteNATBindMappingProto_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 2),
    _DsliteNATBindMappingProto_Type()
)
dsliteNATBindMappingProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsliteNATBindMappingProto.setStatus("current")


class _DsliteNATBindMappingExtRealm_Type(SnmpAdminString):
    """Custom type dsliteNATBindMappingExtRealm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsliteNATBindMappingExtRealm_Type.__name__ = "SnmpAdminString"
_DsliteNATBindMappingExtRealm_Object = MibTableColumn
dsliteNATBindMappingExtRealm = _DsliteNATBindMappingExtRealm_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 3),
    _DsliteNATBindMappingExtRealm_Type()
)
dsliteNATBindMappingExtRealm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsliteNATBindMappingExtRealm.setStatus("current")
_DsliteNATBindMappingExtAddressType_Type = InetAddressType
_DsliteNATBindMappingExtAddressType_Object = MibTableColumn
dsliteNATBindMappingExtAddressType = _DsliteNATBindMappingExtAddressType_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 4),
    _DsliteNATBindMappingExtAddressType_Type()
)
dsliteNATBindMappingExtAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsliteNATBindMappingExtAddressType.setStatus("current")


class _DsliteNATBindMappingExtAddress_Type(InetAddress):
    """Custom type dsliteNATBindMappingExtAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_DsliteNATBindMappingExtAddress_Type.__name__ = "InetAddress"
_DsliteNATBindMappingExtAddress_Object = MibTableColumn
dsliteNATBindMappingExtAddress = _DsliteNATBindMappingExtAddress_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 5),
    _DsliteNATBindMappingExtAddress_Type()
)
dsliteNATBindMappingExtAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsliteNATBindMappingExtAddress.setStatus("current")
_DsliteNATBindMappingExtPort_Type = InetPortNumber
_DsliteNATBindMappingExtPort_Object = MibTableColumn
dsliteNATBindMappingExtPort = _DsliteNATBindMappingExtPort_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 6),
    _DsliteNATBindMappingExtPort_Type()
)
dsliteNATBindMappingExtPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsliteNATBindMappingExtPort.setStatus("current")


class _DsliteNATBindMappingIntRealm_Type(SnmpAdminString):
    """Custom type dsliteNATBindMappingIntRealm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DsliteNATBindMappingIntRealm_Type.__name__ = "SnmpAdminString"
_DsliteNATBindMappingIntRealm_Object = MibTableColumn
dsliteNATBindMappingIntRealm = _DsliteNATBindMappingIntRealm_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 7),
    _DsliteNATBindMappingIntRealm_Type()
)
dsliteNATBindMappingIntRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteNATBindMappingIntRealm.setStatus("current")
_DsliteNATBindMappingIntAddressType_Type = InetAddressType
_DsliteNATBindMappingIntAddressType_Object = MibTableColumn
dsliteNATBindMappingIntAddressType = _DsliteNATBindMappingIntAddressType_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 8),
    _DsliteNATBindMappingIntAddressType_Type()
)
dsliteNATBindMappingIntAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteNATBindMappingIntAddressType.setStatus("current")
_DsliteNATBindMappingIntAddress_Type = InetAddress
_DsliteNATBindMappingIntAddress_Object = MibTableColumn
dsliteNATBindMappingIntAddress = _DsliteNATBindMappingIntAddress_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 9),
    _DsliteNATBindMappingIntAddress_Type()
)
dsliteNATBindMappingIntAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteNATBindMappingIntAddress.setStatus("current")
_DsliteNATBindMappingIntPort_Type = InetPortNumber
_DsliteNATBindMappingIntPort_Object = MibTableColumn
dsliteNATBindMappingIntPort = _DsliteNATBindMappingIntPort_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 10),
    _DsliteNATBindMappingIntPort_Type()
)
dsliteNATBindMappingIntPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteNATBindMappingIntPort.setStatus("current")


class _DsliteNATBindMappingPool_Type(Unsigned32):
    """Custom type dsliteNATBindMappingPool based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_DsliteNATBindMappingPool_Type.__name__ = "Unsigned32"
_DsliteNATBindMappingPool_Object = MibTableColumn
dsliteNATBindMappingPool = _DsliteNATBindMappingPool_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 11),
    _DsliteNATBindMappingPool_Type()
)
dsliteNATBindMappingPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteNATBindMappingPool.setStatus("current")


class _DsliteNATBindMappingMapBehavior_Type(Integer32):
    """Custom type dsliteNATBindMappingMapBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endpointIndependent", 0),
          ("addressDependent", 1),
          ("addressAndPortDependent", 2))
    )


_DsliteNATBindMappingMapBehavior_Type.__name__ = "Integer32"
_DsliteNATBindMappingMapBehavior_Object = MibTableColumn
dsliteNATBindMappingMapBehavior = _DsliteNATBindMappingMapBehavior_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 12),
    _DsliteNATBindMappingMapBehavior_Type()
)
dsliteNATBindMappingMapBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteNATBindMappingMapBehavior.setStatus("current")


class _DsliteNATBindMappingFilterBehavior_Type(Integer32):
    """Custom type dsliteNATBindMappingFilterBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endpointIndependent", 0),
          ("addressDependent", 1),
          ("addressAndPortDependent", 2))
    )


_DsliteNATBindMappingFilterBehavior_Type.__name__ = "Integer32"
_DsliteNATBindMappingFilterBehavior_Object = MibTableColumn
dsliteNATBindMappingFilterBehavior = _DsliteNATBindMappingFilterBehavior_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 13),
    _DsliteNATBindMappingFilterBehavior_Type()
)
dsliteNATBindMappingFilterBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteNATBindMappingFilterBehavior.setStatus("current")


class _DsliteNATBindMappingAddressPooling_Type(Integer32):
    """Custom type dsliteNATBindMappingAddressPooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arbitrary", 0),
          ("paired", 1))
    )


_DsliteNATBindMappingAddressPooling_Type.__name__ = "Integer32"
_DsliteNATBindMappingAddressPooling_Object = MibTableColumn
dsliteNATBindMappingAddressPooling = _DsliteNATBindMappingAddressPooling_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 2, 1, 1, 14),
    _DsliteNATBindMappingAddressPooling_Type()
)
dsliteNATBindMappingAddressPooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteNATBindMappingAddressPooling.setStatus("current")
_DsliteInfo_ObjectIdentity = ObjectIdentity
dsliteInfo = _DsliteInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 240, 1, 3)
)
_DsliteAFTRAlarmScalar_ObjectIdentity = ObjectIdentity
dsliteAFTRAlarmScalar = _DsliteAFTRAlarmScalar_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 1)
)
_DsliteAFTRAlarmB4AddrType_Type = InetAddressType
_DsliteAFTRAlarmB4AddrType_Object = MibScalar
dsliteAFTRAlarmB4AddrType = _DsliteAFTRAlarmB4AddrType_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 1, 1),
    _DsliteAFTRAlarmB4AddrType_Type()
)
dsliteAFTRAlarmB4AddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dsliteAFTRAlarmB4AddrType.setStatus("current")
_DsliteAFTRAlarmB4Addr_Type = InetAddress
_DsliteAFTRAlarmB4Addr_Object = MibScalar
dsliteAFTRAlarmB4Addr = _DsliteAFTRAlarmB4Addr_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 1, 2),
    _DsliteAFTRAlarmB4Addr_Type()
)
dsliteAFTRAlarmB4Addr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dsliteAFTRAlarmB4Addr.setStatus("current")


class _DsliteAFTRAlarmProtocolType_Type(Integer32):
    """Custom type dsliteAFTRAlarmProtocolType based on Integer32"""
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
        *(("tcp", 0),
          ("udp", 1),
          ("icmp", 2),
          ("total", 3))
    )


_DsliteAFTRAlarmProtocolType_Type.__name__ = "Integer32"
_DsliteAFTRAlarmProtocolType_Object = MibScalar
dsliteAFTRAlarmProtocolType = _DsliteAFTRAlarmProtocolType_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 1, 3),
    _DsliteAFTRAlarmProtocolType_Type()
)
dsliteAFTRAlarmProtocolType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dsliteAFTRAlarmProtocolType.setStatus("current")
_DsliteAFTRAlarmSpecificIPAddrType_Type = InetAddressType
_DsliteAFTRAlarmSpecificIPAddrType_Object = MibScalar
dsliteAFTRAlarmSpecificIPAddrType = _DsliteAFTRAlarmSpecificIPAddrType_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 1, 4),
    _DsliteAFTRAlarmSpecificIPAddrType_Type()
)
dsliteAFTRAlarmSpecificIPAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dsliteAFTRAlarmSpecificIPAddrType.setStatus("current")
_DsliteAFTRAlarmSpecificIP_Type = InetAddress
_DsliteAFTRAlarmSpecificIP_Object = MibScalar
dsliteAFTRAlarmSpecificIP = _DsliteAFTRAlarmSpecificIP_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 1, 5),
    _DsliteAFTRAlarmSpecificIP_Type()
)
dsliteAFTRAlarmSpecificIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dsliteAFTRAlarmSpecificIP.setStatus("current")


class _DsliteAFTRAlarmConnectNumber_Type(Integer32):
    """Custom type dsliteAFTRAlarmConnectNumber based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 90),
    )


_DsliteAFTRAlarmConnectNumber_Type.__name__ = "Integer32"
_DsliteAFTRAlarmConnectNumber_Object = MibScalar
dsliteAFTRAlarmConnectNumber = _DsliteAFTRAlarmConnectNumber_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 1, 6),
    _DsliteAFTRAlarmConnectNumber_Type()
)
dsliteAFTRAlarmConnectNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsliteAFTRAlarmConnectNumber.setStatus("current")


class _DsliteAFTRAlarmSessionNumber_Type(Integer32):
    """Custom type dsliteAFTRAlarmSessionNumber based on Integer32"""
    defaultValue = -1


_DsliteAFTRAlarmSessionNumber_Type.__name__ = "Integer32"
_DsliteAFTRAlarmSessionNumber_Object = MibScalar
dsliteAFTRAlarmSessionNumber = _DsliteAFTRAlarmSessionNumber_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 1, 7),
    _DsliteAFTRAlarmSessionNumber_Type()
)
dsliteAFTRAlarmSessionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsliteAFTRAlarmSessionNumber.setStatus("current")


class _DsliteAFTRAlarmPortNumber_Type(Integer32):
    """Custom type dsliteAFTRAlarmPortNumber based on Integer32"""
    defaultValue = -1


_DsliteAFTRAlarmPortNumber_Type.__name__ = "Integer32"
_DsliteAFTRAlarmPortNumber_Object = MibScalar
dsliteAFTRAlarmPortNumber = _DsliteAFTRAlarmPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 1, 8),
    _DsliteAFTRAlarmPortNumber_Type()
)
dsliteAFTRAlarmPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsliteAFTRAlarmPortNumber.setStatus("current")
_DsliteStatisticsTable_Object = MibTable
dsliteStatisticsTable = _DsliteStatisticsTable_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dsliteStatisticsTable.setStatus("current")
_DsliteStatisticsEntry_Object = MibTableRow
dsliteStatisticsEntry = _DsliteStatisticsEntry_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 2, 1)
)
dsliteStatisticsEntry.setIndexNames(
    (0, "DSLite-MIB", "dsliteStatisticsSubscriberIndex"),
)
if mibBuilder.loadTexts:
    dsliteStatisticsEntry.setStatus("current")
_DsliteStatisticsSubscriberIndex_Type = Natv2SubscriberIndex
_DsliteStatisticsSubscriberIndex_Object = MibTableColumn
dsliteStatisticsSubscriberIndex = _DsliteStatisticsSubscriberIndex_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 2, 1, 1),
    _DsliteStatisticsSubscriberIndex_Type()
)
dsliteStatisticsSubscriberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsliteStatisticsSubscriberIndex.setStatus("current")
_DsliteStatisticsDiscards_Type = Counter64
_DsliteStatisticsDiscards_Object = MibTableColumn
dsliteStatisticsDiscards = _DsliteStatisticsDiscards_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 2, 1, 2),
    _DsliteStatisticsDiscards_Type()
)
dsliteStatisticsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteStatisticsDiscards.setStatus("current")
_DsliteStatisticsSends_Type = Counter64
_DsliteStatisticsSends_Object = MibTableColumn
dsliteStatisticsSends = _DsliteStatisticsSends_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 2, 1, 3),
    _DsliteStatisticsSends_Type()
)
dsliteStatisticsSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteStatisticsSends.setStatus("current")
_DsliteStatisticsReceives_Type = Counter64
_DsliteStatisticsReceives_Object = MibTableColumn
dsliteStatisticsReceives = _DsliteStatisticsReceives_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 2, 1, 4),
    _DsliteStatisticsReceives_Type()
)
dsliteStatisticsReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteStatisticsReceives.setStatus("current")
_DsliteStatisticsIpv4Session_Type = Counter64
_DsliteStatisticsIpv4Session_Object = MibTableColumn
dsliteStatisticsIpv4Session = _DsliteStatisticsIpv4Session_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 2, 1, 5),
    _DsliteStatisticsIpv4Session_Type()
)
dsliteStatisticsIpv4Session.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteStatisticsIpv4Session.setStatus("current")
_DsliteStatisticsIpv6Session_Type = Counter64
_DsliteStatisticsIpv6Session_Object = MibTableColumn
dsliteStatisticsIpv6Session = _DsliteStatisticsIpv6Session_Object(
    (1, 3, 6, 1, 2, 1, 240, 1, 3, 2, 1, 6),
    _DsliteStatisticsIpv6Session_Type()
)
dsliteStatisticsIpv6Session.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsliteStatisticsIpv6Session.setStatus("current")
_DsliteConformance_ObjectIdentity = ObjectIdentity
dsliteConformance = _DsliteConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 240, 2)
)
_DsliteCompliances_ObjectIdentity = ObjectIdentity
dsliteCompliances = _DsliteCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 240, 2, 1)
)
_DsliteGroups_ObjectIdentity = ObjectIdentity
dsliteGroups = _DsliteGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 240, 2, 2)
)

# Managed Objects groups

dsliteNATBindGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 240, 2, 2, 1)
)
dsliteNATBindGroup.setObjects(
      *(("DSLite-MIB", "dsliteNATBindMappingIntRealm"),
        ("DSLite-MIB", "dsliteNATBindMappingIntAddressType"),
        ("DSLite-MIB", "dsliteNATBindMappingIntAddress"),
        ("DSLite-MIB", "dsliteNATBindMappingIntPort"),
        ("DSLite-MIB", "dsliteNATBindMappingPool"),
        ("DSLite-MIB", "dsliteNATBindMappingMapBehavior"),
        ("DSLite-MIB", "dsliteNATBindMappingFilterBehavior"),
        ("DSLite-MIB", "dsliteNATBindMappingAddressPooling"))
)
if mibBuilder.loadTexts:
    dsliteNATBindGroup.setStatus("current")

dsliteTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 240, 2, 2, 2)
)
dsliteTunnelGroup.setObjects(
    ("DSLite-MIB", "dsliteTunnelStartAddPreLen")
)
if mibBuilder.loadTexts:
    dsliteTunnelGroup.setStatus("current")

dsliteStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 240, 2, 2, 3)
)
dsliteStatisticsGroup.setObjects(
      *(("DSLite-MIB", "dsliteStatisticsDiscards"),
        ("DSLite-MIB", "dsliteStatisticsSends"),
        ("DSLite-MIB", "dsliteStatisticsReceives"),
        ("DSLite-MIB", "dsliteStatisticsIpv4Session"),
        ("DSLite-MIB", "dsliteStatisticsIpv6Session"))
)
if mibBuilder.loadTexts:
    dsliteStatisticsGroup.setStatus("current")

dsliteAFTRAlarmScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 240, 2, 2, 5)
)
dsliteAFTRAlarmScalarGroup.setObjects(
      *(("DSLite-MIB", "dsliteAFTRAlarmB4AddrType"),
        ("DSLite-MIB", "dsliteAFTRAlarmB4Addr"),
        ("DSLite-MIB", "dsliteAFTRAlarmProtocolType"),
        ("DSLite-MIB", "dsliteAFTRAlarmSpecificIPAddrType"),
        ("DSLite-MIB", "dsliteAFTRAlarmSpecificIP"),
        ("DSLite-MIB", "dsliteAFTRAlarmConnectNumber"),
        ("DSLite-MIB", "dsliteAFTRAlarmSessionNumber"),
        ("DSLite-MIB", "dsliteAFTRAlarmPortNumber"))
)
if mibBuilder.loadTexts:
    dsliteAFTRAlarmScalarGroup.setStatus("current")


# Notification objects

dsliteTunnelNumAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 240, 0, 1)
)
dsliteTunnelNumAlarm.setObjects(
      *(("DSLite-MIB", "dsliteAFTRAlarmProtocolType"),
        ("DSLite-MIB", "dsliteAFTRAlarmB4AddrType"),
        ("DSLite-MIB", "dsliteAFTRAlarmB4Addr"))
)
if mibBuilder.loadTexts:
    dsliteTunnelNumAlarm.setStatus(
        "current"
    )

dsliteAFTRUserSessionNumAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 240, 0, 2)
)
dsliteAFTRUserSessionNumAlarm.setObjects(
      *(("DSLite-MIB", "dsliteAFTRAlarmProtocolType"),
        ("DSLite-MIB", "dsliteAFTRAlarmB4AddrType"),
        ("DSLite-MIB", "dsliteAFTRAlarmB4Addr"))
)
if mibBuilder.loadTexts:
    dsliteAFTRUserSessionNumAlarm.setStatus(
        "current"
    )

dsliteAFTRPortUsageOfSpecificIpAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 240, 0, 3)
)
dsliteAFTRPortUsageOfSpecificIpAlarm.setObjects(
      *(("DSLite-MIB", "dsliteAFTRAlarmSpecificIPAddrType"),
        ("DSLite-MIB", "dsliteAFTRAlarmSpecificIP"))
)
if mibBuilder.loadTexts:
    dsliteAFTRPortUsageOfSpecificIpAlarm.setStatus(
        "current"
    )


# Notifications groups

dsliteNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 240, 2, 2, 4)
)
dsliteNotificationsGroup.setObjects(
      *(("DSLite-MIB", "dsliteTunnelNumAlarm"),
        ("DSLite-MIB", "dsliteAFTRUserSessionNumAlarm"),
        ("DSLite-MIB", "dsliteAFTRPortUsageOfSpecificIpAlarm"))
)
if mibBuilder.loadTexts:
    dsliteNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dsliteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 240, 2, 1, 1)
)
dsliteCompliance.setObjects(
      *(("DSLite-MIB", "dsliteNATBindGroup"),
        ("DSLite-MIB", "dsliteTunnelGroup"),
        ("DSLite-MIB", "dsliteStatisticsGroup"),
        ("DSLite-MIB", "dsliteNotificationsGroup"),
        ("DSLite-MIB", "dsliteAFTRAlarmScalarGroup"))
)
if mibBuilder.loadTexts:
    dsliteCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSLite-MIB",
    **{"dsliteMIB": dsliteMIB,
       "dsliteNotifications": dsliteNotifications,
       "dsliteTunnelNumAlarm": dsliteTunnelNumAlarm,
       "dsliteAFTRUserSessionNumAlarm": dsliteAFTRUserSessionNumAlarm,
       "dsliteAFTRPortUsageOfSpecificIpAlarm": dsliteAFTRPortUsageOfSpecificIpAlarm,
       "dsliteMIBObjects": dsliteMIBObjects,
       "dsliteTunnel": dsliteTunnel,
       "dsliteTunnelTable": dsliteTunnelTable,
       "dsliteTunnelEntry": dsliteTunnelEntry,
       "dsliteTunnelAddressType": dsliteTunnelAddressType,
       "dsliteTunnelStartAddress": dsliteTunnelStartAddress,
       "dsliteTunnelEndAddress": dsliteTunnelEndAddress,
       "dsliteTunnelStartAddPreLen": dsliteTunnelStartAddPreLen,
       "dsliteNAT": dsliteNAT,
       "dsliteNATBindTable": dsliteNATBindTable,
       "dsliteNATBindEntry": dsliteNATBindEntry,
       "dsliteNATBindMappingInstanceIndex": dsliteNATBindMappingInstanceIndex,
       "dsliteNATBindMappingProto": dsliteNATBindMappingProto,
       "dsliteNATBindMappingExtRealm": dsliteNATBindMappingExtRealm,
       "dsliteNATBindMappingExtAddressType": dsliteNATBindMappingExtAddressType,
       "dsliteNATBindMappingExtAddress": dsliteNATBindMappingExtAddress,
       "dsliteNATBindMappingExtPort": dsliteNATBindMappingExtPort,
       "dsliteNATBindMappingIntRealm": dsliteNATBindMappingIntRealm,
       "dsliteNATBindMappingIntAddressType": dsliteNATBindMappingIntAddressType,
       "dsliteNATBindMappingIntAddress": dsliteNATBindMappingIntAddress,
       "dsliteNATBindMappingIntPort": dsliteNATBindMappingIntPort,
       "dsliteNATBindMappingPool": dsliteNATBindMappingPool,
       "dsliteNATBindMappingMapBehavior": dsliteNATBindMappingMapBehavior,
       "dsliteNATBindMappingFilterBehavior": dsliteNATBindMappingFilterBehavior,
       "dsliteNATBindMappingAddressPooling": dsliteNATBindMappingAddressPooling,
       "dsliteInfo": dsliteInfo,
       "dsliteAFTRAlarmScalar": dsliteAFTRAlarmScalar,
       "dsliteAFTRAlarmB4AddrType": dsliteAFTRAlarmB4AddrType,
       "dsliteAFTRAlarmB4Addr": dsliteAFTRAlarmB4Addr,
       "dsliteAFTRAlarmProtocolType": dsliteAFTRAlarmProtocolType,
       "dsliteAFTRAlarmSpecificIPAddrType": dsliteAFTRAlarmSpecificIPAddrType,
       "dsliteAFTRAlarmSpecificIP": dsliteAFTRAlarmSpecificIP,
       "dsliteAFTRAlarmConnectNumber": dsliteAFTRAlarmConnectNumber,
       "dsliteAFTRAlarmSessionNumber": dsliteAFTRAlarmSessionNumber,
       "dsliteAFTRAlarmPortNumber": dsliteAFTRAlarmPortNumber,
       "dsliteStatisticsTable": dsliteStatisticsTable,
       "dsliteStatisticsEntry": dsliteStatisticsEntry,
       "dsliteStatisticsSubscriberIndex": dsliteStatisticsSubscriberIndex,
       "dsliteStatisticsDiscards": dsliteStatisticsDiscards,
       "dsliteStatisticsSends": dsliteStatisticsSends,
       "dsliteStatisticsReceives": dsliteStatisticsReceives,
       "dsliteStatisticsIpv4Session": dsliteStatisticsIpv4Session,
       "dsliteStatisticsIpv6Session": dsliteStatisticsIpv6Session,
       "dsliteConformance": dsliteConformance,
       "dsliteCompliances": dsliteCompliances,
       "dsliteCompliance": dsliteCompliance,
       "dsliteGroups": dsliteGroups,
       "dsliteNATBindGroup": dsliteNATBindGroup,
       "dsliteTunnelGroup": dsliteTunnelGroup,
       "dsliteStatisticsGroup": dsliteStatisticsGroup,
       "dsliteNotificationsGroup": dsliteNotificationsGroup,
       "dsliteAFTRAlarmScalarGroup": dsliteAFTRAlarmScalarGroup}
)
