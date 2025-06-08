# SNMP MIB module (A3COM-HUAWEI-LB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-LB-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:04:06 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cLB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116)
)
if mibBuilder.loadTexts:
    h3cLB.setRevisions(
        ("2010-12-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cLBTables_ObjectIdentity = ObjectIdentity
h3cLBTables = _H3cLBTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 1)
)
_H3cLBRealServerGroupTable_Object = MibTable
h3cLBRealServerGroupTable = _H3cLBRealServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 1, 1)
)
if mibBuilder.loadTexts:
    h3cLBRealServerGroupTable.setStatus("current")
_H3cLBRealServerGroupEntry_Object = MibTableRow
h3cLBRealServerGroupEntry = _H3cLBRealServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 1, 1, 1)
)
h3cLBRealServerGroupEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LB-MIB", "h3cLBRealServerGroupName"),
)
if mibBuilder.loadTexts:
    h3cLBRealServerGroupEntry.setStatus("current")


class _H3cLBRealServerGroupName_Type(DisplayString):
    """Custom type h3cLBRealServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cLBRealServerGroupName_Type.__name__ = "DisplayString"
_H3cLBRealServerGroupName_Object = MibTableColumn
h3cLBRealServerGroupName = _H3cLBRealServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 1, 1, 1, 1),
    _H3cLBRealServerGroupName_Type()
)
h3cLBRealServerGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBRealServerGroupName.setStatus("current")
_H3cLBRealServerTable_Object = MibTable
h3cLBRealServerTable = _H3cLBRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 1, 2)
)
if mibBuilder.loadTexts:
    h3cLBRealServerTable.setStatus("current")
_H3cLBRealServerEntry_Object = MibTableRow
h3cLBRealServerEntry = _H3cLBRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 1, 2, 1)
)
h3cLBRealServerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LB-MIB", "h3cLBRealServerGroupName"),
    (0, "A3COM-HUAWEI-LB-MIB", "h3cLBRealServerName"),
)
if mibBuilder.loadTexts:
    h3cLBRealServerEntry.setStatus("current")


class _H3cLBRealServerName_Type(DisplayString):
    """Custom type h3cLBRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cLBRealServerName_Type.__name__ = "DisplayString"
_H3cLBRealServerName_Object = MibTableColumn
h3cLBRealServerName = _H3cLBRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 1, 2, 1, 1),
    _H3cLBRealServerName_Type()
)
h3cLBRealServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBRealServerName.setStatus("current")


class _H3cLBRealServerStatus_Type(Integer32):
    """Custom type h3cLBRealServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("slowdown", 3))
    )


_H3cLBRealServerStatus_Type.__name__ = "Integer32"
_H3cLBRealServerStatus_Object = MibTableColumn
h3cLBRealServerStatus = _H3cLBRealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 1, 2, 1, 2),
    _H3cLBRealServerStatus_Type()
)
h3cLBRealServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLBRealServerStatus.setStatus("current")
_H3cLBRealServerConnectNumber_Type = Integer32
_H3cLBRealServerConnectNumber_Object = MibTableColumn
h3cLBRealServerConnectNumber = _H3cLBRealServerConnectNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 1, 2, 1, 3),
    _H3cLBRealServerConnectNumber_Type()
)
h3cLBRealServerConnectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBRealServerConnectNumber.setStatus("current")
_H3cLBTrap_ObjectIdentity = ObjectIdentity
h3cLBTrap = _H3cLBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 2)
)
_H3cLBTrapPrex_ObjectIdentity = ObjectIdentity
h3cLBTrapPrex = _H3cLBTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cLBRealServerOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 116, 2, 0, 1)
)
h3cLBRealServerOverLoad.setObjects(
      *(("A3COM-HUAWEI-LB-MIB", "h3cLBRealServerGroupName"),
        ("A3COM-HUAWEI-LB-MIB", "h3cLBRealServerName"),
        ("A3COM-HUAWEI-LB-MIB", "h3cLBRealServerConnectNumber"))
)
if mibBuilder.loadTexts:
    h3cLBRealServerOverLoad.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LB-MIB",
    **{"h3cLB": h3cLB,
       "h3cLBTables": h3cLBTables,
       "h3cLBRealServerGroupTable": h3cLBRealServerGroupTable,
       "h3cLBRealServerGroupEntry": h3cLBRealServerGroupEntry,
       "h3cLBRealServerGroupName": h3cLBRealServerGroupName,
       "h3cLBRealServerTable": h3cLBRealServerTable,
       "h3cLBRealServerEntry": h3cLBRealServerEntry,
       "h3cLBRealServerName": h3cLBRealServerName,
       "h3cLBRealServerStatus": h3cLBRealServerStatus,
       "h3cLBRealServerConnectNumber": h3cLBRealServerConnectNumber,
       "h3cLBTrap": h3cLBTrap,
       "h3cLBTrapPrex": h3cLBTrapPrex,
       "h3cLBRealServerOverLoad": h3cLBRealServerOverLoad}
)
