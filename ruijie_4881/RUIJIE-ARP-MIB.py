# SNMP MIB module (RUIJIE-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ARP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:23 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieArpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieArpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieArpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieArpMIBObjects = _RuijieArpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1)
)
_RuijieArpTable_Object = MibTable
ruijieArpTable = _RuijieArpTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieArpTable.setStatus("current")
_RuijieArpEntry_Object = MibTableRow
ruijieArpEntry = _RuijieArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 1, 1)
)
ruijieArpEntry.setIndexNames(
    (0, "RUIJIE-ARP-MIB", "ruijieArpIfIndex"),
    (0, "RUIJIE-ARP-MIB", "ruijieArpNetAddress"),
)
if mibBuilder.loadTexts:
    ruijieArpEntry.setStatus("current")
_RuijieArpIfIndex_Type = IfIndex
_RuijieArpIfIndex_Object = MibTableColumn
ruijieArpIfIndex = _RuijieArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 1, 1, 1),
    _RuijieArpIfIndex_Type()
)
ruijieArpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieArpIfIndex.setStatus("current")
_RuijieArpPhysAddress_Type = PhysAddress
_RuijieArpPhysAddress_Object = MibTableColumn
ruijieArpPhysAddress = _RuijieArpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 1, 1, 2),
    _RuijieArpPhysAddress_Type()
)
ruijieArpPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieArpPhysAddress.setStatus("current")
_RuijieArpNetAddress_Type = IpAddress
_RuijieArpNetAddress_Object = MibTableColumn
ruijieArpNetAddress = _RuijieArpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 1, 1, 3),
    _RuijieArpNetAddress_Type()
)
ruijieArpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieArpNetAddress.setStatus("current")
_RuijieArpRemainAge_Type = Integer32
_RuijieArpRemainAge_Object = MibTableColumn
ruijieArpRemainAge = _RuijieArpRemainAge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 1, 1, 4),
    _RuijieArpRemainAge_Type()
)
ruijieArpRemainAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieArpRemainAge.setStatus("current")


class _RuijieArpType_Type(Integer32):
    """Custom type ruijieArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("arpa", 1)
    )


_RuijieArpType_Type.__name__ = "Integer32"
_RuijieArpType_Object = MibTableColumn
ruijieArpType = _RuijieArpType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 1, 1, 5),
    _RuijieArpType_Type()
)
ruijieArpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieArpType.setStatus("current")


class _RuijieArpEntryType_Type(Integer32):
    """Custom type ruijieArpEntryType based on Integer32"""
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
        *(("static", 1),
          ("dynamic", 2),
          ("interface", 3),
          ("vrrp", 4),
          ("trusted", 5))
    )


_RuijieArpEntryType_Type.__name__ = "Integer32"
_RuijieArpEntryType_Object = MibTableColumn
ruijieArpEntryType = _RuijieArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 1, 1, 6),
    _RuijieArpEntryType_Type()
)
ruijieArpEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieArpEntryType.setStatus("current")
_RuijieArpStatus_Type = RowStatus
_RuijieArpStatus_Object = MibTableColumn
ruijieArpStatus = _RuijieArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 1, 1, 7),
    _RuijieArpStatus_Type()
)
ruijieArpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieArpStatus.setStatus("current")
_RuijieArpIfTable_Object = MibTable
ruijieArpIfTable = _RuijieArpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieArpIfTable.setStatus("current")
_RuijieArpIfEntry_Object = MibTableRow
ruijieArpIfEntry = _RuijieArpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 2, 1)
)
ruijieArpIfEntry.setIndexNames(
    (0, "RUIJIE-ARP-MIB", "ruijieArpIfIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieArpIfEntry.setStatus("current")
_RuijieArpIfIfIndex_Type = IfIndex
_RuijieArpIfIfIndex_Object = MibTableColumn
ruijieArpIfIfIndex = _RuijieArpIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 2, 1, 1),
    _RuijieArpIfIfIndex_Type()
)
ruijieArpIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieArpIfIfIndex.setStatus("current")


class _RuijieArpIfCacheTimeOut_Type(Integer32):
    """Custom type ruijieArpIfCacheTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 18000),
    )


