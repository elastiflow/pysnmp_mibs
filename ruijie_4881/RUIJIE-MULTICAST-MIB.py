# SNMP MIB module (RUIJIE-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-MULTICAST-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:06 2025
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

(IANAipMRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieMultMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28)
)
if mibBuilder.loadTexts:
    ruijieMultMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieMultMIBObjects_ObjectIdentity = ObjectIdentity
ruijieMultMIBObjects = _RuijieMultMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1)
)
_RuijieIpMRouteInterfaceTable_Object = MibTable
ruijieIpMRouteInterfaceTable = _RuijieIpMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceTable.setStatus("current")
_RuijieIpMRouteInterfaceEntry_Object = MibTableRow
ruijieIpMRouteInterfaceEntry = _RuijieIpMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1, 1)
)
ruijieIpMRouteInterfaceEntry.setIndexNames(
    (0, "RUIJIE-MULTICAST-MIB", "ruijieIpMRouteInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceEntry.setStatus("current")
_RuijieIpMRouteInterfaceIfIndex_Type = InterfaceIndex
_RuijieIpMRouteInterfaceIfIndex_Object = MibTableColumn
ruijieIpMRouteInterfaceIfIndex = _RuijieIpMRouteInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1, 1, 1),
    _RuijieIpMRouteInterfaceIfIndex_Type()
)
ruijieIpMRouteInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceIfIndex.setStatus("current")


