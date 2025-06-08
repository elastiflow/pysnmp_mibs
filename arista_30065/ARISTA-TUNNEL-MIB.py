# SNMP MIB module (ARISTA-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-TUNNEL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

aristaTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34)
)
if mibBuilder.loadTexts:
    aristaTunnelMIB.setRevisions(
        ("2023-09-20 00:00",
         "2022-08-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AristaIpsecTunnelConnectionState(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("connecting", 1),
          ("idle", 2),
          ("established", 3),
          ("shut", 4),
          ("fipsUnsupported", 5),
          ("connected", 6),
          ("ikeVersionUnsupportedWithVrf", 7))
    )



# MIB Managed Objects in the order of their OIDs

_AristaTunnelMibNotifications_ObjectIdentity = ObjectIdentity
aristaTunnelMibNotifications = _AristaTunnelMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34, 0)
)
_AristaTunnelMibObjects_ObjectIdentity = ObjectIdentity
aristaTunnelMibObjects = _AristaTunnelMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34, 1)
)
_AristaIpsecTunnelIfTable_Object = MibTable
aristaIpsecTunnelIfTable = _AristaIpsecTunnelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34, 1, 1)
)
if mibBuilder.loadTexts:
    aristaIpsecTunnelIfTable.setStatus("current")
_AristaIpsecTunnelIfEntry_Object = MibTableRow
aristaIpsecTunnelIfEntry = _AristaIpsecTunnelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34, 1, 1, 1)
)
aristaIpsecTunnelIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aristaIpsecTunnelIfEntry.setStatus("current")
_AristaIpsecTunnelIfConnState_Type = AristaIpsecTunnelConnectionState
_AristaIpsecTunnelIfConnState_Object = MibTableColumn
aristaIpsecTunnelIfConnState = _AristaIpsecTunnelIfConnState_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34, 1, 1, 1, 1),
    _AristaIpsecTunnelIfConnState_Type()
)
aristaIpsecTunnelIfConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaIpsecTunnelIfConnState.setStatus("current")
_AristaTunnelMibConformance_ObjectIdentity = ObjectIdentity
aristaTunnelMibConformance = _AristaTunnelMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34, 2)
)
_AristaTunnelMibCompliances_ObjectIdentity = ObjectIdentity
aristaTunnelMibCompliances = _AristaTunnelMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34, 2, 1)
)
_AristaTunnelMibGroups_ObjectIdentity = ObjectIdentity
aristaTunnelMibGroups = _AristaTunnelMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34, 2, 2)
)

# Managed Objects groups

aristaTunnelMibIpsecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34, 2, 2, 1)
)
aristaTunnelMibIpsecGroup.setObjects(
    ("ARISTA-TUNNEL-MIB", "aristaIpsecTunnelIfConnState")
)
if mibBuilder.loadTexts:
    aristaTunnelMibIpsecGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaTunnelMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 34, 2, 1, 1)
)
aristaTunnelMibCompliance.setObjects(
    ("ARISTA-TUNNEL-MIB", "aristaTunnelMibIpsecGroup")
)
if mibBuilder.loadTexts:
    aristaTunnelMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-TUNNEL-MIB",
    **{"AristaIpsecTunnelConnectionState": AristaIpsecTunnelConnectionState,
       "aristaTunnelMIB": aristaTunnelMIB,
       "aristaTunnelMibNotifications": aristaTunnelMibNotifications,
       "aristaTunnelMibObjects": aristaTunnelMibObjects,
       "aristaIpsecTunnelIfTable": aristaIpsecTunnelIfTable,
       "aristaIpsecTunnelIfEntry": aristaIpsecTunnelIfEntry,
       "aristaIpsecTunnelIfConnState": aristaIpsecTunnelIfConnState,
       "aristaTunnelMibConformance": aristaTunnelMibConformance,
       "aristaTunnelMibCompliances": aristaTunnelMibCompliances,
       "aristaTunnelMibCompliance": aristaTunnelMibCompliance,
       "aristaTunnelMibGroups": aristaTunnelMibGroups,
       "aristaTunnelMibIpsecGroup": aristaTunnelMibIpsecGroup}
)