_RuijieArpIfCacheTimeOut_Type.__name__ = "Integer32"
_RuijieArpIfCacheTimeOut_Object = MibTableColumn
ruijieArpIfCacheTimeOut = _RuijieArpIfCacheTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 2, 1, 2),
    _RuijieArpIfCacheTimeOut_Type()
)
ruijieArpIfCacheTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieArpIfCacheTimeOut.setStatus("current")
_RuijieArpCurrentTotalNumber_Type = Counter32
_RuijieArpCurrentTotalNumber_Object = MibScalar
ruijieArpCurrentTotalNumber = _RuijieArpCurrentTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 3),
    _RuijieArpCurrentTotalNumber_Type()
)
ruijieArpCurrentTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieArpCurrentTotalNumber.setStatus("current")
_RuijieArpCurrentUnresolveNumber_Type = Counter32
_RuijieArpCurrentUnresolveNumber_Object = MibScalar
ruijieArpCurrentUnresolveNumber = _RuijieArpCurrentUnresolveNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 1, 4),
    _RuijieArpCurrentUnresolveNumber_Type()
)
ruijieArpCurrentUnresolveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieArpCurrentUnresolveNumber.setStatus("current")
_RuijieArpMIBConformance_ObjectIdentity = ObjectIdentity
ruijieArpMIBConformance = _RuijieArpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 2)
)
_RuijieArpMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieArpMIBCompliances = _RuijieArpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 2, 1)
)
_RuijieArpMIBGroups_ObjectIdentity = ObjectIdentity
ruijieArpMIBGroups = _RuijieArpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 2, 2)
)

# Managed Objects groups

ruijieArpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 2, 2, 1)
)
ruijieArpMIBGroup.setObjects(
      *(("RUIJIE-ARP-MIB", "ruijieArpIfIndex"),
        ("RUIJIE-ARP-MIB", "ruijieArpPhysAddress"),
        ("RUIJIE-ARP-MIB", "ruijieArpNetAddress"),
        ("RUIJIE-ARP-MIB", "ruijieArpRemainAge"),
        ("RUIJIE-ARP-MIB", "ruijieArpType"),
        ("RUIJIE-ARP-MIB", "ruijieArpEntryType"),
        ("RUIJIE-ARP-MIB", "ruijieArpStatus"),
        ("RUIJIE-ARP-MIB", "ruijieArpIfIfIndex"),
        ("RUIJIE-ARP-MIB", "ruijieArpIfCacheTimeOut"),
        ("RUIJIE-ARP-MIB", "ruijieArpCurrentTotalNumber"),
        ("RUIJIE-ARP-MIB", "ruijieArpCurrentUnresolveNumber"))
)
if mibBuilder.loadTexts:
    ruijieArpMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieArpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 2, 2, 1, 1)
)
ruijieArpMIBCompliance.setObjects(
    ("RUIJIE-ARP-MIB", "ruijieArpMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieArpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ARP-MIB",
    **{"ruijieArpMIB": ruijieArpMIB,
       "ruijieArpMIBObjects": ruijieArpMIBObjects,
       "ruijieArpTable": ruijieArpTable,
       "ruijieArpEntry": ruijieArpEntry,
       "ruijieArpIfIndex": ruijieArpIfIndex,
       "ruijieArpPhysAddress": ruijieArpPhysAddress,
       "ruijieArpNetAddress": ruijieArpNetAddress,
       "ruijieArpRemainAge": ruijieArpRemainAge,
       "ruijieArpType": ruijieArpType,
       "ruijieArpEntryType": ruijieArpEntryType,
       "ruijieArpStatus": ruijieArpStatus,
       "ruijieArpIfTable": ruijieArpIfTable,
       "ruijieArpIfEntry": ruijieArpIfEntry,
       "ruijieArpIfIfIndex": ruijieArpIfIfIndex,
       "ruijieArpIfCacheTimeOut": ruijieArpIfCacheTimeOut,
       "ruijieArpCurrentTotalNumber": ruijieArpCurrentTotalNumber,
       "ruijieArpCurrentUnresolveNumber": ruijieArpCurrentUnresolveNumber,
       "ruijieArpMIBConformance": ruijieArpMIBConformance,
       "ruijieArpMIBCompliances": ruijieArpMIBCompliances,
       "ruijieArpMIBCompliance": ruijieArpMIBCompliance,
       "ruijieArpMIBGroups": ruijieArpMIBGroups,
       "ruijieArpMIBGroup": ruijieArpMIBGroup}
)