class _RuijieIpMRouteInterfaceTtl_Type(Integer32):
    """Custom type ruijieIpMRouteInterfaceTtl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieIpMRouteInterfaceTtl_Type.__name__ = "Integer32"
_RuijieIpMRouteInterfaceTtl_Object = MibTableColumn
ruijieIpMRouteInterfaceTtl = _RuijieIpMRouteInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1, 1, 2),
    _RuijieIpMRouteInterfaceTtl_Type()
)
ruijieIpMRouteInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceTtl.setStatus("current")
_RuijieIpMRouteInterfaceProtocol_Type = IANAipMRouteProtocol
_RuijieIpMRouteInterfaceProtocol_Object = MibTableColumn
ruijieIpMRouteInterfaceProtocol = _RuijieIpMRouteInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1, 1, 3),
    _RuijieIpMRouteInterfaceProtocol_Type()
)
ruijieIpMRouteInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceProtocol.setStatus("current")


class _RuijieIpMRouteInterfaceRateLimit_Type(Integer32):
    """Custom type ruijieIpMRouteInterfaceRateLimit based on Integer32"""
    defaultValue = 0


_RuijieIpMRouteInterfaceRateLimit_Type.__name__ = "Integer32"
_RuijieIpMRouteInterfaceRateLimit_Object = MibTableColumn
ruijieIpMRouteInterfaceRateLimit = _RuijieIpMRouteInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1, 1, 4),
    _RuijieIpMRouteInterfaceRateLimit_Type()
)
ruijieIpMRouteInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceRateLimit.setStatus("current")
_RuijieIpMRouteInterfaceInMcastOctets_Type = Counter32
_RuijieIpMRouteInterfaceInMcastOctets_Object = MibTableColumn
ruijieIpMRouteInterfaceInMcastOctets = _RuijieIpMRouteInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1, 1, 5),
    _RuijieIpMRouteInterfaceInMcastOctets_Type()
)
ruijieIpMRouteInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceInMcastOctets.setStatus("current")
_RuijieIpMRouteInterfaceOutMcastOctets_Type = Counter32
_RuijieIpMRouteInterfaceOutMcastOctets_Object = MibTableColumn
ruijieIpMRouteInterfaceOutMcastOctets = _RuijieIpMRouteInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1, 1, 6),
    _RuijieIpMRouteInterfaceOutMcastOctets_Type()
)
ruijieIpMRouteInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceOutMcastOctets.setStatus("current")
_RuijieIpMRouteInterfaceHCInMcastOctets_Type = Counter64
_RuijieIpMRouteInterfaceHCInMcastOctets_Object = MibTableColumn
ruijieIpMRouteInterfaceHCInMcastOctets = _RuijieIpMRouteInterfaceHCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1, 1, 7),
    _RuijieIpMRouteInterfaceHCInMcastOctets_Type()
)
ruijieIpMRouteInterfaceHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceHCInMcastOctets.setStatus("current")
_RuijieIpMRouteInterfaceHCOutMcastOctets_Type = Counter64
_RuijieIpMRouteInterfaceHCOutMcastOctets_Object = MibTableColumn
ruijieIpMRouteInterfaceHCOutMcastOctets = _RuijieIpMRouteInterfaceHCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1, 1, 8),
    _RuijieIpMRouteInterfaceHCOutMcastOctets_Type()
)
ruijieIpMRouteInterfaceHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceHCOutMcastOctets.setStatus("current")
_RuijieIpMRouteBoundaryAclName_Type = DisplayString
_RuijieIpMRouteBoundaryAclName_Object = MibTableColumn
ruijieIpMRouteBoundaryAclName = _RuijieIpMRouteBoundaryAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 1, 1, 9),
    _RuijieIpMRouteBoundaryAclName_Type()
)
ruijieIpMRouteBoundaryAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIpMRouteBoundaryAclName.setStatus("current")
_RuijieIpRpfTable_Object = MibTable
ruijieIpRpfTable = _RuijieIpRpfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieIpRpfTable.setStatus("current")
_RuijieIpRpfEntry_Object = MibTableRow
ruijieIpRpfEntry = _RuijieIpRpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 2, 1)
)
ruijieIpRpfEntry.setIndexNames(
    (0, "RUIJIE-MULTICAST-MIB", "ruijieIpRpfSourceAddress"),
)
if mibBuilder.loadTexts:
    ruijieIpRpfEntry.setStatus("current")
_RuijieIpRpfSourceAddress_Type = IpAddress
_RuijieIpRpfSourceAddress_Object = MibTableColumn
ruijieIpRpfSourceAddress = _RuijieIpRpfSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 2, 1, 1),
    _RuijieIpRpfSourceAddress_Type()
)
ruijieIpRpfSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIpRpfSourceAddress.setStatus("current")
_RuijieIpRpfInterface_Type = InterfaceIndex
_RuijieIpRpfInterface_Object = MibTableColumn
ruijieIpRpfInterface = _RuijieIpRpfInterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 2, 1, 2),
    _RuijieIpRpfInterface_Type()
)
ruijieIpRpfInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpRpfInterface.setStatus("current")
_RuijieIpRpfNeighborAddress_Type = IpAddress
_RuijieIpRpfNeighborAddress_Object = MibTableColumn
ruijieIpRpfNeighborAddress = _RuijieIpRpfNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 2, 1, 3),
    _RuijieIpRpfNeighborAddress_Type()
)
ruijieIpRpfNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpRpfNeighborAddress.setStatus("current")
_RuijieIpRpfRouteAddress_Type = IpAddress
_RuijieIpRpfRouteAddress_Object = MibTableColumn
ruijieIpRpfRouteAddress = _RuijieIpRpfRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 2, 1, 4),
    _RuijieIpRpfRouteAddress_Type()
)
ruijieIpRpfRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpRpfRouteAddress.setStatus("current")
_RuijieIpRpfRouteMask_Type = IpAddress
_RuijieIpRpfRouteMask_Object = MibTableColumn
ruijieIpRpfRouteMask = _RuijieIpRpfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 2, 1, 5),
    _RuijieIpRpfRouteMask_Type()
)
ruijieIpRpfRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpRpfRouteMask.setStatus("current")


class _RuijieIpRpfType_Type(Integer32):
    """Custom type ruijieIpRpfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("dvmrp", 2))
    )


_RuijieIpRpfType_Type.__name__ = "Integer32"
_RuijieIpRpfType_Object = MibTableColumn
ruijieIpRpfType = _RuijieIpRpfType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 2, 1, 6),
    _RuijieIpRpfType_Type()
)
ruijieIpRpfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpRpfType.setStatus("current")
_RuijieMPingTable_Object = MibTable
ruijieMPingTable = _RuijieMPingTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieMPingTable.setStatus("current")
_RuijieMPingEntry_Object = MibTableRow
ruijieMPingEntry = _RuijieMPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 3, 1)
)
ruijieMPingEntry.setIndexNames(
    (0, "RUIJIE-MULTICAST-MIB", "ruijieMPingIndex"),
    (0, "RUIJIE-MULTICAST-MIB", "ruijieMPingGroupAddress"),
    (0, "RUIJIE-MULTICAST-MIB", "ruijieMPingGroupMember"),
)
if mibBuilder.loadTexts:
    ruijieMPingEntry.setStatus("current")


