# SNMP MIB module (RUIJIE-IP-SET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-IP-SET-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:17 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieIPSetMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111)
)
if mibBuilder.loadTexts:
    ruijieIPSetMgmt.setRevisions(
        ("2012-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieIPSetMIBObjects_ObjectIdentity = ObjectIdentity
ruijieIPSetMIBObjects = _RuijieIPSetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 1)
)
_RuijieIPSetipAddressTable_Object = MibTable
ruijieIPSetipAddressTable = _RuijieIPSetipAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieIPSetipAddressTable.setStatus("current")
_RuijieIPSetIpAddressEntry_Object = MibTableRow
ruijieIPSetIpAddressEntry = _RuijieIPSetIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 1, 1, 1)
)
ruijieIPSetIpAddressEntry.setIndexNames(
    (0, "RUIJIE-IP-SET-MIB", "ruijieIPSetipAddressIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIPSetIpAddressEntry.setStatus("current")
_RuijieIPSetipAddressIfIndex_Type = InterfaceIndex
_RuijieIPSetipAddressIfIndex_Object = MibTableColumn
ruijieIPSetipAddressIfIndex = _RuijieIPSetipAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 1, 1, 1, 1),
    _RuijieIPSetipAddressIfIndex_Type()
)
ruijieIPSetipAddressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIPSetipAddressIfIndex.setStatus("current")
_RuijieIPSetipAddressAddr_Type = IpAddress
_RuijieIPSetipAddressAddr_Object = MibTableColumn
ruijieIPSetipAddressAddr = _RuijieIPSetipAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 1, 1, 1, 2),
    _RuijieIPSetipAddressAddr_Type()
)
ruijieIPSetipAddressAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIPSetipAddressAddr.setStatus("current")
_RuijieIPSetipAddressMask_Type = IpAddress
_RuijieIPSetipAddressMask_Object = MibTableColumn
ruijieIPSetipAddressMask = _RuijieIPSetipAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 1, 1, 1, 3),
    _RuijieIPSetipAddressMask_Type()
)
ruijieIPSetipAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIPSetipAddressMask.setStatus("current")


class _RuijieIPSetipAddressStatus_Type(Integer32):
    """Custom type ruijieIPSetipAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 0),
          ("add", 1))
    )


_RuijieIPSetipAddressStatus_Type.__name__ = "Integer32"
_RuijieIPSetipAddressStatus_Object = MibTableColumn
ruijieIPSetipAddressStatus = _RuijieIPSetipAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 1, 1, 1, 4),
    _RuijieIPSetipAddressStatus_Type()
)
ruijieIPSetipAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIPSetipAddressStatus.setStatus("current")


class _RuijieIPSetipAddressType_Type(Integer32):
    """Custom type ruijieIPSetipAddressType based on Integer32"""
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
        *(("unicast", 1),
          ("anycast", 2),
          ("broadcast", 3))
    )


_RuijieIPSetipAddressType_Type.__name__ = "Integer32"
_RuijieIPSetipAddressType_Object = MibTableColumn
ruijieIPSetipAddressType = _RuijieIPSetipAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 1, 1, 1, 5),
    _RuijieIPSetipAddressType_Type()
)
ruijieIPSetipAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieIPSetipAddressType.setStatus("current")
_RuijieIpSetMIBConformance_ObjectIdentity = ObjectIdentity
ruijieIpSetMIBConformance = _RuijieIpSetMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 2)
)
_RuijieIpSetMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieIpSetMIBCompliances = _RuijieIpSetMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 2, 1)
)
_RuijieIpSetMIBGroups_ObjectIdentity = ObjectIdentity
ruijieIpSetMIBGroups = _RuijieIpSetMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 2, 2)
)

# Managed Objects groups

ruijieIpSetMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 2, 2, 1)
)
ruijieIpSetMIBGroup.setObjects(
      *(("RUIJIE-IP-SET-MIB", "ruijieIPSetipAddressIfIndex"),
        ("RUIJIE-IP-SET-MIB", "ruijieIPSetipAddressAddr"),
        ("RUIJIE-IP-SET-MIB", "ruijieIPSetipAddressMask"),
        ("RUIJIE-IP-SET-MIB", "ruijieIPSetipAddressStatus"),
        ("RUIJIE-IP-SET-MIB", "ruijieIPSetipAddressType"))
)
if mibBuilder.loadTexts:
    ruijieIpSetMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieIcmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 111, 2, 1, 1)
)
ruijieIcmpMIBCompliance.setObjects(
    ("RUIJIE-IP-SET-MIB", "ruijieIpSetMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieIcmpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-IP-SET-MIB",
    **{"ruijieIPSetMgmt": ruijieIPSetMgmt,
       "ruijieIPSetMIBObjects": ruijieIPSetMIBObjects,
       "ruijieIPSetipAddressTable": ruijieIPSetipAddressTable,
       "ruijieIPSetIpAddressEntry": ruijieIPSetIpAddressEntry,
       "ruijieIPSetipAddressIfIndex": ruijieIPSetipAddressIfIndex,
       "ruijieIPSetipAddressAddr": ruijieIPSetipAddressAddr,
       "ruijieIPSetipAddressMask": ruijieIPSetipAddressMask,
       "ruijieIPSetipAddressStatus": ruijieIPSetipAddressStatus,
       "ruijieIPSetipAddressType": ruijieIPSetipAddressType,
       "ruijieIpSetMIBConformance": ruijieIpSetMIBConformance,
       "ruijieIpSetMIBCompliances": ruijieIpSetMIBCompliances,
       "ruijieIcmpMIBCompliance": ruijieIcmpMIBCompliance,
       "ruijieIpSetMIBGroups": ruijieIpSetMIBGroups,
       "ruijieIpSetMIBGroup": ruijieIpSetMIBGroup}
)