class _RuijieMPingIndex_Type(Integer32):
    """Custom type ruijieMPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieMPingIndex_Type.__name__ = "Integer32"
_RuijieMPingIndex_Object = MibTableColumn
ruijieMPingIndex = _RuijieMPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 3, 1, 1),
    _RuijieMPingIndex_Type()
)
ruijieMPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieMPingIndex.setStatus("current")
_RuijieMPingGroupAddress_Type = IpAddress
_RuijieMPingGroupAddress_Object = MibTableColumn
ruijieMPingGroupAddress = _RuijieMPingGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 3, 1, 2),
    _RuijieMPingGroupAddress_Type()
)
ruijieMPingGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieMPingGroupAddress.setStatus("current")
_RuijieMPingGroupMember_Type = IpAddress
_RuijieMPingGroupMember_Object = MibTableColumn
ruijieMPingGroupMember = _RuijieMPingGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 3, 1, 3),
    _RuijieMPingGroupMember_Type()
)
ruijieMPingGroupMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieMPingGroupMember.setStatus("current")
_RuijieMPingResponseTime_Type = TimeTicks
_RuijieMPingResponseTime_Object = MibTableColumn
ruijieMPingResponseTime = _RuijieMPingResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 3, 1, 4),
    _RuijieMPingResponseTime_Type()
)
ruijieMPingResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPingResponseTime.setStatus("current")


class _RuijieMPingDataLength_Type(Unsigned32):
    """Custom type ruijieMPingDataLength based on Unsigned32"""
    defaultValue = 1500


_RuijieMPingDataLength_Type.__name__ = "Unsigned32"
_RuijieMPingDataLength_Object = MibTableColumn
ruijieMPingDataLength = _RuijieMPingDataLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 3, 1, 5),
    _RuijieMPingDataLength_Type()
)
ruijieMPingDataLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMPingDataLength.setStatus("current")


class _RuijieMPingTimeOuts_Type(Unsigned32):
    """Custom type ruijieMPingTimeOuts based on Unsigned32"""
    defaultValue = 1000


_RuijieMPingTimeOuts_Type.__name__ = "Unsigned32"
_RuijieMPingTimeOuts_Object = MibTableColumn
ruijieMPingTimeOuts = _RuijieMPingTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 3, 1, 6),
    _RuijieMPingTimeOuts_Type()
)
ruijieMPingTimeOuts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMPingTimeOuts.setStatus("current")
_RuijieMPingCompleted_Type = TruthValue
_RuijieMPingCompleted_Object = MibTableColumn
ruijieMPingCompleted = _RuijieMPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 3, 1, 7),
    _RuijieMPingCompleted_Type()
)
ruijieMPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPingCompleted.setStatus("current")
_RuijieMPingEntryStauts_Type = RowStatus
_RuijieMPingEntryStauts_Object = MibTableColumn
ruijieMPingEntryStauts = _RuijieMPingEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 3, 1, 8),
    _RuijieMPingEntryStauts_Type()
)
ruijieMPingEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieMPingEntryStauts.setStatus("current")
_RuijieIpMRouteTable_Object = MibTable
ruijieIpMRouteTable = _RuijieIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieIpMRouteTable.setStatus("current")
_RuijieIpMRouteEntry_Object = MibTableRow
ruijieIpMRouteEntry = _RuijieIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1)
)
ruijieIpMRouteEntry.setIndexNames(
    (0, "RUIJIE-MULTICAST-MIB", "ruijieIpMRouteGroup"),
    (0, "RUIJIE-MULTICAST-MIB", "ruijieIpMRouteSource"),
    (0, "RUIJIE-MULTICAST-MIB", "ruijieIpMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    ruijieIpMRouteEntry.setStatus("current")
_RuijieIpMRouteGroup_Type = IpAddress
_RuijieIpMRouteGroup_Object = MibTableColumn
ruijieIpMRouteGroup = _RuijieIpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 1),
    _RuijieIpMRouteGroup_Type()
)
ruijieIpMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIpMRouteGroup.setStatus("current")
_RuijieIpMRouteSource_Type = IpAddress
_RuijieIpMRouteSource_Object = MibTableColumn
ruijieIpMRouteSource = _RuijieIpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 2),
    _RuijieIpMRouteSource_Type()
)
ruijieIpMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIpMRouteSource.setStatus("current")
_RuijieIpMRouteSourceMask_Type = IpAddress
_RuijieIpMRouteSourceMask_Object = MibTableColumn
ruijieIpMRouteSourceMask = _RuijieIpMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 3),
    _RuijieIpMRouteSourceMask_Type()
)
ruijieIpMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieIpMRouteSourceMask.setStatus("current")
_RuijieIpMRouteRP_Type = IpAddress
_RuijieIpMRouteRP_Object = MibTableColumn
ruijieIpMRouteRP = _RuijieIpMRouteRP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 4),
    _RuijieIpMRouteRP_Type()
)
ruijieIpMRouteRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteRP.setStatus("current")
_RuijieIpMRoutePruneFlag_Type = TruthValue
_RuijieIpMRoutePruneFlag_Object = MibTableColumn
ruijieIpMRoutePruneFlag = _RuijieIpMRoutePruneFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 5),
    _RuijieIpMRoutePruneFlag_Type()
)
ruijieIpMRoutePruneFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRoutePruneFlag.setStatus("current")
_RuijieIpMRouteSparseFlag_Type = TruthValue
_RuijieIpMRouteSparseFlag_Object = MibTableColumn
ruijieIpMRouteSparseFlag = _RuijieIpMRouteSparseFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 6),
    _RuijieIpMRouteSparseFlag_Type()
)
ruijieIpMRouteSparseFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteSparseFlag.setStatus("current")
_RuijieIpMRouteConnectedFlag_Type = TruthValue
_RuijieIpMRouteConnectedFlag_Object = MibTableColumn
ruijieIpMRouteConnectedFlag = _RuijieIpMRouteConnectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 7),
    _RuijieIpMRouteConnectedFlag_Type()
)
ruijieIpMRouteConnectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteConnectedFlag.setStatus("current")
_RuijieIpMRouteLocalFlag_Type = TruthValue
_RuijieIpMRouteLocalFlag_Object = MibTableColumn
ruijieIpMRouteLocalFlag = _RuijieIpMRouteLocalFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 8),
    _RuijieIpMRouteLocalFlag_Type()
)
ruijieIpMRouteLocalFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteLocalFlag.setStatus("current")
_RuijieIpMRouteRegisterFlag_Type = TruthValue
_RuijieIpMRouteRegisterFlag_Object = MibTableColumn
ruijieIpMRouteRegisterFlag = _RuijieIpMRouteRegisterFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 9),
    _RuijieIpMRouteRegisterFlag_Type()
)
ruijieIpMRouteRegisterFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteRegisterFlag.setStatus("current")
_RuijieIpMRouteRpFlag_Type = TruthValue
_RuijieIpMRouteRpFlag_Object = MibTableColumn
ruijieIpMRouteRpFlag = _RuijieIpMRouteRpFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 10),
    _RuijieIpMRouteRpFlag_Type()
)
ruijieIpMRouteRpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteRpFlag.setStatus("current")
_RuijieIpMRouteSptFlag_Type = TruthValue
_RuijieIpMRouteSptFlag_Object = MibTableColumn
ruijieIpMRouteSptFlag = _RuijieIpMRouteSptFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 11),
    _RuijieIpMRouteSptFlag_Type()
)
ruijieIpMRouteSptFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteSptFlag.setStatus("current")


class _RuijieIpMRouteInLimit_Type(Integer32):
    """Custom type ruijieIpMRouteInLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieIpMRouteInLimit_Type.__name__ = "Integer32"
_RuijieIpMRouteInLimit_Object = MibTableColumn
ruijieIpMRouteInLimit = _RuijieIpMRouteInLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 12),
    _RuijieIpMRouteInLimit_Type()
)
ruijieIpMRouteInLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteInLimit.setStatus("obsolete")
if mibBuilder.loadTexts:
    ruijieIpMRouteInLimit.setUnits("Kbits/second")
_RuijieIpMRouteLifeAvg_Type = Integer32
_RuijieIpMRouteLifeAvg_Object = MibTableColumn
ruijieIpMRouteLifeAvg = _RuijieIpMRouteLifeAvg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 13),
    _RuijieIpMRouteLifeAvg_Type()
)
ruijieIpMRouteLifeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMRouteLifeAvg.setStatus("current")
_RuijieIpMrouteGroupPktsCount_Type = Integer32
_RuijieIpMrouteGroupPktsCount_Object = MibTableColumn
ruijieIpMrouteGroupPktsCount = _RuijieIpMrouteGroupPktsCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 14),
    _RuijieIpMrouteGroupPktsCount_Type()
)
ruijieIpMrouteGroupPktsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMrouteGroupPktsCount.setStatus("current")
_RuijieIpMrouteSouceCount_Type = Integer32
_RuijieIpMrouteSouceCount_Object = MibTableColumn
ruijieIpMrouteSouceCount = _RuijieIpMrouteSouceCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 15),
    _RuijieIpMrouteSouceCount_Type()
)
ruijieIpMrouteSouceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMrouteSouceCount.setStatus("current")
_RuijieIpMrouteRpPkts_Type = Integer32
_RuijieIpMrouteRpPkts_Object = MibTableColumn
ruijieIpMrouteRpPkts = _RuijieIpMrouteRpPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 16),
    _RuijieIpMrouteRpPkts_Type()
)
ruijieIpMrouteRpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMrouteRpPkts.setStatus("current")
_RuijieIpMrouteRpPktsPerSec_Type = Integer32
_RuijieIpMrouteRpPktsPerSec_Object = MibTableColumn
ruijieIpMrouteRpPktsPerSec = _RuijieIpMrouteRpPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 17),
    _RuijieIpMrouteRpPktsPerSec_Type()
)
ruijieIpMrouteRpPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMrouteRpPktsPerSec.setStatus("current")
_RuijieIpMrouteRpAvgPktsSize_Type = Integer32
_RuijieIpMrouteRpAvgPktsSize_Object = MibTableColumn
ruijieIpMrouteRpAvgPktsSize = _RuijieIpMrouteRpAvgPktsSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 18),
    _RuijieIpMrouteRpAvgPktsSize_Type()
)
ruijieIpMrouteRpAvgPktsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMrouteRpAvgPktsSize.setStatus("current")
_RuijieIpMrouteRpKilobitsPerSec_Type = Integer32
_RuijieIpMrouteRpKilobitsPerSec_Object = MibTableColumn
ruijieIpMrouteRpKilobitsPerSec = _RuijieIpMrouteRpKilobitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 19),
    _RuijieIpMrouteRpKilobitsPerSec_Type()
)
ruijieIpMrouteRpKilobitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMrouteRpKilobitsPerSec.setStatus("current")
_RuijieIpMrouteSoucePkts_Type = Integer32
_RuijieIpMrouteSoucePkts_Object = MibTableColumn
ruijieIpMrouteSoucePkts = _RuijieIpMrouteSoucePkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 20),
    _RuijieIpMrouteSoucePkts_Type()
)
ruijieIpMrouteSoucePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMrouteSoucePkts.setStatus("current")
_RuijieIpMrouteSoucePktsPerSec_Type = Integer32
_RuijieIpMrouteSoucePktsPerSec_Object = MibTableColumn
ruijieIpMrouteSoucePktsPerSec = _RuijieIpMrouteSoucePktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 21),
    _RuijieIpMrouteSoucePktsPerSec_Type()
)
ruijieIpMrouteSoucePktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMrouteSoucePktsPerSec.setStatus("current")
_RuijieIpMrouteSouceAvgPktsSize_Type = Integer32
_RuijieIpMrouteSouceAvgPktsSize_Object = MibTableColumn
ruijieIpMrouteSouceAvgPktsSize = _RuijieIpMrouteSouceAvgPktsSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 22),
    _RuijieIpMrouteSouceAvgPktsSize_Type()
)
ruijieIpMrouteSouceAvgPktsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMrouteSouceAvgPktsSize.setStatus("current")
_RuijieIpMrouteSouceKilobitsPerSec_Type = Integer32
_RuijieIpMrouteSouceKilobitsPerSec_Object = MibTableColumn
ruijieIpMrouteSouceKilobitsPerSec = _RuijieIpMrouteSouceKilobitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 4, 1, 23),
    _RuijieIpMrouteSouceKilobitsPerSec_Type()
)
ruijieIpMrouteSouceKilobitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIpMrouteSouceKilobitsPerSec.setStatus("current")
_RuijieMrinfoTable_Object = MibTable
ruijieMrinfoTable = _RuijieMrinfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieMrinfoTable.setStatus("current")
_RuijieMrinfoEntry_Object = MibTableRow
ruijieMrinfoEntry = _RuijieMrinfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 5, 1)
)
ruijieMrinfoEntry.setIndexNames(
    (0, "RUIJIE-MULTICAST-MIB", "ruijieMrinfoIfAddress"),
)
if mibBuilder.loadTexts:
    ruijieMrinfoEntry.setStatus("current")
_RuijieMrinfoIfAddress_Type = IpAddress
_RuijieMrinfoIfAddress_Object = MibTableColumn
ruijieMrinfoIfAddress = _RuijieMrinfoIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 5, 1, 1),
    _RuijieMrinfoIfAddress_Type()
)
ruijieMrinfoIfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieMrinfoIfAddress.setStatus("current")
_RuijieMrinfoNeighbor_Type = IpAddress
_RuijieMrinfoNeighbor_Object = MibTableColumn
ruijieMrinfoNeighbor = _RuijieMrinfoNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 5, 1, 2),
    _RuijieMrinfoNeighbor_Type()
)
ruijieMrinfoNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMrinfoNeighbor.setStatus("current")
_RuijieMrinfoTtlThreshold_Type = Integer32
_RuijieMrinfoTtlThreshold_Object = MibTableColumn
ruijieMrinfoTtlThreshold = _RuijieMrinfoTtlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 5, 1, 3),
    _RuijieMrinfoTtlThreshold_Type()
)
ruijieMrinfoTtlThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMrinfoTtlThreshold.setStatus("current")
_RuijieMrinfoMetricOffset_Type = Integer32
_RuijieMrinfoMetricOffset_Object = MibTableColumn
ruijieMrinfoMetricOffset = _RuijieMrinfoMetricOffset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 5, 1, 4),
    _RuijieMrinfoMetricOffset_Type()
)
ruijieMrinfoMetricOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMrinfoMetricOffset.setStatus("current")
_RuijieMrinfoQuerier_Type = TruthValue
_RuijieMrinfoQuerier_Object = MibTableColumn
ruijieMrinfoQuerier = _RuijieMrinfoQuerier_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 5, 1, 5),
    _RuijieMrinfoQuerier_Type()
)
ruijieMrinfoQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMrinfoQuerier.setStatus("current")
_RuijieMrinfoDown_Type = TruthValue
_RuijieMrinfoDown_Object = MibTableColumn
ruijieMrinfoDown = _RuijieMrinfoDown_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 5, 1, 6),
    _RuijieMrinfoDown_Type()
)
ruijieMrinfoDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMrinfoDown.setStatus("current")
_RuijieMrinfoLeaf_Type = TruthValue
_RuijieMrinfoLeaf_Object = MibTableColumn
ruijieMrinfoLeaf = _RuijieMrinfoLeaf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 5, 1, 7),
    _RuijieMrinfoLeaf_Type()
)
ruijieMrinfoLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMrinfoLeaf.setStatus("current")
_RuijieMultVidTable_Object = MibTable
ruijieMultVidTable = _RuijieMultVidTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieMultVidTable.setStatus("current")
_RuijieMultVidEntry_Object = MibTableRow
ruijieMultVidEntry = _RuijieMultVidEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 6, 1)
)
ruijieMultVidEntry.setIndexNames(
    (0, "RUIJIE-MULTICAST-MIB", "ruijieMultInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieMultVidEntry.setStatus("current")
_RuijieMultInterfaceIfIndex_Type = IfIndex
_RuijieMultInterfaceIfIndex_Object = MibTableColumn
ruijieMultInterfaceIfIndex = _RuijieMultInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 6, 1, 1),
    _RuijieMultInterfaceIfIndex_Type()
)
ruijieMultInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieMultInterfaceIfIndex.setStatus("current")
_RuijieMultVlan_Type = VlanId
_RuijieMultVlan_Object = MibTableColumn
ruijieMultVlan = _RuijieMultVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 1, 6, 1, 2),
    _RuijieMultVlan_Type()
)
ruijieMultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieMultVlan.setStatus("current")
_RuijieMultMIBConformance_ObjectIdentity = ObjectIdentity
ruijieMultMIBConformance = _RuijieMultMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 2)
)
_RuijieMultMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieMultMIBCompliances = _RuijieMultMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 2, 1)
)
_RuijieMultMIBGroups_ObjectIdentity = ObjectIdentity
ruijieMultMIBGroups = _RuijieMultMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 2, 2)
)

# Managed Objects groups

ruijieIpMRouteInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 2, 2, 1)
)
ruijieIpMRouteInterfaceMIBGroup.setObjects(
      *(("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteInterfaceTtl"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteInterfaceProtocol"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteInterfaceRateLimit"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteInterfaceInMcastOctets"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteInterfaceOutMcastOctets"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteInterfaceHCInMcastOctets"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteInterfaceHCOutMcastOctets"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteBoundaryAclName"))
)
if mibBuilder.loadTexts:
    ruijieIpMRouteInterfaceMIBGroup.setStatus("current")

ruijieIpRpfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 2, 2, 2)
)
ruijieIpRpfMIBGroup.setObjects(
      *(("RUIJIE-MULTICAST-MIB", "ruijieIpRpfInterface"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpRpfNeighborAddress"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpRpfRouteAddress"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpRpfRouteMask"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpRpfType"))
)
if mibBuilder.loadTexts:
    ruijieIpRpfMIBGroup.setStatus("current")

ruijieMPingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 2, 2, 3)
)
ruijieMPingMIBGroup.setObjects(
      *(("RUIJIE-MULTICAST-MIB", "ruijieMPingResponseTime"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMPingDataLength"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMPingTimeOuts"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMPingCompleted"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMPingEntryStauts"))
)
if mibBuilder.loadTexts:
    ruijieMPingMIBGroup.setStatus("current")

ruijieIpMRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 2, 2, 4)
)
ruijieIpMRouteMIBGroup.setObjects(
      *(("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteRP"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRoutePruneFlag"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteSparseFlag"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteConnectedFlag"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteLocalFlag"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteRegisterFlag"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteRpFlag"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteSptFlag"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteInLimit"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteLifeAvg"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMrouteGroupPktsCount"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMrouteSouceCount"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMrouteRpPkts"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMrouteRpPktsPerSec"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMrouteRpAvgPktsSize"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMrouteRpKilobitsPerSec"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMrouteSoucePkts"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMrouteSoucePktsPerSec"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMrouteSouceAvgPktsSize"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMrouteSouceKilobitsPerSec"))
)
if mibBuilder.loadTexts:
    ruijieIpMRouteMIBGroup.setStatus("current")

ruijieMrinfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 2, 2, 5)
)
ruijieMrinfoMIBGroup.setObjects(
      *(("RUIJIE-MULTICAST-MIB", "ruijieMrinfoNeighbor"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMrinfoTtlThreshold"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMrinfoMetricOffset"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMrinfoQuerier"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMrinfoDown"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMrinfoLeaf"))
)
if mibBuilder.loadTexts:
    ruijieMrinfoMIBGroup.setStatus("current")

ruijieMultVidMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 2, 2, 6)
)
ruijieMultVidMIBGroup.setObjects(
    ("RUIJIE-MULTICAST-MIB", "ruijieMultVlan")
)
if mibBuilder.loadTexts:
    ruijieMultVidMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieMultMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 28, 2, 1, 1)
)
ruijieMultMIBCompliance.setObjects(
      *(("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteInterfaceMIBGroup"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpRpfMIBGroup"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMPingMIBGroup"),
        ("RUIJIE-MULTICAST-MIB", "ruijieIpMRouteMIBGroup"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMrinfoMIBGroup"),
        ("RUIJIE-MULTICAST-MIB", "ruijieMultVidMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieMultMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MULTICAST-MIB",
    **{"ruijieMultMIB": ruijieMultMIB,
       "ruijieMultMIBObjects": ruijieMultMIBObjects,
       "ruijieIpMRouteInterfaceTable": ruijieIpMRouteInterfaceTable,
       "ruijieIpMRouteInterfaceEntry": ruijieIpMRouteInterfaceEntry,
       "ruijieIpMRouteInterfaceIfIndex": ruijieIpMRouteInterfaceIfIndex,
       "ruijieIpMRouteInterfaceTtl": ruijieIpMRouteInterfaceTtl,
       "ruijieIpMRouteInterfaceProtocol": ruijieIpMRouteInterfaceProtocol,
       "ruijieIpMRouteInterfaceRateLimit": ruijieIpMRouteInterfaceRateLimit,
       "ruijieIpMRouteInterfaceInMcastOctets": ruijieIpMRouteInterfaceInMcastOctets,
       "ruijieIpMRouteInterfaceOutMcastOctets": ruijieIpMRouteInterfaceOutMcastOctets,
       "ruijieIpMRouteInterfaceHCInMcastOctets": ruijieIpMRouteInterfaceHCInMcastOctets,
       "ruijieIpMRouteInterfaceHCOutMcastOctets": ruijieIpMRouteInterfaceHCOutMcastOctets,
       "ruijieIpMRouteBoundaryAclName": ruijieIpMRouteBoundaryAclName,
       "ruijieIpRpfTable": ruijieIpRpfTable,
       "ruijieIpRpfEntry": ruijieIpRpfEntry,
       "ruijieIpRpfSourceAddress": ruijieIpRpfSourceAddress,
       "ruijieIpRpfInterface": ruijieIpRpfInterface,
       "ruijieIpRpfNeighborAddress": ruijieIpRpfNeighborAddress,
       "ruijieIpRpfRouteAddress": ruijieIpRpfRouteAddress,
       "ruijieIpRpfRouteMask": ruijieIpRpfRouteMask,
       "ruijieIpRpfType": ruijieIpRpfType,
       "ruijieMPingTable": ruijieMPingTable,
       "ruijieMPingEntry": ruijieMPingEntry,
       "ruijieMPingIndex": ruijieMPingIndex,
       "ruijieMPingGroupAddress": ruijieMPingGroupAddress,
       "ruijieMPingGroupMember": ruijieMPingGroupMember,
       "ruijieMPingResponseTime": ruijieMPingResponseTime,
       "ruijieMPingDataLength": ruijieMPingDataLength,
       "ruijieMPingTimeOuts": ruijieMPingTimeOuts,
       "ruijieMPingCompleted": ruijieMPingCompleted,
       "ruijieMPingEntryStauts": ruijieMPingEntryStauts,
       "ruijieIpMRouteTable": ruijieIpMRouteTable,
       "ruijieIpMRouteEntry": ruijieIpMRouteEntry,
       "ruijieIpMRouteGroup": ruijieIpMRouteGroup,
       "ruijieIpMRouteSource": ruijieIpMRouteSource,
       "ruijieIpMRouteSourceMask": ruijieIpMRouteSourceMask,
       "ruijieIpMRouteRP": ruijieIpMRouteRP,
       "ruijieIpMRoutePruneFlag": ruijieIpMRoutePruneFlag,
       "ruijieIpMRouteSparseFlag": ruijieIpMRouteSparseFlag,
       "ruijieIpMRouteConnectedFlag": ruijieIpMRouteConnectedFlag,
       "ruijieIpMRouteLocalFlag": ruijieIpMRouteLocalFlag,
       "ruijieIpMRouteRegisterFlag": ruijieIpMRouteRegisterFlag,
       "ruijieIpMRouteRpFlag": ruijieIpMRouteRpFlag,
       "ruijieIpMRouteSptFlag": ruijieIpMRouteSptFlag,
       "ruijieIpMRouteInLimit": ruijieIpMRouteInLimit,
       "ruijieIpMRouteLifeAvg": ruijieIpMRouteLifeAvg,
       "ruijieIpMrouteGroupPktsCount": ruijieIpMrouteGroupPktsCount,
       "ruijieIpMrouteSouceCount": ruijieIpMrouteSouceCount,
       "ruijieIpMrouteRpPkts": ruijieIpMrouteRpPkts,
       "ruijieIpMrouteRpPktsPerSec": ruijieIpMrouteRpPktsPerSec,
       "ruijieIpMrouteRpAvgPktsSize": ruijieIpMrouteRpAvgPktsSize,
       "ruijieIpMrouteRpKilobitsPerSec": ruijieIpMrouteRpKilobitsPerSec,
       "ruijieIpMrouteSoucePkts": ruijieIpMrouteSoucePkts,
       "ruijieIpMrouteSoucePktsPerSec": ruijieIpMrouteSoucePktsPerSec,
       "ruijieIpMrouteSouceAvgPktsSize": ruijieIpMrouteSouceAvgPktsSize,
       "ruijieIpMrouteSouceKilobitsPerSec": ruijieIpMrouteSouceKilobitsPerSec,
       "ruijieMrinfoTable": ruijieMrinfoTable,
       "ruijieMrinfoEntry": ruijieMrinfoEntry,
       "ruijieMrinfoIfAddress": ruijieMrinfoIfAddress,
       "ruijieMrinfoNeighbor": ruijieMrinfoNeighbor,
       "ruijieMrinfoTtlThreshold": ruijieMrinfoTtlThreshold,
       "ruijieMrinfoMetricOffset": ruijieMrinfoMetricOffset,
       "ruijieMrinfoQuerier": ruijieMrinfoQuerier,
       "ruijieMrinfoDown": ruijieMrinfoDown,
       "ruijieMrinfoLeaf": ruijieMrinfoLeaf,
       "ruijieMultVidTable": ruijieMultVidTable,
       "ruijieMultVidEntry": ruijieMultVidEntry,
       "ruijieMultInterfaceIfIndex": ruijieMultInterfaceIfIndex,
       "ruijieMultVlan": ruijieMultVlan,
       "ruijieMultMIBConformance": ruijieMultMIBConformance,
       "ruijieMultMIBCompliances": ruijieMultMIBCompliances,
       "ruijieMultMIBCompliance": ruijieMultMIBCompliance,
       "ruijieMultMIBGroups": ruijieMultMIBGroups,
       "ruijieIpMRouteInterfaceMIBGroup": ruijieIpMRouteInterfaceMIBGroup,
       "ruijieIpRpfMIBGroup": ruijieIpRpfMIBGroup,
       "ruijieMPingMIBGroup": ruijieMPingMIBGroup,
       "ruijieIpMRouteMIBGroup": ruijieIpMRouteMIBGroup,
       "ruijieMrinfoMIBGroup": ruijieMrinfoMIBGroup,
       "ruijieMultVidMIBGroup": ruijieMultVidMIBGroup}
)
